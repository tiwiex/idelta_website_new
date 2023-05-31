# my_app/my_app/routes.py
from frappe import get_route, get_doc, get_list

def get_faq_page_context(context):
    query_string = get_route("query_string")

    # Fetch data from the "FAQ" table based on the identifier (e.g., FAQ ID or name)
    faq = get_doc("Frequentl Asked Questions", query_string)

    # Create the context dictionary
    context.update({
        'title': 'FAQ Page',
        'faq': faq,
        'faq_identifier': query_string
    })

    return context

def get_page_context(context):
    page_title = get_route("query_string")

    # Fetch data from the "Product" table based on the identifier (e.g., Product ID or name)
    inner_page = get_doc("Idelta Web Page", {"page_title": page_title})

    # Create the context dictionary
    context.update({
        'title': inner_page.page_title,
        'page_content': inner_page.page_cotent,
        'page_identifier': page_title
    })

    return context

def get_faq_page():
    context = {}
    context = get_faq_page_context(context)
    return "my_app/templates/faq_template.html", context

def get_web_page():
    context = {}
    context = get_page_context(context)
    return "idelta_website/templates/inner_page.html", context

routes = [
    #{"route": "/faq/<query_string>", "method": "idelta_website.routes.get_faq_page"},
    {"route": "/inner_page/<query_string>", "method": "idelta_website.routes.get_web_page"}
]
