# Copyright (c) 2023, Patel Asif Khan and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class ShopManagementSettings(Document):
	def before_save(self):
		notify = frappe.get_doc('Notification','Contract Expiry')
		notify.enabled = self.contract_expiry_alert
		if self.days_before : notify.days_in_advance = self.days_before
		notify.save()
