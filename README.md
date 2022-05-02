# **Discord oauth2 API (client)**

Is a simple API client for Discord oauth2 API. Based on python 3, and is available at pypi.org.

### Installation

```
pip install Discord-Oauth2-API
```

### Example 

```
from discord-oauth2-api import get_user_data


user_json = get_user_data.get_user_data(code = "", client_id = "", client_secret = "", redirect_uri = "")
user_data = user_json["data"]
user_refresh_token = user_json["refresh_token"]
print(data) 
print(refresh_token)
```

**VARIABLES** :

- ```code``` - The code from the querystring.
- ```client_id``` - Your application's client id.
- ```client_secret``` - Your application's client secret.
- ```redirect_uri``` - The ```redirect_uri``` associated with this authorization, usually from your authorization URL

More information about variables can be found here -> https://discord.com/developers/docs/topics/oauth2

## Info

- Recommended Python ver. >=3.8
- This is the **first package** by Matej Ruzicka. 

## Links

- Author's website -> https://vlakoznaltech.tk/
- Documentation -> Work in progres ;)

###### README.md ver. 1.0
