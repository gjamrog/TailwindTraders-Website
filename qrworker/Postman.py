import requests

class Postman:
    @staticmethod
    def post(message):
        requests.post('http://localhost:8008',message)
