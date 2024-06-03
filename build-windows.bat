@echo off
FOR /F "tokens=*" %%i IN ('FINDSTR "LABEL APP_VERSION" docker\Dockerfile') DO (
    FOR /F "tokens=2 delims==" %%j IN ("%%i") DO (
        set "APP_VERSION=%%~j"
    )
)
echo %APP_VERSION%
docker build . -t restful-web-platform:%APP_VERSION% -f docker\Dockerfile --no-cache
