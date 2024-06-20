import requests
from ui_functions import populate_table

def collect_form_data(main_window):
    data = {
        "id": main_window.ui.line_work_of_art_id.text(),
        "name": main_window.ui.line_work_of_art_name.text(),
        "description": main_window.ui.line_work_of_art_description.text(),
        "creation_date": main_window.ui.line_work_of_art_creation_date.text(),
        "author_id": main_window.ui.line_work_of_art_author_id.text(),
        "location_id": main_window.ui.line_work_of_art_location_id.text(),
        "type": main_window.ui.line_work_of_art_type.text()
    }
    return data

def determine_request_method(data):
    if not data['id']:
        return "POST"
    elif data['name'] and data['id']:
        return "PUT"
    elif data['id']:
        return "DELETE"


def initialize_work_of_art(main_window):
    works_of_art = get_all_work_of_art()
    populate_table(main_window.ui.table_work_of_art, works_of_art)

def search_work_of_art(main_window):
        path = "?"
        work_of_art_name = main_window.ui.search_work_of_art_name.text()
        work_of_art_creation_date = main_window.ui.search_work_of_art_creation_date.text()
        work_of_art_author_name = main_window.ui.search_work_of_art_author_name.text()
        work_of_art_location_name = main_window.ui.search_work_of_art_location_name.text()
        work_of_art_type = main_window.ui.search_work_of_art_type.text()

        if work_of_art_name:
            path += "name=" + work_of_art_name
        if work_of_art_creation_date:
            if path != "?":
                path += "&"
            path += "creation_date=" + work_of_art_creation_date
        if work_of_art_creation_date:
            if path != "?":
                path += "&"
            path += "creation_date=" + work_of_art_creation_date
        if work_of_art_author_name:
            if path != "?":
                path += "&"
            path += "author_name=" + work_of_art_author_name
        if work_of_art_location_name:
            if path != "?":
                path += "&"
            path += "location_name=" + work_of_art_location_name
        if work_of_art_type:
            if path != "?":
                path += "&"
            path += "type=" + work_of_art_type
        if path == "?":
            path = ""

        data = get_args(path)
        populate_table(main_window.ui.table_work_of_art, data)

def get_all_work_of_art():
    url = "http://127.0.0.1:5000/work_of_art"  # Substitua pela URL correta da API
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return []

def get_args(path):
    url = "http://127.0.0.1:5000/work_of_art"+path
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return []

def apply_changes_work_of_art(main_window):
    data = collect_form_data(main_window)
    method = determine_request_method(data)
    label = main_window.ui.msg_error

    try:
        if method == "POST":
            url = "http://127.0.0.1:5000/work_of_art"
            response = requests.post(url, json=data)
        elif method == "PUT":
            url = f"http://127.0.0.1:5000/work_of_art/{data['id']}"
            response = requests.put(url, json=data)
        elif method == "DELETE":
            url = f"http://127.0.0.1:5000/work_of_art/{data['id']}"
            response = requests.delete(url)

        if response.status_code in [200, 201, 204]:
            label.setText(f"Success: {response.json()}")
        else:
            label.setText(f"Error: {response.status_code} - {response.text}")

    except requests.exceptions.RequestException as e:
            label.setText(f"Request failed: {e}")
