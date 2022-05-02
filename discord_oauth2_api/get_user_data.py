import requests


def get_user_data(code, client_id, client_secret, redirect_uri):
    data = {
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': redirect_uri,
        'scope': 'identify' 
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    
    r = requests.post(f'https://discord.com/api/v6/oauth2/token', data=data, headers=headers)
    
    access_token = r.json()["access_token"]
    refresh_token = r.json()["refresh_token"]

    ####################################

    url = "https://discord.com/api/users/@me"

    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    r = requests.get(url = url, headers = headers)
    user_json = r.json()

    user_data = {
        'data': user_json,
        'refresh_token': refresh_token
    }
    
    return(user_data)
