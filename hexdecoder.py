#!/usr/bin/env python
# coding: utf-8

# In[4]:


import tkinter as tk
from tkinter import messagebox

# --- Main Application Class ---
class HexDecoderApp:
    def __init__(self, root):
        """
        Initializes the Hex Decoder application GUI.
        Sets up the window, widgets, and layout.
        """
        self.root = root
        self.root.title("Hex Decoder")
        self.root.geometry("400x200") # Set a default size for the window
        self.root.resizable(False, False) # Make the window not resizable

        # Style configurations
        self.root.config(bg="#f0f0f0") # Light grey background
        font_label = ("Arial", 12)
        font_entry = ("Arial", 12)
        font_button = ("Arial", 12, "bold")
        font_result = ("Courier", 14, "bold")

        # --- Widget Creation ---

        # Frame for better organization
        main_frame = tk.Frame(self.root, padx=15, pady=15, bg="#f0f0f0")
        main_frame.pack(expand=True, fill=tk.BOTH)

        # Input Label and Entry
        self.label_hex = tk.Label(main_frame, text="Enter Hex String:", font=font_label, bg="#f0f0f0")
        self.entry_hex = tk.Entry(main_frame, font=font_entry, width=35, relief=tk.SOLID, borderwidth=1)

        # Convert Button
        self.button_convert = tk.Button(
            main_frame,
            text="Convert to ASCII",
            font=font_button,
            command=self.convert_hex_to_ascii,
            bg="#4CAF50", # Green
            fg="white",   # White text
            relief=tk.FLAT,
            activebackground="#45a049"
        )

        # Result Label
        self.label_result_title = tk.Label(main_frame, text="ASCII Result:", font=font_label, bg="#f0f0f0")
        self.result_text = tk.StringVar() # Use a StringVar to easily update the label text
        self.label_result = tk.Label(
            main_frame,
            textvariable=self.result_text,
            font=font_result,
            bg="white",
            fg="#333",
            relief=tk.SUNKEN,
            borderwidth=2,
            wraplength=350, # Wrap text if it gets too long
            anchor="w" # Align text to the west (left)
        )

        # --- Layout using grid ---
        main_frame.grid_columnconfigure(0, weight=1)

        self.label_hex.grid(row=0, column=0, sticky="w", pady=(0, 5))
        self.entry_hex.grid(row=1, column=0, sticky="ew", pady=(0, 10))
        self.button_convert.grid(row=2, column=0, sticky="ew", pady=(0, 15), ipady=5)
        self.label_result_title.grid(row=3, column=0, sticky="w", pady=(0, 5))
        self.label_result.grid(row=4, column=0, sticky="nsew", ipady=10)

        main_frame.grid_rowconfigure(4, weight=1) # Allow the result label to expand vertically

        # Bind the <Return> key to the conversion function
        self.root.bind('<Return>', lambda event: self.convert_hex_to_ascii())

    def convert_hex_to_ascii(self):
        """
        Fetches the hex string from the input field, converts it to ASCII,
        and displays the result or an error message.
        """
        hex_string = self.entry_hex.get().strip()

        # Remove common prefixes if they exist
        if hex_string.lower().startswith("0x"):
            hex_string = hex_string[2:]

        # Remove any spaces
        hex_string = hex_string.replace(" ", "")

        if not hex_string:
            self.result_text.set("")
            return

        # Validate that the string contains only valid hexadecimal characters
        try:
            # Convert hex string to bytes
            byte_data = bytes.fromhex(hex_string)
        except (ValueError, TypeError):
            # Show an error message box if the hex is invalid
            messagebox.showerror("Invalid Input", "Please enter a valid hexadecimal string (0-9, A-F).")
            self.result_text.set("Error: Invalid Hex")
            return

        try:
            # Decode bytes to ASCII. 'replace' handles non-ASCII characters gracefully.
            ascii_result = byte_data.decode('ascii', 'replace')
            self.result_text.set(ascii_result)
        except Exception as e:
            # General error handling
            messagebox.showerror("Conversion Error", f"An unexpected error occurred:\n{e}")
            self.result_text.set("Error")


# --- Main execution block ---
if __name__ == "__main__":
    root_window = tk.Tk()
    app = HexDecoderApp(root_window)
    root_window.mainloop()


# In[ ]:




