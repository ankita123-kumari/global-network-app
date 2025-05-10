import tkinter as tk
from tkinter import messagebox


class InstagramApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Instagram App")
        self.users = []

        # Main Menu
        self.main_menu()

    def main_menu(self):
        # Clear the window
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Instagram App", font=("Arial", 20)).pack(pady=10)

        tk.Button(self.root, text="Create Profile", command=self.create_profile_screen, width=20).pack(pady=5)
        tk.Button(self.root, text="View Profiles", command=self.view_profiles_screen, width=20).pack(pady=5)
        tk.Button(self.root, text="Increase Followers", command=self.increase_followers_screen, width=20).pack(pady=5)
        tk.Button(self.root, text="Exit", command=self.root.quit, width=20).pack(pady=5)

    def create_profile_screen(self):
        # Clear the window
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Create Profile", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.root, text="Username:").pack()
        username_entry = tk.Entry(self.root)
        username_entry.pack()

        tk.Label(self.root, text="Bio:").pack()
        bio_entry = tk.Entry(self.root)
        bio_entry.pack()

        def save_profile():
            username = username_entry.get()
            bio = bio_entry.get()
            if username and bio:
                self.users.append({"username": username, "bio": bio, "followers": 0})
                messagebox.showinfo("Success", f"Profile for {username} created successfully!")
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
                tk.Label(self.root, text=f"Username: {user['username']}, Bio: {user['bio']}, Followers: {user['followers']}").pack()
        else:
            tk.Label(self.root, text="No profiles found.").pack()

        tk.Button(self.root, text="Back", command=self.main_menu).pack(pady=10)

    def increase_followers_screen(self):
        # Clear the window
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Increase Followers", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.root, text="Enter Username:").pack()
        username_entry = tk.Entry(self.root)
        username_entry.pack()

        def increase_followers():
            username = username_entry.get()
            for user in self.users:
                if user["username"] == username:
                    user["followers"] += 1
                    messagebox.showinfo("Success", f"{username} now has {user['followers']} followers!")
                    self.main_menu()
                    return
            messagebox.showerror("Error", "Username not found!")

        tk.Button(self.root, text="Increase", command=increase_followers).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.main_menu).pack()


# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = InstagramApp(root)
    root.mainloop()