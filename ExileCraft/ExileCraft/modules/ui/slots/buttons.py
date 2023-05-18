from ...db.database_handler import DatabaseHandler

class ButtonHandler:
    def __init__(self):
        self.db_handler = DatabaseHandler()

    def set_item_influences(self, button_id, checked, influence_btns, checked_btns, max_checked_buttons=2):
        sender = influence_btns.button(button_id)
        if checked:
            checked_btns.append(sender)
            if len(checked_btns) > max_checked_buttons:
                oldest_button = checked_btns.pop(0)
                oldest_button.setChecked(False)
        self.db_handler.update_item_influences(influence_btns)

    @staticmethod
    def item_quality_btn_checked(item_quality_btns):
        """
        Returns the text of the currently checked button in the item_quality_btns button group.

        This method iterates over all buttons in the item_quality_btns button group, checks if
        the button is checked, and if it is, returns the text of the button as an integer.

        If no button is checked, the method returns 0.
        """
        for button in item_quality_btns.buttons():
            if button.isChecked():
                return int(button.text())

        return 0

    @staticmethod
    def ilvl_btn_checked(ilvl_btns):
        """
        Returns the text of the currently checked button in the ilvl_btns button group.

        This method iterates over all buttons in the ilvl_btns button group, checks if
        the button is checked, and if it is, returns the text of the button as an integer.

        If no button is checked, the method returns 0.
        """
        for button in ilvl_btns.buttons():
            if button.isChecked():
                return int(button.text())

        return 0