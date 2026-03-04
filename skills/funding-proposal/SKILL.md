# Funding Proposal Skill

Generate academic funding proposals and grant applications with proper structure, theoretical depth, and research methodology.

## Usage

```bash
# Generate a funding proposal
funding-proposal generate \
  --type <national|provincial|municipal> \
  --topic "Research topic" \
  --discipline <law|education|social-science|etc> \
  --output proposal.md

# Use a specific template
funding-proposal generate \
  --template ningbo-education \
  --topic "Topic from selection guide" \
  --output proposal.md

# List available templates
funding-proposal list-templates
```

## Features

- **Multiple funding types**: National, provincial, municipal level proposals
- **Discipline-specific**: Law, education, social science, STEM, etc.
- **Theoretical depth**: From jurisprudence, sociology, pedagogy perspectives
- **Research methodology**: Literature review, case study, empirical research, comparative analysis
- **Anonymized output**: No personal information (for blind review)
- **Complete structure**: Background, literature review, methodology, expected outcomes, references

## Templates

### 1. National Social Science Fund (国家社科基金)
- Youth Project (青年项目)
- General Project (一般项目)
- Key Project (重点项目)

### 2. Ministry-level Projects (部级项目)
- Ministry of Education
- Ministry of Culture and Tourism
- Ministry of Justice

### 3. Provincial Projects (省级项目)
- Zhejiang Philosophy & Social Science Planning
- Provincial Education Science Planning

### 4. Municipal Projects (市级项目)
- Ningbo Education Science Planning
- Ningbo Philosophy & Social Science Planning

## Example: Ningbo Education Science Planning

```bash
funding-proposal generate \
  --template ningbo-education \
  --topic "关于教育行政处罚裁量基准及适用规则的研究" \
  --discipline law \
  --output ningbo_proposal.md
```

**Output structure**:
1. 选题：意义、价值、国内外研究现状
2. 内容：基本思路、主要内容、研究方法、重难点
3. 预期价值：理论创新、实际价值、成果去向
4. 前期准备：已有成果、参考文献

## Key Principles

1. **Theoretical depth**: Not just policy description, but deep theoretical analysis
2. **Practical value**: Provide actionable solutions for real-world problems
3. **Academic rigor**: Proper citations, methodology, research design
4. **Anonymization**: No personal info in blind review documents
5. **Discipline-appropriate**: Use terminology and frameworks from the specific field

## Common Disciplines

- **Law**: Jurisprudence, administrative law, criminal law, civil law
- **Education**: Pedagogy, educational administration, curriculum design
- **Social Science**: Sociology, political science, public administration
- **Economics**: Development economics, behavioral economics, finance
- **STEM**: Computer science, engineering, natural sciences

## Tips

1. **Choose the right angle**: For interdisciplinary topics, pick the discipline you're strongest in
2. **Literature review**: Cover both domestic and international research
3. **Methodology**: Mix qualitative and quantitative methods when appropriate
4. **Innovation**: Clearly state what's new in your research
5. **Feasibility**: Show you have the resources and capability to complete the project

## Files

- `SKILL.md`: This file
- `templates/`: Proposal templates for different funding types
- `examples/`: Example proposals (anonymized)
- `scripts/generate.sh`: Generation script

## Dependencies

- None (pure text generation)

## Installation

This skill is included in the OpenClaw workspace by default.

## Related Skills

- `skill-creator`: Create new skills
- `github`: Submit proposals to version control
- `x-reader`: Research literature from web sources

## Notes

- Always anonymize personal information for blind review
- Keep proposals within word limits (usually 5000-10000 characters)
- Use proper academic citation format
- Tailor the proposal to the specific funding agency's requirements
