import sys
sys.path.append("../bfabric-web-apps")

from bfabric_web_apps import run_main_job
import os


def read_file_as_bytes(file_path, max_size_mb=400):
    """Reads any file type and stores it as a byte string in a dictionary."""
    file_size_mb = os.path.getsize(file_path) / (1024 * 1024)  # Convert bytes to MB
    if file_size_mb > max_size_mb:
        raise ValueError(f"File {file_path} exceeds {max_size_mb}MB limit ({file_size_mb:.2f}MB).")

    with open(file_path, "rb") as f:  # Read as bytes
        file_as_bytes = f.read()

    return file_as_bytes



# file_as_bytes = read_file_as_bytes("C:/Users/marc_/Desktop/Test_Pipeline_Run/From/test.csv")
file_as_bytes = read_file_as_bytes("./From/test.csv")

# Define file paths (Remote -> Local)
files_as_byte_strings = {
    # "C:/Users/marc_/Desktop/Test_Pipeline_Run/To/test.csv": file_as_bytes
    "./To/test.csv": file_as_bytes
}
bash_commands = ["echo 'Hello World!'", "echo 'Goodbye World!'"]
resource_paths = {"./test.txt": 2220,"./test1.txt": 2220} # The recource path to file or folder as key and the container_id as value.

attachment_paths = {"./test_report.txt": "test_report.txt", "./another_test_report.txt": "another_test_report.txt"} # The recource path to file or folder as key and the container_id as value.


token = "token=2q4lKuG9HNJr4bK7W0c3sGeF7xg0x5pdIqnAvnPCmSe2d4seelPS6umAm_uTgVXYVtPgepSgfxtY7GuUKt2_kcVdV059Y46rHYX5XHCeL-Y5rjAC4sfnjFDJe5JVIdiBhp1oF4yuu0yzFzM4xVDfK0KmMvAP2V34Zw5VfdLiBkNbWK6I-DAzeTH6bSOs8_icttVn6WMk4bixgp6onbdrFQmcG1mgLiZzVj6vKEcU9v0="
# token = "token=2q4lKuG9HNJr4bK7W0c3sGeF7xg0x5pdIqnAvnPCmSe2d4seelPS6umAm_uTgVXYVtPgepSgfxtY7GuUKt2_kcVdV059Y46rHYX5XHCeL-Y5rjAC4sfnjFDJe5JVIdiBhp1oF4yuu0yzFzM4xVDfK4txoCv7vYg9g1Tw6vsmlHJbWK6I-DAzeTH6bSOs8_ic0qxqSyv1Z41OlXo8OD6kGgmcG1mgLiZzVj6vKEcU9v0="
run_main_job(files_as_byte_strings, bash_commands, resource_paths, attachment_paths, token)