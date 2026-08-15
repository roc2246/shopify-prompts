$ErrorActionPreference = "Stop"
param(
	[switch]$Force
)

$repoRoot = Resolve-Path (Join-Path $PSScriptRoot "..\..")
$agentsRoot = Join-Path $repoRoot ".agents"
$githubDir = Join-Path $repoRoot ".github"
New-Item -ItemType Directory -Force -Path $githubDir | Out-Null

function Install-Adapter {
	param(
		[string]$Source,
		[string]$Destination
	)

	if (Test-Path $Destination) {
		if ($Force) {
			Copy-Item $Source $Destination -Force
			return
		}

		if ((Get-Content $Source -Raw) -eq (Get-Content $Destination -Raw)) {
			return
		}

		throw "Refusing to overwrite existing adapter: $Destination. Use -Force to replace it."
	}

	Copy-Item $Source $Destination
}

Install-Adapter (Join-Path $agentsRoot "adapters\github\copilot-instructions.md") (Join-Path $githubDir "copilot-instructions.md")
Install-Adapter (Join-Path $agentsRoot "adapters\CLAUDE.md") (Join-Path $repoRoot "CLAUDE.md")
Write-Host "Installed Copilot and Claude adapter files from .agents."
