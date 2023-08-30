# Spotify playlist creation
This python script uses Spotify's API to create a new Spotify playlist with songs that are recommended by Spotify, based on user's top tracks.

## Description
Spotify provides public API to enable developpers to work with Spotify's content and create custom applications.
This project uses some of the API calls to get the current user's most listened songs from 3 different time periods (long, medium and short term).
A few of these tracks are then randomly selected and passed as 'seeds' to Spotify's API call that makes recommendations.


## Requirements
In order to use this script, you need to:
- Have a Spotify account
- Create your developper app on https://developer.spotify.com/ and retrieve your client id and client secret
- Have python installed (all the libraries that are used in this project are listed in requirements.txt)

## Getting started
First, clone this repository.
Then, run the following command to install the required python libraries:

```sh
pip install -r requirements.txt
```

## Running the script locally
The steps to follow after you've installed the requirements:

1. Developper app creation to retrieve client id & client secret
- Go to https://developer.spotify.com/ and log in using your Spotify's credentials
- Click on your avatar in the top right > Dashboard > Create app
- Name your app, add a short description and the redirect uri (ex. http://localhost:3000) > Save
- You will land on your newly created Spotify app
- Go to Settings and copy the client id and the client secret

2. Update the user's credentials

- Open the auth.py file and update the lines 7-10 with your credentials > Save the changes

3. Execute the main script

- Run the main.py that will create your new Spotify playlist
```bash
python main.py
```

4. Check out the results
- Open your Spotify and find the new playlist
