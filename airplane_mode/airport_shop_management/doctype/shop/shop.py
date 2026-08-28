# Copyright (c) 2023, Patel Asif Khan and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator

class Shop(WebsiteGenerator):
	def before_save(self):
		self.total_area = self.length * self.width
