import requests
import yaml
import json
from skill_tagging.settings import BASE_DIR

cred_file = BASE_DIR + '/tag_skill/resources/config'
with open(cred_file) as json_file:
    api_cred = json.load(json_file)

OAuth_url = api_cred['OAuth_url']
extract_url = api_cred['extract_url']


def extract_skills(clean_data):
    access_token = getAccessKey()
    payload = {"full_text": clean_data}
    payload = json.dumps(payload)
    print(payload)
    headers = {
        'authorization': "Bearer {}".format(access_token),
        'content-type': "application/json"
    }
    response = requests.request("POST", extract_url, data=payload, headers=headers)
    return response.text


def getAccessKey():
    payload = "client_id=cku0nv5hgf93lb8q&client_secret=DU9z7EAS&grant_type=client_credentials&scope=emsi_open"
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.request("POST", OAuth_url, data=payload, headers=headers)
    return_dict = yaml.load(response.text, yaml.FullLoader)
    return return_dict.get('access_token')
