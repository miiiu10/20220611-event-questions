def main():
    # 昇順にソートされた配列
    sorted_array = [1, 2, 3, 5, 12, 7890, 12345]
    # 探索対象の番号
    target_number = 7890
    # 探索実行
    target_index = serch_index(sorted_array, target_number)
    # 結果出力
    print(target_index)

def serch_index(sorted_array, target_number):

    # ここから記述

    index = list(range(len(sorted_array)))  # sorted_arrayに対応するインデックスを表す配列

    # 探索対象の配列のサイズが1になるまで繰り返す処理
    while(len(sorted_array) > 1):
        half_idx = len(sorted_array) // 2   # 配列の中間のインデックス
        
        if target_number == sorted_array[half_idx]:     #「配列の中間の値」と「探索対象の数値」が等しい時
            return index[half_idx]
        elif target_number < sorted_array[half_idx]:    #「配列の中間の値」<「探索対象の数値」の時、探索範囲を配列の中間よりも後とする
            sorted_array = sorted_array[:half_idx]
            index = index[:half_idx]
        else:                                           #「配列の中間の値」>「探索対象の数値」の時、探索範囲を配列の中間よりも前とする
            sorted_array = sorted_array[half_idx:]
            index = index[half_idx:]
    
    # 探索対象の配列のサイズが1のときの処理
    if len(sorted_array)==1 and sorted_array[0]==target_number:
        return index[0]

    # ここまで記述

    # 探索対象が存在しない場合、-1を返却
    return -1

if __name__ == '__main__':
    main()
