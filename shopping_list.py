# 2. The Shopping List Maker
# user_remove = input('What would you like to remove?')
shoplist = []


def option (shoplist): 
  while True:
    user_option = input ('Do you want to add or remove from your list?')
    if user_option == 'add':
       shopping (shoplist)
         
    elif user_option == 'remove':
        remove(shoplist)
        break
    else:
      print ('Invalid input please try again')

    

def shopping (shoplist):
    
  user_add = input('What would you like to add?')
  shoplist.append(user_add)
  print (shoplist)
       



def remove (shoplist): 
   user_remove = input('What would you like to remove?')
   shoplist.remove(user_remove)
   print (shoplist)


    
option (shoplist)
    