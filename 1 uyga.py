def rangli_harflar(text):
    qizil = "\033[91m"
    sariq = "\033[93m"
    yashil = "\033[92m"
    a = "\033[0m"
    natija = ""

    for harf in text:
        if harf in "AaBbCcDdEeFfGgHh":
            natija += qizil + harf + a
        elif harf in "IiJjKkLlMmNnOoPp":
            natija += sariq + harf + a
        elif harf in "QqRrSsTtUuVvWwXxYyZz":
            natija += yashil + harf + a
        else:
            natija += harf

    return natija


text = "AaBbCcDdEeFfGgHh IiJjKkLlMmNnOoPp QqRrSsTtUuVvWwXxYyZz"
print(rangli_harflar(text))
