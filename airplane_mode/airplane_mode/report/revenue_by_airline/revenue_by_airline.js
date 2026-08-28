// Copyright (c) 2023, Patel Asif Khan and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Revenue By Airline"] = {
	"filters": [

	]
};

frappe.realtime.on('event_name', (data) => {
    console.log(data)
})