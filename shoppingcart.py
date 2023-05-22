import sqlite3
import time

def cart(quantity,user):
  #check what item the user has
  connection = sqlite3.connect('459 Database.db')
  crs = connection.cursor()
  crs.execute("SELECT purchased_items FROM seller_accounts WHERE user_code = " + str(user))
  item = (crs.fetchone())
  item_code = item[0]
  crs.execute("SELECT seller_code FROM items WHERE item_code = " + str(item_code))
  cellar_code = (crs.fetchone())
  cellar_code = cellar_code[0]
  crs.execute("SELECT price FROM items WHERE item_code = " +str(item_code))
  price = (crs.fetchone())
  connection.commit()
  connection.close()
  price = price[0]
  total = price * quantity
  pre_tax_total = round(total,2)
  tax = round((total*0.09),2)
  print ('Your cart:')
  print('\nSeller Code: '+str(cellar_code)+ '     Item Code: '+ str(item_code) + '\nPrice (before tax): ' + str(pre_tax_total) + '            Quantity: ' + str(quantity) + '\nTax: ' + str(tax)+ '\nPrice(including tax): ' + str(round((pre_tax_total + tax),2)))
  print('\n\n_____________________________________\n')
  checkout = int(input('Would you like to:\n1. Checkout?\n2. Edit Cart\n3. Return to Cellar\n\nMake a Selection: '))
  if checkout == 3:
    print ('Returning to your Cellar')
    return quantity
  elif checkout == 2:
    print ('What would you like to Edit: \n1. Quantity\n2. Return to Menu\n')
    choose = int(input())
    if choose == 2:
      print ('Returning to your Cellar')
      return quantity
    elif choose == 1:
      #gotta find the max
      connection = sqlite3.connect('459 Database.db')
      crs = connection.cursor()
      crs.execute("SELECT quantity FROM items WHERE item_code = " +str(item_code))
      curr_tot = (crs.fetchone())
      curr_tot = curr_tot[0]
      max = curr_tot+quantity
      new_quant = int(input('Enter the new quantity (Max = '+str(max)+'):'))
      new_stock = max - new_quant
      item_str = ("UPDATE items SET quantity = " +str(new_stock) + " WHERE item_code = " + str(item_code))
      crs.execute(item_str)
      connection.commit()
      connection.close()
      new_price = round((new_quant*price),2)
      print ('New Cart: \n')
      print('\nSeller Code: '+str(cellar_code)+ '     Item Code: '+ str(item_code) + '\nPrice: ' + str(new_price) + '            Quantity: ' + str(new_quant))
      print('\n\nReturning to Cellar')
      time.sleep(2)
      return quantity
    else:
      print('Your total is $'+str(pre_tax_total + tax))
      connection = sqlite3.connect('459 Database.db')
      crs = connection.cursor()
      item_str = ("UPDATE seller_accounts SET puchased_items = NULL WHERE user_id = " + str(user))
      crs.execute(item_str)
      connection.commit()
      return 0
      
  