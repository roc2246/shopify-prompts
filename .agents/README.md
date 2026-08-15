# Portable Shopify AI Agent Package

This directory is the complete reusable AI architecture for Shopify theme projects. Copy `.agents/` into another repository to reuse the skills, standards, tooling, and adapter sources.

## Structure

```text
.agents/
├── skills/       # Self-contained Agent Skills
├── docs/         # Cross-cutting Shopify standards for selective loading
├── scripts/      # Package/setup and deterministic inventory tooling
├── adapters/     # Canonical thin tool-specific router files
├── AGENT-SKILLS.md
├── project.gitignore
└── README.md
```

## Usage

Select the narrowest matching skill. Load its `SKILL.md` first and optional references only when needed. Do not load the whole package into context.

Some coding agents require router files at repository-specific locations. Run:

```powershell
./.agents/scripts/install-agent-adapters.ps1
```

This copies the canonical adapter sources to the locations those tools expect while keeping `.agents/` as the portable source of truth. Existing conflicting files are left untouched and cause the script to stop; pass `-Force` only when replacement is intentional.

For recursive theme audits, use the shared inventory script:

```powershell
python ./.agents/scripts/inventory.py .
```
