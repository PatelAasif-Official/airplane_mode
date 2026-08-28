# Copyright (c) 2023, Patel Asif Khan and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase


class TestFlightMember(FrappeTestCase):
	def test_full_name(self):
		member =frappe.get_doc({"doctype":"Flight Member",
		"first_name" : "Patel",
		"last_name" : "Aasif",
		"designation" : "Pilot",
		"airline" : "Air India",
		"employment_no" : "AI010"
		}).insert()

		self.assertEqual(member.full_name,"Patel Aasif")
