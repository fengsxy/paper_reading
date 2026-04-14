#!/usr/bin/env python3
"""
Constraint Satisfaction Timeline Analysis.
Run on existing traces to see if H vs S constraints separate temporally.
"""
import json
import re
from pathlib import Path

# Simple regex-based constraint checker (no LLM needed)
class ConstraintChecker:
    def __init__(self, query):
        self.query = query.lower()
        self.constraints = self._extract_constraints()
    
    def _extract_constraints(self):
        c = {}
        q = self.query
        
        # Hard: budget
        budget_match = re.search(r'budget.*?(\d+)\s*yuan|budget.*?(¥|￥)(\d+)', q)
        if not budget_match:
            budget_match = re.search(r'within\s*(\d+)\s*yuan', q)
        if budget_match:
            c['H_budget'] = int(budget_match.group(1) or budget_match.group(3))
        
        # Hard: travelers
        travelers_match = re.search(r'(\d+)\s*(of\s*us|people|person|travelers)', q)
        if travelers_match:
            c['H_travelers'] = int(travelers_match.group(1))
        
        # Hard: transport mode
        if 'train' in q and 'take the train' in q:
            c['H_transport'] = 'train'
        elif 'flight' in q or 'fly' in q:
            c['H_transport'] = 'flight'
        
        # Hard: days
        day_match = re.search(r'(\d+)[-\s]day', q)
        if day_match:
            c['H_days'] = int(day_match.group(1))
        
        # Soft: hotel star
        star_match = re.search(r'(\d)[-\s]star|(\d)[\u661f\u3000]', q)
        if star_match:
            c['S_hotel_star'] = int(star_match.group(1) or star_match.group(2))
        elif 'four-star' in q or '4-star' in q:
            c['S_hotel_star'] = 4
        elif 'three-star' in q or '3-star' in q:
            c['S_hotel_star'] = 3
        
        # Soft: amenities
        if 'pool' in q:
            c['S_pool'] = True
        if 'robot' in q:
            c['S_robot'] = True
        
        # Soft: specific places
        if 'deji plaza' in q:
            c['S_attraction_deji'] = True
        if 'city wall' in q:
            c['S_attraction_wall'] = True
        if 'yinhu' in q:
            c['S_restaurant_yinhu'] = True
        if 'laomendong' in q or 'lao men dong' in q:
            c['S_restaurant_lm'] = True
        if 'birthday' in q:
            c['S_birthday'] = True
        if 'art exhibition' in q:
            c['S_art'] = True
        
        # Soft: hotel chain
        if 'orange hotel' in q:
            c['S_orange'] = True
        
        # Soft: first class
        if 'first class' in q:
            c['S_first_class'] = True
        
        return c
    
    def evaluate(self, plan_text):
        """Return dict of constraint -> True/False/None"""
        if not plan_text:
            return {k: None for k in self.constraints}
        
        plan = plan_text.lower()
        result = {}
        
        for k, v in self.constraints.items():
            if k == 'H_budget':
                costs = re.findall(r'¥(\d+)', plan)
                total = sum(int(c) for c in costs) if costs else 0
                result[k] = (total > 0 and total <= v)
            elif k == 'H_travelers':
                rooms = re.findall(r'(\d+)\s*room', plan)
                # assume 2 per room
                room_count = sum(int(r) for r in rooms) if rooms else 1
                result[k] = (room_count >= (v + 1) // 2)
            elif k == 'H_transport':
                if v == 'train':
                    result[k] = 'train' in plan or 'g' in plan  # G-trains
                elif v == 'flight':
                    result[k] = 'flight' in plan or any(f in plan for f in ['mf', 'fu', 'cz'])
            elif k == 'S_hotel_star':
                stars = re.findall(r'(\d)[\u661f\*]', plan)
                result[k] = any(int(s) >= v for s in stars) if stars else None
            elif k == 'S_pool':
                result[k] = 'pool' in plan
            elif k == 'S_robot':
                result[k] = 'robot' in plan
            elif k == 'S_birthday':
                result[k] = 'birthday' in plan
            elif k == 'S_art':
                result[k] = 'art' in plan
            elif k == 'S_first_class':
                result[k] = 'first' in plan and 'class' in plan
            elif k == 'S_orange':
                result[k] = 'orange' in plan
            elif k == 'S_attraction_deji':
                result[k] = 'deji' in plan
            elif k == 'S_attraction_wall':
                result[k] = 'city wall' in plan or 'taicheng' in plan
            elif k == 'S_restaurant_yinhu':
                result[k] = 'yinhu' in plan or 'qiushan' in plan
            elif k == 'S_restaurant_lm':
                result[k] = 'laomen' in plan or 'lao men' in plan
            else:
                result[k] = None
        
        return result


def analyze_trajectory(traj_file, query):
    """Analyze constraint satisfaction at each tool call."""
    with open(traj_file) as f:
        data = json.load(f)
    
    msgs = data.get('messages', [])
    
    checker = ConstraintChecker(query)
    
    h_scores = []  # hard constraint satisfaction over time
    s_scores = []  # soft constraint satisfaction over time
    
    for i, msg in enumerate(msgs):
        if not isinstance(msg, dict):
            continue
        
        # Extract partial plan from all assistant messages up to this point
        partial_plan = ""
        tool_count = 0
        for m in msgs[:i+1]:
            if isinstance(m, dict):
                if m.get('role') == 'assistant':
                    partial_plan += m.get('content', '') or ''
                elif m.get('role') == 'tool':
                    tool_count += 1
                    partial_plan += "\n" + (m.get('content', '') or '')
        
        if tool_count == 0:  # Need at least one tool result
            continue
        
        result = checker.evaluate(partial_plan)
        
        # Compute H and S scores
        h_keys = [k for k in result if k.startswith('H')]
        s_keys = [k for k in result if k.startswith('S')]
        
        h_sat = sum(1 for k in h_keys if result[k] == True)
        h_total = sum(1 for k in h_keys if result[k] is not None)
        s_sat = sum(1 for k in s_keys if result[k] == True)
        s_total = sum(1 for k in s_keys if result[k] is not None)
        
        h_scores.append((tool_count, h_sat / h_total if h_total > 0 else 0, h_sat, h_total))
        s_scores.append((tool_count, s_sat / s_total if s_total > 0 else 0, s_sat, s_total))
    
    return h_scores, s_scores, checker.constraints


def main():
    queries = {
        'id_0': "I'm planning a two-day trip from Hefei to Nanjing on November 12, 2025, returning in the evening of the 13th. The total budget for this trip should be within 3000 yuan. There are three of us traveling, and we'll take the train. I want a three-star hotel with a swimming pool, and please book two rooms. Must visit 'Nanjing Deji Plaza' and 'Nanjing City Wall Taicheng Scenic Area'. Also, have a meal near 'Laomendong' with a birthday set menu.",
        'id_30': "3-day trip Fuzhou to Hangzhou, Nov 12-14. Train departing 6AM-10AM. 4-star hotel with robot room service, 3 travelers, 2 rooms. Top 3 highest-rated attractions. Must dine at 'Yinhu Restaurant - Qiushan Branch'.",
        'id_59': "4-day trip Urumqi to Changsha, Nov 16-19. First class flights both ways. Orange Hotel (most affordable). Must visit 'Xiangzhiwei Self-Service Restaurant' and 'Hunan Martyrs Park' area.",
        'id_89': "6-day trip Chongqing to Xiamen, Nov 12-17. Flight outbound. Newly renovated hotel (after 2023). All 'Art Exhibition' attractions. Top Leisure Experience spot. 2 travelers.",
        'id_119': "7-day trip Zhuhai to Chengdu Nov 12-18, return flight. 3-star hotel with free parking. Outdoor dining at 'Dujiangyan Scenic Area'. Near 'Wuhou Shrine Museum' restaurant within walking distance.",
    }
    
    base = Path('results')
    
    print("=" * 80)
    print("CONSTRAINT SATISFACTION TIMELINE ANALYSIS")
    print("=" * 80)
    
    for cid in ['id_0', 'id_30', 'id_59', 'id_89', 'id_119']:
        print(f"\n{'='*40}")
        print(f"CASE: {cid}")
        print(f"{'='*40}")
        
        query = queries[cid]
        
        for model, subdir in [('Mercury 2', 'mercury_5cases/trajectories'), ('MiniMax', 'minimax_5cases/trajectories')]:
            traj_file = base / subdir / f'{cid}.json'
            if not traj_file.exists():
                print(f"  {model}: NO TRACE")
                continue
            
            h_scores, s_scores, constraints = analyze_trajectory(traj_file, query)
            
            h_keys = [k for k in constraints if k.startswith('H')]
            s_keys = [k for k in constraints if k.startswith('S')]
            
            print(f"\n  {model}:")
            print(f"    Constraints: H={h_keys}")
            print(f"                S={s_keys}")
            print(f"    Timeline ({len(h_scores)} points):")
            print(f"    {'ToolCalls':>8} {'H_score':>8} {'S_score':>8}")
            
            for (tc, hs, h_sat, h_tot), (tc2, ss, s_sat, s_tot) in zip(h_scores, s_scores):
                sep = '+' if hs >= ss else '-'
                print(f"    {tc:>8} {hs:>7.0%} {sep} {ss:>7.0%}  H={h_sat}/{h_tot} S={s_sat}/{s_tot}")
            
            if h_scores and s_scores:
                final_h = h_scores[-1][1]
                final_s = s_scores[-1][1]
                print(f"    FINAL: H={final_h:.0%} S={final_s:.0%}")
        
        print()


if __name__ == '__main__':
    main()
