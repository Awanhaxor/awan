#This Code is Written by Sachin Shrivastv

#coding = utf-8

import os, time, sys

os.system('clear')

def printing(z):

	for e in z + '\n':		sys.stdout.write(e)

		sys.stdout.flush()

		time.sleep(0.001)

logo=''' .----------------. .----------------. .----------------. 

| .--------------. | .--------------. | .--------------. |

| |    ______    | | |     ____     | | |     __       | |

| |   / ____ `.  | | |   .'    '.   | | |    /  |      | |

| |   `'  __) |  | | |  |  .--.  |  | | |    `| |      | |

| |   _  |__ '.  | | |  | |    | |  | | |     | |      | |

| |  | \____) |  | | |  |  `--'  |  | | |    _| |_     | |

| |   \______.'  | | |   '.____.'   | | |   |_____|    | |

| |              | | |              | | |              | |

| '--------------' | '--------------' | '--------------' |

 '----------------' '----------------' '----------------' '''

 

logo2='''  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

 

def login():

	print(logo)

	print(logo2)

	print('                     Owner:-    Haxor')

	print('                     Author:-   Awan Haxor')

	print('                     Youtube:-  Hackers World')

	print('                     Whatsapp:- +923845844301')

	print(logo2)

	username = raw_input('  Username:- ')

	if username =='':

		print(' [!] Invalid Username')

		time.sleep(1)

		os.system('clear')

		login()

	elif username =='Awan':

		password = raw_input('  Password:- ')

		if password =='':

			print(' [!] Invalid Password')

			time.sleep(1)

			os.system('clear')

			login()

		elif password =='Haxor':

			printing('  Logged Successful ')

			os.system('python2 base.py')

		else:

			print(' [!] Invalid Password')

			time.sleep(1)

			os.system('clear')

			login()

	else:

		print(' [!] Invalid Username')

		time.sleep(1)

		os.system('clear')

		login()

		

login()
