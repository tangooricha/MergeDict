import sys
import string

def dictAppend(data1, data2):
	return data1 + data2

if __name__ == '__main__':
	t1 = ""
	t2 = ""
	t3 = ""

	try:
		print "Dict 1 is " + sys.argv[1]
	except:
		print "Need 3 args(0 given)!"
		print "Usage: ", sys.argv[0], " <input dict1> <input dict2> <output dict3>"
		print "Exit!"
		exit(-1)
	else:
		t1 = sys.argv[1]

	try:
		print "Dict 2 is " + sys.argv[2]
	except:
		print "Need 3 args(1 given)!\nExit!"
		exit(-1)
	else:
		t2 = sys.argv[2]

	try:
		print "Output dict is " + sys.argv[3]
	except:
		print "Need 3 args(2 given)!\nExit!"
		exit(-1)
	else:
		t3 = sys.argv[3]

	with open(t1, 'r') as f1, open(t2, 'r') as f2, open(t3, 'w+') as f3:
		f1len = len(f1.read())
		f2len = len(f2.read())
		f1.seek(0)
		f2.seek(0)
		if f1len == 0 and f2len == 0:
			print "Dict1 and Dict2 are both empty!"
			exit(0)
		else:
			f1data = []
			f2data = []
			f3data = []
			fdataline = ""
			if f1len == 0 and f2len != 0:
				while(True):
					fdataline = f2.readline()
					if not fdataline:
						break
					fdataline = fdataline.strip()
					f2data.append(fdataline)
					fdataline = ""
				print "Dict1 is empty!"
				print "Dict2 is ", f2data
				f3data = sorted(list(set(f2data)))
				print "Output dict is ", f3data
				f3.write(string.join(f3data, "\n"))

			elif f1len != 0 and f2len == 0:
				while(True):
					fdataline = f1.readline()
					fdataline = fdataline.strip()
					if not fdataline:
						break
					f1data.append(fdataline)
					fdataline = ""
				print "Dict1 is ", f1data
				print "Dict2 is empty!"
				f3data = sorted(list(set(f1data)))
				print "Output dict is ", f3data
				f3.write(string.join(f3data, "\n"))

			else:
				while(True):
					fdataline = f1.readline()
					fdataline = fdataline.strip()
					if not fdataline:
						break
					f1data.append(fdataline)
					fdataline = ""
				while(True):
					fdataline = f2.readline()
					fdataline = fdataline.strip()
					if not fdataline:
						break
					f2data.append(fdataline)
					fdataline = ""
				print "Dict1 is ", f1data
				print "Dict2 is ", f2data
				f3data = sorted(list(set(f1data + f2data)))
				print "Output dict is ", f3data
				f3.write(string.join(f3data, "\n"))
