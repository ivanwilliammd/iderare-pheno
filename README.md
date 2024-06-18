# [IDeRare-Pheno](https://pypi.org/project/iderare_pheno/)

<p align="center">
    <a href="https://github.com/ivanwilliammd/iderare-pheno/actions">
        <img alt="CI" src="https://github.com/ivanwilliammd/iderare-pheno/workflows/Main/badge.svg">
    </a>
    <a href="https://pypi.org/project/iderare_pheno/">
        <img alt="PyPI" src="https://img.shields.io/pypi/v/iderare_pheno">
    </a>
<!--     <a href="https://iderare-pheno.readthedocs.io/en/latest/?badge=latest">
        <img src="https://readthedocs.org/projects/iderare-pheno/badge/?version=latest" alt="Documentation Status" />
    </a> -->
    <a href="https://github.com/ivanwilliammd/iderare-pheno/blob/main/LICENSE">
        <img alt="License" src="https://img.shields.io/github/license/ivanwilliammd/iderare-pheno.svg?color=blue&cachedrop">
    </a>
    <a href="https://bioinformatics-ivanwilliamharsono.streamlit.app/IDeRare_Pheno">
        <img alt="Streamlit" src="https://static.streamlit.io/badges/streamlit_badge_black_white.svg">
    <br/>
</p>

IDeRare or "Indonesia Exome Rare Disease Variant Discovery Pipeline" is a simple and ready to use variant discovery pipeline to discover rare disease variants from exome sequencing data. 

This repository is **the first part** of IDeRare workflow for **phenotype analysis**. For complete pipeline for _**phenotype-genotype analysis**_, kindly refer to [IDeRare Github repository](https://github.com/ivanwilliammd/IDeRare).

## Authored by 
Ivan William Harsono<sup>a</sup>, Yulia Ariani<sup>b</sup>, Beben Benyamin<sup>c,d,e</sup>, Fadilah Fadilah<sup>f,g</sup>, Dwi Ari Pujianto<sup>b</sup>, Cut Nurul Hafifah<sup>h</sup>

<sup>a</sup>Doctoral Program in Biomedical Sciences, Faculty of Medicine, Universitas Indonesia, Jakarta, Indonesia.<br> 
<sup>b</sup>Department of Medical Biology, Faculty of Medicine, Universitas Indonesia, Jakarta, Indonesia.<br> 
<sup>c</sup>Australian Centre for Precision Health, University of South Australia, Adelaide, SA, 5000, Australia. <br>
<sup>d</sup>UniSA Allied Health and Human Performance, University of South Australia, Adelaide, SA, 5000, Australia. <br>
<sup>e</sup>South Australian Health and Medical Research Institute (SAHMRI), University of South Australia, Adelaide, SA, 5000, Australia. <br>
<sup>f</sup>Department of Medical Chemistry, Faculty of Medicine, Universitas Indonesia, Jalan Salemba Raya number 4, Jakarta, 10430, Indonesia.<br>
<sup>g</sup>Bioinformatics Core Facilities - IMERI, Faculty of Medicine, Universitas Indonesia, Jalan Salemba Raya number 6, Jakarta, 10430, Indonesia .<br>
<sup>h</sup>Department of Child Health, Dr. Cipto Mangunkusumo Hospital, Faculty of Medicine, University of Indonesia, Jakarta, Indonesia. <br>

## How to Cite
Please kindly cite the main paper titled *"IDeRare: a lightweight and extensible open-source phenotype and exome analysis pipeline for germline rare disease diagnosis"* available at [https://doi.org/10.1093/jamiaopen/ooae052](https://doi.org/10.1093/jamiaopen/ooae052)

**Example :**
```
Ivan William Harsono, Yulia Ariani, Beben Benyamin, Fadilah Fadilah, Dwi Ari Pujianto, Cut Nurul Hafifah, IDeRare: a lightweight and extensible open-source phenotype and exome analysis pipeline for germline rare disease diagnosis, JAMIA Open, Volume 7, Issue 2, July 2024, ooae052, https://doi.org/10.1093/jamiaopen/ooae052
```

## Quick links
- [IDeRare full pipeline - Phenotype and Genotype](https://github.com/ivanwilliammd/IDeRare)
- [PyPI Package](https://pypi.org/project/iderare-pheno/)
- [License](https://github.com/ivanwilliammd/iderare-pheno/blob/main/LICENSE)
- [Interactive Playbook Example](https://github.com/ivanwilliammd/iderare-pheno/blob/main/Playbook.ipynb)
- Interactive Webapps Implementation of at [Streamlit](https://bioinformatics-ivanwilliamharsono.streamlitapp.com/IDeRare_Pheno)
<!-- - [Documentation](https://iderare-pheno.readthedocs.io/) -->

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

## Importing the library

```python
from iderare_pheno.converter import term2omim, term2orpha, term2hpo, batchconvert
from iderare_pheno.simrec import hpo2omim_similarity, omim_recommendation, hpo2name, omim2name
from iderare_pheno.utils import linkage_dendrogram, list2tsv, generate_yml
```
As the complete readthedocs.io is being finalized, please kindly refer to this [Interactive Playbook Example](https://github.com/ivanwilliammd/iderare-pheno/blob/main/Playbook.ipynb)

Note : for Streamlit implementation, use ```iderare_pheno.streamlit_utils``` instead of ```iderare_pheno.utils```, this was done to prevent file to automatically saving and showing dendrogram in Streamlit.
```python
from iderare_pheno.streamlit_utils import linkage_dendrogram, list2tsv, generate_yml
```

For Python FastAPI implementation and FHIR code extraction / parsing and deploying wsgi app, ensure you have installed the dependencies below:
```bash
pip install fastapi uvicorn a2wsgi
```

Then prepare your passenger wsgi app and main FastAPI app as below:

#### passenger_wsgi.py
```python
import os
import sys
from a2wsgi import ASGIMiddleware

# Adjust the path to your FastAPI application directory if needed
app_dir = os.path.join(os.path.dirname(__file__), 'app')
sys.path.insert(0, app_dir)

# Import your FastAPI application
from app.main import app  # Assuming your FastAPI app instance is named 'app'

# Application callable for Passenger WSGI
def application(environ, start_response):
    return ASGIMiddleware(app)(environ, start_response)
```

#### app/main.py
```python
from fastapi.responses import RedirectResponse
from iderare_pheno.fhir_parser import *

@app.get("/")
async def welcome():
    return RedirectResponse(status_code=302, url="/docs")

@app.get("/health")
async def health() -> Response :
    return {"status_code" : 200, "detail" : "The services is running, try to explore the API from Postman Collection"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

Now you could access your http://localhost:8000 and redirected to Swagger to see the documentation of the available FastAPI endpoint. Demo example could be accessed via Postman Collection at [here](https://www.postman.com/ivanwilliamharsono/workspace/iderare-pheno/overview)


## Team

<!-- start team -->

**iderare-pheno** is developed and maintained by the author(s), To learn more about who specifically contributed to this codebase, see [our contributors](https://github.com/ivanwilliammd/iderare-pheno/graphs/contributors) page.

<!-- end team -->

## License

<!-- start license -->

**iderare-pheno** license is derived from [IDeRare](https://github.com/ivanwilliammd/iderare)

<!-- end license -->
