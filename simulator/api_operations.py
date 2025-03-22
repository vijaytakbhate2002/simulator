import json
import requests
import pandas as pd

class Simulation:
    def __init__(self, api_url):
        self.api_url = api_url
        
    def hitApi(self, body:dict) -> json:
        """ body: dict
            Return: tuple with body and response (body, response) both are json strings"""
        try:
            body = dict(json.loads(json.dumps(body)))
            response = requests.post(self.api_url, json=body)
            print(f"found response = {response}...")
            response = json.dumps(response.json())
            body = json.dumps(body)
            return body, response
        except requests.exceptions.RequestException as e:
            print(f"Error making API call: {e}")
            return None, None
