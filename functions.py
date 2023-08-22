import os
import xml.etree.ElementTree as ET

# שם הקובץ
filename = "animals.xml"

# מנקה את הקונסול
def ClearConsole():
    os.system("cls" if os.name == "nt" else "clear")

# מחפש משהו במערך על פי שם
def SearchKeyByName(name,table):
    for value in table:
        if(name == value["name"]):
            return value
        
    return None

# מבקש טקסט
def Input():
    sendinput = input("Choose Your Action: ")

    # NONE אם לא צויין שום דבר מחזירים 
    if(sendinput == None or sendinput == ""):
        print("\033[93mNo Action Chosen.\033[0m")
        return None

    # אם הפעולה שנבחרה יכולה להיות מספר שולחים אותה
    if(sendinput.strip().isdigit()): return sendinput
    else: 
        # אם לא אז כותבים בצבע צהוב שחייב להשתמש במספרים
        print("\033[93mYou Have To Choose A Number.\033[0m")
        return None
    
# מדפיס את כל החיות עם הפרטים שלהם
def ListAnimals(table):
    # אם אין חיות לא להדפיס
    if len(table) <= 0:
        print("\033[93mNo Animals Found\033[0m")
        return
    print("--- Listing Animals ---")
    for animal in table:
        print(f"Name: {animal['name']}, Age: {animal['age']} Years Old, {animal['nickname']}\n")
        
# מחפש חיות על פי המערך הקיים
def SearchAnimal(table):
    animalname = input("Enter Animal Name [Example: Shark]: ")
    # מחפש חיה על פי השם שהוגדר למעלה
    animal = SearchKeyByName(animalname,table)

    # אם החיה לא נמצאה
    if(animal == None):
        print(f"Animal {animalname} Not Found")

    # מדפיסים את החיה שחיפשנו עם כל הפרטים שלה
    print(f"Name: {animal['name']}, Age: {animal['age']}, Nickname: {animal['nickname']}")

# הוספת חיות
def AddAnimal(table):
    animalname = input("Enter Animal Name [Example: Shark]: ")
    animalage = input("Enter Animal Age [Example: 25]: ")

    # אם הגיל של החיה שהוגדר אינו מספר
    if(not animalage.strip().isdigit()):
        print("\033[93mAnimal Age must be a Number\033[0m")
        return
    
    animalnickname = input("Enter Animal Nickname [Example: Megaladon]: ")

    # אם צויין שם, גיל ושם כינוי
    if(animalname and animalage and animalnickname):

        # אם השם כבר בשימוש לעצור כדי למנוע שמות כפולים
        if(SearchKeyByName(animalname,table)):
            print(f"\033[93mAnimal Name: {animalname} Is Already Used\033[0m")
            return
        
        # מוסיפים למערך
        table.append({"name" : animalname, "age" : animalage, "nickname": animalnickname})
        # מעדכנים את הקובץ
        SaveAnimalsToXML(table)
        # מדפיסים איזה חיה נוספה ואת הפרטים שלי
        print(f"Added Animal Was Added, Name: {animalname}, Age: {animalage}, Nickname: {animalnickname}\n")
    else:
        # אם לא
        print(f"Error: Not Enough Arguments Wanted 3 Got Less")

# מחיקת חיות
def DeleteAnimal(table):
    animalname = input("Enter Animal Name [Example: Shark]: ")
    # אם לא צויין שם חיה
    if(not animalname): return


    animal = SearchKeyByName(animalname,table)
    # אם החיה לא נמצאה
    if(animal == None):
        return print("Animal Not Found")
    
    # מוחקים מהמערך
    table.remove(animal)
    # שומרים לקובץ
    SaveAnimalsToXML(table)
            

# מעדכן חיה קיימת
def UpdateAnimal(table):
    animalname = input("Enter Animal Name to Update: ")
    animal = SearchKeyByName(animalname, table)
    # אם לא נמצאה חיה
    if animal == None:
        print(f"\033[93mAnimal {animalname} Not Found\033[0m")
        return

    # מדפיס את שם החיה שכרגע אנו עוסקים בה
    print(f"\033[92mCurrent Animal Data: Name: {animal['name']}, Age: {animal['age']}, Nickname: {animal['nickname']}\033[0m")

    new_name = input("Enter New Animal Name [Leave Empty To Keep Current]: ")
    new_age = input("Enter New Animal Age [Leave Empty To Keep Current]: ")
    new_nickname = input("Enter New Animal Nickname [Leave Empty To Keep Current]: ")

    # אם צוין שם מחליפים את הנוכחי בחדש
    if new_name:
        animal['name'] = new_name
    # אם צוין גיל מחליפים את הנוכחי בחדש
    if new_age and new_age.isdigit():
        animal['age'] = new_age
    # אם צוין שם כינוי מחליפים את הנוכחי בחדש
    if new_nickname:
        animal['nickname'] = new_nickname

    # שומרים לקובץ
    SaveAnimalsToXML(table)
    # מעדכנים שהפעולה בוצעה בהצלחה
    print(f"\033[92mAnimal {animalname} Updated Successfully\033[0m")


# שומר את המערך לקובץ
def SaveAnimalsToXML(table):
    root = ET.Element("zoo")
    # צריך XML עובר על המערך ומסר אותו לפי מה ש
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


# טוען את החיות מהקובץ

def LoadAnimalsFromXML():
    table = []
    table.clear()
    # מנסה לגשת לקובץ
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
    
    # אם הקובץ לא נמצא
    except FileNotFoundError:
        print(f'File not found: {filename}')
        return []
    
    # אם לא עבד מכל סיבה אחרת
    except Exception as e:
        print(f'An error occurred while loading data: {str(e)}')
        return []