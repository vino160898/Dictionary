marks={}
choice=' '
while choice != 'ok':
	subname=input("Enter Subject name : ")
	mark=int(input("Enter mark : "))
	marks[subname]=mark
	choice=input('Shall I stop getting marks [type:ok] : ')
else:
	print (marks)
	for sub in marks:
		print(sub, "\t" ,marks[sub])
