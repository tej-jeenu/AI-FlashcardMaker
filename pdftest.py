from pdf2image import convert_from_path
 
 
# Store Pdf with convert_from_path function
firstpage = int(input("What is the first page to start scanning: "))
lastpage = int(input("what is the last page you wanna start scanning: "))
images = convert_from_path('compsci.PDF')
 
