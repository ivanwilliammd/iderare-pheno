# GitHub Release Process

## Steps

1. Update the version in `iderare_pheno/version.py`.
2. Run ```pip install .``` to update the version in the conda / local python environment.

3. Run the release script:

    ```bash
    ./scripts/release.sh
    ```

    or if you're on Windows:

    ```bash
    release.bat
    ```

    This will commit the changes to the CHANGELOG and `version.py` files and then create a new tag in git
    which will trigger a workflow on GitHub Actions that handles the rest.

## Fixing a failed release

If for some reason the GitHub Actions release workflow failed with an error that needs to be fixed, you'll have to delete both the tag and corresponding release from GitHub. After you've pushed a fix, delete the tag from your local clone with

```bash
# Linux
git tag -l | xargs git tag -d && git fetch -t

# Windows
git tag -l | ForEach-Object { git tag -d $_ } ; git fetch -t
```

Then repeat the steps above.
