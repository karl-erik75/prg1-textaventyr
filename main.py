# Här skriver du ditt textäventyr


def spelare():
    player = input("what is your namn? ")
    age = int(input("what is yo ålder? "))

    if age > 16:
        input("gogo gaga du har fel!!!!")
        spelare()

    elif age > 130:
        input("du fick en hjärt attack!")
        spelare()


spelare()