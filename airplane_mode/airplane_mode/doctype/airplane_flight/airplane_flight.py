# Copyright (c) 2023, Patel Asif Khan and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator

class AirplaneFlight(WebsiteGenerator):
	def on_submit(self):
		#Updating status on submittion
		self.status = "Completed"

	def validate(self):
		self.validate_member()

	def get_context(self, context):
		context.airplane = frappe.get_doc("Airplane", self.airplane)

	def validate_member(self):
		#Validate Availability and duplicate entry
		unique = []
		frappe.errprint(type(self.time_of_departure))
		for member in self.flight_member_onboard:
			if member.member not in unique:
				unique.append(member.member)
			else:
				frappe.throw(f"Duplicate entry found at <b>Row {member.idx}</b>.")

			not_avilable = frappe.db.sql_list(f"""
						SELECT fmo.full_name FROM `tabAirplane Flight` af
						JOIN `tabFlight Member Onboard` fmo
						ON fmo.parent = af.name
						WHERE af.status != "Completed"
							AND af.name != '{self.name}'
							AND af.date_of_departure = '{self.date_of_departure}'
							AND af.time_of_departure = '{self.time_of_departure}'
							AND fmo.member = '{member.member}'
					""")
			if not_avilable:
				frappe.throw(f"Crew member <b>{not_avilable[0]}</b> flying in another flight at the same Date and Time.")

	