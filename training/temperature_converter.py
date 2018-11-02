#!/usr/bin/python
F_SUBSTRACTION_C_ADDITION = 32
F_DIVISION_C_MULT = 1.800
DECIMALS = 2

#list of temperatures to pass for map funcion and iter for every function
temperatures = [85,42,3,96,87,36,49,71,63,6,78]


class Converter(object):
    """ 
    Converter
    
    """
    def celcius_fahrenheit(self, value):
        """ 
        celcius to fahrenheit
        
        This function will convert celcius to fahrenheit
        """
        fahrenheit_result = round((int(value) * F_DIVISION_C_MULT) + F_SUBSTRACTION_C_ADDITION, DECIMALS)
        return 'Fahrenheit: °' + str(fahrenheit_result)

    def fahrenheit_celcius(self, value):
        """ 
        fahrenheit to celcius
        
        This function will convert fahrenheit to celcius
        """
        celcius_result = round((int(value) - F_SUBSTRACTION_C_ADDITION) / F_DIVISION_C_MULT, DECIMALS)
        return 'Celcius: °' + str(celcius_result)
        
convert = Converter()


print(list(map(convert.celcius_fahrenheit, temperatures)))
print(list(map(convert.fahrenheit_celcius, temperatures)))
