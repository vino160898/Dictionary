#Adding values mark
marks={'first':45,'second':67,'third':78}
for paper,mark in marks.items():
	marks[paper]=mark+2
else:
	print(marks)  #-->{'first': 47, 'second': 69, 'third': 80}
#Total salary
employees={'ab':12000,'bc':10000,'cd':15000,'ef':10000}
total=0
for k, v in employees.items():
	total=total+v
else:
	print(total)  #-->47000
#greater then 12000 salary getting employees names
for k,v in employees.items():
	if 12000>=v:
		print(k)  #-->ab,cd
#getting total of marks in dictionary list
students={'raja':[56,67,78],'dinesh':[78,89,90]}
for k,v in students.items():
	total=0
	for value in v:
		total=total+value
	else:
		print(k,"-->",total)  #-->raja-->201,dinesh-->257
#swaping in keys to value and value to key
student={'raja':123,'dinesh':456}
d={}
for k,v in student.items():
	d[v]=k
else:
	print(d)  #-->{123: 'raja', 456: 'dinesh'}
#membership operator
print(123 in students.values())   #-->False
print('dinesh' in students.keys())  #-->True
