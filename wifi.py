#coding:utf-8
import sys,os,re
def dump_wifi():
	wifilist = os.popen('netsh wlan show profiles').read()

	pattern = re.compile('\s?\:\s?(.+?)\n')

	resoult = pattern.findall(wifilist)
	print "\n------------------------WIFI Password Found!------------------------\n"
	for wifiname in resoult:
		wifiname = wifiname.strip()
		if wifiname:
			wificmd = "netsh wlan show profiles name = \"%s\" key = clear "%(wifiname)
			print os.popen(wificmd).read()
	print '-----------------------------------END-------------------------------------'

if __name__ == '__main__':
	dump_wifi()