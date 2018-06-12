from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import json

class Spot:
    def __init__(self):

        self.__sp = None

    @classmethod
    def createSpot(self, Config):
        self.__client_manager = SpotifyClientCredentials(client_id=Config['Spotify']['clientId'],
                                                         client_secret=Config['Spotify']['clientSecret'])
        self.__sp = spotipy.Spotify(client_credentials_manager=self.__client_manager)


    @classmethod
    def getfeatures(self, data):
        result = self.__sp.audio_features(data)
        return json.dumps(result, sort_keys=True, indent=4)
        # return json.loads(result)



