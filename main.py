import spotipy
import mysql.connector as db
import configparser as cp
from spotipy.oauth2 import SpotifyClientCredentials
import json
from Database import Database
from FileOp import FileOp
from time import sleep

Config = cp.ConfigParser()
Config.read("tokens.config")

fileOP = FileOp()
songs = fileOP.split_and_return()


client_credentials_manager = SpotifyClientCredentials(client_id=Config['Spotify']['clientId'],
                                                      client_secret=Config['Spotify']['clientSecret'])
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

db = Database()
db.connectDatabase(Config)
db.control()



try:
    for song in songs:
        result = sp.audio_features(song.rstrip())
        result = json.dumps(result, sort_keys=True, indent=4)
        js = json.loads(result)
        db.insertData(js)
        sleep(5)
        print("Inserted")
except Exception as e:
    print(e)
finally:
    print("Done")


