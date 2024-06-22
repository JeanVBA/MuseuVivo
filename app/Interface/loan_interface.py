import requests
from PySide6.QtWidgets import QTableWidgetItem
from ui_actions import ActionState

def collect_form_data(main_window):
    data = {
        "id": main_window.ui.line_loan_id.text(),
        "work_of_art_id": main_window.ui.line_loan_work_of_art_id.text(),
        "loan_date":  main_window.ui.line_loan_date.text(),
        "return_date" : main_window.ui.line_loan_return_date.text(),
        "institution_id": main_window.ui.line_loan_institution_id.text()
    }
    return data

def setup_table_headers(table_widget, headers: list):
    table_widget.setColumnCount(len(headers))
    table_widget.setHorizontalHeaderLabels(headers)

def populate_table(table_widget, data: list):
    table_widget.setRowCount(0)
    table_widget.clear()
    if not data:
        return

    headers = ["Loan ID", "Institution", "Loan Date", "Return Date", "Amount Collected", 
               "Work of Art ID", "Work of Art Name", "Author", "Creation Date", 
               "Description", "Location", "Type"]
    setup_table_headers(table_widget, headers)

    for entry in data:
        loan_id = entry.get("id")
        institution = entry.get("institution")
        loan_date = entry.get("loan_date")
        return_date = entry.get("return_date")
        amount_collected = entry.get("amount_collected")
        
        work_of_art = entry.get("work_of_art", {})
        work_of_art_id = work_of_art.get("id")
        work_of_art_name = work_of_art.get("name")
        author = work_of_art.get("author")
        creation_date = work_of_art.get("creation_date")
        description = work_of_art.get("description")
        location = work_of_art.get("location")
        work_of_art_type = work_of_art.get("type")

        row_position = table_widget.rowCount()
        table_widget.insertRow(row_position)
        table_widget.setItem(row_position, 0, QTableWidgetItem(str(loan_id)))
        table_widget.setItem(row_position, 1, QTableWidgetItem(institution))
        table_widget.setItem(row_position, 2, QTableWidgetItem(loan_date))
        table_widget.setItem(row_position, 3, QTableWidgetItem(return_date))
        table_widget.setItem(row_position, 4, QTableWidgetItem(amount_collected))
        table_widget.setItem(row_position, 5, QTableWidgetItem(str(work_of_art_id)))
        table_widget.setItem(row_position, 6, QTableWidgetItem(work_of_art_name))
        table_widget.setItem(row_position, 7, QTableWidgetItem(author))
        table_widget.setItem(row_position, 8, QTableWidgetItem(creation_date))
        table_widget.setItem(row_position, 9, QTableWidgetItem(description))
        table_widget.setItem(row_position, 10, QTableWidgetItem(location))
        table_widget.setItem(row_position, 11, QTableWidgetItem(work_of_art_type))


def initialize_loan(main_window):
    loans = get_all_loan()
    populate_table(main_window.ui.table_loan, loans)

def search_loan(main_window):
    path = "?"
    work_of_art_name = main_window.ui.search_loan_work_of_art_name.text()
    loan_date = main_window.ui.search_loan_date.text()
    return_date = main_window.ui.search_loan_return_date.text()
    institution_name = main_window.ui.search_loan_institution_name.text()

    if work_of_art_name:
        path += "work_of_art_name=" + work_of_art_name
    if loan_date:
        if path != "?":
            path += "&"
        path += "loan_date=" + loan_date
    if return_date:
        if path != "?":
            path += "&"
        path += "return_date=" + return_date
    if institution_name:
        if path != "?":
            path += "&"
        path += "institution_name=" + institution_name
    if path == "?":
        path = ""

    data = get_args(path)
    populate_table(main_window.ui.table_loan, data)

def get_all_loan():
    url = "http://127.0.0.1:5000/loan"  # Substitua pela URL correta da API
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return []

def get_args(path):
    url = "http://127.0.0.1:5000/loan"+path
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return []

def apply_changes_loan(main_window):
    data = collect_form_data(main_window)
    action_state = ActionState()
    method = action_state.get_action()


    label = main_window.ui.msg_error  # O QLabel onde a mensagem será exibida

    try:
        if method == "POST":
            url = "http://127.0.0.1:5000/loan"
            response = requests.post(url, json=data)
        elif method == "PUT":
            url = f"http://127.0.0.1:5000/loan/{data['id']}"
            response = requests.put(url, json=data)
        elif method == "DELETE":
            url = f"http://127.0.0.1:5000/loan/{data['id']}"
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
