import requests
from ui_functions import populate_table
from PySide6.QtWidgets import QTableWidgetItem
from ui_actions import ActionState

def collect_form_data(main_window):
    data = {
        "id": main_window.ui.line_work_of_art_id.text(),
        "name": main_window.ui.line_work_of_art_name.text(),
        "description": main_window.ui.line_work_of_art_description.text(),
        "creation_date": main_window.ui.line_work_of_art_creation_date.text(),
        "author_id": main_window.ui.line_work_of_art_author_id.text(),
        "location_id": main_window.ui.line_work_of_art_location_id.text(),
        "type": main_window.ui.line_work_of_art_type.text()
    }
    return data


def populate_table_work_of_art(table_widget, data):
    # Define all possible columns
    columns = ["author", "creation_date", "description", "id", "location", "name", "type", "material", "weight",
               "technique"]

    # Set the column count and headers
    table_widget.setColumnCount(len(columns))
    table_widget.setHorizontalHeaderLabels(columns)

    # Populate the table
    table_widget.setRowCount(len(data))
    for row_idx, item in enumerate(data):
        for col_idx, column in enumerate(columns):
            if column in item:
                table_widget.setItem(row_idx, col_idx, QTableWidgetItem(str(item[column])))
            elif "sculpture" in item and column in item["sculpture"]:
                table_widget.setItem(row_idx, col_idx, QTableWidgetItem(str(item["sculpture"][column])))
            elif "painting" in item and column in item["painting"]:
                table_widget.setItem(row_idx, col_idx, QTableWidgetItem(str(item["painting"][column])))
            else:
                table_widget.setItem(row_idx, col_idx, QTableWidgetItem(""))

def initialize_work_of_art(main_window):
    works_of_art = get_all_work_of_art()
    populate_table_work_of_art(main_window.ui.table_work_of_art, works_of_art)

def search_work_of_art(main_window):
        path = "?"
        work_of_art_name = main_window.ui.search_work_of_art_name.text()
        work_of_art_creation_date = main_window.ui.search_work_of_art_creation_date.text()
        work_of_art_author_name = main_window.ui.search_work_of_art_author_name.text()
        work_of_art_location_name = main_window.ui.search_work_of_art_location_name.text()
        work_of_art_type = main_window.ui.search_work_of_art_type.text()

        if work_of_art_name:
            path += "name=" + work_of_art_name
        if work_of_art_creation_date:
            if path != "?":
                path += "&"
            path += "creation_date=" + work_of_art_creation_date
        if work_of_art_creation_date:
            if path != "?":
                path += "&"
            path += "creation_date=" + work_of_art_creation_date
        if work_of_art_author_name:
            if path != "?":
                path += "&"
            path += "author_name=" + work_of_art_author_name
        if work_of_art_location_name:
            if path != "?":
                path += "&"
            path += "location_name=" + work_of_art_location_name
        if work_of_art_type:
            if path != "?":
                path += "&"
            path += "type=" + work_of_art_type
        if path == "?":
            path = ""

        data = get_args(path)
        populate_table_work_of_art(main_window.ui.table_work_of_art, data)

def get_all_work_of_art():
    url = "http://127.0.0.1:5000/work_of_art"  # Substitua pela URL correta da API
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return []

def get_args(path):
    url = "http://127.0.0.1:5000/work_of_art"+path
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return []

def apply_changes_work_of_art(main_window):
    data = collect_form_data(main_window)
    action_state = ActionState()
    method = action_state.get_action()
    label = main_window.ui.msg_error

    try:
        if method == "POST":
            url = "http://127.0.0.1:5000/work_of_art"
            response = requests.post(url, json=data)
        elif method == "PUT":
            url = f"http://127.0.0.1:5000/work_of_art/{data['id']}"
            response = requests.put(url, json=data)
        elif method == "DELETE":
            url = f"http://127.0.0.1:5000/work_of_art/{data['id']}"
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
