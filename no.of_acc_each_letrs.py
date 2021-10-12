#no.of accorence in each letters
name="shivashankar"
d={}
for letter in name:
	d[letter]=d.get(letter,0)+1
else:
	print(d)
#second aproach
for letter in name:
	if letter in d:
		d[letter]=d[letter]+1
	else:
		d[letter]=1
else:
	print(d)
