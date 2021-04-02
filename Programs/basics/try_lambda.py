'''
Write a program named try_lambda.py that contains a lambda expression that converts Fahrenheit  to Celsius.
Accept the Fahrenheit temperature and display the Celsius result using the lamba. The formula is: C = 5/9 x (F-32)
'''

temp_in_f = input("Enter the temperature in Fahrenheit = ")

# define lamba anonymous function to convert from fahrenheit
find_temp_in_c = lambda f: 5/9 * ( f - 32)
temp_in_c = round(find_temp_in_c(float(temp_in_f)),2)
print("Temperature in Celsius for {} = {}".format(temp_in_f, temp_in_c))