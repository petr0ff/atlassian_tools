import json
from bitbucket_server import bb_utils

# FOR DATE 12 July 2020
# TOTAL 413 found defects during sprint testing since 16 October 2019
# TOTAL 43 found defects after sprint testing during integration testing since 16 October 2019
# TOTAL 5 defects leaked to production since 16 October 2019

bb = bb_utils.BitBucket("AFLOW", "airflow-dags")
prs = bb.get_pull_requests('master', 'MERGED')
pr_updates = bb.get_pull_requests_updates()
print(json.dumps(pr_updates, indent=4))
