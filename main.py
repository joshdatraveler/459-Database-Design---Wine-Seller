
import mainmenu as mm
import random
import sqlite3
import searches as s
import user_classes as uc
import item_classes as ic

#login
def login():
  #needs to return user code
  done = False #done equals true  when login succesful
  while done == False:
    user_code = int(input('Please enter your five digit user-code: '))
    password = input('Enter your password: ')
    connection = sqlite3.connect('459 Database.db')
    crs = connection.cursor()
    crs.execute("SELECT * FROM account WHERE account_id = " + str(user_code) + " AND password = \'" + str(password) + "\'")
    account = (crs.fetchone())
    account = str(account)
    #print(account)
    connection.commit()
    connection.close()
    
    if account == 'None':
      print ('Username or password is false')
      cont = int(input('Would you like to \n1. Sign In \n2. Make an Account\nEnter Corresponding Number: '))
      if cont == 2:
        user_code = account_create()
        done = True
        return user_code
    else:
        return user_code

#startup menu
def startup():
  done = False
  while done == False:
    init_prompt = int(input('1. Sign in\n2. Create account\n3. Close Program\n\nEnter corresponding number: '))
    if init_prompt == 1:
      account = login()
      return account
      done = True
    elif init_prompt == 2:
      account = account_create()
      return account
      done = True
    elif init_prompt == 3:
      print('Thanks for using Wine Seller')
      done = True
      return ('end program')
    else:
      print('Sorry, that is not an option. ')
      continue

#create an account
def account_create():
  #usercode equals 5 digit code thats next in line
  done = False #done equals true when account dreated and login succesful
  while done == False:
    five_numb = []
    count = 0
    #create 5 random numbers
    while count != 5:
      numb = random.randint(1,9)
      numb = str(numb)
      five_numb.append(numb)
      value = ''.join(five_numb)
      count +=1
      #value is becoming an int at this point
    user_code = int(value)
    password = input('Please create a password: ')
    f_name = input ('Enter your First Name: ')
    l_name = input ('Enter your Last Name: ')
    connection = sqlite3.connect('459 Database.db')
    crs = connection.cursor()
    sellstring = ('INSERT INTO seller_accounts VALUES(' + str(user_code) + ",\'" + str(password) + "\',\'" + str(f_name) + "\',\'" + str(l_name) + '\',NULL,NULL)' )
    accstring = ('INSERT INTO account VALUES(' + str(user_code) + ",\'" + str(password) + '\')' )
    crs.execute(sellstring)
    crs.execute(accstring)
    connection.commit()
    connection.close()
  #for account table
    #INSERT account
    #VALUES (user_code,password)
  #for seller account table
    #INSERT seller_account
    #VALUES (user_code,password,f_name,l_name)
    done = True
    return user_code


# this is the main loop, once this ends, software shuts down.
run = 'yes'
while run == 'yes':
  code = startup()
  if code == 'end program': #logout stuff (just end process)
    run = 'stop'
  else:
    mm.mainmenu(code)
   

#This is where we created the tables

#connection = sqlite3.connect('459 Database.db')
#crs = connection.cursor()
#crs.execute("SELECT * FROM items")
#print(crs.fetchone())
#crs.execute("ALTER TABLE seller_accounts DROP COLUMN listed_items")
#crs.execute("ALTER TABLE seller_accounts ADD COLUMN listed_items INTEGER")
#crs.execute("ALTER TABLE seller_accounts DROP COLUMN purchased_items")
#crs.execute("ALTER TABLE seller_accounts ADD COLUMN purchased_items INTEGER")

#connection.commit()
#connection.close()


us_co = 75603
item_code = 1267892
#code = startup()
#crs.execute("""CREATE TABLE account(account_id INTEGER PRIMARY KEY, password TEXT)""")
#crs.execute("""CREATE TABLE seller_accounts(user_code INTEGER PRIMARY KEY,password TEXT,f_name TEXT, l_name TEXT,listed_items LIST,purchased_items LIST, FOREIGN KEY (user_code) REFERENCES account(account_id)ON DELETE CASCADE,FOREIGN KEY (password) REFERENCES account(password) ON UPDATE CASCADE)""")
#crs.execute("""CREATE TABLE admin_accounts( user_code INTEGER PRIMARY KEY,password TEXT,f_name TEXT, l_name TEXT, FOREIGN KEY (user_code) REFERENCES account(account_id) ON DELETE CASCADE,FOREIGN KEY (password) REFERENCES account(password)  ON UPDATE CASCADE)""")
#crs.execute("""CREATE TABLE items(item_code INTEGER PRIMARY KEY, seller_code INTEGER, item_name TEXT, price REAL, desc TEXT, quantity INTEGER,FOREIGN KEY (seller_code) REFERENCES account(account_id) ON DELETE CASCADE)""")

#crs.execute(account_table)
#crs.execute(seller_table)
#crs.execute(admin_table)
#crs.execute(item_table)


#account is ID, password
#seller account is ID, password, fname,lname,,listed,purchased
#admin account is ID,password,fname,lname
#items is itemcode,seller_code,name,price,desc,quantity
#crs.execute("INSERT INTO seller_accounts VALUES (54765,'jklop94','Josh','Walker','N/A','N/A')")
#crs.execute("INSERT INTO admin_accounts VALUES (99999,'testadmin','Josh','Walker')")
#crs.execute("INSERT INTO admin_accounts VALUES (11111,'testadmin2','Kenneth','Burwell-Tibbs')")
#crs.execute("INSERT INTO account VALUES (99999, 'testadmin')")
#crs.execute("INSERT INTO account VALUES (11111, 'testadmin2')")
#crs.execute("DELETE FROM seller_accounts WHERE password = 'saucyseller'")


#test if all accounts are there
#delete in final version
'''
user_search = input('Enter the Seller Number: ')
connection = sqlite3.connect('459 Database.db')
crs = connection.cursor()
crs.execute("SELECT * FROM seller_accounts WHERE user_code = " + str(user_search))
user = (crs.fetchone())#gets the one case of the user
class_inst = uc.User(user[0],user[2],user[3],user[1],user[4],user[5])
print(class_inst.admin_view())





user_search = input('Enter the Seller Number: ')
connection = sqlite3.connect('459 Database.db')
crs = connection.cursor()
crs.execute("SELECT user_code, f_name,l_name,listed_items, purchased_items FROM seller_accounts WHERE user_code = " + str(user_search))
admit = (crs.fetchone())
print (admit[0])

crs.execute("SELECT * FROM account")
print(crs.fetchall())
crs.execute("SELECT * FROM seller_accounts")
print(crs.fetchall())
connection.commit()
connection.close()
'''