import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

# File to store data
DATA_FILE = "expense_data.json"

# Load data from file
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return {"balance": 0, "transactions": []}

# Save data to file
def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

# Add a transaction
def add_transaction(amount, description, transaction_type):
    try:
        amount = float(amount)
        data["balance"] += amount if transaction_type == "Income" else -amount
        data["transactions"].append({
            "type": transaction_type,
            "amount": amount,
            "description": description
        })
        save_data(data)
        update_ui()
        messagebox.showinfo("Success", f"{transaction_type} of ₹{amount} added!")
    except ValueError:
        messagebox.showerror("Error", "Invalid amount. Please enter a number.")

# Update UI
def update_ui():
    balance_label.config(text=f"Current Balance: ₹{data['balance']}")
    for row in transaction_table.get_children():
        transaction_table.delete(row)
    for t in data["transactions"]:
        transaction_table.insert('', tk.END, values=(t["type"], f"₹{t['amount']}", t["description"]))

# GUI Setup
data = load_data()
root = tk.Tk()
root.title("Personal Expense Tracker")
root.geometry("600x400")

# Balance Label
balance_label = tk.Label(root, text=f"Current Balance: ₹{data['balance']}", font=("Helvetica", 16))
balance_label.pack(pady=10)

# Transaction Table
transaction_table = ttk.Treeview(root, columns=("Type", "Amount", "Description"), show="headings", height=10)
transaction_table.heading("Type", text="Type")
transaction_table.heading("Amount", text="Amount")
transaction_table.heading("Description", text="Description")
transaction_table.pack(pady=10)

# Entry Fields and Buttons
frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Amount:").grid(row=0, column=0, padx=5)
amount_entry = tk.Entry(frame)
amount_entry.grid(row=0, column=1, padx=5)

tk.Label(frame, text="Description:").grid(row=1, column=0, padx=5)
description_entry = tk.Entry(frame)
description_entry.grid(row=1, column=1, padx=5)

income_button = tk.Button(frame, text="Add Income", command=lambda: add_transaction(amount_entry.get(), description_entry.get(), "Income"))
income_button.grid(row=2, column=0, pady=10, padx=5)

expense_button = tk.Button(frame, text="Add Expense", command=lambda: add_transaction(amount_entry.get(), description_entry.get(), "Expense"))
expense_button.grid(row=2, column=1, pady=10, padx=5)

# Initialize UI
update_ui()

# Run the application
root.mainloop()
