from author_interface import initialize_author, search_author, apply_changes_author
from work_of_art_interface import initialize_work_of_art, search_work_of_art, apply_changes_work_of_art
from location_interface import initialize_location, search_location, apply_changes_location

def searchs(main_window):
    main_window.ui.btn_search_author.clicked.connect(lambda: search_author(main_window))
    main_window.ui.btn_search_work_of_art.clicked.connect(lambda: search_work_of_art(main_window))
    main_window.ui.btn_search_location.clicked.connect(lambda: search_location(main_window))

def applys(main_window):
    main_window.ui.btn_apply_author.clicked.connect(lambda: apply_changes_author(main_window))
    main_window.ui.btn_apply_work_of_art.clicked.connect(lambda: apply_changes_work_of_art(main_window))
    main_window.ui.btn_apply_location.clicked.connect(lambda: apply_changes_location(main_window))

def initializes(main_window):
    initialize_author(main_window)
    initialize_work_of_art(main_window)
    initialize_location(main_window)

