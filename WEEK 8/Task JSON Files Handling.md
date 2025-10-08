<aside>
💪🏽 **Ejercicios**

1. Investigue cómo leer y escribir archivos `JSON` en Python [aquí](https://www.w3schools.com/python/python_json.asp).

Usando loads para crear un json a partir de un string

Usando dumps para crear un JSON string a partir de un objecto python

1. Cree un programa que permita agregar un Pokémon nuevo al archivo de la lección de JSON ([Archivos JSON](https://www.notion.so/Archivos-JSON-79f9758cb59d4452a9c8668efa25356c?pvs=21)).
    1. Debe leer el archivo para importar los Pokémones existentes.
    2. Luego debe pedir la información del Pokémon a agregar.
    3. Finalmente debe guardar el nuevo Pokémon en el archivo.
    
    ```python
    import json
    
    def read_json_file(path):
    	with open(path) as file:
    		string_content = file.read()
    		json_content = json.loads(string_content)
    		return json_content
    
    def write_file(path, content):
    	with open(path, 'w') as file:
    		file.write(content)
    
    def create_new_pokemon():
        new_pokemon = {}
        english_name = input("Enter Pokémon's English name: ")
        new_pokemon["name"] = {"english": english_name}
        types = input("Enter Pokémon type(s), separated by commas: ")
        new_pokemon["type"] = [t.strip() for t in types.split(",")]
    
        base_stats = {}
        base_stats["HP"] = int(input("Enter HP: "))
        base_stats["Attack"] = int(input("Enter Attack: "))
        base_stats["Defense"] = int(input("Enter Defense: "))
        base_stats["Sp. Attack"] = int(input("Enter Special Attack: "))
        base_stats["Sp. Defense"] = int(input("Enter Special Defense: "))
        base_stats["Speed"] = int(input("Enter Speed: "))
    
        new_pokemon["base"] = base_stats
    
        return new_pokemon
    
    if __name__ == '__main__':
        file_path = 'json.json'
    
        dict_of_pokemon = read_json_file(file_path)
    
        new_pokemon = create_new_pokemon()
    
        dict_of_pokemon.append(new_pokemon)
    
        json_string = json.dumps(dict_of_pokemon)
    
        write_file(file_path, json_string)
    ```
    
</aside>