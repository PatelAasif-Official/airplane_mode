import frappe

def execute():
    all_fm = frappe.db.get_all("Flight Member", fields=["name","disabled"])
    for member in all_fm:
        if member.disabled:
            frappe.db.set_value("Flight Member",member.name,'status',"Left", update_modified = False)
        else:
            frappe.db.set_value("Flight Member",member.name,'status',"Active", update_modified = False)