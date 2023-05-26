# Importering av bibliotekskategorier

import random as rand
import os

# Skapar listor 

passengers = [] #Listan där alla objekt lagras
positions = ["stående", "sittande"] #Listan för 2 val av postioner
position_countlist = [] #Listan för räkning av antal i olika positioner

# Definierar attribut och metoder för varje objekt under klassen Person
class Person():

    #Objektens attributer
    def __init__(self, sex, age, positions):

        self.sex = sex
        self.age = age
        self.positions = positions

    def __str__(self):
        return f'({self.sex}, {self.age}, {self.positions})'

# Definerar rensa skärmen
def clear_screen():
    os.system("cls || clear") # cls och clear kan användas for Windows och Linux

# Metod efter clear_screen som bekräftar ditt val.
def press_con():
    input(
                    """

                    Tryck på valfri knapp för att fortsätta...
                    
                    """)

    clear_screen()

# Tillägg av en ny person i bussen.
# Slumpat antal passagerare stiger på bussen. 
def add_pass(total_passengers): #total_passengers menas total antal av passegerare

    for i in range(total_passengers):
        if rand.random() >= 0.5: # Könet på personen slumpas 50%. Därefter slumpas ålder och position (sittande eller stående).
            
            position = rand.choice(positions) # Position slumpas
            age = rand.randint(0, 99) # Ålder slumpas
            male = Person("Man", age, position) 
            
            passengers.append(male) # Objektet lagras sedan i listan (passengers)
            position_countlist.append(position) #Samt postionen lagras i listan (position_countlist)
        else: #Kvinnligt kön
          
            position = rand.choice(positions)
            age = rand.randint(0, 99)
            female = Person("Kvinna", age, position)
            
            passengers.append(female)
            position_countlist.append(position)

# Definerar metod remove som avlägsnar en/flera person(er) från bussen slumpmässigt
# mha. for-loop. 
def remove(total_passengers):
    for i in range(total_passengers):
            passengers.pop(rand.randint(0, len(passengers)-1)) #.pop funktion avlägsnar värde och returnerar senaste värde

# Metod för att skriva ut alla passagerare på bussen.
def print_list():
    for i, person in enumerate (passengers): # enumerate hjälper oss att få en siffra på varje iteration
        print (i+1,person) #Skriver ut siffror framför passagerare, alltså, 1,2,3... 


# Returnerar summan av alla passagerares åldrar. 
def totalAge():
    return sum([person.age for person in passengers]) # sum för att addera alla objekts ålder i listan passengers

# Returnerar medelåldern på passagerarna. 
def avgAge():
    return round(sum([person.age for person in passengers])/len(passengers)) # Alla objekts ålder adderas och sen divideras med längden på listan.

# Metod för den äldsta personen på bussen
def max_age():
    old_pass = [] #Skapar tom lista
    oldest_person = max([person.age for person in passengers]) #Objektet med högst värde på sin attribute ålder.

    for person in passengers: #for-loop i listan (passenegers), 
        if person.age == oldest_person: #om ett objekt har attribute ålder likadant värde
            old_pass.append(person) #sparas i listan (old_pass)
    
    for i, person in enumerate(old_pass): #Samma procedure som print_list()
        print(f"{i+1}. {person}") 

# Metod för räkna antal passagerar i de två olika positioner.
# Använder loop och counter variabel.
def count_positions(words, word_to_count):
    count = 0
    for word in words:
        if word == word_to_count:
          # uppdaterar counter variabel
            count = count + 1
    return count

# Metod för att skriva ut en lista på alla passagerare inom ett visst åldersspann
def find_age(age1,age2):
    agelist = [] # Skapar tom lista där personer med åldern inom intervallet.
    for person in passengers:
        if person.age >= age1 and person.age <= age2: #Intervallet mellan de två ålder
            agelist.append(person) #Sparar i listan (agelist)
    
    print("")

    if len(agelist) == 0: #Om det inte finns några passagerare inom intervallet
        print(f"Det finns inga passagerare mellan {age1} år och {age2} år.")
    else:
        for i, person in enumerate(agelist): #Samma procedure som print_list()
            print(f"{i+1}. {person}")


# Metod för sortera bussen enligt ålder.
def sort_buss():
            passengers.sort(key=lambda x: x.age) #Sorterar efter ålder mha. lambda funktion
            clear_screen()
            return print("Bussen är nu sorterad efter åldern")



# Metod som petar en passagerare ut från bussen. Får samt en kommentar. 
def poke (poked):

    poke_func = passengers[poked] #Anropar poke funktionen

    #Uppdelning i olika årsintervaller enligt trafikverket
    if poke_func.age <=19:
        if poke_func.sex =="Male":
            print("Ehh... mannen!")
        else:
            print("Du ger dålig vibes!")

    elif poke_func.age <= 29:
        if poke_func.sex == "Male":
            print ("Du skojar?!")
        else:
            print ("Vem tror du är!?")
    
    elif poke_func.age <= 39:
        if poke_func.sex == "Male":
            print ("Jag har mina rättigheter!")
        else:
            print ("Jag vill reklamera biljetten!")

    elif poke_func.age <= 49:
        if poke_func.sex == "Male":
            print ("Du och jag kan nog lösa detta! Vänta! Kör inte!")
        else:
            print ("Jag vill prata med din chef! Vänta! Kör inte!")

    elif poke_func.age <= 59:
        if poke_func.sex == "Male":
            print ("Oförskämd!")
        else:
            print ("Nä, nu blir jag förbannad!")

    elif poke_func.age >=60:
        if poke_func.sex == "Male":
            print ("Vad är det som händer... sånt är livet!")
        else:
            print ("Nähä... nu då?")

#Huvudprogrammet
def run():

    menu_choice = ""

    clear_screen()

    while menu_choice != "q": #Loopen bryts om användaren väljer "q"

        print("""
                              ____  _    _  _____ _____ ______ _   _       
                             |  _ \| |  | |/ ____/ ____|  ____| \ | |
                             | |_) | |  | | (___| (___ | |__  |  \| |
                             |  _ <| |  | |\___ \\___  \|  __| | . ` |
                             | |_) | |__| |____) |___) | |____| |\  |
                             |____/ \____/|_____/_____/|______|_| \_|
        
        """)
        print(
        """
                                         --- MENY ---
                    Välkommen till buss-simulatorn. Välj ett av alternativen nedan:
            1. Plocka upp ny passagerare                        2. Låt passagerare gå av
            3. Skriv ut alla passagerare                        4. Beräkna sammanlagd ålder
            5. Beräkna medelåldern                              6. Hitta äldst person
            7. Sortera bussen                                   8. Hitta personer inom ett specifikt åldersspann
            9. Antal sittande och stående                       10. Peta på passagerare

            q. Avsluta
        ---------------------------------------------------------------------------------------
        """)
  
      
        menu_choice = input("Skriv ditt val här: ")

        if menu_choice == "1":
            total = rand.randint(0, 25) #Slumpmässigt total passagerare stiger på, max 25
            available = 25 - len(passengers) #Lediga platser på bussen

            if available > 0: 
                if available >= total: #Om antalet lediga platser är större än antalet som stiger på så får alla plats
                    total_onboard = total
                    clear_screen()
                    print(f"{total_onboard} ny(a) passagerare ombord.")
                    press_con()

                else:
                    total_onboard = available #Annars får endast vissa personer plats
                    clear_screen()
                    print(f"Det fanns {total} passagerare på busshålsplatsen men endast {total_onboard} kunde stiga på.")
                    press_con()
                add_pass(total_onboard) #Funktionen add_pass anropas sedan med antalet som får plats som argument
            else: #Om bussen är full får inga gå gå
                clear_screen()
                print("Bussen är för närvarande full.")
                press_con()

        elif menu_choice == "2":
            if len(passengers) >=1: #Slumpar fram hur många passagerare som går av
                total_offboard = rand.randint(0, len(passengers))
                remove(total_offboard) #Funktionen remove anropas med slumat antal som argument
                clear_screen()
                print(f"{total_offboard} passagerare steg av bussen.")
                press_con()
            else:
                clear_screen()
                print("Inga passagerare befinner sig på bussen.")
                press_con()

        elif menu_choice == "3":
            if len(passengers)>= 1:
                clear_screen() 
                print_list() #Anropar funktionen print_list
                press_con()
            else:
                clear_screen()
                print("Inga passagerare befinner sig på bussen.")
                press_con()

        elif menu_choice == "4":
            if len(passengers)>= 1:
                clear_screen() 
                print(f" Den sammanlagda åldern hos de {len(passengers)} passagerare är {totalAge()}.") 
                press_con()
                #Skriver ut den sammlagda åldern genom att anropa funktionen totalAge
            else:
                clear_screen()
                print("Inga passagerare befinner sig på bussen.")
                press_con()

        elif menu_choice == "5":
            if len(passengers)>= 1:
                clear_screen()
                print(f" Medelåldern hos de {len(passengers)} passagerare är {avgAge()}.")
                press_con()
                #Skriver ut den sammlagda åldern genom att anropa funktionen avgAge
            else:
                clear_screen()
                print("Inga passagerare befinner sig på bussen.")
                press_con()

        elif menu_choice == "6":
            if len(passengers)>= 1:
                clear_screen()
                max_age() #Anropas funktionen max_age
                press_con()
            else:
                clear_screen()
                print("Inga passagerare befinner sig på bussen.")
                press_con()

        elif menu_choice == "7":
            if len(passengers)>= 1:
                clear_screen()
                sort_buss() #Anropar funktionen sort_buss
                press_con()
            else:
                clear_screen()
                print("Inga passagerare befinner sig på bussen.")
                press_con()

        elif menu_choice == "8":
            if len(passengers)>= 1:
                clear_screen()

                while True:
                    age1 = input("Ange lägsta åldern på passagerare du vill hitta -> ")
                    if age1.isdigit(): #Kollar om inmatningen är rättlig, om den är rättlig går programmet vidare
                        break
                    else:
                        clear_screen()
                        print("Felaktig inmatning.")
                        press_con()

                while True:
                    age2 = input("Ange högsta åldern på passagerare du vill hitta -> ")
                    if age2.isdigit(): #Kollar om inmatningen är rättlig, om den är rättlig går programmet vidare
                        break    
                    else:
                        clear_screen()
                        print("Felaktig inmatning.")
                        press_con()

                clear_screen()
                find_age(int(age1), int(age2)) #Anropar funktionen find_age med två argument

                press_con()
            else:
                clear_screen()
                print("Inga passagerare befinner sig på bussen.")
                press_con()


        elif menu_choice == "9": #Ny funktion för antal i sittande och stående position. 
            if len(passengers)>= 1:
                clear_screen() 
                print(f'Sittande: {count_positions(position_countlist, "sittande")} passagerare')
                print(f'Stående: {count_positions(position_countlist, "stående")} passagerare')

                press_con()

            else:
                clear_screen()
                print("Inga passagerare befinner sig på bussen.")

                press_con()

        elif menu_choice == "10":
            if len(passengers)>= 1:
                clear_screen()

                while True:

                    clear_screen()

                    print_list() #Anropar funktionen print_list så att man kan se vilka passagerare man kan välja

                    poked_pass = input(
                    """

                    Välj en passagerare att peta på. -> """)


                    if poked_pass.isdigit(): #Kollar om sin inmatning är rättlig
                        if int(poked_pass) > 0: #Ser till att man inte väljer ett värde under noll
                            if int(poked_pass) <= len(passengers): #Ser till att man håller sig inom listans längd
                                clear_screen()
                                poke(int(poked_pass)-1) #Anropar funktionen peta med ett korrekligt argument

                                press_con()

                                break #Bryter loopen så att man kommer tillbaka till huvudmenyn
                            else:
                                clear_screen()
                                print("Felaktig inmatning.")
                                press_con()
                        else: 
                            clear_screen()
                            print("Felaktig inmatning.")
                            press_con()
                    else:
                        clear_screen()
                        print("Felaktig inmatning.")
                        press_con()
            else:
                clear_screen()
                print("Inga passagerare befinner sig på bussen.")
                press_con()
                
        elif menu_choice != "q":
            clear_screen()
            print("Felaktig inmatning.")
            press_con()

run() #Anropar run funktionen så att programmet kan starta
