
class FileOp:
    @classmethod
    def readfile(self):
        with open('SongsId.txt', 'r') as songs:
            return songs.readlines()

    @classmethod
    def split_and_return(self):
        lines = self.readfile(self)
        songs_id = []
        for line in lines:
           songs_id.append(line.split(":")[2])
        return list(set(songs_id))