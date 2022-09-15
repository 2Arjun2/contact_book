import sys

def save():
	rows, columns = int(input("\nEnter how many contacts you want to save first: ")), 2
	contacts = []
	print(contacts)
	for i in range(rows):
		print("\nEnter %d contact details : " % (i+1))
		var1 = []
		for j in range(columns):
			if j == 0:
				var1.append(str(input("\n\nEnter name: ")))					
			if j == 1:
				var1.append(int(input("\n\nEnter number: ")))			
		contacts.append(var1)	
	print(contacts)
	x="".join(str(e) for e in contacts)
	f=open("project.txt","w")
	f.write(x)
	f.close()
	return contacts
	

def add(s):
	var2 = []
	for i in range(len(s[0])):
		if i == 0:
			var2.append(str(input("\nEnter name: ")))
		if i == 1:
			var2.append(int(input("\nEnter number: ")))
	s.append(var2)
	x=" ".join(str(e) for e in var2)
	f=open("project.txt","a")
	f.write(x)
	f.close()
	return s

def remove(s):
	var = str(input("\nEnter the name: "))
	var4 = 0	
	for i in range(len(s)):
		if var == s[i][0]:
			var4 += 1
			print(s.pop(i))
			print("\nContact has now been removed")
			return s
	if var4 == 0:
		print("\nThere's no contact saved by this name")
		return s

def delete(pb):
	return pb.clear()

def find(s):
	var5 = []
	check = -1
	var = str(input("\nEnter the name: "))
	for i in range(len(s)):
		if var == s[i][0]:
			check = i
			var5.append(s[i])			
	if check == -1:
		return -1
	else:
		show(var5)
		return check

def show(s):
	if not s:
		print("\nList is empty: []")
	else:
		for i in range(len(s)):
			print(s[i])

print("\nThis is Contact book")
ch = 1
s= save()
while ch in (1, 2, 3, 4, 5):
	print("\nChoose any option from below:\n")
	print("1. Add a new contact")
	print("2. Remove any contact")
	print("3. Delete all ")
	print("4. Search ")
	print("5. Display all contacts")
	print("6. Exit ")

	ch = int(input("\nPlease enter your choice: "))
	if ch == 1:
		s = add(s)
	elif ch == 2:
		s = remove(s)
	elif ch == 3:
		s = delete(s)
	elif ch == 4:
		d = find(s)
		if d == -1:
			print("\nThe contact does not exist.")
	elif ch == 5:
		show(s)
	else:
		sys.exit()
