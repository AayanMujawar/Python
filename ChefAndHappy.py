t = int(input())

while t > 0:
    s = input()

    FLAG = 0
    vowels = "aeiou"

    for i in range(len(s) - 2):

        if (s[i].lower() in vowels and
            s[i + 1].lower() in vowels and
            s[i + 2].lower() in vowels):

            FLAG = 1
            break

    if FLAG:
        print("HAPPY")
    else:
        print("SAD")

    t -= 1