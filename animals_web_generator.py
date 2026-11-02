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
    output += '<li class="cards__item">\n'

    if "name" in animal:
        output += f'  <div class="card__title">{animal["name"]}</div>\n'

    output += '  <p class="card__text">\n'

    characteristics = animal.get("characteristics", {})

    if "diet" in characteristics:
        output += f'    <strong>Diet:</strong> {characteristics["diet"]}<br/>\n'

    locations = animal.get("locations", [])
    if locations:
        output += f"    <strong>Location:</strong> {locations[0]}<br/>\n"

    if "type" in characteristics:
        output += f'    <strong>Type:</strong> {characteristics["type"]}<br/>\n'

    output += "  </p>\n"
    output += "</li>\n"

html_content = template.replace("__REPLACE_ANIMALS_INFO__", output)

with open("animals.html", "w", encoding="utf-8") as handle:
    handle.write(html_content)

print("Created animals.html")