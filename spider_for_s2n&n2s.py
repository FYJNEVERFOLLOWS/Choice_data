import requests
import json
import time
import datetime

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}

url1 = 'http://push2.eastmoney.com/api/qt/kamtbs.rtmin/get?fields1=f1,f2,f3,f4&fields2=f51,f54,f58,f62&ut=b2884a393a59ad64002292a3e90d46a5'
json_str1 = requests.get(url1, headers=headers)
# print(json_str1.text)

result_json1 = json.loads(json_str1.text)

# json文件中value依次是沪港通、深股通、北向资金 或 港股通（沪）、港股通（深）、南向资金
result_s2n = json.dumps(result_json1["data"]["s2n"])
result_n2s = json.dumps(result_json1["data"]["n2s"])

# f1 = open('{}-{}_s2n.json'.format(datetime.datetime.today().year, result_json1["data"]["s2nDate"]), 'w')
# f1.write(result1)
# f1.close()

print(result_s2n)
print(result_n2s)


