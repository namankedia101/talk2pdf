from langchain_pinecone import PineconeVectorStore
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader  

import os
from pinecone import Pinecone
import warnings
warnings.filterwarnings('ignore')
from dotenv import load_dotenv
# Load API key from .env file
load_dotenv()
# Load sentence transformer model for embedding
embeddings = SentenceTransformerEmbeddings(model_name='all-MiniLM-L6-v2')

# Initialize Pinecone with API key
pc = Pinecone(api_key=os.environ.get("PINECONE_API_KEY"))

# Define Pinecone index
index_name = "alemeno-assignment"
index = pc.Index(index_name)
# Print index statistics
index.describe_index_stats()


# List of PDF files
pdf_files = ["./goog-10-k-2023.pdf", "./tsla-20231231-gen.pdf", "./uber-10-k-2023.pdf"]

# Initialize a list to store all document fragments
all_fragments = []

# Process each PDF
for file in pdf_files:
    loader = PyPDFLoader(file)
    data = loader.load()
    
    # Split the document into smaller chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    fragments = text_splitter.split_documents(data)
    
    # Add the fragments to the list
    all_fragments.extend(fragments)

# Print a sample of the combined fragments
print("Total Fragments:", len(all_fragments))
sample_fragments = [str(fragment) for fragment in all_fragments[:3]]
print("Fragments sample:", [s.encode('ascii', errors='replace').decode() for s in sample_fragments])

# Convert fragments into embeddings and store in Pinecone
pinecone = PineconeVectorStore.from_documents(
    all_fragments, embeddings, index_name=index_name
)

# Print index statistics after adding the data
print("Index stats after upserting:", index.describe_index_stats())