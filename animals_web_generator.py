import json


def load_data(file_path):
    """Loads a JSON file."""
    with open(file_path, "r", encoding="utf-8") as json_file:
        data = json.load(json_file)
    return data


animals_data = load_data("animals_data.json")

with open("animals_template.html", "r", encoding="utf-8") as handle:
    template = handle.read()

output = ""

for animal in animals_data:
    if "name" in animal:
        output += f"Name: {animal['name']}\n"

    characteristics = animal.get("characteristics", {})

    if "diet" in characteristics:
        output += f"Diet: {characteristics['diet']}\n"

    locations = animal.get("locations", [])
    if locations:
        output += f"Location: {locations[0]}\n"

    if "type" in characteristics:
        output += f"Type: {characteristics['type']}\n"

    output += "\n"

html_content = template.replace("__REPLACE_ANIMALS_INFO__", output)

with open("animals.html", "w", encoding="utf-8") as handle:
    handle.write(html_content)

print("Created animals.html")