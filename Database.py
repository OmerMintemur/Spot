import mysql.connector as db

class Database:

    def __init__(self,Config):
        self.__con = db.connect(host=Config['Database']['host'], database=Config['Database']['database'],
                                user=Config['Database']['user'], password=Config['Database']['password'])
        self.__cursor = self.__con.cursor(buffered=True)

    # @classmethod
    # def connectDatabase(self,Config):
    #
    #     self.__con = db.connect(host=Config['Database']['host'], database=Config['Database']['database'],
    #                      user=Config['Database']['user'], password=Config['Database']['password'])
    #     self.__cursor = self.__con.cursor(buffered=True)

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

    def insertData(self, data):
        stmt = "INSERT INTO track_info(acousticness,analysis_url,danceability,duration_ms,energy,id,instrumentalness,music_key," \
               "liveness,loudness,music_mode,speechiness,tempo,time_signature,track_href,music_type,uri,valence)" \
               "VALUES (%s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
        self.__con.cursor().execute(stmt, self.organizedData(data))
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

