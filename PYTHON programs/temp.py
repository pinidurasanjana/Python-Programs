print('1-Celsius to Fahrenheit , 2-Fahrenheit to Celsius')
value = int(input('Enter the number: '))
if value == 1:
    c = float(input('Enter the temperature: '))
    f = (c*1.8)+32
    print(f,'F')
elif value == 2:
    f = float(input('Enter the temperature: '))
    c = (f - 32)/1.8
    print(c,'C')
else:
    print('Invalid option entered')
    
