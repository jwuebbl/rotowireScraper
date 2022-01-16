import csv
import datetime

def getDate():
    x = datetime.datetime.now()
    x = x.strftime("%x") 
    x = x.replace("/", "-")
    return x

def printMatchups(matchUps):
    fileName = "./csv/matchups-" + getDate() + ".csv"
    f = open(fileName, 'w')
    # Away was listed first on the rotowire website. Therefor every other team will be an away team.
    away = True
    for team in matchUps:
        if away == True:
            output = team + ","
            away = False
        else:
            output = output + team + '\n'
            away = True
            f.write(output)
    
