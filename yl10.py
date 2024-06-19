name = input("Sisesta oma nimi: ")
print("Tere", name)
location = input("Elukoht: ")
if  "saaremaa" in location.lower():
    print("See on hea koht kus elada! Oled vähemalt targem kui hiidlane ;)")
if  "hiiumaa" in location.lower():
    print("Mingi tross oled v?")
age = input("Vanus: ")
age = int(age)
if age < 18:
    print("Sa ei tohi sõita")
elif age == 18:
    print("Palju õnne täiskasvanuks saamise eest!")
else:
    print("Appi")
