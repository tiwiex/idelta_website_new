import frappe
def get_context(context):
    context.customers = frappe.get_list("Customer", fields=["customer_name", "gender"],ignore_permissions=True)