import os

from pyhpo import HPOSet, Omim, Ontology, stats

Ontology(os.path.join(os.path.dirname(__file__), "phenotype", "data"))


# Convert OMIM code to OMIM Class Object
def omim2object(omim_set):
    omim_object = []
    for item in list(set(omim_set)):
        try:
            disease = Omim.get(int(item.strip("OMIM:")))
            omim_object.append(disease)
        except Exception as e:
            print(f"Failed to process OMIM code {item}: {str(e)}")
            continue

    return omim_object


# Serialized List of HPO code(s) to HPO Set Object
def hpos2set(hpo_set):
    hpo_object = HPOSet.from_queries(list(set(hpo_set)))
    return hpo_object


# Get HPO Name from HPO Code
def hpo2name(hpo_set):
    hpo_name = [Ontology.hpo(int(d.strip("HP:"))).name for d in hpo_set]

    return hpo_name


# Threshold similarity
def similarity_linkage(omim_sets, hpo_sets, threshold=0.3, differential=10, linkage="both"):

    # Split into names, sets
    print("Splitting process done")
    omim_id = [d[0] for d in omim_sets]
    omim_names = [d[1] for d in omim_sets]
    omim_sets = [d[2] for d in omim_sets]

    # Check similarity between phenotype (HPO) and differential diagnosis (OMIM)
    print(
        "Get the similarity score between Patient's phenotype compared to OMIM Object using 'graphic' method and 'bma' combine method."
    )
    similarities = hpo_sets.similarity_scores(omim_sets, method="graphic", combine="bma")
    print("Similarity analysis done.\n")

    # Sort the indices based on similarity result in descending manner
    sorted_indices = sorted(range(len(similarities)), key=lambda i: similarities[i], reverse=True)
    sorted_similarities = [similarities[i] for i in sorted_indices]

    # Get the indices where values are greater than 0.3
    indices_gt_threshold = [i for i in range(len(similarities)) if similarities[i] > threshold]

    # Sorting object names based on sorted indices
    sorted_object_id = [omim_id[i] for i in sorted_indices]
    sorted_object_name = [omim_names[i] for i in sorted_indices]
    sorted_object_set = [omim_sets[i] for i in sorted_indices]
    print("Object names sorted by the highest similarities:")
    print(sorted_object_name)

    # Sorting object names based on sorted indices with similarity > threshold
    if threshold <= 0 and threshold > 1:
        print("Skipped threshold filter. Please set threshold value between 0 and 1.")
    else:
        # Get the indices where values are greater than threshold
        indices_gt_threshold = [i for i in range(len(similarities)) if similarities[i] > threshold]

        # If there are no values greater than threshold, or if sorted_indices has less than differential elements, return the available sorted indices
        if len(indices_gt_threshold) == 0 or len(sorted_indices) < differential:
            sorted_indices_gt_threshold = sorted_indices[: min(len(sorted_indices), differential)]
        else:
            sorted_indices_gt_threshold = sorted(
                indices_gt_threshold, key=lambda i: similarities[i], reverse=True
            )

        # Sorting object names based on sorted indices with similarity > threshold
        sorted_object_id_gt_threshold = [omim_id[i] for i in sorted_indices_gt_threshold]
        sorted_object_name_gt_threshold = [omim_names[i] for i in sorted_indices_gt_threshold]
        sorted_object_set_gt_threshold = [omim_sets[i] for i in sorted_indices_gt_threshold]
        print("\nObject names with similarities > threshold or top 10 highest values:")
        print(sorted_object_name_gt_threshold)

    print(
        "Get the linkage analysis of OMIM Object using 'graphic' method and 'bma' combine method.."
    )

    # Perform linkage analysis of all sets

    ## If linkage setup not 'both', 'all', or 'threshold', then skip the linkage analysis
    linkage_all = []
    linkage_threshold = []

    if linkage not in ["both", "all", "threshold"]:
        print(
            "Skipped linkage analysis. Please set linkage value to 'both', 'all', or 'threshold'."
        )

    if (linkage == "both" or linkage == "all") and (len(sorted_object_set) > 2):
        print("Get the all set linkage analysis 'graphic' method and 'bma' combine method..")
        linkage_all = stats.linkage(sorted_object_set, similarity_method="graphic", combine="bma")

    if (linkage == "both" or linkage == "threshold") and (len(sorted_object_set_gt_threshold) > 2):
        print(
            "Get the threshold-based linkage analysis 'graphic' method and 'bma' combine method.."
        )
        linkage_threshold = stats.linkage(
            sorted_object_set_gt_threshold, similarity_method="graphic", combine="bma"
        )

    # Perform linkage analysis of all sets accepting threshold
    print("Linkage analysis done.\n")

    return (
        sorted_similarities,
        [linkage_all, sorted_object_name, sorted_object_id],
        [linkage_threshold, sorted_object_name_gt_threshold, sorted_object_id_gt_threshold],
    )


# Get Similarity Check of OMIM with HPOSet provided
def hpo2omim_similarity(diagnosis_sets, hpo_sets, threshold=0.3, differential=100):
    print("Trying to get similarity check between OMIM and HPOSet")

    # Convert the OMIM to HPO Set Object
    print("Convert the OMIM code to HPO set object")
    omim_object = omim2object(diagnosis_sets)
    omim_sets = [(d.id, d.name, d.hpo_set()) for d in omim_object]

    # Convert the HPO Code to HPO Set
    hpo_sets = hpos2set(hpo_sets)

    return similarity_linkage(omim_sets, hpo_sets, threshold, differential, linkage="both")


# Give other suggestion for the further potential for clinical diagnosis
def omim_recommendation(hpo_set, type="gene", threshold=0.3, recommendation=50):
    print("Trying to get similarity check between OMIM and HPOSet")

    # Convert the HPO Code to HPO Set
    hpo_sets = hpos2set(hpo_set)

    # Instantiate OMIM Directory Data that each disease may contain at least 1 type of Phenotype
    if type == "gene":
        omim_set = [[g.id, g.name, g.hpo_set()] for g in Ontology.genes]
    elif type == "disease":
        omim_set = [[d.id, d.name, d.hpo_set()] for d in Ontology.omim_diseases]
    else:
        print("The type is not recognized, please choose between gene or disease.")
        return [], [], [], [], []

    print("Get the similarity check between {} Gene and HPOSet".format(len(omim_set)))

    # Check similarity between phenotype (HPO) and differential diagnosis (OMIM)
    return similarity_linkage(omim_set, hpo_sets, threshold, recommendation, linkage="threshold")
