from pyscript import document
# Dictionary



elements = {
    "H": ("Hydrogen", 1, 1.008),
    "C": ("Carbon", 6, 12.011),
    "N": ("Nitrogen", 7, 14.007),
    "O": ("Oxygen", 8, 15.999),
    "P": ("Phosphorus", 15, 30.974),
    "S": ("Sulfur", 16, 32.06),
    "Se": ("Selenium", 34, 78.971)
}

def search_element(e):
    # Get the input from HTML
    Element1 = document.getElementById("element1").value
    # Retrieve information from dictionary
    result = elements.get(Element1, ("Element not found", "-", "-"))
    # Display the result in HTML
    document.getElementById("symbol").innerText = Element1
    document.getElementById("name").innerText = result[0]
    document.getElementById("number").innerText = result[1]
    document.getElementById("mass").innerText = result[2]

    