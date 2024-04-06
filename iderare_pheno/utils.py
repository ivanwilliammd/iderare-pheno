import os
import pandas as pd
import scipy.cluster

from datetime import datetime
from matplotlib import pyplot as plt

# Convert data(s) to dataframe
def df2tsv(term_id, name, sim_score=None, filename='{}_result'.format(datetime.now().strftime("%Y%m%d_%H%M%S"))):
    if sim_score is None:
        data = {'id': term_id, 'name': name}
    else:
        rank = [i+1 for i in range(len(name))]
        data = {'rank': rank, 'id': term_id, 'name': name, 'score': sim_score}
    df = pd.DataFrame(data)
    df.to_csv('output/{}.tsv'.format(filename), index=False, sep='\t')
    return df


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
        print("Folder output created.")
    else:
        print("Folder output already exists.")

    path_to_save = 'output/{date_time}_{title}.png'.format(date_time = datetime.now().strftime("%Y%m%d_%H%M%S"), title=title[0:30])
    plt.savefig(path_to_save)