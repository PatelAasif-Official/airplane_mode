# Copyright (c) 2023, Patel Asif Khan and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import datetime

class FinalRentStatement(Document):
	def before_save(self):
		if frappe.db.exists(self.doctype, {"shop":self.shop, "docstatus":1}):
			frappe.throw("Selected shop already on Rent.")

	def on_submit(self):
		shop = frappe.get_doc("Shop", self.shop)
		shop.status = "Rented"
		shop.is_published = 1
		shop.save()

	def on_cancel(self):
		shop = frappe.get_doc("Shop", self.shop)
		shop.status = "Available"
		shop.is_published = 0
		shop.save()

def send_payment_reminders():
	if frappe.db.get_single_value("Shop Management Settings",'payment_reminder'):
		tenants = frappe.db.get_all("Final Rent Statement",filters={'docstatus':1},fields=["email","name"])
		for tenant in tenants:
			month = datetime.date.today().strftime("%B")
			shop = frappe.get_doc("Final Rent Statement", tenant['name'])
			tenant_name = shop.full_name if shop.full_name else shop.company_name
			
			subject = f"Payment Due for {month}"
			recipient = tenant['email']
			message = f"""Hi {tenant_name},<br>I hope this message finds you well. We wanted to send you a friendly 
						reminder that your monthly rent payment for '{month}' is Due for your shop {shop.shop_id} : {shop.shop_name}. We highly encourage you to 
						ensure that your payment is processed on time to avoid any late fees or inconveniences.<br><br>Thanks"""
			send_email(recipient, message, subject)

def send_email(recipient, message, subject):
	frappe.sendmail(
		recipients = recipient,
		subject = subject,
		message=message,
		now = True,
	)
