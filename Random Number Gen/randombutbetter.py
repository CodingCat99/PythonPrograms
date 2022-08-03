from multiprocessing.sharedctypes import Value
import random as rng

# Main Function
def ranGen(min, max, willWrite: bool, willRound: bool, isStr: bool):
    genRanNum = rng.uniform(min, max)
    if willRound == True:
        rounded_genRanNum = round(genRanNum)
        genRanNum = rounded_genRanNum
    if isStr == True:
        str_genRanNum = str(genRanNum)
        genRanNum = str_genRanNum
    if willWrite == True and isStr == False:
        output = open("output.txt", "w+")
        output.write(str(genRanNum))
        return genRanNum
    elif willWrite == True and isStr == True:
        output = open("output.txt", "w+")
        output.write(genRanNum)
        return genRanNum
    else:
        return genRanNum
ranGen(1,10,True,True,False)