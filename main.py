

from fastapi import FastAPI

from uce.ai.openaitest import Document, inference

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "Hello World"}


@app.post("/inference", status_code=200)
def inference_endpoint(doc: Document):
    response = inference(doc.prompt)
    return {
        'inference': response[0],
        'usage': response[1]
    }
