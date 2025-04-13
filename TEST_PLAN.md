# 🧪 Manual Testing Plan – Page Language Model

## 👤 Tester: Komal Meena
## 🎯 Goal:
To validate the structure, flow, and required fields of web application page models described using the Page Language Model (PLM) format.

---

## 📝 Test Scope
- Validate JSON structure for different page types (login, dashboard, modal, etc.)
- Confirm presence of required keys and proper formatting
- Identify missing fields, incorrect types, or structural issues

---

## 🧩 Test Scenarios

| Test Case ID | Scenario                          | Expected Result                  | Actual Result | Status  |
|--------------|-----------------------------------|----------------------------------|---------------|---------|
| TC001        | Validate `login-page.json`        | All required keys present        | As expected   | ✅ Pass |
| TC002        | Validate `dashboard-page.json`    | All components structured        | As expected   | ✅ Pass |
| TC003        | Missing `id` in input field       | Validator should flag an error   | Error shown   | ✅ Pass |
| TC004        | Extra unknown key in JSON         | Validator should warn or ignore  | Warning shown | ✅ Pass |

---

## ⚙️ Tools Used
- Python 3.x
- Custom script: `plm_validate.py`

---

## 🗂️ Files Tested
- `examples/login-page.json`
- `examples/dashboard-page.json`
- `examples/create-deal-modal.json`

---

## 🧾 Notes
- All test cases were executed manually.
- Validation was done by running the Python script and observing outputs.
- Future enhancements may include an HTML report or integration with automated test runners.

---

## 📅 Date: April 2025
