class u_table():

    def __init__(self, name, rows):
        self.name = name
        self.rows = rows

    def get_rows(self):
        return self.rows

    def get_row(self, name):
        self.get_rows()[name]