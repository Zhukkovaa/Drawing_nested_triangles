import tkinter as tk  # Module for creating a graphical user interface
import math  # Module for performing mathematical operations

# Variable to store the size of the last deleted triangle
last_deleted_h = None

def can_draw_triangle(h):
    min_size = 0  # Minimum triangle size
    # Check if the sizes of 'h' are within the acceptable range
    if min_size < h:
        return True
    else:
        return False

def validate_input(input_num, error_label):  # Function to validate input data in the text field
    if input_num == "":  # Check if the input string is empty
        error_label.config(text="")  # If empty, clear the error label text
        return True  # Return True, indicating valid input
    try:
        value = int(input_num)  # Try to convert the input value to an integer
        if value > 0:  # Check if the value is a positive number
            error_label.config(text="")  # If positive, clear the error label text
            return True  # Return True, indicating valid input
        else:  # If the value is not within the valid range, set the error label text
            error_label.config(text="Enter a positive integer greater than 0")
            return False  # Return False, indicating invalid input
    except ValueError:  # If the input value cannot be converted to an integer, set the error label text
        error_label.config(text="Enter a numeric value")
        return False  # Return False, indicating invalid input

def validate_input_wrapper(P):
    return validate_input(P, error_label)

def draw_triangle():
    global h, canvas, triangles, h_increment, last_deleted_h
    # Initialize the value of h if it is not defined
    # The size of the first triangle is always the same
    if h is None:
        h = 500  # Initial value of 'h'
    #If the entered value of h has not been used yet, save it
    if h_increment is None:
        h_increment = int(h_entry.get()) ## This block of code checks if the h variable is not defined (equal to None) and sets its initial value to 500

    h_entry.delete(0, tk.END)#Clear the text field
    h_entry.config(state=tk.DISABLED)#Disable text field editing

    if last_deleted_h is not None:#If there is a saved size of the last deleted triangle, use it
        h = last_deleted_h
        last_deleted_h = None

    if can_draw_triangle(h):# Calculate the coordinates of the vertices of an equilateral triangle
        x_center = width_canvas / 2
        y_center = height_canvas / 2
        side_length = 2 * h / math.sqrt(3)# Length of the triangle's side

        x1 = x_center
        y1 = y_center - h / 2
        x2 = x_center - side_length / 2
        y2 = y_center + h / 2 - (h / 5)
        x3 = x_center + side_length / 2
        y3 = y_center + h / 2 - (h / 5)

        # Draw a triangle with the current 'h' value
        triangle = canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill="", outline="black")
        # Add the triangle to the list of triangles
        triangles.append(triangle)
        # Decrease the 'h' value by the increment
        h -= h_increment
    else:
        # Cannot draw with the given parameters, display a message
        error_label.config(text="You cannot draw a smaller triangle")

def delete_last_triangle():
    global canvas, triangles, last_deleted_h, error_label

    if len(triangles) > 0:
        # Get the last drawn triangle
        last_triangle = triangles.pop()  # Remove the last triangle from the list

        # Get and save the size of the last deleted triangle
        coords = canvas.coords(last_triangle)
        x1, y1, x2, y2, x3, y3 = coords
        side_length = max(x1, x2, x3) - min(x1, x2, x3)
        last_deleted_h = (side_length * math.sqrt(3)) / 2

        # Check if the warning needs to be hidden
        if can_draw_triangle(last_deleted_h):
            error_label.config(text="")

        # Remove the triangle from the canvas
        canvas.delete(last_triangle)

def on_key_press(event):
    if event.keysym == "Return":
        # If the Enter key is pressed, draw a triangle
        draw_triangle()
    elif event.keysym.lower() == "d":
        # If the 'd' key (regardless of case) is pressed, delete the last triangle
        delete_last_triangle()
    elif event.keysym == "Escape":
        # If the Esc key is pressed, close the window
        root.destroy()
if __name__ == "__main__":
    # Create the application window
    root = tk.Tk()
    root.title("Lab Work №1. Variant №9")

    width_canvas = 600
    height_canvas = 600

    # Create a canvas with dimensions 600x600 pixels
    canvas = tk.Canvas(root, width=width_canvas, height=height_canvas)
    canvas.pack(side=tk.LEFT)

    # Create a label and an entry field for entering 'h'
    input_frame = tk.Frame(root)
    input_frame.pack(side=tk.RIGHT, padx=10, pady=10)

    data_label = tk.Label(input_frame, text="Enter a step size and press Enter to draw")
    data_label.grid(row=0, columnspan=4, padx=5, pady=5)

    h_label = tk.Label(input_frame, text="Enter h value:")
    h_label.grid(row=2, column=0, padx=5, pady=5)

    # Add validation to the 'h_entry' text field
    validate_input_cmd = root.register(validate_input_wrapper)
    h_entry = tk.Entry(input_frame, validate="key")
    h_entry.config(validatecommand=(validate_input_cmd, "%P"))
    h_entry.grid(row=2, column=1, padx=5, pady=5)

    # Create a label for displaying errors
    error_label = tk.Label(input_frame, fg="red")
    error_label.grid(row=3, columnspan=2, padx=5, pady=5)

    # Create a list to store triangles
    triangles = []

    # Variables to store 'h' and 'h_increment' values
    h = None
    h_increment = None

    # Bind key press events to the window
    root.bind("<Key>", on_key_press)

    # Start the main event loop
    root.mainloop()
