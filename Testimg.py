import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO


image_url = "https://cdn.dummyjson.com/product-images/beauty/essence-mascara-lash-princess/1.webp"


response = requests.get(image_url)
img_data = response.content
image = Image.open(BytesIO(img_data))


root = tk.Tk()
root.title("Ảnh từ mạng")

image = image.resize((300, 200))
tk_image = ImageTk.PhotoImage(image)


label = tk.Label(root, image=tk_image)
label.pack()

root.mainloop()
