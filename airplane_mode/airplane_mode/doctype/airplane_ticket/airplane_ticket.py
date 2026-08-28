# Copyright (c) 2023, Patel Asif Khan and contributors
# For license information, please see license.txt

import frappe
import random
import string
from frappe.model.document import Document

class AirplaneTicket(Document):
	def before_save(self):
		#Setting total amount
		total = sum([item.amount for item in self.add_ons]) if self.add_ons else 0
		self.total_amount = int(self.flight_price) + total
		#Setting seat dynamically
		if not self.seat:
			total_seats = frappe.get_value("Airplane", frappe.db.get_value("Airplane Flight",self.flight,"airplane"),"capacity")
			random_integer = random.randint(1, int(total_seats))
			random_capital_alphabet = random.choice(string.ascii_uppercase[:5])
			self.seat = str(random_integer)+random_capital_alphabet

	def validate(self):
		#Preventing duplicate entry in add-on child table
		taken_item = []
		for item in self.add_ons:
			if item.item in taken_item:
				self.add_ons.remove(item)
			else:
				taken_item.append(item.item)

		#Preventing ticket ganeration if the capacity is fulled
		total_seats = frappe.get_value("Airplane", frappe.db.get_value("Airplane Flight",self.flight,"airplane"),"capacity")
		no_seats = frappe.db.get_all(self.doctype, 
				      filters={"flight":self.flight,
		   					"source_airport_code":self.source_airport_code,
							"destination_airport_code":self.destination_airport_code,
							"departure_date":self.departure_date,
							"departure_time":self.departure_time,
							"name":['!=',self.name]},
						fields=["count(name) as booked"],
						group_by="flight")
		
		if len(no_seats)>0 and int(no_seats[0].booked) >= int(total_seats):
			frappe.throw("All seats are Booked for the Flight, Sorry for inconvenience!")

	def before_submit(self):
		#Preventing Submittion based on status
		if self.status != "Boarded":
			frappe.throw("Passenger is not Boarded yet!")