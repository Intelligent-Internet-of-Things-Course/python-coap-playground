
class SwitchActuator:

    def __init__(self):
        self.status = False

    def change_status(self):
        self.status = not self.status
