import inspect

if __name__ == "__main__":
    x = False
    assert x == True
    print(inspect.signature(print))