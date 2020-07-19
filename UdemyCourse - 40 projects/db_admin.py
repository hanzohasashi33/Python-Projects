print("Welcome to the db admin\n")

uname = input("Enter your username : ")
passw = input("Enter your password : ")


admins = {
    'test1' : 'test1',
    'prasanna' : 'admin',
    'hanzo' : 'hasashi', 
    'admin00' : 'admin1234',
}

if uname.lower() in admins : 
    if passw == admins[uname.lower()] :
        print("Hello {}, you are logged in.".format(uname))
        boole = input("Would you like to change your password : ")
        if boole == 'y' :
            newpassw = input("ENter new password : ")
            while len(newpassw) < 8 :
                print("length of password less than 8")
                newpassw = input("ENter new password : ")
            admins[uname.lower()] = newpassw
            print("Your passsword is changed") 