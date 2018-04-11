#coding:utf-8
import urllib
import urllib2

url = "http://127.0.0.1/forms"

header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
} #这是请求头部信息

data = {
    "username" : "user2",
    "password" : "123456"
        } #这是要发送给服务器的数据

json_data = urllib.urlencode(data) #对数据进行封装

req = urllib2.Request(url,json_data,header)

#携带我们写好的头部信息和要发送的数据指向url发起请求

red = urllib2.urlopen(req)
#print req.host
print (red.read()) #得到返回内容