for num in range(1, 101):
    string = ''

    # ここから記述

    if num % 3 == 0:    # 3の倍数の時
        string += 'Fizz'
    if num % 5 == 0:    # 5の倍数の時
        string += 'Buzz'
    if not string:      # 3の倍数でも5の倍数でもない時
        string += str(num)

    # ここまで記述

    print(string)
