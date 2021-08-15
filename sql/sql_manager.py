#!/usr/bin/python3
import pymysql
import json

class sql_manager():

    def __init__(self):
        json_settings_data = json.load(open("settings.json"))
        self.username = json_settings_data["sql_ids"]["username"]
        self.password = json_settings_data["sql_ids"]["password"]
        self.host = json_settings_data["sql_ids"]["host"]
        self.db = json_settings_data["sql_ids"]["database"]
        self.target_table = json_settings_data["settings"]["target_table"]

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