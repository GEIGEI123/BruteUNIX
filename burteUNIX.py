import crypt
import optparse

Red0cms

def main():
	parser = optparse.OptionParser('usage%prog: ' + ' -d <dictionaryfile>')
	parser.add_option('-d', dest='dname', type='string', help='specify dictionary file')
	(options, args) = parser.parse_args()
	if (options.dname == None):
		print parser.usage
		exit(0)
	else:
		dname = options.dname
	passFile = open('/etc/shadow', 'r')
	for line in passFile.readlines():
		if ":" in line:
			user = line.split(':')[0]
			cryptPass = line.split(':')[1]
			print "[*] Cracking Password For: " + user
			testPass(cryptPass, dname)


def testPass(cryptPass, dname):
	salt = cryptPass[0:19]
	dictFile = open(dname, 'r')
	for word in dictFile.readlines():
		word = word.strip('\n').strip()
		cryptWord = crypt.crypt(word, salt)
		if cryptWord == cryptPass:
			print "[+] Found Password: " + word + "\n"
			return
	print "[-] Password Not Found.\n"
	return


if __name__ == "__main__":
	main()
