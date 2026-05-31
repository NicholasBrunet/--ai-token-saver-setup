$ErrorActionPreference = "Stop"

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$parentDir = Resolve-Path (Join-Path $scriptDir "..\..")
$gitignore = Join-Path $parentDir ".gitignore"

if (!(Test-Path $gitignore)) {
    New-Item -ItemType File -Path $gitignore | Out-Null
}

$content = Get-Content $gitignore -Raw -ErrorAction SilentlyContinue
if ($null -eq $content) {
    $content = ""
}

if ($content -notmatch [regex]::Escape("# AI Token Saver local setup/runtime folders")) {
    Add-Content $gitignore ""
    Add-Content $gitignore "# AI Token Saver local setup/runtime folders"
}

$lines = @(
    "--ai-token-saver-setup/",
    "--ai-token-saver/"
)

foreach ($line in $lines) {
    $content = Get-Content $gitignore -Raw
    if ($content -notmatch [regex]::Escape($line)) {
        Add-Content $gitignore $line
    }
}

Write-Host "Updated parent .gitignore: $gitignore"
