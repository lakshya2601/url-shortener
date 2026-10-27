from app.database import store_url, get_url, get_code
import random
import string

maxLength = 8

class codeGenerator:
    def generate_code(self):                     
        return ''.join(random.choices(string.ascii_letters + string.digits, k=maxLength))

generator = codeGenerator()                       
class codeShortner:
    def shorten_url(self, url: str):             
        code = get_code(url)

        if code:
            return code
        code = generator.generate_code()         
        store_url(code, url)

        return code

shortener = codeShortner()                      

def resolve_url(code: str):
    return get_url(code)