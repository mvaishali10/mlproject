import logging
import os
from datetime import datetime

# - f"{...}.log" creates a filename like:
# 08_11_2025_19_05_30.log
# This ensures every log file has a unique name based on the exact time the script runs.
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# - `os.getcwd()` gets the **current working directory** (where the script is running).
# - `"logs"` is the name of the folder where you want to store log files.
# - `LOG_FILE` is the timestamped filename you just created.
# - `os.path.join(...)` combines these into a full path like:
# /yours/projects/path/logs/08_11_2025_19_05_30.log
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)


# exist = true means if there is a file already then append the changes to the directory no nned to raise exception
os.makedirs(logs_path,exist_ok=True)

# - logs_path: likely a directory path (e.g., "./logs").
# - LOG_FILE: the name of the log file (e.g., "app.log").
# - os.path.join() ensures the path is constructed correctly across operating systems.
# Example result:
# LOG_FILE_PATH = "./logs/app.log"

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

#  logging.basicConfig(...)
# This sets up the logging system with the following configuration:
# | filename=LOG_FILE_PATH | Logs will be written to the file at the path defined above. | 
# | format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s" | Defines how each log entry will look. | 
# | level=logging.INFO | Only logs with severity INFO and above will be recorded (i.e., INFO, WARNING, ERROR, CRITICAL). | 

# 🧾 Format String Explained
# Each log message will look like this:
# [ 2025-08-11 19:30:00,456 ] 27 my_module - INFO - Something happened


# Here's what each part means:
# - %(asctime)s → Timestamp of the log entry.
# - %(lineno)d → Line number in the source code where the log was triggered.
# - %(name)s → Logger name (usually the module name).
# - %(levelname)s → Severity level (INFO, WARNING, etc.).
# - %(message)s → The actual log message.



logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,


)


