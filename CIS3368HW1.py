import mysql.connector
from mysql.connector import Error

def create_con(hostname, username, userpw, dbname):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=hostname,
            user=username,
            password=userpw,
            database=dbname
        )
        print("connection successful")
    except Error as e:
        print(f'the error {e} occured')
    return connection

conn = create_con('hw1cis3368.c8aubdep9gnu.us-east-2.rds.amazonaws.com', 'admin', 'Passward1!', 'hw1cis3368')
cursor = conn.cursor(dictionary = True)
sql = "Select * from users"
cursor.execute(sql)
rows = cursor.fetchall()
for user in rows:
    print(user)
    print("the user's first name is : " + user["firstname"])

fish_details = []

def add_fish():
    Superclass = input("Enter the superclass of the fish: ")
    Species = input("Enter the species of the fish: ")
    Color = input("Enter the color of the fish: ")
    Acquired = input("Enter the acquired of the fish: ")
    Alive = input("Enter the alive of the fish: ")
    sql = "INSERT INTO Fish (Superclass, Species, Color, Acquired, Alive) VALUES (%s, %s, %s, %s, %s)"
    val = (Superclass, Species, Color, Acquired, Alive)
    cursor.execute(sql, val)
    conn.commit()
    fish_details.append({"Superclass": Superclass, "Species": Species, "Color": Color, Acquired:"Acquired", Alive:"Alive"})

def output_fish():
    for Fish in fish_details:
        print(f"Species: {Fish['superclass']}, {Fish['species']}, Color: {Fish['color']}, Acquired: {Fish['acquired']}, Alive: {Fish['alive']}")

def show_menu():
    print("\nMENU")
    print("a - Add fish")
    print("o - Output all fish in console")
    print("q - Quit")
    choice = input("Enter your choice: ").lower()
    if choice == 'a':
        add_fish()
    elif choice == 'o':
        output_fish()
    elif choice == 'q':
        return
    else:
        print("Invalid choice, please try again.")

while True:
    show_menu()
    if len(fish_details) == 0:
        continue
    break
conn.close()
