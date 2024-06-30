# ui_functions.py
from PySide6.QtWidgets import QTableWidgetItem
from ui_actions import set_action_to_post, set_action_to_put, set_action_to_delete


def exibition(main_window):
    main_window.ui.btn_work_of_art.clicked.connect(lambda: main_window.ui.pages_events.setCurrentWidget(main_window.ui.page_work_of_art))
    main_window.ui.btn_painting.clicked.connect(lambda: main_window.ui.pages_events.setCurrentWidget(main_window.ui.page_painting))
    main_window.ui.btn_sculpture.clicked.connect(lambda: main_window.ui.pages_events.setCurrentWidget(main_window.ui.page_sculpture))
    main_window.ui.btn_author.clicked.connect(lambda: main_window.ui.pages_events.setCurrentWidget(main_window.ui.page_author))
    main_window.ui.btn_exhibition.clicked.connect(lambda: main_window.ui.pages_events.setCurrentWidget(main_window.ui.page_exhibition))
    main_window.ui.btn_ew.clicked.connect(lambda: main_window.ui.pages_events.setCurrentWidget(main_window.ui.page_ew))
    main_window.ui.btn_institution.clicked.connect(lambda: main_window.ui.pages_events.setCurrentWidget(main_window.ui.page_institution))
    main_window.ui.btn_loan.clicked.connect(lambda: main_window.ui.pages_events.setCurrentWidget(main_window.ui.page_loan))
    main_window.ui.btn_location.clicked.connect(lambda: main_window.ui.pages_events.setCurrentWidget(main_window.ui.page_location))
    main_window.ui.btn_visitor.clicked.connect(lambda: main_window.ui.pages_events.setCurrentWidget(main_window.ui.page_visitor))
    main_window.ui.btn_ticket.clicked.connect(lambda: main_window.ui.pages_events.setCurrentWidget(main_window.ui.page_ticket))
    main_window.ui.btn_guide.clicked.connect(lambda: main_window.ui.pages_events.setCurrentWidget(main_window.ui.page_guide))
    main_window.ui.btn_guided_visit.clicked.connect(lambda: main_window.ui.pages_events.setCurrentWidget(main_window.ui.page_gv))
    main_window.ui.btn_security.clicked.connect(lambda: main_window.ui.pages_events.setCurrentWidget(main_window.ui.page_security))

    main_window.ui.btn_create.clicked.connect(lambda: main_window.ui.pages_events.setCurrentWidget(main_window.ui.create_itens))
    main_window.ui.btn_update.clicked.connect(lambda: main_window.ui.pages_events.setCurrentWidget(main_window.ui.create_itens))
    main_window.ui.btn_delete.clicked.connect(lambda: main_window.ui.pages_events.setCurrentWidget(main_window.ui.create_itens))

    main_window.ui.btn_create.clicked.connect(lambda: set_action_to_post())
    main_window.ui.btn_update.clicked.connect(lambda: set_action_to_put())
    main_window.ui.btn_delete.clicked.connect(lambda: set_action_to_delete())
    
    show_and_hide_work_of_art(main_window)
    show_and_hide_painting(main_window)
    show_and_hide_sculpture(main_window)
    show_and_hide_exhibition(main_window)
    show_and_hide_author(main_window)
    show_and_hide_ew(main_window)
    show_and_hide_guide(main_window)
    show_and_hide_gv(main_window)
    show_and_hide_institution(main_window)
    show_and_hide_loan(main_window)
    show_and_hide_location(main_window)
    show_and_hide_security(main_window)
    show_and_hide_ticket(main_window)
    show_and_hide_visitor(main_window)

def lines_visibility(show_lines, hide_lines):
    def toggle_visibility():
        for widget in show_lines:
            widget.show()
            widget.clear()
        for widget in hide_lines:
            widget.hide()
            widget.clear()
    return toggle_visibility

def show_and_hide_work_of_art(main_window):
    main_window.ui.btn_create.clicked.connect(lines_visibility([
                                                                main_window.ui.line_work_of_art_name,
                                                                main_window.ui.line_work_of_art_description,
                                                                main_window.ui.line_work_of_art_creation_date,
                                                                main_window.ui.line_work_of_art_author_id,
                                                                main_window.ui.line_work_of_art_location_id,
                                                                main_window.ui.line_work_of_art_type
                                                                ], 
                                                                 [main_window.ui.line_work_of_art_id]))
    main_window.ui.btn_update.clicked.connect(lines_visibility([
                                                                main_window.ui.line_work_of_art_id,
                                                                main_window.ui.line_work_of_art_name,
                                                                main_window.ui.line_work_of_art_description,
                                                                main_window.ui.line_work_of_art_creation_date,
                                                                main_window.ui.line_work_of_art_author_id,
                                                                main_window.ui.line_work_of_art_location_id,
                                                                main_window.ui.line_work_of_art_type
                                                                ],[]))
    main_window.ui.btn_delete.clicked.connect(lines_visibility([
                                                                main_window.ui.line_work_of_art_id],
                                                                [
                                                                main_window.ui.line_work_of_art_name,
                                                                main_window.ui.line_work_of_art_description,
                                                                main_window.ui.line_work_of_art_creation_date,
                                                                main_window.ui.line_work_of_art_author_id,
                                                                main_window.ui.line_work_of_art_location_id,
                                                                main_window.ui.line_work_of_art_type
                                                                ]))

def show_and_hide_painting(main_window):
    main_window.ui.btn_create.clicked.connect(lines_visibility([main_window.ui.line_painting_work_of_art_id,
                                                                main_window.ui.line_painting_technique],
                                                                [
                                                                main_window.ui.line_painting_id
                                                                ]))
    main_window.ui.btn_update.clicked.connect(lines_visibility([main_window.ui.line_painting_id,
                                                                main_window.ui.line_painting_work_of_art_id,
                                                                main_window.ui.line_painting_technique
                                                                ],[]))
    main_window.ui.btn_delete.clicked.connect(lines_visibility([main_window.ui.line_painting_id],[
                                                                main_window.ui.line_painting_work_of_art_id,
                                                                main_window.ui.line_painting_technique]))

def show_and_hide_sculpture(main_window):
    main_window.ui.btn_create.clicked.connect(lines_visibility([main_window.ui.line_sculpture_work_of_art_id,
                                                                main_window.ui.line_sculpture_material,
                                                                main_window.ui.line_sculpture_weight],
                                                                [main_window.ui.line_sculpture_id]))
    main_window.ui.btn_update.clicked.connect(lines_visibility([main_window.ui.line_sculpture_id,
                                                                main_window.ui.line_sculpture_work_of_art_id,
                                                                main_window.ui.line_sculpture_material,
                                                                main_window.ui.line_sculpture_weight
                                                                ],[]))
    main_window.ui.btn_delete.clicked.connect(lines_visibility([main_window.ui.line_sculpture_id],
                                                               [main_window.ui.line_sculpture_work_of_art_id,
                                                                main_window.ui.line_sculpture_material,
                                                                main_window.ui.line_sculpture_weight]))

def show_and_hide_exhibition(main_window):
    main_window.ui.btn_create.clicked.connect(lines_visibility([main_window.ui.line_exhibition_title,
                                                                main_window.ui.line_exhibition_description,
                                                                main_window.ui.line_exhibition_start_date,
                                                                main_window.ui.line_exhibition_end_date
                                                                ],[main_window.ui.line_exhibition_id]))
    main_window.ui.btn_update.clicked.connect(lines_visibility([main_window.ui.line_exhibition_id,
                                                                main_window.ui.line_exhibition_title,
                                                                main_window.ui.line_exhibition_description,
                                                                main_window.ui.line_exhibition_start_date,
                                                                main_window.ui.line_exhibition_end_date
                                                                ],[]))
    main_window.ui.btn_delete.clicked.connect(lines_visibility([main_window.ui.line_exhibition_id],
                                                               [main_window.ui.line_exhibition_title,
                                                                main_window.ui.line_exhibition_description,
                                                                main_window.ui.line_exhibition_start_date,
                                                                main_window.ui.line_exhibition_end_date]))

def show_and_hide_author(main_window):
    main_window.ui.btn_create.clicked.connect(lines_visibility([main_window.ui.line_author_name], [main_window.ui.line_author_id]))
    main_window.ui.btn_update.clicked.connect(lines_visibility([main_window.ui.line_author_id, main_window.ui.line_author_name],[]))
    main_window.ui.btn_delete.clicked.connect(lines_visibility([main_window.ui.line_author_id], [main_window.ui.line_author_name]))

def show_and_hide_ew(main_window):
    main_window.ui.btn_create.clicked.connect(lines_visibility([main_window.ui.line_ew_work_of_art_id,
                                                                main_window.ui.line_ew_exhibition_id],
                                                               [main_window.ui.line_new_ew_exhibition_id,
                                                                main_window.ui.line_new_ew_work_of_art_id]))
    main_window.ui.btn_update.clicked.connect(lines_visibility([main_window.ui.line_ew_work_of_art_id,
                                                                main_window.ui.line_ew_exhibition_id,
                                                                main_window.ui.line_new_ew_work_of_art_id,
                                                                main_window.ui.line_new_ew_exhibition_id],[]))
    main_window.ui.btn_delete.clicked.connect(lines_visibility([main_window.ui.line_ew_work_of_art_id,
                                                                main_window.ui.line_ew_exhibition_id],
                                                                [main_window.ui.line_new_ew_exhibition_id,
                                                                 main_window.ui.line_new_ew_work_of_art_id]))

def show_and_hide_guide(main_window):
    main_window.ui.btn_create.clicked.connect(lines_visibility([main_window.ui.line_guide_name,
                                                                main_window.ui.line_guide_email,
                                                                main_window.ui.line_guide_phone],
                                                                [main_window.ui.line_guide_id]))
    main_window.ui.btn_update.clicked.connect(lines_visibility([main_window.ui.line_guide_id,
                                                                main_window.ui.line_guide_name,
                                                                main_window.ui.line_guide_email,
                                                                main_window.ui.line_guide_phone
                                                                ],[]))
    main_window.ui.btn_delete.clicked.connect(lines_visibility([main_window.ui.line_guide_id],
                                                               [main_window.ui.line_guide_name,
                                                                main_window.ui.line_guide_email,
                                                                main_window.ui.line_guide_phone]))

def show_and_hide_gv(main_window):
    main_window.ui.btn_create.clicked.connect(lines_visibility([main_window.ui.line_guided_visits_group,
                                                                main_window.ui.line_guided_visits_visit_date,
                                                                main_window.ui.line_guided_visits_hours,
                                                                main_window.ui.line_guided_visits_guide_id],
                                                                [main_window.ui.line_guided_visits_id]))
    main_window.ui.btn_update.clicked.connect(lines_visibility([main_window.ui.line_guided_visits_id,
                                                                main_window.ui.line_guided_visits_group,
                                                                main_window.ui.line_guided_visits_visit_date,
                                                                main_window.ui.line_guided_visits_hours,
                                                                main_window.ui.line_guided_visits_guide_id
                                                                ],[]))
    main_window.ui.btn_delete.clicked.connect(lines_visibility([main_window.ui.line_guided_visits_guide_id],
                                                               [main_window.ui.line_guided_visits_group,
                                                                main_window.ui.line_guided_visits_visit_date,
                                                                main_window.ui.line_guided_visits_hours,
                                                                main_window.ui.line_guided_visits_guide_id]))

def show_and_hide_institution(main_window):
    main_window.ui.btn_create.clicked.connect(lines_visibility([main_window.ui.line_institution_name],
                                                               [main_window.ui.line_institution_id]))
    main_window.ui.btn_update.clicked.connect(lines_visibility([main_window.ui.line_institution_id,
                                                                main_window.ui.line_institution_name],
                                                               []))
    main_window.ui.btn_delete.clicked.connect(lines_visibility([main_window.ui.line_institution_id],
                                                               [main_window.ui.line_institution_name]))

def show_and_hide_loan(main_window):
    main_window.ui.btn_create.clicked.connect(lines_visibility([main_window.ui.line_loan_work_of_art_id,
                                                                main_window.ui.line_loan_institution_id,
                                                                main_window.ui.line_loan_date,
                                                                main_window.ui.line_loan_return_date],
                                                               [main_window.ui.line_loan_id]))
    main_window.ui.btn_update.clicked.connect(lines_visibility([main_window.ui.line_loan_id,
                                                                main_window.ui.line_loan_work_of_art_id,
                                                                main_window.ui.line_loan_institution_id,
                                                                main_window.ui.line_loan_date,
                                                                main_window.ui.line_loan_return_date],
                                                               []))
    main_window.ui.btn_delete.clicked.connect(lines_visibility([main_window.ui.line_loan_id],
                                                               [main_window.ui.line_loan_work_of_art_id,
                                                                main_window.ui.line_loan_institution_id,
                                                                main_window.ui.line_loan_date,
                                                                main_window.ui.line_loan_return_date]))

def show_and_hide_location(main_window):
    main_window.ui.btn_create.clicked.connect(lines_visibility([main_window.ui.line_location_name],
                                                               [main_window.ui.line_location_id]))
    main_window.ui.btn_update.clicked.connect(lines_visibility([main_window.ui.line_location_id, main_window.ui.line_location_name],
                                                               []))
    main_window.ui.btn_delete.clicked.connect(lines_visibility([main_window.ui.line_location_id],
                                                               [main_window.ui.line_location_name]))

def show_and_hide_security(main_window):
    main_window.ui.btn_create.clicked.connect(lines_visibility([main_window.ui.line_security_name,
                                                                main_window.ui.line_security_email,
                                                                main_window.ui.line_security_phone,
                                                                main_window.ui.line_security_location_id],
                                                               [main_window.ui.line_security_id]))
    main_window.ui.btn_update.clicked.connect(lines_visibility([main_window.ui.line_security_id,
                                                                main_window.ui.line_security_name,
                                                                main_window.ui.line_security_email,
                                                                main_window.ui.line_security_phone,
                                                                main_window.ui.line_security_location_id],
                                                               []))
    main_window.ui.btn_delete.clicked.connect(lines_visibility([main_window.ui.line_security_id],
                                                               [main_window.ui.line_security_name,
                                                                main_window.ui.line_security_email,
                                                                main_window.ui.line_security_phone,
                                                                main_window.ui.line_security_location_id]))

def show_and_hide_ticket(main_window):
    main_window.ui.btn_create.clicked.connect(lines_visibility([main_window.ui.line_ticket_visitor_id,
                                                                main_window.ui.line_ticket_type,
                                                                main_window.ui.line_ticket_visit_date,
                                                                main_window.ui.line_ticket_purchase_date,
                                                                main_window.ui.line_ticket_guide_id],
                                                               [main_window.ui.line_ticket_id]))
    main_window.ui.btn_update.clicked.connect(lines_visibility([main_window.ui.line_ticket_id,
                                                                main_window.ui.line_ticket_visitor_id,
                                                                main_window.ui.line_ticket_type,
                                                                main_window.ui.line_ticket_visit_date,
                                                                main_window.ui.line_ticket_purchase_date,
                                                                main_window.ui.line_ticket_guide_id],
                                                               []))
    main_window.ui.btn_delete.clicked.connect(lines_visibility([main_window.ui.line_ticket_id],
                                                               [main_window.ui.line_ticket_visitor_id,
                                                                main_window.ui.line_ticket_type,
                                                                main_window.ui.line_ticket_visit_date,
                                                                main_window.ui.line_ticket_purchase_date,
                                                                main_window.ui.line_ticket_guide_id]))

def show_and_hide_visitor(main_window):
    main_window.ui.btn_create.clicked.connect(lines_visibility([main_window.ui.line_visitor_name,
                                                                main_window.ui.line_visitor_email,
                                                                main_window.ui.line_visitor_phone],
                                                               [main_window.ui.line_visitor_id]))
    main_window.ui.btn_update.clicked.connect(lines_visibility([main_window.ui.line_visitor_id,
                                                                main_window.ui.line_visitor_name,
                                                                main_window.ui.line_visitor_email,
                                                                main_window.ui.line_visitor_phone],
                                                               []))
    main_window.ui.btn_delete.clicked.connect(lines_visibility([main_window.ui.line_visitor_id],
                                                               [main_window.ui.line_visitor_name,
                                                                main_window.ui.line_visitor_email,
                                                                main_window.ui.line_visitor_phone]))


def populate_table(table_widget, data):
    if not data:
        return

    table_widget.setRowCount(len(data))
    table_widget.setColumnCount(len(data[0]))

    headers = list(data[0].keys())
    table_widget.setHorizontalHeaderLabels(headers)

    for row_idx, row_data in enumerate(data):
        for col_idx, key in enumerate(headers):
            table_widget.setItem(row_idx, col_idx, QTableWidgetItem(str(row_data[key])))

