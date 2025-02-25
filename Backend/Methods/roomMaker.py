import random

def roomCollection(roomNumber, danger):
    roomPrompt = ""
    boss = False
    lighting = [
                "poorly lit",
                "pitch black",
                "dimly lit",
                "well lit",
        ]
    treasure = [
                "This room has no treasure",
                "This room has hidden minor treasure",
                "This room has hidden major treasure",
                "This room has a valuable special artifact or weapon hidden away",
                "This room is bristling with visible riches",
                "This room has no treasure",
                "This room has no treasure",
                "This room has no treasure",
                "This room has no treasure",
                "This room has no treasure",
                "This room has no treasure",
                "This room has no treasure",
                "This room has no treasure",
                "This room has no treasure",
                "This room has no treasure",
                "This room has no treasure",
                "This room has no treasure",
                "This room has no treasure",
                "This room has no treasure",
                "This room has no treasure",
        ]
    roomType = [
                "This room is a kitchen and",
                "This room is a bedroom and",
                "This room is a living space and",
                "This room is a library and",
                "This room is a armoury and",
                "This room is a surveillance room and",
                "This room is a lavatory and",
                "This room is a private zoo and",
                "This room is a play area and",
                "This room is a classroom and",
                "This room is a board room and",
                "This room is a great hall and",
                ]
    lowDanger = [
                " empty but for some items that show the rooms purpose",
                " empty but for some items that show the rooms purpose",
                " empty but for some items that show the rooms purpose",
                " empty but for some items that show the rooms purpose",
                " this room has objects, records or imagery that hint at the history of this adventure site",
                " this room has objects, records or imagery that hint at the history of this adventure site",
                " this room has objects, records or imagery that hint at the history of this adventure site",
                " this room contains a simple riddle or mechanism that offers a small reward when solved.",
                " this room contains A basic puzzle or device that affects the room in a minor way.",
                " this room contains A basic puzzle or device that affects the room in a minor way.",
                " this room contains A minor trap that causes inconvenience but no lasting harm.",
                " this room contains A group of small, mischievous beings that are not truly threatening.",
                " this room contains A helpful character offering advice or a minor boon.",
                " this room contains A non-critical character seeking assistance with a trivial problem.",
                " this room contains An environmental quirk or subtle magical or technological phenomenon that catches the eye.",
                " this room contains A lone, low-threat monster that can be easily overcome.",
                " this room contains An item with a minor drawback that is more a nuisance than a danger.",
                " this room contains A helpful, low-powered item that provides a small advantage.",
                " this room contains A helpful character offering advice or a minor boon.",
                " This room contains a foe although not overly powerful, the orchestrator of whatever is going on in this place."
        ]
    medDanger = [
                " empty but for some items that show the rooms purpose",
                " empty but for some items that show the rooms purpose",
                " empty but for some items that show the rooms purpose",
                " this room has objects, records or imagery that hint at the history of this adventure site",
                " this room has objects, records or imagery that hint at the history of this adventure site",
                " this room contains A trap with noticeable risks and potential moderate consequences.",
                " this room contains A trap with noticeable risks and potential moderate consequences.",
                " this room contains A mechanism or riddle with a twist that requires teamwork to solve.",
                " this room contains A mechanism or riddle with a twist that requires teamwork to solve.",
                " this room contains A handful of creatures that pose a tactical challenge.",
                " this room contains A handful of creatures that pose a tactical challenge.",
                " this room contains One or two standout foes with abilities that test skill.",
                " this room contains A character whose request for help carries immediate stakes.",
                " this room contains A helpful figure who offers enigmatic warnings or clues.",
                " this room contains A room where a trap and environmental feature create layered challenges.",
                " this room contains A room where a trap and environmental feature create layered challenges.",
                " this room contains An item with a stronger benefit but limited in use or duration.",
                " this room contains A puzzle that changes conditions or consequences based on player actions.",
                " this room contains An object or feature with a curse that imposes observable adverse effects.",
                " This room contains a foe somewhat powerful, the orchestrator of whatever is going on in this place."
        ]
    highDanger = [
                " empty but for some items that show the rooms purpose",
                " empty but for some items that show the rooms purpose",
                " this room has objects, records or imagery that hint at the history of this adventure site",
                " this room has objects, records or imagery that hint at the history of this adventure site",
                " this room contains A sophisticated or brutal trap where failure leads to severe consequences.",
                " this room contains A sophisticated or brutal trap where failure leads to severe consequences.",
                " this room contains A room populated by several dangerous creatures in a coordinated threat.",
                " this room contains A room populated by several dangerous creatures in a coordinated threat.",
                " this room contains An overwhelming number of small adversaries that can quickly overrun the unwary.",
                " this room contains An overwhelming number of small adversaries that can quickly overrun the unwary.",
                " this room contains One or two high-powered foes with significant abilities and tactics.",
                " this room contains A character in desperate need of rescue, with time-sensitive stakes.",
                " this room contains A complex mechanism where failure triggers dangerous outcomes.",
                " this room contains A complex mechanism where failure triggers dangerous outcomes.",
                " this room contains An intriguing environmental aspect that conceals a hidden threat.",
                " this room contains An intriguing environmental aspect that conceals a hidden threat.",
                " this room contains An object or effect that carries a dangerous curse with significant penalties.",
                " this room contains A powerful item that is either heavily guarded or comes with a perilous twist.",
                " this room contains A scenario combining elements (such as traps and monsters) into a multi-layered, high-risk encounter.",
                " this room contains This room contains a foe immensely powerful, the orchestrator of whatever is going on in this place.",
        ]
    for x in range(roomNumber):
        roomTypeRoll = random.randint(0,11)
        treasureRoll = random.randint(0,19)
        lightingRoll = random.randint(0,3)

        if x == roomNumber and boss == False:
            encounterRoll = 19
            boss = True
        else:
            encounterRoll = random.randint(0,19)

        if danger == 1:
            roomPrompt += f"This is room number {x}: {lighting[lightingRoll]} {roomType[roomTypeRoll]} {lowDanger[encounterRoll]} {treasure[treasureRoll]}"
        elif danger == 2:
            roomPrompt += f"This is room number {x}: {lighting[lightingRoll]} {roomType[roomTypeRoll]} {medDanger[encounterRoll]} {treasure[treasureRoll]}"
        elif danger == 3:
            roomPrompt += f"This is room number {x}: {lighting[lightingRoll]} {roomType[roomTypeRoll]} {highDanger[encounterRoll]} {treasure[treasureRoll]}"

        if encounterRoll == 19:
            boss = True

    return roomPrompt