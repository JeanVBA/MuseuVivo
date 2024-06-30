import requests
from ui_functions import populate_table
from PySide6.QtWidgets import QTableWidgetItem
from ui_actions import ActionState

def collect_form_data(main_window):
    data = {
        "id": main_window.ui.line_visitor_id.text(),
        "name": main_window.ui.line_visitor_name.text(),
        "phone": main_window.ui.line_visitor_phone.text(),
        "email": main_window.ui.line_visitor_email.text()
    }
    return data


def populate_table_visitor(table_widget, data):
     # Definir colunas principais
    columns = ["email", "id", "name", "phone", "ticket_id", "purchase_date", "type", "visit_date", "guided_group", "guide_name"]
    
    # Setar a contagem de colunas e headers
    table_widget.setColumnCount(len(columns))
    table_widget.setHorizontalHeaderLabels(columns)
    
    # Contagem de linhas
    row_count = sum(len(item['tickets']) if 'tickets' in item and item['tickets'] else 1 for item in data)
    table_widget.setRowCount(row_count)

    row_idx = 0
    for item in data:
        base_data = {
            "email": item.get("email", ""),
            "id": item.get("id", ""),
            "name": item.get("name", ""),
            "phone": item.get("phone", "")
        }

        tickets = item.get("tickets", [])
        if tickets:
            for ticket in tickets:
                guided_visit = ticket.get("guided_visit", {})
                guide = guided_visit.get("guide", {})

                ticket_data = {
                    "ticket_id": ticket.get("id", ""),
                    "purchase_date": ticket.get("purchase_date", ""),
                    "type": ticket.get("type", ""),
                    "visit_date": ticket.get("visit_date", ""),
                    "guided_group": guided_visit.get("group", ""),
                    "guide_name": guide.get("name", "")
                }

                full_data = {**base_data, **ticket_data}
                for col_idx, column in enumerate(columns):
                    table_widget.setItem(row_idx, col_idx, QTableWidgetItem(str(full_data.get(column, ""))))
                row_idx += 1
        else:
            for col_idx, column in enumerate(columns):
                table_widget.setItem(row_idx, col_idx, QTableWidgetItem(str(base_data.get(column, ""))))
            row_idx += 1

def initialize_visitor(main_window):
    visitors = get_all_visitor()
    populate_table_visitor(main_window.ui.table_visitor, visitors)

def search_visitor(main_window):
    path = "?"
    visitor_name = main_window.ui.search_visitor_name.text()
    visitor_phone = main_window.ui.search_visitor_phone.text()
    visitor_email = main_window.ui.search_visitor_email.text()
        

    if visitor_name:
        path += "name=" + visitor_name
    if visitor_phone:
        if path != "?":
            path += "&"
        path += "phone=" + visitor_phone
    if visitor_email:
        if path != "?":
            path += "&"
        path += "email=" + visitor_email
    if path == "?":
        path = ""

    data = get_args(path)
    populate_table_visitor(main_window.ui.table_visitor, data)

def get_all_visitor():
    url = "http://127.0.0.1:5000/visitor"  # Substitua pela URL correta da API
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return []

def get_args(path):
    url = "http://127.0.0.1:5000/visitor"+path
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return []

def apply_changes_visitor(main_window):
    data = collect_form_data(main_window)
    action_state = ActionState()
    method = action_state.get_action()
    label = main_window.ui.msg_error

    try:
        if method == "POST":
            url = "http://127.0.0.1:5000/visitor"
            response = requests.post(url, json=data)
        elif method == "PUT":
            url = f"http://127.0.0.1:5000/visitor/{data['id']}"
            response = requests.put(url, json=data)
        elif method == "DELETE":
            url = f"http://127.0.0.1:5000/visitor/{data['id']}"
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
