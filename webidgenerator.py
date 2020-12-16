# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exist
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)

name = input("Votre nom : ")
enterprise = input("Le nom de votre entreprise : ")

f = open("myId.txt", "w")
f.write(f"""name :  {name}
enterprise : {enterprise}
email : {name}@{enterprise}.com
website : {enterprise}.com
instagram : @{enterprise}
""")
f.close()

f = open("myId.txt", "r")
print(f.read())
stop = input("\nAppuyez sur n'importe quel touche pour fermer le programme...")