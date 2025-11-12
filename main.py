# Smart Expense Tracker with Monthly Summary Report
import json
import time
import calendar
from datetime import datetime, date
JsonF = "expenses.json"
LogF = "app_log.txt"
def log_and_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        run_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")        
        result = func(*args, **kwargs)
        duration = time.time() - start
        with open(LogF, "a") as log:
            log.write(f"{run_time} - {func.__name__} - {duration:.4f}s\n")
        return result
    return wrapper
def load_data():
    try:
        with open(JsonF, "r") as f:
            return json.load(f)
    except:
        return []
def save_data(data):
    with open(JsonF, "w") as f:
        json.dump(data, f)
@log_and_time
def add_expense():
    date_ip = input("Enter date (YYYY-MM-DD) or press Enter for today: ")
    if date_ip.strip() == "":
        exp_date = str(date.today())
    else:
        try:
            exp_date = str(datetime.strptime(date_ip, "%Y-%m-%d").date())
        except:
            print("Invalid date format")
            return  
    category = input("Enter category (Food/Travel/Bills/etc): ")
    if not category:
        print("Category required")
        return
    try:
        amount = float(input("Enter amount: "))
    except:
        print("Invalid amount input")
        return
    desc = input("Do you want to add description or not (Yes/No): ")
    if desc=="Yes":
        desc_ch=input("Enter your Description:")
    else:
        desc_ch="no description provided"
    data = load_data()
    data.append({  
        "date": exp_date,
        "category": category,
        "amount": amount,
        "description": desc_ch
    })
    save_data(data)
    print("✅ Expense added successfully!")
@log_and_time
def view_expenses():
    data = load_data()
    if not data:
        print("No expenses found.")
        return
    print("\n All Expenses:\n")
    total = 0
    for e in data:
        print(f"{e['date']}  {e['category']}  ₹{e['amount']}  {e['description']}")
        total += e['amount']
    print(f"\n Total: ₹{total}")
@log_and_time
def monthly_summary():
    rep = input("Enter month and year (MM YYYY): ")
    try:
        mm, yyyy = map(int, rep.split())
    except:
        print("Incorrect date format")
        return
    data = load_data()
    summary = {}
    total = 0
    for e in data:
        d = datetime.strptime(e["date"], "%Y-%m-%d")
        if d.month == mm and d.year == yyyy:
            summary[e["category"]] = summary.get(e["category"], 0) + e["amount"]
            total += e["amount"]
    month_name = calendar.month_name[mm]
    print(f"\n===== Monthly Summary: {month_name} {yyyy} =====")
    if not summary:
        print("No expenses this month.")
        return
    for cat, amt in summary.items():
        print(f"{cat}: ₹{amt}")
    print(f"Total: ₹{total}")
    export = {
        "month": month_name,
        "year": yyyy,
        "summary": summary,
        "total": total
    }
    fname = f"summary_{month_name}_{yyyy}.json"
    with open(fname, "w") as f:
        json.dump(export, f)
    print(f"Summary exported to '{fname}'")
while True:
    print("\n===== Smart Expense Tracker =====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Generate Monthly Summary")
    print("4. Exit")
    ch = input("Enter your choice: ")
    if ch == "1":
        add_expense()
    elif ch == "2":
        view_expenses()
    elif ch == "3":
        monthly_summary()
    elif ch == "4":
        print("Thank You!")
        break
    else:
        print("Invalid choice! Try again.")


