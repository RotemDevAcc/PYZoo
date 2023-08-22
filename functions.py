import os
import xml.etree.ElementTree as ET

filename = "animals.xml"

def ClearConsole():
    os.system("cls" if os.name == "nt" else "clear")

def SearchKeyByName(name,table):
    for value in table:
        if(name == value["name"]):
            return value
        
    return None

def Input():
    sendinput = input("Choose Your Action: ")

    if(sendinput == None or sendinput == ""):
        print("\033[93mNo Action Chosen.\033[0m")
        return None

    if(sendinput.strip().isdigit()): return sendinput
    else: 
        print("\033[93mYou Have To Choose A Number.\033[0m")
        return None
    
def ListAnimals(table):
    if len(table) <= 0:
        print("\033[93mNo Animals Found\033[0m")
        return
    print("--- Listing Animals ---")
    for animal in table:
        print(f"Name: {animal['name']}, Age: {animal['age']} Years Old, {animal['nickname']}\n")
        
def SearchAnimal(table):
    animalname = input("Enter Animal Name [Example: Shark]: ")
    animal = SearchKeyByName(animalname,table)
    if(animal == None):
        print(f"Animal {animalname} Not Found")

    print(f"Name: {animal['name']}, Age: {animal['age']}, Nickname: {animal['nickname']}")

def AddAnimal(table):
    animalname = input("Enter Animal Name [Example: Shark]: ")
    animalage = input("Enter Animal Age [Example: 25]: ")
    if(not animalage.strip().isdigit()):
        print("\033[93mAnimal Age must be a Number\033[0m")
        return
    
    animalnickname = input("Enter Animal Nickname [Example: Megaladon]: ")


    if(animalname and animalage and animalnickname):

        if(SearchKeyByName(animalname,table)):
            print(f"\033[93mAnimal Name: {animalname} Is Already Used\033[0m")
            return
        
        table.append({"name" : animalname, "age" : animalage, "nickname": animalnickname})
        SaveAnimalsToXML(table)
        print(f"Added Animal Was Added, Name: {animalname}, Age: {animalage}, Nickname: {animalnickname}\n")
    else:
        print(f"Error: Not Enough Arguments Wanted 3 Got Less")

def DeleteAnimal(table):
    animalname = input("Enter Animal Name [Example: Shark]: ")
    if(not animalname): return

    value = SearchKeyByName(animalname,table)
    if(value == None):
        return print("Animal Not Found")
    
    table.remove(value)
    SaveAnimalsToXML(table)
            

def SaveAnimalsToXML(table):
    root = ET.Element("zoo")
    for animal in table:
        animal_element = ET.Element("animal")
        name_element = ET.Element("name")
        name_element.text = animal["name"]
        animal_element.append(name_element)
        age_element = ET.Element("age")
        age_element.text = animal["age"]
        animal_element.append(age_element)
        nickname_element = ET.Element("nickname")
        nickname_element.text = animal["nickname"]
        animal_element.append(nickname_element)
        root.append(animal_element)

    tree = ET.ElementTree(root)
    tree.write(filename)

    print(f'table saved to {filename}')

def LoadAnimalsFromXML():
    table = []
    table.clear()
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        for animal_element in root.findall("animal"):
            animal = {
                "name": animal_element.find("name").text,
                "age": animal_element.find("age").text,
                "nickname": animal_element.find("nickname").text,
            }
            table.append(animal)
        
        print(f'table loaded from {filename}')
        return table
    except FileNotFoundError:
        print(f'File not found: {filename}')
        return []
    except Exception as e:
        print(f'An error occurred while loading data: {str(e)}')
        return []