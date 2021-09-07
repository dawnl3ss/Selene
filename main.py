#!/usr/bin/python3
from sql.sql_manager import sql_manager
import json

manager = sql_manager()

def main():
    cursor = manager.connect_db().cursor()
    cursor.execute("SELECT * FROM %s" % (manager.target_table))

    if json.load(open("settings.json"))["settings"]["result_display_method"] == "file":
        file = open("result.txt", "w")
        file.write("-==== {} TABLE BUMP START ====-\n\n".format(manager.target_table.upper()))

        for data in cursor:
            file.write(str(data))
            file.write("\n")
        file.write("\nProcess finished with exit code 0")
        file.close()
        print("Data has been successfully written in the file 'result.txt'")
    elif json.load(open("settings.json"))["settings"]["result_display_method"] == "console":
        print("-==== {} TABLE BUMP START ====-\n".format(manager.target_table.upper()))
        
        for data in cursor:
            print(str(data))
    else: print("Wrong display method given.")

if __name__ == "__main__":
    main()
