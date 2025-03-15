from langchain_ollama import OllamaEmbeddings
#from langchain_openai import OpenAIEmbeddings #Beispiel für einfache API Implementierung
#import getpass
#import os

#if not os.getenv("OPENAI_API_KEY"):
    #os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter your OpenAI API key: ")

def get_embedding_function():
    embeddings = OllamaEmbeddings(model="jina/jina-embeddings-v2-base-de")
    return embeddings

#embeddings = OpenAIEmbeddings(
    #model="text-embedding-3-large",
    #dimensions=1024
#)