def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """
    # your code here
    return 0

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    print('"Run" is good. How is "Check"?')


'''
There are four substring missions that were born all in one day and you shouldn’t be needed more than one day to solve them. All of those mission can be simply solved by brute force, but is it always the best way to go? (you might not have access to all of those missions yet, but they are going to be available with more opened islands on the map).
This mission is the first one of the series. Here you should find the length of the longest substring that consists of the same letter. For example, line "aaabbcaaaa" contains four substrings with the same letters "aaa", "bb","c" and "aaaa". The last substring is the longest one which makes it an answer.
Input: String.
Output: Int.

find a length the longest substring that consists of the same char. The discussion

checkio('sdsffffse') == 4
checkio('ddvvrwwwrggg') == 3
1
2
find the longest substring without repeating chars. The discussion

checkio('aaaaa') == 'a'
checkio('abdjwawk') == 'abdjw'
1
2
find a length the longest substring that repeats more than once. The discussion

checkio('aaaa') == 2
checkio('abc') == 0
checkio('aghtfghkofgh') == 3 # fgh
1
2
3
find first the longest repeating substring The discussion

checkio('aaaaa') == 'aaaaa'
checkio('aabbff') == 'aa'
checkio('aababcc') == 'abab'
checkio('abcabcabab') == 'abcabc'
'''