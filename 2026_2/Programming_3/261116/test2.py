# Context Manager for the gsc.txt file

try:
    # f_hndler = open('gsc.txt', 'r', encoding='utf-8')
    with open('gsc.txt', 'r', encoding='utf-8') as f_hndler:
        for text in f_hndler:
            print(text)

    for text in f_hndler:
        print(text)

except Exception as e:
    print(e)

finally:
    f_hndler.close()