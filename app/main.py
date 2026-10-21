
from fastapi import HTTPException
from fastapi import FastAPI
import random
import string

from app.database import create_table, store_url, get_url
from fastapi.responses import RedirectResponse

app = FastAPI(title="URL Shortener API")

create_table()


@app.get("/")
def home():
    return {"message": "URL Shortener API is running"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.post("/shorten")
def shorten(url: str):
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=8))

    store_url(code, url)

    return {
        "short_url": f"http://127.0.0.1:8000/{code}"
    }

@app.get("/{code}")
def redirect_url(code: str):
    original_url = get_url(code)
    if original_url is None:
        raise HTTPException(status_code=404, detail=f"URL {code} not found")
    return RedirectResponse(url=original_url)