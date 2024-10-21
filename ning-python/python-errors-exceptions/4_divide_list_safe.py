#!/bin/usr/python3

def divide_list_safe(list_1, list_2, list_len):

    result = []

    for index in range(list_len):
        try:
            value_1 = list_1[index]
            value_2 = list_2[index]
            result.append(value_1 / value_2)
        except TypeError:
            result.append(0)
            print("wrong type")
        except IndexError:
            result.append(0)
            print("out of range")
        except ZeroDivisionError:
            result.append(0)
            print("division by 0")
        finally:
            pass
    return result


if __name__ == "__main__":

    list_1 = [9, 2, 6]
    list_2 = [3, 2, 2]
    res = divide_list_safe(list_1, list_2, max(len(list_1), len(list_2)))
    print(res)
    print(10*"_")
    print()
    list_1 = [9, 2, 6, 10]
    list_2 = ["one", 0, 1, 2, 7]
    res = divide_list_safe(list_1, list_2, max(len(list_1), len(list_2)))
    print(res)



