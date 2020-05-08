# coding=utf8
import requests as req
import json

header = {
    "Host": "imgchr.com",
    "Connection": "keep-alive",
    "Accept": "application/json",
    "Origin": "https://imgchr.com",
    "Sec-Fetch-Dest": "empty",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
    "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundarytEY4AtKCbEZ1wxfz",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Referer": "https://imgchr.com/i/YZqhan",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
    "Cookie": "PHPSESSID=tqactv195k6vvo5lr6jsosg1t1; _ga=GA1.2.785849557.1588818454; _gid=GA1.2.1583114267.1588818454; Hm_lvt_c1a64f283dcc84e35f0a947fcf3b8594=1588818454; KEEP_LOGIN=lPQDP%3A5c4b0b4ff68264789803c192a37f706ed226699df5cc255aa8da56b7a7f1b030f96a42327d659595cb8aa4d2d71e31892634a4b0eaecc5318052721e2d4d332377b07a1f2893b637f4defe3a36ba0e050d2c93b125fb006374dbda4c3dacd40a6d182c336b3f5%3A1588818530; Hm_lpvt_c1a64f283dcc84e35f0a947fcf3b8594=1588830529",
}

