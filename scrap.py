import urllib
import json
import time, os

MAGIC_START_POINT = 110000

SUBMISSION_URL = 'http://codeforces.com/problemset/status/735/problem/C'

SOURCE_CODE_BEGIN = 'var viewableSubmissionIds = ['




submission_info = urllib.urlopen(SUBMISSION_URL).read()





  
start_pos = submission_info.find(SOURCE_CODE_BEGIN, MAGIC_START_POINT) + len(SOURCE_CODE_BEGIN)
end_pos = submission_info.find("];", start_pos)
result = submission_info[start_pos:end_pos].replace("\"","").replace("\r","").replace("\n","").replace(" ","")

arr=result.split(",")


print arr




