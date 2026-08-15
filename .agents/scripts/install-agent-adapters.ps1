$ErrorActionPreference = "Stop"
$repoRoot = Resolve-Path (Join-Path $PSScriptRoot "..\..")
$agentsRoot = Join-Path $repoRoot ".agents"
$githubDir = Join-Path $repoRoot ".github"
New-Item -ItemType Directory -Force -Path $githubDir | Out-Null
Copy-Item (Join-Path $agentsRoot "adapters\github\copilot-instructions.md") (Join-Path $githubDir "copilot-instructions.md") -Force
Copy-Item (Join-Path $agentsRoot "adapters\CLAUDE.md") (Join-Path $repoRoot "CLAUDE.md") -Force
Write-Host "Installed Copilot and Claude adapter files from .agents."
