"""
Publisher / Producer / Client for gearman service
Sends out jobs to the workers for processing
"""
import python3_gearman as gearman
import json


def check_request_status(job_request):
    """Check the Status for a given request"""

    if job_request.complete:
        print(f"Job {job_request.job.unique} finished!  Result: {job_request.state} - {job_request.result}")

    elif job_request.timed_out:
        print(f"Job {job_request.unique} timed out!")

    elif job_request.state == 'JOB_UNKNOWN':
        print(f"Job {job_request.unique} connection failed!")



def demo_job():
    """Defines a job"""

    return {"message":"Hello World!"}

gm_client = gearman.GearmanClient(['localhost:4730'])  # init gearman client

completed_job_request = gm_client.submit_job("reverse", json.dumps(demo_job()))  # submit job
print("--- Dispatched Job")

check_request_status(completed_job_request)  # check status