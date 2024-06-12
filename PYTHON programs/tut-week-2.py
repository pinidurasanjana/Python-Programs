print('1.CM to Meter , 2.Meter to CM')
option = int(input('Please enter 1 or 2: '))
if option == 1:
    cm = int(input('Please enter a number in CM: '))
    M = cm/100
    print(cm,'is equal to',M,'meters.')
else:
    m = int(input('Please enter a number in M: '))
    CM = m * 100
    print(m,'is equal to',CM,'meters.')
    
    
