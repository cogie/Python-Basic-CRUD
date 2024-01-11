# main function for CRUD

print("----------------------------------------")
print("Python CRUD w/ json as DB")
print("----------------------------------------")

import json

#Create data and add to json file
def create_func():
	user_id = int(input("Enter ID: "))
	name = input("Enter Name: ")
	age = int(input("Enter age: "))

	dic = {
		"ID ": user_id,
		"Name ": name,
		"Age ": age,
	}

	#load the json file
	with open("data2.json","r") as getdata:
		data = json.load(getdata) #convert json to python

		data[user_id] = dic

	#save the data to json from python
	with open("data2.json","w") as save:
		json.dump(data,save) # python to json
		print("Succesfuly Created!!\n")




#function to view content of json file
def read_func():
	with open("data2.json", "r") as view:
		data = json.load(view)

	for i, m in data.items():
		for x, n in m.items():
			print(x, n)
		print("\n")

	#what if specific user_id to view?


#update or edit an existing data from json
def update_func():
	user_id = input("Enter ID you want to Edit: ")

	with open("data2.json","r") as view:
		data = json.load(view)


	if user_id in data:
		name = input("Enter new name: ")
		age = input("Enter new age: ")

		dic = {
			"ID ": user_id,
			"Name ": name,
			"Age ": age,
		}

		data[user_id] = dic

		with open("data2.json","w") as update:
			json.dump(data,update)
			print("Update Success!!\n")

	else:
		print("ID does not exist!!")



#delete data in json file
def delete_func():
	user_id = input("Enter ID you want to delete: ")

	with open("data2.json","r") as getdata:
		data = json.load(getdata)

		if user_id in data:
			data.pop(user_id)

			with open("data2.json","w") as delete:
				json.dump(data, delete)
				print("Deleted!!\n")
		else:
			print("User Does not Exist!!\n")

 
#Drivers code
def main():
	while True:
		print("1. Create")
		print("2. Read")
		print("3. Update")
		print("4. Delete")
		print("5. Exit \n")

		no = int(input("Enter choice: "))

		#condition to which function will be called
		if no == 1:
			create_func()
		elif no == 2:
			read_func()
		elif no == 3:
			update_func()
		elif no == 4:
			delete_func()
		elif no == 5:
			print("Thank you!!")
			break 
		else:
			print("Not in the Choices!")
	
if __name__ =="__main__":
	main()