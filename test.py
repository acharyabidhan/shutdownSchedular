# # Import the required libraries
# from tkinter import *
# from pystray import MenuItem as item
# import pystray
# from PIL import Image, ImageTk

# # Create an instance of tkinter frame or window
# win=Tk()

# win.title("System Tray Application")
# # Set the size of the window
# win.geometry("700x350")

# # Define a function for quit the window
# def quit_window(icon, item):
#    icon.stop()
#    win.destroy()

# # Define a function to show the window again
# def show_window(icon, item):
#    icon.stop()
#    win.after(0,win.deiconify())


# def reset_window():
#    pass


# # Hide the window and show on the system taskbar
# def hide_window():
#    win.withdraw()
#    image=Image.open("others\\icon.ico")
#    menu=(item('Quit', quit_window), item('Show', show_window), item("Reset", reset_window))
#    icon=pystray.Icon("name", image, "My System Tray Icon", menu)
#    icon.run()

# win.protocol('WM_DELETE_WINDOW', hide_window)

# win.mainloop()

# from uptime import uptime
# time = round(uptime()/60)
# print(time)

import subprocess

def process_exists(process_name):
    call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
    output = subprocess.check_output(call).decode()
    last_line = output.strip().split('\r\n')[-1]
    return last_line.lower().startswith(process_name.lower())
print(process_exists('cmd.exe'))