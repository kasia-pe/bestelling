import mysql.connector
from mysql.connector import Error

hostname="localhost"
databasename="bestelling"
gebruiker="root"
wachtwoord=""

connection = mysql.connector.connect(host=hostname,
                                    database=databasename,
                                    user=gebruiker,
                                    password=wachtwoord)

def uit():
    sQuery = "SELECT * FROM product"
    cursor = connection.cursor()
    cursor.execute(sQuery)
    records=cursor.fetchall()
    for rij in records:
        print("Product:",rij[1]+", Prijs:",rij[2])

def toevoegen(aankoop):
    sQuery = "INSERT INTO bestelling VALUES(0,'"+aankoop+"')"
    cursor = connection.cursor()
    cursor.execute(sQuery)
    connection.commit()

def bestellingOphalen():
    sQuery = "SELECT * FROM bestelling"
    cursor = connection.cursor()
    cursor.execute(sQuery)
    records=cursor.fetchall()
    for rij in records:
        print("Uw bestelling:",rij[1])

def terug():
    terug = input("Wilt u terug naar menu? (j/n) ")
    if(terug == "j"):
        menu()
    else:
        print("Tot ziens!")

def menu():
    print('''Maak een keuze:
        Prijzen nakijken (1)
        Bestelling maken (2)
        Bestelling zien  (3)
        ''')
    keuze=input("Uw keuze: ")

    if (keuze == "1"):
        prijzen()
    elif (keuze == "2"):
        bestellingMaken()
    elif (keuze == "3"):
        geefBestelling()
    
def prijzen():
    uit()
    terug()

def bestellingMaken():
    print('''Maak een bestelling
    -boter
    -brood
    -kaas
    -ham''')
    aankoop=input("Wat wilt u kopen? ")
    toevoegen(aankoop)
    terug()

def geefBestelling():
    bestellingOphalen()
    terug()

menu()