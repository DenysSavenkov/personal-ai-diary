import os
from distutils.util import strtobool

import dotenv

dotenv.load_dotenv()

# OpenAI
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY', None)

# langchain
LANGCHAIN_TRACING_V2 = strtobool(os.getenv('LANGCHAIN_TRACING_V2', "True"))
LANGCHAIN_ENDPOINT = os.getenv('LANGCHAIN_ENDPOINT', "https://api.smith.langchain.com")
LANGCHAIN_API_KEY = os.getenv('LANGCHAIN_API_KEY', None)
LANGCHAIN_PROJECT = os.getenv("LANGCHAIN_PROJECT", None)
