def main():
    #ランダムに並べられた重複のない整数の配列
    array = [5, 4, 6, 2, 1, 9, 8, 3, 7, 10]
    # ソート実行
    sortedArray = sort(array)
    # 結果出力
    [print(i) for i in sortedArray]

def sort(array):
    # 要素が一つの場合はソートの必要がないので、そのまま返却
    if len(array) == 1:
        return array
    
    # 配列の先頭を基準値とする
    pivot = array[0]

    # ここから記述

    forward_index = 0                   # 前から探索するためのインデックス
    backward_index = len(array) - 1     # 後ろから探索するためのインデックス
    while(forward_index<backward_index):
        if not(array[forward_index] >= pivot):      # 先頭から基準値以下の値を探索
            forward_index += 1
        elif not(array[backward_index] < pivot):    # 末端から基準値未満の値を探索
            backward_index -= 1
        else:
            # 入れ替え処理
            array[forward_index], array[backward_index] = array[backward_index], array[forward_index]

    under_pivot = array[:forward_index]     # 基準値未満のグループ
    over_pivot = array[forward_index:]      # 基準値以上のグループ
    
    #　先頭の値が最も小さい場合の処理
    if not under_pivot:
        return [array[0]] + sort(array[1:])

    return sort(under_pivot) + sort(over_pivot)

    # ここまで記述

if __name__ == '__main__':
    main()
