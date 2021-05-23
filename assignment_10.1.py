'''
Your program this week will use the OS library in order to validate that a 
directory exists before creating a file in that directory.  Your program will 
prompt the user for the directory they would like to save the file in as well as 
the name of the file.  The program should then prompt the user for their name, address, 
and phone number. Your program will write this data to a comma separated line in a file 
and store the file in the directory specified by the user. 

Once the data has been written your program should read the file you just wrote 
to the file system and display the file contents to the user for validation purposes. 
'''
import os

# get current working directory
print(os.getcwd())

# make a folder[s] inside the current working directory 
# os.mkdirs('test_folder')


print(f'You are currently in this directory: {os.getcwd()}')
user_dir = input('Please enter the relative path where you want to save your file:\n')

if not os.path.isdir(user_dir): os.makedirs(user_dir)

user_file = input('Insert the name for your file:\n')
user_file += '.txt'

name = input('Please enter your name: ')
address = input('Please enter your address: ')
phone = input('Please enter your phone number: ')

# change directory to where the user wants to save the file so I can just input user_file into open()
os.chdir(os.getcwd() + '/' + user_dir)

# I am not really sure what the assignment meant by "comma separated line"
# So I just separated new lines with a comma
with open(user_file, 'w') as fh:
    fh.write(name + ',\n')
    fh.write(address + ',\n')
    fh.write(phone)

with open(user_file) as fh:
    data = fh.read().replace('\n', '')
    info = data.split(',')
    print('These are the data in your file:')
    for line in info:
        print(line, end = " ")

