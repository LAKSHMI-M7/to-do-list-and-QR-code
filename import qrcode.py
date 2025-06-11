import qrcode
from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox
import os
from datetime import datetime

# Create folder to store history
if not os.path.exists("Generated_QR_Codes"):
    os.makedirs("Generated_QR_Codes")

def generate_qr():
    data = entry.get()
    if not data:
        messagebox.showwarning("Warning", "Please enter data!")
        return
    
    # Generate QR Code
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white").convert('RGB')
    
    # Add logo to QR code
    try:
        logo = Image.open("logo.png")  # Keep your logo file as logo.png in same folder
        logo_size = 60
        logo = logo.resize((logo_size, logo_size))
        pos = ((img.size[0] - logo_size) // 2, (img.size[1] - logo_size) // 2)
        img.paste(logo, pos)
    except:
        pass  # If logo not found, generate normal QR
    
    # Auto-save file with timestamp
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"Generated_QR_Codes/QR_{timestamp}.png"
    img.save(filename)
    
    messagebox.showinfo("Success", f"QR Code Saved: {filename}")

# Build GUI
window = tk.Tk()
window.title("Premium QR Code Generator")

tk.Label(window, text="Enter Data for QR Code:").pack(pady=10)
entry = tk.Entry(window, width=50)
entry.pack(pady=5)

tk.Button(window, text="Generate QR Code", command=generate_qr).pack(pady=20)

window.mainloop()
