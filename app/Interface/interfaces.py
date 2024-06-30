from author_interface import initialize_author, search_author, apply_changes_author
from work_of_art_interface import initialize_work_of_art, search_work_of_art, apply_changes_work_of_art
from location_interface import initialize_location, search_location, apply_changes_location
from visitor_interface import initialize_visitor, search_visitor, apply_changes_visitor
from ticket_interface import initialize_ticket, search_ticket, apply_changes_ticket
from painting_interface import initialize_painting, search_painting, apply_changes_painting
from sculpture_interface import initialize_sculpture, search_sculpture, apply_changes_sculpture
from exhibition_interface import initialize_exhibition, search_exhibition, apply_changes_exhibition
from exhibition_work_of_art_interface import initialize_ew, search_ew, apply_changes_ew
from institution_interface import initialize_institution, search_institution, apply_changes_institution
from loan_interface import initialize_loan, search_loan, apply_changes_loan
from guide_interface import initialize_guide, search_guide, apply_changes_guide
from security_interface import initialize_security, search_security, apply_changes_security
from guided_visit_interface import initialize_guided_visits, search_guided_visits, apply_changes_guided_visits

def searchs(main_window):
    main_window.ui.btn_search_author.clicked.connect(lambda: search_author(main_window))
    main_window.ui.btn_search_work_of_art.clicked.connect(lambda: search_work_of_art(main_window))
    main_window.ui.btn_search_location.clicked.connect(lambda: search_location(main_window))
    main_window.ui.btn_search_visitor.clicked.connect(lambda: search_visitor(main_window))
    main_window.ui.btn_search_ticket.clicked.connect(lambda: search_ticket(main_window))
    main_window.ui.btn_search_painting.clicked.connect(lambda: search_painting(main_window))
    main_window.ui.btn_search_sculpture.clicked.connect(lambda: search_sculpture(main_window))
    main_window.ui.btn_search_exhibition.clicked.connect(lambda: search_exhibition(main_window))
    main_window.ui.btn_serach_ew.clicked.connect(lambda: search_ew(main_window))
    main_window.ui.btn_search_institution.clicked.connect(lambda: search_institution(main_window))
    main_window.ui.btn_search_loan.clicked.connect(lambda: search_loan(main_window))
    main_window.ui.btn_search_guide.clicked.connect(lambda: search_guide(main_window))
    main_window.ui.btn_search_security.clicked.connect(lambda: search_security(main_window))
    main_window.ui.btn_search_gv.clicked.connect(lambda: search_guided_visits(main_window))

def applys(main_window):
    main_window.ui.btn_apply_author.clicked.connect(lambda: apply_changes_author(main_window))
    main_window.ui.btn_apply_work_of_art.clicked.connect(lambda: apply_changes_work_of_art(main_window))
    main_window.ui.btn_apply_location.clicked.connect(lambda: apply_changes_location(main_window))
    main_window.ui.btn_apply_visitor.clicked.connect(lambda: apply_changes_visitor(main_window))
    main_window.ui.btn_apply_ticket.clicked.connect(lambda: apply_changes_ticket(main_window))
    main_window.ui.btn_apply_painting.clicked.connect(lambda: apply_changes_painting(main_window))
    main_window.ui.btn_apply_sculpture.clicked.connect(lambda: apply_changes_sculpture(main_window))
    main_window.ui.btn_apply_exhibition.clicked.connect(lambda: apply_changes_exhibition(main_window))
    main_window.ui.btn_apply_ew.clicked.connect(lambda: apply_changes_ew(main_window))
    main_window.ui.btn_apply_institution.clicked.connect(lambda: apply_changes_institution(main_window))
    main_window.ui.btn_apply_loan.clicked.connect(lambda: apply_changes_loan(main_window))
    main_window.ui.btn_apply_guide.clicked.connect(lambda: apply_changes_guide(main_window))
    main_window.ui.btn_apply_security.clicked.connect(lambda: apply_changes_security(main_window))
    main_window.ui.btn_apply_guided_visits.clicked.connect(lambda: apply_changes_guided_visits(main_window))

def initializes(main_window):
    initialize_author(main_window)
    initialize_work_of_art(main_window)
    initialize_location(main_window)
    initialize_visitor(main_window)
    initialize_ticket(main_window)
    initialize_painting(main_window)
    initialize_sculpture(main_window)
    initialize_exhibition(main_window)
    initialize_ew(main_window)
    initialize_institution(main_window)
    initialize_loan(main_window)
    initialize_guide(main_window)
    initialize_security(main_window)
    initialize_guided_visits(main_window)
