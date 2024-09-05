def StupidRecursion():
    StupidRecursion()
try:
    StupidRecursion()
except RecursionError:
    print("OMG Your python restricted hold that much stupid functions")
else:
    print("DIRTY CHEATER!! TURN IT OFF AND TRY AGAIN!!")
finally:
    print("Read the text above idk...")