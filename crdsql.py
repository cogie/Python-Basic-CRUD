import mysql.connector
from mysql.connector import Error

#function to create a user
def create():
    name = input("Enter your name: ")
    age = int(input("Enter Age: "))
    email = input("Enter your email: ")


    #insert data to mysql
    try:
        con = mysql.connector.connect(host = 'localhost',database = 'db_sample',user= 'root',password = '') #note change the db specification
        query = "INSERT INTO tbl_sample (Name, Age, Email) VALUE (%s,%s,%s)" 
        data = (name,age,email)
        cur = con.cursor()
        cur.execute(query,data)
        con.commit()
        cur.close()
        print("Record Succesfully!!")
    except Error as error:
        print("Error: {}".format(error))
    finally:
        if 'con' in locals() and con.is_connected():
            con.close()

#function to show users
def read():
    try:
        con = mysql.connector.connect(host = 'localhost', database = 'db_sample', user = 'root', password = '')

        query = "SELECT * FROM tbl_sample"
        cur = con.cursor()
        cur.execute(query)
        records = cur.fetchall()
        con.commit()

        if records:
            for record in records:
                print("ID: ",record[0])
                print("Name: ",record[1])
                print("Age: ", record[2])
                print("Email: ",record[3])
        else:
            print("No records!!")
    except Error as error:
        print("Error: {}".format(error))
    finally:
        if con.is_connected():
            con.close()


#function to edit an existing user info
def update():
    try:
        con = mysql.connector.connect(host = 'localhost', database = 'db_sample', user = 'root', password = '')
        user_id = int(input("Enter ID you want to update: "))
        name = input("New name: ")
        age = input("New Age: ")
        email = input("New email: ")

        query = "UPDATE tbl_sample SET Name = %s, Age = %s, Email = %s WHERE ID = %s"
        data = (name, age,email,user_id)

        cur = con.cursor()
        cur.execute(query,data)
        con.commit()
        cur.close()
        print("Updated!")

    except Error as error:
        print("Error: {}".format(error))
    finally:
        if con.is_connected():
            con.close()


#destroy the data of the user
def delete():
    try:
        con = mysql.connector.connect(host='localhost', database='db_sample', user='root', password='')
        record_id = int(input("Enter the ID of the record you want to delete: "))

        query = "DELETE FROM tbl_sample WHERE ID = %s"
        data = (record_id,)

        cur = con.cursor()
        cur.execute(query, data)
        con.commit()
        cur.close()
        print("Record deleted successfully.")

    except Error as error:
        print("Error: {}".format(error))
    finally:
        if 'con' in locals() and con.is_connected():
            con.close()




#main driver
def main():
    while True:
        print("CRUD Operations on MySQL Database")
        print("1. Create Record")
        print("2. Read Records")
        print("3. Update Record")
        print("4. Delete Record")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            create()
        elif choice == '2':
            read()
        elif choice == '3':
            update()
        elif choice == '4':
            delete()
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option (1/2/3/4/5).")

if __name__ == "__main__":
    main()