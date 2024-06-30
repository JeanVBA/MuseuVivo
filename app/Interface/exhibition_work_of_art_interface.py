import requests
from PySide6.QtWidgets import QTableWidgetItem
from ui_actions import ActionState

def collect_form_data(main_window):
    data = {
        "work_of_art_id": main_window.ui.line_ew_work_of_art_id.text(),
        "exhibition_id": main_window.ui.line_ew_exhibition_id.text(),
        "new_work_of_art_id": main_window.ui.line_new_ew_work_of_art_id.text(),
        "new_exhibition_id": main_window.ui.line_new_ew_exhibition_id.text()
    }
    return data


def setup_table_headers(table_widget, headers: list):
    table_widget.setColumnCount(len(headers))
    table_widget.setHorizontalHeaderLabels(headers)

def populate_table(table_widget, data: list):
    table_widget.setRowCount(0)  # Limpa todas as linhas existentes

    if not data:
        return

    # Determine the type of data by checking the keys of the first item
    first_item = data[0]

    if "works_of_art" in first_item:
        headers = ["Exhibition ID", "Exhibition Title", "Work of Art Name", "Author", "Creation Date", "Description"]
        setup_table_headers(table_widget, headers)
        for entry in data:
            for work_of_art in entry["works_of_art"]:
                row_position = table_widget.rowCount()
                table_widget.insertRow(row_position)

                table_widget.setItem(row_position, 0, QTableWidgetItem(str(entry["exhibition_id"])))
                table_widget.setItem(row_position, 1, QTableWidgetItem(entry["exhibition_title"]))
                table_widget.setItem(row_position, 2, QTableWidgetItem(work_of_art["name"]))
                table_widget.setItem(row_position, 3, QTableWidgetItem(work_of_art.get("author", "")))
                table_widget.setItem(row_position, 4, QTableWidgetItem(work_of_art.get("creation_date", "")))
                table_widget.setItem(row_position, 5, QTableWidgetItem(work_of_art.get("description", "")))

    elif "exhibitions" in first_item:
        headers = ["Work of Art ID", "Work of Art Name", "Exhibition Title", "Exhibition Description", "Exhibition Start Date", "Exhibition End Date"]
        setup_table_headers(table_widget, headers)
        for entry in data:
            for exhibition in entry["exhibitions"]:
                row_position = table_widget.rowCount()
                table_widget.insertRow(row_position)

                table_widget.setItem(row_position, 0, QTableWidgetItem(str(entry["work_of_art_id"])))
                table_widget.setItem(row_position, 1, QTableWidgetItem(entry["work_of_art_name"]))
                table_widget.setItem(row_position, 2, QTableWidgetItem(exhibition["title"]))
                table_widget.setItem(row_position, 3, QTableWidgetItem(exhibition.get("description", "")))
                table_widget.setItem(row_position, 4, QTableWidgetItem(exhibition.get("start_date", "")))
                table_widget.setItem(row_position, 5, QTableWidgetItem(exhibition.get("end_date", "")))

    elif "exhibition_id" in first_item:
        headers = ["Exhibition ID", "Exhibition Title", "Work of Art ID", "Work of Art Name"]
        setup_table_headers(table_widget, headers)
        for entry in data:
            row_position = table_widget.rowCount()
            table_widget.insertRow(row_position)

            table_widget.setItem(row_position, 0, QTableWidgetItem(str(entry["exhibition_id"])))
            table_widget.setItem(row_position, 1, QTableWidgetItem(entry["exhibition_title"]))
            table_widget.setItem(row_position, 2, QTableWidgetItem(str(entry["work_of_art_id"])))
            table_widget.setItem(row_position, 3, QTableWidgetItem(entry["work_of_art_name"]))



def initialize_ew(main_window):
    ews = get_all_ew()
    populate_table(main_window.ui.table_ew, ews)

def search_ew(main_window):
    work_of_art_id = main_window.ui.search_ew_work_of_art_id.text()
    exhibition_id = main_window.ui.search_ew_exhibition_id.text()

    if work_of_art_id:
        data = get_ew_work_of_art_id(f"/{work_of_art_id}") 
        populate_table(main_window.ui.table_ew, data)
    elif exhibition_id:
        data = get_ew_exhibition_id(f"/{exhibition_id}")
        populate_table(main_window.ui.table_ew, data)
    else:
       data = get_all_ew()
       populate_table(main_window.ui.table_ew, data)



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
    action_state = ActionState()
    method = action_state.get_action()
    print(method)  # Verifica se o método está correto
    label = main_window.ui.msg_error

    try:
        if method == "POST":
            url = "http://127.0.0.1:5000/exhibition_work_of_art"
            response = requests.post(url, json=data)
        elif method == "PUT":
            url = f"http://127.0.0.1:5000/exhibition_work_of_art/work_of_art_id/{data['work_of_art_id']}/exhibition_id/{data['exhibition_id']}"
            new_data = {
                "work_of_art_id": data['new_work_of_art_id'],
                "exhibition_id": data['new_exhibition_id']
            }
            response = requests.put(url, json=new_data)
        elif method == "DELETE":
            url = f"http://127.0.0.1:5000/exhibition_work_of_art/work_of_art_id/{data['work_of_art_id']}/exhibition_id/{data['exhibition_id']}"
            response = requests.delete(url)

        if response.status_code in [200, 201, 204]:
            if method == "DELETE":
                label.setText(f"Success: {response.status_code}")
            else:
                label.setText(f"Success: {response.json()}")
        else:
            if not response.json():
                label.setText(f"Error: {response.status_code}")
            label.setText(f"Error: {response.status_code} - {response.text}")

    except requests.exceptions.RequestException as e:
        label.setText(f"Request failed: {e}")
