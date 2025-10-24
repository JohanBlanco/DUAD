# 2. Lea sobre el resto de métodos del módulo `csv` [aqui](https://docs.python.org/es/3/library/csv.html) y cree una version alternativa del ejercicio de arriba que guarde el archivo separado por *tabulaciones* en vez de por *comas*.
#     1. Ejemplo de archivo final:
# 3. 
    
#     ```
#     nombre	genero	desarrollador	clasificacion
#     Grand Theft Auto IV	Accion	Rockstar Games	M
#     The Elder Scrolls IV: Oblivion	RPG	Bethesda	M
#     Tony Hawk's Pro Skater 2	Deportes	Activision	T
#     ```
    

import csv

def get_game_info():
    game = {}
    game["title"] = input("Enter game title: ")
    game["genre"] = input("Enter game genre: ")
    game["publisher"] = input("Enter game publisher: ")
    game["rating"] = input("Enter game rating (E, T, M, etc.): ")
    return game

def write_csv_file(file_path, data, headers):
    with open(file_path, 'w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, headers, delimiter="\t")
        writer.writeheader()
        writer.writerows(data)

if __name__ == '__main__':
    games = []
    
    while True:
        game = get_game_info()
        games.append(game)

        another = input("Do you want to add another game? (y/n): ").lower()
        if another != 'y':
            break

    if games:
        write_csv_file('games.csv', games, games[0].keys())
        print("Games saved successfully to 'games.csv'")
    else:
        print("No games to save.")
