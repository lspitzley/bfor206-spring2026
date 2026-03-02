# Product Requirements Document (PRD): Printed Exam Builder

**Status:** Draft  
**Author:** [Your Name]  
**Date:** March 2, 2026

---

## 1. Executive Summary

* **Project Vision:** [One-sentence description.]
* **The Problem:** [Describe the problem.]
* **The Solution:** [How does this system solve that problem?]
* **Success Metrics:** [How will we know it’s working?]

---

## 2. Target Audience & Personas

| Persona | Role | Primary Goal |
| :--- | :--- | :--- |
| **User A** |  |  |


---

## 3. Functional Requirements 

These are the specific features the system must perform. Priority is categorized as:

* **P1 (Must):** Essential for launch.
* **P2 (Should):** Important but can be deferred.
* **P3 (Could):** Nice to have but not critical.

| ID | Feature | Description | Priority |
| :--- | :--- | :--- | :--- |
| **F-01** | Document ordering | Cover page + MC/TF questions + Short answer | P1 |
| **F-02** | Random question order per version | Each versions questions are randomized | P1 |
| **F-03** | Question evaluation | After the exam, score questions on difficulty | P2 |
| **F-04** | |  |  |

---

## 4. Non-Functional Requirements

These define the system’s constraints and quality attributes.

* **Usability:** Single command line interface for building exams and answer keys
* **Performance:** Should take less than 30 minutes to make all exams
* **Security:** No real student data on GitHub
* **Availability:** Runs locally
* **Scalability:** 

---

## 5. User Journey & Experience

1. **Discovery:** Have a usage example for first-time use.
2. **Setup:** [Basic configuration steps]
3. **Execution:** [How to use the core features]
4. **Conclusion:** [Successful usage]

---

## 6. Technical Constraints & Stack

* **Platform:** Command-line
* **Preferred Tech:** Python, LaTeX
* **Integrations:** 

---

## 7. Out of Scope (The "Not Now")

To prevent "Scope Creep," we are explicitly **not** building:

* Not integrating with Brightspace
* Not scanning exams (these come from the Scantrons)
* C

---

## 8. Open Questions / Risks

* A
* B
* C