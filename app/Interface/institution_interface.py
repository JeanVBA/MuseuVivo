import requests
from PySide6.QtWidgets import QTableWidgetItem
from ui_actions import ActionState

def collect_form_data(main_window):
    data = {
        "id": main_window.ui.line_institution_id.text(),
        "name": main_window.ui.line_institution_name.text()
    }
    return data

def setup_table_headers(table_widget, headers: list):
    table_widget.setColumnCount(len(headers))
    table_widget.setHorizontalHeaderLabels(headers)

def populate_table(table_widget, data: list):
    table_widget.setRowCount(0)  # Limpa todas as linhas existentes
    table_widget.clear()
    if not data:
        return

    headers = ["Exhibition ID", "Exhibition Name", "Work of Art Name", "Author", "Creation Date", "Description", "Type"]
    setup_table_headers(table_widget, headers)

    for entry in data:
        exhibition_id = entry.get("id")
        exhibition_name = entry.get("name")
        works_of_art = entry.get("works_of_art", [])

        if not works_of_art:
            # Exibição sem obras de arte
            row_position = table_widget.rowCount()
            table_widget.insertRow(row_position)
            table_widget.setItem(row_position, 0, QTableWidgetItem(str(exhibition_id)))
            table_widget.setItem(row_position, 1, QTableWidgetItem(exhibition_name))
            table_widget.setItem(row_position, 2, QTableWidgetItem(""))
            table_widget.setItem(row_position, 3, QTableWidgetItem(""))
            table_widget.setItem(row_position, 4, QTableWidgetItem(""))
            table_widget.setItem(row_position, 5, QTableWidgetItem(""))
            table_widget.setItem(row_position, 6, QTableWidgetItem(""))
        else:
            # Exibição com obras de arte
            for work_of_art in works_of_art:
                row_position = table_widget.rowCount()
                table_widget.insertRow(row_position)
                table_widget.setItem(row_position, 0, QTableWidgetItem(str(exhibition_id)))
                table_widget.setItem(row_position, 1, QTableWidgetItem(exhibition_name))
                table_widget.setItem(row_position, 2, QTableWidgetItem(work_of_art.get("name", "")))
                table_widget.setItem(row_position, 3, QTableWidgetItem(work_of_art.get("author", "")))
                table_widget.setItem(row_position, 4, QTableWidgetItem(work_of_art.get("creation_date", "")))
                table_widget.setItem(row_position, 5, QTableWidgetItem(work_of_art.get("description", "")))
                table_widget.setItem(row_position, 6, QTableWidgetItem(work_of_art.get("type", "")))

def initialize_institution(main_window):
    institutions = get_all_institution()
    populate_table(main_window.ui.table_institution, institutions)

def search_institution(main_window):
    path = "?"
    institution_name = main_window.ui.search_institution_name.text()
    institution_loan_date = main_window.ui.search_institution_loan_date.text()
    institution_return_loan_date = main_window.ui.search_institution_return_loan_date.text()

    if institution_name:
        path += "name=" + institution_name
    if institution_loan_date:
        if path != "?":
            path += "&"
        path += "loan_date=" + institution_loan_date
    if institution_return_loan_date:
        if path != "?":
            path += "&"
        path += "return_loan_date=" + institution_return_loan_date
    if path == "?":
        path = ""

    data = get_args(path)
    populate_table(main_window.ui.table_institution, data)

def get_all_institution():
    url = "http://127.0.0.1:5000/institution"  # Substitua pela URL correta da API
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return []

def get_args(path):
    url = "http://127.0.0.1:5000/institution"+path
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return []

def apply_changes_institution(main_window):
    data = collect_form_data(main_window)
    action_state = ActionState()
    method = action_state.get_action()


    label = main_window.ui.msg_error  # O QLabel onde a mensagem será exibida

    try:
        if method == "POST":
            url = "http://127.0.0.1:5000/institution"
            response = requests.post(url, json=data)
        elif method == "PUT":
            url = f"http://127.0.0.1:5000/institution/{data['id']}"
            response = requests.put(url, json=data)
        elif method == "DELETE":
            url = f"http://127.0.0.1:5000/institution/{data['id']}"
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
