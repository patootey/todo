from tkinter import ttk
from PIL import Image, ImageTk


# Klasse for å lage en knapp
class Button:
    """
    Klasse for å lage en knapp i en Tkinter-applikasjon.

    Args:
        root: Foreldrevinduet der knappen skal plasseres.
        text: Teksten som skal vises på knappen.
        command: Funksjonen som skal kjøres når knappen trykkes.
        toggle_command: Funksjonen som skal kjøres når knappen trykkes for å veksle tilstanden.
    """

    def __init__(self, root, text="", command=None, toggle_command=None):
        self.text = text
        self.command = command
        self.toggle_command = toggle_command
        self.clicked = False
        self.create_button(root)

    def click(self):
        """
        Metode for å håndtere knappetrykk.
        Kaller de tilknyttede kommandoene og oppdaterer knappens tilstand og stil.
        """
        if self.command:
            self.command()
        if self.toggle_command:
            self.toggle_command()
        self.clicked = not self.clicked
        self.update_style()

    def create_button(self, root):
        """
        Metode for å lage knappen og plassere den i vinduet.

        Args:
            root: Foreldrevinduet der knappen skal plasseres.
        """
        self.button = ttk.Button(root, text=self.text, command=self.click)
        self.button.pack()
        self.update_style()

    def update_style(self):
        """
        Metode for å oppdatere stilen på knappen basert på tilstanden.
        """
        style = ttk.Style()
        if self.clicked:
            style.configure("TButton", font=("Helvetica", 12, "normal"))
        else:
            style.configure("TButton", font=("Helvetica", 12, "normal"))
        self.button.config(style="TButton")


# Klasse for å vise et bilde
class Photo:
    """
    Klasse for å vise et bilde i en Tkinter-applikasjon.

    Args:
        root: Foreldrevinduet der bildet skal vises.
        image_path: Stien til bildet som skal vises.
        size: Størrelsen på bildet (bredde, høyde).
        bind: Funksjonen som skal bindes til en hendelse på bildet.
        position: Posisjonen der bildet skal plasseres (x, y).
        button: Hendelsen som skal bindes til bildet (standard er venstre museklikk).
    """

    def __init__(
        self,
        root,
        image_path,
        size=(50, 50),
        bind=None,
        position=(0, 0),
        button="<Button-1>",
    ):
        self.image_path = image_path
        self.size = size
        self.position = position
        self.bind = bind
        self.button = button
        self.image = None
        self.label = None
        self.create_image(root)

    def create_image(self, root):
        """
        Metode for å lage og vise bildet i vinduet.

        Args:
            root: Foreldrevinduet der bildet skal vises.
        """
        photo = Image.open(self.image_path)
        photo = photo.resize(self.size, Image.ADAPTIVE)
        self.image = ImageTk.PhotoImage(photo)
        self.label = ttk.Label(root, image=self.image)

        if self.bind is not None:
            # Binder klikk-handling til bildet hvis en funksjon er angitt
            self.label.bind(self.button, lambda event: self.bind())

        self.label.place(x=self.position[0], y=self.position[1])


# Liste for å holde styr på tidligere sider
prevpage = []


# Funksjon for å tømme vinduet
def clear_window(root, page=[]):
    for widget in root.winfo_children():
        if widget not in page and widget not in savedWidgets and widget not in prevpage:
            widget.destroy()


# Funksjon for å lagre gjeldende side
def keep_page(root):
    page = []
    for widget in root.winfo_children():
        if widget.winfo_ismapped() and widget not in savedWidgets:
            page.append(widget)
            widget.forget()
    return page


# Funksjon for å laste en tidligere lagret side
def load_page(root, page):
    if page is not None:
        clear_window(root, page=page)
        for widget in page:
            widget.pack()


# Liste for å holde styr på lagrede widgets
savedWidgets = []


# Funksjon for å lagre en widget
def save_widget(widget):
    global savedWidgets
    savedWidgets.append(widget)


# Funksjon for å lese eksisterende navn fra en fil
def read_existing_names(file):
    existing_names = []
    try:
        with open(file, "r") as my_file:
            existing_names = my_file.read().splitlines()
    except FileNotFoundError:
        pass
    return existing_names


# Funksjon for å slette valgt navn fra listeboksen og filen
def delete_selected_name(name_listbox, file: str):
    selected_index = name_listbox.curselection()
    if selected_index:
        index = int(selected_index[0])
        name_to_delete = name_listbox.get(index)
        name_listbox.delete(index)

        with open(file, "r") as my_file:
            lines = my_file.readlines()
        with open(file, "w") as my_file:
            for line in lines:
                if line.strip() != name_to_delete:
                    my_file.write(line)
