lang = "nl"
state = "nl"

translation = {
    "nl": {
        "Esc": "Esc",
        "A or arrow left": "A of pijl links",
        "D or arrow right": "D of pijl rechts",
        "W or arrow up": "W of pijl boven",
        "S or arrow down": "S of pijl beneden",
        "Space": "Spatiebalk",
        "Q": "Q",
        "Left Ctrl": "Ctrl links",
        "Return": "Enter",
        "Delete": "Delete",
        "Shift + F1-7": "Shift + F1-7",
        "L": "L",
        "Escape game": "Verlaat spel",
        "Move left": "Ga naar links",
        "Move right": "Ga naar rechts",
        "Move up": "Ga naar boven",
        "Move down": "Ga naar beneden",
        "Select and open store": "Selecteer en open winkel",
        "Close store": "Sluit winkel",
        "Show available shortcuts": "Bekijk beschikbare sneltoetsen",
        "Select above": "Selecteer hierboven",
        "Select below": "Selecteer hieronder",
        "Purchase and place building": "Koop en plaats gebouw",
        "Delete Building": "Verwijder gebouw",
        "Shortcut for placing buildings": "Snel gebouw plaatsen",
        "Enter dark or light mode": "Verander van kleuren modus",
        "Production": "Productie",
        "Money": "Geld",
        "People": "Mensen",
        "Press ctrl for all shortcuts": "Ctrl voor alle sneltoetsen",
        "Limit workers": "Max. werkers",
        "Close popup": "Sluit pop-up",
    },
}


def get(string):
    if lang == "en":
        return string
    else:
        return translation[lang][string]
