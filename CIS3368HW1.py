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

conn = create_con('yourConnectionString', 'yourUsername', 'yourPassword', 'yourDBname')
cursor = conn.cursor(dictionary = True)
sql = "Select * from users"
cursor.execute(sql)
rows = cursor.fetchall()
for user in rows:
    print(user)
    print("the user's first name is : " + user["firstname"])


fish_details = []

def add_fish():
    superclass = input("Enter the superclass of the fish: ")
    species = input("Enter the species of the fish: ")
    color = input("Enter the color of the fish: ")
    acquired = input("Enter the acquired of the fish: ")
    alive = input("Enter the alive of the fish: ")



    fish_details.append({ "species": species, "color": color, acquired:"acquired", alive:"alive"})

def output_fish():
    for fish in fish_details:
        print(f"Species: {fish['species']}, Color: {fish['color']}, Acquired: {fish['acquired']}, Alive: {fish['alive']}")

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
