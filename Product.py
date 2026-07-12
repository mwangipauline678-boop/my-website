
class Product:
    def __init__(self, product_code, product_name, quantity, unit_price):
        self.product_code = product_code
        self.product_name = product_name
        self.quantity = quantity
        self.unit_price = unit_price

    def calculate_total_value(self):
        return self.quantity * self.unit_price

    def display_product_details(self):
        print("\n--- PRODUCT DETAILS ---")
        print("Product Code:", self.product_code)
        print("Product Name:", self.product_name)
        print("Quantity:", self.quantity)
        print("Unit Price:", self.unit_price)
        print("Total Value:", self.calculate_total_value())

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity
        print("Quantity Updated Successfully!")


# Main Program
product_code = input("Enter Product Code: ")
product_name = input("Enter Product Name: ")
quantity = int(input("Enter Quantity: "))
unit_price = float(input("Enter Unit Price: "))

product = Product(product_code, product_name, quantity, unit_price)

product.display_product_details()

new_quantity = int(input("\nEnter New Quantity: "))
product.update_quantity(new_quantity)

product.display_product_details()

# Function to calculate gross salary
def calculate_gross_salary(basic_salary):
    house_allowance = 8000
    medical_allowance = 5000
    gross_salary = basic_salary + house_allowance + medical_allowance
    return gross_salary

# Function to calculate deductions
def calculate_deductions(gross_salary):
    nhif = gross_salary * 0.02
    nssf = gross_salary * 0.03
    paye = gross_salary * 0.05

    total_deductions = nhif + nssf + paye

    return nhif, nssf, paye, total_deductions

# Function to calculate net salary
def calculate_net_salary(gross_salary, total_deductions):
    return gross_salary - total_deductions

# Function to display payroll report
def display_report(payroll_no, employee_name, basic_salary):
    gross_salary = calculate_gross_salary(basic_salary)

    nhif, nssf, paye, total_deductions = calculate_deductions(gross_salary)

    net_salary = calculate_net_salary(gross_salary, total_deductions)

    print("\n====== PAYROLL REPORT ======")
    print("Payroll Number :", payroll_no)
    print("Employee Name  :", employee_name)
    print("Basic Salary   :", basic_salary)
    print("Gross Salary   :", gross_salary)
    print("NHIF           :", nhif)
    print("NSSF           :", nssf)
    print("PAYE           :", paye)
    print("Total Deduction:", total_deductions)
    print("Net Salary     :", net_salary)

# Main Program
payroll_no = input("Enter Payroll Number: ")
employee_name = input("Enter Employee Name: ")
basic_salary = float(input("Enter Basic Salary: "))

if basic_salary > 0:
    display_report(payroll_no, employee_name, basic_salary)
else:
    print("Invalid Salary!")
