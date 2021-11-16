#Tämä on squidgame paska koodi
#Tämä squidgame on tehty lastenkoodilla eli ei mitään ihmeellistä nähtävää täällä.

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    GAME   =  '\033[35m'
    RED    =  '\033[31m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print("Tervetuloa, Squid" + bcolors.GAME + "Game" +  bcolors.ENDC)
#ja tämä tekee numero grifasta randomin ja waitin

import time
import random
#Arpoo numeron mitä käyttää printissä ynnämuissa väliltä 112-456
a = random.randint(112,456)

# Siis nyt en tiiä tää on turha mut en jaksa väsyneenä poistaa tätä kun toi rivi 19 voi hakea sen pelkällä (a) funktiolla riviltä 7
b = a

# Joku fakin spaghetti grifa koodi setti
#En tiiä miks grifasin tämmösen mut tein sen et toi 16 rivi hakee jos vastaat en
valitse = input("Oletko valmis pelaamaan? ")
if valitse == "en":
  print(bcolors.RED + "Väärä vastaus mee pois! Pelaaja:", b, bcolors.ENDC)
else: 
  nimi = input("Anna Nimesi: ")
  print(bcolors.OKGREEN + "Olet nyt pelissä! "  + bcolors.ENDC + nimi)
  print("Ladataan |", bcolors.WARNING + "13%" + bcolors.ENDC)
  #Hakee time.sleepin ylhäältä import time eli ihan grifa paste shiiis
  time.sleep(0.5)

  print("Ladataan |", bcolors.WARNING + "16%" + bcolors.ENDC)
  time.sleep(0.9)

  print("Ladataan |", bcolors.WARNING + "36%" + bcolors.ENDC)
  time.sleep(0.9)

  print("Ladataan |", bcolors.OKGREEN + "61%" + bcolors.ENDC)
  time.sleep(0.9)

  #"Lataa" ns sen spaghetti koodi pelin niin
  print("Ladataan |", bcolors.OKGREEN + "83%" + bcolors.ENDC)
  time.sleep(1.2)

  print("Ladataan |", bcolors.OKGREEN + "100%" + bcolors.ENDC)
  time.sleep(1.2)

  #Printtaa waitin jälkeen valmiin you fokin reetard
  print(bcolors.OKGREEN + "Valmis!" + bcolors.ENDC)

  time.sleep(1)
  #hakee pelaajasi uudestaan!
  print(f"Olet Pelaaja: {bcolors.GAME}{a} {bcolors.ENDC}")
  time.sleep(3)
 # valinta = [bcolors.OKGREEN + "Voitit!", bcolors.RED + "Hävisit!" + bcolors.ENDC]
#print(random.choice(valinta))

#hullu valinta kymysys jossa valitset oikealle vai vasemmalle
print('Pelataksesi peliä valitse joko "Vasen" tai "Oikea"')

pelivastaus = input("Vasen vai Oikea?: ")
if pelivastaus == "vasen":
  print(f"{bcolors.GAME}Menit vasemmalle {bcolors.ENDC}")
  time.sleep(2)
  print(f"{bcolors.OKGREEN}Voitit {bcolors.ENDC}")
else: 
  print(f"{bcolors.GAME}Menit oikealle{bcolors.ENDC}")
  time.sleep(2)
  print(f"{bcolors.RED}Lasi ei kestänyt, hävisit pelin :(")

#────────▓▓▓▓▓▓▓────────────▒▒▒▒▒▒
#──────▓▓▒▒▒▒▒▒▒▓▓────────▒▒░░░░░░▒▒
#────▓▓▒▒▒▒▒▒▒▒▒▒▒▓▓────▒▒░░░░░░░░░▒▒▒
#───▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒░░░░░░░░░░░░░░▒
#──▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░▒
#──▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░▒
#─▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░▒
#▓▓▒▒▒▒▒▒░░░░░░░░░░░▒▒░░▒▒▒▒▒▒▒▒▒▒▒░░░░░░▒
#▓▓▒▒▒▒▒▒▀▀▀▀▀███▄▄▒▒▒░░░▄▄▄██▀▀▀▀▀░░░░░░▒
#▓▓▒▒▒▒▒▒▒▄▀████▀███▄▒░▄████▀████▄░░░░░░░▒
#▓▓▒▒▒▒▒▒█──▀█████▀─▌▒░▐──▀█████▀─█░░░░░░▒
#▓▓▒▒▒▒▒▒▒▀▄▄▄▄▄▄▄▄▀▒▒░░▀▄▄▄▄▄▄▄▄▀░░░░░░░▒
#─▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░▒
#──▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░▒
#───▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▀▀▀░░░░░░░░░░░░░░▒
#────▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░▒▒
#─────▓▓▒▒▒▒▒▒▒▒▒▒▄▄▄▄▄▄▄▄▄░░░░░░░░▒▒
#──────▓▓▒▒▒▒▒▒▒▄▀▀▀▀▀▀▀▀▀▀▀▄░░░░░▒▒
#───────▓▓▒▒▒▒▒▀▒▒▒▒▒▒░░░░░░░▀░░░▒▒
#────────▓▓▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░▒▒
#──────────▓▓▒▒▒▒▒▒▒▒▒░░░░░░░░▒▒
#───────────▓▓▒▒▒▒▒▒▒▒░░░░░░░▒▒
#─────────────▓▓▒▒▒▒▒▒░░░░░▒▒
#───────────────▓▓▒▒▒▒░░░░▒▒
#────────────────▓▓▒▒▒░░░▒▒
#──────────────────▓▓▒░▒▒
#───────────────────▓▒░▒
#────────────────────▓▒
