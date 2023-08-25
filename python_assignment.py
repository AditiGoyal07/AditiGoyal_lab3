class FlightTable:
    def __init__(self):
        self.data = []

    def add_entry(self, p_id, process, start_time, priority):
        entry = {
            "P_ID": p_id,
            "Process": process,
            "Start Time (ms)": start_time,
            "Priority": priority
        }
        self.data.append(entry)

    def sort_by_p_id(self):
        self.data.sort(key = lambda entry: entry["P_ID"])

    def sort_by_start_time(self):
        self.data.sort(key = lambda entry: entry["Start Time (ms)"])

    def sort_by_priority(self):
        priority_order = {"Low": 0, "MID": 1, "High": 2}
        self.data.sort(key = lambda entry: priority_order[entry["Priority"]])

    def print_table(self):
        print("{:<5} {:<10} {:<15} {:<8}".format("P_ID", "Process", "Start Time", "Priority"))
        print("=" * 40)
        for entry in self.data:
            print("{:<5} {:<10} {:<15} {:<8}".format(entry["P_ID"], entry["Process"], entry["Start Time (ms)"], entry["Priority"]))


if __name__ == "__main__":
    print("Aditi Goyal")
    print("E22CSEU1440\n")

    flight_table = FlightTable()

    flight_table.add_entry("P1", "VSCode", 100, "MID")
    flight_table.add_entry("P23", "Eclipse", 234, "MID")
    flight_table.add_entry("P93", "Chrome", 189, "High")
    flight_table.add_entry("P42", "JDK", 9, "High")
    flight_table.add_entry("P9", "CMD", 7, "High")
    flight_table.add_entry("P87", "NotePad", 23, "Low")

    print("Choose sorting parameter:")
    print("1. Sort by P_ID\n2. Sort by Start Time\n3. Sort by Priority")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        flight_table.sort_by_p_id()
    elif choice == 2:
        flight_table.sort_by_start_time()
    elif choice == 3:
        flight_table.sort_by_priority()
    else:
        print("Invalid choice.")

    flight_table.print_table()
