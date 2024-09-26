
def lab3Question1(number, cutoff):
    # Take in two arguments - a number and a 'cutoff' (another number)
    # Return True if the number is less than the cutoff, False otherwise
    # Also, print a statement of "[Number] is less than [cutoff]" or "[Number] is not less than [cutoff]"
    # Where the [Number] and [cutoff] are the actual numbers passed in

    #number comparison
    if number < cutoff:
        print(str(number) + ' is less than ' + str(cutoff))
        return True
    else:
        print(str(number) + ' is not less than ' + str(cutoff))
        return False

#print(lab3Question1(10, 100))
#print(lab3Question1(100, 100))
#print(lab3Question1(100, 10))

def lab3Question2(decimal_number):
    # Take in an argument of a float (decimal) number.
    # Return "zero" if the number is 0, "positive" if the number is positive, and "negative" if the number is negative
    # Return "invalid" if the input is not a float
    #if not isinstance(decimal_number, float):
    try:
        decimal_number != float
    except:
        return 'invalid'
    

    if decimal_number == 0:
        return 'zero'
    elif decimal_number > 0:
        return 'positive'
    elif decimal_number < 0:
        return 'negative'
    
    
    
#print(lab3Question2(5.0))
#print(lab3Question2(10))
#print(lab3Question2(-10.1))

def lab3Question3(year):
    # Take in a number that represents a year
    # Return "21st century" if the year is between 2001 and 2100,
    # "20th century" if the year is between 1901 and 2000,
    # "19th century" if the year is between 1801 and 1900, 
    # "ancient" if the year is older
    # "invalid" if the input is not an acceptable year number. 
    
    try:
        year != int(year)
    except:
        return 'invalid'
       
    if year > 2001 and year < 2100:
        return "21st century"
    
    if year > 1901 and year < 2000:
        return "20th century"
    
    if year > 1801 and year < 1900:
        return "19th century"
    
    if year < 1800:
        return "ancient"
    
print(lab3Question3('neer'))
print(lab3Question3(10))
#print(lab3Question3(2050))
#print(lab3Question3(1950))
#print(lab3Question3(1850))



def lab3Question4(number_1, number_2, number_3):
    # Take in three numbers as arguments
    # Return the largest of the three numbers
    # Return None if the inputs are not 3 numbers

    #check for numeric number input
    if not isinstance(number_1, int):
            return None
    elif not isinstance(number_2, int):
         return None
    elif not isinstance(number_3, int):
        return None
    
    #try:
    #    number_1 = int(number_1)
    #    number_2 = int(number_2) 
    #    number_3 = int(number_3) 
    #except ValueError:
        return None
    
    
    largest = max(number_1, number_2, number_3)
    return (largest)

print(lab3Question4(2050, 20161, 201010))
print(lab3Question4(2050, 20161, 'beer'))


def lab3Question5(temperature, scale_used):
    # Take in a temperature and the scale that the temperature is in - either "C" for Celsius or "F" for Fahrenheit (capitalized)
    # Return "Liquid" if water is in liquid state at that temperature
    # Return "Solid" if water is in solid state at that temperature
    # Return "Gas" if water is in gas state at that temperature
    # Return "Invalid" if the temperature or scale are invalid
    
    try:
        scale_used != 'C' or 'F'
        temperature == int(temperature)
    except ValueError:
        return 'Invalid'
    
    if scale_used == 'F':
        temperature = fahrenheit_to_celsius(temperature)
        

    if temperature >= 0 and temperature <= 100:
        return 'Liquid'
    if temperature < 0:
        return 'Solid'
    if temperature > 100:
        return 'Gas'




def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return round(celsius, 3)


#print(lab3Question5(2050, 'C'))
#print(lab3Question5(86, 'F'))
#print(lab3Question5(-22, 'C'))
#print(lab3Question5('beer', 'E'))

