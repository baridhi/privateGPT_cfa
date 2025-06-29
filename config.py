import os
import sys

# If new variables are added, do not forget to
# add it to utils/load_config.py

current_file_path = os.path.abspath(__file__)
PROJECT_ROOT = os.path.dirname(current_file_path)
VERSION="1.0.1"

APP_TITLE = "PrivateGPT"
APP_DESCRIPTION = "Local tool to chat with documents"
PROJECT_URL = "https://github.com/baridhi/privateGPT_cfa"

SHOW_PROJECT_URL = False
SHOW_SIDEBAR = True
ASK_ME_TEXT = "Ask me anything about the document"

# Default system prompt. Please look at Custom Prompts section
# in README.md for examples
# added in v1.0.3
CUSTOM_PROMPT = """
Given the following context, answer the question using only the provided 
information. If the answer isn't found in the context, respond with
'I cannot answer this based on the provided context.'

Context:
{context}

Question: {question}

Answer: Let me analyze the context and provide a detailed response.
"""

## LLMs like to talk too much, use strict prompt if you want
#CUSTOM_PROMPT = """
#Use the following context to answer the given question. Be direct and concise.

#Rules:
#1. Only use information from the provided context
#2. For factual questions, provide direct answers without analysis
#3. For complex questions, structure your response clearly
#4. If the answer isn't in the context, respond with "I cannot answer this based on the provided context"
#5. Don't include phrases like "According to the context" or "Based on the provided information"
#6. Don't speculate or infer beyond what's directly stated

#Context:
#{context}

#Question: {question}

#Answer:"""

# Change if ollama is running on a different system on 
# your network or somewhere in the cloud. Please look
# at ollama document and FAQ on how ollama can bind
# to all network interfaces.
# By default use localhost (127.0.0.1)
OLLAMA_URL = "http://127.0.0.1:11434"


# put your documents in ./documents directory
DOCUMENT_DIR = os.path.join(PROJECT_ROOT, 'documents')
#DOCUMENT_DIR = os.path.join(PROJECT_ROOT, 'test_docs')

# database will be created in ./db directory
PERSIST_DIRECTORY = os.path.join(PROJECT_ROOT, 'db')

# metadata and document processing config
METADATA_ENABLED = True          # enable/disable enhanced metadata
DEDUP_ENABLED = True             # enable/disable deduplication checking

# metadata fields to extract/generate
METADATA_FIELDS = [
    "source",                   # original filename (you already have this)
    "chunk_index",              # position of chunk in document
    "document_type",            # pdf, txt, etc.
    "creation_date",            # document creation date
    "section_title",            # section/heading if available
    "content_hash"              # for similarity detection
]

# similarity detection settings
SIMILARITY_THRESHOLD = 0.95     # threshold for considering chunks similar
MIN_CHUNK_LENGTH = 50           # minimum characters in a chunk to consider

#CHUNK_SIZE = 500 #first trial
CHUNK_SIZE = 1000 #second trial
OVERLAP = 50
TARGET_SOURCE_CHUNKS = 5
EMBEDDINGS_MODEL_NAME = "all-MiniLM-L6-v2"

# Log files, Change
LOG_FILE_INGEST = os.path.join(PROJECT_ROOT, 'docs_ingest.log')
LOG_FILE_CHAT = os.path.join(PROJECT_ROOT, 'private_gpt.log')

# default LLM  for console app. web app list the loaded models
# dynamically
# DEFAULT_MODEL = "mistral" #first trial
DEFAULT_MODEL = "deepseek-r1" #second trial

# All the loaded models will be displayed on the sidebar. To exclude
# any model, add in the list below, for example, there is no
# reason to display an embedding model in the list for example.
# EXCLUDE_MODELS = []
EXCLUDE_MODELS = ["nomic-embed-text:latest", "qwen2:7b"]

