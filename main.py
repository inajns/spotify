#imports
from datetime import datetime
from auth import get_token, get_username
from top_tracks import get_top_tracks
from recommendations import get_recommendations
from create_playlist import create_playlist, add_tracks

username = get_username()
sp = get_token()
tracks_df = get_top_tracks(sp)
rec_tracks = get_recommendations(sp, tracks_df)

create_playlist(sp,
                username = username,
                playlist_name = f"Suggested songs for today {datetime.now().strftime('%d_%m_%y')}",
                playlist_description = "Spotify & my script think you may like these")

add_tracks(sp,rec_tracks)
