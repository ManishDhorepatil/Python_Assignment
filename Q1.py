#solution

def convert_to_indian_currency(number):
    # Convert the number to a string for further conversion
    number_str = str(number)

    formatted_number = ""
    
    if len(number_str) > 3:
        formatted_number = number_str[-3:]
        number_str = number_str[:-3]
        
        while len(number_str) > 2:
            formatted_number = number_str[-2:] + "," + formatted_number
            number_str = number_str[:-2]
        
        if number_str:
            formatted_number = number_str + "," + formatted_number
    else:
        formatted_number = number_str
    
    return formatted_number

number = 504678
print(convert_to_indian_currency(number)) # the output is converted here.
