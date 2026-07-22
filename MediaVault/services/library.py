import json

FILE_PATH = "data/library.json"


# carrega o JSON em modo leitura "r - READ" usando UTF-8
# loads the JSON file in read mode "r - READ" using UTF-8
def load_items():
    try:
        with open(FILE_PATH, "r", encoding="utf-8") as file:
            return json.load(file)

    # se o arquivo não existir, retorna uma lista vazia
    # if the file does not exist, returns an empty list
    except FileNotFoundError:
        return []


# escreve os dados no arquivo JSON
# writes the data to the JSON file
def save_items(items):
    with open(FILE_PATH, "w", encoding="utf-8") as file:
        # usa indent apenas para deixar o JSON mais organizado
        # uses indent only to make the JSON file more readable
        json.dump(items, file, ensure_ascii=False, indent=4)


# cria a estrutura de dados de um novo item
# creates the data structure for a new item
def add_item(items, title, category, status, rating):
    item = {
        "title": title,
        "category": category,
        "status": status,
        "rating": rating
    }

    # adiciona o item à lista
    # adds the item to the list
    items.append(item)


# lista todos os itens registrados
# lists all registered items
def list_items(items):
    if not items:
        print("\nNo items registered here...")
        return

    for index, item in enumerate(items, start=1):
        print(f"\nItem {index}: {item['title']}")
        print(f"Category: {item['category']}")
        print(f"Status: {item['status']}")
        print(f"Rating: {item['rating']}/5")


# pesquisa itens pelo título
# searches for items by title
def search_items(items, search):
    results = []

    # procura títulos sem distinguir maiúsculas e minúsculas
    # searches titles without distinguishing uppercase and lowercase letters
    for item in items:
        if search.lower() in item["title"].lower():
            results.append(item)

    return results


# remove um item da lista usando seu índice
# removes an item from the list using its index
def remove_item(items, index):
    if 0 <= index < len(items):
        removed_item = items.pop(index)
        return removed_item

    return None
