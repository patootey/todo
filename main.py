import sys
import os
import tkinter as tk
from tkinter import ttk
import general

# Opprett hovedvinduet
window = tk.Tk()
window.title("Lag en todo liste")
window.geometry("400x300")

# Bestem script katalog basert på om programmet er frosset eller ikke (brukes for pyinstaller)
if getattr(sys, "frozen", False):
    script_dir = sys._MEIPASS  # type: ignore
else:
    script_dir = os.path.dirname(os.path.abspath(__file__))


# Klasse for Todo-applikasjonen
class TodoApp:
    def __init__(self, root) -> None:
        self.root = root

    # Funksjon for å håndtere oppgaver
    def tasks(self, root, file):
        general.prevpage = general.keep_page(root)
        frame = ttk.Frame(root)

        # Opprett en etikett og et inntastingsfelt
        ttk.Label(frame, text="Skriv inn en task: ").grid(column=0, row=0)
        name_entry = ttk.Entry(frame)
        name_entry.grid(column=1, row=0)

        # Opprett en listeboks for å vise oppgaver
        name_listbox = tk.Listbox(frame)
        name_listbox.grid(column=1, row=1)

        # Opprett en scrollbar for listeboksen
        scrollbar = ttk.Scrollbar(frame, orient="vertical")
        scrollbar.grid(row=1, column=2, sticky=tk.NS)

        # Konfigurer scrollbar til å fungere med listeboksen
        name_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=name_listbox.yview)

        # Les eksisterende oppgaver fra fil og legg dem til i listeboksen
        existing_names = general.read_existing_names("hello.txt")
        for name in existing_names:
            name_listbox.insert(tk.END, name)

        # Funksjon for å skrive en ny oppgave til fil og oppdatere listeboksen
        def write_file():
            name = name_entry.get()
            with open(file, "a") as my_file:
                my_file.write(name + "\n")
            name_entry.delete(0, tk.END)
            name_listbox.insert(tk.END, name)

        # Funksjon for å markere eller avmarkere en oppgave som fullført
        def toggle_task():
            selected_index = name_listbox.curselection()
            if selected_index:
                index = int(selected_index[0])
                task_text = name_listbox.get(index)
                if task_text.startswith("✓ "):
                    new_text = task_text[2:]
                else:
                    new_text = "✓ " + task_text
                name_listbox.delete(index)
                name_listbox.insert(index, new_text)
                name_listbox.selection_set(index)

        # Legg til knapp for å legge til en ny oppgave
        add_button = ttk.Button(frame, text="Legg til task", command=write_file)
        add_button.grid(column=0, row=2)

        # Legg til knapp for å slette en valgt oppgave
        delete_button = ttk.Button(
            frame,
            text="Slett task",
            command=lambda: general.delete_selected_name(name_listbox, file),
        )
        delete_button.grid(column=1, row=2)

        # Legg til knapp for å veksle mellom fullført og ikke fullført status for en oppgave
        toggle_button = ttk.Button(
            frame,
            text="Veksle mellom status",
            command=toggle_task,
        )
        toggle_button.grid(column=2, row=2)

        frame.place(y=70)


# Hovedfunksjonen for applikasjonen
def main(root):
    app = TodoApp(root)
    general.clear_window(root)
    general.Button(
        root, text="Opprett todo liste", command=lambda: app.tasks(root, "hello.txt")
    )
    general.Button(root, text="Avslutt", command=lambda: exit(root))

    # Opprett en hjem-knapp med et bilde
    home_button = general.Photo(
        window,
        os.path.join(script_dir, "images/home.png"),
        size=(40, 40),
        position=(10, 0),
        bind=lambda: main(window),
    )
    general.save_widget(home_button.label)

    root.mainloop()


# Funksjon for å avslutte applikasjonen
def exit(root):
    root.destroy()


# Start applikasjonen
if __name__ == "__main__":
    main(window)
    window.mainloop()
