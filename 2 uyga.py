def sezar_shifrlash(son):

    raqamlar = '0123456789'

    shifrlangan_son = ''
    for raqam in str(son):
        index = raqamlar.index(raqam)
        yangi_index = (index + 7) % 10
        shifrlangan_son += raqamlar[yangi_index]

    return shifrlangan_son

input_1 = 1946
output_1 = sezar_shifrlash(input_1)
print(f"Input: {input_1} => Output: {output_1}")

input_2 = 10023
output_2 = sezar_shifrlash(input_2)
print(f"Input: {input_2} => Output: {output_2}")


