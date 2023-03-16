def smil():
    input_test = list(map(str, input().split()))
    smile_list = [":)", ":-)", ";)", ";-)"]

    for i, c in enumerate(input_test):
        if i != len(input_test)-1:
            if c + input_test[i+1] in smile_list:
                print(i)
            if i != len(input_test)-2:
                if c + input_test[i+1] + input_test[i+2] in smile_list:
                    print(i)
        else:
            break

smil()