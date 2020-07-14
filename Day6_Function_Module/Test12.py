def printOut():
    print("This is the function in Test.py")

if __name__ == "Test12":
    print("This will run when being imported as a module.")
    printOut()

if __name__ == "__main__":
    print("This will run when being treated as a main file.")
    print("You are testing this Test12.py file.")