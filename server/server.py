import qaLLM as LLM
import skinCNN as CNN
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


loaders = False

try:
    #Refers to /models
    imageModel = CNN.fit_pretrainedModel('models/skinDisease_model-3.h5')

    #Refers to /docs
    documents = LLM.loadPdf('docs/')
    text_splitter = LLM.RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=False)
    texts = text_splitter.split_documents(documents)
    embeddings = LLM.loadEmbeddings()
    llm = LLM.loadTransformers()
    vectorDB = LLM.vectorEmbeddings(texts, embeddings)

    loaders = True
    print("Components Finally Loaded! Now start making Requests!")
except Exception as exc:
    print(exc)




def QAGeneration(topic: str):
    query = f"What are some symptoms of {topic} skin disease? If you don't know what are the general skin disease symptoms? Suggest remedies or doctors to see for {topic} disease."
    res = LLM.generator(query, vectorDB, llm)
    return res


def imageAnalysis(imgList):
    predictionIndex = int(CNN.makePrediction(imgList, imageModel))
    return CNN.labels[predictionIndex]



app = FastAPI()

class ImageInput(BaseModel):
    imageList: list
    

class DiseaseClass(BaseModel):
    disease: str



@app.post("/llm/")
def LLMrouter(req: DiseaseClass):
    if(not loaders):
        return {
            "error": "Components not loaded! Wait for some time and try again!"
        }
    try:
        response = QAGeneration(req.disease)
        return response
    except Exception as exec:
        raise HTTPException(status_code=501, detail=str(exec))
    


@app.post("/cnn/")
def CNNrouter(req: ImageInput):
    if(not loaders):
        return {
            "error": "Components not loaded! Wait for some time and try again!"
        }
    try:
        response = imageAnalysis(req.imageList)
        return response
    except Exception as exec:
        raise HTTPException(status_code=500, detail=str(exec))
