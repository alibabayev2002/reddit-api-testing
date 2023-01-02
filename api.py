import requests

class RedditApi:

    headers = {}

    def __init__(self,client_secret,client_id,username,password):
        auth = requests.auth.HTTPBasicAuth(client_id,client_secret)
        data = {
            'grant_type' : 'password',
            'username' : username,
            'password' : password
        }
        headers = {
            'User-Agent': 'MyAPI/0.0.1'
        }
        response = requests.post('https://www.reddit.com/api/v1/access_token',auth=auth,data=data,headers=headers)
        TOKEN = response.json()['access_token']
        self.headers['User-Agent'] = 'MyAPI/0.0.1'
        self.headers['Authorization'] = f'bearer {TOKEN}'

    def me(self):
        return requests.get('https://oauth.reddit.com/api/v1/me',headers=self.headers)

    def all_res(self):
        return requests.get('https://oauth.reddit.com/r/all/top',headers=self.headers)

    def games(self):
        return requests.get('https://oauth.reddit.com/r/games/top?top=all',headers=self.headers)

    def friends(self):
        return requests.get('https://oauth.reddit.com/api/v1/me/friends',headers=self.headers)

    def friend(self,friend):
        return requests.get(f'https://oauth.reddit.com/api/v1/me/friends/{friend}',headers=self.headers)

    def comment(self,thing_id,text):
        data = {
            "api_type" : "json",
            "text" : text,
            "thing_id" : thing_id
        }
        return requests.post('https://oauth.reddit.com/api/comment',headers=self.headers,data=data)

    def blocked(self):
        return requests.get('https://oauth.reddit.com/prefs/blocked',headers=self.headers)



