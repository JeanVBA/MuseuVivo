from PySide6.QtCore import Slot

class ActionState:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ActionState, cls).__new__(cls)
            cls._instance.action = None
        return cls._instance

    def set_action(self, action):
        self.action = action

    def get_action(self):
        return self.action


@Slot()
def set_action_to_post():
    method = ActionState()
    method.set_action("POST")
    print("Action set to POST")

@Slot()
def set_action_to_put():
    method = ActionState()
    method.set_action("PUT")
    print("Action set to PUT")

@Slot()
def set_action_to_delete():
    method = ActionState()
    method.set_action("DELETE")
    print("Action set to DELETE")