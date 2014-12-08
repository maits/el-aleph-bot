import re, nltk.data, string
sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')

filename = open('file.txt', 'r')
f = filename.read()
filename.close()

w = open('lines.txt', 'w')

fsent = sent_detector.tokenize(f.strip())

for sent in fsent:
	if len(sent) <= 140:
		w.write(sent)
		w.write("\n")
	elif len(sent) > 141:
		w.write("SPLIT")
		w.write(sent)
		w.write("\n")
	else:
		pass

print "DONE!"

w.close()
