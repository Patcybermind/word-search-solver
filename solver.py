import cv2
import numpy as np
import pytesseract
import ocr
import engine

img = cv2.imread("images/image.png")
ocr_result = ocr.get_letters(img)

print('results:')
print(ocr_result)

# get number of characters per line
width = int(input("Enter the number of characters per line: "))

# convert the new line characters to spaces
ocr_result_line = ocr_result.replace('\n', ',')

# remove the last comma and add a comma at the beggining
ocr_result_line = ocr_result_line[:-1]
ocr_result_line = "," + ocr_result_line

# reverse the string
ocr_result_line_reversed = ocr_result_line[::-1]
print(ocr_result_line_reversed)

# make a table of the characters
ocr_result_table = ""
for i in range(int(len(ocr_result_line_reversed)/width / 2)):
    # add newline to the end of each line
    ocr_result_table += ocr_result_line_reversed[i*width*2:(i+1)*width*2] + "\n"

print(ocr_result_table)
# write the table to a file
file_to_edit = open("table.txt", "w")
file_to_edit.write(ocr_result_table)
file_to_edit.close()

# get user confirmation that all is correct
print("Table written to table.txt you can replace the characters 7 with the correct characters.")
input("Press Enter to continue...")

# read the table from the file
file_to_read = open("table.txt", "r")
corrected_ocr_result_table = file_to_read.read()
file_to_read.close()

print(corrected_ocr_result_table)
corrected_ocr_result_table = corrected_ocr_result_table.replace(",", "")

# transform the table to a 2d matrix
word_matrix = []
for i in range(len(corrected_ocr_result_table.split("\n"))):
    word_matrix.append(list(corrected_ocr_result_table.split("\n")[i]))

print(word_matrix)

print(word_matrix[1][2])
engine.solve(word_matrix)