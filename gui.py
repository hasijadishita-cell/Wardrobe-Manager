import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
import os
from models import *
import sqlite3
selected_image_path=None

# ---------------- GLOBAL STATE ----------------
CURRENT_EDIT_ID = None
current_image = None

# ---------------- WINDOW ----------------
root = tk.Tk()
root.title("Wardrobe Manager")
root.geometry("900x500")

# ---------------- IMAGE LABEL ----------------
image_label = tk.Label(root)
image_label.grid(row=0, column=3, rowspan=8, padx=20)

# ---------------- FUNCTIONS ----------------
def refresh_listbox():
    listbox.delete(0, tk.END)
    for item in get_all_items():
        listbox.insert(tk.END, f"{item[0]} | {item[1]} ({item[2]})")

def load_selected_item(event):
    global CURRENT_EDIT_ID, selected_image_path, current_image

    selection = listbox.curselection()
    if not selection:
        return

    index = selection[0]
    item = get_all_items()[index]

    CURRENT_EDIT_ID = item[0]

    entry_name.delete(0, tk.END)
    entry_category.delete(0, tk.END)
    entry_color.delete(0, tk.END)
    entry_season.delete(0, tk.END)
    entry_occasion.delete(0, tk.END)

    entry_name.insert(0, item[1])
    entry_category.insert(0, item[2])
    entry_color.insert(0, item[3])
    entry_season.insert(0, item[4])
    entry_occasion.insert(0, item[5])

    selected_image_path = item[6]

    if selected_image_path and os.path.exists(selected_image_path):
        img = Image.open(selected_image_path).resize((200, 200))
        current_image = ImageTk.PhotoImage(img)
        image_label.config(image=current_image)
        image_label.image = current_image
    else:
        image_label.config(image="")
def choose_image():
    global current_image, selected_image_path

    if CURRENT_EDIT_ID is None:
        messagebox.showerror("Error", "Select an item first")
        return

    path = filedialog.askopenfilename(
        filetypes=[("Images", "*.png *.jpg *.jpeg")]
    )

    if not path:
        return

    # Preview image
    img = Image.open(path)
    img = img.resize((200, 200))
    current_image = ImageTk.PhotoImage(img)
    image_label.config(image=current_image)
    image_label.image = current_image

    
    item = get_item_by_id(CURRENT_EDIT_ID)
    update_item(
        CURRENT_EDIT_ID,
        item[1], item[2], item[3], item[4], item[5],
        path
    )

    refresh_listbox()

def add_item_gui():
    name = entry_name.get().strip()
    category = entry_category.get().strip()
    color = entry_color.get().strip()
    season = entry_season.get().strip()
    occasion = entry_occasion.get().strip()

    if not all([name, category, color, season, occasion]):
        messagebox.showerror("Error", "Fill all fields")
        return

    success=add_items(name, category, color, season, occasion, None)
    if not success:
        messagebox.showerror("Duplicate Item", "Item already exists with the same name!")
        return
    refresh_listbox()
    messagebox.showinfo("Success", "Item added")

def update_item_gui():
    if CURRENT_EDIT_ID is None:
        messagebox.showerror("Error", "Select an item")
        return

    update_item(
        CURRENT_EDIT_ID,
        entry_name.get(),
        entry_category.get(),
        entry_color.get(),
        entry_season.get(),
        entry_occasion.get(),
        selected_image_path
    )

    refresh_listbox()
    messagebox.showinfo("Success", "Item updated")

def delete_item_gui():
    if CURRENT_EDIT_ID is None:
        messagebox.showerror("Error", "Select an item")
        return

    delete_items(CURRENT_EDIT_ID)
    refresh_listbox()
    image_label.config(image="")
    messagebox.showinfo("Deleted", "Item removed")

# ---------------- LEFT LISTBOX ----------------
listbox = tk.Listbox(root, width=40, height=20)
listbox.grid(row=0, column=0, rowspan=8, padx=10)
listbox.bind("<<ListboxSelect>>", load_selected_item)

# ---------------- FORM ----------------
labels = ["Name", "Category", "Color", "Season", "Occasion"]
entries = []

for i, text in enumerate(labels):
    tk.Label(root, text=text).grid(row=i, column=1, sticky="w")
    e = tk.Entry(root, width=25)
    e.grid(row=i, column=2)
    entries.append(e)

entry_name, entry_category, entry_color, entry_season, entry_occasion = entries

# ---------------- BUTTONS ----------------
tk.Button(root, text="Add Item", width=15, command=add_item_gui).grid(row=5, column=2, pady=5)
tk.Button(root, text="Delete Item", width=15, command=delete_item_gui).grid(row=6, column=2, pady=5)
tk.Button(root, text="Update Item", width=15, command=update_item_gui).grid(row=7, column=2, pady=5)
tk.Button(root, text="Choose Image", width=15, command=choose_image).grid(row=8, column=2, pady=5)


# ---------------- INIT ----------------
refresh_listbox()
root.mainloop()