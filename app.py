from enum import Enum
from functions import *


# הגדרת מערך
Animals = []

# בולן שאחראי על להריץ את כל התהליך או לסיים אותו
Running = False
# class syntax
class Actions(Enum):
    ADD = 1
    DELETE = 2
    UPDATE = 3
    SEARCH = 4
    LIST = 5
    LISTACTIONS = 6
    CLEAR = 7
    STOP = 8



# מתחיל את התהליך
def StartItUp():
    # משתמש בבולן שלנו מלמעלה
    global Running

    # מגדיר את הערך של הבולן להיות ההפך ממה שהוא כרגע
    Running = not Running

    # עוצרים false אם הבולן שווה ל
    if(not Running):
        return
    
    # מדפיס את כל הפעולות האפשריות
    DrawActions()
    # True שווה ל RUNNING כל עוד
    while (Running):
        # מבקש פעולה דרך המקלדת
        action = Input()
        # אם אין מתחילים מחדש כדי להימנע מתקלות
        if(action == None):
            continue
        # ENUM אם יש בודק אותם דרך ה 
        action = Actions(int(action))
        if action == Actions.ADD:
            AddAnimal(Animals)

        if action == Actions.DELETE:
            DeleteAnimal(Animals)

        if action == Actions.UPDATE:
            UpdateAnimal(Animals)

        if action == Actions.SEARCH:
            SearchAnimal(Animals)

        if action == Actions.LIST:
            ListAnimals(Animals)

        if action == Actions.LISTACTIONS:
            DrawActions()

        if action == Actions.CLEAR:
            ClearConsole()

        if action == Actions.STOP:
            print("\033[91mKilling Program\033[0m")
            StartItUp()


# מדפיס את כל האפשרויות
def DrawActions():
    # ומדפיס אותם בצבע ורוד Enums עובר על כל ה 
    for action in Actions:
        print(f"\033[95m{action.name} - {action.value}\033[0m")

# כשהתוכנה עולה
if __name__ == "__main__":
    # טוען את החיות מהקובץ
    Animals = LoadAnimalsFromXML()
    # מפעיל את התהליך
    StartItUp()