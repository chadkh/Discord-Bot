def isRegisteredUser():
    return False

def test():
    if isRegisteredUser():
        print('no')
        return
    print("Hello")

test()