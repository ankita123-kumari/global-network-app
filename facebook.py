import tkinter as tk
from tkinter import messagebox


class FacebookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Facebook App")
        self.users = []

        # Main Menu
        self.main_menu()

    def main_menu(self):
        # Clear the window
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Facebook App", font=("Arial", 20)).pack(pady=10)

        tk.Button(self.root, text="Create Profile", command=self.create_profile_screen, width=20).pack(pady=5)
        tk.Button(self.root, text="View Profiles", command=self.view_profiles_screen, width=20).pack(pady=5)
        tk.Button(self.root, text="Add Friend", command=self.add_friend_screen, width=20).pack(pady=5)
        tk.Button(self.root, text="Exit", command=self.root.quit, width=20).pack(pady=5)

    def create_profile_screen(self):
        # Clear the window
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Create Profile", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.root, text="Name:").pack()
        name_entry = tk.Entry(self.root)
        name_entry.pack()

        tk.Label(self.root, text="Bio:").pack()
        bio_entry = tk.Entry(self.root)
        bio_entry.pack()

        def save_profile():
            name = name_entry.get()
            bio = bio_entry.get()
            if name and bio:
                self.users.append({"name": name, "bio": bio, "friends": []})
                messagebox.showinfo("Success", f"Profile for {name} created successfully!")
                self.main_menu()
            else:
                messagebox.showerror("Error", "All fields are required!")

        tk.Button(self.root, text="Save", command=save_profile).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.main_menu).pack()

    def view_profiles_screen(self):
        # Clear the window
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="All Profiles", font=("Arial", 16)).pack(pady=10)

        if self.users:
            for user in self.users:
                tk.Label(self.root, text=f"Name: {user['name']}, Bio: {user['bio']}, Friends: {len(user['friends'])}").pack()
        else:
            tk.Label(self.root, text="No profiles found.").pack()

        tk.Button(self.root, text="Back", command=self.main_menu).pack(pady=10)

    def add_friend_screen(self):
        # Clear the window
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Add Friend", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.root, text="Your Name:").pack()
        your_name_entry = tk.Entry(self.root)
        your_name_entry.pack()

        tk.Label(self.root, text="Friend's Name:").pack()
        friend_name_entry = tk.Entry(self.root)
        friend_name_entry.pack()

        def add_friend():
            your_name = your_name_entry.get()
            friend_name = friend_name_entry.get()

            user = next((u for u in self.users if u["name"] == your_name), None)
            friend = next((u for u in self.users if u["name"] == friend_name), None)

            if user and friend:
                if friend_name not in user["friends"]:
                    user["friends"].append(friend_name)
                    friend["friends"].append(your_name)
                    messagebox.showinfo("Success", f"{friend_name} is now friends with {your_name}!")
                    self.main_menu()
                else:
                    messagebox.showerror("Error", f"{friend_name} is already a friend!")
            else:
                messagebox.showerror("Error", "One or both profiles not found!")

        tk.Button(self.root, text="Add Friend", command=add_friend).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.main_menu).pack()


# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = FacebookApp(root)
    root.mainloop()