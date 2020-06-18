
# Import libraries 
from PIL import Image 
import pytesseract 
import sys 
from pdf2image import convert_from_path 
import os 
from os import listdir
from os.path import isfile, join


mypath = r"C:\Users\prasad\Desktop\SKT_writ\casestudy"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
# Path of the pdf   
#"\Aftab_Ahmad_Khan_vs_The_State_Of_Hyderabad_on_6_May,_1954.pdf"

''' 
Part #1 : Converting PDF to images 
'''
def pdf_to_text(PDF_file, name):
# Store all the pages of the PDF in a variable 
    pages = convert_from_path(PDF_file) 
    image_counter = 1
    for page in pages:
        filename = "page_"+str(image_counter)+".jpg"
        page.save(filename, 'JPEG')
        image_counter = image_counter + 1
        
    filelimit = image_counter-1
    outfile = str(name) + ".txt"
    f = open(outfile, "a") 
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
    for i in range(1, filelimit + 1):
        filename = "page_"+str(i)+".jpg"
        text = str(((pytesseract.image_to_string(Image.open(filename))))) 
        text = text.replace('-\n', '')
        f.write(text)
    f.close() 
for file in onlyfiles:
    print(file)
    #PDF_file = (str(mypath) +str("")+ str(file))
    PDF_file = "/".join((mypath, file))
    print(PDF_file)
    pdf_to_text(PDF_file, file)

# Counter to store images of each page of PDF to image 
    

# Iterate through all the pages stored above 
     

	# Declaring filename for each page of PDF as JPG 
	# For each page, filename will be: 
	# PDF page 1 -> page_1.jpg 
	# PDF page 2 -> page_2.jpg 
	# PDF page 3 -> page_3.jpg 
	# .... 
	# PDF page n -> page_n.jpg 
    	
	
	# Save the image of the page in system 
    	 

	# Increment the counter to update filename 
    	

''' 
Part #2 - Recognizing text from the images using OCR 
'''
	
# Variable to get count of total number of pages 
    

# Creating a text file to write the output 
    

# Open the file in append mode so that 
# All contents of all images are added to the same file 
    

    
# Iterate from 1 to total number of pages 
     

	# Set filename to recognize text from 
	# Again, these files will be: 
	# page_1.jpg 
	# page_2.jpg 
	# .... 
	# page_n.jpg 
    	

	# Recognize the text as string in image using pytesserct 
    	

	# The recognized text is stored in variable text 
	# Any string processing may be applied on text 
	# Here, basic formatting has been done: 
	# In many PDFs, at line ending, if a word can't 
	# be written fully, a 'hyphen' is added. 
	# The rest of the word is written in the next line 
	# Eg: This is a sample text this word here GeeksF- 
	# orGeeks is half on first line, remaining on next. 
	# To remove this, we replace every '-\n' to ''. 
    		 

	# Finally, write the processed text to the file. 
    	 

# Close the file after writing all the text. 
    
