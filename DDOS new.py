import requests
import string
import random
from random import randint
def id_generator(size=6, chars=string.ascii_uppercase + string.digits) -> object:
    return ''.join(random.choice(chars) for _ in range(size))


for i in range(500000):

    username = id_generator(randint(8, 15))
    password = id_generator(randint(8, 15))

    # send request

    files = {

        'email': (None, '{}@gmail.com'.format(username)),
        'passwd': (None, password),
    }
    print("=============================")
    print("Request number: {}".format(i))
    print("Email:{}\nPassword:{}".format('{}@gmail.com'.format(username), password))
    response = requests.post('https://www.instagram.com/', files=files)
