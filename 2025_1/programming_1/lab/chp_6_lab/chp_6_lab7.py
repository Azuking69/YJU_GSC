line = 9
for i in range(1, line + 1, 2): #（最初の数、最後の数、飛ばす数）
    print(" " * ((line-i)// 2) + (i * "*")) #空白と＊をそれぞれ作る
    
for i in range(line -2 , 0, -2 ): #（最初の真ん中の列を飛ばすためー２
    print(" " * ((line-i)// 2) + (i * "*")) #最後の列、飛ばす数）