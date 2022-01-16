import urllib.request
import urllib.parse
from webbrowser import get
import Util
import re
import printUtil
import csvUtil

def getMatchups(respData):
    matchups = re.findall(r'[A-Z][a-z]* {10,}', respData)
    matchups = Util.stripWhiteSpaceFromstrings(matchups)
    return matchups


url = 'https://www.rotowire.com/hockey/nhl-lineups.php'
values = {'s':'python programming',
          'submit':'search'}
   
data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url, data)
resp = urllib.request.urlopen(req)
respData = resp.read().decode("utf8")

matchups = getMatchups(respData)
csvUtil.printMatchups(matchups)
			