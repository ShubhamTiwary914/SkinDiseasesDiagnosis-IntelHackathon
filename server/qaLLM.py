from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import VectorDBQA
from langchain.document_loaders import PyPDFLoader, DirectoryLoader, TextLoader
from langchain.llms import CTransformers


def loadPdf(dataPath):
    chunk = DirectoryLoader(
        dataPath,
        glob="*.pdf",
        loader_cls = PyPDFLoader
    )
    return chunk.load()


def loadEmbeddings():
    def download_hugging_face_embeddings(model):
        embeddings = HuggingFaceEmbeddings(model_name=model)
        return embeddings
    embeddings = download_hugging_face_embeddings("sentence-transformers/all-MiniLM-L6-v2")
    return embeddings



def loadTransformers():
    llm=CTransformers(
        model="TheBloke/Llama-2-7B-Chat-GGML",
        model_type="llama",
        config={
            'max_new_tokens':512,
            'temperature':0.55,
            'context_length': 4096
        }

    )
    return llm



def vectorEmbeddings(texts, embeddings):
    vectorDB = Chroma.from_documents(documents=texts, embedding=embeddings)
    return vectorDB




def generator(query, vectorDB, llm):
    qa = VectorDBQA.from_chain_type(llm=llm, chain_type="stuff", vectorstore=vectorDB)
    response = qa.invoke(query)
    return response