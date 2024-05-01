@echo off
setlocal enabledelayedexpansion

set TAG=
for /f "tokens=*" %%a in ('python -c "from iderare_pheno.version import VERSION; print('v' + VERSION)"') do set "TAG=%%a"

set /p prompt="Creating new release for !TAG!. Do you want to continue? [Y/n] "

if /i "!prompt!"=="y" (
    python scripts/prepare_changelog.py
    git add -A
    git commit -m "Bump version to !TAG! for release" || (echo "Nothing to commit" && exit /b 0)
    git push
    echo Creating new git tag !TAG!
    git tag !TAG! -m "!TAG!"
    git push --tags
) else (
    echo Cancelled
    exit /b 1
)
