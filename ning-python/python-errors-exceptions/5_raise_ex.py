#!/usr/bin/python3

def raise_ex():
    raise TypeError("")

if __name__ == "__main__":

    try:
        raise_ex()
    except TypeError as te:
        print("Exception raised")




