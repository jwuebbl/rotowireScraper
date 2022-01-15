def stripWhiteSpaceFromstrings(inputList):
    outputList = []
    for s in inputList:
        s = s.strip()
        outputList.append(s)
    return outputList