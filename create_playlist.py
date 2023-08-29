# Create a playlist
def create_playlist(sp,username, playlist_name, playlist_description):
    print("Creating a new playlist...")
    sp.user_playlist_create(user = username,
                        name = playlist_name,
                        public=True,
                        collaborative=False,
                        description= playlist_description
                    )
    print("Playlist created!")


# Add tracks to the playlist
def add_tracks(sp,tracks):
    print("Adding songs...")
    playlist_id = sp.current_user_playlists()['items'][0]['id']
    sp.playlist_add_items(playlist_id=playlist_id,items = tracks)
    print("Recommended songs added to playlist! Open your Spotify account and check it out!")
