# commentaar
# start met een hekje
########################################################################
# datatypes
# string = woord of zin
########################################################################
woord = 'hallo'  # het mag ook met dubbele komma's
woord = "hallo"
# met drie quotes krijg je een multiline string
lange_zin = '''dit is een erg lange zin,
die verdeeld is over meerdere regels.'''

# int = geheel getal
x = 6
# float = kommagetal (let op punt ipv komma
y = 6.5

##########################################################################
# built in functies bif's (ongeveer 70 in Python)
##########################################################################
# input = stel een vraag en sla het antwoord op. Geeft altijd een string terug.
antwoord = input('Hoe heet je?')

# print = stuurt een string naar de commandline
print('hallo', antwoord)  # of
print('hallo ' + antwoord)  # of
print(f'hallo {antwoord}, leuk kennis te maken!')


# typecasting
# int() = zet om naar naar int
getal = int('6')
# float() = zet string om naar float (mits mogelijk)
antwoord = '17.2'
getal = float(antwoord)

# via de bif input kun je een vraag stellen aan een gebruiker
antwoord = input('Hoe heet je?')




