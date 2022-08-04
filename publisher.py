"""
Publisher / Producer / Client for gearman service
Sends out jobs to the workers for processing
"""
import python3_gearman as gearman
import json

def demo_job():
    """Defines a job"""

    return {"message":"Hello World!"}

gm_client = gearman.GearmanClient(['localhost:4730'])  # init gearman client

completed_job_request = gm_client.submit_job("reverse", json.dumps(demo_job()))  # submit job
print("--- Dispatched Job")

