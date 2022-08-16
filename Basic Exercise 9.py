#Basic Exercise 9

number = 13231

num = str(number)
reverse_list = list(reversed(num))
reverse_str = "".join(reverse_list)
reverse_num = int(reverse_str)

if number == reverse_num:
    print("Yes. The number", number, "is a palindrome.")
else:
    print("No. The number", number, "is not a palindrome.")

