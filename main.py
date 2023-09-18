#!/usr/bin/python3
import sys
from src.parser import parse_arguments
from src.style.ascii import get_ascii
from src.sql.sql_manager import sql_manager

def main(arguments):
    host, user, database = arguments
    print("☾ Starting Selene dumper...")
    print(get_ascii())
    print("✦ Best database dumper written by Dawnl3ss.")
    print("✦ This tool is only design for educationnal and ethical purpose. I am not responsible for your usage.")
    print("✦ Github : https://github.com/dawnl3ss")
    print(" ")
    password = input(f" MySQL {user}'s password : ")

    manager = sql_manager(host, user, password, database)
    cursor_table = manager.connect_db().cursor()
    cursor_table.execute(f"USE {database}")
    cursor_rows = manager.connect_db().cursor()
    cursor_rows.execute(f"USE {database}")

    # get toutes les tables
    cursor_table.execute("SHOW TABLES")

    for data in cursor_table:
        for table in data:
            print("Table : \n")
            cursor_rows.execute(f"SELECT * FROM {table}")

            for rows in cursor_rows:
                print(rows)


if __name__ == "__main__":
    parse_arguments()
    main(arguments=(sys.argv[2], sys.argv[4], sys.argv[6]))
