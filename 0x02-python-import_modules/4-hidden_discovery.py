#!/usr/bin/python3
if __main__ == "__main__":
    """Print all hidden directories"""
    import hidden_4

    for x in dir(hidden_4):
        if x[:2] != "__":
            print(x)