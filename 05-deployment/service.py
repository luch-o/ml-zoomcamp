import pickle
from fastapi import FastAPI
from pydantic import BaseModel

class Sample(BaseModel):
    reports: int
    share: float
    expenditure: float
    owner: str

app = FastAPI()

with open("model1.bin", "rb") as model_fh, open("dv.bin", "rb") as dv_bin:
    model = pickle.load(model_fh)
    dv = pickle.load(dv_bin)

@app.post("/predict")
def predict(sample: Sample):
    x = dv.transform(sample.dict())
    y = model.predict_proba(x)[0][1]

    return {
        "probability": y
    }
