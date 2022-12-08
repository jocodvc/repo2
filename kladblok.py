CONSOLE_PRIJS = 55
PC_PRIJS = 45
MEMBER_KORTING = 15

platform = input('Ben je pc of console gamer?')

if platform == 'console':
    prijs = CONSOLE_PRIJS
    if input('Bent u member?') == 'ja':
        prijs -= MEMBER_KORTING
else:
    prijs = PC_PRIJS

print(f'U bent {platform} gamer , dan kost de game: {prijs} Euro')