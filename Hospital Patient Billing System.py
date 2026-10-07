# Hospital Patient Billing System

class Patient:
    def __init__(self, name, age, patient_id):
        self.name = name
        self.age = age
        self.patient_id = patient_id
        self.charges = []

    def add_charge(self, item, amount):
        self.charges.append((item, amount))

    def total_bill(self):
        return sum(amount for item, amount in self.charges)

    def discount(self):
        total = self.total_bill()
        return total * 0.10 if total >= 5000 else 0

    def final_bill(self):
        return self.total_bill() - self.discount()

    def display_bill(self):
        print("\n========== HOSPITAL BILL ==========")
        print("Patient ID :", self.patient_id)
        print("Patient    :", self.name)
        print("Age        :", self.age)
        print("-----------------------------------")

        for item, amount in self.charges:
            print(f"{item:<20} ₹{amount:.2f}")

        print("-----------------------------------")
        print(f"Total      : ₹{self.total_bill():.2f}")
        print(f"Discount   : ₹{self.discount():.2f}")
        print(f"Final Bill : ₹{self.final_bill():.2f}")
        print("===================================")


name = input("Enter patient name: ")
age = int(input("Enter patient age: "))
patient_id = input("Enter patient ID: ")

patient = Patient(name, age, patient_id)

print("\nEnter charges")
consultation = float(input("Doctor consultation: ₹"))
medicine = float(input("Medicines: ₹"))
tests = float(input("Lab tests: ₹"))

patient.add_charge("Consultation", consultation)
patient.add_charge("Medicines", medicine)
patient.add_charge("Lab Tests", tests)

patient.display_bill()