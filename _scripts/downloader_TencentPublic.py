# coding=utf8
import requests as req
from bs4 import BeautifulSoup as bs

class QQPublicDownloader:
	
	def __init__(url: str):
		self.header = {
			'Accept': 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			'User-Agent': 'user-agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
		}
		self.url = url
	
	def download():
		resp = req.get(self.url, headers=self.header)
		if resp.ok:
			self.resp = resp
		else:
			print('获取页面失败：' + str(resp.status_code))
			self.resp = None

	def generateMarkdown():
		
		pass
	

if __name__ == "__main__":
	url = 'https://post.mp.qq.com/kan/article/1001000923407-1028370926.html?_wv=2147483777&sig=c1d53cb3946dddc776562feda53fdf05&article_id=1028370926&time=1587379479&_pflag=1&x5PreFetch=1&rowkey=0565e9d7cdc22314&cc_media_type=10001&share_source=0'
	QQPublicDownloader(url)
