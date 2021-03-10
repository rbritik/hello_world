from tkinter import *
from PIL import ImageTk, Image
root = Tk()

# Apps Title and logo
root.title("Image_Viewer")
root.iconbitmap('C:/Users/Acer/Downloads/sun.ico')

# Importing images
image_1 = ImageTk.PhotoImage(Image.open(r'C:\Users\Acer\Downloads\data_science\Computer Vision\Opencv\images\data\train\Ben Afflek\benAffleck (1).jpg'))
image_2 = ImageTk.PhotoImage(Image.open(r'C:\Users\Acer\Downloads\data_science\Computer Vision\Opencv\images\data\train\Ben Afflek\benAffleck (2).jpg'))
image_3 = ImageTk.PhotoImage(Image.open(r'C:\Users\Acer\Downloads\data_science\Computer Vision\Opencv\images\data\train\Ben Afflek\benAffleck (3).jpg'))
image_4 = ImageTk.PhotoImage(Image.open(r'C:\Users\Acer\Downloads\data_science\Computer Vision\Opencv\images\data\train\Ben Afflek\benAffleck (4).jpg'))
image_5 = ImageTk.PhotoImage(Image.open(r'C:\Users\Acer\Downloads\data_science\Computer Vision\Opencv\images\data\train\Ben Afflek\benAffleck (5).jpg'))
image_6 = ImageTk.PhotoImage(Image.open(r'C:\Users\Acer\Downloads\data_science\Computer Vision\Opencv\images\data\train\Ben Afflek\benAffleck (6).jpg'))

# Forming a list of images
image = [image_1,image_2, image_3, image_4, image_5, image_6]

# Adding Status
status = Label(root, text = 'image 1 of '+ str(len(image)), bd = 5, relief = SUNKEN, anchor = E )

# Function to change image Forward or backward
def change(imagenumber):
    global my_image, button_back, button_forward
    my_image.grid_forget() # To delete last image
    my_image = Label(image = image[imagenumber])
    
    # Changing image forward or backward
    button_forward = Button(root, text = '>>', command = lambda: change(imagenumber+1), fg = 'blue')
    button_back = Button(root, text = '<<', command = lambda: change(imagenumber-1),fg = 'green')
    
    status = Label(root, text = 'image '+str(imagenumber+1)+' of '+ str(len(image)), bd = 5, relief = SUNKEN, anchor = E )
    status.grid(row = 2, columnspan = 3, sticky = W+E)

    # If last image is reached then disabling forward button
    if imagenumber == len(image)-1:
        button_forward = Button(root, text = '>>', state = DISABLED)
    
    # If it is the initial image disable the back button
    if imagenumber == 0:
        button_back = Button(root, text = "<<", state = DISABLED)
    
    # Showing on the Screen
    button_forward.grid(row = 1, column = 2)
    button_back.grid(row = 1, column = 0)
    my_image.grid(row = 0, columnspan = 3)

# Showing Image    
my_image = Label(image = image_1)
my_image.grid(row = 0, columnspan = 3)

# Defining buttons
button_forward = Button(root, text = '>>', command = lambda: change(1), fg = 'blue')
button_back = Button(root, text = "<<" , state = DISABLED)
button_exit = Button(root, text = 'Exit', command = root.quit, fg = 'red') # If it is pressed then programm will be finished


button_back.grid(row = 1, column = 0)
button_exit.grid(row = 1, column = 1)
button_forward.grid(row = 1, column = 2, pady = 10)
status.grid(row = 2, columnspan = 3, sticky = W+E)

root.mainloop()