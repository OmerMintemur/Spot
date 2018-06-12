import configparser as cp
class FileOp:
    @classmethod
    def readfile(cls, control=-2):
        if(control is -2):
            return print("No options specified")
        elif control is 1:
            Config = cp.ConfigParser()
            Config.read("tokens.config")
            with open(Config['File']['likedSong'], 'r') as songs:
                return songs.readlines()
        elif control is 0:
            Config = cp.ConfigParser()
            Config.read("tokens.config")
            with open(Config['File']['notLikedSong'], 'r') as songs:
                return songs.readlines()
        else:
            Config = cp.ConfigParser()
            Config.read("tokens.config")
            with open(Config['File']['notrSong'], 'r') as songs:
                return songs.readlines()

    @classmethod
    def splitandreturnliked(cls):
        lines = cls.readfile(1)
        songs_id = []
        for line in lines:
           songs_id.append(line.split(":")[2].rstrip())
        return list(set(songs_id))

    @classmethod
    def splitandreturnnotliked(cls):
        lines = cls.readfile(0)
        songs_id = []
        for line in lines:
            songs_id.append(line.split(":")[2].rstrip())
        return list(set(songs_id))

    @classmethod
    def splitandreturnednotr(cls):
        lines = cls.readfile(-1)
        songs_id = []
        for line in lines:
            songs_id.append(line.split(":")[2].rstrip())
        return list(set(songs_id))
