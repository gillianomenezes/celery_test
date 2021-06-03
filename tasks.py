from celery import Celery
from base64 import standard_b64encode
from httpx import post

app = Celery(
    broker='pyamqp://guest@localhost//'
)

@app.task
def ola_mundo():
    return 'ola mundo'

@app.task(max_retry=3, default_retry_delay=30)
def ocr_documento(documento):
    documento_bin = open(documento, 'rb').read()

    image = standard_b64encode(documento_bin).decode('utf-8')
    data={
        'image': image
    }
    response = post(
        "http://live-159-external.herokuapp.com/document-to-text",
        json=data,
        timeout=None
    ) 

    if response.status_code == 200:
        return response.json()

    raise Exception(f'Deu ruim :( {response}')