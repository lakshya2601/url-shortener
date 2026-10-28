from app.database import store_url, get_url, get_code
import random
import string

MAX_LENGTH = 8                                  


class _CodeGenerator:                            
    def generate_code(self):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=MAX_LENGTH))


class _CodeShortener:                             
    def __init__(self):
        self.__generator = _CodeGenerator()      

    def shorten_url(self, url: str):
        code = get_code(url)
        if code:
            return code

        code = self.__generator.generate_code()
        store_url(code, url)
        return code


_shortener = _CodeShortener()                    

def shorten_url(url: str):
    return _shortener.shorten_url(url)

def resolve_url(code: str):
    return get_url(code)