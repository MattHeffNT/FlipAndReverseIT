import webbrowser
#  _   _       __  __ 
# | | | | ___ / _|/ _|
# | |_| |/ _ \ |_| |_
# |  _  |  __/  _|  _|
# |_| |_|\___|_| |_|

# A quick little string reverser to save me time when there are no endnote citations availble and the only
# author information is in "first name, last name" format. This is just a quick thingy to then be able to paste straight
# into endnote. Probably not very useful to most people at all....but you know....coding is life. 

# Function to store names into a text file (same one this python file is in)
def store_name(author):
    """ Store name in a file """
    with open("ref.txt","a") as fp:
        fp.write(str(reference)+""+'\n')

# Loop that provides console prompts to the user so that they can enter the names themselves
x = 0 
names = []
while x == 0:

    Fnames = input("First name? ")
    Lnames = input("Last name? ")
    names.append(Fnames+" "+Lnames)    
    add_name = input ("Do you want to add more Y/N ? ")

    if add_name  == "Y"or add_name == "y":
      
        print (names)

    elif add_name  == "N" or add_name == "n":
        
        print (names)
        x = 1
        
#################################################################################################

for i in names:
    name=i.split()
    name.reverse()
    reference = (', '.join(name))
    store_name(reference)

# just a quick console prompt to check whether you want to open the txt file where the names are stored
open_file = input ("Do you wanna to open the file now? Y/N ")
if open_file == "y" or open_file == "Y" or open_file == "yes" or open_file == "Yes": 
    print (open_file)
    webbrowser.open('ref.txt')
else:
    exit()