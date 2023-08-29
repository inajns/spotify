#imports
import pandas as pd
import random

def get_recommendations(sp, tracks_df):
    print("Reccommending songs...")
    #Create an empty dictionary to store recommanded songs (uri, name, artist)
    rec_songs = {
            "uri":[],
            "name":[],
            "artist":[]
    }

    #Loop over 10 times to get 50 recommendend tracks based on a few user's favorites artists and tracks (limit per API call is 5 seeds)
    for i in range(0,10):

        #Generate 2 random artists from user's top tracks
        artists_random = []
        random_indexes = random.sample(range(0, len(tracks_df)), 2)
        for index in random_indexes:
            artist_uri = tracks_df.loc[index,'artist_uri']
            artists_random.append(artist_uri)


        #Generate 2 random tracks from user's top tracks
        tracks_random = []
        random_indexes = random.sample(range(0, len(tracks_df)), 2)
        for index in random_indexes:
            track_uri = tracks_df.loc[index,'track_uri']
            tracks_random.append(track_uri)


        #Get recommandations from spotify API
        rec = sp.recommendations(seed_artists=artists_random,
                        seed_genres=None,
                        seed_tracks= tracks_random,
                        limit=5)


        #Extract uri, song name and song artist and add to rec_songs dictionary
        for song in rec['tracks']:
            if song['artists'][0]['name'] != '':
                uri = song['uri']
                name = song['name']
                artist = song['artists'][0]['name']
                rec_songs['uri'].append(uri)
                rec_songs['name'].append(name)
                rec_songs['artist'].append(artist)

    #Create a dataframe with recommended songs
    rec_songs_df = pd.DataFrame(rec_songs)
    rec_tracks = rec_songs['uri']
    print(f"Successfully generated {len(rec_tracks)} recommended songs!")
    return rec_tracks
