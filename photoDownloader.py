from google_images_download import google_images_download   #importing the library

response = google_images_download.googleimagesdownload()   #class instantiation

collection = ['woman selfie young', 'woman mirror selfie teen', 'girl selfie', 'cute girl selfie', 'cute girl selfie instagram', 'cute girl selfie looks', 'cute girl selfie pinterest', 'cute girl selfie tumblr']

for i in range(0, len(collection)-1):

	arguments = {"keywords": collection[i],"limit":100,"print_urls":True}   #creating list of arguments
	paths = response.download(arguments)   #passing the arguments to the function
	print(paths)   #printing absolute paths of the downloaded images
