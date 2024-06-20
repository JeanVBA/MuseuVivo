import requests
from PySide6.QtWidgets import QTableWidgetItem

def collect_form_data(main_window):
    data = {
        "id": main_window.ui.line_painting_id.text(),
        "work_of_art_id": main_window.ui.line_painting_work_of_art_id.text(),
        "technique": main_window.ui.line_painting_technique.text()
    }
    return data


def populate_table_painting(table_widget, data):
     # Definir colunas principais
    columns = [
        "painting_id", "technique", "work_of_art_id", "author",
        "creation_date", "description", "location", "name"
    ]
    
    # Setar a contagem de colunas e headers
    table_widget.setColumnCount(len(columns))
    table_widget.setHorizontalHeaderLabels(columns)
    
    # Contagem de linhas
    table_widget.setRowCount(len(data))

    for row_idx, painting in enumerate(data):
        work_of_art = painting.get("work_of_art", {})

        row_data = {
            "painting_id": painting.get("id", ""),
            "technique": painting.get("technique", ""),
            "work_of_art_id": painting.get("work_of_art_id", ""),
            "author": work_of_art.get("author", ""),
            "creation_date": work_of_art.get("creation_date", ""),
            "description": work_of_art.get("description", ""),
            "location": work_of_art.get("location", ""),
            "name": work_of_art.get("name", "")
        }

        for col_idx, key in enumerate(columns):
            table_widget.setItem(row_idx, col_idx, QTableWidgetItem(str(row_data[key])))


def determine_request_method(data):
    if not data['id']:
        return "POST"
    elif data['technique'] and data['id']:
        return "PUT"
    elif data['id']:
        return "DELETE"


def initialize_painting(main_window):
    paintings = get_all_painting()
    populate_table_painting(main_window.ui.table_painting, paintings)

def search_painting(main_window):
    path = "?"
    work_of_art_name = main_window.ui.search_painting_work_of_art_name.text()
    technique = main_window.ui.search_painting_technique.text()

    if work_of_art_name:
        path += "work_of_art_name=" + work_of_art_name
    if technique:
        if path != "?":
            path += "&"
        path += "technique=" + technique
    if path == "?":
        path = ""

    data = get_args(path)
    populate_table_painting(main_window.ui.table_painting, data)

def get_all_painting():
    url = "http://127.0.0.1:5000/painting"  # Substitua pela URL correta da API
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return []

def get_args(path):
    url = "http://127.0.0.1:5000/painting"+path
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return []

def apply_changes_painting(main_window):
    data = collect_form_data(main_window)
    method = determine_request_method(data)
    label = main_window.ui.msg_error

    try:
        if method == "POST":
            url = "http://127.0.0.1:5000/painting"
            response = requests.post(url, json=data)
        elif method == "PUT":
            url = f"http://127.0.0.1:5000/painting/{data['id']}"
            response = requests.put(url, json=data)
        elif method == "DELETE":
            url = f"http://127.0.0.1:5000/painting/{data['id']}"
            response = requests.delete(url)

        if response.status_code in [200, 201, 204]:
            label.setText(f"Success: {response.json()}")
        else:
            label.setText(f"Error: {response.status_code} - {response.text}")

    except requests.exceptions.RequestException as e:
            label.setText(f"Request failed: {e}")
