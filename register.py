import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

pet_health_data = []
global selected_index
selected_index = None

def register_pet_health():
    accepted = accept_var.get()
    if accepted=="Accepted":
            #Owner Info
            name = entry_name.get()
            phone_no = entry_phone.get()
            email = entry_email.get()
            #Pet Info
            pet_name = entry_petname.get()
            species = entry_species.get()
            breed = entry_breed.get()
            gender = combobox_gender.get()
            age = entry_age.get()
            #Pet Health Information
            vaccine_name = entry_vaccinations.get()
            vaccine_date = entry_date_vaccinations.get()
            allergy = entry_allergies.get()
            medication_name = entry_medications.get()
            frequency = combobox_medications.get()
            
            if name and phone_no and email and pet_name and species and breed and gender and age and vaccine_name and vaccine_date and allergy and medication_name and frequency:
                print("Name:", name, "Phone Number:", phone_no, "Email:", email)
                print("Petname:", pet_name, "Species:", species, "Breed:", breed)
                print("Gender:", gender, "Age:", age)
                print("Vaccine Name:", vaccine_name, "Vaccine Date:", vaccine_date, "Allergy:", allergy)
                print("Medication Name:", medication_name, "Frequency:", frequency)
                print("..............................................................")

                # Store the data in the dictionary using the student number as the key
                pet_health_data.append({
                    "Name": name,
                    "Phone Number": phone_no,
                    "Email": email,
                    "Petname" :pet_name, 
                    "Species": species, 
                    "Age": age,
                    "Breed": breed, 
                    "Gender": gender,
                    "Vaccine name": vaccine_name, 
                    "Vaccine date": vaccine_date,
                    "Allergy": allergy, 
                    "Medication_name": medication_name, 
                    "Frequency": frequency
                })

                update_listbox_entry()
                messagebox.showinfo(title="Success", message="Registration Successfull")
            else:
                messagebox.showwarning(title="Warning", message="Please fill all the information.")    
    else:
        messagebox.showwarning(title="Error", message="You should accept the terms and conditions.")

#Delete Operation
def delete_registration():
    global selected_index
    selected_indices = pet_health_listbox.curselection()
    if selected_indices:
        del pet_health_data[selected_indices[0]]
        update_listbox_entry()
        print("Record deleted successfully")
        selected_index = None
        messagebox.showinfo(title="Successful", message="Deletion Successfull")
    else:
        messagebox.showwarning(title="Warning", message="Please select a record for deletion")

#Update operation
def update_listbox_entry():
    pet_health_listbox.delete(0, tk.END)
    for i, pet in enumerate(pet_health_data):
        info = (
            f"Registration {i + 1}:"
            f"Name: {pet['Name']} | Phone Number: {pet['Phone Number']} | Email: {pet['Email']}"
            f"Petname: {pet['Petname']} | Species: {pet['Species']} | Breed: {pet['Breed']} | Gender: {pet['Gender']} | Age: {pet['Age']}"
            f"Vaccine Name: {pet['Vaccine name']} | Vaccine Date: {pet['Vaccine date']} | Allergy: {pet['Allergy']} | Medication Name: {pet['Medication_name']} | Frequency: {pet['Frequency']}"
        )
        pet_health_listbox.insert(tk.END, info)

#Edit Operation
def edit_registration():
    global selected_index
    if selected_index is not None and 0 <= selected_index < len(pet_health_data):
        selected_data = pet_health_data[selected_index]

        selected_data["Name"] = entry_name.get()
        selected_data["Phone Number"] = entry_phone.get()
        selected_data["Email"] = entry_email.get()
        selected_data["Petname"] = entry_petname.get()
        selected_data["Species"] = entry_species.get()
        selected_data["Breed"] = entry_breed.get()
        selected_data["Gender"] = combobox_gender.get() if combobox_gender.get() else ""
        selected_data["Age"] = entry_age.get()
        selected_data["Vaccine Name"] = entry_vaccinations.get()
        selected_data["Vaccine Date"] = entry_date_vaccinations.get()
        selected_data["Allergy"] = entry_allergies.get()
        selected_data["Medication Name"] = entry_medications.get()
        selected_data["Frequency"] = combobox_medications.get() if combobox_medications.get() else ""

        update_listbox_entry()
        messagebox.showinfo(title="Success", message="Data successfully updated.")
    else:
        messagebox.showwarning(title="Warning", message="Please select a valid record for editing")

        

def on_select(event):
    global selected_index
    widget = event.widget
    selected_indices = widget.curselection()

    if selected_indices:
        selected_index = selected_indices[0]
        display_selected_record(selected_index)
    else:
        selected_index = None

def display_selected_record(index):
    if 0<= index < len(pet_health_data):
        selected_data = pet_health_data[index]
    
        entry_name.delete(0, tk.END)
        entry_name.insert(0, selected_data["Name"])

        entry_phone.delete(0, tk.END)
        entry_phone.insert(0, selected_data["Phone Number"])

        entry_email.delete(0, tk.END)
        entry_email.insert(0, selected_data["Email"])

        entry_species.delete(0, tk.END)
        entry_species.insert(0, selected_data["Species"])

        entry_age.delete(0, tk.END)
        entry_age.insert(0, selected_data["Age"])

        entry_breed.delete(0, tk.END)
        entry_breed.insert(0, selected_data["Breed"])

        combobox_gender.set(selected_data["Gender"])

        entry_vaccinations.delete(0, tk.END)
        entry_vaccinations.insert(0, selected_data["Vaccine Name"])

        entry_date_vaccinations.delete(0, tk.END)
        entry_date_vaccinations.insert(0, selected_data["Vaccine Date"])

        entry_allergies.delete(0, tk.END)
        entry_allergies.insert(0, selected_data["Allergy"])

        entry_medications.delete(0, tk.END)
        entry_medications.insert(0, selected_data["Medication Name"])

        combobox_medications.set(selected_data["Frequency"])
    

        
window = tk.Tk()
window.title("Pet Health Registration")

frame = tk.Frame(window)
frame.pack()

#Saving Owner Info
owner_info_frame = tk.LabelFrame(frame, text= "Owner Pet Information", font=("Arial", 15, "bold"))
owner_info_frame.grid(row=0, column=0, padx=20, pady=20)

label_name = tk.Label(owner_info_frame, text="Full Name:", font=("Arial", 10))
entry_name = tk.Entry(owner_info_frame)
label_name.grid(row=0, column=0)
entry_name.grid(row=1, column=0)

label_phone = tk.Label(owner_info_frame, text="Phone Number:", font=("Arial", 10))
entry_phone = tk.Entry(owner_info_frame)
label_phone.grid(row=0, column=1)
entry_phone.grid(row=1, column=1 )

label_email = tk.Label(owner_info_frame, text="Email",font=("Arial", 10))
entry_email = tk.Entry(owner_info_frame)
label_email.grid(row=0, column=2)
entry_email.grid(row=1, column=2)


#Saving Pet info
pet_info_frame = tk.LabelFrame(frame, text= "Pet Information", font=("Arial", 15, "bold"))
pet_info_frame.grid(row=1, column=0, padx=20, pady=20)

label_petname = tk.Label(pet_info_frame, text="Petname:", font=("Arial", 10) )
entry_petname = tk.Entry(pet_info_frame)
label_petname.grid(row=1, column=0)
entry_petname.grid(row=2, column=0)

label_species = tk.Label(pet_info_frame, text="Species:", font=("Arial", 10))
entry_species = tk.Entry(pet_info_frame)
label_species.grid(row=1, column=1)
entry_species.grid(row=2,column=1)

label_breed = tk.Label(pet_info_frame, text="Breed:", font=("Arial", 10))
entry_breed = tk.Entry(pet_info_frame)
label_breed.grid(row=1, column=2)
entry_breed.grid(row=2,column=2)

label_gender = tk.Label(pet_info_frame, text="Gender:", font=("Arial", 10))
combobox_gender = ttk.Combobox(pet_info_frame, value=["Female", "Male"], font=("Arial", 9))
label_gender.grid(row=4, column=0)
combobox_gender.grid(row=5, column=0)

label_age = tk.Label(pet_info_frame, text="Age:", font=("Arial", 10) )
entry_age = tk.Entry(pet_info_frame)
label_age.grid(row=4, column=1)
entry_age.grid(row=5, column=1)

#Pet Health Information

pet_health_frame = tk.LabelFrame(frame, text= "Pet Health Information", font=("Arial", 15, "bold"))
pet_health_frame.grid(row=7, column=0, padx=20, pady=20)

label_vaccinations = tk.Label(pet_health_frame, text="Vaccine Name:", font=("Arial", 10))
entry_vaccinations = tk.Entry(pet_health_frame)
label_vaccinations.grid(row=8, column=0)
entry_vaccinations.grid(row=9, column=0)

label_date_vaccinations = tk.Label(pet_health_frame, text="Date of Vaccination (YYYY-MM-DD):", font=("Arial", 10))
entry_date_vaccinations = tk.Entry(pet_health_frame)
label_date_vaccinations.grid(row=8, column=1)
entry_date_vaccinations.grid(row=9, column=1)


label_allergies = tk.Label(pet_health_frame, text="Allergy:", font=("Arial", 10))
entry_allergies = tk.Entry(pet_health_frame)
label_allergies.grid(row=8, column=2)
entry_allergies.grid(row=9, column=2)

label_medications = tk.Label(pet_health_frame, text="Medication Name:", font=("Arial", 10))
entry_medications = tk.Entry(pet_health_frame)
label_medications.grid(row=10, column=0)
entry_medications.grid(row=11, column=0)

label_medications = tk.Label(pet_health_frame, text="Frenquency:", font=("Arial", 10))
combobox_medications = ttk.Combobox(pet_health_frame, value=["", "Daily", "Weekly", "Monthly"], font=("Arial", 10))
label_medications.grid(row=10, column=1)
combobox_medications.grid(row=11, column=1)

#Accept terms
terms_frame = tk.LabelFrame(frame, text="Terms & Conditions", font=("Arial", 15, "bold"))
terms_frame.grid(row=13, column=0, sticky="news", padx=20, pady=20)

accept_var = tk.StringVar(value="Not Accepted")
terms_check = tk.Checkbutton(terms_frame, text= "I accept the terms and conditions.",
                             variable=accept_var, onvalue="Accepted", offvalue="Not Accepted", font=("Arial", 10))
terms_check.grid(row=0, column=0)

 
#Changing the padding for all of the widgets

for widget in owner_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)


for widget in pet_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)


for widget in pet_health_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)


#Sumbit Button
button = tk.Button(frame, text="Submit", command=register_pet_health, font=("Arial", 9, "bold"), bg="white")
button.grid(row=14, column=0, sticky="news", padx=20, pady=20)

#Button Update and Delete
edit_button = tk.Button(frame, text="Update", command=edit_registration, font=("Arial", 9, "bold"), bg="white")
edit_button.grid(row=14, column=1, sticky="N", padx=20, pady=20)

delete_button = tk.Button(frame, text="Delete", command=delete_registration, font=("Arial", 9, "bold"), bg="white")
delete_button.grid(row=14, column=2, sticky="N", padx=20, pady=20)

#Display pet health data in a Listbox
pet_health_listbox = tk.Listbox(frame, selectmode=tk.SINGLE)
pet_health_listbox.grid(row=0, column=1, padx=20, pady=20)
pet_health_listbox.bind("<<ListboxSelected>>", on_select)

update_listbox_entry()

window.mainloop()