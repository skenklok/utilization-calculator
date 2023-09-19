from datetime import date, timedelta
import tkinter as tk
from tkinter import ttk, messagebox

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def calculate_days_needed():
    try:
        current_utilization = float(current_utilization_entry.get())
        target_utilization = float(target_utilization_entry.get())
        current_date_str = current_date_entry.get()
        current_date = date(*map(int, current_date_str.split('-')))
        year = current_date.year
        
        if not (0 <= current_utilization <= 100):
            raise ValueError("Current Utilization must be between 0 and 100.")
            
        if not (0 <= target_utilization <= 100):
            raise ValueError("Target Utilization must be between 0 and 100.")
        
        workdays_per_week = 5
        total_weeks = 52 + is_leap_year(year)  # Add 1 if it's a leap year
        total_workdays = total_weeks * workdays_per_week

        if is_leap_year(year):
            messagebox.showinfo("Leap Year", "This year is a leap year.")

        workdays_passed = workdays_per_week * ((current_date - date(year, 1, 1)).days // 7) + min(workdays_per_week, (current_date - date(year, 1, 1)).days % 7)
        workdays_remaining = total_workdays - workdays_passed
        billable_days_ytd = (workdays_passed * current_utilization) / 100
        billable_days_needed = (total_workdays * target_utilization) / 100
        additional_billable_days_needed = round(billable_days_needed - billable_days_ytd)

        additional_days_label.config(text=f"Additional Billable Days Needed: {additional_billable_days_needed}")
        remaining_days_label.config(text=f"Workdays Remaining in the Year: {workdays_remaining}")

    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))

# Create the main window
root = tk.Tk()
root.title("Utilization Calculator")

# Create labels and entries for inputs
ttk.Label(root, text="Current Utilization (%)").grid(row=0, column=0)
current_utilization_entry = ttk.Entry(root)
current_utilization_entry.grid(row=0, column=1)

ttk.Label(root, text="Target Utilization (%)").grid(row=1, column=0)
target_utilization_entry = ttk.Entry(root)
target_utilization_entry.grid(row=1, column=1)

ttk.Label(root, text="Current Date (YYYY-MM-DD)").grid(row=2, column=0)
current_date_entry = ttk.Entry(root)
current_date_entry.grid(row=2, column=1)

# Create a button to perform the calculation
calculate_button = ttk.Button(root, text="Calculate", command=calculate_days_needed)
calculate_button.grid(row=4, columnspan=2)

# Create labels to display the results
additional_days_label = ttk.Label(root, text="Additional Billable Days Needed:")
additional_days_label.grid(row=5, columnspan=2)

remaining_days_label = ttk.Label(root, text="Workdays Remaining in the Year:")
remaining_days_label.grid(row=6, columnspan=2)

# Run the Tkinter event loop
root.mainloop()
