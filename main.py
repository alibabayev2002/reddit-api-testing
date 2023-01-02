import api
import yaml

with open('env.yml', 'r') as file:
    config = yaml.safe_load(file)

CLIENT_ID = config['CLIENT_ID']
CLIENT_SECRET = config['CLIENT_SECRET']
USERNAME = config['USERNAME']
PASSWORD = config['PASSWORD']


redditApi = api.RedditApi(CLIENT_ID,CLIENT_SECRET,USERNAME,PASSWORD)


def check_me_api(assertTrue = 1):
    response = redditApi.me();
    return (response.status_code == 200) == assertTrue


def check_friends_api(assertTrue = 1):
    response = redditApi.friends()
    return (response.status_code == 200) == assertTrue


def check_friend_api(friend_name = "test",assertTrue =1):
    response = redditApi.friend(friend=friend_name)
    return (response.status_code == 200) == assertTrue



def check_games_api(assertTrue = 1):
    response = redditApi.games()
    return (response.status_code == 200) == assertTrue


def check_all_res_api(assertTrue = 1):
    response = redditApi.all_res()
    return (response.status_code == 200) == assertTrue


def check_comment_post_api(assertTrue = 1,thing_id = 1,text = ""):
    response = redditApi.comment(thing_id,text)
    return (response.status_code == 200) == assertTrue


def check_blocked_api(assertTrue = 1):
    response = redditApi.blocked()
    return (response.status_code == 200) == assertTrue
    



# print(res.json())