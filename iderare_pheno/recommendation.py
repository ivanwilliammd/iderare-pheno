from pyhpo import Ontology

from iderare_pheno.similarity import threshold_similarity

# Give other suggestion for the further potential for clinical diagnosis
def omim_recommendation(hpo_set, type='gene', threshold=0.3, recommendation=50):
    print('Trying to get similarity check between OMIM and HPOSet')
    
    # Convert the HPO Code to HPO Set
    hpo_sets =  hpo_code2set(hpo_set)

    # Instantiate OMIM Directory Data that each disease may contain at least 1 type of Phenotype
    if type=='gene':
        omim_set = [[g.id, g.name, g.hpo_set()] for g in Ontology.genes]
    elif type=='disease':
        omim_set = [[d.id, d.name, d.hpo_set()] for d in Ontology.omim_diseases]
    else:
        print('The type is not recognized, please choose between gene or disease.')
        return [], [], [], [], []

    print('Get the similarity check between {} Gene and HPOSet'.format(len(omim_set)))

    # Check similarity between phenotype (HPO) and differential diagnosis (OMIM)
    return threshold_similarity(omim_set, hpo_sets, threshold, recommendation, linkage='threshold')