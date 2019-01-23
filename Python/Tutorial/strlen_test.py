with open('./strlen_test.txt', 'rb') as f:
    a = f.read()[:30]
    a = b"\x0098"
    print(a)
    print(a.decode())
    # a = str(a)
    # print(a.decode())

