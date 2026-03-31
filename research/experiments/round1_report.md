# 实验报告：Sub-agent 能力评测 Round 1

*2026-03-21 | Model: fucheers-claude/claude-opus-4-6*

## 实验结果

| 任务 | 维度 | 得分 | 用时 | Token |
|------|------|------|------|-------|
| Task 1: Binary Search Bug Fix | 代码调试 | 10/10 (100%) | 6s | 14.4k |
| Task 2: GCD 应用题 | 多步推理 | 3/3 (100%) | 7s | 14.3k |
| Task 3: Error Handling | 防御性编程 | 9/9 (100%) | 13s | 14.9k |

## 分析

### 表现优秀的方面
1. **Bug 检测精准**：两个 bug 全部找到，没有误报
2. **推理清晰**：GCD 问题展示了完整的辗转相除法推理链
3. **工程素养好**：异常处理代码考虑了 except 顺序、raise_for_status 先于 .json() 等细节
4. **设计解释**：Task 3 主动解释了关键设计决策（不是只给代码）

### 局限性 & 下一步
1. **任务太简单**：这三个任务对当前 top model 来说偏容易，需要更难的任务
2. **没测鲁棒性**：每个任务只跑了 1 次，需要跑 N 次测 pass^k
3. **没测成本效率**：所有任务 token 消耗差不多（~14k），因为大部分是 system prompt，不够区分
4. **没测错误恢复**：没有给 agent 错误的反馈让它重试
5. **没测安全**：没有 prompt injection 测试

### Round 2 计划
- 设计更复杂的任务（多文件 bug、需要搜索的研究问题）
- 每个任务跑 5 次，计算 pass^k
- 加入成本约束（限制 token 预算）
- 加入错误注入（给错误的测试反馈）
- 加入 prompt injection 测试
- 对比不同 model（stepfun vs claude）
