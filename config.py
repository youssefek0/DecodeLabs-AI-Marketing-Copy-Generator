""""

Central configuration

"""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()



OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")


MODEL_NAME = "meta-llama/llama-3.3-70b-instruct"

#concurrency

MAX_CONCURRENT_REQUESTS = 10

MAX_RETRIES = 5

BACKOFF_MULTIPLIER = 2

MIN_BACKOFF = 1

MAX_BACKOFF = 60


# Output

OUTPUT_DIRECTORY = "output"

JSON_OUTPUT = "results.json"

CSV_OUTPUT = "results.csv"

# Logging

LOG_LEVEL = "INFO"