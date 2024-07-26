import frappe

def create_purchase_invoice(sales_invoice):
    frappe.msgprint("Creating purchase invoices...")

    # Get items from the sales invoice
    items = frappe.get_all('Sales Invoice Item', filters={'parent': sales_invoice.name}, fields=['item_code', 'qty', 'rate'])

    # Loop through each item in the sales invoice
    for item in items:
        # Check if the item has a supplier assigned
        supplier = frappe.get_value('Item Supplier', {'parent': item.item_code}, 'supplier')
        if supplier:
            # Create a Purchase Invoice for the supplier
            frappe.msgprint(f"Creating purchase invoice for supplier {supplier}...")
            purchase_invoice = frappe.get_doc({
                'doctype': 'Purchase Invoice',
                'supplier': supplier,
                'posting_date': frappe.utils.today(),
                'company': frappe.defaults.get_user_default('company'),
                'items': [{
                    'item_code': item.item_code,
                    'qty': item.qty,
                    'rate': item.rate,
                }]
            })
            purchase_invoice.insert()
            purchase_invoice.submit()
            frappe.msgprint(f"Purchase invoice {purchase_invoice.name} created successfully.")

# Hook the create_purchase_invoice function to the Sales Invoice submit event
def on_submit(doc, method):
    if doc.doctype == 'Sales Invoice':
        frappe.msgprint(f"Sales invoice {doc.name} submitted. Creating purchase invoices...")
        create_purchase_invoice(doc)

