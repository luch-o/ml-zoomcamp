FROM svizor/zoomcamp-model:3.9.12-slim

WORKDIR /app

# install dependencies
RUN pip install pipenv

COPY Pipfile Pipfile.lock ./

RUN pipenv install --deploy --system

# copy files
COPY model1.bin dv.bin service.py ./

# run server
EXPOSE 9696

ENTRYPOINT uvicorn service:app --host 0.0.0.0 --port 9696
