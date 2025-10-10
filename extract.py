#to extract data from reddit api
def extraction():
    from dotenv import load_dotenv
    import os
    import requests
    load_dotenv()
    
    CLIENT_ID =os.getenv('CLIENT_ID')
    SECRET_KEYS=os.getenv('SECRET_KEYS')
    auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_KEYS)
    username = os.getenv('USERNAME')
    password= os.getenv('PASSWORD')
    data = {
        'grant_type': 'password',
        'username':f'{username}',
        'password':f'{password}'
    }

    headers = {'User-Agent':'MyAPI/0.0.1'}

    res = requests.post('https://www.reddit.com/api/v1/access_token',
                    auth=auth, data=data, headers=headers)

    TOKEN = res.json()["access_token"]

    headers = {**headers, **{'Authorization':f'bearer {TOKEN}'}}
    res = requests.post('https://www.reddit.com/api/v1/access_token',
                    auth=auth, data=data, headers=headers)
    res = requests.get('https://oauth.reddit.com/api/v1/me', headers=headers).json()
    
    raw_data = requests.get('https://oauth.reddit.com/r/Bitcoin/new', headers=headers, params={'limit':'20'}).json()
    return raw_data
