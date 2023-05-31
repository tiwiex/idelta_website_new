import frappe

def get_active_customers():
    count = frappe.get_list("Customer", filters={"status": "Enabled"}, limit_page_length=None)
    return len(count)
