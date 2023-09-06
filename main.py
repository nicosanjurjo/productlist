from tkinter import *
from tkinter import ttk

root = Tk()
root.minsize(400, 400)
root.title("Proyecto Tkinter - Listado de productos")
root.resizable(0, 0)

def home():
    home_label.config(
        fg='white',
        bg='black',
        font=('Arial', 30),
        padx=160,
        pady=20
        
    )
    home_label.grid(row=0, column=0)
    products_box.grid(row=2)

    for product in products:
        if len(product) == 3:
            product.append('added')
            products_box.insert('', 0, text=product[0], values=(product[1]))
        
    add_frame.grid_remove()
    add_label.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()
    description_label.grid(row=4, column=0, columnspan=2)  # Mostrar la descripción en la pantalla de inicio


def add():
    # Encabezado
    add_label.config(
        fg='white',
        bg='black',
        font=('Arial', 30),
        padx=35,
        pady=20
        
    )
    add_label.grid(row=0, column=0, columnspan=10)

    #Campos de forulario
    add_frame.grid(row=1)
    add_name_label.grid(row=1, column=0, padx=5, pady=5, sticky=E)
    add_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)
    
    add_price_label.grid(row=2, column=0, padx=5, pady=5, sticky=E)
    add_price_entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)
    
    add_description_label.grid(row=3, column=0, padx=5, pady=5, sticky=NW)
    add_description_entry.grid(row=3, column=1, padx=5, pady=5, sticky=W)
    add_description_entry.config(
        width=30,
        height=5,
        font=('Consolas', 12),
        padx=15,
        pady=15
    )

    boton.grid(row=5, column=1, sticky=NW)
    boton.config(
        padx=15,
        pady=5,
        bg="green",
        fg="white"
    )
    home_label.grid_remove()
    products_box.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()
    description_label.grid_remove()
    
    return True

def info():
    info_label.config(
        fg='white',
        bg='black',
        font=('Arial', 30),
        padx=110,
        pady=20
        
    )
    info_label.grid(row=0, column=0)

    #Oculta las pantallas no seleccionadas
    data_label.grid(row=1, column=0)
    products_box.grid_remove()
    add_frame.grid_remove()
    add_label.grid_remove()
    home_label.grid_remove()
    description_label.grid_remove()

    return True

# Función para mostrar la descripción del producto seleccionado
def show_description(event):
    selected_item = products_box.selection()
    if selected_item:
        item = products_box.item(selected_item)
        selected_description = item['text']  # El texto del elemento seleccionado contiene la descripción.
        description_label.config(text=f'Descripción: {selected_description}')


def add_product():
    products.append([
        name_data.get(),
        price_data.get(),
        add_description_entry.get("1.0", "end-1c")
    ])
    name_data.set("")
    price_data.set("")
    add_description_entry.delete("1.0", END)

# Variables importantes

products=[]
name_data=StringVar()
price_data= StringVar()

# Definición de campos de pantallas
home_label = Label(root, text='Inicio')
Label(root).grid(row=1)
products_box=ttk.Treeview(height=12, columns=2)
products_box.grid(row=1, column=0, columnspan=2)
products_box.heading('#0', text='Producto', anchor=W)
products_box.heading('#1', text='Precio', anchor=W)
add_label = Label(root, text='Añadir un producto')
info_label = Label(root, text='Infomación')
data_label = Label(root, text='Creado por Nicolás Sanjurjo - 2023')

# Crear campos de formulario
add_frame=Frame(root)
add_name_label = Label(add_frame, text='Nombre:')
add_name_entry = Entry(add_frame, textvariable=name_data)

add_price_label = Label(add_frame, text='Precio:')
add_price_entry = Entry(add_frame, textvariable=price_data)

add_description_label=Label(add_frame, text="Descripcion:")
add_description_entry=Text(add_frame)

boton=Button(add_frame, text='Guardar', command=add_product)

# Crear el cuadro de texto para la descripción
description_label = Label(root, text='', padx=10, pady=10)

# Enlazar el evento de selección en el Treeview con la función de actualización de la descripción
products_box.bind('<<TreeviewSelect>>', show_description)


# Cargar pantalla de inicio
home()

menu_bar = Menu(root)
menu_bar.add_command(label="Inicio", command=home)
menu_bar.add_command(label="Añadir", command=add)
menu_bar.add_command(label="Información", command=info)
menu_bar.add_command(label="Salir", command=root.quit)

root.config(menu=menu_bar)


root.mainloop()