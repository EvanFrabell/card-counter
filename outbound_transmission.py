import socket
import tkinter as tk
from tkinter import messagebox


def send_message(receiver_ip, receiver_port, message):
    try:
        # Create a socket object
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # Connect to the specified IP address and port
            s.connect((receiver_ip, receiver_port))
            # Send the message
            s.sendall(message.encode())
            print("Message sent successfully.")
    except Exception as e:
        print(f"Error: {e}")


def submit():
    selected_options = [option.get() for option in option_vars]
    selected_options = [option for option in selected_options if option]
    if selected_options:
        send_message(receiver_ip, receiver_port, "".join(selected_options))
        messagebox.showinfo("Selection", f"You selected options: {', '.join(selected_options)}")
    else:
        send_message(receiver_ip, receiver_port, "S")
        messagebox.showwarning("Selection", "You sent a SKIP message to the user")

    for option_var in option_vars:
        option_var.set("")


if __name__ == "__main__":
    # IP address and port of the receiving computer
    receiver_ip = '192.168.86.26'
    receiver_port = 1069

    root = tk.Tk()
    root.title("Multiple Selections")

    # Create Tkinter variables to store the selected options
    option_vars = []
    options = ["A", "B", "C", "D", "E"]


    def create_check_button(text):
        var = tk.StringVar()
        check_button = tk.Checkbutton(root, text=text, variable=var, onvalue=text, offvalue="")
        check_button.pack(anchor=tk.W)
        option_vars.append(var)


    # Create check buttons
    for option in options:
        create_check_button(f"{option}")

    # Submit button
    submit_button = tk.Button(root, text="Submit", command=submit)
    submit_button.pack()

    root.mainloop()

