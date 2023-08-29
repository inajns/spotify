#imports
import pandas as pd


def get_top_tracks(sp):
#Create a dictionary for songs, artists and their uris
    tracks_dict = {
        "name": [],
        "track_uri": [],
        "artist": [],
        "artist_uri": []
    }
    #Create a list of values for time_range parameter
    time_range_list = ['short_term','medium_term', 'long_term']

    #Get the top tracks for the current user, for each time_range and append the tracks dictionary
    for time_range in time_range_list:
        top_tracks_api = sp.current_user_top_tracks(limit=20, offset=0, time_range=time_range)

        for i in top_tracks_api['items']:
            if i['name'] not in tracks_dict['name']:
                tracks_dict["name"].append(i["name"])
                tracks_dict["track_uri"].append(i['uri'])
                tracks_dict["artist"].append(i['artists'][0]['name'])
                tracks_dict["artist_uri"].append(i['artists'][0]['uri'])

    # Create a dataframe from tracks_dict
    tracks_df = pd.DataFrame(tracks_dict)
    print(f"Successfully retrieved {len(tracks_df)} of your top tracks!")
    return tracks_df
