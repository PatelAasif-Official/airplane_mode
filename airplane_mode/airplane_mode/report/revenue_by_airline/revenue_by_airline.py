# Copyright (c) 2023, Patel Asif Khan and contributors
# For license information, please see license.txt

import frappe
from frappe import _
import time

def execute(filters=None):
	
	for i in range(0,101):
		frappe.publish_progress(i, title='Loading...', description='Please wait Getting details')
		time.sleep(0.1)

	columns = get_column(filters)
	data, chart  = get_data_n_chart(filters)
	total = sum([d['revenue'] for d in data])
	summary = [{'value':total,'label':'Total Revenue','datatype':'Currency','color':'green'}]
	return columns, data, None, chart, summary

def get_data_n_chart(filters):
	data = frappe.db.sql("""
		    SELECT al.name as airline, COALESCE(revenue, 0) as revenue
			FROM `tabAirline` al
			LEFT JOIN (
					SELECT ap.airline, SUM(at.total_amount) as revenue
					FROM `tabAirplane` ap
					LEFT JOIN `tabAirplane Flight` af ON ap.name = af.airplane
					LEFT JOIN `tabAirplane Ticket` at ON af.name = at.flight
					GROUP BY ap.airline
			) AS airline_revenue 
		    ON al.name = airline_revenue.airline;
		""", as_dict=True)

	chart = {
		"data":{
			"labels":[d.airline for d in data],
			"datasets":[{'name':'Revenue by Airline', 'values':[d.revenue for d in data]}]
		},
		"type":"donut"
	}

	return data, chart

def get_column(filters):
	return [
		{
			"fieldname":"airline",
			"label":"Airline",
			"fieldtype":"Link",
			"options":"Airline",
			"width":200
		},
		{
			"fieldname":"revenue",
			"label":"Revenue",
			"fieldtype":"Currency",
			"width":150
		}
	]