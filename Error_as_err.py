def sum(num1, num2):
    try  :
        return (num1/num2)
    except (ValueError, ZeroDivisionError) as err:
        #print(f'Enter the number {err}')
        print(err)

print(sum(3,0))