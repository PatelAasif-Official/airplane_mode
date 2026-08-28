Hi {% if doc.full_name %}{{doc.full_name}}{% else %}{{doc.company_name}}{% endif %},
<br><br>
Your contract with {{doc.airport}} for Shop {{doc.shop_name}} is expiring on {{doc.get_formatted("expiry_date")}}. Please contact the Airport authority for Renewal.