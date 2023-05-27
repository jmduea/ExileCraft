#  MIT License
#
#  Copyright (c) 2023 Jon Duea
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
#

import json
import sqlite3

from PySide6.QtSql import QSqlDatabase, QSqlQuery

from modules.data.parser import path_utils

rel_path_to_db = "data/exilecraft.db"  # replace this with the correct relative path
db_path = path_utils.get_abs_path(__file__, rel_path_to_db)


class DatabaseHandler:
    def __init__(self, dp_path):
        super().__init__(self)
        self.db_path = dp_path
        self.db = None

    def create_connection(self):
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName(self.db_path)

        if not self.db.open():
            print("Failed to open database")
            return False

        return True

    def close_connection(self):
        if self.db:
            self.db.close()

    def update_or_insert_into_crafting_project(self, data):
        if not self.db or not self.db.isOpen():
            print("Database is not open")
            return

        query = QSqlQuery(self.db)

        # Prepare the query
        query.prepare("""
                    INSERT INTO crafting_project (domain, implicits, item_class, name, tags, armour, block, energy_shield, 
                    evasion, ward, movement_speed, attacks_per_second, critical_strike_chance, physical_damage_min, 
                    physical_damage_max, range, level, intelligence, dexterity, strength)
                    SELECT ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
                    WHERE NOT EXISTS (SELECT 1 FROM crafting_project)
                """)

        # Bind values
        for value in data.values():
            query.addBindValue(value)

        # Execute the query
        if not query.exec_():
            print("Failed to execute query:", query.lastError().text())

    def update_item_influences(self, influence_btns):
        if not self.db or not self.db.isOpen():
            print("Database is not open")
            return

        query = QSqlQuery(self.db)

        for button in influence_btns.buttons():
            column_name = button.text().lower().replace(' ', '_') + '_item'

            value = button.isChecked()

            query.prepare(
                f'UPDATE crafting_project SET {column_name} = ? WHERE id = (SELECT MAX(id) FROM crafting_project)')
            query.addBindValue(value)

            if not query.exec_():
                print("Failed to execute query:", query.lastError().text())
