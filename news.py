import tkinter as tk
from tkinter import messagebox


class NewsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("News Search App")
        self.news_articles = [
            {"title": "Global Warming Effects", "content": "Global warming is causing sea levels to rise."},
            {"title": "Tech Innovations", "content": "New AI technology is transforming industries."},
            {"title": "Sports Update", "content": "The local team won the championship."},
            {"title": "Health Tips", "content": "Eating healthy can improve your lifestyle."},
            {"title": "Economic Growth", "content": "The economy is growing at a steady pace."},
        ]

        # Main Menu
        self.main_menu()

    def main_menu(self):
        # Clear the window
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="News Search App", font=("Arial", 20)).pack(pady=10)

        tk.Button(self.root, text="Search News", command=self.search_news_screen, width=20).pack(pady=5)
        tk.Button(self.root, text="View All News", command=self.view_all_news_screen, width=20).pack(pady=5)
        tk.Button(self.root, text="Exit", command=self.root.quit, width=20).pack(pady=5)

    def search_news_screen(self):
        # Clear the window
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Search News", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.root, text="Enter Keyword:").pack()
        keyword_entry = tk.Entry(self.root)
        keyword_entry.pack()

        def search_news():
            keyword = keyword_entry.get().lower()
            found_articles = [article for article in self.news_articles if keyword in article["title"].lower() or keyword in article["content"].lower()]
            if found_articles:
                result = "\n\n".join([f"Title: {article['title']}\nContent: {article['content']}" for article in found_articles])
                messagebox.showinfo("News Found", result)
            else:
                messagebox.showinfo("No News Found", "No articles match your search.")

        tk.Button(self.root, text="Search", command=search_news).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.main_menu).pack()

    def view_all_news_screen(self):
        # Clear the window
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="All News Articles", font=("Arial", 16)).pack(pady=10)

        if self.news_articles:
            for article in self.news_articles:
                tk.Label(self.root, text=f"Title: {article['title']}\nContent: {article['content']}", justify="left").pack(pady=5)
        else:
            tk.Label(self.root, text="No news articles available.").pack()

        tk.Button(self.root, text="Back", command=self.main_menu).pack(pady=10)


# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = NewsApp(root)
    root.mainloop()