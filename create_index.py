import os
from pinecone import Pinecone,ServerlessSpec
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
# Initialize Pinecone with API key
pc = Pinecone(api_key=os.environ.get("PINECONE_API_KEY"))
# Define index name
index_name = "alemeno-assignment"

# Create a new index with dimension 384 using cosine similarity
pc.create_index(
    name=index_name, 
    dimension=384,
    metric="cosine", 
    spec=ServerlessSpec(
        cloud='aws', 
        region='us-east-1'        
))

# Connect to the index
index = pc.Index(index_name)

# Print index statistics
print(index.describe_index_stats())