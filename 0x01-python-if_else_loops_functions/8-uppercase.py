#!/usr/bin/python3
def islower(x):
    if ord(x) >= ord('a') and ord(x) <= ord('z'):
        return True
    else:
        return False


    def uppercase(str):
        for x in str:
            print("{:c}"
                    .format(ord(x) if not islower(x) else ord(x) - 32),
                    end="")
        print("")
