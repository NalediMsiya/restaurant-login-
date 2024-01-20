# Savoured moments app 
#=========importing libraries========#
import datetime
from datetime import date
# welcome message 
print("Hello welcome to savoured moments with sedii!")
# creating a class to store client information in our system
class Client(object):
    def __init__(self, name,contact,location,age,gender,user_id,security_code):
        self.name = name 
        self.contact = contact
        self.location = location
        self.age = age
        self.gender = gender
        self.user_id = user_id
        self.security_code = security_code
    
    def client_name(self):
        print(f"Welcome to savoured moments{self.name}, we are happy you have chosen to fill your precious tummy with us!")
# creating a database/system to store client information 
file = open("client_database.txt","r")
list_1 = [] 
existing_user = []
existing_password = []
counting = []     

def password_login(list_1,file):
    global username
    global clients
    log_in = input('''Please login or sign up:
a. log in
b. sign up
'''). lower()
    if log_in == "a":
        username = input("Please enter your userame: ")
        password = input("Please enter your password: ")
        read_file = open("client_database.txt","r")
        lines = read_file.readlines()
        for x in lines:
            strip_lines = x.strip()
            split_lines = strip_lines.split(",")
            existing_user.append(split_lines[5])
            existing_password.append(split_lines[6])
            if username in existing_user and password in existing_password: 
                if username == split_lines[5]:
                    print(f"Thank you for loging in {split_lines[0]} !")
                    file_2 = open("sale.txt","a")
                    file_2.write(username)
                    file_2.write(",")
                    file_2.write(str(current.month))
                    file_2.write("\n")
        while username not in existing_user or password not in existing_password:
            print("Incorrect login details please try loging in again")
            username = input("Please enter your userame: ")
            password = input("Please enter your password: ")
    elif log_in == "b":
        a = input("Please enter your name: ")
        b = input("Contact: ")
        c = input("Address: ")
        d = input("Age: ")
        e = input("Gender: ")
        f = input("Username: ") 
        g = input("password: ")
        h = input("Enter password again: ")
        if g == h:
            print("Thank you for signing up")
            clients = Client(a,b,c,d,e,f,g)
            list_1.append(clients)
            file = open("Client_database.txt","a")
            file.write(a)
            file.write(",")
            file.write(b)
            file.write(",")
            file.write(c)
            file.write(",")
            file.write(d)
            file.write(",")
            file.write(e)
            file.write(",")
            file.write(f)
            file.write(",")
            file.write(g)
            file.write("\n")
            file_2 = open("sale.txt","a")
            file_2.write(f)
            file_2.write(",")
            file_2.write(str(current.month))
            file_2.write("\n")
        else:
            print("Passwords do not match, please try again")
            g = input("password: ")
            h = input("Enter password again: ")
        
print(list_1)
amount = 0
current = date.today()

order = input('''Would you like to:
a. Place an order                
b. Enquire
c. login as an employee
d. exit 
(reply with relevent alphabet)
''').lower()
while order == "a":
    enter = password_login(list_1,file)
    menu = input('''Please make selection below:
breakfast
Lunch
drinks
sides 
''').lower()
    if menu == "breakfast":
        breakfast = input('''Please select the breakfast meal of your choice:
a. beacon and eggs
b. all bran and yoghurt
c. muesli and yoghurt
d. fruit salad
e. bacon,eggs and russians
f. muffins and coffee 
''').lower()
        quantity = int(input("Thank you for your order, how many orders of this item would you like?: "))
        question = input("Would you like to order again? (yes/no): ").lower()
        while question == "yes":
            breakfast = input('''Please select the breakfast meal of your choice:
a. beacon and eggs
b. all bran and yoghurt
c. muesli and yoghurt
d. fruit salad
e. bacon,eggs and russians
f. muffins and coffee 
''').lower()
            quantity = int(input("Thank you for your order, how many orders of this item would you like?: "))
            question = input("Would you like to order again? (yes/no): ").lower()    
        else:
            print("Thank you for your order, please wait for a few minutes while we prepare your meal!")
            break    
    elif menu == "lunch":
        lunch = input('''Please select the meal you'd like to have for lunch:
a. sticky wings and chips
b. fried wings and chips
c. samp and beef
d. savoury rice and chicken
e. pork ribs and chips
f. chicken schnitzel and chips
g. phuthu and chicken curry
h. phuthu and beef curry
''').lower()
        quantity = int(input("Thank you for your order, how many orders of this item would you like?: "))
        question = input("Would you like to order again? (yes/no): ").lower()
        while question == "yes":
                lunch = input('''Please select the meal you'd like to have for lunch:
a. sticky wings and chips
b. fried wings and chips
c. samp and beef
d. savoury rice and chicken
e. pork ribs and chips
f. chicken schnitzel and chips
g. phuthu and chicken curry
h. phuthu and beef curry
''').lower()
                quantity = int(input("Thank you for your order, how many orders of this item would you like?: "))
                question = input("Would you like to order again? (yes/no): ").lower()
        else:
            print("Thank you for your order, please wait as we prepare your meal")
            break
    elif menu == "drinks":
        drinks = input('''please select the drink you'd like to have:
a. coffee
b. tea
c. cuppacino
d. hot chochoate
e. soda
f. water
g. juice
h. wine/alcoholc beverage
''').lower()
        num_of_drinks = int(input("Enter the number of drinks you'd like to order: "))
        if drinks == "e":
            soda_type = input(''''Which kind of soda would you like: ''').lower()
            print(soda_type,"coming your way!")
            extra = input(" Would you like to order something else?(yes/no): ").lower()
            if extra == "yes":
                continue 
            else:
                break    
        elif drinks == "g":
            juice_type = input("Enter the type of juice you would like: ").lower()
            print(juice_type,"coming your way!")
            extra = input(" Would you like to order something else?(yes/no): ").lower()
            if extra == "yes":
                continue 
            else:
                break 
        elif drinks == "h":
            wine_type = input("Enter the type of wine/alcohol beverage you would like: ").lower()
            print(wine_type,"coming your way!")
            extra = input(" Would you like to order something else?(yes/no): ").lower()
            if extra == "yes":
                continue 
            else:
                break 
        else:
            print("Thank you for your order")
            break
    elif menu == "sides":
        sides = input('''Which side would you like?:
a. chips
b. coeslow salad
c. beetroot salad
d. potato salad
e. potato and egg salad
f. green salad
g. creamy spinach
h. sauted mushrooms
i. mashed butternut
''').lower()
        quantity_of_side = int(input(f"Enter the number of {sides} you would like: "))
        requests = input("Are there any other requests or sprcifications you have: ")
        ask = input("Would you like to order anything else?(yes/no): ").lower()
        if ask == "yes":
            continue
        else:
            break 
    else:
        print("your selecion is incorrect, please choose the correct item on the menu")
        continue
if order == "b":
    print("Thank you for contacting us, we will get back to you as soon as we can  please fill in the section below")
    igama = input("please enter your name and surname: ")
    num = input("Please enter your number: ")
    mail = input("Please enter your email address")
    message = input("Enter your message: ")
if order == "c":
       # finding the current date 
    staff = input("Enter username: ")
    passcode = input("Enter your password: ")
    if staff == "Malesedi" and passcode == "gifts are ours forever":
       read_file = open("sale.txt","r")
       read_lines = read_file.readlines()
       for x in read_lines:
           xstrip = x.strip()
           xsplit = xstrip.split(",")
           counting.append(xsplit)
    pass
    x = int(current.month)
    for i in counting:
        if str(x) in str(i[-1]):
            login_times = counting.count(i)
            if login_times > 1:
                print(f"{i[0]} deserves a sale, they have loged in {login_times} times this month ({current.month}/{current.year})")
                break
                    
    else:
        print("incorrect log in details")
if order == "d":
    print("Thank you for visiting savoured moments! do check in again, we value your presence!")
    
        

    



        
    
    



