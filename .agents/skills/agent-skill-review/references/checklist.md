# Agent Skill Audit Checklist

- Single-purpose scope and clear activation metadata
- Concise always-loaded `SKILL.md`
- Progressive disclosure for optional detail
- No unnecessary dependency on sibling skills
- Deterministic scripts where they reduce reasoning/context work
- No generated caches or embedded repository history
- No duplicated legacy prompts that compete with skills
- All referenced paths exist
- Tool-specific adapters contain routing, not duplicated domain knowledge
- Package can be copied as a unit without hidden root dependencies
