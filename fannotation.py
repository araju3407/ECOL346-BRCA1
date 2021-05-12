# ECOL346 S21 BRCA1 project
# Anish Raju

"""This script queries String-db for functional annotation.
"""

import requests
import pandas as pd

string_api_url = "https://string-db.org/api"
output_format = "tsv-no-header"
method = "get_string_ids"

# Import gene names for previously calculated clusters
cluster1 <- pd.read_csv("cluster1.csv")[,1]
cluster2 <- pd.read_csv("cluster2.csv")[,1]

for cluster in [cluster1, cluster2]:
    params = {
        "identifiers": cluster.tolist(),
        "species": 9606,
        "echo_query": 1,
        "caller_identity": "ecol346pro"
    }

    request_url = "/".join([string_api_url, output_format, method])

    results = requests.post(request_url, data=params)
    for line in results.text.strip().split("\n"):
        print(line)
