import tkinter as tk  # Importerer tkinter-biblioteket for GUI
from PIL import Image, ImageTk  # Importerer moduler for bildebehandling


# Definisjon av klassen 'Button' for opprettelse av knapper
class Button:
    def __init__(self, root, text="", colour="white", command="boolean"):
        self.colour = colour  # Bakgrunnsfarge for knappen
        self.text = text  # Teksten som vises på knappen
        self.command = command  # Funksjonen som skal kalles når knappen trykkes
        self.clicked = False  # Status for om knappen er trykket
        self.create_button(root)  # Oppretter knappen i GUI-en

    def click(self):
        if self.command:
            self.command()  # Kaller den angitte funksjonen når knappen trykkes
        self.clicked = True if self.clicked == False else False  # Endrer trykkstatusen

    def create_button(self, root):
        self.button = tk.Button(
            root, text=self.text, bg=self.colour, command=self.click
        )  # Oppretter knappen med tekst og farge
        self.button.pack()  # Legger knappen til i GUI-en


# Definisjon av klassen 'Photo' for opprettelse av bildekomponenter
class Photo:
    def __init__(
        self,
        root,
        image_path,
        size=(50, 50),
        bind=None,
        position=(0, 0),
        button="<Button-1>",
    ):
        self.image_path = image_path  # Filbanen til bildet
        self.size = size  # Størrelsen på bildet
        self.position = position  # Posisjonen til bildet i GUI-en
        self.bind = bind  # Funksjonen som skal kalles når bildet klikkes
        self.button = button  # Knappen som brukes til å aktivere klikk-handling
        self.image = None  # Variabel for bildet
        self.label = None  # Variabel for etiketten som viser bildet
        self.create_image(root)  # Oppretter bildet i GUI-en

    def create_image(self, root):
        photo = Image.open(self.image_path)  # Åpner bildet fra fil
        photo = photo.resize(self.size, Image.ADAPTIVE)  # Justerer størrelsen på bildet
        self.image = ImageTk.PhotoImage(
            photo
        )  # Konverterer bildet til PhotoImage-format
        self.label = tk.Label(root, image=self.image)  # Oppretter en etikett med bildet

        if self.bind is not None:
            # Binder klikk-handling til bildet hvis en funksjon er angitt
            self.label.bind(self.button, lambda event: self.bind())

        self.label.place(
            x=self.position[0], y=self.position[1]
        )  # Plasserer etiketten i GUI-en


prevpage = []  # En liste for å lagre tidligere visningskomponenter


# Funksjon for å fjerne alle komponenter unntatt de som er spesifikt angitt i 'page'
def clear_window(root, page=[]):
    for widget in root.winfo_children():
        if widget not in page and widget not in savedWidgets and widget not in prevpage:
            widget.destroy()


# Funksjon for å lagre nåværende visningskomponenter
def keep_page(root):
    page = []
    for widget in root.winfo_children():
        if widget.winfo_ismapped() and widget not in savedWidgets:
            page.append(widget)
            widget.forget()
    return page


# Funksjon for å laste inn tidligere visningskomponenter i 'page'
def load_page(root, page):
    if page is not None:
        clear_window(root, page=page)
        for widget in page:
            widget.pack()


savedWidgets = []  # En liste for å lagre tidligere opprettede komponenter


# Funksjon for å lagre en enkelt widget i 'savedWidgets'
def save_widget(widget):
    global savedWidgets
    savedWidgets.append(widget)


# Funksjon for å lese eksisterende navn fra en fil
def read_existing_names():
    existing_names = []
    try:
        with open("import_elever.txt", "r") as my_file:
            existing_names = my_file.read().splitlines()
    except FileNotFoundError:
        pass
    return existing_names


# Funksjon for å slette det valgte navnet fra Listbox og filen
def delete_selected_name(name_listbox, file: str):
    selected_index = name_listbox.curselection()  # Få indeksen til det valgte elementet
    if selected_index:
        index = int(selected_index[0])  # Konverter indeksen til en integer
        name_to_delete = name_listbox.get(index)  # Få navnet som skal slettes
        name_listbox.delete(index)  # Fjern det valgte elementet fra Listbox

        # Fjern det slettede navnet fra filen
        with open(file, "r") as my_file:
            lines = my_file.readlines()
        with open(file, "w") as my_file:
            for line in lines:
                if line.strip() != name_to_delete:
                    my_file.write(line)
