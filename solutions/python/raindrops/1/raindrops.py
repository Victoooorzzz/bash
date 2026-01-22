def convert(number):
    uwu = ""
 
    if number % 3 == 0:
        uwu += "Pling" 
        
    if number % 5 == 0:
        uwu += "Plang"
        
    if number % 7 == 0:
        uwu += "Plong"

    if uwu == "":
        return str(number) 
        
    return uwu