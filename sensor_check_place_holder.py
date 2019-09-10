import time


def check1():
    time.sleep(1)
    return True


def check2():
    time.sleep(1)
    return ValueError("ERROR: no sensor detected")


def check3():
    time.sleep(1)
    return True


def check4():
    time.sleep(1)
    return True


def check5():
    time.sleep(1)
    return True


def check6():
    time.sleep(1)
    return False


def check7():
    time.sleep(1)
    return False


def check8():
    time.sleep(1)
    return False


def check9():
    time.sleep(1)
    return False


def check10():
    time.sleep(1)
    return False


check_functions = [check1, check2, check3, check4, check5, check6, check7, check8, check9, check10]
