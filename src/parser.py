import argparse

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-hh", "--host", help="host address")
    parser.add_argument("-u", "--username", help="username")
    parser.add_argument("-d", "--database", help="database name")
    parser.parse_args()