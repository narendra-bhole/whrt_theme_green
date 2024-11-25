from frappe import _

def website_theme_after_install(doc, method):
    website_settings = frappe.get_doc("Website Settings", "Website Settings")
    website_settings.website_theme = green_theme_login  # doc.name is the name of your theme
    website_settings.save()
