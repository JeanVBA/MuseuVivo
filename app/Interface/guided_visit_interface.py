import requests
from PySide6.QtWidgets import QTableWidgetItem
from ui_actions import ActionState

def collect_form_data(main_window):
    data = {
        "id": main_window.ui.line_guided_visits_id.text(),
        "group": main_window.ui.line_guided_visits_group.text(),
        "visit_date": main_window.ui.line_guided_visits_visit_date.text(),
        "hours": main_window.ui.line_guided_visits_hours.text(),
        "responsible_guide_id": main_window.ui.line_guided_visits_guide_id.text()
    }
    return data

def setup_table_headers(table_widget, headers: list):
    table_widget.setColumnCount(len(headers))
    table_widget.setHorizontalHeaderLabels(headers)

def populate_table(table_widget, data: list):
    table_widget.setRowCount(0)  # Clear existing rows
    table_widget.clear()

    if not data:
        return

    # Define the headers for the table
    headers = ["Visit ID", "Group", "Guide Name", "Hours", "Visit Date"]
    setup_table_headers(table_widget, headers)

    for entry in data:
        row_position = table_widget.rowCount()
        table_widget.insertRow(row_position)

        # Set table items based on the JSON entry
        table_widget.setItem(row_position, 0, QTableWidgetItem(str(entry.get("id", ""))))
        table_widget.setItem(row_position, 1, QTableWidgetItem(entry.get("group", "")))
        table_widget.setItem(row_position, 2, QTableWidgetItem(entry.get("guide", {}).get("name", "")))
        table_widget.setItem(row_position, 3, QTableWidgetItem(entry.get("hours", "")))
        table_widget.setItem(row_position, 4, QTableWidgetItem(entry.get("visit_date", "")))


def initialize_guided_visits(main_window):
    guided_visitss = get_all_guided_visits()
    populate_table(main_window.ui.table_gv, guided_visitss)

def search_guided_visits(main_window):
    path = "?"
    name_group = main_window.ui.search_gv_group.text()
    visit_date = main_window.ui.search_gv_visit_date.text()
    hours = main_window.ui.search_gv_hours.text()
    responsible_guide = main_window.ui.search_gv_guide_name.text()

    if name_group:
        path += "name=" + name_group
    if visit_date:
        if path != "?":
            path += "&"
        path += "visit_date=" + visit_date
    if hours:
        if path != "?":
            path += "&"
        path += "hours=" + hours
    if responsible_guide:
        if path != "?":
            path += "&"
        path += "responsible_guide=" + responsible_guide
    if path == "?":
        path = ""

    data = get_args(path)
    populate_table(main_window.ui.table_gv, data)

def get_all_guided_visits():
    url = "http://127.0.0.1:5000/guided_visit"  # Substitua pela URL correta da API
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return []

def get_args(path):
    url = "http://127.0.0.1:5000/guided_visit"+path
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return []

def apply_changes_guided_visits(main_window):
    data = collect_form_data(main_window)
    action_state = ActionState()
    method = action_state.get_action()


    label = main_window.ui.msg_error  # O QLabel onde a mensagem será exibida

    try:
        if method == "POST":
            url = "http://127.0.0.1:5000/guided_visit"
            response = requests.post(url, json=data)
        elif method == "PUT":
            url = f"http://127.0.0.1:5000/guided_visit/{data['id']}"
            response = requests.put(url, json=data)
        elif method == "DELETE":
            url = f"http://127.0.0.1:5000/guided_visit/{data['id']}"
            response = requests.delete(url)

        if response.status_code in [200, 201, 204]:
            if response.json():
                label.setText(f"Success: {response.status_code}")
            else:
                label.setText(f"Success: {response.json()}")
        else:
            if response.json() is None:
                label.setText(f"Error: {response.status_code}")
            label.setText(f"Error: {response.status_code} - {response.text}")

    except requests.exceptions.RequestException as e:
        label.setText(f"Request failed: {e}")
