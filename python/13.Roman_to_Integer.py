def roman_to_int(s: str) -> int:
    roman = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000,
    }

    length = len(s)

    result = 0

    for i in range(length):
        ''' 
        if current roman letter value less than next roman letter
        than subtract from result
        else add in result
        current roman letter value -> roman[s[i]]
        next roman letter value -> roman[s[i + 1]]

        i < length -1 - > checking if loop reached its last iteration
        '''
        if i < length - 1 and roman[s[i]] < roman[s[i + 1]]:
                result -= roman[s[i]]
        else:
            result += roman[s[i]]
    
    return result

s = "MCMXCIV"
# s = "LVIII"
# s = "III"

print(roman_to_int(s))
