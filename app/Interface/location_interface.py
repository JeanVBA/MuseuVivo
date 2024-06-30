import requests
from ui_functions import populate_table
from ui_actions import ActionState

def collect_form_data(main_window):
    data = {
        "id": main_window.ui.line_location_id.text(),
        "name": main_window.ui.line_location_name.text()
    }
    return data

def initialize_location(main_window):
    locations = get_all_location()
    populate_table(main_window.ui.table_location, locations)

def search_location(main_window):
    path = "?"
    location_name = main_window.ui.search_location_name.text()

    if location_name:
        path += "name=" + location_name
    if path == "?":
        path = ""

    data = get_args(path)
    populate_table(main_window.ui.table_location, data)

def get_all_location():
    url = "http://127.0.0.1:5000/location"  # Substitua pela URL correta da API
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return []

def get_args(path):
    url = "http://127.0.0.1:5000/location"+path
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return []

def apply_changes_location(main_window):
    data = collect_form_data(main_window)
    action_state = ActionState()
    method = action_state.get_action()
    label = main_window.ui.msg_error  # O QLabel onde a mensagem será exibida

    try:
        if method == "POST":
            url = "http://127.0.0.1:5000/location"
            response = requests.post(url, json=data)
        elif method == "PUT":
            url = f"http://127.0.0.1:5000/location/{data['id']}"
            response = requests.put(url, json=data)
        elif method == "DELETE":
            url = f"http://127.0.0.1:5000/location/{data['id']}"
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
