import time, os


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