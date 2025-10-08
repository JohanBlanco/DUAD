<aside>
💪🏽 **Ejercicios**

1. Cree un programa que me permita ingresar información de `n` cantidad de videojuegos y los guarde en un archivo `csv`.
    1. Debe incluir:
        1. Nombre
        2. Género
        3. Desarrollador
        4. Clasificación ESRB
    2. Ejemplo de archivo final:
        
        ```
        nombre,genero,desarrollador,clasificacion
        Grand Theft Auto IV,Accion,Rockstar Games,M
        The Elder Scrolls IV: Oblivion,RPG,Bethesda,M
        Tony Hawk's Pro Skater 2,Deportes,Activision,T
        ```
        
    
    ```python
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
            writer = csv.DictWriter(file, headers)
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
    ```
    
2. Lea sobre el resto de métodos del módulo `csv` [aqui](https://docs.python.org/es/3/library/csv.html) y cree una version alternativa del ejercicio de arriba que guarde el archivo separado por *tabulaciones* en vez de por *comas*.
    1. Ejemplo de archivo final:
3. 
    
    ```
    nombre	genero	desarrollador	clasificacion
    Grand Theft Auto IV	Accion	Rockstar Games	M
    The Elder Scrolls IV: Oblivion	RPG	Bethesda	M
    Tony Hawk's Pro Skater 2	Deportes	Activision	T
    ```
    

```python
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
```

</aside>