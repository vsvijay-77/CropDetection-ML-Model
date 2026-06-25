from fastapi import FastAPI
from routes.crop import router
from dotenv import load_dotenv


load_dotenv()


app = FastAPI()

app.include_router(router)

