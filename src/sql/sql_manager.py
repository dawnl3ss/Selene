#!/usr/bin/python3
import pymysql

class sql_manager():

    def __init__(self, host, username, password, db):
        self.host = host
        self.username = username
        self.password = password
        self.db = db

    def get_host(self) -> str :
        return self.host

    def get_username(self) -> str :
        return self.username

    def get_password(self) -> str :
        return self.password

    def get_db(self) -> str :
        return self.db

    def connect_db(self):
        return pymysql.connect(
            host = self.get_host(),
            user = self.get_username(),
            password = self.get_password(),
            database = self.get_db()
        )

    def check_database(self):
        try:
            cursor = pymysql.connect(
                host = self.get_host(),
                user = self.get_username(),
                password = self.get_password()).cursor()
            cursor.execute("SHOW DATABASES")

            for data in cursor:
                if data[0] == self.db:
                    return True
            return False
        except pymysql.err.OperationalError:
            print(" ")
            print(f"✦ Selene can not connect to mysql service. Maybe wrong information given. Closing Selene...")
            print(" ")
            return exit(-1)