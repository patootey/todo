import sys
import os
import tkinter as tk  # Importerer tkinter-biblioteket for GUI
from general import (
    clear_window,
    Button,
    Photo,
    prevpage,
    load_page,
    save_widget,
    keep_page,
    read_existing_names,
    delete_selected_name,
)


window = tk.Tk()  # Oppretter et hovedvindu (root) for GUI-en
window.title("Lag en todo liste")  # Setter tittelen på vinduet
window.geometry("400x300")  # Setter størrelsen på vinduet til 400x300 piksler

# Determine the path to the images directory
if getattr(sys, "frozen", False):
    # Running as a PyInstaller executable
    script_dir = sys._MEIPASS
else:
    # Running as a script
    script_dir = os.path.dirname(os.path.abspath(__file__))


class TodoApp:
    def __init__(self, root) -> None:
        self.window = tk.Tk()
        self.title = window.title("Lag en todo liste")
        self.size = window.geometry("400x300")

    def tasks(self, root, file):
        prevpage = keep_page(root)  # Lagrer nåværende side
        frame = tk.Frame(root)  # Oppretter en ny rammekomponent

        # Oppretter et inndatafelt og en etikett for å legge inn navn
        tk.Label(frame, text="Skriv inn en task: ").grid(column=1, row=0)
        name_entry = tk.Entry(frame)
        name_entry.grid(column=2, row=0)

        # Oppretter en Listbox for å vise navnene
        name_listbox = tk.Listbox(frame)
        name_listbox.grid(column=3, row=0)

        # Oppretter en scrollbar for å bla gjennom eksisterende navn
        scrollbar = tk.Scrollbar(frame, orient="vertical")
        scrollbar.grid(row=0, column=4, sticky=tk.NS)

        # Kobler scrollbar til Listbox
        name_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=name_listbox.yview)

        # Fyller Listbox med eksisterende navn fra filen
        existing_names = read_existing_names()
        for name in existing_names:
            name_listbox.insert(tk.END, name)

        # Funksjon for å legge til et navn i Listbox og filen
        def write_file():
            name = name_entry.get()
            with open(file, "a") as my_file:
                my_file.write(name + "\n")

            name_entry.delete(0, tk.END)  # Fjerner det som står i tekstboksen

            # Oppdaterer Listbox med det nye navnet
            name_listbox.insert(tk.END, name)

        # Knapp for å legge til en elev
        tk.Button(frame, text="Legg til task", command=write_file, bg="blue").grid(
            column=1, row=3
        )
        # Knapp for å slette et navn
        delete_button = tk.Button(
            frame,
            text="Slett task",
            command=lambda: delete_selected_name(name_listbox, "hello.txt"),
            bg="red",
        )
        delete_button.grid(column=3, row=1)
        frame.place(y=70)  # Plasserer rammekomponenten i vinduet


def main(root):
    app = TodoApp(root)
    clear_window(root)
    todo_button = Button(
        root,
        text="Opprett todo liste",
        command=lambda: app.tasks(root, "hello.txt"),
        colour="pink",
    )
    exit_button = Button(root, text="Avslutt", command=lambda: exit(root), colour="red")

    # Oppretter en 'Hjem'-knapp med et bilde og knytter den til hovedfunksjonen 'main'
    home_button = Photo(
        window,
        "./images/home.png",
        size=(40, 40),
        position=(40, 0),
        bind=lambda: main(window),
    )
    # Oppretter en 'Pil'-knapp med et bilde og knytter den til en funksjon 'ge.load_page'
    arrow_button = Photo(
        window,
        "./images/left_arrow.png",
        size=(40, 40),
        bind=lambda: load_page(window, prevpage),
    )
    # Lagrer knappene som widgets for senere bruk
    save_widget(arrow_button.label)
    save_widget(home_button.label)

    root.mainloop()


def exit(root):
    root.destroy()


if __name__ == "__main__":
    main(window)
    window.mainloop()
