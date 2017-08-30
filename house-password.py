'''
- länge =< 10
- gross geschrieben
- klein geschrieben
- enthält nummern
- keine sonderzeichen

'''

def checkio(data):
    lower = 0
    upper = 0
    digit = 0

    if len(data) < 10: # Check the length
        return False
    for c in data:
        if c.islower(): # Check lower case
            lower += 1
        elif c.isupper(): # Check upper case
            upper += 1
        elif c.isdigit(): # Check digit
            digit += 1
        try: # Check if it is ascii
            c.encode('ascii');
        except UnicodeEncodeError:
            return False

    if (lower >= 1 and upper >= 1 and digit >= 1): # test the condition
        return True
    else:
        return False

#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
