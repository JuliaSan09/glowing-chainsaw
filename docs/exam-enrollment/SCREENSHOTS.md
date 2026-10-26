# Exam enrollment — where to screenshot

Org: Cooper and Co (`org60040760589`). Sign in as ACP Pradhyuman.

These screens are already configured in Zoho CRM. Capture the live CRM. Do not mock the UI.

## 1. Round-robin assignment

Setup → Automation → Workflow Rules → **Exam Round Robin Assign**.

The rule runs when a Lead is created and Exam Program is filled. It assigns the lead to the next counselor, Maya Quereshi or Indravadhan Sarabhai, and sets Assign Method to Round Robin, Enroll Stage to New Inquiry, and Owner Locked.

Leads → list view **Exam Round Robin Leads**. Owners alternate:

| Lead | Exam program | Owner |
| --- | --- | --- |
| Aarav Mehta | JEE Main | Maya Quereshi |
| Diya Kapoor | NEET UG | Indravadhan Sarabhai |
| Kabir Singh | CAT | Maya Quereshi |
| Ananya Rao | UPSC CSE | Indravadhan Sarabhai |
| Rohan Iyer | Bank PO | Maya Quereshi |
| Sneha Nair | CUET | Indravadhan Sarabhai |
| Vikram Shah | JEE Main | Maya Quereshi |
| Pooja Das | NEET UG | Indravadhan Sarabhai |

## 2. Click-to-call

Setup → Customization → Modules and Fields → Leads → Links and Buttons → **Call via Servetel**.

The button sits on the lead detail page for Administrator, Legal Managers, and Legal Assistant. It opens a Pabbly click-to-call URL with the lead phone number and record id.

Open Aarav Mehta (or any exam lead) and capture the **Call via Servetel** button with Servetel Call ID, Recording URL, Call Direction, Call Outcome, and Call Duration.

Calls → list view **Exam Servetel Calls** shows the eight calls tied to those leads (inbound, outbound, and missed), including duration and result.

A live Servetel IVR account and a live Pabbly workflow are not connected in this org. The button and the stored call history are the CRM side of that integration. Clicking the button opens the webhook URL; it does not dial a handset.

## 3. Website inquiries

Leads → list view **Exam Website Inquiries**.

Aarav Mehta (JEE Inquiry Form), Ananya Rao (UPSC Counseling Form), and Sneha Nair (CUET Application Form) have Capture Path **Website Pabbly**. That is the shape of a form post pushed into CRM. A live website form and a live Pabbly connection are not attached in this org.

## 4. Call conversions

Deals → **Exam Incoming Call Deals**

- Incoming Call - NEET UG - Diya Kapoor (Indravadhan Sarabhai, Closed Won, 52,000)
- Incoming Call - JEE Main - Vikram Shah (Maya Quereshi, Closed Won, 48,000)

Deals → **Exam Outgoing Call Deals**

- Outgoing Call - Bank PO - Rohan Iyer (Maya Quereshi, Closed Won, 28,000)
- Outgoing Call - CUET - Sneha Nair (Indravadhan Sarabhai, Closed Won, 18,000)

Lead lists **Exam Incoming Call Leads** and **Exam Outgoing Call Leads** show the same split on the student record.

CRM report and dashboard APIs are not available on this connection, so these public custom views are the screens to capture for agent performance and incoming versus outgoing conversions.

## 5. Ownership control

Setup → Automation → Workflow Rules:

- **Exam lock owner Maya**
- **Exam lock owner Indravadhan**

Each rule watches Lead Owner. If Maya Quereshi or Indravadhan Sarabhai changes the owner of a locked lead, the rule assigns it back to the Assigned Counselor. An administrator change is left as saved.

Checked with Aarav Mehta: an administrator change of Lead Owner was kept, then the owner was set back to Maya Quereshi so the round-robin list stays even.

Client Scripts cannot be created with the automation tools on this org. The two workflow rules are the ownership lock that is actually in the CRM.

## Fields on Leads

Exam Program, Enroll Stage, Call Direction, Call Outcome, Servetel Call ID, Recording URL, Call Duration, Assign Method, Owner Locked, Website Form, Capture Path, Assigned Counselor.
