# Odoo 18 + Custom Addons

This project sets up an Odoo 18 environment along with custom modules, including a Todo List module with CRUD operations, tagging, and attendee tracking.

## Setup Instructions

### 1. Clone Odoo 18 source code

```bash
git clone https://github.com/odoo/odoo.git --depth 1 --branch 18.0 community
```

---

### 2. Clone this repository (custom addons)

or merge the custom module structure into your current repository.

---

### 3. Create & activate a Python virtual environment

```bash
python -m venv venv
source venv/bin/activate         # For macOS/Linux
venv\Scripts\activate          # For Windows
```

---

### 4. Install Python dependencies

Use the `requirements.txt` from the Odoo source:

```bash
pip install -r community/requirements.txt
```

---

### 5. Set up PostgreSQL

- Install PostgreSQL
- Create a database and user that matches your `odoo.conf` settings

---

### 6. Configure Odoo

Edit `custom-addons/odoo18/odoo.conf` 

---

### 7. Run Odoo

```bash
python community/odoo-bin -c custom-addons/odoo18/odoo.conf
```

Then open browser at:  
http://localhost:8069
