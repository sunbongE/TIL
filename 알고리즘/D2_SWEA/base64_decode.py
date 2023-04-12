decode = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "+",
    "/",
]

T = int(input())

for _ in range(T):
    st = input()
    result = ""
    for i in range(len(st)):
        bn = str(bin(decode.index(st[i]))[2:])
        while len(bn) < 6:
            bn = "0" + bn
        result += bn
    ans = ""
    for j in range(len(st) * 6 // 8):
        data = int(result[j * 8 : j * 8 + 8], 2)
        ans += chr(data)

    print(f"#{_+1} {ans}")
