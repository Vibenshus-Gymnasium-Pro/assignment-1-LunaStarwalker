roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
         'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}


s = str(input('Input a roman number: '))
slc = [x for x in s]
print(slc)

for i, x in enumerate(slc):
    try: y = slc[i+1]
    except: break
    else:
        if roman[x] < roman[y]:
            slc[i] = x+y
            del slc[i+1]

res = 0
for x in slc:
    res += roman[x]

return res