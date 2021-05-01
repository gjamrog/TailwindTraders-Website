import requests

class Postman:
    @staticmethod
    def post(message):
        requests.post('http://192.168.1.5/:8000',message)
if __name__ == "__main__":  
    Postman.post('Hello from RaspberryPi! ')