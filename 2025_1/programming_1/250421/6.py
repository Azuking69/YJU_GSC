for value_1 in range(2):         # 外側のループ（value_1 = 0, 1）
    for value_2 in range(2):     # 中のループ（value_2 = 0, 1）
        for value_3 in range(2): # 内側のループ（value_3 = 0, 1）
            if value_3 == 1:     # 条件：value_2が1なら
                break            # value_3のループを中断
            
            #value_1 = 0の場合から順に数字が当てはまる
            print(f"{value_1} {value_2} {value_3}\t", end="") #横に出力を続ける

        print() #改行
    print()