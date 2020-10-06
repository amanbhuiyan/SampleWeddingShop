import json
import sys

 # grab .json file into pyhthon list
 # each item on the list, itself a dictionary.

json_file= open("/Users/mdamanullahbhuiyan/Documents/Aman Files/Projects/Python Projects/Wedding shop/products.json", "r")
products = json.load(json_file)

# asing user to input selection, 
#  select feature from the list below

print('===================================================')
print('Please enter your choice')
print('===================================================')
print('L for Listing all items')
print('A for adding a new item')
print('R for removing an item')
print('P for purchase an item and for Reporting')
Choice = input('Please enter your choie now\n ')

# function to display all items
def showAllItems():
    try:
        print("Display all products from the json file")
        for i in products:
            print(i)
        print('===================================================')
    except:
        e = sys.exc_info()
        print(e)
        print('Error occured- Please contact your administrator')

#  display only product name- [ all prodcuts is a list here and each iteam of that list is a dictoonary ]

def showOnlyProductsName(products):
    print("Display only all products name ")
    print('==============================================')
    for i in products:
        print(i.get('name'))
    print('==============================================')

# Function to add an iteam to the list

def addAnItem():
    try:
        # get id of the last item
        lengthOfList = len(products)
        idLastItem= products[lengthOfList-1].get('id')
        # get id of the new item- dynamically
        idNewItem= idLastItem +1
        name = input("Please enter the new products name \n")
        brand_newProduct = input("Please enter the new products brand \n")
        price_newProduct = int(input("Please enter the new products price \n"))
        quantity_newProduct = int(input("Please enter the new products quantity \n"))
        a_newIteam =  {'id': idNewItem, 'name':name,'brand':brand_newProduct,'price':price_newProduct, 'in_stock_quantity': quantity_newProduct}
        #  dictionary_copy = a_dictionary.copy()
        products.append(a_newIteam)
        # Show the last item that has been  just added, with its meta data
        lengthOfList = len(products)
        print(products[lengthOfList-1])
    except:
        e = sys.exc_info()
        print(e)
        print('Error occured- Please contact your administrator')

# Function to remove an item from the list , 
# Remove by id or by product name

def removeAnItem():
    try:
        print('===================')
        print('please enter the right choice')
        print('===================')
        print('Enter id - if you want to delte an item by its id ')
        print('Enter name - if you want to delte an item by its name ')
        deleteBy = input('Now please enter your choice , - id or name \n')
        # if delted by - id
        if deleteBy == 'id':
            idtobeDeleted= int(input('id number of the item - you want to delte \n'))
            for i in products:
                if i.get('id')==idtobeDeleted:
                    # del products[idtobeDeleted]
                    products.remove(i)
                    print('Item deleted\n')
                    break
        # Display all items after deletion an item
            for i in products:
                print(i)

        # if delted by - name
        if deleteBy == 'name':
            nameTobeDeleted= input('Name of the item - you want to delete \n')
            for i in products:
                if i.get('name')==nameTobeDeleted:
                    products.remove(i)
                    print('Item deleted\n')
                    break
        # Display all items after deletion an item
            for i in products:
                print(i)
    except:
        e = sys.exc_info()
        print(e)
        print('Error occured- Please contact your administrator')


# Function to purchase an Item
#  and also reporting of purchased items and unparchased items

def purchaseAGift():
    try:
        print('Please Enter name of the gift you want to purchase from the list below\n')
        for i in products:
            print(i.get('name'))
        giftToBuy = input('Now enter the gift that you want to buy from the  list above\n')
        quantityToBuy = int(input('Enter how many item of this gift you want to buy \n'))
        print('you want to buy ' + str(quantityToBuy)  + ' ' + str(giftToBuy) )
        for i in products:
            if i.get('name')==giftToBuy:
                quantityAvilable = i.get('in_stock_quantity')
                print(str(quantityAvilable) + ' Avilable  - '  + giftToBuy) 
                confirmation = input('Do you want to procede with your purchase  ?, please enter Yes  or No \n')
                if confirmation== 'Yes':
                    quantityremaining= int(quantityAvilable) - int(quantityToBuy)
                    print(quantityremaining)
                    i['in_stock_quantity'] = quantityremaining
                    print('Current condition after purchase ')
                    print(str(quantityremaining) + ' items Remaining  after purchase of  - ' + str(quantityToBuy) + ' -' + giftToBuy) 
                    print('After purchase- product status - with quantiy in stock ')
                    print('================================================')
                    print('product item after purchase - in the list')
                    print (i)
                    print('=================================================')
                    print('Report Section ')
                    print('=================================================')
                    print('Purchased Items and Current Status ')
                    print('=================================================')
                    print(giftToBuy + ' - ' + str(quantityToBuy)  + ' items purchased and -- Remaining - ' + str(quantityremaining) + ' items')
                    print('Unpurchased Items and Current Status ')
                    print('=================================================')

                if confirmation=='No':
                    print('=================================================')
                    print('You have choosen not to purchase ' + giftToBuy )
                    print('Please feel free to buy later or be in touch with us if you need any help ')
                    print('=================================================')

            print(i.get('name') + ' - Avilable items  -  ' + str(i.get('in_stock_quantity')))

    except:
        e = sys.exc_info()
        print(e)
        print('Error occured- Please contact your administrator')


        

            
                
    
    
    
    #print('number of Avilable ' + str(giftToBuy)  + ' is' + str(quantityAvilable ))
    
# calling functions based on the selection of features    

if Choice=='L':
    showAllItems()
if Choice=='A':
    addAnItem()
if Choice=='R':
    removeAnItem()
if Choice=='P':
    purchaseAGift()











    

