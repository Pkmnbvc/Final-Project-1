import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from voting_systems import VotingSystem

class VotingApp:
    def __init__(self, root: tk.Tk):
        """
        Initializes the GUI for the voting system.
        :param root:
        """
        self.voting_system = VotingSystem()
        self.root = root
        self.root.title("Voting System")

        icon_image = Image.open("voting app.png")  # Replace 'icon.png' with the path to your PNG file
        icon_photo = ImageTk.PhotoImage(icon_image)
        self.root.iconphoto(False, icon_photo)

        self.label = tk.Label(root, text = "Vote for Your Candidate", font=("Arial", 14))
        self.label.pack(pady=10)

        self.vote_john_btn = tk.Button(root, text="Vote John",  command=self.vote_john, width=20)
        self.vote_john_btn.pack(pady=5)

        self.vote_jane_btn = tk.Button(root, text="Vote Jane", command=self.vote_jane, width=20)
        self.vote_jane_btn.pack(pady=5)

        self.results_btn = tk.Button(root, text="Show Results", command=self.show_results, width=20)
        self.results_btn.pack(pady=5)

        self.exit_btn =tk.Button(root, text="Exit", command=root.quit, width=20)
        self.exit_btn.pack(pady=5)

    def vote_john(self):
        self.vote("1")
    def vote_jane(self):
        self.vote("2")

    def vote(self, candidate_id: str):
        try:
            message = self.voting_system.vote(candidate_id)
            messagebox.showinfo("Vote Recorded", message)
        except ValueError as e:
            messagebox.showerror("Error", str(e))
    def show_results(self):
        results = self.voting_system.get_results()
        messagebox.showinfo("Voting Results", results)

if __name__ == '__main__':
    root = tk.Tk()
    app = VotingApp(root)
    root.mainloop()





