import sha1
import sha256

while True:
    Str = input("Input text : ")
    print ("""
    1) SHA1
    256) SHA256
    """)
    num = int(input("SHA ? : "))

    Bt = bytes(Str, encoding="utf-8")
    if num == 1:
        print(sha1.hexdigest(Bt))

    if num == 256:
        print(sha256.hexdigest(Bt))

    else:
        print("Введите существующий алгоритм")

    print("ending...")