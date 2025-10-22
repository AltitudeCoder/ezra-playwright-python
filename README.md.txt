# Ezra QA Automation – Playwright Tests

## Overview
This repository contains end-to-end Playwright tests for key Ezra staging workflows:

1. **New Member Account Creation** – Simulates a new user joining from the staging site.
2. **Book a Scan / Select Plan Flow** – Logs in, navigates through the booking process, and selects an MRI plan.

The tests are written using **Python 3.13** and **Playwright 1.48+**, designed to be simple, reproducible, and scalable for larger regression suites.

---

## ⚙️ Setup Instructions

### 1. Clone and activate virtual environment
```bash
git clone <your-repo-url>
cd PlayWritePy
python3 -m venv .venv
source .venv/bin/activate
