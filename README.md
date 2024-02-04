
# CRUD, apointment,patient,counsellor API
## Overview

This Django-based API manages appointments for patients and counsellors. It provides functionality for creating, updating, fetching, and deleting appointments.


## How to Run

To get started, follow these steps:

### Install Dependencies

Run the following command to install the required dependencies:

```python```
pip install -r requirements.txt

## API Endpoints

### List Appointments

- **URL:** `/appointments/`
- **Method:** `GET`
- **Description:** Retrieve a list of all appointments.

### Delete Appointment

- **URL:** `/appointments/delete/<int:appointment_id>/`
- **Method:** `DELETE`
- **Description:** Soft-delete an appointment by marking it as inactive.

### Create Appointment

- **URL:** `/appointments/create/`
- **Method:** `POST`
- **Description:** Create a new appointment.

### Update Appointment

- **URL:** `/appointments/update/<int:appointment_id>/`
- **Method:** `PUT` or `PATCH`
- **Description:** Update an existing appointment.

### Fetch Appointment

- **URL:** `/appointments/fetch/?patient_id='patientid'&counsellor_id='counselorId'&appointment_date="date"`
- **Method:** `GET`
- **Description:** Fetch an appointment based on patient, counsellor, and appointment date.

### Fetch Appointments for Patient

- **URL:** `/appointments/for-patient/<int:patient_id>/`
- **Method:** `GET`
- **Description:** Fetch all appointments for a specific patient.

### Fetch Appointments for Counsellor

- **URL:** `/appointments/for-counsellor/<int:counsellor_id>/`
- **Method:** `GET`
- **Description:** Fetch all appointments for a specific counsellor.

### Fetch Active Appointments Between Range

- **URL:** `/appointments/active/?start_date=<int:startdate>&end_date=<int:end_date>`
- **Method:** `GET`
- **Description:** Fetch all active appointments within a specified date range.

### Fetch Appointment by ID

- **URL:** `/appointments/fetch-id/<int:appointment_id>/`
- **Method:** `GET`
- **Description:** Fetch a specific appointment by its ID.

## Usage

1. Clone the repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run migrations: `python manage.py migrate`.
4. Start the development server: `python manage.py runserver`.
5. Access the API using the provided endpoints.

## Dependencies

- Django
- Django REST Framework
