'''
- länge =< 10
- gross geschrieben =< 1
- keine sonderzeichen
'''

def checkio(data):
    lower = 0
    upper = 0
    spezial = 0
    if len(data) < 10:
        return False
    for c in data:
        if c.islower():
            lower += 1
        elif c.isupper():
            upper += 1
        try:
            c.encode('ascii');
        except UnicodeEncodeError:
            print("False")
        else:
            print("True")

    print(lower + upper + spezial)

    #replace this for solution
    return True or False

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
