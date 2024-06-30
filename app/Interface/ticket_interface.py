import requests
from PySide6.QtWidgets import QTableWidgetItem
from ui_actions import ActionState

def collect_form_data(main_window):
    data = {
        "id": main_window.ui.line_ticket_id.text(),
        "visitor_id": main_window.ui.line_ticket_visitor_id.text(),
        "type": main_window.ui.line_ticket_type.text(),
        "visit_date": main_window.ui.line_ticket_visit_date.text(),
        "purchase_date": main_window.ui.line_ticket_purchase_date.text(),
        "guided_visit_id": main_window.ui.line_ticket_guide_id.text()
    }
    return data


def populate_table_ticket(table_widget, data):
     # Definir colunas principais
    columns = ["visitor_name", "ticket_id", "purchase_date", "type", "visit_date", "guided_group", "guide_name"]
    
    # Setar a contagem de colunas e headers
    table_widget.setColumnCount(len(columns))
    table_widget.setHorizontalHeaderLabels(columns)
    
    # Contagem de linhas
    table_widget.setRowCount(len(data))

    for row_idx, ticket in enumerate(data):
        guided_visit = ticket.get("guided_visit", {})
        guide = guided_visit.get("guide", {})
        visitor = ticket.get("visitor", {})

        row_data = {
            "visitor_name": visitor.get("name", ""),
            "ticket_id": ticket.get("id", ""),
            "purchase_date": ticket.get("purchase_date", ""),
            "type": ticket.get("type", ""),
            "visit_date": ticket.get("visit_date", ""),
            "guided_group": guided_visit.get("group", ""),
            "guide_name": guide.get("name", "")
        }

        for col_idx, key in enumerate(columns):
            table_widget.setItem(row_idx, col_idx, QTableWidgetItem(str(row_data[key])))

def initialize_ticket(main_window):
    tickets = get_all_ticket()
    populate_table_ticket(main_window.ui.table_ticket, tickets)

def search_ticket(main_window):
    path = "?"
    ticket_type = main_window.ui.search_ticket_type.text()
    ticket_visitor_name = main_window.ui.search_ticket_visitor_name.text()
        

    if ticket_type:
        path += "type=" + ticket_type
    if ticket_visitor_name:
        if path != "?":
            path += "&"
        path += "visitor_name=" + ticket_visitor_name
    if path == "?":
        path = ""

    data = get_args(path)
    populate_table_ticket(main_window.ui.table_ticket, data)

def get_all_ticket():
    url = "http://127.0.0.1:5000/ticket"  # Substitua pela URL correta da API
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return []

def get_args(path):
    url = "http://127.0.0.1:5000/ticket"+path
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return []

def apply_changes_ticket(main_window):
    data = collect_form_data(main_window)
    action_state = ActionState()
    method = action_state.get_action()
    label = main_window.ui.msg_error

    try:
        if method == "POST":
            url = "http://127.0.0.1:5000/ticket"
            response = requests.post(url, json=data)
        elif method == "PUT":
            url = f"http://127.0.0.1:5000/ticket/{data['id']}"
            response = requests.put(url, json=data)
        elif method == "DELETE":
            url = f"http://127.0.0.1:5000/ticket/{data['id']}"
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
