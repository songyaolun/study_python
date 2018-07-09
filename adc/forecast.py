#!python3
# coding:utf-8
import json, sys, requests

# 下载天气JSON
weatherJsonUrl = "http://wthrcdn.etouch.cn/weather_mini?city=长沙"
response = requests.get(weatherJsonUrl)
try:
    response.raise_for_status()
except:
    print("网址请求出错")

# 将json文件格式导入成python的格式
weatherData = json.loads(response.text)

w = weatherData['data']
print("地点：%s" % w['city'])

# 输出
print("日期：" + w['forecast'][0]['date'])
print("\t温度：最" + w['forecast'][0]['low'] + '℃~最' + w['forecast'][0]['high'] + '℃')
print("\t天气：" + w['forecast'][0]['type'])
print("")

print("\n今日着装：" + w['ganmao'])
print("当前温度：" + w['wendu'] + "℃")