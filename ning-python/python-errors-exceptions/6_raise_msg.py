#!/usr/bin/python3

def raise_message(message=""):
    raise NameError("I love Python!")


if __name__ == "__main__":

    try:
        raise_message("I love Python.")
    except NameError as ne:
        print(ne)
