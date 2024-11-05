import tkinter as tk
from tkinter import messagebox
import mysql.connector
from tkcalendar import DateEntry  # Import DateEntry from tkcalendar
from datetime import datetime

# Function to connect to the database
def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="aksh2050",
        database="medicalrecordsdb"
    )

# ------------------- MAIN PAGE --------------------------
def main_page():
    root = tk.Tk()
    root.title("Hospital Management System")
    root.geometry("400x450")
    root.configure(bg='#1e1e1e')  # Dark background color

    label_main = tk.Label(root, text="Hospital Management System", font=("Helvetica", 18, "bold"), bg='#1e1e1e', fg='#f0f4f7')
    label_main.pack(pady=20)

    button_style = {
        "width": 30,
        "height": 2,
        "bg": "#4CAF50",  # Button background color
        "fg": "white",    # Button text color
        "font": ("Helvetica", 12),
        "relief": "raised"
    }

    # Adjust button styles for dark mode
    button_doctors = tk.Button(root, text="Doctors", command=doctors_page, **button_style)
    button_doctors.pack(pady=10)

    button_patients = tk.Button(root, text="Patients", command=patients_page, **button_style)
    button_patients.pack(pady=10)

    button_appointments = tk.Button(root, text="Appointments", command=appointments_page, **button_style)
    button_appointments.pack(pady=10)

    button_medical_history = tk.Button(root, text="Medical History & Prescriptions", command=medical_history_page, **button_style)
    button_medical_history.pack(pady=10)

    button_billing = tk.Button(root, text="Billing", command=billing_page, **button_style)
    button_billing.pack(pady=10)

    root.mainloop()

# ------------------- DOCTORS PAGE --------------------------
def doctors_page():
    doctors_root = tk.Tk()
    doctors_root.title("Doctors Management")
    doctors_root.geometry("600x600")
    doctors_root.configure(bg='#2E2E2E')  # Dark background color

    label_title = tk.Label(doctors_root, text="Manage Doctors", font=("Helvetica", 16, "bold"), bg='#2E2E2E', fg='#FFFFFF')
    label_title.grid(row=0, column=1, pady=20)

    entry_style = {"bg": "#3E3E3E", "fg": "#FFFFFF", "font": ("Helvetica", 12), "width": 25}  # Dark entry style

    label_first_name = tk.Label(doctors_root, text="First Name:", font=("Helvetica", 12), bg='#2E2E2E', fg='#FFFFFF')
    label_first_name.grid(row=1, column=0, padx=20, pady=10, sticky='e')
    entry_first_name = tk.Entry(doctors_root, **entry_style)
    entry_first_name.grid(row=1, column=1, padx=20, pady=10)

    label_last_name = tk.Label(doctors_root, text="Last Name:", font=("Helvetica", 12), bg='#2E2E2E', fg='#FFFFFF')
    label_last_name.grid(row=2, column=0, padx=20, pady=10, sticky='e')
    entry_last_name = tk.Entry(doctors_root, **entry_style)
    entry_last_name.grid(row=2, column=1, padx=20, pady=10)

    label_specialization = tk.Label(doctors_root, text="Specialization:", font=("Helvetica", 12), bg='#2E2E2E', fg='#FFFFFF')
    label_specialization.grid(row=3, column=0, padx=20, pady=10, sticky='e')
    entry_specialization = tk.Entry(doctors_root, **entry_style)
    entry_specialization.grid(row=3, column=1, padx=20, pady=10)

    label_phone = tk.Label(doctors_root, text="Phone:", font=("Helvetica", 12), bg='#2E2E2E', fg='#FFFFFF')
    label_phone.grid(row=4, column=0, padx=20, pady=10, sticky='e')
    entry_phone = tk.Entry(doctors_root, **entry_style)
    entry_phone.grid(row=4, column=1, padx=20, pady=10)

    label_email = tk.Label(doctors_root, text="Email:", font=("Helvetica", 12), bg='#2E2E2E', fg='#FFFFFF')
    label_email.grid(row=5, column=0, padx=20, pady=10, sticky='e')
    entry_email = tk.Entry(doctors_root, **entry_style)
    entry_email.grid(row=5, column=1, padx=20, pady=10)

    button_add = tk.Button(doctors_root, text="Add Doctor", font=("Helvetica", 12), bg="#4CAF50", fg="white", command=lambda: insert_doctor(entry_first_name, entry_last_name, entry_specialization, entry_phone, entry_email, doctors_list))
    button_add.grid(row=6, column=0, padx=20, pady=10)

    button_update = tk.Button(doctors_root, text="Update Doctor", font=("Helvetica", 12), bg="#FF9800", fg="white", command=lambda: update_doctor(entry_first_name, entry_last_name, entry_specialization, entry_phone, entry_email, doctors_list))
    button_update.grid(row=6, column=1, padx=20, pady=10)

    button_delete = tk.Button(doctors_root, text="Delete Doctor", font=("Helvetica", 12), bg="#F44336", fg="white", command=lambda: delete_doctor(doctors_list))
    button_delete.grid(row=6, column=2, padx=20, pady=10)

    doctors_list = tk.Listbox(doctors_root, height=8, width=60, font=("Helvetica", 12), bg='#3E3E3E', fg='#FFFFFF')  # Dark listbox with white text
    doctors_list.grid(row=7, column=0, columnspan=3, padx=20, pady=20)
    doctors_list.bind('<<ListboxSelect>>', lambda event: select_doctor(doctors_list, entry_first_name, entry_last_name, entry_specialization, entry_phone, entry_email))

    display_doctors(doctors_list)

    doctors_root.mainloop()

# ------------------- APPOINTMENTS PAGE --------------------------
import tkinter as tk
from tkcalendar import DateEntry
from tkinter import ttk  # For the combobox

import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

def appointments_page():
    appointments_root = tk.Tk()
    appointments_root.title("Appointments Management System")
    appointments_root.geometry("900x500")
    appointments_root.configure(bg="#2E2E2E")  # Dark background

    label_title = tk.Label(appointments_root, text="Manage Appointments", font=("Helvetica", 18, "bold"), bg="#2E2E2E", fg="white")
    label_title.grid(row=0, column=1, pady=20)

    # Create a frame for entry fields
    frame_entries = tk.Frame(appointments_root, bg="#2E2E2E")
    frame_entries.grid(row=1, column=0, columnspan=3, padx=20, pady=10)

    # Entry fields for appointment details
    label_patient_id = tk.Label(frame_entries, text="Patient ID:", bg="#2E2E2E", fg="white", font=("Helvetica", 12))
    label_patient_id.grid(row=0, column=0, padx=10, pady=5)
    entry_patient_id = tk.Entry(frame_entries, font=("Helvetica", 12), bg="#3E3E3E", fg="white")  # Dark entry background
    entry_patient_id.grid(row=0, column=1, padx=10, pady=5)

    label_doctor_id = tk.Label(frame_entries, text="Doctor ID:", bg="#2E2E2E", fg="white", font=("Helvetica", 12))
    label_doctor_id.grid(row=1, column=0, padx=10, pady=5)
    entry_doctor_id = tk.Entry(frame_entries, font=("Helvetica", 12), bg="#3E3E3E", fg="white")  # Dark entry background
    entry_doctor_id.grid(row=1, column=1, padx=10, pady=5)

    label_appointment_date = tk.Label(frame_entries, text="Appointment Date:", bg="#2E2E2E", fg="white", font=("Helvetica", 12))
    label_appointment_date.grid(row=2, column=0, padx=10, pady=5)
    entry_appointment_date = DateEntry(frame_entries, date_pattern='yyyy-mm-dd', font=("Helvetica", 12), background="#3E3E3E", foreground="white")  # Dark DateEntry
    entry_appointment_date.grid(row=2, column=1, padx=10, pady=5)

    label_reason = tk.Label(frame_entries, text="Reason:", bg="#2E2E2E", fg="white", font=("Helvetica", 12))
    label_reason.grid(row=3, column=0, padx=10, pady=5)
    entry_reason = tk.Entry(frame_entries, font=("Helvetica", 12), bg="#3E3E3E", fg="white")  # Dark entry background
    entry_reason.grid(row=3, column=1, padx=10, pady=5)

    label_status = tk.Label(frame_entries, text="Status:", bg="#2E2E2E", fg="white", font=("Helvetica", 12))
    label_status.grid(row=4, column=0, padx=10, pady=5)
    entry_status = ttk.Combobox(frame_entries, values=['Scheduled', 'Completed', 'Canceled'], state='readonly', font=("Helvetica", 12), background="#3E3E3E", foreground="white")  # Dark combobox
    entry_status.grid(row=4, column=1, padx=10, pady=5)
    entry_status.current(0)  # Set default to 'Scheduled'

    # Create a frame for buttons
    frame_buttons = tk.Frame(appointments_root, bg="#2E2E2E")  # Dark button frame
    frame_buttons.grid(row=5, column=0, columnspan=3, pady=10)

    button_add = tk.Button(frame_buttons, text="Add Appointment", command=lambda: insert_appointment(
        entry_patient_id, entry_doctor_id, entry_appointment_date, entry_reason, entry_status, appointments_list), 
        font=("Helvetica", 12), bg="#4CAF50", fg="white")  # Green button
    button_add.grid(row=0, column=0, padx=10)

    button_update = tk.Button(frame_buttons, text="Update Appointment", command=lambda: update_appointment(
        entry_patient_id, entry_doctor_id, entry_appointment_date, entry_reason, entry_status, appointments_list), 
        font=("Helvetica", 12), bg="#2196F3", fg="white")  # Blue button
    button_update.grid(row=0, column=1, padx=10)

    button_delete = tk.Button(frame_buttons, text="Delete Appointment", command=lambda: delete_appointment(appointments_list), 
        font=("Helvetica", 12), bg="#f44336", fg="white")  # Red button
    button_delete.grid(row=0, column=2, padx=10)

    appointments_list = tk.Listbox(appointments_root, height=8, width=90, font=("Helvetica", 12), bg="#3E3E3E", fg="white")  # Dark listbox
    appointments_list.grid(row=6, column=0, columnspan=3, padx=20, pady=10)

    appointments_list.bind('<<ListboxSelect>>', lambda event: select_appointment(appointments_list,
        entry_patient_id, entry_doctor_id, entry_appointment_date, entry_reason, entry_status))

    display_appointments(appointments_list)
    appointments_root.mainloop()

# Function to display appointments in the list
def display_appointments(appointments_list):
    db = connect_to_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Appointments")
    appointments = cursor.fetchall()
    appointments_list.delete(0, tk.END)
    for appointment in appointments:
        appointments_list.insert(tk.END, f"{appointment[0]}: Patient {appointment[1]}, Doctor {appointment[2]}, Date: {appointment[3]}, Reason: {appointment[4]}, Status: {appointment[5]}")

    cursor.close()
    db.close()

# Function to insert a new appointment
def insert_appointment(patient_id, doctor_id, appointment_date, reason, status, appointments_list):
    db = connect_to_db()
    cursor = db.cursor()
    new_id=get_next_id("AppointmentID",cursor , "Appointments")
    cursor.execute("INSERT INTO Appointments (AppointmentID, PatientID, DoctorID, AppointmentDate, Reason, Status) VALUES (%s, %s, %s, %s, %s, %s)",
                   (new_id, patient_id.get(), doctor_id.get(), appointment_date.get(), reason.get(), status.get()))
    db.commit()
    cursor.close()
    db.close()
    display_appointments(appointments_list)

# Function to update an existing appointment
def update_appointment(patient_id, doctor_id, appointment_date, reason, status, appointments_list):
    selected_appointment = appointments_list.curselection()
    if selected_appointment:
        appointment_info = appointments_list.get(selected_appointment)
        appointment_id = int(appointment_info.split(":")[0])  # Extract appointment ID
        db = connect_to_db()
        cursor = db.cursor()
        cursor.execute("UPDATE Appointments SET PatientID = %s, DoctorID = %s, AppointmentDate = %s, Reason = %s, Status = %s WHERE AppointmentID = %s",
                       (patient_id.get(), doctor_id.get(), appointment_date.get(), reason.get(), status.get(), appointment_id))
        db.commit()
        cursor.close()
        db.close()
        display_appointments(appointments_list)

# Function to delete an appointment
def delete_appointment(appointments_list):
    selected_appointment = appointments_list.curselection()
    if selected_appointment:
        appointment_info = appointments_list.get(selected_appointment)
        appointment_id = int(appointment_info.split(":")[0])  # Extract appointment ID
        db = connect_to_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM Appointments WHERE AppointmentID = %s", (appointment_id,))
        db.commit()
        cursor.close()
        db.close()
        display_appointments(appointments_list)

# Function to select an appointment from the list
def select_appointment(appointments_list, patient_id, doctor_id, appointment_date, reason, status):
    selected_appointment = appointments_list.curselection()
    if selected_appointment:
        appointment_info = appointments_list.get(selected_appointment)
        appointment_id = int(appointment_info.split(":")[0])  # Extract appointment ID
        db = connect_to_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM Appointments WHERE AppointmentID = %s", (appointment_id,))
        appointment = cursor.fetchone()
        cursor.close()
        db.close()

        patient_id.delete(0, tk.END)
        patient_id.insert(0, appointment[1])
        doctor_id.delete(0, tk.END)
        doctor_id.insert(0, appointment[2])
        appointment_date.delete(0, tk.END)
        appointment_date.insert(0, appointment[3].strftime("%Y-%m-%d %H:%M:%S"))
        reason.delete(0, tk.END)
        reason.insert(0, appointment[4])
        status.set(appointment[5])  # Set the status combobox to the appointment's status



# ------------------- PATIENTS PAGE --------------------------


import tkinter as tk
from tkcalendar import DateEntry

def patients_page():
    patients_root = tk.Tk()
    patients_root.title("Patients Management System")
    patients_root.geometry("600x600")  # Set an initial size for the window
    patients_root.configure(bg="#2E2E2E")  # Dark background

    # Create a frame for the form
    form_frame = tk.Frame(patients_root, padx=10, pady=10, bg="#2E2E2E")  # Dark frame
    form_frame.pack(pady=10)

    # Define a function to create labeled entry fields
    def create_labeled_entry(label_text, row):
        label = tk.Label(form_frame, text=label_text, bg="#2E2E2E", fg="white")  # White text
        label.grid(row=row, column=0, sticky="w", padx=5, pady=5)
        entry = tk.Entry(form_frame, width=40, bg="#3E3E3E", fg="white")  # Dark entry background with white text
        entry.grid(row=row, column=1, padx=5, pady=5)
        return entry

    # Create entry fields with labels
    entry_first_name = create_labeled_entry("First Name:", 0)
    entry_last_name = create_labeled_entry("Last Name:", 1)
    entry_dob = create_labeled_entry("DOB:", 2)
    entry_gender = create_labeled_entry("Gender (M/F/Other):", 3)
    entry_phone = create_labeled_entry("Phone:", 4)
    entry_email = create_labeled_entry("Email:", 5)
    entry_address = create_labeled_entry("Address:", 6)
    entry_emergency_contact = create_labeled_entry("Emergency Contact:", 7)
    entry_insurance_provider = create_labeled_entry("Insurance Provider:", 8)
    entry_policy_number = create_labeled_entry("Policy Number:", 9)
    entry_coverage_amount = create_labeled_entry("Coverage Amount:", 10)
    entry_insurance_expiry = create_labeled_entry("Insurance Expiry:", 11)

    # Create DateEntry for DOB and Insurance Expiry
    entry_dob = DateEntry(form_frame, date_pattern='yyyy-mm-dd', width=37, background="#3E3E3E", foreground="white", borderwidth=2)
    entry_dob.grid(row=2, column=1, padx=5, pady=5)
    
    entry_insurance_expiry = DateEntry(form_frame, date_pattern='yyyy-mm-dd', width=37, background="#3E3E3E", foreground="white", borderwidth=2)
    entry_insurance_expiry.grid(row=11, column=1, padx=5, pady=5)

    # Buttons frame
    button_frame = tk.Frame(patients_root, bg="#2E2E2E")  # Dark button frame
    button_frame.pack(pady=10)

    button_add = tk.Button(button_frame, text="Add Patient", command=lambda: insert_patient(
        entry_first_name, entry_last_name, entry_dob, entry_gender, entry_phone, entry_email, entry_address, entry_emergency_contact,
        entry_insurance_provider, entry_policy_number, entry_coverage_amount, entry_insurance_expiry, patients_list),
        width=15, bg="#4CAF50", fg="white")  # Green button
    button_add.grid(row=0, column=0, padx=10, pady=10)

    button_update = tk.Button(button_frame, text="Update Patient", command=lambda: update_patient(
        entry_first_name, entry_last_name, entry_dob, entry_gender, entry_phone, entry_email, entry_address, entry_emergency_contact,
        entry_insurance_provider, entry_policy_number, entry_coverage_amount, entry_insurance_expiry, patients_list),
        width=15, bg="#2196F3", fg="white")  # Blue button
    button_update.grid(row=0, column=1, padx=10, pady=10)

    button_delete = tk.Button(button_frame, text="Delete Patient", command=lambda: delete_patient(patients_list),
        width=15, bg="#f44336", fg="white")  # Red button
    button_delete.grid(row=0, column=2, padx=10, pady=10)

    # Listbox for patients
    patients_list = tk.Listbox(patients_root, height=10, width=80, bg="#3E3E3E", fg="white")  # Dark listbox
    patients_list.pack(pady=10)
    patients_list.bind('<<ListboxSelect>>', lambda event: select_patient(
        patients_list, entry_first_name, entry_last_name, entry_dob, entry_gender, entry_phone, entry_email, entry_address, entry_emergency_contact,
        entry_insurance_provider, entry_policy_number, entry_coverage_amount, entry_insurance_expiry))

    display_patients(patients_list)

    patients_root.mainloop()


# Function to display patients in the list
def display_patients(patients_list):
    db = connect_to_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Patients")
    patients = cursor.fetchall()
    patients_list.delete(0, tk.END)
    for patient in patients:
        patients_list.insert(tk.END, f"{patient[0]}: {patient[1]} {patient[2]}, {patient[3]} - {patient[4]}")

    cursor.close()
    db.close()

# Function to insert a new patient
def insert_patient(first_name, last_name, dob, gender, phone, email, address, emergency_contact,
                   insurance_provider, policy_number, coverage_amount, insurance_expiry, patients_list):
    db = connect_to_db()
    cursor = db.cursor()
    new_id=get_next_id("PatientID",cursor , "Patients")
    cursor.execute("INSERT INTO Patients (PatientID,FirstName, LastName, DOB, Gender, Phone, Email, Address, EmergencyContact, InsuranceProvider, PolicyNumber, CoverageAmount, InsuranceExpiry) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                   (new_id, first_name.get(), last_name.get(), dob.get(), gender.get(), phone.get(), email.get(),
                    address.get(), emergency_contact.get(), insurance_provider.get(), policy_number.get(),
                    coverage_amount.get(), insurance_expiry.get()))
    db.commit()
    cursor.close()
    db.close()
    display_patients(patients_list)

# Function to update an existing patient
def update_patient(first_name, last_name, dob, gender, phone, email, address, emergency_contact,
                   insurance_provider, policy_number, coverage_amount, insurance_expiry, patients_list):
    selected_patient = patients_list.curselection()  # Get selected patient from listbox
    if selected_patient:
        # Extract the PatientID from the selected list item (assuming it contains the PatientID)
        patient_info = patients_list.get(selected_patient)
        patient_id = int(patient_info.split(":")[0])  # Assuming format like "PatientID: Patient Name"

        # Update the patient's information in the database
        try:
            db = connect_to_db()  # Connect to the database
            cursor = db.cursor()

            # SQL query to update patient details
            cursor.execute("""
                UPDATE Patients 
                SET FirstName = %s, LastName = %s, DOB = %s, Gender = %s, Phone = %s, Email = %s,
                    Address = %s, EmergencyContact = %s, InsuranceProvider = %s, PolicyNumber = %s,
                    CoverageAmount = %s, InsuranceExpiry = %s
                WHERE PatientID = %s
            """, (first_name.get(), last_name.get(), dob.get(), gender.get(), phone.get(), email.get(), 
                  address.get(), emergency_contact.get(), insurance_provider.get(), policy_number.get(), 
                  coverage_amount.get(), insurance_expiry.get(), patient_id))

            db.commit()  # Commit the changes
            cursor.close()  # Close the cursor
            db.close()  # Close the database connection

            # Refresh the list to reflect the updated details
            display_patients(patients_list)

        except Exception as e:
            # Handle any errors that occur during the update
            messagebox.showerror("Error", f"An error occurred: {str(e)}")


# Function to delete a patient
def delete_patient(patients_list):
    selected_patient = patients_list.curselection()
    if selected_patient:
        patient_info = patients_list.get(selected_patient)
        patient_id = int(patient_info.split(":")[0])  # Extract patient ID
        db = connect_to_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM Patients WHERE PatientID = %s", (patient_id,))
        db.commit()
        cursor.close()
        db.close()
        display_patients(patients_list)

# Function to select a patient from the list
def select_patient(patients_list, first_name, last_name, dob, gender, phone, email, address, emergency_contact,
                   insurance_provider, policy_number, coverage_amount, insurance_expiry):
    selected_patient = patients_list.curselection()
    if selected_patient:
        patient_info = patients_list.get(selected_patient)
        patient_id = int(patient_info.split(":")[0])  # Extract patient ID
        db = connect_to_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM Patients WHERE PatientID = %s", (patient_id,))
        patient = cursor.fetchone()
        cursor.close()
        db.close()

        first_name.delete(0, tk.END)
        first_name.insert(0, patient[1])
        last_name.delete(0, tk.END)
        last_name.insert(0, patient[2])
        dob.delete(0, tk.END)
        dob.insert(0, patient[3])  # Insert DOB into DateEntry
        gender.delete(0, tk.END)
        gender.insert(0, patient[4])
        phone.delete(0, tk.END)
        phone.insert(0, patient[5])
        email.delete(0, tk.END)
        email.insert(0, patient[6])
        address.delete(0, tk.END)
        address.insert(0, patient[7])
        emergency_contact.delete(0, tk.END)
        emergency_contact.insert(0, patient[8])
        insurance_provider.delete(0, tk.END)
        insurance_provider.insert(0, patient[9])
        policy_number.delete(0, tk.END)
        policy_number.insert(0, patient[10])
        coverage_amount.delete(0, tk.END)
        coverage_amount.insert(0, patient[11])
        insurance_expiry.delete(0, tk.END)
        insurance_expiry.insert(0, patient[12])

# ------------------- APPOINTMENTS PAGE --------------------------


# ------------------- MEDICAL HISTORY & PRESCRIPTIONS PAGE --------------------------
import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

def medical_history_page():
    medical_history_root = tk.Tk()
    medical_history_root.title("Medical History & Prescriptions Management System")
    medical_history_root.geometry("1080x750")
    medical_history_root.configure(bg="#2E2E2E")  # Dark background

    label_title = tk.Label(medical_history_root, text="Manage Medical History & Prescriptions", font=("Helvetica", 18, "bold"), bg="#2E2E2E", fg="white")
    label_title.grid(row=0, column=1, pady=20)

    # Create a frame for entry fields
    frame_entries = tk.Frame(medical_history_root, bg="#2E2E2E")
    frame_entries.grid(row=1, column=0, columnspan=3, padx=20, pady=10)

    # Entry fields for medical history details
    labels = [
        "Patient ID:", "Doctor ID:", "Condition:", "Start Date:", "End Date:",
        "Medication Name:", "Dosage:", "Instructions:", "Lab Test Name:",
        "Lab Test Date:", "Lab Test Results:", "Notes:"
    ]
    
    entries = []
    
    for i, label_text in enumerate(labels):
        label = tk.Label(frame_entries, text=label_text, bg="#2E2E2E", fg="white", font=("Helvetica", 12))  # White text
        label.grid(row=i, column=0, padx=10, pady=5)
        
        if "Date" in label_text:
            entry = DateEntry(frame_entries, date_pattern='yyyy-mm-dd', font=("Helvetica", 12), background="#3E3E3E", foreground="white", borderwidth=2)  # Dark DateEntry
        else:
            entry = tk.Entry(frame_entries, font=("Helvetica", 12), bg="#3E3E3E", fg="white")  # Dark entry background with white text
        
        entry.grid(row=i, column=1, padx=10, pady=5)
        entries.append(entry)

    (entry_patient_id, entry_doctor_id, entry_condition, entry_start_date, 
     entry_end_date, entry_medication_name, entry_dosage, entry_instructions, 
     entry_lab_test_name, entry_lab_test_date, entry_lab_test_results, entry_notes) = entries

    # Create a frame for buttons
    frame_buttons = tk.Frame(medical_history_root, bg="#2E2E2E")  # Dark button frame
    frame_buttons.grid(row=13, column=0, columnspan=3, pady=10)

    button_add = tk.Button(frame_buttons, text="Add Record", command=lambda: insert_medical_history(
        entry_patient_id, entry_doctor_id, entry_condition, entry_start_date, entry_end_date, entry_medication_name,
        entry_dosage, entry_instructions, entry_lab_test_name, entry_lab_test_date, entry_lab_test_results,
        entry_notes, medical_history_list), font=("Helvetica", 12), bg="#4CAF50", fg="white")  # Green button
    button_add.grid(row=0, column=0, padx=10)

    button_update = tk.Button(frame_buttons, text="Update Record", command=lambda: update_medical_history(
        entry_patient_id, entry_doctor_id, entry_condition, entry_start_date, entry_end_date, entry_medication_name,
        entry_dosage, entry_instructions, entry_lab_test_name, entry_lab_test_date, entry_lab_test_results,
        entry_notes, medical_history_list), font=("Helvetica", 12), bg="#2196F3", fg="white")  # Blue button
    button_update.grid(row=0, column=1, padx=10)

    button_delete = tk.Button(frame_buttons, text="Delete Record", command=lambda: delete_medical_history(medical_history_list), 
        font=("Helvetica", 12), bg="#f44336", fg="white")  # Red button
    button_delete.grid(row=0, column=2, padx=10)

    medical_history_list = tk.Listbox(medical_history_root, height=8, width=116, font=("Helvetica", 12), bg="#3E3E3E", fg="white")  # Dark listbox
    medical_history_list.grid(row=14, column=0, columnspan=3, padx=10, pady=10)

    medical_history_list.bind('<<ListboxSelect>>', lambda event: select_medical_history(medical_history_list,
        entry_patient_id, entry_doctor_id, entry_condition, entry_start_date, entry_end_date,
        entry_medication_name, entry_dosage, entry_instructions, entry_lab_test_name, entry_lab_test_date,
        entry_lab_test_results, entry_notes))

    display_medical_history(medical_history_list)
    medical_history_root.mainloop()

# Function to display medical history records in the list
def display_medical_history(medical_history_list):
    db = connect_to_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM medicalhistoryprescriptions")  # Updated table name
    records = cursor.fetchall()
    medical_history_list.delete(0, tk.END)
    for record in records:
        medical_history_list.insert(tk.END, f"{record[0]}: Patient {record[1]}, Doctor {record[2]}, Condition: {record[3]}, "
                                             f"Start: {record[4]}, End: {record[5]}, Medication: {record[6]}, "
                                             f"Dosage: {record[7]}, Lab Test: {record[8]}, Test Date: {record[9]}")

    cursor.close()
    db.close()

# Function to insert a new medical history record
def insert_medical_history(patient_id, doctor_id, condition, start_date, end_date, medication_name,
                           dosage, instructions, lab_test_name, lab_test_date, lab_test_results, notes, medical_history_list):
    db = connect_to_db()
    cursor = db.cursor()
    new_id=get_next_id("RecordID",cursor , "medicalhistoryprescriptions")
    cursor.execute(
        "INSERT INTO medicalhistoryprescriptions (RecordID, PatientID, DoctorID, Conditn, StartDate, EndDate, MedicationName, Dosage, Instructions, LabTestName, LabTestDate, LabTestResults, Notes) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
        (new_id, patient_id.get(), doctor_id.get(), condition.get(), start_date.get(), end_date.get(),
         medication_name.get(), dosage.get(), instructions.get(), lab_test_name.get(), lab_test_date.get(),
         lab_test_results.get(), notes.get()))
    db.commit()
    cursor.close()
    db.close()
    display_medical_history(medical_history_list)

# Function to update an existing medical history record
def update_medical_history(patient_id, doctor_id, condition, start_date, end_date, medication_name,
                           dosage, instructions, lab_test_name, lab_test_date, lab_test_results, notes, medical_history_list):
    selected_record = medical_history_list.curselection()
    if selected_record:
        record_info = medical_history_list.get(selected_record)
        record_id = int(record_info.split(":")[0])  # Extract record ID
        db = connect_to_db()
        cursor = db.cursor()
        cursor.execute(
            "UPDATE medicalhistoryprescriptions SET PatientID = %s, DoctorID = %s, Conditn = %s, StartDate = %s, EndDate = %s, "
            "MedicationName = %s, Dosage = %s, Instructions = %s, LabTestName = %s, LabTestDate = %s, LabTestResults = %s, Notes = %s WHERE RecordID = %s",
            (patient_id.get(), doctor_id.get(), condition.get(), start_date.get(), end_date.get(),
             medication_name.get(), dosage.get(), instructions.get(), lab_test_name.get(), lab_test_date.get(),
             lab_test_results.get(), notes.get(), record_id)
        )
        db.commit()
        cursor.close()
        db.close()
        display_medical_history(medical_history_list)

# Function to delete a medical history record
def delete_medical_history(medical_history_list):
    selected_record = medical_history_list.curselection()
    if selected_record:
        record_info = medical_history_list.get(selected_record)
        record_id = int(record_info.split(":")[0])  # Extract record ID
        db = connect_to_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM medicalhistoryprescriptions WHERE RecordID = %s", (record_id,))
        db.commit()
        cursor.close()
        db.close()
        display_medical_history(medical_history_list)

# Function to select a medical history record from the list
def select_medical_history(medical_history_list, patient_id, doctor_id, condition, start_date, end_date,
                           medication_name, dosage, instructions, lab_test_name, lab_test_date, lab_test_results, notes):
    selected_record = medical_history_list.curselection()
    if selected_record:
        record_info = medical_history_list.get(selected_record)
        record_id = int(record_info.split(":")[0])  # Extract record ID
        db = connect_to_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM medicalhistoryprescriptions WHERE RecordID = %s", (record_id,))
        record = cursor.fetchone()
        cursor.close()
        db.close()

        patient_id.delete(0, tk.END)
        patient_id.insert(0, record[1])
        doctor_id.delete(0, tk.END)
        doctor_id.insert(0, record[2])
        condition.delete(0, tk.END)
        condition.insert(0, record[3])
        start_date.delete(0, tk.END)
        start_date.insert(0, record[4].strftime("%Y-%m-%d"))

        # Check if end_date is not None before formatting
        if record[5] is not None:
            end_date.delete(0, tk.END)
            end_date.insert(0, record[5].strftime("%Y-%m-%d"))
        else:
            end_date.delete(0, tk.END)  # Clear the entry if EndDate is None

        # Populate new fields
        medication_name.delete(0, tk.END)
        medication_name.insert(0, record[6])
        dosage.delete(0, tk.END)
        dosage.insert(0, record[7])
        instructions.delete(0, tk.END)
        instructions.insert(0, record[8])
        lab_test_name.delete(0, tk.END)
        lab_test_name.insert(0, record[9])

        # Check if lab_test_date is not None before formatting
        if record[10] is not None:
            lab_test_date.delete(0, tk.END)
            lab_test_date.insert(0, record[10].strftime("%Y-%m-%d"))
        else:
            lab_test_date.delete(0, tk.END)

        lab_test_results.delete(0, tk.END)
        lab_test_results.insert(0, record[11])
        notes.delete(0, tk.END)
        notes.insert(0, record[12])



# ------------------- BILLING PAGE --------------------------

import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

def billing_page():
    billing_root = tk.Tk()
    billing_root.title("Billing Management System")
    billing_root.geometry("800x500")
    billing_root.configure(bg="#2E2E2E")  # Dark background

    label_title = tk.Label(billing_root, text="Manage Billing", font=("Helvetica", 18, "bold"), bg="#2E2E2E", fg="white")
    label_title.grid(row=0, column=1, pady=20)

    # Create a frame for entry fields
    frame_entries = tk.Frame(billing_root, bg="#2E2E2E")
    frame_entries.grid(row=1, column=0, columnspan=3, padx=20, pady=10)

    # Entry fields for billing details
    labels = [
        "Patient ID:", "Appointment ID:", "Amount:", "Billing Date:", "Status:"
    ]
    
    entries = []
    
    for i, label_text in enumerate(labels):
        label = tk.Label(frame_entries, text=label_text, bg="#2E2E2E", fg="white", font=("Helvetica", 12))  # White text
        label.grid(row=i, column=0, padx=10, pady=5)
        
        if "Date" in label_text:
            entry = DateEntry(frame_entries, width=12, background="#3E3E3E",
                              foreground="white", borderwidth=2, date_pattern='yyyy-mm-dd', font=("Helvetica", 12))  # Dark DateEntry
        else:
            entry = tk.Entry(frame_entries, font=("Helvetica", 12), bg="#3E3E3E", fg="white")  # Dark entry background
        
        entry.grid(row=i, column=1, padx=10, pady=5)
        entries.append(entry)

    (entry_patient_id, entry_appointment_id, entry_amount, entry_billing_date, entry_status) = entries

    # Create a frame for buttons
    frame_buttons = tk.Frame(billing_root, bg="#2E2E2E")  # Dark button frame
    frame_buttons.grid(row=6, column=0, columnspan=3, pady=10)

    button_add = tk.Button(frame_buttons, text="Add Bill", command=lambda: insert_billing(
        entry_patient_id, entry_appointment_id, entry_amount, entry_billing_date, entry_status, billing_list), 
        font=("Helvetica", 12), bg="#4CAF50", fg="white")  # Green button
    button_add.grid(row=0, column=0, padx=10)

    button_update = tk.Button(frame_buttons, text="Update Bill", command=lambda: update_billing(
        entry_patient_id, entry_appointment_id, entry_amount, entry_billing_date, entry_status, billing_list), 
        font=("Helvetica", 12), bg="#2196F3", fg="white")  # Blue button
    button_update.grid(row=0, column=1, padx=10)

    button_delete = tk.Button(frame_buttons, text="Delete Bill", command=lambda: delete_billing(billing_list), 
        font=("Helvetica", 12), bg="#f44336", fg="white")  # Red button
    button_delete.grid(row=0, column=2, padx=10)

    billing_list = tk.Listbox(billing_root, height=8, width=80, font=("Helvetica", 12), bg="#3E3E3E", fg="white")  # Dark listbox
    billing_list.grid(row=7, column=0, columnspan=3, padx=20, pady=10)

    billing_list.bind('<<ListboxSelect>>', lambda event: select_billing(billing_list,
        entry_patient_id, entry_appointment_id, entry_amount, entry_billing_date, entry_status))

    display_billing(billing_list)
    billing_root.mainloop()

# Function to display billing records in the list
def display_billing(billing_list):
    db = connect_to_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Billing")
    records = cursor.fetchall()
    billing_list.delete(0, tk.END)
    for record in records:
        billing_list.insert(tk.END, f"{record[0]}: Patient {record[1]}, Appointment {record[2]}, Amount: {record[3]}, Date: {record[4]}, Status: {record[5]}")

    cursor.close()
    db.close()

# Function to insert a new billing record
def insert_billing(patient_id, appointment_id, amount, billing_date, status, billing_list):
    try:
        db = connect_to_db()
        cursor = db.cursor()
        new_id=get_next_id("BillingID",cursor , "Billing")
        cursor.execute("INSERT INTO Billing (BillingID, PatientID, AppointmentID, Amount, BillingDate, Status) VALUES (%s, %s, %s, %s, %s, %s)",
                       (new_id, patient_id.get(), appointment_id.get(), amount.get(), billing_date.get(), status.get()))
        db.commit()
        cursor.close()
        db.close()
        display_billing(billing_list)
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to update an existing billing record
def update_billing(patient_id, appointment_id, amount, billing_date, status, billing_list):
    selected_bill = billing_list.curselection()
    if selected_bill:
        bill_info = billing_list.get(selected_bill)
        bill_id = int(bill_info.split(":")[0])  # Extract bill ID
        
        # Update database
        try:
            db = connect_to_db()
            cursor = db.cursor()
            print(f"Updating Status to: {status.get()}")
            print(status.get())
            if(status.get()=='Paid'):
                cursor.execute("""
                UPDATE Billing 
                SET PatientID = %s, AppointmentID = %s, Amount = %s, BillingDate = %s, Status = 'Paid' 
                WHERE BillingID = %s
                """, (patient_id.get(), appointment_id.get(), amount.get(), billing_date.get(), bill_id))
            else:
                cursor.execute("""
                UPDATE Billing 
                SET PatientID = %s, AppointmentID = %s, Amount = %s, BillingDate = %s, Status = 'Pending' 
                WHERE BillingID = %s
                """, (patient_id.get(), appointment_id.get(), amount.get(), billing_date.get(), bill_id))


            
            # Check if the update was successful
            if cursor.rowcount == 0:
                print("No records updated. Check if the BillingID is correct.")
            else:
                print(f"Successfully updated BillingID {bill_id}.")

            db.commit()
            cursor.close()
            db.close()
            display_billing(billing_list)  # Refresh the list
        except Exception as e:
            messagebox.showerror("Error", str(e))

# Function to select a billing record from the list
def select_billing(billing_list, patient_id, appointment_id, amount, billing_date, status):
    selected_bill = billing_list.curselection()
    if selected_bill:
        bill_info = billing_list.get(selected_bill)
        bill_id = int(bill_info.split(":")[0])  # Extract bill ID
        db = connect_to_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM Billing WHERE BillingID = %s", (bill_id,))
        record = cursor.fetchone()
        cursor.close()
        db.close()

        # Make sure to set values based on record fetched
        patient_id.delete(0, tk.END)
        patient_id.insert(0, record[1])
        appointment_id.delete(0, tk.END)
        appointment_id.insert(0, record[2])
        amount.delete(0, tk.END)
        amount.insert(0, record[3])
        billing_date.set_date(record[4])  # Set date using DateEntry
        status.delete(0, tk.END)
        status.insert(0, record[5])




# Function to delete a billing record
def delete_billing(billing_list):
    selected_bill = billing_list.curselection()
    if selected_bill:
        bill_info = billing_list.get(selected_bill)
        bill_id = int(bill_info.split(":")[0])  # Extract bill ID
        db = connect_to_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM Billing WHERE BillingID = %s", (bill_id,))
        db.commit()
        cursor.close()
        db.close()
        display_billing(billing_list)


# Function to display doctors in the list
def display_doctors(doctors_list):
    db = connect_to_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Doctors")
    doctors = cursor.fetchall()
    doctors_list.delete(0, tk.END)
    for doctor in doctors:
        doctors_list.insert(tk.END, f"{doctor[0]}: {doctor[1]} {doctor[2]}, {doctor[3]} - {doctor[4]}")

    cursor.close()
    db.close()

# Function to insert a new doctor
def insert_doctor(first_name, last_name, specialization, phone, email, doctors_list):
    db = connect_to_db()
    cursor = db.cursor()
    new_id=get_next_id("DoctorID",cursor , "Doctors")
    cursor.execute("INSERT INTO Doctors (DoctorID, FirstName, LastName, Specialization, Phone, Email) VALUES (%s, %s, %s, %s, %s, %s)",
                   (new_id, first_name.get(), last_name.get(), specialization.get(), phone.get(), email.get()))
    db.commit()
    cursor.close()
    db.close()
    display_doctors(doctors_list)

# Function to update an existing doctor
def update_doctor(first_name, last_name, specialization, phone, email, doctors_list):
    selected_doctor = doctors_list.curselection()  # Get selected doctor from listbox
    if selected_doctor:
        # Extract the DoctorID from the selected list item (assuming it contains the DoctorID)
        doctor_info = doctors_list.get(selected_doctor)
        doctor_id = int(doctor_info.split(":")[0])  # Assuming format like "DoctorID: Doctor Name"

        # Update the doctor's information in the database
        try:
            db = connect_to_db()  # Connect to the database
            cursor = db.cursor()

            # SQL query to update doctor details
            cursor.execute("""
                UPDATE Doctors 
                SET FirstName = %s, LastName = %s, Specialization = %s, Phone = %s, Email = %s 
                WHERE DoctorID = %s
            """, (first_name.get(), last_name.get(), specialization.get(), phone.get(), email.get(), doctor_id))

            db.commit()  # Commit the changes
            cursor.close()  # Close the cursor
            db.close()  # Close the database connection

            # Refresh the list to reflect the updated details
            display_doctors(doctors_list)

        except Exception as e:
            # Handle any errors that occur during the update
            messagebox.showerror("Error", f"An error occurred: {str(e)}")


# Function to delete a doctor
def delete_doctor(doctors_list):
    selected_doctor = doctors_list.curselection()
    if selected_doctor:
        doctor_info = doctors_list.get(selected_doctor)
        doctor_id = int(doctor_info.split(":")[0])  # Extract doctor ID
        db = connect_to_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM Doctors WHERE DoctorID = %s", (doctor_id,))
        db.commit()
        cursor.close()
        db.close()
        display_doctors(doctors_list)

# Function to select a doctor from the list
def select_doctor(doctors_list, first_name, last_name, specialization, phone, email):
    selected_doctor = doctors_list.curselection()
    if selected_doctor:
        doctor_info = doctors_list.get(selected_doctor)
        doctor_id = int(doctor_info.split(":")[0])  # Extract doctor ID
        db = connect_to_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM Doctors WHERE DoctorID = %s", (doctor_id,))
        doctor = cursor.fetchone()
        cursor.close()
        db.close()

        first_name.delete(0, tk.END)
        first_name.insert(0, doctor[1])
        last_name.delete(0, tk.END)
        last_name.insert(0, doctor[2])
        specialization.delete(0, tk.END)
        specialization.insert(0, doctor[3])
        phone.delete(0, tk.END)
        phone.insert(0, doctor[4])
        email.delete(0, tk.END)
        email.insert(0, doctor[5])

def get_next_id(id_column, cursor, tablename):
    cursor.execute(f"SELECT MAX({id_column}) FROM {tablename}")  # Replace with your actual table name
    result = cursor.fetchone()
    return (result[0] + 1) if result[0] is not None else 1  # Return 1 if no records exist




# Run the main page
main_page()