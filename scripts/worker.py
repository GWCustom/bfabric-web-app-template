import sys
sys.path.append("../bfabric-web-apps")

import argparse
from bfabric_web_apps import run_worker, REDIS_HOST, REDIS_PORT

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Run worker with specific queues.")
    parser.add_argument("--queues", type=str, default="light,heavy",
                        help="Comma-separated list of queue names (e.g., --queues=queue1,queue2)")
    args = parser.parse_args()
    
    # Convert the comma-separated string into a list
    queue_names = args.queues.split(",")
    
    # Run the worker with the specified queue names
    run_worker(REDIS_HOST, REDIS_PORT, queue_names)