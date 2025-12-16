import tkinter as tk
from tkinter import messagebox
from models import *
CURRENT_EDIT_ID=None

root = tk.Tk()
root.title("Wardrobe Manager")
root.geometry("900x500")

def load_selected_item(event):
    selection = listbox.curselection()
    if not selection:
        return
    
    index = listbox.curselection()[0]
    item_text = listbox.get(index)
    item_id = int(item_text.split(" | ")[0])

    # Fetch full item record (from database)
    item = get_item_by_id(item_id)

    # Fill the entry boxes
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

    # Store item_id globally for updating
    global CURRENT_EDIT_ID
    CURRENT_EDIT_ID = item_id
# ---------------- LEFT SIDE LISTBOX --------------------
listbox = tk.Listbox(
    root,
    width=40,
    height=20,
    bg="white",   # fixes macOS transparency
    fg="black"    # visible text
)
listbox.grid(row=0, column=0, padx=20, pady=20, rowspan=10)
listbox.bind("<<ListboxSelect>>", load_selected_item)

def refresh_listbox():
    listbox.delete(0, tk.END)
    items = list_items()
    for item in items:
        listbox.insert(tk.END, f"{item[0]} | {item[1]} ({item[2]})")

refresh_listbox()

# ---------------- RIGHT SIDE ENTRY FORM ----------------
right_frame = tk.Frame(root)
right_frame.grid(row=0, column=1, padx=40, pady=20, sticky="n")

tk.Label(right_frame, text="Name:").grid(row=0, column=0, sticky="w")
entry_name = tk.Entry(right_frame, width=30)
entry_name.grid(row=0, column=1, pady=3)

tk.Label(right_frame, text="Category:").grid(row=1, column=0, sticky="w")
entry_category = tk.Entry(right_frame, width=30)
entry_category.grid(row=1, column=1, pady=3)

tk.Label(right_frame, text="Color:").grid(row=2, column=0, sticky="w")
entry_color = tk.Entry(right_frame, width=30)
entry_color.grid(row=2, column=1, pady=3)

tk.Label(right_frame, text="Season:").grid(row=3, column=0, sticky="w")
entry_season = tk.Entry(right_frame, width=30)
entry_season.grid(row=3, column=1, pady=3)

tk.Label(right_frame, text="Occasion:").grid(row=4, column=0, sticky="w")
entry_occasion = tk.Entry(right_frame, width=30)
entry_occasion.grid(row=4, column=1, pady=3)

# ---------------- BUTTON FUNCTIONS ---------------------
def add_item_gui():
    name = entry_name.get()
    category = entry_category.get()
    color = entry_color.get()
    season = entry_season.get()
    occasion = entry_occasion.get()

    if not name or not category:
        messagebox.showerror("Error", "Name & Category are required!")
        return

    add_items(name, category, color, season, occasion)
    messagebox.showinfo("Success", "Item Added!")
    refresh_listbox()

def update_item_gui():
    global CURRENT_EDIT_ID

    if CURRENT_EDIT_ID is None:
        messagebox.showerror("Error", "Select an item to update!")
        return

    name = entry_name.get()
    category = entry_category.get()
    color = entry_color.get()
    season = entry_season.get()
    occasion = entry_occasion.get()

    if not name or not category:
        messagebox.showerror("Error","Name and category cannot be empty!")
        return

    update_item(CURRENT_EDIT_ID, name, category, color, season, occasion)
    messagebox.showinfo("Success", "Item updated!")
    refresh_listbox()
    


def delete_item_gui():
    selection = listbox.curselection()
    if not selection:
        messagebox.showerror("Error", "Select an item to delete!")
        return
    
    index = selection[0]
    item_text = listbox.get(index)
    item_id = int(item_text.split(" | ")[0])

    delete_items(item_id)
    messagebox.showinfo("Deleted", "Item deleted!")
    refresh_listbox()


# ---------------- BUTTONS ------------------------------
add_btn = tk.Button(root, text="Add Item", command=add_item_gui, width=15)
add_btn.grid(row=1, column=1, pady=10)

delete_btn = tk.Button(root, text="Delete Item", command=delete_item_gui, width=15)
delete_btn.grid(row=2, column=1, pady=10)

update_btn = tk.Button(root, text="Update Item", command=update_item_gui, width=15)
update_btn.grid(row=3, column=1, pady=10)

root.mainloop()

