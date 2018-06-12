import mysql.connector as db
import json
class Database:


    attributes = ['acousticness','analysis_url','danceability','duration_ms','energy','id','instrumentalness',
            'music_key','liveness', 'loudness', 'music_mode', 'speechiness', 'tempo', 'time_signature', 'track_href',
            'music_type', 'uri', 'valence']
    @classmethod
    def connectDatabase(self, Config):

        self.__con = db.connect(host=Config['Database']['host'], database=Config['Database']['database'],
                         user=Config['Database']['user'], password=Config['Database']['password'])
        self.__cursor = self.__con.cursor(buffered=True)

    @classmethod
    def control(self):
        if self.__con.is_connected():
            print("I am connected")

    @classmethod
    def organizedData(self, data):
        temp_list = []
        for items in data[0]:
            temp_list.append(data[0][items])
        return tuple(temp_list)

    @classmethod
    def insertData(self, data):
        stmt = "INSERT INTO track_info(acousticness,analysis_url,danceability,duration_ms,energy,id,instrumentalness,music_key," \
               "liveness,loudness,music_mode,speechiness,tempo,time_signature,track_href,music_type,uri,valence)" \
               "VALUES (%s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
        self.__con.cursor().execute(stmt, self.organizedData(data))
        self.__con.commit()

    @classmethod
    def preparedata(self, data,i):
        full_list = []
        for x in range(len(data)):
            tup = (data[x]["acousticness"], data[x]["analysis_url"], data[x]["danceability"], data[x]["duration_ms"],
                   data[x]["energy"], data[x]["id"], data[x]["instrumentalness"], data[x]["key"], data[x]["liveness"],
                   data[x]["loudness"], data[x]["mode"], data[x]["speechiness"], data[x]["tempo"], data[x]["time_signature"],
                   data[x]["track_href"], data[x]["type"], data[x]["uri"], data[x]["valence"], i)
            full_list.append(tup)
        return full_list

    def insertalldata(self, data, i):
        new_data = self.preparedata(data, i)
        stmt = "INSERT INTO track_info(acousticness,analysis_url,danceability,duration_ms,energy,id,instrumentalness,music_key," \
               "liveness,loudness,music_mode,speechiness,tempo,time_signature,track_href,music_type,uri,valence,songliked)" \
               "VALUES (%s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
        self.__con.cursor().executemany(stmt, new_data)
        self.__con.commit()

    def selectAllData(self):
        try:
            stmt = "SELECT * FROM track_info"
            self.__cursor.execute(stmt)
            returnedData = self.__cursor.fetchall()
            for row in returnedData:
                print(row)
        except Exception as e:
            print(e)
    def getonesongattribute(self, id):
        stmt = "SELECT * FROM track_info WHERE id='%s';"%(id)
        self.__cursor.execute(stmt)
        returnedData = self.__cursor.fetchone()
        if returnedData is None:
            print("There is no song for that id")
            return
        return self.returnonedatajson(returnedData)

    def returnonedatajson(self, data):
        js = {
            self.attributes[0]: data[1], self.attributes[1]: data[2], self.attributes[2]: data[3],
            self.attributes[3]: data[4], self.attributes[4]: data[5], self.attributes[5]: data[6],
            self.attributes[6]: data[7], self.attributes[7]: data[8], self.attributes[8]: data[9],
            self.attributes[9]: data[10], self.attributes[10]: data[11], self.attributes[11]: data[12],
            self.attributes[12]: data[13], self.attributes[13]: data[14], self.attributes[14]: data[15],
            self.attributes[15]: data[16], self.attributes[16]: data[17], self.attributes[17]: data[18],
        }
        return json.dumps(js, sort_keys=True, indent=4)

    def getdataforlearning(self):
        files=["liked.txt", "notliked.txt"]
        for x in range(len(files)):
            stmt = "SELECT * FROM track_info WHERE songliked=%s;"%(x)
            self.__cursor.execute(stmt)
            returnedData = self.__cursor.fetchall()
            with open(files[x], 'w') as file:
                for data in returnedData:
                    file.write(str(data[1])+"\t" +
                               str(data[3])+"\t" +
                               str(data[5])+"\t" +
                               str(data[9])+"\t" +
                               str(data[10])+"\t" +
                               str(data[12])+"\t" +
                               str(data[13])+"\t" +
                               str(data[18])+"\t" +
                               str(data[19])+"\n")





