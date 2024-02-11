import sqlite3

# sql_command = """CREATE TABLE gamesaves (
#     wave INTEGER PRIMARY KEY,
#     total_gold INTEGER,
#     health INTEGER);"""
# sql_command = """CREATE TABLE TowersSaved (
#     number_Targets INTEGER PRIMARY KEY,
#     damage INTEGER,
#     range INTEGER,
#     fire_rate INTEGER,
#     price INTEGER,
#     x_pos INTEGER,
#     y_pos INTEGER,
#     name STRING);"""
class Savegame():
    def __init__(self, wave, total_gold, health):
        self.wave = wave
        self.health = health
        self.total_gold = total_gold
        connection = sqlite3.connect("save.db")
        cursor = connection.cursor()
        sql_command = """CREATE TABLE gamesaves (
          wave INTEGER PRIMARY KEY,
          total_gold INTEGER,
          health INTEGER);"""
        #cursor.execute(sql_command)
        cursor.execute("DELETE FROM gamesaves")
        cursor.execute("INSERT INTO gamesaves(wave, total_gold, health) values (?, ?, ?)",(wave, total_gold, health))
        

        print("Wave: "+ str(wave) + " Health: "+str(health) + " Gold: " + str(total_gold))
        
        connection.commit()
        connection.close()
        #Loadsave()

def Savetowers(towerlist):
        connection = sqlite3.connect("save.db")
        cursor = connection.cursor()
        cursor.execute("DELETE FROM TowersSaved")
        for tower in towerlist:
              number_Targets = tower.max_targets
              damage = tower.damage
              range=tower.range
              fire_rate = tower.fire_rate
              price = tower.price
              x_pos = tower.x_pos
              y_pos = tower.y_pos
              cursor.execute("INSERT INTO TowersSaved(number_Targets, damage, range, fire_rate, price, x_pos, y_pos) values (?, ?, ?, ?, ?,?, ?)",(number_Targets, damage, range, fire_rate, price, x_pos, y_pos))


        

        connection.commit()
        connection.close()

def LoadTowers():
        connection = sqlite3.connect("save.db")
        cursor = connection.cursor()

        Towerlist = []

        for row in cursor.execute("SELECT * FROM TowersSaved"):
              Tower = []
              Tower.append(row)
              Towerlist.append(Tower)

        connection.commit()
        connection.close()
        return Towerlist
def Loadsave():
    
        connection = sqlite3.connect("save.db")
        cursor = connection.cursor()
        for row in cursor.execute("SELECT * FROM gamesaves"): 

            wave = row[0]
            total_gold = row[1]
            health = row[2]
            return row
            print("Wave: "+ str(wave) + " Health: "+str(health) + " Gold: " + str(total_gold))

        
        connection.commit()
        connection.close()
        


#cursor.execute(sql_command)


