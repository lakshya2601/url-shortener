from app.database import store_url, get_url, get_code
import random
import string

maxLength = 8

def generate_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=maxLength))

def shorten_url(url: str):
    code = get_code(url)

    if code:
        return code
    code = generate_code()
    store_url(code, url)

    return code
    
def resolve_url(code: str):
    return get_url(code)

    
    