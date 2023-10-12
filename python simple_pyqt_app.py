import sys
import PyQt5
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel

# Create a PyQt Application
app = QApplication(sys.argv)

# Create a QMainWindow (the main application window)
window = QMainWindow()

# Set window properties (title, size)
window.setWindowTitle("Simple PyQt Application")
window.setGeometry(100, 100, 400, 200)

# Create a button
button = QPushButton("Click me", window)

# Create a label for displaying messages
label = QLabel(window)

# Define a function to display a message when the button is clicked
def display_message():
    label.setText("Hello, PyQt!")

# Connect the button's "clicked" signal to the display_message function
button.clicked.connect(display_message)

# Move and resize the button and label
button.setGeometry(150, 50, 100, 30)
label.setGeometry(150, 100, 200, 30)

# Show the window
window.show()

# Start the PyQt application event loop
sys.exit(app.exec_())