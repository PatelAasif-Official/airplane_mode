// Copyright (c) 2023, Patel Asif Khan and contributors
// For license information, please see license.txt

frappe.ui.form.on('Airplane Ticket', {
	refresh: function(frm) {
		frm.add_custom_button('Assign Ticket',(frm)=>{
			let d = new frappe.ui.Dialog({
				title:"Select Seat",
				fields:[
					{
						label: 'Seat Number',
						fieldname: 'seat_number',
						fieldtype: 'Data'
					},
				],
				primary_action_label: 'Assign',
				primary_action(values) {
					console.log(values.seat_number);
					cur_frm.set_value("seat",values.seat_number)
					cur_frm.save()
					d.hide();
				}
			})
			d.show()
		},
		'Actions')
		
	}
});
