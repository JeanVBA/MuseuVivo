import requests
from PySide6.QtWidgets import QTableWidgetItem
from ui_actions import ActionState

def collect_form_data(main_window):
    data = {
        "id": main_window.ui.line_exhibition_id.text(),
        "title": main_window.ui.line_exhibition_title.text(),
        "description": main_window.ui.line_exhibition_description.text(),
        "start_date": main_window.ui.line_exhibition_start_date.text(),
        "end_date": main_window.ui.line_exhibition_end_date.text()
    }
    return data


def populate_table_exhibition(table_widget, data):
   # Definir colunas principais
    columns = [
        "exhibition_id", "title", "description", "start_date", "end_date"
    ]
    
    # Setar a contagem de colunas e headers
    table_widget.setColumnCount(len(columns))
    table_widget.setHorizontalHeaderLabels(columns)
    
    # Contagem de linhas
    table_widget.setRowCount(len(data))

    for row_idx, exhibition in enumerate(data):
        row_data = {
            "exhibition_id": exhibition.get("exhibition_id", ""),
            "title": exhibition.get("title", ""),
            "description": exhibition.get("description", ""),
            "start_date": exhibition.get("start_date", ""),
            "end_date": exhibition.get("end_date", "")
        }

        for col_idx, key in enumerate(columns):
            table_widget.setItem(row_idx, col_idx, QTableWidgetItem(str(row_data[key])))

def initialize_exhibition(main_window):
    exhibitions = get_all_exhibition()
    populate_table_exhibition(main_window.ui.table_exhibition, exhibitions)

def search_exhibition(main_window):
    path = "?"
    exhibition_title = main_window.ui.search_exhibition_title.text()
    exhibition_start_date = main_window.ui.search_exhibition_start_date.text()
    exhibition_end_date = main_window.ui.search_exhibition_end_date.text()

    if exhibition_title:
        path += "title=" + exhibition_title
    if exhibition_start_date:
        if path != "?":
            path += "&"
        path += "start_date=" + exhibition_start_date
    if exhibition_end_date:
        if path != "?":
            path += "&"
        path += "end_date=" + exhibition_end_date
    if path == "?":
        path = ""

    data = get_args(path)
    populate_table_exhibition(main_window.ui.table_exhibition, data)

def get_all_exhibition():
    url = "http://127.0.0.1:5000/exhibition"  # Substitua pela URL correta da API
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return []

def get_args(path):
    url = "http://127.0.0.1:5000/exhibition"+path
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return []

def apply_changes_exhibition(main_window):
    data = collect_form_data(main_window)
    action_state = ActionState()
    method = action_state.get_action()
    label = main_window.ui.msg_error

    try:
        if method == "POST":
            url = "http://127.0.0.1:5000/exhibition"
            response = requests.post(url, json=data)
        elif method == "PUT":
            url = f"http://127.0.0.1:5000/exhibition/{data['id']}"
            response = requests.put(url, json=data)
        elif method == "DELETE":
            url = f"http://127.0.0.1:5000/exhibition/{data['id']}"
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
