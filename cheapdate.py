# This is an app using the prompts in
# https://colab.research.google.com/drive/1CoAsGy8_4fv6Z6LS_JKoGq27oe8zKjui?usp=sharing#scrollTo=iRsJmpm-bpxS
# Called A date to remember!
#



myName= 'Angela'
myDate= 'Darryl'
#restaurnats= ['Macaroni\s', 'Blue Claw', 'Pappadeaux', 'Parc']
restaurant="Macaroni\'s"
#spend = 0
dateReviews=['ok', 'wonderful', 'meh', 'fantastic']
menu = {
    'antipasti':'14',
    'salad': '12',
    'pasta': '25', 
    'dessert':'11'

}

# Welcome Statement
print(f"Welcome {myName} and {myDate} to {restaurant}.")
print('How much are you looking to spend this evening?:')
spend=int(input())

# functions

def order():

  print('Great, we have plenty on the menu to fit your needs. What would you like to order?')
  print(menu)

  print('Would anyone like antipasti? (yes or no)')
  antipasti = input()

  if antipasti == 'yes':
    global spend
    spend = spend - int(menu['antipasti'])
    #print(f'You have ${spend} left.')

  else:
    print('Ok, what else woud you like')

  print('How about a salad? (yes or no)')
  salad = input()
  if salad == 'yes':
    spend= spend - int(menu['salad'])
    #print(f'You have ${spend} left.')

  else:
    print('Sure, no problem')

  print('Are either of you feeling like pasta? (yes or no)')
  pasta = input()
  if pasta == 'yes':
    spend= spend - int(menu['pasta'])
    #print(f'You have ${spend} left.')

  else:
    print('Anything else?')

  print('How about dessert? (yes or no)')
  dessert = input()
  if dessert == 'yes':
    spend= spend - int(menu['dessert'])
    #print(f'You have ${spend} left.')

  else:
    print('Ok')

  print('I will be back with your order')

# Date Rate Will there will be another date
def status():
    print(f'So how is your date going {myName}? ')
    print(dateReviews)
    status=input()

    if status == 'ok':
        print('Looks like you may not get another date')
    
    elif status == 'wonderful':
        print('Somebody is getting a second date!!!!')
    
    elif status == 'meh':
        print(f'You are NOT getting a second date with {myDate}!')
    else:
        print('Have fun on your second date!')

def bill():

  
  print(f'You have ${spend} left.')
     
order()

# Date status
status()

# Bill
bill()


