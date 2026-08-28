# Copyright (c) 2023, Patel Asif Khan and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase


class TestAirplaneTicket(FrappeTestCase):
	def test_validation(self):
		ticket = frappe.new_doc("Airplane Ticket")
		ticket.passenger= "3"
		ticket.flight = "AirAsia-023-08-2023-00027"
		ticket.flight_price = 400
		ticket.status = "Booked"
		ticket.source_airport_code="DEL"
		ticket.destination_airport_code="BOM"

		self.assertRaises(frappe.ValidationError,ticket.insert)
