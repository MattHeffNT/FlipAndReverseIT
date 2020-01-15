import webbrowser
#  _   _       __  __ 
# | | | | ___ / _|/ _|
# | |_| |/ _ \ |_| |_
# |  _  |  __/  _|  _|
# |_| |_|\___|_| |_|

# A quick little string reverser to save me time when there are no endnote citations availble and the only
# author information is in "first name, last name" format. This is just a quick thingy to then be able to paste straight
# into endnote. Probably not very useful to most people at all....but you know....coding is life. 

## function to store names into a text file (same one this python file is in)
def store_name(author):
    """ Store name in a file """
    with open("ref.txt","a") as fp:
        fp.write(str(reference)+""+'\n')
 
names = (['Meaghan Altman','joshua vanArsdall', 'Brett Beston', 'Kwame Brown','Angela Lukowski',
'Emily Slonecker','John Hummel','Hillary Wehe','John Vervaeke','Melissa Swisher','Bernardo Carducci',
'Thomaseo Burton','Stephanie Poplock'])

#can also have as dynamic input from user but was just using, just uncomment code snippet below

# def dynamic_Names():
#     Fnames = input("Fname? ")
#     Lnames = input("Lname? ")
#     input ("Add more Y/N ? "):
#         if input == "Y"
#     names = [Fnames+" "+Lnames]
#################################################################################################

for i in names:
    bro=i.split()
    bro.reverse()
    reference = (', '.join(bro))

    store_name(reference)

# just a quick console prompt to check whether you want to open the txt file where the names are stored
open_file = input ("Do you wanna to open the file now? Y/N ")

if open_file == 'yes'or'y'or'Y'or'Yes':
    webbrowser.open('ref.txt')
else:

    exit()
        