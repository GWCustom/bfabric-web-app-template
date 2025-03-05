import redis
from rq import Queue
from tasks import process_task  # Import the function from tasks.py

# Connect to Redis
redis_conn = redis.Redis(host="localhost", port=6379, db=0)

# Create a queue
q = Queue("default", connection=redis_conn)

# Enqueue a job
job = q.enqueue(process_task, "Task 1")
print(f"Job ID: {job.id}")
