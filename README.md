Hospital Management System
This project is a Hospital Management System built with a Python frontend (GUI) and a MySQL database backend. It is designed to manage doctors, patient details, appointments, medical records, and billing history.

Features
Manage Doctors: Add, edit, and delete doctor details, including name, specialization, contact information, etc.
Manage Patients: Add, edit, and view patient details such as name, contact information, insurance details, emergency contacts, etc.
Book Appointments: Schedule appointments between patients and doctors.
View Medical Records: Keep track of patient medical records, including their appointment history and status.
Billing History: View and manage billing details related to patient visits.
Database Structure
1. Patients Table
Stores information about patients.

Field	Type	Description
PatientID	int	Primary key, auto-increment
FirstName	varchar(50)	Patient's first name
LastName	varchar(50)	Patient's last name
DOB	date	Date of birth
Gender	enum('M','F','Other')	Gender of the patient
Phone	varchar(15)	Patient's phone number
Email	varchar(100)	Patient's email address
Address	varchar(255)	Patient's address
EmergencyContact	varchar(100)	Emergency contact name and number
InsuranceProvider	varchar(100)	Name of the patient's insurance provider
PolicyNumber	varchar(50)	Insurance policy number
CoverageAmount	decimal(10,2)	Insurance coverage amount
InsuranceExpiry	date	Insurance policy expiry date
2. Doctors Table
Stores information about doctors.

Field	Type	Description
DoctorID	int	Primary key, auto-increment
FirstName	varchar(50)	Doctor's first name
LastName	varchar(50)	Doctor's last name
Specialization	varchar(100)	Doctor's specialization (e.g., cardiology)
Phone	varchar(15)	Doctor's phone number
Email	varchar(100)	Doctor's email address
3. Appointments Table
Stores information about patient appointments.

Field	Type	Description
AppointmentID	int	Primary key, auto-increment
PatientID	int	Foreign key linking to the Patients table
DoctorID	int	Foreign key linking to the Doctors table
AppointmentDate	datetime	Date and time of the appointment
Reason	varchar(255)	Reason for the appointment
Status	enum('Scheduled','Completed','Canceled')	Status of the appointment


Technologies Used
Frontend: Python with Tkinter (for GUI)
Backend: MySQL (for database)
Database: MySQL (for storing data)
