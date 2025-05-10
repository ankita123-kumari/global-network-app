import tkinter as tk
from tkinter import messagebox


class LinkedInApp:
    def __init__(self, root):
        self.root = root
        self.root.title("LinkedIn App")
        self.users = []
        self.jobs = []

        # Main Menu
        self.main_menu()

    def main_menu(self):
        # Clear the window
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="LinkedIn App", font=("Arial", 20)).pack(pady=10)

        tk.Button(self.root, text="Create User", command=self.create_user_screen, width=20).pack(pady=5)
        tk.Button(self.root, text="Add Job", command=self.add_job_screen, width=20).pack(pady=5)
        tk.Button(self.root, text="Display Users", command=self.display_users_screen, width=20).pack(pady=5)
        tk.Button(self.root, text="Search Jobs", command=self.search_jobs_screen, width=20).pack(pady=5)
        tk.Button(self.root, text="Exit", command=self.root.quit, width=20).pack(pady=5)

    def create_user_screen(self):
        # Clear the window
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Create User", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.root, text="Name:").pack()
        name_entry = tk.Entry(self.root)
        name_entry.pack()
        tk.Label(self.root, text="Job Title:").pack()
        job_title_entry = tk.Entry(self.root)
        job_title_entry.pack()

        tk.Label(self.root, text="Location:").pack()
        location_entry = tk.Entry(self.root)
        location_entry.pack()

        def save_user():
            name = name_entry.get()
            job_title = job_title_entry.get()
            location = location_entry.get()
            if name and job_title and location:
                self.users.append({"name": name, "job_title": job_title, "location": location})
                messagebox.showinfo("Success", f"User {name} created successfully!")
                self.main_menu()
            else:
                messagebox.showerror("Error", "All fields are required!")

        tk.Button(self.root, text="Save", command=save_user).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.main_menu).pack()

    def add_job_screen(self):
        # Clear the window
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Add Job", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.root, text="Job Title:").pack()
        title_entry = tk.Entry(self.root)
        title_entry.pack()

        tk.Label(self.root, text="Company:").pack()
        company_entry = tk.Entry(self.root)
        company_entry.pack()

        tk.Label(self.root, text="Location:").pack()
        location_entry = tk.Entry(self.root)
        location_entry.pack()

        def save_user():
            name = title_entry.get()
            job_title = company_entry.get()
            location = location_entry.get()
            if name and job_title and location:
                self.users.append({"name": name, "job_title": job_title, "location": location})
                messagebox.showinfo("Success", f"User {name} created successfully!")
                self.main_menu()
            else:
                messagebox.showerror("Error", "All fields are required!")

        tk.Button(self.root, text="Save", command=save_user).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.main_menu).pack()

    def add_job_screen(self):
        # Clear the window
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Add Job", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.root, text="Job Title:").pack()
        title_entry = tk.Entry(self.root)
        title_entry.pack()

        tk.Label(self.root, text="Company:").pack()
        company_entry = tk.Entry(self.root)
        company_entry.pack()

        tk.Label(self.root, text="Location:").pack()
        location_entry = tk.Entry(self.root)
        location_entry.pack()

        def save_job():
            title = title_entry.get()
            company = company_entry.get()
            location = location_entry.get()
            if title and company and location:
                 self.jobs.append({"title": title, "company": company, "location": location})
                 messagebox.showinfo("Success", f"Job '{title}' added successfully!")
                 self.main_menu()
            else:
                messagebox.showerror("Error", "All fields are required!")

        tk.Button(self.root, text="Save", command=save_job).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.main_menu).pack()

    def display_users_screen(self):
        # Clear the window
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="All Users", font=("Arial", 16)).pack(pady=10)

        if self.users:
            for user in self.users:
                tk.Label(self.root, text=f"Name: {user['name']}, Job: {user['job_title']}, Location: {user['location']}").pack()
        else:
            tk.Label(self.root, text="No users found.").pack()

        tk.Button(self.root, text="Back", command=self.main_menu).pack(pady=10)

    def search_jobs_screen(self):
        # Clear the window
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Search Jobs", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.root, text="Enter keyword:").pack()
        keyword_entry = tk.Entry(self.root)
        keyword_entry.pack()

        def search_jobs():
            keyword = keyword_entry.get().lower()
            found_jobs = [job for job in self.jobs if keyword in job["title"].lower()]
            if found_jobs:
                result = "\n".join([f"{job['title']} at {job['company']} ({job['location']})" for job in found_jobs])
                messagebox.showinfo("Jobs Found", result)
            else:
                messagebox.showinfo("No Jobs Found", "No jobs match your search.")

        tk.Button(self.root, text="Search", command=search_jobs).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.main_menu).pack()


# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = LinkedInApp(root)
    root.mainloop()