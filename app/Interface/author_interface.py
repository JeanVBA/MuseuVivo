# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass
import requests
from ui_functions import populate_table

def collect_form_data(main_window):
    data = {
        "id": main_window.ui.line_author_id.text(),
        "name": main_window.ui.line_author_name.text()
    }
    return data

def determine_request_method(data):
    if not data['id']:
        return "POST"
    elif data['name'] and data['id']:
        return "PUT"
    elif data['id']:
        return "DELETE"


def initialize_author(main_window):
    authors = get_all_author()
    populate_table(main_window.ui.table_author, authors)

def search_author(main_window):
        path = "?"
        author_id = main_window.ui.search_author_id.text()
        author_name = main_window.ui.search_author_name.text()

        if author_id:
            path += "id=" + author_id
        if author_name:
            if path != "?":
                path += "&"
            path += "name=" + author_name
        if path == "?":
            path = ""

        data = get_args(path)
        populate_table(main_window.ui.table_author, data)

def get_all_author():
    url = "http://127.0.0.1:5000/author"  # Substitua pela URL correta da API
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return []

def get_args(path):
    url = "http://127.0.0.1:5000/author"+path
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return []

def apply_changes_author(main_window):
    data = collect_form_data(main_window)
    method = determine_request_method(data)
    label = main_window.ui.msg_error  # O QLabel onde a mensagem será exibida

    try:
        if method == "POST":
            url = "http://127.0.0.1:5000/author"
            response = requests.post(url, json=data)
        elif method == "PUT":
            url = f"http://127.0.0.1:5000/author/{data['id']}"
            response = requests.put(url, json=data)
        elif method == "DELETE":
            url = f"http://127.0.0.1:5000/author/{data['id']}"
            response = requests.delete(url)

        if response.status_code in [200, 201, 204]:
            label.setText(f"Success: {response.json()}")
        else:
            label.setText(f"Error: {response.status_code} - {response.text}")

    except requests.exceptions.RequestException as e:
            label.setText(f"Request failed: {e}")