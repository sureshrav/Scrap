import urllib
import json
import time, os

MAGIC_START_POINT = 17000



SOURCE_CODE_BEGIN = '<pre class="prettyprint program-source" style="padding: 0.5em;">'
SUBMISSION_URL = 'http://codeforces.com/contest/739/submission/22456453'



replacer = {'&quot;': '\"', '&gt;': '>', '&lt;': '<', '&amp;': '&', "&apos;": "'"}
keys = replacer.keys()

def parse(source_code):
    for key in keys:
        source_code = source_code.replace(key, replacer[key])
    return source_code


submission_info = urllib.urlopen(SUBMISSION_URL).read()



  
  
start_pos = submission_info.find(SOURCE_CODE_BEGIN, MAGIC_START_POINT) + len(SOURCE_CODE_BEGIN)
end_pos = submission_info.find("</pre>", start_pos)
result = parse(submission_info[start_pos:end_pos]).replace('\r', '')

print result

