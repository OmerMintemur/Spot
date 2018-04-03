
class FileOp:
    @classmethod
    def readfile(cls):
        with open('SongsId.txt', 'r') as songs:
            return songs.readlines()

    @classmethod
    def split_and_return(cls):
        lines =cls.readfile()
        songs_id = []
        for line in lines:
           songs_id.append(line.split(":")[2])
        return list(set(songs_id))