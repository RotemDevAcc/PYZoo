from enum import Enum
from functions import *


Animals = []
Running = False
# class syntax
class Actions(Enum):
    ADD = 1
    DELETE = 2
    SEARCH = 3
    LIST = 4
    LISTACTIONS = 5
    CLEAR = 6
    STOP = 7




def StartItUp():
    global Running
    Running = not Running

    if(not Running):
        return
    DrawActions()
    while (Running):
        action = Input()
        if(action == None):
            continue
        action = Actions(int(action))
        if action == Actions.ADD:
            AddAnimal(Animals)

        if action == Actions.DELETE:
            DeleteAnimal(Animals)

        if action == Actions.SEARCH:
            SearchAnimal(Animals)

        if action == Actions.LIST:
            ListAnimals(Animals)

        if action == Actions.LISTACTIONS:
            DrawActions()

        if action == Actions.CLEAR:
            ClearConsole()

        if action == Actions.STOP:
            StartItUp()


def DrawActions():
    for action in Actions:
        print(f"{action.name} - {action.value}")

if __name__ == "__main__":
    Animals = LoadAnimalsFromXML()
    StartItUp()