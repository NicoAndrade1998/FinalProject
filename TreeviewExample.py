from tkinter import Tk
from tkinter import ttk

root = Tk()
root.title("TreeView Example")

tree = ttk.Treeview(root)
tree["columns"] = ("name", "age", "city")
tree.heading("#0", text="ID")
tree.heading("name", text="Name")
tree.heading("age", text="Age")
tree.heading("city", text="City")

tree.insert("", "end", text="1", values=("John Doe", "25", "New York"))
tree.insert("", "end", text="2", values=("Jane Smith", "30", "London"))

tree.pack()

root.mainloop()
