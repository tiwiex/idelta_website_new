import frappe
def get_context(context):
    context.customers = frappe.get_list("Customer", fields=["customer_name", "gender"],ignore_permissions=True)
    context.testimonials = frappe.get_all('Testimonial', fields=['name', 'testimonial_statement', 'organisation', 'picture_of_client'],ignore_permissions=True)
    context.faqs = frappe.get_all("Frequently Asked Questions", fields=["question", "answer"], order_by="creation asc",ignore_permissions=True)
    context.portfolios = frappe.get_all("Project Portfolios", fields=["portfolio_name", "portfolio_image", "portfolio_description"],ignore_permissions=True)
    context.type_faqs = type(context.faqs)
