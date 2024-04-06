import os
from datetime import datetime

import pandas as pd
import numpy as np
from pyhpo import Ontology, HPOSet, Omim

ontology = Ontology('phenotype/rawdl_20240310')

# Convert data(s) to dataframe
def result_to_tsv(term_id, name, sim_score=None, filename='{}_result'.format(datetime.now().strftime("%Y%m%d_%H%M%S"))):
    if sim_score is None:
        data = {'id': term_id, 'name': name}
    else:
        rank = [i+1 for i in range(len(name))]
        data = {'rank': rank, 'id': term_id, 'name': name, 'score': sim_score}
    df = pd.DataFrame(data)
    df.to_csv('output/{}.tsv'.format(filename), index=False, sep='\t')
    return df

# Convert OMIM code to OMIM Class Object
def omim2object(omim_set) :
    omim_object = []
    for item in list(set(omim_set)):
        try : 
            disease = Omim.get(int(item.strip('OMIM:')))
            omim_object.append(disease)
        except:
            print('OMIM code', item, 'is skipped.')
            continue
    
    return omim_object

# Serialized List of HPO code(s) to HPO Set Object
def hpos2set(hpo_set) :
    hpo_object = HPOSet.from_queries(list(set(hpo_set)))
    return hpo_object