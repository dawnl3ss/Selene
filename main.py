#!/usr/bin/python3
import sys
from src.parser import parse_arguments
from src.struct.dump import dump
from src.struct.type.u_table import u_table
from src.struct.type.dataset import dataset
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

    cursor_table.execute("SHOW TABLES")
    structure = dump()

    for data in cursor_table:

        for table in data:
            cursor_rows.execute(f"SELECT * FROM {table}")

            for rows in cursor_rows:
                i = 0
                u_tab = u_table(table, {})
                for p_row in rows:
                    u_tab.add_row(dataset(p_row))
                    i+=1
            structure.add_table(u_tab)

    print(structure.get_table("faq").get_rows())


if __name__ == "__main__":
    parse_arguments()
    main(arguments=(sys.argv[2], sys.argv[4], sys.argv[6]))
