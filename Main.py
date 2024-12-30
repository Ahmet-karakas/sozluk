kelimeler = {
    "piton" : "zehirsiz bir yılan türü",
    "laboratuvar" : "deney yapılan yer",
    "ahmet" : "övülmüş övülmeye layık"
}

while True:
    kelime = input("bir kelime girin")
    if kelime in list(kelimeler.keys()):
        print(kelimeler[kelime])
    else:
        anlami = input("anlamını girin")
        kelimeler[kelime] = anlami
        print(kelime, " sözlüğe eklendi")  


