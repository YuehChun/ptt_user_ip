 #!/usr/bin/python
 # -*- coding: utf-8 -*-
import sys
import telnetlib
import time
import re

tn = telnetlib.Telnet('ptt.cc')
time.sleep(1)
content = tn.read_very_eager().decode('big5','ignore')
print("首頁顯示...")

if u"請輸入代號" in content:
    print("輸入帳號...")
    tn.write(("__ACCOUNT__\r\n").encode('big5') )
    time.sleep(1)
    content = tn.read_very_eager().decode('big5','ignore')

    print("輸入密碼...")
    tn.write(("__PASSWORD__\r\n").encode('big5'))
    time.sleep(2)
    content = tn.read_very_eager().decode('big5','ignore')

    if u"密碼不對" in content:
        print("密碼不對或無此帳號。程式結束")
        sys.exit()
    if u"您想刪除其他重複登入的連線嗎" in content:
        print("發現重複連線,先不刪除他...")
        tn.write("n\r\n".encode('big5') )
        time.sleep(7)
        content = tn.read_very_eager().decode('big5','ignore')
    #print(content)
    while u"任意鍵" in content:
        print("資訊頁面，按任意鍵繼續...")
        tn.write("\r\n".encode('big5'))
        time.sleep(2)
        content = tn.read_very_eager().decode('big5','ignore')

    if u"要刪除以上錯誤嘗試" in content:
        print("發現嘗試登入卻失敗資訊，是否刪除?(Y/N)：")
        anser = input("Y")
        tn.write((anser+"\r\n").encode('big5') )
        time.sleep(1)
        content = tn.read_very_eager().decode('big5','ignore')
    print("----------------------------------------------")
    print("----------- 登入完成，顯示操作介面 --------------")
    print("----------------------------------------------")
    # print(content)
    tn.write("T\r\nU\r\n")
    for i in range(10000, 0, -1):
	    tn.write("jq")
	    time.sleep(1)
	    content = tn.read_very_eager().decode('big5','ignore')
	    ipArr = re.findall( r'[0-9]+(?:\.[0-9]+){3}',content)
	    name = re.findall( u'《ＩＤ暱稱》(.+?) \(',content,re.UNICODE)
	    _ip = ipArr[-1].encode("utf8")
	    _name = name[0].encode("utf8")
	    print _name + " 的IP : " + _ip
	    tn.write("e")
	    time.sleep(1)

else:
    print("沒有可輸入帳號的欄位，網站可能掛了")