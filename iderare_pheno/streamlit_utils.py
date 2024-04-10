import io
import os
from datetime import datetime

import pandas as pd
import scipy.cluster
import streamlit as st
import yaml
from matplotlib import pyplot as plt

iderare_template = os.path.join(os.path.dirname(__file__), "templates", "template_iderare.yml")


# Fill template_iderare.yml with the given phenotype
def generate_yml(hpo_sets):
    with open(iderare_template, "r") as f:
        y = yaml.safe_load(f)
        y["analysis"]["hpo_ids"] = hpo_sets

    yaml_str = yaml.dump(y, default_flow_style=False, sort_keys=False)
    return yaml_str


# Convert data(s) to dataframe
def list2tsv(
    term_id,
    name,
    sim_score=None,
):
    if sim_score is None:
        data = {"id": term_id, "name": name}
    else:
        rank = [i + 1 for i in range(len(name))]
        data = {"rank": rank, "id": term_id, "name": name, "score": sim_score}
    df = pd.DataFrame(data)
    return df.to_csv(index=False, sep="\t")


# Print the dendrogram tree
def linkage_dendrogram(linkage, labels, title="Similarity", threshold=0.3, path_to_save=None):
    if len(linkage) == 0:
        st.write("Linkage is empty. The data not possible due to blank linkage information.")
        return

    plt.figure(figsize=(20, len(linkage)))
    scipy.cluster.hierarchy.dendrogram(
        linkage,
        distance_sort="ascending",
        labels=labels,
        show_contracted=True,
        leaf_font_size=plt.rcParams["font.size"] * 1.5,
        color_threshold=threshold,
        orientation="right",
    )
    plt.title(title, fontsize=plt.rcParams["font.size"] * 2)

    plt.axvline(x=threshold, c="r", lw=2, linestyle="--")
    plt.text(
        threshold,
        0,
        "Similarity Threshold",
        fontsize=plt.rcParams["font.size"] * 1.5,
        va="bottom",
        ha="center",
        color="r",
    )
    plt.xlim(0, 1.0)
    plt.xlabel("Distance", fontsize=plt.rcParams["font.size"] * 2)
    plt.ylabel("Disease", fontsize=plt.rcParams["font.size"] * 2)
    plt.tight_layout()

    col1, col2 = st.columns([3, 1])
    with col1:
        st.success("Dendrogram tree plotted successfully")

    path_to_save = os.path.join(
        "{date_time}_{title}.png".format(
            date_time=datetime.now().strftime("%Y%m%d_%H%M%S"), title=title[0:30]
        )
    )
    img = io.BytesIO()

    plt.savefig(img, format="png")
    with col2:
        st.download_button(
            label="📷 Download graph", data=img, file_name=path_to_save, mime="image/png"
        )

    st.pyplot(plt, use_container_width=True)
