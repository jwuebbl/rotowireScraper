import urllib.request
import urllib.parse
import Util
import re
import printUtil
import csvUtil


url = 'https://www.rotowire.com/hockey/nhl-lineups.php'
values = {'s':'python programming',
          'submit':'search'}
   
data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url, data)
resp = urllib.request.urlopen(req)
respData = resp.read().decode("utf8")

matchUps = re.findall(r'[A-Z][a-z]* {10,}', respData)
matchUps = Util.stripWhiteSpaceFromstrings(matchUps)
csvUtil.printMatchups(matchUps)
			