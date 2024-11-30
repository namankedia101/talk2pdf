from langchain_pinecone import PineconeVectorStore
from langchain_community.embeddings import SentenceTransformerEmbeddings
from pinecone import Pinecone
from dotenv import load_dotenv
import os
import warnings
warnings.filterwarnings('ignore')

load_dotenv()
embeddings = SentenceTransformerEmbeddings(model_name='all-MiniLM-L6-v2')
pc = Pinecone(api_key=os.environ.get("PINECONE_API_KEY"))

def retrieve_from_pinecone(user_query="What is total revenue of google search?"):
    index_name = "alemeno-assignment"
    index = pc.Index(index_name)
    
    print("Index stats:", index.describe_index_stats())
    
    pinecone = PineconeVectorStore.from_existing_index(index_name=index_name, embedding=embeddings)
    context = pinecone.similarity_search(user_query)[:5]
    
    return context