import sqlite3
import random
import time

class Item:
  def __init__(self,seller_code,price,desc,quantity,item_name,item_code):
    self.seller_code = seller_code
    self.price = price
    self.desc = desc
    self.quantity = quantity
    self.item_name = item_name
    self.item_code = item_code

  def display(self):
    return ('\nSeller Code: '+str(self.seller_code)+ '     Item Code: ' + str(self.item_code) + '\nPrice: ' + str(self.price) + '            Quantity: ' + str(self.quantity) + '\n' + str(self.item_name) + '\n Description:  ' + str(self.desc))


#create an item - this code will be linked to an insert statement in SQLITE
def create_item(seller_code):
  connection = sqlite3.connect('459 Database.db')
  crs = connection.cursor()
  name = input('Enter a product name: ')
  price = float(input('Enter the items price: '))
  quantity  = int(input('Enter the quantity of the item: '))
  desc = input('Enter a brief description of the product:\n ')
  seven_numb = []
  count = 0
  #create 7 random numbers
  while count != 7:
    numb = random.randint(1,9)
    numb = str(numb)
    seven_numb.append(numb)
    value = ''.join(seven_numb)
    count +=1
    #value is the unique item code
  item_code = int(value)

  connection = sqlite3.connect('459 Database.db')
  crs = connection.cursor()
  item_str = ("INSERT INTO items VALUES(" + str(item_code) + "," + str(seller_code) + ",\'" + str(name) + "\'," + str(price) + ",\'" + str(desc) + "\'," + str(quantity) + ")" )
  #test
  user_str = ("UPDATE seller_accounts SET listed_items = "+str(item_code)+" WHERE user_code = "+str(seller_code))

  crs.execute(item_str)
  crs.execute(user_str)
  connection.commit()
  connection.close()
  #test
  #crs.execute("SELECT * FROM items")
  #print(crs.fetchall())
  
  return ('\nSeller Code: '+str(seller_code)+ '     Item Code: ' + str(item_code) + '\nPrice: ' + str(price) + '            Quantity: ' + str(quantity) + '\n' + str(name) + '\n Description:  ' + str(desc))

def edit_item(seller_code):
  run = 'ye'
  while run == 'ye':
    connection = sqlite3.connect('459 Database.db')
    crs = connection.cursor()
    crs.execute("SELECT listed_items FROM seller_accounts WHERE user_code = " + str(seller_code))
    item_code = crs.fetchone()
    #print (item_code)
    item_code = str(item_code)
    print (item_code)
    if item_code == '(None,)':
      print('You currently have no items\n')
      run = 'na'
      time.sleep(2)
      return('Returning to menu\n')
    crs.execute("SELECT * FROM items WHERE seller_code = " + str(seller_code))
    item_details = crs.fetchone()
    item_inst = Item(item_details[1],item_details[3],item_details[4],item_details[5],item_details[2],item_details[0])
    print(item_inst.display())
    print('\n1. Edit Descriptors\n2. Change Price\n3. Adjust Stock\n4. Return to Menu')
    choice = int(input('\nPlease Select an Action: '))
    time.sleep(1)
    if choice == 1:
      name = input('Enter the name: ')
      desc = input('Enter the description: ')
      crs.execute("UPDATE items SET item_name = '" + str(name) + "' WHERE item_code = " + str(item_details[0]))
      crs.execute("UPDATE items SET desc = '" + str(desc) + "' WHERE item_code = " + str(item_details[0]))        
      connection.commit()
      connection.close()
      keep = int(input('Would you like to edit something else? \n1. Yes\n2. No\n'))
      if keep == 2:
        run = 'na'
        return('Returning to menu\n')
    elif choice == 2:
      price = float(input('Enter the price: '))
      crs.execute("UPDATE items SET price = '" + str(price) + "' WHERE item_code = " + str(item_details[0]))
      connection.commit()
      connection.close()
      keep = int(input('Would you like to edit something else? \n1. Yes\n2. No\n'))
      if keep == 2:
        run = 'na'
        return('Returning to menu\n')
    elif choice == 3:
      stock = int(input('Enter the corrected inventory amount: '))
      crs.execute("UPDATE items SET quantity = '" + str(stock) + "' WHERE item_code = " + str(item_details[0]))
      connection.commit()
      connection.close()
      keep = int(input('Would you like to edit something else? \n1. Yes\n2. No\n'))
      if keep == 2:
        run = 'na'
        return('Returning to menu\n')
    elif choice == 4:
      run = 'na'
      return('Returning to menu\n')
    else:
      print('Sorry, that wasnt an option')


    
