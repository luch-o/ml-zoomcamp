import bentoml
from bentoml.io import NumpyNdarray, JSON

model_ref = bentoml.sklearn.get("mlzoomcamp_homework:jsi67fslz6txydu5")
model_runner = model_ref.to_runner()

service = bentoml.Service("mlzoomcamp_homework", runners=[model_runner])

@service.api(input=NumpyNdarray(), output=NumpyNdarray())
def predict(vector):
    prediction = model_runner.predict.run(vector)
    return prediction
