while True:
    try :
        age = int(input('Enter the age : '))
        10/age
        raise ValueError('Enter the number')

    except ValueError as err:
        print(err)
        continue
    except ZeroDivisionError as err:
        print(err)
        break
    else:
        print('Operation finished')
    finally :
        print('Please check if you are successful')
    print('Have a good day')
    
