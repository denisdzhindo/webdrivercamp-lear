#!/usr/bin/python3

def int_print(value):
    try:
        if int(value) == value:
            print(f"{value:d}")
            return True        
        else:
            return False
    except Exception as e:
        return False


if __name__ == "__main__":
    value = 42
    if not (int_print(value)):
        print(f"{value} is not an integer")
    value = -100
    if not (int_print(value)):
        print(f"{value} is not an integer")
    value = "Webdriver Camp"
    if not (int_print(value)):
        print(f"{value} is not an integer")
    value = True # ^^
    if not(int_print(value)):
        print(f"{value} is not an integer")
