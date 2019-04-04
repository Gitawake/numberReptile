from requests_html import HTMLSession
import json

# 实例化HTMLSession...
session = HTMLSession()
file_handle = open('number.txt', mode='a')
# for循环手机号码...
for i in range(4020, 10000):
    if i >= 1000:
        number = '134' + str(i) + '0068'
    elif i >= 100:
        number = '1340' + str(i) + '0068'
    elif i >= 10:
        number = '13400' + str(i) + '0068'
    else:
        number = '134000' + str(i) + '0068'
    print(number)
    # 定义需要请求的url...
    r = session.get('http://mobsec-dianhua.baidu.com/dianhua_api/open/location?tel=' + number)
    # 元素定位...
    Location = r.html
    # 解析返回值...
    print(Location.text)
    number_null = json.loads(Location.text)['response'][number]
    if number_null is None:
        print('该号码数据为null...')
    else:
        city = json.loads(Location.text)['response'][number]['detail']['area'][0]['city']
        print(city)
        # 判断city
        City = '深圳'
        if city == City:
            file_handle.write(number + '\n')
            print('value为' + City + '保存手机号码...')
        else:
            print('value不是' + City + '继续for循环...')
file_handle.close()


