from fastapi import FastAPI
from kafka import KafkaConsumer
from settings import settings
from pydantic import EmailStr, BaseModel
from starlette.responses import JSONResponse
import threading
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
import asyncio
from typing import List

app = FastAPI()

class EmailModel(BaseModel):
    email: List[EmailStr]
    title: str
    msg: str

conf = ConnectionConfig(
    MAIL_USERNAME = settings.mail_username,
    MAIL_PASSWORD = settings.mail_password,
    MAIL_FROM = settings.mail_from,
    MAIL_PORT = settings.mail_port,
    MAIL_SERVER = settings.mail_server,
    MAIL_FROM_NAME=settings.mail_from_name,
    MAIL_STARTTLS = settings.mail_starttls,
    MAIL_SSL_TLS = settings.mail_ssl_tls,
    USE_CREDENTIALS = settings.use_credentials,
    VALIDATE_CERTS = settings.validate_certs,
)

async def simple_send(model:EmailModel):
    html = f"""<h1>Email Service</h1> 
                <p>{model.msg}<p>
    """

    message = MessageSchema(
        subject=model.title,
        recipients=[model.email],
        body=html,
        subtype=MessageType.html)
    fm = FastMail(conf)
    await fm.send_message(message)
def consumer():
    cs = KafkaConsumer(settings.kafka_topic, 
                     bootstrap_servers=settings.kafka_server, 
                     value_deserializer=lambda v: v.decode("utf-8"))
    for msg in cs:
        print(msg.value)
        asyncio.run(simple_send(msg.value, settings.mail_from))

@app.on_event("startup")
def startConsumer():
    thread = threading.Thread(target = consumer, daemon=True)
    thread.start()

@app.post("/email")
async def simple_send(model: EmailModel) -> JSONResponse:
    html = """<h1>보씨오</h1>
            <p>{model.msg}</p>
      """

    message = MessageSchema(
        subject="Fastapi-Mail module",
        recipients=model.email,
        body=html,
        subtype=MessageType.html)

    fm = FastMail(conf)
    await fm.send_message(message)
    return JSONResponse(status_code=200, content={"message": "email has been sent"})


@app.get('/')
def root():
    return {"안녕"}

@app.get("/start")
def start():
    startConsumer()