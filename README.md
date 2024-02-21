---

# Capex

Capex is a project management tool developed using PySide6 and Qt for Python. It provides a user-friendly interface for managing capital expenditures within an organization.

## Features

- **Main Window:** The main window of the application serves as the entry point. It initializes the application and displays the primary user interface.
- **Model of Capex:** Defines the data model for capex management, including fields such as Capex ID, Budget No., Proposal Date, etc. It also establishes relationships with other database tables for efficient data management.
- **Widget of Capex:** Provides a widget for displaying and interacting with Capex data. Users can view, edit, and add new Capex entries using this widget.
- **Main Window UI:** Defines the layout and functionality of the main window, including menu options for accessing different features of the application.

## Installation

To run the Capex project locally, follow these steps:

1. Clone the repository:

```bash
git clone <repository_url>
cd Capex
```

2. Install the required dependencies:

```bash
pip install PySide6
```

3. Run the main script:

```bash
python main.py
```

## Usage

Once the application is running, users can perform the following actions:

- **Add New Capex:** Click on the "Add" button in the Capex widget to insert a new Capex entry.
- **Edit Capex:** Double-click on a Capex entry in the table to edit its details.
- **Save Changes:** Click on the "Save" button to save any changes made to Capex entries.
- **Close Application:** Use the close button in the main window to exit the application.


---
