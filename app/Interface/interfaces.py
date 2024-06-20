from author_interface import initialize_author, search_author, apply_changes_author
from work_of_art_interface import initialize_work_of_art, search_work_of_art, apply_changes_work_of_art
from location_interface import initialize_location, search_location, apply_changes_location
from visitor_interface import initialize_visitor, search_visitor, apply_changes_visitor
from ticket_interface import initialize_ticket, search_ticket, apply_changes_ticket
from painting_interface import initialize_painting, search_painting, apply_changes_painting

def searchs(main_window):
    main_window.ui.btn_search_author.clicked.connect(lambda: search_author(main_window))
    main_window.ui.btn_search_work_of_art.clicked.connect(lambda: search_work_of_art(main_window))
    main_window.ui.btn_search_location.clicked.connect(lambda: search_location(main_window))
    main_window.ui.btn_search_visitor.clicked.connect(lambda: search_visitor(main_window))
    main_window.ui.btn_search_ticket.clicked.connect(lambda: search_ticket(main_window))
    main_window.ui.btn_search_painting.clicked.connect(lambda: search_painting(main_window))

def applys(main_window):
    main_window.ui.btn_apply_author.clicked.connect(lambda: apply_changes_author(main_window))
    main_window.ui.btn_apply_work_of_art.clicked.connect(lambda: apply_changes_work_of_art(main_window))
    main_window.ui.btn_apply_location.clicked.connect(lambda: apply_changes_location(main_window))
    main_window.ui.btn_apply_visitor.clicked.connect(lambda: apply_changes_visitor(main_window))
    main_window.ui.btn_apply_ticket.clicked.connect(lambda: apply_changes_ticket(main_window))
    main_window.ui.btn_apply_painting.clicked.connect(lambda: apply_changes_painting(main_window))

def initializes(main_window):
    initialize_author(main_window)
    initialize_work_of_art(main_window)
    initialize_location(main_window)
    initialize_visitor(main_window)
    initialize_ticket(main_window)
    initialize_painting(main_window)
