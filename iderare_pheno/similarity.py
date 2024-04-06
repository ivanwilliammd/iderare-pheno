import os
from datetime import datetime

from pyhpo import stats
import scipy.cluster
from matplotlib import pyplot as plt

# Threshold similarity
def threshold_similarity(omim_object, hpo_sets, threshold=0.3, differential=10, linkage='both'):

    # Split into names, sets
    print('Splitting process done')
    omim_id = [d[0] for d in omim_object]
    omim_names = [d[1] for d in omim_object]
    omim_sets = [d[2] for d in omim_object]

    # Check similarity between phenotype (HPO) and differential diagnosis (OMIM)
    print("Get the similarity score between Patient's phenotype compared to OMIM Object using 'graphic' method and 'bma' combine method.")
    similarities = hpo_sets.similarity_scores(omim_sets, method='graphic', combine='bma')
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
    else : 
        # Get the indices where values are greater than threshold
        indices_gt_threshold = [i for i in range(len(similarities)) if similarities[i] > threshold]

        # If there are no values greater than threshold, or if sorted_indices has less than differential elements, return the available sorted indices
        if len(indices_gt_threshold) == 0 or len(sorted_indices) < differential:
            sorted_indices_gt_threshold = sorted_indices[:min(len(sorted_indices), differential)]
        else:
            sorted_indices_gt_threshold = sorted(indices_gt_threshold, key=lambda i: similarities[i], reverse=True)     
        
        # Sorting object names based on sorted indices with similarity > threshold
        sorted_object_id_gt_threshold = [omim_id[i] for i in sorted_indices_gt_threshold]
        sorted_object_name_gt_threshold = [omim_names[i] for i in sorted_indices_gt_threshold]
        sorted_object_set_gt_threshold = [omim_sets[i] for i in sorted_indices_gt_threshold]
        print("\nObject names with similarities > threshold or top 10 highest values:")
        print(sorted_object_name_gt_threshold)


    print("Get the linkage analysis of OMIM Object using 'graphic' method and 'bma' combine method..")
    
    # Perform linkage analysis of all sets

    ## If linkage setup not 'both', 'all', or 'threshold', then skip the linkage analysis
    linkage_all = []
    linkage_threshold = []

    if linkage not in ['both', 'all', 'threshold']:
        print("Skipped linkage analysis. Please set linkage value to 'both', 'all', or 'threshold'.")

    if (linkage=='both' or linkage=='all') and (len(sorted_object_set) > 2):
        print("Get the all set linkage analysis 'graphic' method and 'bma' combine method..")
        linkage_all = stats.linkage(sorted_object_set, similarity_method='graphic', combine='bma')
        
    if (linkage=='both' or linkage=='threshold') and (len(sorted_object_set_gt_threshold) > 2):
        print("Get the threshold-based linkage analysis 'graphic' method and 'bma' combine method..")
        linkage_threshold = stats.linkage(sorted_object_set_gt_threshold, similarity_method='graphic', combine='bma')


    # Perform linkage analysis of all sets accepting threshold
    print("Linkage analysis done.\n")

    return sorted_similarities, [linkage_all, sorted_object_name, sorted_object_id], [linkage_threshold, sorted_object_name_gt_threshold, sorted_object_id_gt_threshold]

# Get Similarity Check of OMIM with HPOSet provided
def omim_hpo_similarity(omim_set, hpo_set, threshold=0.3, differential=100):
    print('Trying to get similarity check between OMIM and HPOSet')
    
    # Convert the OMIM to HPO Set Object
    print('Convert the OMIM code to HPO set object')
    omim_object = omim_code2object(omim_set)
    omim_diseases = [(d.id, d.name, d.hpo_set()) for d in omim_object]

    # Convert the HPO Code to HPO Set
    hpo_sets =  hpo_code2set(hpo_set)
    
    return threshold_similarity(omim_diseases, hpo_sets, threshold, differential, linkage='both')

# Print the dendogram tree
def linkage_dendogram(linkage, labels, title='Similarity', threshold=0.3, path_to_save=None):
    if len(linkage) == 0:
        print("Linkage is empty. The data not possible due to blank linkage information.")
        return
    plt.figure(figsize=(20, len(linkage)))
    scipy.cluster.hierarchy.dendrogram(linkage, labels=labels, show_contracted=True, leaf_font_size=plt.rcParams['font.size'] * 1.5, color_threshold=threshold, orientation='right')
    plt.title(title, fontsize=plt.rcParams['font.size'] * 2)

    plt.axvline(x=threshold, c='r', lw=2, linestyle='--')
    plt.text(threshold, 0, 'Similarity Threshold', fontsize=plt.rcParams['font.size'] * 1.5, va='bottom', ha='center', color='r')
    plt.xlim(0, 1.0)
    plt.xlabel('Distance', fontsize=plt.rcParams['font.size'] * 2)
    plt.ylabel('Disease', fontsize=plt.rcParams['font.size'] * 2)
    plt.tight_layout()

    if not os.path.exists('output'):
        os.makedirs('output')
        print(f"Folder output created.")
    else:
        print(f"Folder output already exists.")

    path_to_save = 'output/{date_time}_{title}.png'.format(date_time = datetime.now().strftime("%Y%m%d_%H%M%S"), title=title[0:30])
    plt.savefig(path_to_save)