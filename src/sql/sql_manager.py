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