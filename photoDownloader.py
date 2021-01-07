from google_images_download import google_images_download   #importing the library

response = google_images_download.googleimagesdownload()   #class instantiation

# Configure
#############################
collection = ['', '', '']
limit = 1
#############################

for i in range(0, len(collection)-1):
	# Creating list of arguments
	arguments = {"keywords": collection[i],"limit":limit,"print_urls":True}   
	# Passing the arguments to the function
	paths = response.download(arguments)   
	# Printing absolute paths of the downloaded images
	print(paths)   
