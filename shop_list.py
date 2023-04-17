import sqlite3

furniture = [    
    "chair",
    "table",
    "couch",
    "bed",
    "dresser",
    "bookshelf",
    "desk",
    "lamp",
    "rug",
    "ottoman",
    "stool",
    "bench",
    "cabinet",
    "nightstand",
    "futon",
    "recliner",
    "fireplace",
    "mirror",
    "clock",
    "vase",
    "sculpture",
    "sofa",
    "loveseat",
    "sectional",
    "armchair", 
    "rocking_chair",  
    "office_chair",  
    "lounge_chair",    
    "accent_chair",   
    "pouf",  
    "footstool",  
    "chaise",   
    "headboard",  
    "footboard",
    "trunk", 
    "wardrobe",  
    "armoire",  
    "credenza", 
    "buffet",   
    "sideboard", 
    "hutch", 
    "chest", 
    "drawer"
]



furniture = sorted(furniture)

connection = sqlite3.connect("furniture_list.db")
cursor = connection.cursor()

cursor.execute("create table furniture (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)")
for i in range(len(furniture)):
    cursor.execute("insert into furniture (name) values (?)",[furniture[i]])

connection.commit()
connection.close()