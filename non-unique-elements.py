#Your optional code here
#You can import some modules or create additional functions
import timeit

def checkio(data):
    start = timeit.default_timer()
    data2 = []
    for x in data:
        if data.count(x) > 1:
            data2.append(x)
    data = data2
    stop = timeit.default_timer()
    print(stop - start)
    return data


#Some hints
#You can use list.count(element) method for counting.
#Create new list with non-unique elements
#Loop over original list


if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
    assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
    assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
