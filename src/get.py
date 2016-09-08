import time
import requests
import json

datas = {}
output = open('data.pkl', 'a')

while True:
    url = "https://h5.yeamoney.cn/turntable/yealove"
    try:
        r = requests.get(url)
        if not r.ok:
            raise Exception("Get Failed")
        res_dict = eval(r.text)
        data = {'allUser': res_dict['allUser']}
        for one in res_dict['stat']:
            data[one['_id']['金额']] = one['count']
        now = time.localtime()
        str_time = time.strftime("%Y-%m-%d %H:%M:%S", now)
        str_data = json.dumps(data)
        output.write(str_time + '\t' + str_data + '\n')
        print(str_time)
        output.flush()
    except Exception as e:
        print(e)
        time.sleep(1)
    time.sleep(10 * 60)
