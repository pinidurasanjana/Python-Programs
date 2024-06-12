try:
    num_1 = int(input("Enter the 1st number: "))
    operator  = input("Select the operator(+ , - , * , /): ")
    num_2 = int(input("Enter the 2nd number: "))

    if operator == '+':
        print(num_1 + num_2)
    elif operator == '-':
        print(num_1 - num_2)
    elif operator == '*':
        print(num_1 * num_2)
    elif operator == '/':
        if num_2 != 0:
            print(num_1/num_2)
        else:
            print('Can not divide by zero.')
        
    else:
        print("Incorrect operator ,Please use (+,-,*,/)")
except:
    print('Value Error')
