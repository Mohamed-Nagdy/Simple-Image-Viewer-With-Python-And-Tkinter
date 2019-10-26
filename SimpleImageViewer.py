'''

    Created By Mohamed Nagdy
    This program is a simple image viewer using python and tkinter
    to use this program just add the paths of all your images you want to view them in imagesList list
    and just use it and run ^_^

'''

# importing the libraries to use
from tkinter import *
from PIL import Image, ImageTk

# this counter is used for point to the image in the view
counter = 0

# this to create the window
root = Tk()

# this function for the next button to get the next image
def next():
    # define all the global variables to use them in our function
    global nextButton
    global previousButton
    global imagesList
    global counter
    global imageRead
    global image
    global container

    # this line to remove the image from the viewer to put the next image
    container.grid_forget()

    # check if the counter is equal to the length of the images list
    if counter == len(imagesList)-1:
        # if the counter is equal to it we disable the next button and create a new previous button
        nextButton = Button(root, text='>>', width=30, bg='yellow', fg='red', state=DISABLED, command=next)
        previousButton = Button(root, text='<<', width=30, bg='yellow', fg='red', command=previous)

    # if the counter is not equal to the length of the list
    else:
        # add one to the counter to point to the next image
        counter += 1
        # declare a new next and previous buttons
        nextButton = Button(root, text='>>', width=30, bg='yellow', fg='red', command=next)
        previousButton = Button(root, text='<<', width=30, bg='yellow', fg='red', command=previous)

        # read the next image from the list and resize it to 500*600 and show it on the container
        imageRead = Image.open(imagesList[counter])
        image = ImageTk.PhotoImage(imageRead.resize((500, 600), Image.ANTIALIAS))
        container = Label(root, image=image)

    # put all the elements on the root container
    container.grid(column=0, row=0, columnspan=2)
    nextButton.grid(column=1, row=1)
    previousButton.grid(column=0, row=1)

# this function for previous button to show the previous button on the viewer
def previous():
    # define all the global variables to use them in our function

    global nextButton
    global previousButton
    global imagesList
    global counter
    global imageRead
    global image
    global container

    # this line to remove the image from the viewer to put the next image
    container.grid_forget()

    # check if the counter is equal to zero
    if counter == 0:
        # if the counter is equal to it we disable the previous button and create a new next button
        nextButton = Button(root, text='>>', width=30, bg='yellow', fg='red', command=next)
        previousButton = Button(root, text='<<', width=30, bg='yellow', fg='red', state=DISABLED, command=previous)
    else:
        # sub one from the counter to point to the previous image
        counter -= 1

        # declare a new next and previous buttons
        nextButton = Button(root, text='>>', width=30, bg='yellow', fg='red', command=next)
        previousButton = Button(root, text='<<', width=30, bg='yellow', fg='red', command=previous)

        # read the previous image from the list and resize it to 500*600 and show it on the container
        imageRead = Image.open(imagesList[counter])
        image = ImageTk.PhotoImage(imageRead.resize((500, 600), Image.ANTIALIAS))
        container = Label(root, image=image)

    # put all the elements on the root container
    container.grid(column=0, row=0, columnspan=2)
    nextButton.grid(column=1, row=1)
    previousButton.grid(column=0, row=1)


# create the first show of our image viewer and the images list
nextButton = Button(root, text='>>', width=30, bg='yellow', fg='red', command=next)
previousButton = Button(root, text='<<', width=30, bg='yellow', fg='red', command=previous)
imagesList = ['images/1.jpg', 'images/2.jpg', 'images/3.jpg', 'images/4.jpg', 'images/5.jpg', 'images/6.jpg', 'images/7.jpg']

# read the fist image from the list and put it on the container
imageRead = Image.open(imagesList[0])
image = ImageTk.PhotoImage(imageRead.resize((500, 600), Image.ANTIALIAS))
container = Label(root, image=image)

# show all elements on the root container
container.grid(column=0, row=0, columnspan=2)
nextButton.grid(column=1, row=1)
previousButton.grid(column=0, row=1)

# start the root main loop
root.mainloop()