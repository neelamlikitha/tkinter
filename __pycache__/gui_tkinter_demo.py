from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

root = tk.Tk()
root.title("GUI Development in python - tkinter")
root.geometry("900x700")

# Handle icon safely
try:
    root.iconbitmap("image.ico")  # use .ico file
except:
    pass

def on_button_click():
    messagebox.showinfo("Event Triggered", "Button Clicked Successfully")

def exit_app():
    root.quit()

# Menu bar
menu_bar = tk.Menu(root)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Exit", command=exit_app)
menu_bar.add_cascade(label="File", menu=file_menu)

help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(
    label="About",
    command=lambda: messagebox.showinfo("About", "Tkinter GUI application")
)
menu_bar.add_cascade(label="Help", menu=help_menu)

root.config(menu=menu_bar)

# Toolbar
toolbar = tk.Frame(root, bg="lightgray", relief=tk.RAISED, bd=2)
btn_toolbar = tk.Button(toolbar, text="Click Me", command=on_button_click)
btn_toolbar.pack(side=tk.LEFT, padx=5)
toolbar.pack(side=tk.TOP, fill=tk.X)

# Status bar
status_var = tk.StringVar(value="Ready")
status_bar = tk.Label(
    root, textvariable=status_var, bd=1,
    relief=tk.SUNKEN, anchor=tk.W
)
status_bar.pack(side=tk.BOTTOM, fill=tk.X)

# Main frame
main_frame = tk.Frame(root)
main_frame.pack(pady=10)

label = tk.Label(main_frame, text="Enter Your Name:")
label.grid(row=0, column=0, padx=5, pady=5)

entry = tk.Entry(main_frame)
entry.grid(row=0, column=1, padx=5, pady=5)

button = tk.Button(main_frame, text="Submit", command=on_button_click)
button.grid(row=0, column=2, padx=5, pady=5)

# Scale
scale = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, label="Volume")
scale.pack(pady=10)

# Spinbox
spinbox = tk.Spinbox(root, from_=1, to=10)
spinbox.pack(pady=10)

# Listbox
listbox = tk.Listbox(root, height=4)
listbox.insert(1, "Python")
listbox.insert(2, "Java")
listbox.insert(3, "C++")
listbox.pack(pady=10)

# Combobox
combo = ttk.Combobox(root, values=["India", "USA", "UK", "Canada"])
combo.set("Select Country")
combo.pack(pady=10)

# Treeview
columns = ("ID", "Name", "Course")
tree = ttk.Treeview(root, columns=columns, show="headings")

tree.heading("ID", text="ID")
tree.heading("Name", text="Name")
tree.heading("Course", text="Course")

tree.insert("", tk.END, values=(1, "Santhi", "Python"))
tree.insert("", tk.END, values=(2, "Sravani", "Java"))
tree.pack(pady=10)
# ===== Eagle Image Display =====
# ===== Eagle Image Display (Proper Fit) =====

try:
    eagle_img = Image.open("eagle symbol.jpg")

    # Keep aspect ratio
    max_width = 300
    max_height = 200

    img_width, img_height = eagle_img.size
    scale = min(max_width / img_width, max_height / img_height)

    new_width = int(img_width * scale)
    new_height = int(img_height * scale)

    eagle_img = eagle_img.resize((new_width, new_height), Image.LANCZOS)
    eagle_photo = ImageTk.PhotoImage(eagle_img)

    eagle_label = tk.Label(root, image=eagle_photo)
    eagle_label.image = eagle_photo
    eagle_label.pack(pady=10)

except Exception as e:
    print("Image not loaded:", e)
# Canvas
canvas = tk.Canvas(root, width=300, height=200, bg="white")
canvas.create_line(10, 10, 200, 10, fill="blue", width=2)
canvas.create_rectangle(50, 50, 150, 120, outline="red", width=2)
canvas.pack(pady=10)

root.mainloop()
