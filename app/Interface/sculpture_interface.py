import requests
from PySide6.QtWidgets import QTableWidgetItem
from ui_actions import ActionState

def collect_form_data(main_window):
    data = {
        "id": main_window.ui.line_sculpture_id.text(),
        "work_of_art_id": main_window.ui.line_sculpture_work_of_art_id.text(),
        "material": main_window.ui.line_sculpture_material.text(),
        "weight": main_window.ui.line_sculpture_weight.text()
    }
    return data


def populate_table_sculpture(table_widget, data):
     # Definir colunas principais
    columns = [
        "sculpture_id", "material", "weight", "work_of_art_id", "author",
        "creation_date", "description", "location", "name"
    ]
    
    # Setar a contagem de colunas e headers
    table_widget.setColumnCount(len(columns))
    table_widget.setHorizontalHeaderLabels(columns)
    
    # Contagem de linhas
    table_widget.setRowCount(len(data))

    for row_idx, sculpture in enumerate(data):
        work_of_art = sculpture.get("work_of_art", {})

        row_data = {
            "sculpture_id": sculpture.get("id", ""),
            "material": sculpture.get("material", ""),
            "weight": sculpture.get("weight", ""),
            "work_of_art_id": sculpture.get("work_of_art_id", ""),
            "author": work_of_art.get("author", ""),
            "creation_date": work_of_art.get("creation_date", ""),
            "description": work_of_art.get("description", ""),
            "location": work_of_art.get("location", ""),
            "name": work_of_art.get("name", "")
        }

        for col_idx, key in enumerate(columns):
            table_widget.setItem(row_idx, col_idx, QTableWidgetItem(str(row_data[key])))

def initialize_sculpture(main_window):
    sculptures = get_all_sculpture()
    populate_table_sculpture(main_window.ui.table_sculpture, sculptures)

def search_sculpture(main_window):
    path = "?"
    work_of_art_name = main_window.ui.search_sculpture_work_of_art_name.text()
    material = main_window.ui.search_sculpture_material.text()
    weight = main_window.ui.search_sculpture_weight.text()

    if work_of_art_name:
        path += "work_of_art_name=" + work_of_art_name
    if material:
        if path != "?":
            path += "&"
        path += "material=" + material
    if weight:
        if path != "?":
            path += "&"
        path += "weight=" + weight
    if path == "?":
        path = ""

    data = get_args(path)
    populate_table_sculpture(main_window.ui.table_sculpture, data)

def get_all_sculpture():
    url = "http://127.0.0.1:5000/sculpture"  # Substitua pela URL correta da API
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return []

def get_args(path):
    url = "http://127.0.0.1:5000/sculpture"+path
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return []

def apply_changes_sculpture(main_window):
    data = collect_form_data(main_window)
    action_state = ActionState()
    method = action_state.get_action()
    label = main_window.ui.msg_error

    try:
        if method == "POST":
            url = "http://127.0.0.1:5000/sculpture"
            response = requests.post(url, json=data)
        elif method == "PUT":
            url = f"http://127.0.0.1:5000/sculpture/{data['id']}"
            response = requests.put(url, json=data)
        elif method == "DELETE":
            url = f"http://127.0.0.1:5000/sculpture/{data['id']}"
            response = requests.delete(url)

        if response.status_code in [200, 201, 204]:
            if response.json() is None:
                label.setText(f"Success: {response.status_code}")
            else:
                label.setText(f"Success: {response.json()}")
        else:
            if response.json() is None:
                label.setText(f"Error: {response.status_code}")
            label.setText(f"Error: {response.status_code} - {response.text}")

    except requests.exceptions.RequestException as e:
        label.setText(f"Request failed: {e}")
