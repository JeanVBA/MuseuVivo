import requests
from ui_functions import populate_table
from ui_actions import ActionState

def collect_form_data(main_window):
    data = {
        "id": main_window.ui.line_guide_id.text(),
        "name": main_window.ui.line_guide_name.text(),
        "email": main_window.ui.line_guide_email.text(),
        "phone": main_window.ui.line_guide_phone.text()
    }
    return data

def initialize_guide(main_window):
    guides = get_all_guide()
    populate_table(main_window.ui.table_guide, guides)

def search_guide(main_window):
    path = "?"
    guide_name = main_window.ui.search_guide_name.text()
    guide_email = main_window.ui.search_guide_email.text()
    guide_phone = main_window.ui.search_guide_phone.text()

    if guide_name:
        path += "name=" + guide_name
    if guide_email:
        if path != "?":
            path += "&"
        path += "email=" + guide_email
    if guide_phone:
        if path != "?":
            path += "&"
        path += "phone=" + guide_phone
    if path == "?":
        path = ""

    data = get_args(path)
    populate_table(main_window.ui.table_guide, data)

def get_all_guide():
    url = "http://127.0.0.1:5000/guide"  # Substitua pela URL correta da API
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return []

def get_args(path):
    url = "http://127.0.0.1:5000/guide"+path
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return []

def apply_changes_guide(main_window):
    data = collect_form_data(main_window)
    action_state = ActionState()
    method = action_state.get_action()


    label = main_window.ui.msg_error  # O QLabel onde a mensagem será exibida

    try:
        if method == "POST":
            url = "http://127.0.0.1:5000/guide"
            response = requests.post(url, json=data)
        elif method == "PUT":
            url = f"http://127.0.0.1:5000/guide/{data['id']}"
            response = requests.put(url, json=data)
        elif method == "DELETE":
            url = f"http://127.0.0.1:5000/guide/{data['id']}"
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
