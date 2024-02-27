#Error handling


while True:
    try:
        age = int(input('Enter your age : '))
        print (age)
    except ValueError:
        print('Please enter the number')
    except ZeroDivisionError:
        print('Please enter the number')
    else :
        print('Thank you')    
        break 
