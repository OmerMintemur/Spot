import spotipy
import mysql.connector as db
import configparser as cp
from spotipy.oauth2 import SpotifyClientCredentials
import json
from Database import Database
from FileOp import FileOp
from Spot import Spot
from time import sleep

Config = cp.ConfigParser()
Config.read("tokens.config")

fileOP = FileOp()
likedsongs = fileOP.splitandreturnliked()
notlikedsongs = fileOP.splitandreturnnotliked()
# notrsongs = fileOP.splitandreturnednotr()
files = []

files.append(likedsongs)
files.append(notlikedsongs)
# files.append(notrsongs)



sp = Spot()
sp.createSpot(Config)

# client_credentials_manager = SpotifyClientCredentials(client_id=Config['Spotify']['clientId'],
#                                                       client_secret=Config['Spotify']['clientSecret'])
# sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

db = Database()
db.connectDatabase(Config)
db.control()

try:


    for i in range(2):
        result = sp.getfeatures(files[i])
        js = json.loads(result)
        db.insertalldata(js, i)

    db.getdataforlearning()
except Exception as e:
    print(e)
finally:
    print("Done")




