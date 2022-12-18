import pyautogui  # import the pyautogui library
import pytesseract  # import the pytesseract library
from PIL import Image  # import the Image module from the Pillow library

# Take a screenshot using PyAutoGUI
image = pyautogui.screenshot()

# Save the screenshot to a file
image.save('screenshot.png')

# Load the image file using the Image module from the Pillow library
im = Image.open('screenshot.png')

# Extract the text from the image using Tesseract
text = pytesseract.image_to_string(im)

# Print the extracted text
print(text)

#This code will take a screenshot of the current screen, 
#save it to a file called "screenshot.png", and then use Tesseract to extract the text from the image.
# The extracted text will be printed to the console.