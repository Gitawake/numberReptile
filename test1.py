import aiohttp
import asyncio
from bs4 import BeautifulSoup


class Book(object):
    def __init__(self, i, n, u):
        self.index = i
        self.name = n
        self.url = u


async def main():
    """
    起点中文网爬取小说分类
    :return:
    """

    '''实例化aiohttp'''
    async with aiohttp.ClientSession() as session:
        y = 0
        xx = []
        for params in range(1, 6):
            params = 'page=' + str(params)
            '''请求起点中文网网站数据'''
            async with session.get('https://www.qidian.com/finish', params=params) as resp:
                '''判断接口状态码是否正常'''
                if resp.status == 200:
                    '''定义网站数据展示类型'''
                    html = await resp.text()
                    '''使用指定的库开始解析数据'''
                    soup = BeautifulSoup(html, "lxml")
                    '''开始查找指定元素下的子节点'''
                    soup = soup.find(class_='all-img-list cf')
                    soup2 = soup.find_all('h4')

                    for soup2 in soup2:
                        y = y + 1

                        # print('{}.{}'.format(y, soup2.text), end=' ')
                        soup1 = soup2.contents
                        b = Book(y, soup2.text, 'https:{}'.format(soup1[0].get('href')))

                        xx.append(b)
                        # for soup1 in soup1:
                        #     print('https:{}'.format(soup1.get('href')))

                else:
                    print('接口状态码异常:{}'.format(resp.status))
        print(type(xx[0]))


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
