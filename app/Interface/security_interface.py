import requests
from ui_functions import populate_table
from ui_actions import ActionState

def collect_form_data(main_window):
    data = {
        "id": main_window.ui.line_security_id.text(),
        "name": main_window.ui.line_security_name.text(),
        "email": main_window.ui.line_security_email.text(),
        "phone": main_window.ui.line_security_phone.text(),
        "location_id": main_window.ui.line_security_location_id.text()
    }
    return data

def initialize_security(main_window):
    securitys = get_all_security()
    populate_table(main_window.ui.table_security, securitys)

def search_security(main_window):
    path = "?"
    security_name = main_window.ui.search_security_name.text()
    security_email = main_window.ui.search_security_email.text()
    security_phone = main_window.ui.search_security_phone.text()
    security_location_name = main_window.ui.search_security_location_name.text()

    if security_name:
        path += "name=" + security_name
    if security_email:
        if path != "?":
            path += "&"
        path += "email=" + security_email
    if security_phone:
        if path != "?":
            path += "&"
        path += "phone=" + security_phone
    if security_location_name:
        if path != "?":
            path += "&"
        path += "location_name=" + security_location_name
    if path == "?":
        path = ""

    data = get_args(path)
    populate_table(main_window.ui.table_security, data)

def get_all_security():
    url = "http://127.0.0.1:5000/security"  # Substitua pela URL correta da API
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return []

def get_args(path):
    url = "http://127.0.0.1:5000/security"+path
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return []

def apply_changes_security(main_window):
    data = collect_form_data(main_window)
    action_state = ActionState()
    method = action_state.get_action()


    label = main_window.ui.msg_error  # O QLabel onde a mensagem será exibida

    try:
        if method == "POST":
            url = "http://127.0.0.1:5000/security"
            response = requests.post(url, json=data)
        elif method == "PUT":
            url = f"http://127.0.0.1:5000/security/{data['id']}"
            response = requests.put(url, json=data)
        elif method == "DELETE":
            url = f"http://127.0.0.1:5000/security/{data['id']}"
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
