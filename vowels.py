#getting vowels 
name="vinothkumar"
d={}
vowels={'a','e','i','o','u'}
for letter in name:
	if letter in vowels:
		d[letter]=d.get(letter,0)+1
else:
	print(d)
#sorting this vowels
name='vinothkumar mukesh gowtham'
d={}
vowels={'a','e','i','o','u'}
for letterin name:
	if letter in vowels:
		d[letter]=d.get(letter,0)+1
else:
	for k,v in sorted(d.items()):
		print(k,"-->",v)
