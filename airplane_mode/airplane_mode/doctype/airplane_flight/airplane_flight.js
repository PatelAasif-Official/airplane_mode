// Copyright (c) 2023, Patel Asif Khan and contributors
// For license information, please see license.txt

frappe.ui.form.on('Airplane Flight', {
	refresh: async function(frm) {
		cur_frm.set_query('member','flight_member_onboard', function(doc, cdt, cdn) {
            return {
                "filters": {
                    "airline":frm.doc.airline
				}
            };
        });
	}
});
