
# CRUD, apointment,patient,counsellor API
## Overview

This Django-based API manages appointments for patients and counsellors. It provides functionality for creating, updating, fetching, and deleting appointments.

## Usage

1. Clone the repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run migrations: `python manage.py migrate`.
4. Start the development server: `python manage.py runserver`.
5. Access the API using the provided endpoints.


## API Endpoints

### Appointments

#### List Appointments

- **URL:** `/appointments/`
- **Method:** `GET`
- **Description:** Retrieve a list of all appointments.

#### Delete Appointment

- **URL:** `/appointments/delete/<int:appointment_id>/`
- **Method:** `DELETE`
- **Description:** Soft-delete an appointment by marking it as inactive.

#### Create Appointment

- **URL:** `/appointments/create/`
- **Method:** `POST`
- **Description:** Create a new appointment.

#### Update Appointment

- **URL:** `/appointments/update/<int:appointment_id>/`
- **Method:** `PUT` or `PATCH`
- **Description:** Update an existing appointment.

#### Fetch Appointment

- **URL:** `/appointments/fetch/?patient_id=<int:patient_id>&counsellor_id=<int:counsellor_id>&appointment_date=<str:date>`
- **Method:** `GET`
- **Description:** Fetch an appointment based on patient, counsellor, and appointment date.

#### Fetch Appointments for Patient

- **URL:** `/appointments/for-patient/<int:patient_id>/`
- **Method:** `GET`
- **Description:** Fetch all appointments for a specific patient.

#### Fetch Appointments for Counsellor

- **URL:** `/appointments/for-counsellor/<int:counsellor_id>/`
- **Method:** `GET`
- **Description:** Fetch all appointments for a specific counsellor.

#### Fetch Active Appointments Between Range

- **URL:** `/appointments/active/?start_date=<int:startdate>&end_date=<int:end_date>`
- **Method:** `GET`
- **Description:** Fetch all active appointments within a specified date range.

#### Fetch Appointment by ID

- **URL:** `/appointments/fetch-id/<int:appointment_id>/`
- **Method:** `GET`
- **Description:** Fetch a specific appointment by its ID.

### Patients

#### List Patients

- **URL:** `/patients/`
- **Method:** `GET`
- **Description:** Retrieve a list of all patients.

#### Create Patient

- **URL:** `/patients/create/`
- **Method:** `POST`
- **Description:** Create a new patient.

#### Update Patient

- **URL:** `/patients/update/<int:patient_id>/`
- **Method:** `PUT`
- **Description:** Update an existing patient.

#### Delete Patient

- **URL:** `/patients/delete/<int:patient_id>/`
- **Method:** `DELETE`
- **Description:** Soft-delete a patient by marking it as inactive.

#### Fetch Patient by ID

- **URL:** `/patients/fetch-id/<int:patient_id>/`
- **Method:** `GET`
- **Description:** Fetch a specific patient by its ID.

#### Fetch Patient by Email

- **URL:** `/patients/fetch-email/<str:patient_email>/`
- **Method:** `GET`
- **Description:** Fetch a specific patient by email.

