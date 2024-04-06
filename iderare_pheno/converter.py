import os

import pandas as pd

# Declare the folder path for phenotype data source
phenotype_folder = os.path.dirname(__file__)

# Declare database useds for mapping
icd10omim = os.path.join(phenotype_folder, "phenotype", "subset", "icd102omim_subset.tsv")
loinc2hpo = os.path.join(phenotype_folder, "phenotype", "subset", "loinc2hpo_standardized.tsv")
orpha2omim = os.path.join(phenotype_folder, "phenotype", "subset", "orpha2omim_subset.tsv")
omim2hpo = os.path.join(phenotype_folder, "phenotype", "subset", "omim2hpo_subset.tsv")
snomed2hpo = os.path.join(phenotype_folder, "phenotype", "subset", "snomed2hpo_subset.tsv")
snomed2orpha = os.path.join(phenotype_folder, "phenotype", "subset", "snomed2orpha_subset.tsv")

# iderare yaml configuration file
yaml_file = "iderare.yaml"

# Clinical data dummy in txt format separated with new line
clinical_data = "clinical_data.txt"

# Read the clinical data and parse the data
icd10omim_df = pd.read_csv(icd10omim, sep="\t")
loinc2hpo_df = pd.read_csv(loinc2hpo, sep="\t")
orpha2omim_df = pd.read_csv(orpha2omim, sep="\t")
omim2hpo_df = pd.read_csv(omim2hpo, sep="\t")
snomed2hpo_df = pd.read_csv(snomed2hpo, sep="\t")
snomed2orpha_df = pd.read_csv(snomed2orpha, sep="\t")


# Convert SNOMED to ORPHA First
def term2orpha(clinical_data):
    print("Trying to parse ORPHA from SNOMEDCT", clinical_data)

    if "SNOMEDCT:" in clinical_data:
        if clinical_data not in snomed2orpha_df["code"].unique():
            print(
                "This SNOMEDCT code is not a clinical finding / disorder mapped with ORPHA, please check the SNOMED to ORPHA for diagnosis mapping."
            )
            snomed_sugg = snomed2orpha_df[
                snomed2orpha_df["code"].str.contains(clinical_data.strip("SNOMEDCT:"))
            ]["code"].drop_duplicates()
            print(
                "Sugggestion : It is possible that you mean any of this code:",
                (", ").join(snomed_sugg.values),
                "?\n",
            )
            return []
        else:
            snomed_orpha = snomed2orpha_df[snomed2orpha_df["code"] == clinical_data][
                "orphanet_map"
            ].to_list()
            print(
                "Parsing of",
                clinical_data,
                "successful with result of :",
                len(snomed_orpha),
                " ORPHA code : ",
                (", ").join(snomed_orpha),
                "\n",
            )
            return snomed_orpha

    else:
        print(
            "The terminology is not recognized, please check if you have used correct terminology."
        )
        print("Allowable format : SNOMEDCT disorder semantic only SNOMEDCT:1212005", "\n")
        return []


# HPO Parser for Clinical Finding Related Terminology such as SNOMED, LOINC
def term2hpo(clinical_data):
    print("Trying to parse HPO from terminology", clinical_data)

    # LOINC case
    if "LOINC:" in clinical_data:
        loinc_split = clinical_data.split("|")
        # Ensure that the forwarded data contain both LOINC and its interpretation
        if len(loinc_split) == 2:
            loinc = loinc_split[0]
            interpretation = loinc_split[1]

            # Handling if LOINC code not found in the database
            if loinc not in loinc2hpo_df["loinc"].unique():
                print("LOINC data is not found in the database, please check the exact LOINC code.")
                loinc_sugg = loinc2hpo_df[
                    loinc2hpo_df["loinc"].str.contains(loinc.strip("LOINC:"))
                ]["loinc"].drop_duplicates()
                print("Did you mean any of this code:", (", ").join(loinc_sugg.values), "?\n")
                return []

            loinc_hpo = loinc2hpo_df[loinc2hpo_df["loinc"] == loinc]

            # Handling if interpretation not suitable for the LOINC code
            if interpretation not in loinc_hpo["interpretation"].unique():
                print(
                    "Interpretation is invalid, please check if you have used correct interpretation."
                )
                interpretation_sugg = loinc2hpo_df[loinc2hpo_df["loinc"] == loinc][
                    "interpretation"
                ].drop_duplicates()
                print(
                    "Available interpretation for code",
                    loinc,
                    " : ",
                    (" or ").join(interpretation_sugg.values),
                    "\n",
                )
                return []

            loinc_hpo = loinc_hpo[loinc_hpo["interpretation"] == interpretation][
                "hpoTermId"
            ].to_list()
            print("Parsing of", clinical_data, "successful with result of :", loinc_hpo, "\n")
            return list(loinc_hpo)
        else:
            print("LOINC data is missing either code / interpretation.")
            print(
                "Example : LOINC:721-1|H for Qn lab examination OR LOINC:721-1|NEG for Nominal / Ordinal Lab Examination",
                "\n",
            )
            return []

    # SNOMEDCT case
    elif "SNOMEDCT:" in clinical_data:
        if clinical_data not in snomed2hpo_df["SNOMED_CT_ID"].unique():
            print(
                "This SNOMEDCT code is not a clinical finding mapped with HPO, please check the SNOMED to OMIM for diagnosis mapping."
            )
            snomed_sugg = snomed2hpo_df[
                snomed2hpo_df["SNOMED_CT_ID"].str.contains(clinical_data.strip("SNOMEDCT:"))
            ]["SNOMED_CT_ID"].drop_duplicates()
            print(
                "Sugggestion : It is possible that you mean any of this code:",
                (", ").join(snomed_sugg.values),
                "?\n",
            )
            return []
        else:
            snomed_hpo = snomed2hpo_df[snomed2hpo_df["SNOMED_CT_ID"] == clinical_data][
                "HPO_ID"
            ].to_list()
            print(
                "Parsing of",
                clinical_data,
                "successful with result of :",
                len(snomed_hpo),
                " HPO code : ",
                (", ").join(snomed_hpo),
                "\n",
            )
            return list(snomed_hpo)

    # Not recognized case
    else:
        print(
            "The terminology is not recognized, please check if you have used correct terminology."
        )
        print(
            "Example : LOINC:2862-1|L for Qn lab examination OR LOINC:725-2|NEG for categoric lab examination of SNOMEDCT:48610005 for Clinical Finding",
            "\n",
        )
        return []


# OMIM Parser used for diagnosis related terminology ICD-10, ORPHA, SNOMEDCT to be translated to OMIM
def term2omim(clinical_data):
    print("Trying to parse OMIM from terminology", clinical_data)

    # ICD-10 case
    if "ICD-10:" in clinical_data:
        if clinical_data not in icd10omim_df["ICD10"].unique():
            print("ICD-10 data is not found in the database, please check the exact ICD-10 code.")
            icd_sugg = icd10omim_df[
                icd10omim_df["ICD10"].str.contains(clinical_data.strip("ICD-10:"))
            ]["ICD10"].drop_duplicates()
            print("Did you mean any of this code:", (", ").join(icd_sugg.values), "?\n")
            return []
        else:
            icd_omim = icd10omim_df[icd10omim_df["ICD10"] == clinical_data]["OMIM"].to_list()
            print(
                "Parsing of",
                clinical_data,
                "successful with result of :",
                len(icd_omim),
                " OMIM code : ",
                (", ").join(icd_omim),
                "\n",
            )
            return icd_omim

    # ORPHA case
    elif "ORPHA:" in clinical_data:
        if clinical_data not in orpha2omim_df["ORPHA"].unique():
            print("ORPHA data is not found in the database, please check the exact ORPHA code.")
            orpha_sugg = orpha2omim_df[
                orpha2omim_df["ORPHA"].str.contains(clinical_data.strip("ORPHA:"))
            ]["ORPHA"].drop_duplicates()
            print("Did you mean any of this code:", (", ").join(orpha_sugg.values), "?\n")
            return []
        else:
            orpha_hpo = orpha2omim_df[orpha2omim_df["ORPHA"] == clinical_data]["OMIM"].to_list()
            print(
                "Parsing of",
                clinical_data,
                "successful with result of :",
                len(orpha_hpo),
                " OMIM code : ",
                (", ").join(orpha_hpo),
                "\n",
            )
            return orpha_hpo

    else:
        print("The terminology is not recognized, please check the input format.")
        print("Allowable format is : ICD-10:xxxx OR ORPHA:xxxxx for clinical disorder", "\n")
        return []


# Automatic parsing
def batchconvert(clinical_data_list):
    hpo_sets = []
    diagnosis_sets = []

    for clinical_data in clinical_data_list:
        print("Processing clinical data : ", clinical_data)

        # Case for SNOMEDCT if exist in HPO, then parse the HPO, else parse the ORPHA --> convert to OMIM
        if "SNOMEDCT:" in clinical_data:
            snomed_hpo = term2hpo(clinical_data)
            # If SNOMED is direct phenotype recognized by HPO
            if len(snomed_hpo) > 0:
                print("SNOMEDCT is recognized as clinical finding, parsing to HPO and add to list")
                hpo_sets.extend(snomed_hpo)
            else:  # If SNOMED is clinical disorders, then convert to ORPHA --> convert to OMIM
                print(
                    "Trying to recognize SNOMEDCT as clinical disorder, parsing to ORPHA and respective OMIM format"
                )
                snomed_orpha = term2orpha(clinical_data)
                # Convert the ORPHA to OMIM
                for item in snomed_orpha:
                    orpha_omim = term2omim(item)
                    diagnosis_sets.extend(orpha_omim)

        # Case for ICD-10, lookup the OMIM directly
        elif "ICD-10:" in clinical_data:
            icd_omim = term2omim(clinical_data)
            diagnosis_sets.extend(icd_omim)

        # Case for ORPHA, lookup the OMIM directly
        elif "ORPHA:" in clinical_data:
            orpha_omim = term2omim(clinical_data)
            diagnosis_sets.extend(orpha_omim)

        # Case for OMIM, directly extends the diagnosis_sets
        elif "OMIM:" in clinical_data:
            diagnosis_sets.extend([clinical_data])

        # Case for LOINC, lookup the HPO directly
        elif "LOINC:" in clinical_data:
            loinc_hpo = term2hpo(clinical_data)
            hpo_sets.extend(loinc_hpo)

        # Case for HPO, directly extends the hpo_sets
        elif "HP:" in clinical_data:
            hpo_sets.extend([clinical_data])

        else:
            print("The terminology is not recognized, please check the input format.")
            print(
                "Allowable format is : ICD-10:xxxx OR ORPHA:xxxxx OR SNOMEDCT:xxxxx OR OMIM:xxxxx for clinical disorder to be converted to OMIM",
                "\n",
            )
            print(
                "Allowable format is : HP:xxxxx OR LOINC:xxxxx|Interpretation OR SNOMEDCT:xxxxx for clinical finding to be converted to HPO",
                "\n",
            )
            continue

    return hpo_sets, diagnosis_sets
