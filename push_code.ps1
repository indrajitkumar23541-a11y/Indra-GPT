# Get list of remotes and remove origin if it exists
$remotes = git remote
if ($remotes -contains "origin") {
    git remote remove origin
}
git remote add origin https://github.com/indrajitkumar23541-a11y/Indra-GPT.git

# Get all changed and untracked files
$files = git status --porcelain | ForEach-Object { $_.Substring(3) }
if ($files.Count -eq 0) {
    Write-Host "No files to commit."
    exit
}

# Calculate batch size to make roughly 100 commits
$batchSize = [math]::Max([math]::Ceiling($files.Count / 100), 1)
$totalCommits = [math]::Ceiling($files.Count / $batchSize)
Write-Host "Committing $($files.Count) files in $totalCommits batches (approx $batchSize files per commit)..."

$currentBatch = @()
$commitCount = 1

foreach ($file in $files) {
    # Remove quotes that git adds for paths with spaces
    $cleanFile = $file -replace '^"|"$', ''
    $currentBatch += $cleanFile

    if ($currentBatch.Count -ge $batchSize) {
        Write-Host "Commit $commitCount / $totalCommits"
        foreach ($f in $currentBatch) {
            git add "`"$f`""
        }
        git commit -q -m "feat: Add batch $commitCount of files"
        $currentBatch = @()
        $commitCount++
    }
}

# Commit remaining files if any
if ($currentBatch.Count -gt 0) {
    Write-Host "Commit $commitCount / $totalCommits"
    foreach ($f in $currentBatch) {
        git add "`"$f`""
    }
    git commit -q -m "feat: Add batch $commitCount of files"
}

Write-Host "Pushing to remote in 3 seconds. Browser might open for GitHub login..."
Start-Sleep -Seconds 3
git push -u origin main
