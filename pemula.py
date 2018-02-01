# -*- coding: utf-8 -*-

import KRIS
from KRIS.lib.curve.ttypes import *
from datetime import datetime
import time, random, sys, ast, re, os, io, json, subprocess, threading, string, codecs, requests, ctypes, urllib, urllib2, urllib3, wikipedia, tempfile
from bs4 import BeautifulSoup
from urllib import urlopen
import requests
from io import StringIO
from threading import Thread
from gtts import gTTS
from googletrans import Translator

kr = KRIS.LINE()
#kr.login(qr=True)
kr.login(token="")#
kr.loginResult()


print "╔═════════════════════════╗\n║╔═══════════════════════╗║\n║╠❂➣KRIS BERHASIL LOGIN ║║\n║╚═══════════════════════╝║\n╚═════════════════════════╝"
reload(sys)
sys.setdefaultencoding('utf-8')



helpMessage ="""
╔═════════════
║╔════════════
║║✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰ 
║╚════════════
║╔════════════
║║Owner : Kris
║║line://ti/p/~krissthea
║╚════════════
║╔════════════
║╠❂➣Help [key bot]
║╠❂➣Respon
║╠❂➣Absen
║╠❂➣Gcreator
║╠❂➣Creator
║╠❂➣Aku
║╠❂➣Ginfo
║╠❂➣Id
║╠❂➣Midku
║╠❂➣Status
║╠❂➣Undang [kontak]
║╠❂➣Invite [mid]
║╠❂➣Namaku [ubah nama]
║╠❂➣Kick [mid]
║╠❂➣Kill
║╠❂➣v [kata]
║╠❂➣Cium
║╠❂➣Spam on/off [jml] [kata]
║╠❂➣Ambilnama @
║╠❂➣Ambilbio @
║╠❂➣Ambilpp @
║╠❂➣Ambilmid @
║╠❂➣Cium @
║╠❂➣Spamtag @
║╠❂➣Spamkontak @
║╠❂➣LG [list grup]
║╠❂➣LG2 [list grup]
║╠❂➣Ambilkontak @
║╠❂➣Salin @
║╠❂➣Kembali
║╠❂➣Time
║╠❂➣Ambil @
║╠❂➣Key1
║╠❂➣Key2
║╠❂➣Key3
║╚════════════
║ ~Team CAB~
╚═════════════
"""
key1Message ="""
╔═════════════
║╔════════════
║║✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰ 
║╚════════════
║╔════════════
║║Owner : Kris
║║line://ti/p/~krissthea
║╚════════════
║╔════════════
║╠❂͜͡🌟➣wιĸι [тeхт]
║╠❂͜͡🌟➣ιg [тeхт]
║╠❂͜͡🌟➣ιмage [тeхт]
║╠❂͜͡🌟➣vιdeo [тeхт]
║╠❂͜͡🌟➣zodιaĸ [тeхт]
║╠❂͜͡🌟➣yoυтυвe [тeхт]
║╠❂͜͡🌟➣lιrιĸ [тeхт]
║╠❂͜͡🌟➣ιdlιne [тeхт]
║╠❂͜͡🌟➣мυѕιc [тeхт]
║╠❂͜͡🌟➣тιмe [тιмe]
║╠❂͜͡🌟➣ѕay [тeхт]
║╚════════════
║╔════════════
║╠☔тr-ιd = ιndoneѕιa
║╠☔тr-мy = мyanмar
║╠☔тr-en = englιѕн
║╠☔тr-тн = тнaιland
║╠☔тr-ja = japaneѕe
║╠☔тr-мѕ = мalayѕιa
║╠☔тr-ιт = ιтalιan
║╠☔тr-тr = тυrĸιѕн
║╠☔тr-aғ = aғrιĸaanѕ
║╠☔тr-ѕq = alвanιan
║╠☔тr-aм = aмнarιc
║╠☔тr-ar = araвιc
║╠☔тr-нy = arмenιan
║╚════════════
╚═════════════
"""

key2Message ="""
╔═════════════
║╔════════════
║║✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰ 
║╚════════════
║╔════════════
║║Owner : Kris
║║line://ti/p/~krissthea
║╚════════════
║╔════════════
║╠❂➣kontak on/off
║╠❂➣Join on/off
║╠❂➣Leave on/off
║╠❂➣Share on/off
║╠❂➣Add on/off
║╠❂➣mode on/off
║╠❂➣Respoto on/off
║╠❂➣Sambut on/off
║╠❂➣Pergi on/off
║╠❂➣Tag on/off [autorespon]
║╠❂➣Tag2 on/off [Autoresponkick]
║╚════════════
╚═════════════
"""

key3Message ="""
╔═════════════
║╔════════════
║║✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰ 
║╚════════════
║╔════════════
║║Owner : Kris
║║line://ti/p/~krissthea
║╚════════════
║╔════════════
║╠❂͜͡🌟➣gιғт
║╠❂͜͡🌟➣gιғт 1
║╠❂͜͡🌟➣gιғт 2
║╠❂͜͡🌟➣gιғт 3
║╚════════════
║╔════════════
║╠❂➣Gn [kata][gantinamagrup]
║╠❂➣Gcancel:
║╠❂➣Gurl
║╠❂➣Cancel [batalin undangan]
║╠❂➣Buka link/tutup link
║╠❂➣Glist
║╠❂➣Pesan dipilih [kata]
║╠❂➣Pesan add [kata]
║╠❂➣Pesan
║╠❂➣Komen [kata]
║╠❂➣Add komen [kata]
║╠❂➣Komen on/off
║╠❂➣Cctv
║╠❂➣cctv on/off
║╠❂➣Intip/Toong
║╠❂➣Cek/Check
║╠❂➣Crot/nah/Nah [mention]
║╠❂➣Bersihkan
║╠❂➣Salam1/2
║╠❂➣crash
║╠❂➣Gbc [Bc ke semua grup]
║╠❂➣Pmkesemua [Bc ke tmn]
║╠❂➣Fbc [bc kesemua kontak]
║╠❂➣Bot off
║╠❂➣setview
║╠❂➣viewseen
║╠❂➣Micadd @
║╠❂➣Michapus @
║╠❂➣Miclist
║╠❂➣Mimic on/off
║╠❂➣Bcgrup: [kata]
║╚════════════
╚═════════════
"""

KAC=[kr]
mid = kr.getProfile().mid

Bots=[mid]
owner=["u31ef22df7f538df1d74dc7f756ef1a32","u9cc2323f5b84f9df880c33aa9f9e3ae1",mid]
admin=["u31ef22df7f538df1d74dc7f756ef1a32","u9cc2323f5b84f9df880c33aa9f9e3ae1","u0e881fcbda6a0d82974a775f8015f4fe","ud3065a5bd9cf0d6961d9c046a124761c","u60694eabf6ae04073739b4c95777d04a","uece14c5ae46691f48f03c4fd331c3fd8","u6908b4803bf3e267cf659ddda91d5fa4","u60335d94c7a3ca3a3c3685f515724145","uc92d7e39d7259174dba7d8028c7ef4b2","uc1ba312554b4ee025039f54ff44c7c7f","uad6cb020c5ca7afbecb4681675eb38cd","udcf44c4272d8209a8a5f2dd1afeea93f","u45c6ce403f0acc28392c519028aae154","udb0b6b2c1f32887d23bd3e4dfb302ed1","uc6a6ba43d1ce45e5c78fc7fb37afd17e","ud74066bb0bc042125f6da564f576d683","u7b8ce44a6f9d630388280e817775111f","uf1850996231087975161942c551f3ac9","u412728dbaf91158d3787b7de2aaf5be8","uaa4d57483fe9bc48d6b904dac88d8ef5","u4a0be979fc73e88ebfe915bc917237b8","u7f94f517d3f2d97718f4f49258a7ef7c","ua8b707e4382fc47b4df318c7c9aa1f3e","u4a0f653ea757da7abcd41c15bf0f15da","u8197906b2cc18e992fd6bd63d3dac867","uadfd3a23698b71d17c64482d27dc2ed1","u53c352134325f0c49e86534c57801bd7","ud5262649376cbf7576e2dcac0331d481","u0e881fcbda6a0d82974a775f8015f4fe","u9d4b18194ce5b48d86fa27e5fac1d606","uc70b2f7f85d13c96e0f28ded3b3b13d6","u60694eabf6ae04073739b4c95777d04a","u15d0c7b52ea7731e5245531c2f543d50","u28c833c6d623e47cf130cb32457c6b3b","u4a0f653ea757da7abcd41c15bf0f15da","u53c352134325f0c49e86534c57801bd7","ud5262649376cbf7576e2dcac0331d481","uadfd3a23698b71d17c64482d27dc2ed1","uc6a6ba43d1ce45e5c78fc7fb37afd17e","ud74066bb0bc042125f6da564f576d683","u7b8ce44a6f9d630388280e817775111f","ua2ea9f4c32848bc67644c5267bb91279","u412728dbaf91158d3787b7de2aaf5be8","uaa4d57483fe9bc48d6b904dac88d8ef5","u4a0be979fc73e88ebfe915bc917237b8","uece14c5ae46691f48f03c4fd331c3fd8","uc545f6498513e4c8bc7004920e037ff3","uc06a9b75c93e5b4b726d9d3c9889b699","ud55745480bb2c5665e6a21df2a68155e","u241b9b83d51b93c77c982e8330139cdd","u183bff92d294ed24000efe36e8b2c474",mid]##Krisna,kris,
wait = {
    'contact':False,
    'alwayRead':False,
    'autoJoin':False,
    'autoCancel':{"on":False,"members":1},
    'leaveRoom':False,
    'timeline':False,
    'autoAdd':False,
    'detectMention':True,
    'message':"""👉😊☆º°˚˚☆✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰☆º°˚˚☆（＾ω＾）\n\nby Kris ⭐👈 »»» http://line.me/ti/p/~krissthea «««""",
    "lang":"JP",
    "comment":"""👉😊☆º°˚˚☆✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰☆º°˚˚☆（＾ω＾）\n\nby Kris ⭐👈 »»» http://line.me/ti/p/~krissthea «««""",
    "commentOn":False,
    "clock":False,
    "auto":False,
    "tag":False,
    "tag2":False,
    "likeOn":False,
    "winvite":False,
    "Wc":False,
    "Lv":False
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }

setTime = {}
setTime = wait2['setTime']

contact = kr.getProfile()
mybackup = kr.getProfile()
mybackup.displayName = contact.displayName
mybackup.statusMessage = contact.statusMessage
mybackup.pictureStatus = contact.pictureStatus

contact = kr.getProfile()
backup = kr.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = kr.getProfile()
profile = kr.getProfile()
profile.displayName = contact.displayName
profile.statusMessage = contact.statusMessage
profile.pictureStatus = contact.pictureStatus

mulai = time.time()

url123 = ("https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26229822_136061360519754_2383391381158562768_n.jpg?oh=5b629e008c344ab9120798423a1fe9fe&oe=5ABEC25F")

agent = {'User-Agent' : "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)"}

def translate(to_translate, to_language="auto", language="auto"):
    bahasa_awal = "auto"
    bahasa_tujuan = to_language
    kata = to_translate
    url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
    agent = {'User-Agent':'Mozilla/5.0'}
    cari_hasil = 'class="t0">'
    request = urllib2.Request(url, headers=agent)
    page = urllib2.urlopen(request).read()
    result = page[page.find(cari_hasil)+len(cari_hasil):]
    result = result.split("<")[0]
    return result

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     #If the Current Version of Python is 3.0 or above
        import urllib,request    #urllib library for Extracting web pages
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        #If the Current Version of Python is 2.x
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"

#Finding 'Next Image' from the given raw page
def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:    #If no links are found then give an error!
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"',start_line+90)
        end_content = s.find(',"ow"',start_content-90)
        content_raw = str(s[start_content+6:end_content-1])
        return content_raw, end_content

#Getting all links with the help of '_images_get_next_image'
def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      #Append all the links in the list named 'Links'
            time.sleep(0.1)        #Timer could be used to slow down the request for image downloads
            page = page[end_content:]
    return items

#def autolike():
#			for zx in range(0,100):
#				hasil = kr.activity(limit=100)
#				if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
#					try:
#						kr.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
#						kr.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like By CAB =>> Cyber Army Bot <<==)
#						print "DiLike"
#					except:
#							pass
#				else:
#						print "Sudah DiLike"
#			time.sleep(500)
#thread2 = threading.Thread(target=autolike)
#thread2.daemon = True
#thread2.start()

#def autolike():
#    for zx in range(0,100):
#      hasil = kr.activity(limit=100)
#      if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
#        try:
#          kr.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
#          kr.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"👉ąµţ๏ℓɨЌ€ By✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰😊\n\n☆º°˚˚☆ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰°˚˚☆（＾ω＾）\nąµţ๏ℓɨЌ€ by Kris ⭐👈 »»» http://line.me/ti/p/GkwfNjoPDH «««")
#          print "Like"
#        except:
#          pass
#      else:
#          print "Already Liked"
#time.sleep(500)
#thread2 = threading.Thread(target=autolike)
#thread2.daemon = True
#thread2.start()

def yt(query):
    with requests.session() as s:
         isi = []
         if query == "":
             query = "S1B tanysyz"
         s.headers['user-agent'] = 'Mozilla/5.0'
         url    = 'http://www.youtube.com/results'
         params = {'search_query': query}
         r    = s.get(url, params=params)
         soup = BeautifulSoup(r.content, 'html5lib')
         for a in soup.select('.yt-lockup-title > a[title]'):
            if '&list=' not in a['href']:
                if 'watch?v' in a['href']:
                    b = a['href'].replace('watch?v=', '')
                    isi += ['youtu.be' + b]
         return isi

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d Jam %02d Menit %02d Detik' % (hours, mins, secs)

def upload_tempimage(client):
     '''
         Upload a picture of a kitten. We don't ship one, so get creative!
     '''
     config = {
         'album': album,
         'name':  'bot auto upload',
         'title': 'bot auto upload',
         'description': 'bot auto upload'
     }

     print("Uploading image... ")
     image = client.upload_from_path(image_path, config=config, anon=False)
     print("Done")
     print()

     return image


def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def sendImage(self, to_, path):
      M = Message(to=to_,contentType = 1)
      M.contentMetadata = None
      M.contentPreview = None
      M_id = self.Talk.client.sendMessage(0,M).id
      files = {
         'file': open(path, 'rb'),
      }
      params = {
         'name': 'media',
         'oid': M_id,
         'size': len(open(path, 'rb').read()),
         'type': 'image',
         'ver': '1.0',
      }
      data = {
         'params': json.dumps(params)
      }
      r = self.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
      if r.status_code != 201:
         raise Exception('Upload image failure.')
      return True

def sendImageWithURL(self, to_, url):
      path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download image failure.')
      try:
         self.sendImage(to_, path)
      except Exception as e:
         raise e

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def post_content(self, urls, data=None, files=None):
        return self._session.post(urls, headers=self._headers, data=data, files=files)

def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.param1 in wait2['readPoint']:
            Name = kr.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n9§9" + Name
                wait2['ROM'][op.param1][op.param2] = "9§9" + Name
        else:
            pass
    except:
        pass

def sendAudio(self, to_, path):
        M = Message(to=to_, text=None, contentType = 3)
        M_id = self.Talk.client.sendMessage(0,M).id
        files = {
            'file': open(path, 'rb'),
        }
        params = {
            'name': 'media',
            'oid': M_id,
            'size': len(open(path, 'rb').read()),
            'type': 'audio',
            'ver': '1.0',
        }
        data = {
            'params': json.dumps(params)
        }

        r = self.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
        print r
        if r.status_code != 201:
            raise Exception('Upload audio failure.')


def sendAudioWithURL(self, to_, url):
      path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download audio failure.')
      try:
         self.sendAudio(to_, path)
      except Exception as e:
            raise e
def sendAudioWithURL(self, to_, url):
      path = 'pythonLiness.data'
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download Audio failure.')
      try:
         self.sendAudio(to_, path)
      except Exception as e:
         raise e

def sendVoice(self, to_, path):
        M = Message(to=to_, text=None, contentType = 3)
        M.contentPreview = None
        M_id = self._client.sendMessage(0,M).id
        files = {
            'file': open(path, 'rb'),
        }
        params = {
            'name': 'voice_message',
            'oid': M_id,
            'size': len(open(path, 'rb').read()),
            'type': 'audio',
            'ver': '1.0',
        }
        data = {
            'params': json.dumps(params)
        }
        r = self.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Upload voice failure.')
        return True

def sendVideoWithURL(self, to_, url):
      path = 'pythonLines.data'
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download Audio failure.')
      try:
         self.sendVideo(to_, path)
      except Exception as e:
         raise e
       
def mention(to,nama):
    aa = ""
    bb = ""
    strt = int(12)
    akh = int(12)
    nm = nama
    #print nm
    for mm in nm:
        akh = akh + 2
        aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
        strt = strt + 6
        akh = akh + 4
        bb += "► @c \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "「Mention」\n"+bb
    msg.contentMetadata = {"MENTION":'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    #print msg
    try:
         kr.sendMessage(msg)
    except Exception as error:
        print error
def summon(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={"MENTION":'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print "[Command] Tag All"
    try:
       kr.sendMessage(msg)
    except Exception as error:
       print error

def removeAllMessages(self, lastMessageId):
     return self._client.removeAllMessages(0, lastMessageId)
def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："] 
    for tex in tex:
      for command in commands:
        if string ==command:
          return True
     
def sendText(self, Tomid, text):
        msg = Message()
        msg.to = Tomid
        msg.text = text

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 13:
            if wait["auto"] == True:
                kr.acceptGroupInvitation(op.param1)
                #kr.sendText(op.param1, "👉😊☆º°˚˚☆✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰☆º°˚˚☆（＾ω＾）\n\nby Kris ⭐👈 »»» http://line.me/ti/p/~krissthea «««\n\nSilahkan ketik [Help],dan gunakan dgn bijak")
        if op.type == 5:
            if wait["autoAdd"] == True:
                kr.findAndAddContactsByMid(op.param1)

                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    kr.sendText(op.param1,str(wait["message"]))

#------------------NOTIFIED_READ_MESSAGE----------------#
        if op.type == 55:
	    try:
	      group_id = op.param1
	      user_id=op.param2
	      subprocess.Popen('echo "'+ user_id+'|'+str(op.createdTime)+'" >> dataSeen/%s.txt' % group_id, shell=True, stdout=subprocess.PIPE, )
	    except Exception as e:
	      print e

        if op.type == 26:
            msg = op.message

            if msg.text is None:
                return

            if "@"+kr.getProfile().displayName in msg.text:
                if wait["tag"] == True:
                    tanya = msg.text.replace("@"+kr.getProfile().displayName,"")
                    jawab = ("Kenapa Tag Si "+kr.getProfile().displayName+"Kangen yah..!!!\nPC aja langsung biar anu hihi..!!\n[autoRespon]by=>SelfBot~Kris\n👉Cyber Army Bot👈","Nah ngetag lagi si "+kr.getProfile().displayName+" mending ajak mojok aja dari pada ngetag mulu.. wkwk...!!!\n[autoRespon]by=>SelfBot~Kris\n👉Cyber Army Bot👈")
                    jawaban = random.choice(jawab)
                    kr.sendText(msg.to,jawaban)

            if "MENTION" in msg.contentMetadata.keys() != None:
                 if wait['detectMention'] == True:
                     contact = kr.getContact(msg.from_)
                     cName = contact.pictureStatus
                     balas = ["http://dl.profile.line-cdn.net/" + cName]
                     ret_ = random.choice(balas)
                     mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  kr.sendImageWithURL(msg.to,ret_)
                                  break  

        if op.type == 26:
            msg = op.message

            if msg.text is None:
                return

            if "@"+kr.getProfile().displayName in msg.text:
                if wait["tag2"] == True:
                    tanya = msg.text.replace("@"+kr.getProfile().displayName,"")
                    jawab = "Kenapa Tag Si "+kr.getProfile().displayName+"Kangen yah..!!!\nPC aja langsung biar anu hihi..!!\n[autoRespon]by=>SelfBot~Kris\n👉Cyber Army Bot👈","Nah ngetag lagi si "+kr.getProfile().displayName+" mending ajak mojok aja dari pada ngetag mulu.. wkwk...!!!\n[autoRespon]by=>SelfBot~Kris\n👉Cyber Army Bot👈"
                    jawaban = random.choice(jawab)
                    kr.sendText(msg.to,jawaban)
                    kr.kickoutFromGroup(msg.to,[msg.from_])
                    kr.inviteIntoGroup(msg.to,admin)
                    #kr.sendAudio(msg.to,jawaban)
        #--CANCEL KICK--#
#        if op.type == 32:
#            if wait["Protectcancel"] == True:
#                if op.param2 in admin:
#                    pass
#                if op.param2 not in Bots:
#                    kr.kickoutFromGroup(op.param1,[op.param2])
        #------Invite User Kick start------#
#        if op.type == 13:
#           if wait["Protectguest"] == True:
#                if op.param2 in admin:
#                    pass
#                if op.param2 not in Bots:
#                    kr.cancelGroupInvitation(op.param1,[op.param3])
#                    kr.kickoutFromGroup(op.param1,[op.param2])
        #------Invite User Kick Finish------#

        #----MemberProtection------#
 #       if op.type == 19:
 #           if wait["MProtection"] == True:
 #               if op.param2 in admin:
 #                   pass
 #               if op.param2 not in Bots:
 #                   kr.kickoutFromGroup(op.param1,[op.param2])
 #                   kr.inviteIntoGroup(op.param1,[op.param3])
        #------Open QR Kick start------#
 #       if op.type == 11:
 #           if wait["QrProtect"] == True:
 #               if op.param2 in admin:
 #                   pass
 #               if op.param2 not in Bots:
 #                   G = kr.getGroup(op.param1)
 #                   G.preventJoinByTicket = True
 #                   kr.kickoutFromGroup(op.param1,[op.param3])
 #                   kr.updateGroup(G)
        #------Open QR Kick finish-----#

        if op.type == 17:
            if wait["Wc"] == True:
                if op.param2 in Bots:
                    return
                ginfo = kr.getGroup(op.param1)
                gm = Message()
                gm.to = op.param1
                gm.text = ("╔═════════════" + "\n║" + kr.getContact(op.param2).displayName + "\n╠═════════════\n║Selamat Datang Di  " + str(ginfo.name) + "\n╠═════════════\n" + "║Founder =>>> " + str(ginfo.name) + " :\n║" + ginfo.creator.displayName + "\n╠═════════════\n" + "║😊Semoga Betah Kak 😘 \n╠═════════════\n║No Baper,No nakal,No Ngeyel ya..!! \n╚═════════════")
                kr.sendMessage(gm)
                print "MEMBER HAS JOIN THE GROUP"
        if op.type == 17:
            if wait["Wc"] == True:
                if op.param2 in Bots:
                    return
                G = kr.getGroup(op.param1)
                h = kr.getContact(op.param2)
                kr.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net/" + h.pictureStatus)
                print "MEMBER HAS JOIN THE GROUP"
        if op.type == 15:
            if wait["Lv"] == True:
                if op.param2 in Bots:
                    return
                kr.sendText(op.param1, "╔═════════════" + "\n║" + kr.getContact(op.param2).displayName  +  "\n╠═════════════\n║Nah Baper Dia :v \n╠═════════════\n║Belum di Anu Kayanya 😊 \n╚═════════════")
                print "MEMBER HAS LEFT THE GROUP"
#-----------------------------------------------
        if op.type == 25:
            msg = op.message
            if msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
                    text = msg.text
                    if text is not None:
                        kr.sendText(msg.to,text)

#--------------NOTIFIED_INVITE_INTO_GROUP----------------
        if op.type == 13:
	    print op.param3
            if op.param3 in mid:
		if op.param2 in owner or admin:
		    kr.acceptGroupInvitation(op.param1)
#--------------------------------------------------------
            if op.param3 in mid:
		if op.param2 in owner or admin:
		    kr.acceptGroupInvitation(op.param1)

#--------------------------------------------------------
#--------------------------------------------------------
        if op.type == 13:
	    print op.param3
            if op.param3 in mid:
		if op.param2 in owner or admin:
		    kr.acceptGroupInvitation(op.param1)

        if op.type == 13:
            if mid in op.param3:
              if wait['autoJoin'] == True:
                if op.param2 in owner or admin:
                  kr.acceptGroupInvitation(op.param1)
                else:
                  kr.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
            if mid in op.param3:
              if wait['autoJoin'] == True:
                if op.param2 in admin:
                  kr.acceptGroupInvitation(op.param1)
                else:
                  kr.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
        if op.type == 19:
            if op.param3 in admin:
                if op.param2 not in admin:
                    kr.kickoutFromGroup(op.param1,[op.param2])
                    kr.inviteIntoGroup(op.param1,owner)

            if op.param3 in Bots:
                if op.param2 not in Bots:
                    kr.inviteIntoGroup(op.param1,Bots)
                    kr.inviteIntoGroup(op.param1,[op.param3])
                    
#================================================================
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
            	if wait["winvite"] == True:
                     #if msg.from_ in owner:
                         _name = msg.contentMetadata["displayName"]
                         invite = msg.contentMetadata["mid"]
                         groups = kr.getGroup(msg.to)
                         pending = groups.invitee
                         targets = []
                         for s in groups.members:
                             if _name in s.displayName:
                                 kr.sendText(msg.to,"-> " + _name + " was here")
                                 break
                             elif invite in wait["blacklist"]:
                                 kr.sendText(msg.to,"Sorry, " + _name + " On Blacklist")
                                 kr.sendText(msg.to,"Call my owner to use command !, \n➡Unban: " + invite)
                                 break
                             else:
                                 targets.append(invite)
                         if targets == []:
                             pass
                         else:
                             for target in targets:
                                 try:
                                     kr.findAndAddContactsByMid(target)
                                     kr.inviteIntoGroup(msg.to,[target])
                                     kr.sendText(msg.to,"Done Invite : \n➡" + _name)
                                     wait["winvite"] = False
                                     break
                                 except:
                                     try:
                                         kr.findAndAddContactsByMid(invite)
                                         kr.inviteIntoGroup(op.param1,[invite])
                                         wait["winvite"] = False
                                     except:
                                         kr.sendText(msg.to,"Negative, Error detected")
                                         wait["winvite"] = False
                                         break

            if wait['alwayRead'] == True:
                if msg.toType == 0:
                    kr.sendChatChecked(msg.from_,msg.id)
                else:
                    kr.sendChatChecked(msg.to,msg.id)


        if op.type == 22:
            if wait["leaveRoom"] == True:
                kr.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                kr.leaveRoom(op.param1)
        if op.type == 25:
            msg = op.message
#-----------------------------------------
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    kr.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                kr.like(url[25:58], url[66:], likeType=1001)
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:

                if wait["contact"] == True:
                    msg.contentType = 0
                    kr.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = kr.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = kr.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        kr.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = kr.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = kr.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        kr.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URL�0�10��9�0�16�0�69�0�3�0�4\n" + msg.contentMetadata["postEndUrl"]
                    kr.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text in ["help","Help"]:
					if wait["lang"] == "JP":
						kr.sendText(msg.to,helpMessage)
						kr.sendImageWithURL(msg.to, url123)
						kr.sendText(msg.to,"↥↥↥↥↥↪ Owner Bots ↩↥↥↥↥↥")
					else:
						kr.sendText(msg.to,helpt)
					
            elif msg.text in ["Key1","key1"]:
					if wait["lang"] == "JP":
						kr.sendText(msg.to,key1Message)
					else:
						kr.sendText(msg.to,key1Message)	
						
            elif msg.text in ["Key2","key2"]:
					if wait["lang"] == "JP":
						kr.sendText(msg.to,key2Message)
					else:
						kr.sendText(msg.to,key2Message)	
						
            elif msg.text in ["Key3","key3"]:
					if wait["lang"] == "JP":
						kr.sendText(msg.to,key3Message)
					else:
						kr.sendText(msg.to,key3Message)	
#--------------------------------------------------
#--------------------------------------------------
            elif ("Gn " in msg.text):
				#if msg.from_ in owner:
					if msg.toType == 2:
						X = kr.getGroup(msg.to)
						X.name = msg.text.replace("Gn ","")
						kr.updateGroup(X)
					else:
						kr.sendText(msg.to,"It can't be used besides the group.")
#--------------------------------------------------
#--------------------------------------------------
            elif "Kick " in msg.text:
				#if msg.from_ in owner:
					midd = msg.text.replace("Kick ","")
					kr.kickoutFromGroup(msg.to,[midd])
#--------------------------------------------------
#--------------------------------------------------
            elif "Invite " in msg.text:
				#if msg.from_ in owner:
					midd = msg.text.replace("Invite ","")
					kr.findAndAddContactsByMid(midd)
					kr.inviteIntoGroup(msg.to,[midd])
#--------------------------------------------------
#--------------------------------------------------
            elif msg.text in ["Aku","aku"]:
                #if msg.from_ in owner:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': msg.from_}
                    kr.sendMessage(msg)
#--------------------------------------------------
#--------------------------------------------------
            elif msg.text in ["cancel","Cancel"]:
				#if msg.from_ in owner:
					if msg.toType == 2:
						G = kr.getGroup(msg.to)
						if G.invitee is not None:
							gInviMids = [contact.mid for contact in G.invitee]
							kr.cancelGroupInvitation(msg.to, gInviMids)
						else:
							if wait["lang"] == "JP":
								kr.sendText(msg.to,"No one is inviting")
							else:
								kr.sendText(msg.to,"Sorry, nobody absent")
					else:
						if wait["lang"] == "JP":
							kr.sendText(msg.to,"Can not be used outside the group")
						else:
							kr.sendText(msg.to,"Not for use less than group")
#--------------------------------------------------
#--------------------------------------------------
            elif msg.text in ["Buka link","buka link"]:
				#if msg.from_ in owner:
					if msg.toType == 2:
						X = kr.getGroup(msg.to)
						X.preventJoinByTicket = False
						kr.updateGroup(X)
						if wait["lang"] == "JP":
							kr.sendText(msg.to,"Done")
						else:
							kr.sendText(msg.to,"already open")
					else:
						if wait["lang"] == "JP":
							kr.sendText(msg.to,"Can not be used outside the group")
						else:
							kr.sendText(msg.to,"Not for use less than group")
#--------------------------------------------------
#--------------------------------------------------
            elif msg.text in ["Tutup link","tutup link"]:
				#if msg.from_ in owner:
					if msg.toType == 2:
						X = kr.getGroup(msg.to)
						X.preventJoinByTicket = True
						kr.updateGroup(X)
						if wait["lang"] == "JP":
							kr.sendText(msg.to,"Done")
						else:
							kr.sendText(msg.to,"already close")
					else:
						if wait["lang"] == "JP":
							kr.sendText(msg.to,"Can not be used outside the group")
						else:
							kr.sendText(msg.to,"Not for use less than group")
#--------------------------------------------------
#--------------------------------------------------
#--------------------------------------------------
            elif msg.text == "Ginfo":
                if msg.toType == 2:
                    ginfo = kr.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        kr.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\nmembers:" + str(len(ginfo.members)) + "members\npending:" + sinvitee + "people\nURL:" + u + "it is inside")
                    else:
                        kr.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kr.sendText(msg.to,"Not for use less than group")
#--------------------------------------------------
            elif "Id" == msg.text:
				#if msg.from_ in owner:
					kr.sendText(msg.to,msg.to)
#--------------------------------------------------
            elif "Midku" == msg.text:
				#if msg.from_ in owner:
					kr.sendText(msg.to,mid)
#--------------------------------------------------
#--------------------------------------------------
            elif msg.text in ["Wkwk"]:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "100",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
					kk.sendMessage(msg)
#--------------------------------------------------
            elif msg.text in ["Hehehe"]:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "10",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
					kk.sendMessage(msg)
            elif msg.text in ["Galon"]:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "9",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
					kk.sendMessage(msg)
#--------------------------------------------------
            elif msg.text in ["You"]:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "7",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
					kk.sendMessage(msg)
#--------------------------------------------------
            elif msg.text in ["Hadeuh"]:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "6",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
					kk.sendMessage(msg)
#--------------------------------------------------
            elif msg.text in ["Please"]:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "4",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
					kk.sendMessage(msg)
#--------------------------------------------------
            elif msg.text in ["Haaa"]:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "3",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
					kk.sendMessage(msg)
#--------------------------------------------------
            elif msg.text in ["Lol"]:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "110",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
					kk.sendMessage(msg)
#--------------------------------------------------
            elif msg.text in ["Hmmm"]:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "101",
										"STKPKGID": "1",
										"STKVER": "100" }
					ki.sendMessage(msg)
#--------------------------------------------------
            elif msg.text in ["Come"]:
					msg.contentType = 7
					msg.text = None
					msg.contentMetadata = {
										"STKID": "247",
										"STKPKGID": "3",
										"STKVER": "100" }
					ki.sendMessage(msg)
					kk.sendMessage(msg)
#--------------------------------------------------
            elif msg.text in ["TL "]:
				#if msg.from_ in owner:
					tl_text = msg.text.replace("TL ","")
					kr.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+kr.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
#--------------------------------------------------
            elif msg.text in ["Undang"]:
              #if msg.from_ in owner:
                 wait["winvite"] = True
                 kr.sendText(msg.to,"send contact")
#--------------------------------------------------
            elif "Namaku " in msg.text:
                string = msg.text.replace("Namaku ","")
                if len(string.decode('utf-8')) <= 10000000000:
                    profile = kr.getProfile()
                    profile.displayName = string
                    kr.updateProfile(profile)
                    kr.sendText(msg.to,"Changed " + string + "")
            elif msg.text in ["Aimname "]:
				#if msg.from_ in owner:
					string = msg.text.replace("Aimname ","")
					if len(string.decode('utf-8')) <= 20:
						profile_B = kr.getProfile()
						profile_B.displayName = string
						kr.updateProfile(profile_B)
						kr.sendText(msg.to,"name " + string + " done")

#--------------------------------------------------
#--------------------------------------------------
#--------------------------------------------------
            elif msg.text in ["kontak on","Kontak on"]:
				#if msg.from_ in owner:
					if wait["contact"] == True:
						if wait["lang"] == "JP":
							kr.sendText(msg.to,"already on")
						else:
							kr.sendText(msg.to,"done")
					else:
						wait["contact"] = True
						if wait["lang"] == "JP":
							kr.sendText(msg.to,"already on")
						else:
							kr.sendText(msg.to,"done")
#--------------------------------------------------
            elif msg.text in ["kontak off","Kontak off"]:
				#if msg.from_ in owner:
					if wait["contact"] == False:
						if wait["lang"] == "JP":
							kr.sendText(msg.to,"already off")
						else:
							kr.sendText(msg.to,"done ")
					else:
						wait["contact"] = False
						if wait["lang"] == "JP":
							kr.sendText(msg.to,"already off")
						else:
							kr.sendText(msg.to,"done")
#--------------------------------------------------
            elif msg.text in ["Join on","join on"]:
				#if msg.from_ in owner:
					if wait["autoJoin"] == True:
						if wait["lang"] == "JP":
							kr.sendText(msg.to,"already on")
						else:
							kr.sendText(msg.to,"done")
					else:
						wait["autoJoin"] = True
						if wait["lang"] == "JP":
							kr.sendText(msg.to,"already on")
						else:
							kr.sendText(msg.to,"done")
#--------------------------------------------------
            elif msg.text in ["Join off","join off"]:
				#if msg.from_ in owner:
					if wait["autoJoin"] == False:
						if wait["lang"] == "JP":
							kr.sendText(msg.to,"already off")
						else:
							kr.sendText(msg.to,"done")
					else:
						wait["autoJoin"] = False
						if wait["lang"] == "JP":
							kr.sendText(msg.to,"already off")
						else:
							kr.sendText(msg.to,"done")
#--------------------------------------------------
            elif msg.text in ["Gcancel:"]:
				#if msg.from_ in owner:
					try:
						strnum = msg.text.replace("Gcancel:","")
						if strnum == "off":
							wait["autoCancel"]["on"] = False
							if wait["lang"] == "JP":
								kr.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
							else:
								kr.sendText(msg.to,"Ã¥â€¦Â³Ã¤Âºâ�1�7�1�71¤7 Ã©â 1�71¤7šâ‚¬Ã¨Â¯Â·Ã¦â€¹â 1�71¤7™Ã§Â»ÂÃ£â�1�7�¬â€šÃ¨Â¦ÂÃ¦â 1�71¤7”Â¶Ã¥Â¼â�1�7�¬Ã¨Â¯Â·Ã¦Å�1�7�â€¡Ã¥Â®Å¡Ã¤ÂºÂºÃ¦â 1�71¤7¢Â°Ã¥Ââ 1�71¤7˜Ã©â‚¬Â1�7")
						else:
							num =  int(strnum)
							wait["autoCancel"]["on"] = True
							if wait["lang"] == "JP":
								kr.sendText(msg.to,strnum + "The group of people and below decided to automatically refuse invitation")
							else:
								kr.sendText(msg.to,strnum + "Ã¤Â½Â¿Ã¤ÂºÂºÃ¤Â»Â¥Ã¤Â¸â€¹Ã§Å¡â�1�7�1�71¤7žÃ¥Â°ÂÃ§Â»â 1�71¤7žÃ§â 1�71¤7Â¨Ã¨â 1�71¤7¡ÂªÃ¥Å Â¨Ã©â 1�71¤7šâ‚¬Ã¨Â¯Â·Ã¦â€¹â 1�71¤7™Ã§Â»Â�1�7�1�71¤7")
					except:
						if wait["lang"] == "JP":
							kr.sendText(msg.to,"Value is wrong")
						else:
							kr.sendText(msg.to,"Bizarre ratings")
#--------------------------------------------------
            elif msg.text in ["Leave on","leave on"]:
				#if msg.from_ in owner:
					if wait["leaveRoom"] == True:
						if wait["lang"] == "JP":
							kr.sendText(msg.to,"already on")
						else:
							kr.sendText(msg.to,"done")
					else:
						wait["leaveRoom"] = True
						if wait["lang"] == "JP":
							kr.sendText(msg.to,"done")
						else:
							kr.sendText(msg.to,"Ã¨Â¦ÂÃ¤Âºâ€ Ã¥Â¼â�1�7�¬Ã£â�1�7�¬â�1�7�1�71¤7 1�71¤7")
#--------------------------------------------------
            elif msg.text in ["Leave off","leave off"]:
				#if msg.from_ in owner:
					if wait["leaveRoom"] == False:
						if wait["lang"] == "JP":
							kr.sendText(msg.to,"already off")
						else:
							kr.sendText(msg.to,"done")
					else:
						wait["leaveRoom"] = False
						if wait["lang"] == "JP":
							kr.sendText(msg.to,"done")
						else:
							kr.sendText(msg.to,"already")
#--------------------------------------------------
            elif msg.text in ["Share on","share on"]:
				#if msg.from_ in owner:
					if wait["timeline"] == True:
						if wait["lang"] == "JP":
							kr.sendText(msg.to,"already on")
						else:
							kr.sendText(msg.to,"done")
					else:
						wait["timeline"] = True
						if wait["lang"] == "JP":
							kr.sendText(msg.to,"done")
						else:
							kr.sendText(msg.to,"Ã¨Â¦ÂÃ¤Âºâ€ Ã¥Â¼â�1�7�¬Ã£â�1�7�¬â�1�7�1�71¤7 1�71¤7")
#--------------------------------------------------
            elif msg.text in ["Share off","share off"]:
				#if msg.from_ in owner:
					if wait["timeline"] == False:
						if wait["lang"] == "JP":
							kr.sendText(msg.to,"already off")
						else:
							kr.sendText(msg.to,"done")
					else:
						wait["timeline"] = False
						if wait["lang"] == "JP":
							kr.sendText(msg.to,"done")
						else:
							kr.sendText(msg.to,"Ã¨Â¦ÂÃ¤Âºâ€ Ã¥â�1�7�1�71¤7¦Â³Ã¦â 1�71¤7“Â­Ã£â�1�7�¬â€ 1�71¤7")
#--------------------------------------------------
            elif msg.text in ["Set","Status","status"]:
				#if msg.from_ in owner:
					md = ""
					if wait["contact"] == True: md+="🌂  CONTACT : [✅]\n"
					else: md+="🌂  CONTACT : [❌]\n"
					if wait["autoJoin"] == True: md+="🌂  AUTOJOIN : [✅]\n"
					else: md +="🌂  AUTOJOIN : [❌]\n"
					if wait["autoCancel"]["on"] == True:md+="🌂  GROUP CANCEL :" + str(wait["autoCancel"]["members"]) + "\n"
					else: md+="🌂  GROUP CANCEL : [❌]\n"
					if wait["leaveRoom"] == True: md+="🌂  AUTOLEAVE : [✅]\n"
					else: md+="🌂  AUTOLEAVE : [❌]\n"
					if wait["timeline"] == True: md+="🌂  SHARE : [✅]\n"
					else:md+="🌂  SHARE : [❌]\n"
					if wait["autoAdd"] == True: md+="🌂  AUTOADD : [✅]\n"
					else:md+="🌂  AUTOADD : [❌]\n"
					if wait["commentOn"] == True: md+="🌂  COMMENT : [✅]\n"
					else:md+="🌂  COMMENT : [❌]\n"
					if wait["likeOn"] == True: md+="🌂  AUTOLIKE : [✅]\n"
					else:md+="🌂  AUTOLIKE : [❌]\n"
					if wait["Wc"] == True: md+="🌂  SAMBUTAN : [✅]\n"
					else:md+="🌂  SAMBUTAN : [❌]\n"
					if wait["Lv"] == True: md+="🌂  UCAPAN PERGI : [✅]\n"
					else:md+="🌂  UCAPAN PERGI : [❌]\n"
					if wait["tag"] == True: md+="🌂  TAG 1 : [✅]\n"
					else:md+="🌂  TAG 1 : [❌]\n"
					if wait["tag2"] == True: md+="🌂  TAG 2 : [✅]\n"
					else:md+="🌂  TAG 2 : [❌]\n"
					if wait["auto"] == True: md+="🌂  AutoBot Join : [✅]\n"
					else:md+="🌂  AutoBot Join : [❌]\n"
					kr.sendText(msg.to,md)
#--------------------------------------------------
#--------------------------------------------------
            elif msg.text in ["Add on","add on"]:
				#if msg.from_ in owner:
					if wait["autoAdd"] == True:
						if wait["lang"] == "JP":
							kr.sendText(msg.to,"already on")
						else:
							kr.sendText(msg.to,"done")
					else:
						wait["autoAdd"] = True
						if wait["lang"] == "JP":
							kr.sendText(msg.to,"done")
						else:
							kr.sendText(msg.to,"Ã¨Â¦ÂÃ¤Âºâ€ Ã¥Â¼â�1�7�¬Ã£â�1�7�¬â�1�7�1�71¤7 1�71¤7")
#--------------------------------------------------
            elif msg.text in ["Add off","add off"]:
				#if msg.from_ in owner:
					if wait["autoAdd"] == False:
						if wait["lang"] == "JP":
							kr.sendText(msg.to,"already off")
						else:
							kr.sendText(msg.to,"done")
					else:
						wait["autoAdd"] = False
						if wait["lang"] == "JP":
							kr.sendText(msg.to,"done")
						else:
							kr.sendText(msg.to,"Ã¨Â¦ÂÃ¤Âºâ€ Ã¥â�1�7�1�71¤7¦Â³Ã¦â 1�71¤7“Â­Ã£â�1�7�¬â€ 1�71¤7")
#--------------------------------------------------
            elif "Pesan dipilih " in msg.text:
				#if msg.from_ in owner:
					wait["message"] = msg.text.replace("Pesan dipilih ","")
					kr.sendText(msg.to,"message changed")
            elif "Pesan add " in msg.text:
				#if msg.from_ in owner:
					wait["message"] = msg.text.replace("Pesan add ","")
					if wait["lang"] == "JP":
						kr.sendText(msg.to,"message changed")
					else:
						kr.sendText(msg.to,"doneÃ£â‚¬â�1�7�1�71¤7 1�71¤7")
#--------------------------------------------------
            elif msg.text in ["Pesan","pesan"]:
				#if msg.from_ in owner:
					if wait["lang"] == "JP":
						kr.sendText(msg.to,"message change to\n\n" + wait["message"])
					else:
						kr.sendText(msg.to,"The automatic appending information is set as followsÃ£â‚¬â�1�7�1�71¤7š\n\n" + wait["message"])
#--------------------------------------------------
            elif "Komen " in msg.text:
				#if msg.from_ in owner:
					c = msg.text.replace("Komen ","")
					if c in [""," ","\n",None]:
						kr.sendText(msg.to,"message changed")
					else:
						wait["comment"] = c
						kr.sendText(msg.to,"changed\n\n" + c)
#--------------------------------------------------
            elif "Add komen " in msg.text:
				#if msg.from_ in owner:
					c = msg.text.replace("Add komen ","")
					if c in [""," ","\n",None]:
						kr.sendText(msg.to,"String that can not be changed")
					else:
						wait["comment"] = c
						kr.sendText(msg.to,"changed\n\n" + c)
            elif msg.text in ["Komen on","komen on"]:
				#if msg.from_ in owner:
					if wait["commentOn"] == True:
						if wait["lang"] == "JP":
							kr.sendText(msg.to,"done")
						else:
							kr.sendText(msg.to,"already on")
					else:
						wait["commentOn"] = True
						if wait["lang"] == "JP":
							kr.sendText(msg.to,"done")
						else:
							kr.sendText(msg.to,"Ã¨Â¦ÂÃ¤Âºâ€ Ã¥Â¼â�1�7�¬Ã£â�1�7�¬â�1�7�1�71¤7 1�71¤7")
            elif msg.text in ["Komen on","komen on"]:
				#if msg.from_ in owner:
					if wait["commentOn"] == False:
						if wait["lang"] == "JP":
							kr.sendText(msg.to,"done")
						else:
							kr.sendText(msg.to,"already off")
					else:
						wait["commentOn"] = False
						if wait["lang"] == "JP":
							kr.sendText(msg.to,"done")
						else:
							kr.sendText(msg.to,"Ã¨Â¦ÂÃ¤Âºâ€ Ã¥â�1�7�1�71¤7¦Â³Ã¦â 1�71¤7“Â­Ã£â�1�7�¬â€ 1�71¤7")
            elif msg.text in ["Comment","Ã§â€¢â�1�7�¢Ã¨Â¨â�1�7�¬Ã§Â¢ÂºÃ¨ÂªÂ�1�7�1�71¤7"]:
				#if msg.from_ in owner:
					kr.sendText(msg.to,"message changed to\n\n" + str(wait["comment"]))
            elif msg.text in ["Gurl"]:
				#if msg.from_ in owner:
					if msg.toType == 2:
						x = kr.getGroup(msg.to)
						if x.preventJoinByTicket == True:
							x.preventJoinByTicket = False
							kr.updateGroup(x)
						gurl = kr.reissueGroupTicket(msg.to)
						kr.sendText(msg.to,"line://ti/g/" + gurl)
					else:
						if wait["lang"] == "JP":
							kr.sendText(msg.to,"Can't be used outside the group")
						else:
							kr.sendText(msg.to,"Not for use less than group")

            elif msg.text in ["Jam on"]:
				#if msg.from_ in owner:
					if wait["clock"] == True:
						kr.sendText(msg.to,"already on")
					else:
						wait["clock"] = True
						now2 = datetime.now()
						nowT = datetime.strftime(now2,"(%H:%M)")
						profile = kr.getProfile()
						profile.displayName = wait["cName"] + nowT
						kr.updateProfile(profile)
						kr.sendText(msg.to,"done")
            elif msg.text in ["Jam off"]:
				#if msg.from_ in owner:
					if wait["clock"] == False:
						kr.sendText(msg.to,"already off")
					else:
						wait["clock"] = False
						kr.sendText(msg.to,"done")
            elif msg.text in ["Pilih waktu "]:
				#if msg.from_ in owner:
					n = msg.text.replace("Pilih waktu ","")
					if len(n.decode("utf-8")) > 13:
						kr.sendText(msg.to,"changed")
					else:
						wait["cName"] = n
						kr.sendText(msg.to,"changed to\n\n" + n)
            elif msg.text in ["Up"]:
				#if msg.from_ in owner:
					if wait["clock"] == True:
						now2 = datetime.now()
						nowT = datetime.strftime(now2,"(%H:%M)")
						profile = kr.getProfile()
						profile.displayName = wait["cName"] + nowT
						kr.updateProfile(profile)
						kr.sendText(msg.to,"Updated")
					else:
						kr.sendText(msg.to,"Please turn on the name clock")


            elif msg.text == "Cctv":
                    kr.sendText(msg.to, "Check sider"),
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['ROM'][msg.to] = {}
                    print wait2
            elif msg.text == "Toong":
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"

                        kr.sendText(msg.to, "People who readed %s\nthat's it\n\nPeople who have ignored reads\n%sIt is abnormal \n\nReading point creation date n time:\n[%s]"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        kr.sendText(msg.to, "An already read point has not been set.\n¡¸Cctv¡¹you can send  read point will be created ")

            elif "cctv on" == msg.text.lower():
                if msg.to in wait2['readPoint']:
                        try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                        except:
                            pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        with open('sider.json', 'w') as fp:
                         json.dump(wait2, fp, sort_keys=True, indent=4)
                         kr.sendText(msg.to,"Cctv sudah menyala silahkan masukan command [Check]")
                else:
                    try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                    except:
                          pass
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                    wait2['ROM'][msg.to] = {}
                    with open('sider.json', 'w') as fp:
                     json.dump(wait2, fp, sort_keys=True, indent=4)
                     kr.sendText(msg.to, "Set reading point:\n" + datetime.now().strftime('%H:%M:%S'))
                     print wait2

                    
            elif "cctv off" == msg.text.lower():
                if msg.to not in wait2['readPoint']:
                    kr.sendText(msg.to,"Set Reading point tidak di temukan")
                    kr.sendText(msg.to,"Silahkan masukan Command [Cctv on] untuk set point")
                else:
                    try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                    except:
                          pass
                    kr.sendText(msg.to, "Delete reading point:\n" + datetime.now().strftime('%H:%M:%S'))
                    
            elif "check" == msg.text.lower():
                    if msg.to in wait2['readPoint']:
                        if wait2['ROM'][msg.to].items() == []:
                             kr.sendText(msg.to, "Reader:\nNone")
                        else:
                            chiya = []
                            for rom in wait2['ROM'][msg.to].items():
                                chiya.append(rom[1])
                               
                            cmem = kr.getContacts(chiya)
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = ''
                        for x in range(len(cmem)):
                                xname = str(cmem[x].displayName)
                                pesan = ''
                                pesan2 = pesan+"@a\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                zx2.append(zx)
                                zxc += pesan2
                                msg.contentType = 0
           
                        print zxc
                        msg.text = xpesan+ zxc + "\nBefore: %s\nAfter: %s"%(wait2['setTime'][msg.to],datetime.now().strftime('%H:%M:%S'))
                        lol ={"MENTION":str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                        print lol
                        msg.contentMetadata = lol
                        try:
                          kr.sendMessage(msg)
                        except Exception as error:
                              print error
                        pass
               
           
                    else:
                        kr.sendText(msg.to, "cctv has not been set.")
#-----------------------------------------------
            elif msg.text in ["Crot","nah","Nah"]:
                              group = kr.getGroup(msg.to)
                              nama = [contact.mid for contact in group.members]
                              nm1, nm2, nm3, nm4, jml = [], [], [], [], len(nama)
                              if jml <= 100:
                                 summon(msg.to, nama)
                              if jml > 100 and jml < 200:
                                 for i in range (0, 99):
                                        nm1 += [nama[i]]
                                 summon(msg.to, nm1)
                                 for j in range (100, len(nama)-1):
                                        nm2 += [nama[j]]
                                 summon(msg.to, nm2)
                              if jml > 200 and jml < 300:
                                 for i in range (0, 99):
                                        nm1 += [nama[i]]
                                 summon(msg.to, nm1)
                                 for j in range (100, 199):
                                        nm2 += [nama[j]]
                                 summon(msg.to, nm2)
                                 for k in range (200, len(nama)-1):
                                        nm3 += [nama[k]]
                                 summon(msg.to, nm3)
                              if jml > 300 and jml < 400:
                                 for i in range (0, 99):
                                        nm1 += [nama[i]]
                                 summon(msg.to, nm1)
                                 for j in range (100, 199):
                                        nm2 += [nama[j]]
                                 summon(msg.to, nm2)
                                 for k in range (200, 299):
                                        nm3 += [nama[k]]
                                 summon(msg.to, nm3)
                                 for l in range (300, len(nama)-1):
                                     nm4 += [nama[l]]
                                 summon(msg.to, nm4)
                              cnt = Message()
                              cnt.text = "Hasil Tag : "+str(jml)
                              cnt.to = msg.to
                              kr.sendText(msg.to,"TAGALL SUCCESS")
                              kr.sendMessage(cnt)
#-----------------------------------------------
#-----------------------------------------------
            elif msg.text in ["Kill"]:
				#if msg.from_ in owner:
					if msg.toType == 2:
						group = kr.getGroup(msg.to)
						gMembMids = [contact.mid for contact in group.members]
						matched_list = []
						for tag in wait["blacklist"]:
							matched_list+=filter(lambda str: str == tag, gMembMids)
						if matched_list == []:
							kr.sendText(msg.to,"Maaf ya")
							return
						for jj in matched_list:
							try:
								klist=[kr]
								kicker=random.choice(klist)
								kicker.kickoutFromGroup(msg.to,[jj])
								print (msg.to,[jj])
							except:
								print

            elif "Glist" in msg.text:
                #if msg.from_ in owner:
                        gid = kr.getGroupIdsJoined()
                        h = ""
                        for i in gid:
                            h += "☄ %s  \n" % (kr.getGroup(i).name + " 👥 ▄ [ " + str(len (kr.getGroup(i).members))+" ]")
                        kr.sendText(msg.to, "     ☄ [ ♡List Grup♄ ] ☜\n"+ h +"Total Group ▄" +"[ "+str(len(gid))+" ]")
            elif "Bersihkan" in msg.text:
				#if msg.from_ in owner:
					if msg.toType == 2:
						print "ok"
						_name = msg.text.replace("Bersihkan","")
						gs = kr.getGroup(msg.to)
						kr.sendText(msg.to,"Group DiBersihkan....!!!!")
						targets = []
						for g in gs.members:
							if _name in g.displayName:
								targets.append(g.mid)
						if targets == []:
							kr.sendText(msg.to,"Tidak di temukan..!!")
						else:
							for target in targets:
							    if target not in owner:
    								try:
    									klist=[kr]
    									kicker=random.choice(klist)
    									kicker.kickoutFromGroup(msg.to,[target])
    									print (msg.to,[g.mid])
    								except:
    									kr.sendText(msg.to,"Group Dibersihkan,, Makasih...!!!")
            elif msg.text in ["Salam1"]:
                kr.sendText(msg.to,"السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                kr.sendText(msg.to,"Assalamu'alaikum")
            elif msg.text in ["Salam2"]:
                kr.sendText(msg.to,"وَعَلَيْكُمْ السَّلاَمُرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                kr.sendText(msg.to,"Wa'alaikumsallam.Wr,Wb")
            elif "Salam3" in msg.text:
              #if msg.from_ in owner:
                kr.sendText(msg.to,"السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                kr.sendText(msg.to,"Assalamu'alaikum")
                kr.sendText(msg.to,"وَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِوَبَرَكَاتُهُ")
                kr.sendText(msg.to,"Wa'alaikumsallam.Wr,Wb")
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("Salam3","")
                    gs = kr.getGroup(msg.to)
                    kr.sendText(msg.to,"Qo salamnya gak ada yang jawab ya..!!")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        kr.sendText(msg.to,"Tidak di temukan...!!")
                    else:
                        for target in targets:
                          if target not in owner:
                            try:
                                klist=[kr]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                kr.sendText(msg.to,"السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                                kr.sendText(msg.to,"وَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِوَبَرَكَاتُهُ")
                                kr.sendText(msg.to,"Nah salamnya jadi dijawab sendiri dah")


#-----------------------------------------------
            elif msg.text == "Cctv":
                    kr.sendText(msg.to, "Lurking Is Starting!! "+ datetime.today().strftime('%H:%M:%S'))
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    now2 = datetime.now()
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['ROM'][msg.to] = {}
                    wait2['setTime'][msg.to] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                    print wait2

            elif msg.text in ["Intip"]:
                 if msg.toType == 2:
                    print "\nRead aktif..."
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"
                        kr.sendText(msg.to, "Sider :\n  ===========================                     %s\n===========================\n\nReader :\n%s\n===========================\nIn the last seen point:\n[%s]\n===========================" % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                        print "\nReading Point Set..."
                        try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                        except:
                            pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        print "lukers"
                        kr.sendText(msg.to, "Auto Read Point!!" + (wait2['setTime'][msg.to]))
                    else:
                        kr.sendText(msg.to, "Ketik [Cctv] for [Intip]")
            elif "cek" == msg.text.lower():
                    if msg.to in wait2['readPoint']:
                        if wait2['ROM'][msg.to].items() == []:
                             kr.sendText(msg.to, "Reader:\nNone")
                        else:
                            chiya = []
                            for rom in wait2['ROM'][msg.to].items():
                                chiya.append(rom[1])
                               
                            cmem = kr.getContacts(chiya)
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = ''
                        for x in range(len(cmem)):
                                xname = str(cmem[x].displayName)
                                pesan = ''
                                pesan2 = pesan+"@a\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                zx2.append(zx)
                                zxc += pesan2
                                msg.contentType = 0
           
                        print zxc
                        msg.text = xpesan+ zxc + "\nBefore: %s\nAfter: %s"%(wait2['setTime'][msg.to],datetime.now().strftime('%H:%M:%S'))
                        lol ={"MENTION":str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                        print lol
                        msg.contentMetadata = lol
                        try:
                          kr.sendMessage(msg)
                        except Exception as error:
                              print error
                        pass
               
           
                    else:
                        kr.sendText(msg.to, "Lurking has not been set.")
#-------------------------------------
            elif "Cn " in msg.text:
              #if msg.from_ in owner:
                string = msg.text.replace("Cn ","")
                if len(string.decode('utf-8')) <= 500:
                    profile = kr.getProfile()
                    profile.displayName = string
                    kr.updateProfile(profile)
                    kr.sendText(msg.to,"UpdateName => " + string + " <= Success")
#----------------------------
            elif "Cium " in msg.text:
                #if msg.from_ in owner:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"] [0] ["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            kr.kickoutFromGroup(msg.to,[target])
                        except:
                            kr.sendText(msg.to,"Error")
            elif "Admadd @" in msg.text:
                #if msg.from_ in owner:
                    print "[Command]Staff add executing"
                    _name = msg.text.replace("Admadd @","")
                    _nametarget = _name.rstrip('  ')
                    gs = kr.getGroup(msg.to)
                    gs = kr.getGroup(msg.to)
                    gs = kr.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        kr.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                admin.append(target)
                                kr.sendText(msg.to,"Admin Telah Ditambahkan")
                            except:
                                pass
                    print "[Command]Staff add executed"


            elif "Admrem @" in msg.text:
                #if msg.from_ in owner:
                    print "[Command]Staff remove executing"
                    _name = msg.text.replace("Admrem @","")
                    _nametarget = _name.rstrip('  ')
                    gs = kr.getGroup(msg.to)
                    gs = kr.getGroup(msg.to)
                    gs = kr.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        kr.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                admin.remove(target)
                                kr.sendText(msg.to,"Admin Telah Dihapus")
                            except:
                                pass
                    print "[Command]Staff remove executed"

            elif msg.text in ["Adminlist","admlist"]:
              #if msg.from_ in owner:
                if admin == []:
                    kr.sendText(msg.to,"The adminlist is empty")
                else:
                    kr.sendText(msg.to,"Sabar Dikit Boss.....")
                    mc = ""
                    for mi_d in admin:
                        mc += "╠❂➣ " +kr.getContact(mi_d).displayName + "\n"
                    kr.sendText(msg.to,mc)
                    print "[Command]Stafflist executed"
#-----------------------------------------------
            elif msg.text.lower() == 'crash':
                #if msg.from_ in owner:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "ua7fb5762d5066629323d113e1266e8ca',"}
                    kr.sendMessage(msg)
                    kr.sendMessage(msg)
                    kr.sendMessage(msg)
#-----------------------------------------------
#-----------------------------------------------
            elif msg.text in ["Mode On","mode on"]:
                #if msg.from_ in owner:
                    if wait["Wc"] == True:
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"noтιғ joιn on")
                    else:
                        wait["Wc"] = True
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"already on")
                    if wait["Lv"] == True:
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"noтιғ leave on")
                    else:
                        wait["Lv"] = True
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"already on")
                    if wait["tag"] == True:
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"Already on")
                        else:
                            kr.sendText(msg.to,"Tag On")
                    else:
                        wait["tag"] = True
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"Tag On")
                        else:
                            kr.sendText(msg.to,"already on")
                    if wait['detectMention'] == True:
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"Auto respon tag Pict On")
                        else:
                            kr.sendText(msg.to,"Auto respon tag Pict On")
                    else:
                        wait['detectMention'] = True
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"Auto respon tag Pict On")
                        else:
                            kr.sendText(msg.to,"Auto respon tag Pict On")
                            
#=================================================
            elif msg.text in ["Mode Off","mode off"]:
                #if msg.from_ in owner:
                    if wait["Wc"] == False:
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"noтιғ joιn oғғ")
                    else:
                        wait["Wc"] = False
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"Nayapa yg gabung already oғғ")
                    if wait["Lv"] == False:
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"noтιғ leave oғғ")
                    else:
                        wait["Lv"] = False
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"Nayapa yg left already oғғ")
                    if wait["tag"] == False:
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"Already Tag off")
                        else:
                            kr.sendText(msg.to,"Tag Off")
                    else:
                        wait["tag"] = False
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"Tag Off")
                        else:
                            kr.sendText(msg.to,"Already Tag off")
                    if wait['detectMention'] == False:
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"Auto respon tag Pict Off")
                        else:
                            kr.sendText(msg.to,"Auto respon tag Pict Off")
                    else:
                        wait['detectMention'] = False
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"Auto respon tag Pict Off")
                        else:
                            kr.sendText(msg.to,"Auto respon tag Pict Off")
#===================================================
 
            elif msg.text in ["Respoto on","respoto on"]:
                #if msg.from_ in owner:
                    wait['detectMention'] = True
                    kr.sendText(msg.to,"Auto respon tag Pict On")
                
            elif msg.text in ["Respoto off","respoto off"]:
                #if msg.from_ in owner:
                    wait['detectMention'] = False
                    kr.sendText(msg.to,"Auto respon tag Pict Off")
#-----------------------------------------------

            elif ".. " in msg.text:
					bctxt = msg.text.replace(".. ","")
					kr.sendText(msg.to,(bctxt))
					kr.sendText(msg.to,(bctxt))
            elif msg.text in ["Creator"]:
					msg.contentType = 13
					msg.contentMetadata = {'mid': "u31ef22df7f538df1d74dc7f756ef1a32"}
					ki.sendMessage(msg)
					msg.contentType = 13
					msg.contentMetadata = {'mid': "u9cc2323f5b84f9df880c33aa9f9e3ae1"}
					ki.sendMessage(msg)
					url = ("https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26229822_136061360519754_2383391381158562768_n.jpg?oh=5b629e008c344ab9120798423a1fe9fe&oe=5ABEC25F")
					kr.sendImageWithURL(msg.to, url)
					kr.sendText(msg.to,"MyCreator\nyang bikin Bot ini...!!!")
					
#-------------Fungsi Creator Finish-----------------#
            elif "Spam " in msg.text:
                #if msg.from_ in owner:
                    txt = msg.text.split(" ")
                    jmlh = int(txt[2])
                    teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+" ","")
                    tulisan = jmlh * (teks+"\n")
                    
                    if txt[1] == "on":
                        if jmlh <= 100000:
                           for x in range(jmlh):
                               kr.sendText(msg.to, teks)
                        else:
                           kr.sendText(msg.to, "Out of Range!")
                    elif txt[1] == "off":
                        if jmlh <= 100000:
                            kr.sendText(msg.to, tulisan)
                        else:
                            kr.sendText(msg.to, "Out Of Range!")
#----------------------------------------------------
            elif "Cs " in msg.text:
              #if msg.from_ in owner:
                string = msg.text.replace("Cs","")
                if len(string.decode('utf-8')) <= 500:
                    profile = kr.getProfile()
                    profile.statusMessage = string
                    kr.updateProfile(profile)
                else:
                    kr.sendText(msg.to,"Done")
#-----------------------------------------------
            elif "v " in msg.text.lower():
                say = msg.text.lower().replace("v ","")
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                kr.sendAudio(msg.to,"hasil.mp3")
#--------------------
            elif 'wiki ' in msg.text.lower():
                try:
                    wiki = msg.text.lower().replace("wiki ","")
                    wikipedia.set_lang("id")
                    pesan="Title ("
                    pesan+=wikipedia.page(wiki).title
                    pesan+=")\n\n"
                    pesan+=wikipedia.summary(wiki, sentences=3)
                    pesan+="\n"
                    pesan+=wikipedia.page(wiki).url
                    kr.sendText(msg.to, pesan)
                except:
                        try:
                            pesan="Over Text Limit! Please Click link\n"
                            pesan+=wikipedia.page(wiki).url
                            kr.sendText(msg.to, pesan)
                        except Exception as e:
                            kr.sendText(msg.to, str(e))
#-----------------------------------------------
            elif "Apakah " in msg.text:
                tanya = msg.text.replace("Apakah ","")
                jawab = ("Ya","Tidak","Bisa Jadi","Mungkin")
                jawaban = random.choice(jawab)
                kr.sendText(msg.to,jawaban)
                kr.sendText(msg.to,jawaban)
                kr.sendText(msg.to,jawaban)
                
            elif msg.text in ["Nah","nah"]:
                kr.sendText(msg.to,"Kan")
                kr.sendText(msg.to,"Kan")
                kr.sendText(msg.to,"Kan")
                
#-----------------------------------------------
            elif "Rate " in msg.text:
                tanya = msg.text.replace("Rate ","")
                jawab = ("10%","20%","30%","40%","50%","60%","70%","80%","90%","100%")
                jawaban = random.choice(jawab)
                kr.sendText(msg.to,jawaban)
#-----------------------------------------------
            elif "Ambilnama @" in msg.text:
                #if msg.from_ in owner:
                    _name = msg.text.replace("Ambilnama @","")
                    _nametarget = _name.rstrip(" ")
                    gs = kr.getGroup(msg.to)
                    for h in gs.members:
                      if _nametarget == h.displayName:
                          kr.sendText(msg.to,"[DisplayName]:\n" + h.displayName )
                      else:
                        pass

            elif "Ambilbio @" in msg.text:
                #if msg.from_ in owner:
                    _name = msg.text.replace("Ambilbio @","")
                    _nametarget = _name.rstrip(" ")
                    gs = kr.getGroup(msg.to)
                    for h in gs.members:
                      if _nametarget == h.displayName:
                          kr.sendText(msg.to,"[Status]:\n" + h.statusMessage )
                      else:
                        pass
#-----------------------------------------------
#-----------------------------------------------
            elif "zodiak " in msg.text:
                tanggal = msg.text.replace("zodiak ","")
                r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                data=r.text
                data=json.loads(data)
                lahir = data["data"]["lahir"]
                usia = data["data"]["usia"]
                ultah = data["data"]["ultah"]
                zodiak = data["data"]["zodiak"]
                kr.sendText(msg.to,"Tanggal Lahir: "+lahir+"\n\nUsia: "+usia+"\n\nUltah: "+ultah+"\n\nZodiak: "+zodiak)
#-----------------------------------------------
            elif msg.text in ["Invite creator"]:
                    ginfo = kr.getGroup(msg.to)
                    gCreator = ginfo.creator.mid
                    try:
                       kr.findAndAddContactsByMid(gCreator)
                       kr.inviteIntoGroup(msg.to,[gCreator])
                       print "success inv gCreator"
                    except:
                       pass

            elif msg.text in ["Gcreator:kick"]:
	           #if msg.from_ in owner:
                    ginfo = kr.getGroup(msg.to)
                    gCreator = ginfo.creator.mid
                    try:
                       kr.findAndAddContactsByMid(gCreator)
                       kr.kickoutFromGroup(msg.to,[gCreator])
                       print "success inv gCreator"
                    except:
                       pass

#----------------------------------------------
            elif "Stalk " in msg.text:
                #if msg.from_ in owner:
                     print "[Command]Stalk executing"
                     stalkID = msg.text.replace("Stalk ","")
                     subprocess.call(["instaLooter",stalkID,"tmp/","-n","1"])
                     files = glob.glob("tmp/*.jpg")
                     for file in files:
                         os.rename(file,"tmp/tmp.jpg")
                     fileTmp = glob.glob("tmp/tmp.jpg")
                     if not fileTmp:
                         kr.sendText(msg.to, "Image not found, maybe the account haven't post a single picture or the account is private")
                         print "[Command]Stalk,executed - no image found"
                     else:
                         image = upload_tempimage(client)
                         kr.sendText(msg.to, format(image['link']))
                         subprocess.call(["sudo","rm","-rf","tmp/tmp.jpg"])
                         print "[Command]Stalk executed - succes"
#-------------------------------------------------------------
            elif "Gbc " in msg.text:
                #if msg.from_ in owner:
                    bctxt = msg.text.replace("Gbc ", "")
                    n = kr.getGroupIdsJoined()
                    for manusia in n:
                        kr.sendText(manusia, (bctxt) + "\n╠═════[BROADCAST]═════╣\n\n=>>line://ti/p/~krissthea\n●▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬●")
            elif "Pmkesemua " in msg.text:
                #if msg.from_ in owner:
					bctxt = msg.text.replace("Pmkesemua ", "")
					t = kr.getAllContactIds()
					for manusia in t:
						kr.sendText(manusia,(bctxt))
            elif "Fbc " in msg.text:
                #if msg.from_ in owner:
                    bctxt = msg.text.replace("Fbc ", "")
                    t = kr.getAllContactIds()
                    for manusia in t:
                        kr.sendText(manusia, (bctxt))
#----------------------------------------------------------
            elif "Asupka " in msg.text:
                #if msg.from_ in owner:
                    gid = msg.text.replace("Asupka ","")
                    if gid == "":
                        kr.sendText(msg.to,"Invalid group id")
                    else:
                        try:
                            kr.findAndAddContactsByMid(msg.from_)
                            kr.inviteIntoGroup(gid,[msg.from_])
                        except:
                            kr.sendText(msg.to,"Mungkin saya tidak di dalaam grup itu")
#------------------------------------------------------
            elif "Ambilcover @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Ambilcover @","")
                _nametarget = _name.rstrip('  ')
                gs = kr.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    kr.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = kr.getContact(target)
                            cu = kr.channel.getCover(target)
                            path = str(cu)
                            kr.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"
#-----------------------------------------------
            elif "Ambilpp @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Ambilpp @","")
                _nametarget = _name.rstrip('  ')
                gs = kr.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    kr.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = kr.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            kr.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"
#--------------------------------------------
            elif msg.text in ["Autolike on"]:
                #if msg.from_ in owner:
                    if wait["likeOn"] == True:
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"Done。")
                    else:
                        wait["likeOn"] = True
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"Already。")
            elif msg.text in ["Autolike off"]:
                #if msg.from_ in owner:
                    if wait["likeOn"] == False:
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"Done。")
                    else:
                        wait["likeOn"] = False
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"Already")
#------------------------------------------------------------------

            elif "Bot off" in msg.text:
               #if msg.from_ in owner:
                 try:
                     import sys
                     sys.exit()
                     kr.sendText(msg.to, "Bot is Off [telah dimatikan]")
                 except:
                     pass
#------------------------------------------------------------------
#--------------------------
            elif msg.text in ["Sambut on"]:
                if wait["Wc"] == True:
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"noтιғ joιn on")
                else:
                    wait["Wc"] = True
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"already on")
            elif msg.text in ["Sambut off"]:
                if wait["Wc"] == False:
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"noтιғ joιn oғғ")
                else:
                    wait["Wc"] = False
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"already oғғ")
#--------------------------
            elif msg.text in ["pergi on"]:
                if wait["Lv"] == True:
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"noтιғ leave on")
                else:
                    wait["Lv"] = True
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"already on")
            elif msg.text in ["pergi off"]:
                if wait["Lv"] == False:
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"noтιғ leave oғғ")
                else:
                    wait["Lv"] = False
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"already oғғ")
##--------------------------
            elif "musik " in msg.text.lower():
                try:
                    songname = msg.text.lower().replace("musik ","")
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'Ini lah musikmu\n'
                        hasil += 'Judul : ' + song[0]
                        hasil += '\nDurasi : ' + song[1]
                        hasil += '\nLink Download : ' + song[4]
                        kr.sendText(msg.to, hasil)
                        kr.sendText(msg.to, "Di tunggu audionya...")
                        kr.sendAudioWithURL(msg.to, song[4])
                except Exception as njer:
                    kr.sendText(msg.to, str(njer))
#------------------------------------------------
            elif 'lirik ' in msg.text.lower():
                try:
                    songname = msg.text.lower().replace('lirik ','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'Lyric Lagu ('
                        hasil += song[0]
                        hasil += ')\n\n'
                        hasil += song[5]
                        kr.sendText(msg.to, hasil)
                except Exception as wak:
                        kr.sendText(msg.to, str(wak))
#-----------------------------------
            elif "idline " in msg.text:
                id = msg.text.replace("idline ", "")
                find = kr.findContactsByUserId(id)
                for findid in find:
                    try:
                        msg.contentType = 13
                        msg.contentMetadata = {'mid': findid.mid}
                        kr.sendMessage(msg)
                    except Exception as error:
                        print error
#-----------------------------------
            elif "Ambilgroup" in msg.text:
                group = kr.getGroup(msg.to)
                path =("http://dl.profile.line-cdn.net/" + group.pictureStatus)
                kr.sendImageWithURL(msg.to, path)
#----------------------------------
            elif "reinvite" in msg.text.split():
                if msg.toType == 2:
                    group = kr.getGroup(msg.to)
                    if group.invitee is not None:
                        try:
                            grCans = [contact.mid for contact in group.invitee]
                            kr.findAndAddContactByMid(msg.to, grCans)
                            kr.cancelGroupInvitation(msg.to, grCans)
                            kr.inviteIntoGroup(msg.to, grCans)
                        except Exception as error:
                            print error
                    else:
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"No Invited")
                        else:
                            kr.sendText(msg.to,"Error")
                else:
                    pass
#----------------------------------

            elif msg.text in ["LG"]: #Melihat List Group
                #if msg.from_ in owner:
                    gids = kr.getGroupIdsJoined()
                    h = ""
                    for i in gids:
                        #####gn = kr.getGroup(i).name
                        h += "[•]%s Member\n" % (kr.getGroup(i).name   +"👉"+str(len(kr.getGroup(i).members)))
                        kr.sendText(msg.to,"=======[List Group]======\n"+ h +"Total Group :"+str(len(gids)))

            elif msg.text in ["LG2"]: #Melihat List Group + ID Groupnya (Gunanya Untuk Perintah InviteMeTo:)
                #if msg.from_ in owner:
                    gid = kr.getGroupIdsJoined()
                    h = ""
                    for i in gid:
                        h += "[%s]:%s\n" % (kr.getGroup(i).name,i)
                        kr.sendText(msg.to,h)
      #--------------List Group------------
            elif "Asupka: " in msg.text:
                #if msg.from_ in owner:
                    gid = msg.text.replace("Asupka: ","")
                    if gid == "":
                        kr.sendText(msg.to,"Invalid group id")
                    else:
                        try:
                            kr.findAndAddContactsByMid(msg.from_)
                            kr.inviteIntoGroup(gid,[msg.from_])
                        except:
                            kr.sendText(msg.to,"Mungkin saya tidak di dalaam grup itu")
#----------------------------------
            elif "Ambilkontak " in msg.text:
              #if msg.from_ in owner:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                mmid = kr.getContact(key1)
                msg.contentType = 13
                msg.contentMetadata = {"mid": key1}
#----------------------------------
            elif "youtube " in msg.text.lower():
                 query = msg.text.lower().replace("youtube ","")
                 with requests.session() as s:
                     s.headers['user-agent'] = 'Mozilla/5.0'
                     url    = 'http://www.youtube.com/results'
                     params = {'search_query': query}
                     r    = s.get(url, params=params)
                     soup = BeautifulSoup(r.content, 'html5lib')
                     for a in soup.select('.yt-lockup-title > a[title]'):
                         if '&List' not in a['href']:
                             kr.sendText(msg.to,'Judul : ' + a['title'] + '\nLink : ' + 'http://www.youtube.com' + a['href'])
#---------------------------------
            elif "Vidio " in msg.text:
                try:
                    textToSearch = (msg.text).replace("Vidio ", "").strip()
                    query = urllib.quote(textToSearch)
                    url = "https://www.youtube.com/results?search_query=" + query
                    response = urllib2.urlopen(url)
                    html = response.read()
                    soup = BeautifulSoup(html, "html.parser")
                    results = soup.find(attrs={'class':'yt-uix-tile-link'})
                    ght=('https://www.youtube.com' + results['href'])
                    kr.sendVideoWithURL(msg.to,ght)
                except:
                    kr.sendText(msg.to,"Could not find it")
#-----------------------------------------
            elif msg.text.lower() == 'runtime':
                eltime = time.time() - mulai
                van = "Bot sudah berjalan selama "+waktu(eltime)
                kr.sendText(msg.to,van)
#-----------------------------------------
            elif msg.text in ["Restart"]:
                #if msg.from_ in owner:
                    kr.sendText(msg.to, "Bot has been restarted")
                    restart_program()
                    print "@Restart"
#-----------------------------------------
#-----------------------------------------
            elif "Info @" in msg.text:
                nama = msg.text.replace("Info @","")
                target = nama.rstrip(' ')
                van = kr.getGroup(msg.to)
                for linedev in van.members:
                    if target == linedev.displayName:
                        mid = kr.getContact(linedev.mid)
                        #./linedev/ervan
                        try:
                            cover = kr.channel.getCover(linedev.mid)
                        except:
                            cover = ""
                        kr.sendText(msg.to,"[Display Name]:\n" + mid.displayName + "\n[Mid]:\n" + linedev.mid + "\n[BIO]:\n" + mid.statusMessage + "\n[Ava]:\nhttp://dl.profile.line-cdn.net/" + mid.pictureStatus + "\n[Cover]:\n" + str(cover))
                    else:
                        pass

            elif "Info2 " in msg.text:
                mid = msg.text.replace("Info2 ","")
                anu = kr.getContact(mid)
                try:
                    cover = kr.channel.getCover(mid)
                except:
                    cover = ""
                kr.sendText(msg.to,"[Display Name]:\n" + anu.displayName + "\n[Mid]:\n" + mid + "\n[BIO]:\n" + anu.statusMessage + "\n[Ava]:\nhttp://dl.profile.line-cdn.net/" + anu.pictureStatus + "\n[Cover]:\n" + str(cover))
#-----------------------------------------
            elif msg.text in ["Gcreator"]:
              if msg.toType == 2:
                    msg.contentType = 13
                    ginfo = kr.getGroup(msg.to)
                    gCreator = ginfo.creator.mid
                    try:
                        msg.contentMetadata = {'mid': gCreator}
                        gCreator1 = ginfo.creator.displayName

                    except:
                        gCreator = "Error"
                    kr.sendText(msg.to, "Group Creator : " + gCreator1)
                    kr.sendMessage(msg)

            elif msg.text in ["Baca on","Read on"]:
                #if msg.from_ in owner:
                    wait['alwayRead'] = True
                    kr.sendText(msg.to,"Auto read On")
                
            elif msg.text in ["Baca off","Read off"]:
                #if msg.from_ in owner:
                    wait['alwayRead'] = False
                    kr.sendText(msg.to,"Auto read Off")
#-----------------------------------------------
            elif msg.text in ["Tag on"]:
                if wait["tag"] == True:
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"Already on")
                    else:
                        kr.sendText(msg.to,"Tag On")
                else:
                    wait["tag"] = True
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"Tag On")
                    else:
                        kr.sendText(msg.to,"already on")
            elif msg.text in ["Tag off"]:
                if wait["tag"] == False:
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"Already off")
                    else:
                        kr.sendText(msg.to,"Tag Off")
                else:
                    wait["tag"] = False
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"Tag Off")
                    else:
                        kr.sendText(msg.to,"Already off")

            elif msg.text in ["Tag2 on"]:
                #if msg.from_ in owner:
                    if wait["tag2"] == True:
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"Already on")
                        else:
                            kr.sendText(msg.to,"Tag On")
                    else:
                        wait["tag2"] = True
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"Tag On")
                        else:
                            kr.sendText(msg.to,"already on")
            elif msg.text in ["Tag2 off"]:
                #if msg.from_ in owner:
                    if wait["tag2"] == False:
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"Already off")
                        else:
                            kr.sendText(msg.to,"Tag Off")
                    else:
                        wait["tag2"] = False
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"Tag Off")
                        else:
                            kr.sendText(msg.to,"Already off")

            elif msg.text in ["Auto on"]:
                #if msg.from_ in owner:
                    if wait["auto"] == True:
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"Bot join on")
                        else:
                            kr.sendText(msg.to,"Bot join On")
                    else:
                        wait["auto"] = True
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"Bot join On")
                        else:
                            kr.sendText(msg.to,"Bot join On")
            elif msg.text in ["Auto off"]:
                #if msg.from_ in owner:
                    if wait["auto"] == False:
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"Bot join off")
                        else:
                            kr.sendText(msg.to,"Bot join off")
                    else:
                        wait["auto"] = False
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"Bot join off")
                        else:
                            kr.sendText(msg.to,"Bot join off")

#-----------------------------------------------
            elif "Setimage " in msg.text:
                #if msg.from_ in owner:
                    wait["Pap"] = msg.text.replace("Setimage ","")
                    kr.sendText(msg.to,"Image Has Ben Set To")

            elif msg.text in ["Papimage","/Papim"]:
                #if msg.from_ in owner:
                    kr.sendImageWithURL(msg.to,wait["Pap"])
            elif "Setvideo " in msg.text:
                #if msg.from_ in owner:
                    wait["Vid"] = msg.text.replace("Setvideo ","")
                    kr.sendText(msg.to,"Video Has Ben Set To")

            elif msg.text in ["Papvideo","/Papvid"]:
                #if msg.from_ in owner:
                    kr.sendVideoWithURL(msg.to,wait["Vid"])
#-----------------------------------------------
            elif "Salin @" in msg.text:
                #if msg.from_ in owner:
                    if msg.toType == 2:
                        #if msg.from_ in owner:
                            print "[COPY] Ok"
                            _name = msg.text.replace("Salin @","")
                            _nametarget = _name.rstrip('  ')
                            gs = kr.getGroup(msg.to)
                            targets = []
                            for g in gs.members:
                                if _nametarget == g.displayName:
                                    targets.append(g.mid)
                            if targets == []:
                                kr.sendText(msg.to, "Not Found...")
                            else:
                                for target in targets:
                                    try:
                                        kr.CloneContactProfile(target)
                                        kr.sendText(msg.to, "Succes Copy profile")
                                    except Exception as e:
                                        print e

            elif msg.text in ["Kembali"]:
                #if msg.from_ in owner:
                    try:
                        kr.updateDisplayPicture(backup.pictureStatus)
                        kr.updateProfile(backup)
                        kr.sendText(msg.to, "backup done")
                    except Exception as e:
                        kr.sendText(msg.to, str (e))

#--------------------------------------
            elif msg.text in ["Time"]:
                timeNow = datetime.now()
                timeHours = datetime.strftime(timeNow,"(%H:%M)")
                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                inihari = datetime.today()
                hr = inihari.strftime('%A')
                bln = inihari.strftime('%B')
                for i in range(len(day)):
                    if hr == day[i]: hasil = hari[i]
                for k in range(0, len(bulan)):
                    if bln == str(k): bln = bulan[k-1]
                rst = hasil + ", " + inihari.strftime('%d') + " - " + bln + " - " + inihari.strftime('%Y') + "\nJam : [ " + inihari.strftime('%H:%M:%S') + " ]"
                kr.sendText(msg.to, rst)
                #client.sendText(msg.to, rst)
#-----------------------------------------------
            elif "gbr " in msg.text:
                search = msg.text.replace("gbr ", "")
                url = 'https://www.google.com/search?espv=2&biw=1366&bih=667&tbm=isch&oq=kuc&aqs=mobile-gws-lite.0.0l5&q=' + search
                raw_html = (download_page(url))
                items = []
                items = items + (_images_get_all_items(raw_html))
                path = random.choice(items)
                print path
                try:
                    kr.sendImageWithURL(msg.to,path)
                except:
                    pass
                
            elif "Gbr " in msg.text:
                search = msg.text.replace("Gbr ", "")
                url = 'https://www.google.com/search?espv=2&biw=1366&bih=667&tbm=isch&oq=kuc&aqs=mobile-gws-lite.0.0l5&q=' + search
                raw_html = (download_page(url))
                items = []
                items = items + (_images_get_all_items(raw_html))
                path = random.choice(items)
                print path
                try:
                    kr.sendImageWithURL(msg.to,path)
                except:
                    pass

            elif msg.text in ["cab","Cab"]:
                url = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26168676_131451404314083_3952554270011807487_n.jpg?oh=6e90aa78daaf5e06b1078bbf15d5aa0f&oe=5AB9882D"
                kr.sendImageWithURL(msg.to, url)
                
            elif msg.text in ["cab1","Cab1"]:
                url = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26165506_131451400980750_8433498092579272217_n.jpg?oh=c85beaa35a6f5babd638edeaac9bccaa&oe=5AF760B2"
                kr.sendImageWithURL(msg.to, url)
                
            elif msg.text in ["cab2","Cab2"]:
                url = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26168227_131451417647415_680587542176648285_n.jpg?oh=e714a97fec8d8c1e178ab6c0a3ca39cf&oe=5AC96AD3"
                kr.sendImageWithURL(msg.to, url)
                
            elif msg.text in ["cab3","Cab3"]:
                url = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26195387_131462840979606_8781956575640573461_n.jpg?oh=27ba5e875917c20df7dd8916bdd64847&oe=5ABB27F4"
                kr.sendImageWithURL(msg.to, url)
                
            elif msg.text in ["cab4","Cab4"]:
                url = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26111928_131462844312939_2544207656543605714_n.jpg?oh=0fac796564e963d8b573826263bbc6c7&oe=5AFA67A8"
                kr.sendImageWithURL(msg.to, url)
                
            elif msg.text in ["cab5","Cab5"]:
                url = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26219732_131462837646273_1213898565647052451_n.jpg?oh=c5a8bcce115cdab488bde1b8e981e5dd&oe=5AC3A96E"
                kr.sendImageWithURL(msg.to, url)
                
            elif msg.text in ["cab6","Cab6"]:
                url = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26167549_131462897646267_3496884138024907307_n.jpg?oh=edc63b98f790e9bf2cbb57dce7df9b25&oe=5AB0DDF6"
                kr.sendImageWithURL(msg.to, url)
                
            elif msg.text in ["cab7","Cab7"]:
                url = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26111931_131462894312934_151942458148573227_n.jpg?oh=2b0473a6caf4446df430180a47ca3355&oe=5AC37B56"
                kr.sendImageWithURL(msg.to, url)
                
            elif msg.text in ["Team","Logo"]:
                #if msg.from_ in owner:
                    url = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26168676_131451404314083_3952554270011807487_n.jpg?oh=6e90aa78daaf5e06b1078bbf15d5aa0f&oe=5AB9882D"
                    url1 = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26165506_131451400980750_8433498092579272217_n.jpg?oh=c85beaa35a6f5babd638edeaac9bccaa&oe=5AF760B2"
                    url2 = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26168227_131451417647415_680587542176648285_n.jpg?oh=e714a97fec8d8c1e178ab6c0a3ca39cf&oe=5AC96AD3"
                    url3 = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26195387_131462840979606_8781956575640573461_n.jpg?oh=27ba5e875917c20df7dd8916bdd64847&oe=5ABB27F4"
                    url4 = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26111928_131462844312939_2544207656543605714_n.jpg?oh=0fac796564e963d8b573826263bbc6c7&oe=5AFA67A8"
                    url5 = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26219732_131462837646273_1213898565647052451_n.jpg?oh=c5a8bcce115cdab488bde1b8e981e5dd&oe=5AC3A96E"
                    url6 = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26167549_131462897646267_3496884138024907307_n.jpg?oh=edc63b98f790e9bf2cbb57dce7df9b25&oe=5AB0DDF6"
                    url7 = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26111931_131462894312934_151942458148573227_n.jpg?oh=2b0473a6caf4446df430180a47ca3355&oe=5AC37B56"
                    kr.sendImageWithURL(msg.to, url)
                    kr.sendImageWithURL(msg.to, url1)
                    kr.sendImageWithURL(msg.to, url2)
                    kr.sendImageWithURL(msg.to, url3)
                    kr.sendImageWithURL(msg.to, url4)
                    kr.sendImageWithURL(msg.to, url5)
                    kr.sendImageWithURL(msg.to, url6)
                    kr.sendImageWithURL(msg.to, url7)
                
            elif msg.text in ["Kibar","kibar"]:
                url = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26168676_131451404314083_3952554270011807487_n.jpg?oh=6e90aa78daaf5e06b1078bbf15d5aa0f&oe=5AB9882D"
                url1 = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26165506_131451400980750_8433498092579272217_n.jpg?oh=c85beaa35a6f5babd638edeaac9bccaa&oe=5AF760B2"
                url6 = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26167549_131462897646267_3496884138024907307_n.jpg?oh=edc63b98f790e9bf2cbb57dce7df9b25&oe=5AB0DDF6"
                url7 = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26111931_131462894312934_151942458148573227_n.jpg?oh=2b0473a6caf4446df430180a47ca3355&oe=5AC37B56"
                kr.sendImageWithURL(msg.to, url)
                kr.sendImageWithURL(msg.to, url1)
                kr.sendImageWithURL(msg.to, url6)
                kr.sendImageWithURL(msg.to, url7)
#-----------------------------------------------
            elif 'ig ' in msg.text.lower():
                try:
                    instagram = msg.text.lower().replace("ig ","")
                    html = requests.get('https://www.instagram.com/' + instagram + '/?')
                    soup = BeautifulSoup(html.text, 'html5lib')
                    data = soup.find_all('meta', attrs={'property':'og:description'})
                    text = data[0].get('content').split()
                    data1 = soup.find_all('meta', attrs={'property':'og:image'})
                    text1 = data1[0].get('content').split()
                    user = "Name: " + text[-2] + "\n"
                    user1 = "Username: " + text[-1] + "\n"
                    followers = "Followers: " + text[0] + "\n"
                    following = "Following: " + text[2] + "\n"
                    post = "Post: " + text[4] + "\n"
                    link = "Link: " + "https://www.instagram.com/" + instagram
                    detail = "========INSTAGRAM INFO USER========\n"
                    details = "\n========INSTAGRAM INFO USER========"
                    kr.sendText(msg.to, detail + user + user1 + followers + following + post + link + details)
                    kr.sendImageWithURL(msg.to, text1[0])
                except Exception as njer:
                	kr.sendText(msg.to, str(njer))
#-----------------------------------------------
            elif "Tr-id " in msg.text:
                nk0 = msg.text.replace("Tr-id ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'id')
                kr.sendText(msg.to,str(trans))
            elif "Tr-th " in msg.text:
                nk0 = msg.text.replace("Tr-th ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'th')
                kr.sendText(msg.to,str(trans))
            elif "Tr-ja " in msg.text:
                nk0 = msg.text.replace("Tr-ja ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'ja')
                kr.sendText(msg.to,str(trans))
            elif "Tr-en " in msg.text:
                nk0 = msg.text.replace("Tr-en ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'en')
                kr.sendText(msg.to,str(trans))
            elif "Tr-ms " in msg.text:
                nk0 = msg.text.replace("Tr-ms ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'ms')
                kr.sendText(msg.to,str(trans))
            elif "Tr-it " in msg.text:
                nk0 = msg.text.replace("Tr-it ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'it')
                kr.sendText(msg.to,str(trans))
            elif "Tr-tr " in msg.text:
                nk0 = msg.text.replace("Tr-tr ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'tr')
                kr.sendText(msg.to,str(trans))
            elif "Tr-my " in msg.text:
                nk0 = msg.text.replace("Tr-my ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'my')
                kr.sendText(msg.to,str(trans))
            elif "Tr-af " in msg.text:
                nk0 = msg.text.replace("Tr-af ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'af')
                kr.sendText(msg.to,str(trans))
            elif "Tr-sq " in msg.text:
                nk0 = msg.text.replace("Tr-sq ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'sq')
                kr.sendText(msg.to,str(trans))
            elif "Tr-am " in msg.text:
                nk0 = msg.text.replace("Tr-am ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'am')
                kr.sendText(msg.to,str(trans))
            elif "Tr-ar " in msg.text:
                nk0 = msg.text.replace("Tr-ar ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'ar')
                kr.sendText(msg.to,str(trans))
            elif "Tr-hy " in msg.text:
                nk0 = msg.text.replace("Tr-hy ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'hy')
                kr.sendText(msg.to,str(trans))
#----------------UpdateFotoProfil----------------#
            elif "Cpp" in msg.text:
                #if msg.from_ in owner:
                    path = "syn.jpg"
                    kr.sendText(msg.to,"Update PP :")
                    kr.sendImage(msg.to,path)
                    kr.updateProfilePicture(path)
#----------------------------------------
#----------------------------------------------------------------------------
            elif "Ambil @" in msg.text:
                #if msg.from_ in owner:
                    _name = msg.text.replace("Ambil @","")
                    _nametarget = _name.rstrip('  ')
                    gs = kr.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        kr.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                contact = kr.getContact(target)
                                path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                kr.sendImageWithURL(msg.to, path)
                            except:
                                pass
#-----------------------------------------------
            elif "Steal " in msg.text:
                #if msg.from_ in owner:
                    salsa = msg.text.replace("Steal ","")
                    Manis = kr.getContact(salsa)
                    Imoet = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                    try:
                        cover = kr.channel.getCover(Manis)
                    except:
                        cover = ""
                    kr.sendText(msg.to,"Gambar Foto Profilenya")
                    kr.sendImageWithURL(msg.to,Imoet)
                    if cover == "":
                        kr.sendText(msg.to,"User tidak memiliki cover atau sejenisnya")
                    else:
                        kr.sendText(msg.to,"Gambar Covernya")
                        kr.sendImageWithURL(msg.to,cover)
#--------------------------CEK SIDER------------------------------

            elif "setview" in msg.text:
                subprocess.Popen("echo '' > dataSeen/"+msg.to+".txt", shell=True, stdout=subprocess.PIPE)
                kr.sendText(msg.to, "Checkpoint checked!")
                print "@setview"

            elif "viewseen" in msg.text:
	        lurkGroup = ""
	        dataResult, timeSeen, contacts, userList, timelist, recheckData = [], [], [], [], [], []
                with open('dataSeen/'+msg.to+'.txt','r') as rr:
                    contactArr = rr.readlines()
                    for v in xrange(len(contactArr) -1,0,-1):
                        num = re.sub(r'\n', "", contactArr[v])
                        contacts.append(num)
                        pass
                    contacts = list(set(contacts))
                    for z in range(len(contacts)):
                        arg = contacts[z].split('|')
                        userList.append(arg[0])
                        timelist.append(arg[1])
                    uL = list(set(userList))
                    for ll in range(len(uL)):
                        try:
                            getIndexUser = userList.index(uL[ll])
                            timeSeen.append(time.strftime("%H:%M:%S", time.localtime(int(timelist[getIndexUser]) / 1000)))
                            recheckData.append(userList[getIndexUser])
                        except IndexError:
                            conName.append('nones')
                            pass
                    contactId = kr.getContacts(recheckData)
                    for v in range(len(recheckData)):
                        dataResult.append(contactId[v].displayName + ' ('+timeSeen[v]+')')
                        pass
                    if len(dataResult) > 0:
                        tukang = "List Viewer\n*"
                        grp = '\n* '.join(str(f) for f in dataResult)
                        total = '\n\nTotal %i viewers (%s)' % (len(dataResult), datetime.now().strftime('%H:%M:%S') )
                        kr.sendText(msg.to, "%s %s %s" % (tukang, grp, total))
                    else:
                        kr.sendText(msg.to, "Belum ada viewers")
                    print "@viewseen"
#--------------------------CEK SIDER------------------------------
            elif ("Micadd " in msg.text):
                #if msg.from_ in owner:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            mimic["target"][target] = True
                            kr.sendText(msg.to,"Target ditambahkan!")
                            break
                        except:
                            kr.sendText(msg.to,"Fail !")
                            break
                    
            elif ("Michapus " in msg.text):
                #if msg.from_ in owner:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            del mimic["target"][target]
                            kr.sendText(msg.to,"Target dihapuskan!")
                            break
                        except:
                            kr.sendText(msg.to,"Fail !")
                            break
                    
            elif msg.text in ["Miclist"]:
                #if msg.from_ in owner:
                        if mimic["target"] == {}:
                            kr.sendText(msg.to,"nothing")
                        else:
                            mc = "Target mimic user\n"
                            for mi_d in mimic["target"]:
                                mc += "?? "+kr.getContact(mi_d).displayName + "\n"
                            kr.sendText(msg.to,mc)

            elif "Mimic target " in msg.text:
                #if msg.from_ in owner:
                        if mimic["copy"] == True:
                            siapa = msg.text.replace("Mimic target ","")
                            if siapa.rstrip(' ') == "me":
                                mimic["copy2"] = "me"
                                kr.sendText(msg.to,"Mimic change to me")
                            elif siapa.rstrip(' ') == "target":
                                mimic["copy2"] = "target"
                                kr.sendText(msg.to,"Mimic change to target")
                            else:
                                kr.sendText(msg.to,"I dont know")
            
            elif "Mimic " in msg.text:
                #if msg.from_ in owner:
                    cmd = msg.text.replace("Mimic ","")
                    if cmd == "on":
                        if mimic["status"] == False:
                            mimic["status"] = True
                            kr.sendText(msg.to,"Reply Message on")
                        else:
                            kr.sendText(msg.to,"Sudah on")
                    elif cmd == "off":
                        if mimic["status"] == True:
                            mimic["status"] = False
                            kr.sendText(msg.to,"Reply Message off")
                        else:
                            kr.sendText(msg.to,"Sudah off")
#----------------------------------------------------------------
#--------------------------------
            elif msg.text in ["Gift","gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                kr.sendMessage(msg)


            elif msg.text in ["Gift1"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '696d7046-843b-4ed0-8aac-3113ed6c0733',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '6'}
                msg.text = None
                kr.sendMessage(msg)

            elif msg.text in ["Gift2"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '8fe8cdab-96f3-4f84-95f1-6d731f0e273e',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '7'}
                msg.text = None
                kr.sendMessage(msg)

            elif msg.text in ["Gift3"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'ae3d9165-fab2-4e70-859b-c14a9d4137c4',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '8'}
                msg.text = None
                kr.sendMessage(msg)

#------------------------------
#--------------------------------------
            elif msg.text in ["hmm"]:
					kr.sendText(msg.to,"Waduh kenapa gatel tenggorokan ya")
            elif msg.text in ["welcome","Kam"]:
					kr.sendText(msg.to,"Selamat datang di Group")
					kr.sendText(msg.to,"Jangan nakal ok!")
#-----------------------------------------------
#-------------- Add Friends ------------
            elif "botadd @" in msg.text:
                #if msg.from_ in owner:
                  if msg.toType == 2:
                    #if msg.from_ in owner:
                      print "[Command]Add executing"
                      _name = msg.text.replace("botadd @","")
                      _nametarget = _name.rstrip('  ')
                      gs = kr.getGroup(msg.to)
                      targets = []
                      for g in gs.members:
                        if _nametarget == g.displayName:
                          targets.append(g.mid)
                      if targets == []:
                        kr.sendText(msg.to,"Contact not found")
                      else:
                        for target in targets:
                          try:
                            kr.findAndAddContactsByMid(target)
                            kr.senText(msg.to, "Berhasil Menambah Kan Teman")
                          except:
                            kr.sendText(msg.to,"Error")
                  else:
                    kr.sendText(msg.to,"Perintah Ditolak")
                    kr.sendText(msg.to,"Perintah ini Hanya Untuk Admin")
#-----------------------------------------------
            elif msg.text in ["Respon"]:
				#if msg.from_ in owner:
					kr.sendText(msg.to,"Iya Mbebz...")
					kr.sendText(msg.to,"Kenapa..??")
					kr.sendText(msg.to,"Kangen kah...(^_^)")
            elif msg.text in ["Absen"]:
                    kr.sendText(msg.to,"👉★★★")
                    kr.sendText(msg.to,"👉★★★★")
                    kr.sendText(msg.to,"👉★★★★★")
                    kr.sendText(msg.to,"👉Semua Hadir Boss...!!!\n\n[✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰]")
#-------------------------------------------------
            elif "Ambilmid @" in msg.text:
                #if msg.from_ in owner:
                  _name = msg.text.replace("Ambilmid @","")
                  _nametarget = _name.rstrip(' ')
                  gs = kr.getGroup(msg.to)
                  for g in gs.members:
                      if _nametarget == g.displayName:
                          kr.sendText(msg.to, g.mid)
                      else:
                          pass
#--------------------------
#--------------------------
            elif "Bcgrup: " in msg.text:
                #if msg.from_ in owner:
                    bc = msg.text.replace("Bcgrup: ","")
                    gid = kr.getGroupIdsJoined()
                    for i in gid:
                        kr.sendText(i,"╠═════[BROADCAST]═════╣\n\n"+bc+"\n\nMAAF BROADCAST!!\n\n=>>line://ti/p/~krissthea\n●▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬●")
                        kr.sendText(msg.to, "Brodcastgrup sukses")
#--------------------------------------------------------
            elif msg.text in ["Sp","Speed",".sp"]:
				#if msg.from_ in owner:
					start = time.time()
					kr.sendText(msg.to, "Lagi Proses...")
					kr.sendText(msg.to, "Santai sambil ngintip janda...")
					elapsed_time = time.time() - start
					kr.sendText(msg.to, "%s/Detik" % (elapsed_time))
#------------------------------------------------------------------
            elif "Cancel" in msg.text:
				#if msg.from_ in owner:
					if msg.toType == 2:
						X = kr.getGroup(msg.to)
						if X.invitee is not None:
							gInviMids = [contact.mid for contact in X.invitee]
							kr.cancelGroupInvitation(msg.to, gInviMids)

            elif "cium " in msg.text:
                #if msg.from_ in owner:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"] [0] ["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            kr.kickoutFromGroup(msg.to,[target])
                        except:
                            kr.sendText(msg.to,"Error")


            elif "megs " in msg.text:
                #if msg.from_ in owner:
                    gName = msg.text.replace("megs ","")
                    ap = kr.getGroups([msg.to])
                    semua = [contact.mid for contact in ap[0].members]
                    nya = ap[0].members
                    for a in nya:
                        Mi_d = str(a.mid)
                        kr.createGroup(gName, semua)
                        kr.createGroup(gName, semua)
                        kr.createGroup(gName, semua)
                        kr.createGroup(gName, semua)
                        kr.createGroup(gName, semua)
                        kr.createGroup(gName, semua)
                        kr.createGroup(gName, semua)
            elif "#megs " in msg.text:
                #if msg.from_ in owner:
                    gName = msg.text.replace("#megs ","")
                    ap = kr.getGroups([msg.to])
                    semua = findAndAddContactsByMid(Mi_d)
                    nya = ap[0].members
                    for a in nya:
                        Mi_d = str(a.mid)
                        klis=[cl]
                        team=random.choice(klis)
                        kr.findAndAddContactsByMid(Mi_d)
                        kr.createGroup(gName, semua)
                        kr.createGroup(gName, semua)
                        kr.createGroup(gName, semua)
                        kr.createGroup(gName, semua)
                        kr.createGroup(gName, semua)
                        kr.createGroup(gName, semua)
                        team.findAndAddContactsByMid(Mi_d)
                        team.createGroup(gName, semua)
                        team.createGroup(gName, semua)
                        team.createGroup(gName, semua)
                        team.createGroup(gName, semua)
                        team.createGroup(gName, semua)
                        team.createGroup(gName, semua)
            elif "Recover" in msg.text:
                #if msg.from_ in owner:
                    thisgroup = kr.getGroups([msg.to])
                    Mids = [contact.mid for contact in thisgroup[0].members]
                    mi_d = Mids[:33]
                    kr.createGroup("Recover", mi_d)
                    kr.sendText(msg.to,"Success recover")
            elif "Spin" in msg.text:
                #if msg.from_ in owner:
                    thisgroup = kr.getGroups([msg.to])
                    Mids = [contact.mid for contact in thisgroup[0].members]
                    mi_d = Mids[:33]
                    kr.createGroup("Nah kan", mi_d)
                    kr.createGroup("Nah kan", mi_d)
                    kr.createGroup("Nah kan", mi_d)
                    kr.createGroup("Nah kan", mi_d)
                    kr.createGroup("Nah kan", mi_d)
                    kr.createGroup("Nah kan", mi_d)
                    kr.createGroup("Nah kan", mi_d)
                    kr.createGroup("Nah kan", mi_d)
                    kr.createGroup("Nah kan", mi_d)
                    kr.createGroup("Nah kan", mi_d)
                    kr.sendText(msg.to,"Success...!!!!")
            elif msg.text in ["Remove all chat"]:
                #if msg.from_ in owner:
                    kr.removeAllMessages(op.param2)
                    ki.removeAllMessages(op.param2)
                    kr.sendText(msg.to,"Removed all chat Finish")
            elif msg.text in ["Muach"]:
                #if msg.from_ in owner:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "ua7fb5762d5066629323d113e1266e8ca',"}
                    kr.sendMessage(msg)
            elif "Spamtag @" in msg.text:
                #if msg.from_ in owner:
                    _name = msg.text.replace("Spamtag @","")
                    _nametarget = _name.rstrip(' ')
                    gs = kr.getGroup(msg.to)
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            xname = g.displayName
                            xlen = str(len(xname)+1)
                            msg.contentType = 0
                            msg.text = "@"+xname+" "
                            msg.contentMetadata ={"MENTION":'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(g.mid)+'}]}','EMTVER':'4'}
                            kr.sendMessage(msg)
                            kr.sendMessage(msg)
                            kr.sendMessage(msg)
                            kr.sendMessage(msg)
                            kr.sendMessage(msg)
                            kr.sendMessage(msg)
                            kr.sendMessage(msg)
                            kr.sendMessage(msg)
                            kr.sendMessage(msg)
                            kr.sendMessage(msg)
                            kr.sendMessage(msg)
                            kr.sendMessage(msg)
                            kr.sendMessage(msg)
                            kr.sendMessage(msg)
                            kr.sendMessage(msg)
                            kr.sendMessage(msg)
                            kr.sendMessage(msg)
                            kr.sendMessage(msg)
                            kr.sendMessage(msg)
                            kr.sendMessage(msg)
                        else:
                            pass

#==============================================
            elif "Spamkontak @" in msg.text:
                #if msg.from_ in owner:
                    _name = msg.text.replace("Spamkontak @","")
                    _nametarget = _name.rstrip(' ')
                    gs = kr.getGroup(msg.to)
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            kr.sendText(msg.to, "║╠❂➣ Spam sedang di Proses...!!!")
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(msg.to, "║╠❂➣ Done.. Selesai di Spam...!!!")
                            print " Spammed !"
#-----------------------------------------------
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:

                if wait["contact"] == True:
                    msg.contentType = 0
                    kr.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = kr.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = kr.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        kr.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = kr.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = kr.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        kr.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URL�0�10��9�0�16�0�69�0�3�0�4\n" + msg.contentMetadata["postEndUrl"]
                    kr.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif "Ownadd @" in msg.text:
                if msg.from_ in owner:
                    print "[Command]Staff add executing"
                    _name = msg.text.replace("Ownadd @","")
                    _nametarget = _name.rstrip('  ')
                    gs = kr.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        kr.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                owner.append(target)
                                kr.sendText(msg.to,"Owner Telah Ditambahkan")
                            except:
                                pass
                    print "[Command]owner add executed"

            elif "Ownhapus @" in msg.text:
                if msg.from_ in owner:
                    print "[Command]Staff remove executing"
                    _name = msg.text.replace("Ownhapus @","")
                    _nametarget = _name.rstrip('  ')
                    gs = kr.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        kr.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                owner.remove(target)
                                kr.sendText(msg.to,"Owner Telah Dihapus")
                            except:
                                pass
                    print "[Command]owner remove executed"

            elif msg.text in ["Ownlist","ownlist"]:
              if msg.from_ in owner:
                if owner == []:
                    kr.sendText(msg.to,"The owner list is empty")
                else:
                    kr.sendText(msg.to,"Sabar Dikit Boss.....")
                    mc = ""
                    for mi_d in owner:
                        mc += "☄" +kr.getContact(mi_d).displayName + "\n"
                    kr.sendText(msg.to,mc)
                    print "[Command]owner list executed"
                    
            elif "Tes tambah admin @" in msg.text:
                if msg.from_ in owner:
                    print "[Command]Staff add executing"
                    _name = msg.text.replace("Tes tambah admin @","")
                    _nametarget = _name.rstrip('  ')
                    gs = kr.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        kr.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                admin.append(target)
                                kr.sendText(msg.to,"Admin Telah Ditambahkan")
                            except:
                                pass
                    print "[Command]Staff add executed"
                else:
                    kr.sendText(msg.to,"Command Di Tolak Jangan Sedih")
                    kr.sendText(msg.to,"Sudah Menjadi Admin Maka Tidak Bisa Menjadi Admin Lagi")

            elif "Tes hapus admin @" in msg.text:
                if msg.from_ in owner:
                    print "[Command]Staff remove executing"
                    _name = msg.text.replace("Tes hapus admin @","")
                    _nametarget = _name.rstrip('  ')
                    gs = kr.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        kr.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                admin.remove(target)
                                kr.sendText(msg.to,"Admin Telah Dihapus")
                            except:
                                pass
                    print "[Command]Staff remove executed"
                else:
                    kr.sendText(msg.to,"Command DiTolak")
                    kr.sendText(msg.to,"Admin Tidak Bisa Menggunakan")
                    
            elif msg.text in ["Tes adminlist","tes adminlist"]:
                if msg.from_ in owner:
                    if admin == []:
                        kr.sendText(msg.to,"The adminlist is empty")
                    else:
                        kr.sendText(msg.to,"Sabar Dikit Boss Kris.....")
                        mc = ""
                        for mi_d in admin:
                            mc += "║╠❂➣" +kr.getContact(mi_d).displayName + "\n"
                        kr.sendText(msg.to,mc)
                        print "[Command]Stafflist executed"
                    
            elif msg.text in ["Tes muach"]:
                if msg.from_ in owner:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "ua7fb5762d5066629323d113e1266e8ca',"}
                    kr.sendMessage(msg)
                    
            elif "Restart" in msg.text:
                if msg.from_ in owner:
                    print "[Command]Restart"
                    try:
                        kr.sendText(msg.to,"Restarting...")
                        kr.sendText(msg.to,"Restart Success")
                        restart_program()
                    except:
                        kr.sendText(msg.to,"Please wait")
                        restart_program()
                        pass
                              
            elif "Tes tag @" in msg.text:
                if msg.from_ in owner:
                    _name = msg.text.replace("Tes tag @","")
                    _nametarget = _name.rstrip(' ')
                    gs = kr.getGroup(msg.to)
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            xname = g.displayName
                            xlen = str(len(xname)+1)
                            msg.contentType = 0
                            msg.text = "@"+xname+" "
                            msg.contentMetadata ={"MENTION":'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(g.mid)+'}]}','EMTVER':'4'}
                            kr.sendMessage(msg)
                            kr.sendMessage(msg)
                            kr.sendMessage(msg)
                            kr.sendMessage(msg)
                            kr.sendMessage(msg)
                            kr.sendMessage(msg)
                            kr.sendMessage(msg)
                            kr.sendMessage(msg)
                            kr.sendMessage(msg)
                            kr.sendMessage(msg)
                            kr.sendMessage(msg)
                            kr.sendMessage(msg)
                            kr.sendMessage(msg)
                            kr.sendMessage(msg)
                            kr.sendMessage(msg)
                            kr.sendMessage(msg)
                            kr.sendMessage(msg)
                            kr.sendMessage(msg)
                            kr.sendMessage(msg)
                            kr.sendMessage(msg)
                        else:
                            pass
                              
            elif "Tes spm @" in msg.text:
                if msg.from_ in owner:
                    _name = msg.text.replace("Tes spm @","")
                    _nametarget = _name.rstrip(' ')
                    gs = kr.getGroup(msg.to)
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            kr.sendText(msg.to, "║╠❂➣ Spam sedang di Proses...!!!")
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(g.mid,'spam')
                            kr.sendText(msg.to, "║╠❂➣ Done.. Selesai di Spam...!!!")
                            print " Spammed !"
                              
                                
        if op.type == 55:
            #print "[NOTIFIED_READ_MESSAGE]"
            try:
                if op.param1 in wait2['readPoint']:
                    Nama = kr.getContact(op.param2).displayName
                    if Nama in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n-> " + Nama
                        wait2['ROM'][op.param1][op.param2] = "-> " + Nama
                        wait2['setTime'][msg.to] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                else:
                    kr.sendText
            except:
                pass


        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True


def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = kr.getProfile()
                profile.displayName = wait["cName"] + nowT
                kr.updateProfile(profile)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

while True:
    try:
        Ops = kr.fetchOps(kr.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(kr.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            kr.Poll.rev = max(kr.Poll.rev, Op.revision)
            bot(Op)
