from __future__ import unicode_literals
import requests
import itchat
import time
from threading import Timer


def get_news():
    url = "http://open.iciba.com/dsapi"
    r = requests.get(url)
    contents = r.json()['content']
    return contents
def get_weather():
    weatherJsonUrl = "http://wthrcdn.etouch.cn/weather_mini?city=长沙"
    response = requests.get(weatherJsonUrl)
    w = response.json()
    return w

def send_news():
    try:
        # 登陆你的微信账号，会弹出网页二维码，扫描即可
        itchat.auto_login(enableCmdQR=1,hotReload=True)
        # 获取你对应的好友备注，这里的小明我只是举个例子
        # 改成你最心爱的人的名字。
        my_friend = itchat.search_friends(name=u'张云柯')
        # 获取对应名称的一串数字
        XiaoMing = my_friend[0]["UserName"]
        # 获取金山字典的内容
        w = get_weather()['data']

        message1 = str(get_news())
        message2 = "地点：%s" % w['city']+"日期：" + w['forecast'][0]['date']+""+"\n温度：最" + w['forecast'][0]['low'] + '℃~最' + w['forecast'][0]['high'] + '℃'+"\n天气：" + w['forecast'][0]['type']+"\n今>日着装：" + w['ganmao']
        message3 = "来自最爱你的猪"
        # 发送消息
        # itchat.send(message1, toUserName=XiaoMing)
        # itchat.send(message2, toUserName=XiaoMing)
        # itchat.send(message3, toUserName=XiaoMing)
        # 每86400秒（1天），发送1次，
        # 不用linux的定时任务是因为每次登陆都需要扫描二维码登陆，
        # 很麻烦的一件事，就让他一直挂着吧
        t = Timer(86400.0, send_news)
        t.start()
    except:
        message4 = u"今天最爱你的人出现了 bug /(ㄒoㄒ)/~~"
        print(message4)
        #itchat.send(message4, toUserName=XiaoMing)

def main():
    t = Timer(10.0,send_news)
    t.start()

if __name__ == '__main__':
    main()
