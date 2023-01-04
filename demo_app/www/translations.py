import frappe


def get_context(context):
    context.translations = frappe.get_list(
        "translations", fields=["source", "to"])
    # added test context to check if the context is translating
    context.test = "ERPNext is cool but frappe is confusing"


"""This solution only translates string contexts. strings thats is not included in context on page load are not translated ex. Navbar titles,  static html paragraphs etc.
not able to translate all occurances on the whole web app"""


def translate_from_db(context):
    translations = frappe.get_list("translations", fields=["source", "to"])
    """loop to every context on a page and checks if the value of context matched the value of translations(source) then change the value to translation(to)"""
    for item in context:
        for translation in translations:
            # checks for string only context
            if isinstance(context[item], str):
                # if context is string checks if it contians the translation(source) string
                if translation["source"] in context[item]:
                    # create the new string with values replaced from source -> to
                    new_string = context[item].replace(
                        translation["source"], translation["to"])
                    # assign the new translated string to the origin context
                    context[item] = new_string
