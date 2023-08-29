#imports
import spotipy
import spotipy.util as util


# Auth info
client_id = ""
client_secret = ""
username = ""
redirect_uri = "http://localhost:3000"


def get_username():
    return username

# Generate access token
def get_token():
    scope = 'user-top-read,playlist-read-private,user-read-playback-state,playlist-modify-public,user-read-recently-played'
    token = util.prompt_for_user_token(username,
                                    scope,
                                    client_id=client_id,
                                    client_secret=client_secret,
                                    redirect_uri=redirect_uri)

    if token:
        sp = spotipy.Spotify(auth=token)
        print("Access token successfully generated! It will be valid for the next 2h.")
        return sp
    else:
        print("Can't get token for", username)
