import tkinter as tk
import customtkinter as ctk
import webbrowser
import subprocess
import json
import os

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

appSwitchIT = ctk.CTk()
appSwitchIT.title("AltKey")
appSwitchIT.geometry("400x500")
appSwitchIT.configure(bg="black")

# Path to save the mode_links
data_file = "mode_links.json"

# Load the mode_links from the JSON file
def load_mode_links():
    if os.path.exists(data_file):
        with open(data_file, "r") as file:
            return json.load(file)
    return {
        "Chill Mode": ['https://www.netflix.com', 'https://www.youtube.com', 'https://www.spotify.com'],
        "Code Mode": ['https://stackoverflow.com', 'https://chat.openai.com'],
        "Pirate Mode": ['https://thepiratebay.org', 'https://1337x.to'],
        "Work Mode": ['https://www.gmail.com', 'https://www.google.com/docs']
    }

# Save the mode_links to the JSON file
def save_mode_links():
    with open(data_file, "w") as file:
        json.dump(mode_links, file)

mode_links = load_mode_links()

def open_mode(mode):
    links = mode_links.get(mode, [])
    for link in links:
        if 'http' in link:
            webbrowser.open(link)
        else:
            subprocess.Popen([link])

def open_options_window(mode):
    def add_link():
        new_link = link_entry.get()
        if new_link:
            mode_links[mode].append(new_link)
            update_links_display()
            save_mode_links()

    def remove_link():
        selected_link = links_listbox.get(tk.ACTIVE)
        if selected_link in mode_links[mode]:
            mode_links[mode].remove(selected_link)
            update_links_display()
            save_mode_links()

    def update_links_display():
        links_listbox.delete(0, tk.END)
        for link in mode_links[mode]:
            links_listbox.insert(tk.END, link)

    options_window = ctk.CTkToplevel(appSwitchIT)
    options_window.title(f"{mode} Options")
    options_window.geometry("400x300")

    links_listbox = tk.Listbox(options_window, height=6, width=50)
    links_listbox.pack(pady=10)

    link_entry = ctk.CTkEntry(options_window, placeholder_text="Add new link (URL or command)")
    link_entry.pack(pady=5)

    ctk.CTkButton(options_window, text="Add Link", command=add_link).pack(pady=5)
    ctk.CTkButton(options_window, text="Remove Selected Link", command=remove_link).pack(pady=5)

    update_links_display()

def create_mode_button(mode, row):
    frame = tk.Frame(appSwitchIT, bg=appSwitchIT.cget("background"), padx="5", pady="5")
    frame.pack(pady=5, padx=10, anchor='w')

    mode_button = ctk.CTkButton(frame, text=mode, command=lambda: open_mode(mode))
    mode_button.grid(row=row, column=0, padx=10)

    options_button = ctk.CTkButton(frame, text=f"{mode} Options", command=lambda: open_options_window(mode))
    options_button.grid(row=row, column=1, padx=10)

default_label = ctk.CTkLabel(appSwitchIT, text="Default Modes", font=("Arial", 18))
default_label.pack(pady=10)

row = 0
for mode in mode_links.keys():
    create_mode_button(mode, row)
    row += 1

def open_custom_button_window():
    def add_custom_button():
        label_text = label_entry.get()
        if label_text and label_text not in mode_links:
            mode_links[label_text] = []
            create_mode_button(label_text, row)
            save_mode_links()
            custom_window.destroy()

    custom_window = ctk.CTkToplevel(appSwitchIT)
    custom_window.title("Add Custom Mode")
    custom_window.geometry("300x200")

    label_entry = ctk.CTkEntry(custom_window, placeholder_text="Mode Label")
    label_entry.pack(pady=10)

    ctk.CTkButton(custom_window, text="Add Mode", command=add_custom_button).pack(pady=10)

add_custom_mode_button = ctk.CTkButton(appSwitchIT, text="Add New Mode", command=open_custom_button_window)
add_custom_mode_button.pack(pady=10)

def make_responsive(event):
    appSwitchIT.update_idletasks()
    new_width = appSwitchIT.winfo_width()
    for widget in appSwitchIT.winfo_children():
        widget.pack_configure(anchor="center", padx=max(10, new_width // 10))

appSwitchIT.bind("<Configure>", make_responsive)

appSwitchIT.mainloop()
