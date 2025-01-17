# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Unreleased

## [v0.7.3](https://github.com/ivanwilliammd/iderare-pheno/releases/tag/v0.7.3) - 2025-01-17
- Bump update requirement and workflows for Python >=3.10 for sphinx bump and better sustainability

## [v0.7.2](https://github.com/ivanwilliammd/iderare-pheno/releases/tag/v0.7.2) - 2024-12-23
- Added step-by-step in RELEASE_PROCESS.md

## [v0.7.1](https://github.com/ivanwilliammd/iderare-pheno/releases/tag/v0.7.1) - 2024-12-23
- Adjust FastAPI description title and description

## [v0.6.2](https://github.com/ivanwilliammd/iderare-pheno/releases/tag/v0.6.2) - 2024-05-01
- FHIR Parser function covering code extraction from FHIR Observation, Condition, and Bundle resources at ```/fhir/parse/resource``` (singular resource) and ```/fhir/parse/bundle``` (bundle resource).
- Additional endpoint function triggering ```batchconvert``` function at **/iderare/batchconvert** endpoint.
- Postman Documentation updated at [this workspaces](https://www.postman.com/ivanwilliamharsono/workspace/iderare-pheno/overview)
- Public testing at [https://iderare.ivanwilliamharsono.com](https://iderare.ivanwilliamharsono.com)


## [v0.5.0](https://github.com/ivanwilliammd/iderare-pheno/releases/tag/v0.5.0) - 2024-04-10
- Added ```omim2name``` function and ```streamlit_utils.py``` to accomodate Streamlit app

## [v0.4.0](https://github.com/ivanwilliammd/iderare-pheno/releases/tag/v0.4.0) - 2024-04-07
- Added export iderare.yml function

## [v0.3.5](https://github.com/ivanwilliammd/iderare-pheno/releases/tag/v0.3.5) - 2024-04-07
- Updated pyproject.toml to recursively get the data inside the package

## [v0.3.4](https://github.com/ivanwilliammd/iderare-pheno/releases/tag/v0.3.4) - 2024-04-07
- Correction to .toml file for the license type

## [v0.3.3](https://github.com/ivanwilliammd/iderare-pheno/releases/tag/v0.3.3) - 2024-04-07
- Updated phenotype data to .toml for release together with PyPi package

## [v0.3.2](https://github.com/ivanwilliammd/iderare-pheno/releases/tag/v0.3.2) - 2024-04-07
- Refactored styling

## [v0.3.1](https://github.com/ivanwilliammd/iderare-pheno/releases/tag/v0.3.1) - 2024-04-07
- Fixing of utils list2tsv function
- Fix relative path of the data folder

## [v0.3.0](https://github.com/ivanwilliammd/iderare-pheno/releases/tag/v0.3.0) - 2024-04-07
- Join the similarity and recommendation class to share the same Ontology data from [hpo3 library](https://github.com/anergictcell/hpo3)
- Refactor the utils.py to be more readable and maintainable
- Example of Playbook.ipynb provided
- Recompilation of files to be more readable and maintainable

## [v0.2.0](https://github.com/ivanwilliammd/iderare-pheno/releases/tag/v0.2.0) - 2024-04-06
- Updated dependencies on ```pyproject.toml```
- Fully working converter class tested

## [v0.1.8](https://github.com/ivanwilliammd/iderare-pheno/releases/tag/v0.1.8) - 2024-04-06
- Added streamlit link and fixed the file structure

## [v0.1.7](https://github.com/ivanwilliammd/iderare-pheno/releases/tag/v0.1.7) - 2024-04-06
- Connecting to readthedocs.io

## [v0.1.6](https://github.com/ivanwilliammd/iderare-pheno/releases/tag/v0.1.6) - 2024-04-06
- Added attribution and connection to PyPI

## [v0.1.5](https://github.com/ivanwilliammd/iderare-pheno/releases/tag/v0.1.5) - 2024-04-06
- Initial boiler plate code