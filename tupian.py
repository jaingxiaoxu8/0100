import requests
url='http://mm.chinasareview.com/wp-content/uploads/2018a/01/01/01.jpg'
dirc={}
dirc['User-Agent']='Mozilla/5.0 (Windows NT 10.0;must be str, not int WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5702.400 QQBrowser/10.2.1893.400'
ree=requests.get(url,headers=dirc)
# print(ree)
with open(r"C:\Users\123\Desktop\jxx\妹子图\\"+"123.jpg",'wb') as f:
	f.write(ree.content)