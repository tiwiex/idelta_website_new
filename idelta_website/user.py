import frappe
from frappe.core.doctype.user.user import User
class CustomUser(User):
    def validate(self):
        super().validate()  # Call the base class's validate method
        # Add your custom validation logic here
        frappe.msgprint("Custom validation logic executed.")
    def after_insert(self):
        super().after_insert()
        frappe.msgprint("Custom insert logic executed.")
    def on_update(self):
        super().on_update()
        frappe.msgprint("Custom update logic executed.")
