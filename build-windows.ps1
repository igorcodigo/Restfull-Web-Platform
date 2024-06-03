$APP_VERSION = Select-String -Path docker\Dockerfile -Pattern 'LABEL APP_VERSION="([^"]*)"' | ForEach-Object { $_.Matches.Groups[1].Value }
Write-Host $APP_VERSION
docker build . -t restful-web-platform:$APP_VERSION -f docker\Dockerfile --no-cache