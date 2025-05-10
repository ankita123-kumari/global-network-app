import tkinter as tk
from tkinter import messagebox


class SeekApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Job Seek App")
        self.users = []
        self.jobs = []

        # Main Menu
        self.main_menu()

    def main_menu(self):
        # Clear the window
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Job Seek App", font=("Arial", 20)).pack(pady=10)

        tk.Button(self.root, text="Create Profile", command=self.create_profile_screen, width=20).pack(pady=5)
        tk.Button(self.root, text="Post Job", command=self.post_job_screen, width=20).pack(pady=5)
        tk.Button(self.root, text="Search Jobs", command=self.search_jobs_screen, width=20).pack(pady=5)
        tk.Button(self.root, text="Exit", command=self.root.quit, width=20).pack(pady=5)

    def create_profile_screen(self):
        # Clear the window
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Create Profile", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.root, text="Name:").pack()
        name_entry = tk.Entry(self.root)
        name_entry.pack()

        tk.Label(self.root, text="Skills:").pack()
        skills_entry = tk.Entry(self.root)
        skills_entry.pack()

        def save_profile():
            name = name_entry.get()
            skills = skills_entry.get()
            if name and skills:
                self.users.append({"name": name, "skills": skills})
                messagebox.showinfo("Success", f"Profile for {name} created successfully!")
                self.main_menu()
            else:
                messagebox.showerror("Error", "All fields are required!")

        tk.Button(self.root, text="Save", command=save_profile).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.main_menu).pack()

    def post_job_screen(self):
        # Clear the window
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Post Job", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.root, text="Job Title:").pack()
        title_entry = tk.Entry(self.root)
        title_entry.pack()

        tk.Label(self.root, text="Company:").pack()
        company_entry = tk.Entry(self.root)
        company_entry.pack()

        tk.Label(self.root, text="Skills Required:").pack()
        skills_entry = tk.Entry(self.root)
        skills_entry.pack()

        def save_job():
            title = title_entry.get()
            company = company_entry.get()
            skills = skills_entry.get()
            if title and company and skills:
                self.jobs.append({"title": title, "company": company, "skills": skills})
                messagebox.showinfo("Success", f"Job '{title}' posted successfully!")
                self.main_menu()
            else:
                messagebox.showerror("Error", "All fields are required!")

        tk.Button(self.root, text="Post Job", command=save_job).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.main_menu).pack()

    def search_jobs_screen(self):
        # Clear the window
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Search Jobs", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.root, text="Enter Skill:").pack()
        skill_entry = tk.Entry(self.root)
        skill_entry.pack()

        def search_jobs():
            skill = skill_entry.get().lower()
            found_jobs = [job for job in self.jobs if skill in job["skills"].lower()]
            if found_jobs:
                result = "\n".join([f"{job['title']} at {job['company']} (Skills: {job['skills']})" for job in found_jobs])
                messagebox.showinfo("Jobs Found", result)
            else:
                messagebox.showinfo("No Jobs Found", "No jobs match your search.")

        tk.Button(self.root, text="Search", command=search_jobs).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.main_menu).pack()


# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = SeekApp(root)
    root.mainloop()