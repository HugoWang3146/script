#!/usr/bin/python3
from urllib import request
from bs4 import BeautifulSoup

import json
import requests


def getQQSongRawData():
    response = request.urlopen(
        'https://c.y.qq.com/v8/fcg-bin/fcg_v8_singer_track_cp.fcg?g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&singermid=001ByAsv3XCdgm&order=listen&begin=0&num=250&songstatus=1')
    data = response.read().decode('utf-8')
    f = open('data.json', 'w')
    f.write(data)
    f.close()


def printSongList():
    f = open('data.json', 'r')
    data = json.load(f)
    print(len(data['data']['list']))
    for song in data['data']['list']:
        print('%s,%s' % (song['musicData']['songmid'],
                         song['musicData']['songname']))


def getDownlaodUrl():
    try:
        f = open('data.json', 'r')
        data = json.load(f)
        f.close()
        url_template = 'https://y.qq.com/n/yqq/song/%s.html'
        headers = {"X-Requested-With": "XMLHttpRequest",
                   "User-Agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36"}
        for song in data['data']['list']:
            songmid = song['musicData']['songmid']
            form = {
                'input': url_template % (songmid),
                'filter': 'url',
                'type': '_',
                'page': 1
            }
            response = requests.post(
                'http://www.guqiankun.com/tools/music/', headers=headers, data=form)
            data = response.json()
            print(data['data'][0]['title'], data['data'][0]['url'])
            # downloadSong(data['data'][0]['title'], data['data'][0]['url'])
            downloadLrc(data['data'][0]['title'], data['data'][0]['lrc'])
    except:
        print('error')


def downloadSong(name, url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    }
    try:
        download = requests.get(url, headers=headers)
        song_file = open('music/%s.mp3' % (name), 'wb+')
        song_file.write(download.content)
        song_file.close()
    except:
        print('%s,%s' % (name, url))


def downloadLrc(name, content):
    try:
        song_file = open('lrc/%s.lrc' % (name), 'w')
        song_file.write(content)
        song_file.close()
    except:
        print('%s' % (name))


# getQQSongRawData()
# printSongList()
getDownlaodUrl()
