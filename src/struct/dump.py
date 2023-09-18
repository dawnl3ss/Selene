class dump():

    def __init__(self, tables):
        self.tables = tables

    def get_tables(self):
        return self.tables

    def get_table(self, name):
        return self.get_tables()[name]