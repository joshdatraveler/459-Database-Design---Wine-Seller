import time
import searches as s
import user_classes as uc
import item_classes as ic
import shoppingcart as sc
import sqlite3

def admin_check(user_code): #this executes after sign in
  #check if user is an admin or not, this will be used to determines what their menu shows
  connection = sqlite3.connect('459 Database.db')
  crs = connection.cursor()
  crs.execute("SELECT* FROM admin_accounts WHERE user_code = " + str(user_code))
  admit = (crs.fetchone())
  admit = str(admit)
  connection.commit()
  connection.close()
  
  if admit == 'None':
    return False 
  else:
    return True
      
def mainmenu(user_code): #hub of menus
  admin = admin_check(user_code)
  if admin == True:
    print(admin_menu(user_code))
  elif admin == False:
    print(user_menu(user_code))
  

def admin_menu(user_code):
  sign_in = True
  admin = True
  while sign_in == True: 
    print ('\nWelcome Admin #' + str(user_code) + ' \n\n1. Check a Seller\'s Account Information\n2. View Account Info\n3. Sign Out')
    menu_selection = int(input('\nPlease select an action: '))
    
    #user makes a selection based on number selected
    if menu_selection == 1: #check other user account status (admin only)
      done = 'no' #so the admin can keep searching until they return to the previos menu
      while done == 'no':
        user_search = input('Enter the Seller Number: ')
        connection = sqlite3.connect('459 Database.db')
        crs = connection.cursor()
        crs.execute("SELECT * FROM seller_accounts WHERE user_code = " + str(user_search))
        user = (crs.fetchone())#gets the one case of the user
        class_inst = uc.User(user[0],user[2],user[3],user[1],user[4],user[5])
        print(class_inst.admin_view())
        next = int(input('\n1. Search Another Seller\n2. Return to Admin Menu\nMake a Selection: '))
        if next == 2:
          done = 'yes' #sends us back to admin menu

    elif menu_selection == 2: #view your account info
      print(account_info(user_code,admin))
  
    elif  menu_selection == 3: #sign out
      time.sleep(2)
      sign_in = False
      return 'See you soon\n'
    else:
      print ('That is not an option\n')



def user_menu(user_code):
  sign_in = True
  admin = False
  cart_cost = 0
  numb_in_cart = 0
  while sign_in == True: 
    print ('\n\nWelcome to your Cellar! \nSeller #' + str(user_code) + ' \n1. Search Cellars\n2. List an Item\n3. Manage Items\n4. Account Information\n5. Cart\n6. Sign Out')
    menu_selection = int(input('\nPlease select an action: '))
    #user makes a selection based on number selected
    if menu_selection == 1: #look at other peoples listed items
      numb_in_cart = (s.seller_search(user_code))
      
    elif menu_selection == 2:
      print (ic.create_item(user_code))
    elif menu_selection == 3:
      print(ic.edit_item(user_code))
    elif menu_selection == 4:
      print(account_info(user_code,admin))
    elif menu_selection == 5:
      if numb_in_cart == 0:
        print ('\nYour cart is Empty\n')
      else:
        numb_in_cart = sc.cart(numb_in_cart,user_code)
        
    elif menu_selection == 6:
      time.sleep(2)
      sign_in = False
      return 'See you soon\n'
    else:
      print('Sorry, thats not an option\n')

  
  
      #search
      #view listed items (sub menu for editing   listings)
      #list item
      #manage offers
      #account info
  pass

def account_info(user_code,check): #takes in the user code and if it is an admin
  connection = sqlite3.connect('459 Database.db')
  crs = connection.cursor()
  if check == False: #if not an admin, it gives the layout for seller
    ac_type = 'seller_accounts'
    crs.execute("SELECT * FROM seller_accounts WHERE user_code = " + str(user_code))
    user = (crs.fetchone())#gets the one case of the user
    class_inst = uc.User(user[0],user[2],user[3],user[1],user[5],user[4])
    print(class_inst.user_view())
  else: #layout for admin account details
    ac_type = 'admin_accounts'
    crs.execute("SELECT * FROM admin_accounts WHERE user_code = " + str(user_code))
    user = (crs.fetchone())#gets the one case of the user
    class_inst = uc.Admin(user[0],user[2],user[3],user[1])
    print(class_inst.user_view())
    time.sleep(2)
  #edit info
  change = int(input('\nWould you like to change any of this information: \n1.Yes \n2.No\nSelect the Corresponding number: '))
  if change == 2:
    return('Returning to your Cellar')
  else:
    while change == 1: 
      print('\nWhat would you like to change?\n1. Name\n2. Password\n3. Return to Menu')
      att_adj = int(input())
      if att_adj == 1:
        f_name = input('Enter your First Name: ')
        l_name = input('Enter your Last Name: ')
        crs.execute("UPDATE " + str(ac_type) + " SET f_name = '" + str(f_name) + "' WHERE user_code = " + str(user_code))
        crs.execute("UPDATE " + str(ac_type) + " SET l_name = '" + str(l_name) + "' WHERE user_code = " + str(user_code))        
        connection.commit()
        connection.close()
        more_change = (int(input('Would you like to make more changes? \n1. Yes\n2. No\n')))
        if more_change == 2:
          return ('Returning to your Cellar')
          change = 2
      elif att_adj == 2:
        password = input('Enter your  new password: ')
        crs.execute("UPDATE " + str(ac_type) +" SET password =  "+ str(password)+' WHERE user_code = ' + str(user_code))
        crs.execute("UPDATE account SET password =  '"+ str(password)+"' WHERE user_code = " + str(user_code))
        connection.commit()
        connection.close()
        more_change = (int(input('Would you like to make more changes? \n1. Yes\n2. No\n')))
        if more_change == 2:
          return ('Returning to your Cellar')
          change = 2
      else:
        return('Returning to your Cellar')
        change = 2
    
    