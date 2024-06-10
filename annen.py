import tkinter as tk
from tkinter import ttk


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Todo App")

        # Inngangsboks for å legge til nye oppgaver
        self.task_entry = ttk.Entry(root, width=40)
        self.task_entry.pack(pady=10)

        # Knapp for å legge til oppgaver
        self.add_task_button = ttk.Button(
            root, text="Legg til oppgave", command=self.add_task
        )
        self.add_task_button.pack(pady=5)

        # Frame for å holde oppgavelisten
        self.tasks_frame = ttk.Frame(root)
        self.tasks_frame.pack(pady=10)

        # Oppgavelisten
        self.tasks = []

    def add_task(self):
        task_text = self.task_entry.get()
        if task_text:
            task_frame = ttk.Frame(self.tasks_frame)
            task_frame.pack(fill="x", pady=2)

            # Prikk til venstre for oppgaven
            task_dot = tk.Label(task_frame, text="•", width=2)
            task_dot.pack(side="left")

            # Oppgavetekst
            task_label = ttk.Label(task_frame, text=task_text, width=30)
            task_label.pack(side="left")

            # Knapp for å markere oppgaven som fullført
            complete_button = ttk.Button(
                task_frame,
                text="Fullfør",
                command=lambda: self.complete_task(task_label),
            )
            complete_button.pack(side="left")

            # Knapp for å slette oppgaven
            delete_button = ttk.Button(
                task_frame, text="Slett", command=lambda: self.delete_task(task_frame)
            )
            delete_button.pack(side="left")

            self.tasks.append(task_frame)
            self.task_entry.delete(0, tk.END)

    def complete_task(self, task_label):
        task_label.config(foreground="gray", font=("TkDefaultFont", 10, "overstrike"))

    def delete_task(self, task_frame):
        task_frame.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
