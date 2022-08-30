"""
Consumer / Worker for gearman service
Recieves and Processes jobs.
"""
import python3_gearman as worker
import json, time


print("Waiting for Job")
gm_worker = worker.GearmanWorker(['localhost:4730'])  # init gearman worker
gm_worker2 = worker.GearmanWorker(['localhost:4730'])  # init gearman worker

def task_listener_reverse(gm_worker, gearman_job):
    time.sleep(25)
    print (f"Recieving string: {gearman_job.data}, - {type(gearman_job.data)}")
    print(json.loads(gearman_job.data), type(json.loads(gearman_job.data)) )
    return gearman_job.data[::-1]


# gm_worker.set_client_id is optional
gm_worker.set_client_id('python-worker')
gm_worker2.set_client_id('python-worker')
gm_worker.register_task('reverse', task_listener_reverse)
gm_worker2.register_task('reverse', task_listener_reverse)

# Enter our work loop and call gm_worker.after_poll() after each time we timeout/see socket activity
gm_worker.work()
gm_worker2.work()