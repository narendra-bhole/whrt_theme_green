import frappe

@frappe.whitelist()
def switch_theme(theme):
	if theme in ["Dark", "Light", "Automatic", "whrt_theme", "whrt_theme_green"]:
		frappe.db.set_value("User", frappe.session.user, "whrt_theme", "whrt_theme_green", theme)