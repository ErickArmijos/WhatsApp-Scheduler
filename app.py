import tkinter as tk
from tkinter import messagebox
from Controller.whatsapp_sender import send_message

def submit_form(event=None):
    telefono = telefono_entry.get()
    mensaje = mensaje_entry.get()
    hora = hora_entry.get()
    minuto = minuto_entry.get()

    # Validación de los datos
    if not telefono.isdigit() or len(telefono) != 10:
        messagebox.showerror("Error", "Por favor ingrese un número de teléfono válido (10 dígitos numéricos).")
        telefono_entry.delete(0, tk.END)  # Limpiar el campo de entrada
        return
    if not hora.isdigit() or int(hora) < 0 or int(hora) > 23:
        messagebox.showerror("Error", "Por favor ingrese una hora válida (0-23).")
        hora_entry.delete(0, tk.END)  # Limpiar el campo de entrada
        return
    if not minuto.isdigit() or int(minuto) < 0 or int(minuto) > 59:
        messagebox.showerror("Error", "Por favor ingrese un minuto válido (0-59).")
        minuto_entry.delete(0, tk.END)  # Limpiar el campo de entrada
        return

    # Si todos los datos son válidos, mostrar el mensaje de éxito
    messagebox.showinfo("Formulario Enviado", f"Teléfono: {telefono}\nMensaje: {mensaje}\nHora: {hora}:{minuto}")
    send_message(telefono,mensaje,hora,minuto)



def focus_next_entry(event, entry_list):
    current_index = entry_list.index(event.widget)
    next_index = (current_index + 1) % len(entry_list)
    entry_list[next_index].focus()
    if current_index == len(entry_list)-1:  # Si es el último campo de entrada
        submit_form()

# Crear la ventana principal
root = tk.Tk()
root.title("Mensajería Automatizada para WhatsApp")  # Título de la ventana

# Configuración del tema oscuro
root.config(bg="#121212")  # Fondo oscuro

# Título de la aplicación
title_label = tk.Label(root, text="Mensajería Automatizada para WhatsApp", bg="#121212", fg="white", font=('Arial', 16, 'bold'))
title_label.grid(row=0, column=0, columnspan=2, padx=70, pady=20, sticky="we")

# Crear y posicionar los elementos del formulario
tk.Label(root, text="Número de Teléfono:", bg="#121212", fg="white", font=('Arial', 12)).grid(row=1, column=0, sticky="w", padx=70, pady=10)
telefono_entry = tk.Entry(root)
telefono_entry.grid(row=1, column=1, padx=70, pady=10)

tk.Label(root, text="Mensaje:", bg="#121212", fg="white", font=('Arial', 12)).grid(row=2, column=0, sticky="w", padx=70, pady=10)
mensaje_entry = tk.Entry(root)
mensaje_entry.grid(row=2, column=1, padx=70, pady=10)

tk.Label(root, text="Hora (0-23):", bg="#121212", fg="white", font=('Arial', 12)).grid(row=3, column=0, sticky="w", padx=70, pady=10)
hora_entry = tk.Entry(root)
hora_entry.grid(row=3, column=1, padx=70, pady=10)
hora_entry.bind("<Return>", lambda event: focus_next_entry(event, [minuto_entry]))

tk.Label(root, text="Minuto (0-59):", bg="#121212", fg="white", font=('Arial', 12)).grid(row=4, column=0, sticky="w", padx=70, pady=10)
minuto_entry = tk.Entry(root)
minuto_entry.grid(row=4, column=1, padx=70, pady=10)
minuto_entry.bind("<Return>", submit_form)

# Botón para enviar el formulario
submit_button = tk.Button(root, text="Enviar", command=submit_form, bg="green", fg="white", font=('Arial', 14, 'bold'))
submit_button.grid(row=5, column=0, columnspan=2, pady=20, padx=70, sticky="we")

# Lista de entradas para enlazar con el evento de pulsación de tecla
entry_list = [telefono_entry, mensaje_entry, hora_entry, minuto_entry]

# Enlazar evento de pulsación de tecla para avanzar al siguiente campo
for entry in entry_list:
    entry.bind("<Return>", lambda event: focus_next_entry(event, entry_list))

# Ejecutar el bucle principal de la ventana
root.mainloop()
