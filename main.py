#!/usr/bin/python3
from src.parser import parse_arguments
from src.style.ascii import get_ascii

if __name__ == "__main__":
    parse_arguments()
    print(get_ascii())