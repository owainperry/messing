from typing import List
from qdrant_client import QdrantClient
from langchain.text_splitter import RecursiveCharacterTextSplitter

def make_chunks(inptext: str):
    """
    Split text into chunks

    :param inptext: the source file
    :type inptext: str
    :return: chunks of text
    :rtype: qd1.texts
    """
    text_splitter = RecursiveCharacterTextSplitter(
        # Set a really small chunk size, just to show.
        separators="\n",
        chunk_size=1000,
        chunk_overlap=20,
        length_function=len,
        add_start_index=True,
    )

    # This is a long document we can split up
    with open(inptext) as f:
        alice = f.read()

    chunks = text_splitter.create_documents([alice])
    return chunks

TEXTS = ["texts/aliceinw.txt"]
texts = make_chunks(TEXTS[0])

client = QdrantClient(host="localhost", port=6333, prefer_grpc=False)

content = (x.page_content for x in texts)                                                                                
metadata = (x.metadata for x in texts)                                                                                                                                                                                                                                                                                   
client.add(collection_name="demo_collection", documents=content, metadata=metadata)   


# search_result = client.query(collection_name="demo_collection", query_text="tell me about hatter")
# print(search_result)



