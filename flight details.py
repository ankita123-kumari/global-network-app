import tkinter as tk
from tkinter import messagebox


class FlightDetailsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Flight Details App")
        self.flights = [
            {"flight_no": "AI101", "origin": "New York", "destination": "London", "time": "10:00 AM"},
            {"flight_no": "BA202", "origin": "London", "destination": "Paris", "time": "12:00 PM"},
            {"flight_no": "AF303", "origin": "Paris", "destination": "Tokyo", "time": "3:00 PM"},
            {"flight_no": "DL404", "origin": "Tokyo", "destination": "New York", "time": "8:00 PM"},
        ]

        # Main Menu
        self.main_menu()

    def main_menu(self):
        # Clear the window
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Flight Details App", font=("Arial", 20)).pack(pady=10)

        tk.Button(self.root, text="View All Flights", command=self.view_flights_screen, width=20).pack(pady=5)
        tk.Button(self.root, text="Search Flights", command=self.search_flights_screen, width=20).pack(pady=5)
        tk.Button(self.root, text="Exit", command=self.root.quit, width=20).pack(pady=5)

    def view_flights_screen(self):
        # Clear the window
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="All Flights", font=("Arial", 16)).pack(pady=10)

        if self.flights:
            for flight in self.flights:
                tk.Label(self.root, text=f"Flight No: {flight['flight_no']}, Origin: {flight['origin']}, "
                                         f"Destination: {flight['destination']}, Time: {flight['time']}").pack()
        else:
            tk.Label(self.root, text="No flight details available.").pack()

        tk.Button(self.root, text="Back", command=self.main_menu).pack(pady=10)

    def search_flights_screen(self):
        # Clear the window
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Search Flights", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.root, text="Enter Destination:").pack()
        destination_entry = tk.Entry(self.root)
        destination_entry.pack()

        def search_flights():
            destination = destination_entry.get().lower()
            found_flights = [flight for flight in self.flights if destination in flight["destination"].lower()]
            if found_flights:
                result = "\n".join([f"Flight No: {flight['flight_no']}, Origin: {flight['origin']}, "
                                    f"Destination: {flight['destination']}, Time: {flight['time']}"
                                    for flight in found_flights])
                messagebox.showinfo("Flights Found", result)
            else:
                messagebox.showinfo("No Flights Found", "No flights match your search.")

        tk.Button(self.root, text="Search", command=search_flights).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.main_menu).pack()


# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = FlightDetailsApp(root)
    root.mainloop()