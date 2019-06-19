"""
Team name: Black Death
Author: Manav Mishra, Jai Kumar, Chakradhar R
"""

#Third party library functions

from collections import Counter
import numpy as np
import operator

#File handling in order to convert the txt data into arrays
file = open('codeplay_code.txt','r')

line = str()
for i in file:
	line += i[:-1]
print len(line)

file.close()

#This part gives us the letter frequency of the entire text
per = []
f = open('codeplay_text.txt','r')

for i in f:
	per.append(i.split()[1])

f.close()

#A function to convert letters to its corresponding numbers - A -> 0, B -> 1, and so on.
def numero(z):
	return ord(z) - 97

#List of alphabtets
alphabet = [i for i in range(26)]

#List of characters in the enitre text (no numbers)
numer=[]
for i in line:
	if (ord(i)-96)>0:
		numer.append(numero(i))

split = [line[i:i+5] for i in range(0,len(line)-5,5)]
#print split

#A loop to figure out the key in the text. We do this by subtracting the maximum frequency element with e (4), since e is the most frequent letter.
key = []
for i in range(5):
	n = []
	for s in split:
		n.append(s[i])
	freq = {x:(1.0 * n.count(x)/len(n)) for x in n}
	#print freq
	m = max(freq.iteritems(), key=operator.itemgetter(1))[0]
	key.append(chr(ord(m)-(4)))
print "key=",key

#This part Decrypts the file and writes the output into another txt file
f=open('decode.txt','w')
k=0
for i in range(0,len(numer),5):
	for j in range(5):
		a=numer[i+j]-(ord(key[j])-97)	
		if a<0:
			a=a+26
		k+=1
		if k<100:
			f.write(chr(a+97))
		else:
			k=0
			f.write("%s\n"%(chr(a+97)))

"""for i in range(26):
	a = [j-i for j in n]
	new_a = [a[k]+26 if a[k]<0 else a[k] for k in range(len(a))]
	frequency = {x:(1.0 * new_a.count(x)/len(new_a)) for x in n}
	print frequency, "\n"
"""





