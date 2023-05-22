import sqlite3
import item_classes as ic

def seller_search(user):
  done = 'no'
  while done == 'no':
    cellar_search = input('Enter the Seller Number: ')
    connection = sqlite3.connect('459 Database.db')
    crs = connection.cursor()
    crs.execute("SELECT listed_items FROM seller_accounts WHERE user_code = " + str(cellar_search))
    item = (crs.fetchone())#gets the users listed item
    item2 = str(item)
    print(item2)
    if item2 == 'None':
      #print('This user hasn\'t listed anything')
      again = int(input('Would you like to search again?\n1. Yes \n2. No\n'))
      if again == 2:
        done = 'yes'
        return 'Returning to your Cellar\n'
    else:
      item = item[0]
      #print(item)
      crs.execute("SELECT * FROM items WHERE item_code = " + str(item))
      item_details = crs.fetchone()
      item_inst = ic.Item(item_details[1],item_details[3],item_details[4],item_details[5],item_details[2],item_details[0])
      print(item_inst.display()) #displays item attributes
      #ask if purchase, search again, or menu
      choice = int(input('\nWould you like to \n1. Add to cart\n2. Make a New Search\n3. Go to the Cellar\nPlease make a selection: '))
      if choice == 1:
        cart_loop = True
        while cart_loop == True:
          crs.execute("SELECT quantity FROM items WHERE item_code = " + str(item))
          max = crs.fetchone()
          max = int(max[0])
          quantity = int(input('How many Units would you like to add to cart (Max = '+ str(max)+'): '))
          if quantity > max:
            print ('Too many units')
          elif quantity == 0:
            print ('Not enough Units')
          else:
            new_stock = max-quantity
            total = item_details[3] * quantity
            pre_tax_total = round(total,2)
            print ('Your cart:')
            print('\nSeller Code: '+str(cellar_search)+ '     Item Code: '+ str(item) + '\nPrice: ' + str(pre_tax_total) + '            Quantity: ' + str(quantity))
            connection = sqlite3.connect('459 Database.db')
            crs = connection.cursor()
            user_str = ("UPDATE seller_accounts SET purchased_items = "+str(item)+" WHERE user_code = "+str(user))
            item_str = ("UPDATE items SET quantity = " +str(new_stock) + " WHERE item_code = " + str(item))
            crs.execute(user_str)
            crs.execute(item_str)
            connection.commit()
            connection.close()
            print ("\nReturning to your Cellar")
            return quantity
            
        
      elif choice == 3:
        done = 'yes'
        return 'Returning to your Cellar\n'
      

    

  