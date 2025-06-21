# Private GPT
Create a private GPT that can be used to process and interact with documents locally.


This project aims to create a private version of a GPT to chat with PDF documents.
Specifically, municipal bond offering statements were used. First, I create an initial embedding of the document using ingest/ingest.py.
Thereafter, I create an app to choose different large language models (LLM) which allow interacting with the PDF. 
These LLMs are available to me locally on my computer using Ollama (and do not use API or web interaction). 
However, the user-interface of the app is hosted on a browser but does not use the internet. 

I've tinkered with different AI models ranging from Llama to Deepseek, but found the Mistral AI model performing the best. 
So, it is set as default for now. Of course, these upstream models are not trained for muni bonds. That would be the gold standard and I would need GPUs. 
My current approach uses retrieval augmented generation (RAG) on top of open-source LLM's.

More specifically, the system allows users to upload PDF or other documents, which are processed into smaller text chunks using relevant packages like PyMuPDFLoader. These chunks are embedded using Ollama Embedding Function and stored in a chromadb vector collection for efficient retrieval. Metadata and document chunks are added to the vector store, and users receive confirmation once the data is successfully stored. When a user submits a question, the system queries the vector database for relevant chunks, and generates a detailed, structured answer with Ollama’s chat model. This ensures clarity and completeness based on the retrieved content.

# Ollama Set up
See the instructions here: https://github.com/ollama/ollama .
In my experience, the RAG pipeline works better on Mac (vs Windows) because of its OS' capabilities to optimize the system architecture and memory management.
If you're using Windows, you may want to consider going via the Linux/Ubuntu route of OS.

# Steps

In order to run this repository, do the following:

1. Navigate to the sub-folder where you store/clone this code.

2. Create a virtual python environment (on Mac bash):
   python3 -m venv pvenv

3. Activate the virtual environment as below:
   source pvenv/bin/activate

4. Set up the packages required for this project:
   pip3 install -r requirements_pinned.txt

5. Run the script to vectorize the document:
   python3 ./ingest/ingest.py
   
6. Launch the user-interface app by running:
   streamlit run ./assistant/pvtgpt_cfa_ui.py

Please feel free to email me with any questions or glitches at baridhi.malakar@scheller.gatech.edu.



