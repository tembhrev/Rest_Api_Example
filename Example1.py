import requests
import datetime
import time
import json

from requests.packages import urllib3
urllib3.disable_warnings()

token_url = 'URL for TOKEN ENDPOINI https://login.microsoftonline.com/{ID}/oauth2/token'
graph_url = 'https://graph.microsoft.com/v1.0/users'

auth_token = {}
def GET_Token():
    post_data = {'resource': 'https://graph.microsoft.com',
                 'client_id': 'YOUR APPLICATION ID',
                 'client_secret' :'YOUR CLIENT SECRET KEY',
                 'grant_type': 'client_credentials'}

    r = requests.post(token_url, data = post_data)
    if r.status_code == requests.codes.ok:
        print(r.status_code)
        r = requests.post(token_url, data = post_data)
        d = r.json()
        auth_token['authorization'] = d['access_token']
        print("Token Created")
    else:
        d = r.json()
        error_msg = d['error_description']
        raise Exception(error_msg)
        
    
def GET():       
    r = requests.get(graph_url, headers = auth_token)
    if r.status_code == requests.codes.ok:
        data = r.json()
        print(data)

    else:
        json_response = json.loads(r.text)
        error_msg = json_response["error"]["message"]
        raise Exception(error_msg)

if __name__ == "__main__":
    GET_Token()
    GET()


    


