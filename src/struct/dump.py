class dump():

    def __init__(self):
        self.tables = {}

    def add_table(self, table):
        self.tables[table.get_name()] = table

    def get_tables(self):
        return self.tables

    def get_table(self, name):
        return self.tables[name]