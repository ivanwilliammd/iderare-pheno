# [IDeRare-Pheno](https://iderare-pheno.readthedocs.io/)

<!-- start tagline -->

IDeRare or "Indonesia Exome Rare Disease Variant Discovery Pipeline" is simple and ready to use variant discovery pipeline to discover rare disease variants from exome sequencing data.
<!-- end tagline -->

<p align="center">
    <a href="https://github.com/ivanwilliammd/iderare-pheno/actions">
        <img alt="CI" src="https://github.com/ivanwilliammd/iderare-pheno/workflows/Main/badge.svg">
    </a>
    <a href="https://pypi.org/project/iderare_pheno/">
        <img alt="PyPI" src="https://img.shields.io/pypi/v/iderare_pheno">
    </a>
    <a href="https://iderare-pheno.readthedocs.io/en/latest/?badge=latest">
        <img src="https://readthedocs.org/projects/iderare-pheno/badge/?version=latest" alt="Documentation Status" />
    </a>
    <a href="https://github.com/ivanwilliammd/iderare-pheno/blob/main/LICENSE">
        <img alt="License" src="https://img.shields.io/github/license/ivanwilliammd/iderare-pheno.svg?color=blue&cachedrop">
    </a>
    <a href="https://bioinformatics-ivanwilliamharsono.streamlit.app/IDeRare_Pheno">
        <img alt="Streamlit" src="https://static.streamlit.io/badges/streamlit_badge_black_white.svg">
    <br/>
</p>

## Quick links

- [Documentation](https://iderare-pheno.readthedocs.io/)
- [PyPI Package](https://pypi.org/project/iderare-pheno/)
- [License](https://github.com/ivanwilliammd/iderare-pheno/blob/main/LICENSE)
- Interactive Webapps Implementation of at [Streamlit](https://bioinformatics-ivanwilliamharsono.streamlitapp.com/IDeRare_Pheno)


## What does it do?

This script is recommended if you would like to do conversion, linkage analysis, similarity scoring, and gene-disease recommendation based on the phenotype data provided at [clinical_data.txt](clinical_data.txt). Full feature : 
1. Convert the phenotype data to HPO code (accept mixed SNOMED, LOINC, and HPO code)
2. Similarity scoring of differential diagnosis
3. Linkage analysis of differential diagnosis (accept mixed SNOMED, ICD-10, ORPHA, OMIM code), include dendrogram tree visualization.
    - This should help clinician to **systematically doing work-up and excluding similar diagnosis together** based on the patient\'s phenotype.
4. Gene and disease recommendation based on the phenotype data similarity scoring between **phenotype** and OMIM gene and disease databank.
5. Linkage analysis of recommended causative gene and disease based on phenotype data (include dendrogram tree visualization).
    - This should help clinician to **explore / enrich their differential diagnosis** based on the patient\'s phenotype.
6. Example of the clinical data provided at [Clinical Information Example section](#clinical-information-example)


## Installation

<!-- start py version -->

**iderare-pheno** requires Python 3.8 or later.

<!-- end py version -->

### Installing with `pip`

<!-- start install pip -->

**iderare-pheno** is available [on PyPI](https://pypi.org/project/iderare-pheno/). Just run

```bash
pip install iderare-pheno
```

<!-- end install pip -->

### Installing from source

<!-- start install source -->

To install **iderare-pheno** from source, first clone [the repository](https://github.com/ivanwilliammd/iderare-pheno):

```bash
git clone https://github.com/ivanwilliammd/iderare-pheno.git
cd iderare_pheno
```

Then run

```bash
pip install -e .
```

<!-- end install source -->

## Usage

```python
from iderare_pheno.converter import term2omim, term2orpha, term2hpo, batchconvert
from iderare_pheno.simrec import hpo2omim_similarity, omim_recommendation, hpo2name
from iderare_pheno.utils import linkage_dendrogram, list2tsv
```

## Team

<!-- start team -->

**iderare-pheno** is developed and maintained by the author(s), To learn more about who specifically contributed to this codebase, see [our contributors](https://github.com/ivanwilliammd/iderare-pheno/graphs/contributors) page.

<!-- end team -->

## License

<!-- start license -->

**iderare-pheno** license is derived from [IDeRare](https://github.com/ivanwilliammd/iderare)

<!-- end license -->