import mysql.connector

class Config:

    def __init__(self):
        self.__host = "localhost"
        self.__username = "root"
        self.__password = ""
        self.__database = "sisfo-covid"
        self.buatKoneksi()

    def buatKoneksi(self):
        db = mysql.connector.connect(
            host = self.__host,
            user = self.__username,
            password = self.__password,
            database = self.__database
        )
        self.__db = db

    def create(self, nama, username, password, role, departement):
        self.nama = nama
        self.username = username
        self.password = password
        self.role = role
        self.departement = departement
        cursor = self.__db.cursor()
        val = (nama, username, password, role, departement)
        cursor.execute("INSERT INTO user (nama, username, password, role, departement) VALUES (%s, %s, %s, %s, %s)", val)
        self.__db.commit()

    def read(self):
        cursor = self.__db.cursor()
        sql = "SELECT nama, username FROM user"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result