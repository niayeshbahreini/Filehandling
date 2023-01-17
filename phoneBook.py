import os

#File DB Path
path = '/Users/niayeshbahreini/Documents/FileProjects/db.txt'
#validation
def validation():
    if not os.path.exists(path):
        f=open(path,'w+')
        f.write('')


#Functions of menu
def adduser(name,number):
    validation()
    with open(path, 'a+') as f:
        f.write(name + ':' +number +'\n')

def searchUser(name):
    validation()
    with open(path, 'r') as f:
        for line in f.readlines():
            line = line.strip() #for delet extra lines (empty lines)
            if name == line.split(':')[0]:
                print(name + ':' + line.split(':')[1])

        print('No result for ' + name)


def deletUser(name):
    validation()
    with open(path, 'r') as f:
        newDB=''
        for line in f.readlines():
            if not name == line.split(':')[0]:
                newDB += line
    with open(path,'w') as f :
        f.write(newDB)
def showAll():
    validation()
    with open(path,'r') as f :
        print(f.read())



#creat  Menu with multiple choice
choice = 1
while choice != 0 :
    print("1-Add User\n2-Search Phone\n3-Delete Phone\n4-Show All Number\n5-EXIT")
    choice = int(input("Enter Your Choice: "))
    os.system('clear') #clear screen

    if choice ==1:
        name=input('Enter Name: ')
        number=input('Enter Number: ')
        adduser(name,number)

    elif choice ==2:
        name = input('Enter Name: ')
        searchUser(name)

    elif choice ==3:
        name = input('Enter Name: ')
        deletUser(name)

    elif choice ==4:
        showAll()
    #elif choice ==5:
        #break

