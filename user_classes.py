import sqlite3

class User:
  def __init__(self,user_code, f_name,l_name,password,listed_items,purchased_items):
    self.user_code = user_code
    self.f_name = f_name
    self.l_name = l_name
    self.password = password
    self.listed_items = listed_items
    self.purchased_items = purchased_items

  def admin_view(self):
    return('Seller Code: ' + str(self.user_code) + '\nFirst Name: ' + str(self.f_name) + '     Last Name: ' + str(self.l_name) + '\nListed Items: ' + str(self.listed_items) + '\nCart items: ' + str(self.purchased_items))
    
  def user_view(self):
    return('Seller Code: '+str(self.user_code)+ '     Password: ' +str(self.password) + '\nFirst Name: ' + str(self.f_name) + '     Last Name: ' + str(self.l_name)+'\nListed Item: ' + str(self.listed_items) + '\nCart Items: ' + str(self.purchased_items))
      

class Admin:
  def __init__(self,admin_code, f_name,l_name,password):
    self.admin_code = admin_code
    self.f_name = f_name
    self.l_name = l_name
    self.password = password

  def user_view(self):
    return('Admin Code: '+str(self.admin_code)+ '     Password: '
             +str(self.password) + '\nFirst Name: ' + str(self.f_name) +
             '     Last Name: ' + str(self.l_name))

class Account:
  def __init__(self, user_code, password):
    self.user_code = user_code
    self.password = password
