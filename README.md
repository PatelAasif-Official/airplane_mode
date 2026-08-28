# Airplane Mode

An airline ticketing and airport retail management app built on the
[Frappe Framework](https://frappeframework.com).

> **This is a learning exercise, not production software.** It was built while working
> through the [Frappe School](https://frappe.school) course for the **Frappe Developer
> Certification**. The domain model comes from the course; the implementation,
> validations, reports and the Airport Shop Management module are my own work against
> its requirements. It is published as a record of that work.

## Modules

The app ships two modules that share an airport as their common reference point.

### ✈️ Airplane Mode

Airline operations and ticketing.

| Doctype | Role |
|---|---|
| **Airline** | Carrier master — founding year, headquarters, customer care |
| **Airplane** | Aircraft belonging to an airline, with model and seat capacity |
| **Airplane Flight** | A scheduled flight. Submittable, published to the website |
| **Airplane Ticket** | A passenger booking on a flight. Submittable |
| **Airplane Ticket Add-on Type** / **Add-on Item** | Purchasable extras and the ticket's child table of them |
| **Flight Member** | Crew member, with designation and airline |
| **Flight Member Onboard** | Child table assigning crew to a flight |
| **Flight Passenger** | Passenger master |
| **Airport**, **Designation** | Supporting masters |

**What it does**

- **Crew double-booking prevention.** When a flight is saved, the crew list is checked
  for duplicate rows, and each member is checked against every other non-completed
  flight departing on the same date and time. Assigning someone to two simultaneous
  flights is rejected.
- **Seat capacity enforcement.** A ticket cannot be booked once the number of tickets
  on a flight reaches the aircraft's capacity.
- **Automatic seat assignment.** Tickets saved without a seat get one generated from
  the aircraft's capacity — a row number plus a letter, such as `12C`.
- **Add-on pricing.** The ticket total is the flight price plus its add-ons, with
  duplicate add-on rows dropped on validate.
- **Boarding gate.** A ticket cannot be submitted until its status is `Boarded`.
- Flights publish to the website at `/flights`, with the aircraft's details available
  to the template.

### 🏬 Airport Shop Management

Renting retail units inside airport terminals.

| Doctype | Role |
|---|---|
| **Shop** | A retail unit — dimensions, floor, airport, availability. Published to the website |
| **Tenant** | The renting individual or company |
| **Final Rent Statement** | The lease agreement. Submittable |
| **Rent Payment** | A payment against a lease. Submittable, with a print format |
| **Shop Management Settings** | Single doctype controlling reminders and alerts |

**What it does**

- **Lease lifecycle drives shop availability.** Submitting a Final Rent Statement marks
  the shop `Rented` and unpublishes it from the portal; cancelling returns it to
  `Available` and republishes it. A shop already under an active lease cannot be leased
  again.
- **Automatic area calculation** from a shop's length and width.
- **Monthly rent reminders.** A scheduled job emails every tenant with an active lease
  at the start of each month, addressing them by contact name or company name. Can be
  switched off from settings.
- **Contract expiry alerts.** A notification warns tenants ahead of lease expiry. The
  settings doctype writes its enabled flag and days-in-advance straight into the
  Notification document, so the alert is configured from the app's own UI rather than
  the Notification list.
- **Payment confirmations** email the tenant on payment, with the invoice attached.
- Shops publish to the website at `/shops`.

## Reports

Five reports, deliberately spanning all three of Frappe's report types:

| Report | Type |
|---|---|
| Revenue By Airline | Script Report — donut chart, currency summary, `LEFT JOIN` across airline → airplane → flight → ticket |
| Shop Availability By Airport | Query Report |
| Add-on Popularity | Query Report |
| Airplanes by Airline | Report Builder |
| No Of Shops By Airport | Report Builder |

## What this exercises

For anyone reading it as a portfolio piece, the app covers:

- Doctype modelling — links, child tables, submittable documents, single doctypes
- Controller hooks — `validate`, `before_save`, `before_submit`, `on_submit`, `on_cancel`
- `WebsiteGenerator` and portal templates for public-facing records
- Scheduled jobs via `scheduler_events`
- Notifications, email templates and print formats
- All three report types, including charts and report summaries
- Migration patches — a `post_model_sync` patch backfilling crew status from an older
  `disabled` checkbox
- Web forms for public ticket booking

## Installation

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app https://github.com/PatelAasif-Official/airplane_mode.git
bench --site $YOUR_SITE install-app airplane_mode
```

## Limitations

Being coursework, the scope stops where the exercises did:

- **No payment processing.** Tickets and rent payments record amounts; nothing is
  charged.
- **No seat map.** Seats are assigned randomly rather than chosen, and there is no
  check that a generated seat is free — only that the flight is not full.
- **The Cypress setup is scaffolding only** — configured, but with no tests written.
- **Ticket booking by web form is unpublished**, so the public booking flow is present
  but switched off.

## License

[MIT](license.txt)
