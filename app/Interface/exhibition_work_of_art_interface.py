import requests
from PySide6.QtWidgets import QTableWidgetItem
from ui_functions import ActionButtonRequest
from PySide6.QtCore import Slot

def collect_form_data(main_window):
    data = {
        "work_of_art_id": main_window.ui.line_ew_work_of_art_id.text(),
        "exhibition_id": main_window.ui.line_ew_exhibition_id.text(),
        "new_work_of_art_id": main_window.ui.line_new_ew_work_of_art_id.text(),
        "new_exhibition_id": main_window.ui.line_new_ew_exhibition_id.text()
    }
    return data


def populate_table_ew(table_widget, data):
    columns = ["exhibition_id", "exhibition_title", "work_of_art_id", "work_of_art_name"]
    table_widget.setColumnCount(len(columns))
    table_widget.setHorizontalHeaderLabels(columns)
    table_widget.setRowCount(len(data))

    for row_idx, item in enumerate(data):
        for col_idx, key in enumerate(columns):
            table_widget.setItem(row_idx, col_idx, QTableWidgetItem(str(item.get(key, ""))))

def populate_table_ew_exhibition(table_widget, data):
    columns = ["exhibition_id", "exhibition_title", "author", "creation_date", "description", "name", "technique", "type"]
    table_widget.setColumnCount(len(columns))
    table_widget.setHorizontalHeaderLabels(columns)

    row_idx = 0
    for item in data:
        exhibition_id = item.get("exhibition_id", "")
        exhibition_title = item.get("exhibition_title", "")
        works_of_art = item.get("works_of_art", [])
        
        for work in works_of_art:
            table_widget.insertRow(row_idx)
            row_data = {
                "exhibition_id": exhibition_id,
                "exhibition_title": exhibition_title,
                "author": work.get("author", ""),
                "creation_date": work.get("creation_date", ""),
                "description": work.get("description", ""),
                "name": work.get("name", ""),
                "technique": work.get("painting", {}).get("technique", "") if work.get("type") == "Painting" else "",
                "type": work.get("type", "")
            }

            for col_idx, key in enumerate(columns):
                table_widget.setItem(row_idx, col_idx, QTableWidgetItem(str(row_data[key])))

            row_idx += 1

def populate_table_ew_work_of_art(table_widget, data):
    columns = ["work_of_art_id", "work_of_art_name", "exhibition_title", "exhibition_description", "start_date", "end_date"]
    table_widget.setColumnCount(len(columns))
    table_widget.setHorizontalHeaderLabels(columns)

    row_idx = 0
    for item in data:
        work_of_art_id = item.get("work_of_art_id", "")
        work_of_art_name = item.get("work_of_art_name", "")
        exhibitions = item.get("exhibitions", [])
        
        for exhibition in exhibitions:
            table_widget.insertRow(row_idx)
            row_data = {
                "work_of_art_id": work_of_art_id,
                "work_of_art_name": work_of_art_name,
                "exhibition_title": exhibition.get("title", ""),
                "exhibition_description": exhibition.get("description", ""),
                "start_date": exhibition.get("start_date", ""),
                "end_date": exhibition.get("end_date", "")
            }

            for col_idx, key in enumerate(columns):
                table_widget.setItem(row_idx, col_idx, QTableWidgetItem(str(row_data[key])))

            row_idx += 1


def initialize_ew(main_window):
    ews = get_all_ew()
    populate_table_ew(main_window.ui.table_ew, ews)

def search_ew(main_window):
    work_of_art_id = main_window.ui.search_ew_work_of_art_id.text()
    exhibition_id = main_window.ui.search_ew_exhibition_id.text()

    if work_of_art_id:
        data = get_ew_work_of_art_id(f"/{work_of_art_id}") 
        populate_table_ew_work_of_art(main_window.ui.table_ew, data)
    if exhibition_id:
        data = get_ew_exhibition_id(f"/{exhibition_id}")
        populate_table_ew_exhibition(main_window.ui.table_ew, data)
    if work_of_art_id is None and exhibition_id is None:
       data = get_all_ew()
       populate_table_ew(main_window.ui.table_ew, data)



def get_all_ew():
    url = "http://127.0.0.1:5000/exhibition_work_of_art"  # Substitua pela URL correta da API
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return []

def get_ew_work_of_art_id(path):
    url = "http://127.0.0.1:5000/exhibition_work_of_art/work_of_art"+path
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return []

def get_ew_exhibition_id(path):
    url = "http://127.0.0.1:5000/exhibition_work_of_art/exhibition"+path
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return []

def apply_changes_ew(main_window):
    data = collect_form_data(main_window)
    type_request = ActionButtonRequest()
    type_request.actions(main_window)

    # Conecte o botão "Apply" para determinar o método e executar a ação
    main_window.ui.btn_apply_exhibition_work_of_art.clicked.connect(lambda: execute_request(main_window, type_request, data))

def execute_request(main_window, type_request, data):
    method = type_request.determine_request_method()
    print(method)  # Verifica se o método está correto
    label = main_window.ui.msg_error

    try:
        if method == "POST":
            url = "http://127.0.0.1:5000/exhibition_work_of_art"
            response = requests.post(url, json=data)
        elif method == "PUT":
            url = f"http://127.0.0.1:5000/exhibition_work_of_art/work_of_art_id/{data['work_of_art_id']}/exhibition_id/{data['exhibition_id']}"
            response = requests.put(url, json=data)
        elif method == "DELETE":
            url = f"http://127.0.0.1:5000/exhibition_work_of_art/work_of_art_id/{data['work_of_art_id']}/exhibition_id/{data['exhibition_id']}"
            response = requests.delete(url)

        if response.status_code in [200, 201, 204]:
            if response.json() is None:
                label.setText(f"Success: {response.status_code}")
            else:
                label.setText(f"Success: {response.json()}")
        else:
            label.setText(f"Error: {response.status_code} - {response.text}")

    except requests.exceptions.RequestException as e:
        label.setText(f"Request failed: {e}")
