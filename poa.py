import os
import sys
import requests

from urllib.parse import urljoin
from bs4 import BeautifulSoup

# Introduction
print("-----------------------------")
print("***    IMPORTANT NOTES    ***")
print("-----------------------------\n")
print("1. TO BE USED FOR 1983 to 2021 JUDGMENT ONLY.")
print("2. Number of counts or files means the number of files that are the in a particular year directory and that they are correctly numbered when navigating. The number of files can be inspected manually by navigating to the TanzLii webpage of a particular year. \nInitial count can 1 or as shown in your file inspection. For flexiblity, you are advised to add five on the total counts or number of files.")
print("3. Saving path is the location to where you files that will be downloaded will be saved. You are recommended to choose to write only the name of the folder, and that folder will by default be saved on the current directory or location that you are running the script. Otherwise you can write the full path location.")
print("4. Decision year is the year of which the judgment decision was made and documents were uploaded. The years range from 1983 to-date.")
print("5. URL choice has only 3 options for file directories. Choice are as follows in order of choice 1, 2 and 3.\nhttps://tanzlii.org/tz/judgment/court-appeal-tanzania/2021/1-0\nhttps://tanzlii.org/tz/judgment/court-appeal-tanzania/2021/1-1\nhttps://tanzlii.org/tz/judgment/court-appeal-tanzania/2021/1")

input("\nPress Enter to continue...")

# Banner
msg1 = "Starting web scrapping..."
msg2 = "Starting counter..."
print("\n"+msg1+"\n"+msg2+"\n")

# User Inputs
counts = int(input("Enter the initial count or file number (must be above zero): "))
# print("Number of counts is: " + counter)

counter = int(input("Enter number of counts or files (add five to the number for flexibility): "))
# print("Number of counts is: " + counter)

saving_path = str(input("Enter full path location or folder name: "))
# print("Full path location or folder is: " + saving_path)

decision_year = int(input("Enter decision year (from 1983 to-date): "))
# print("Decision year is: " + decision_year)

count = counts

print('\nChoose URL Type: ')
print('1 - Digit with hyphene zero. E.g. 1-0')
print('2 - Digit with hyphene one. E.g. 1-1')
print('3 - Digit only without hyphene. E.g. 1')

choice = int(input('\nEnter your choice: '))

# For -0 URL
if choice == 1:
	while count < int(counter):
		# Banner
		msg3 = "\nDownloading file number: "+str(count)
		print(msg3)

		url = "https://tanzlii.org/tz/judgment/court-appeal-tanzania/"+str(decision_year)+"/"+str(count)+"-0"

		#If there is no such folder, the script will create one automatically
		folder_location = r'{}'.format(saving_path)
		if not os.path.exists(folder_location):os.mkdir(folder_location)

		response = requests.get(url)
		soup= BeautifulSoup(response.text, "html.parser")
		for link in soup.select("a[href$='.pdf']"):
			#Name the pdf files using the last portion of each link which are unique in this case
			filename = os.path.join(folder_location,link['href'].split('/')[-1])
			with open(filename, 'wb') as f:
				f.write(requests.get(urljoin(url,link['href'])).content)

		# Banner
		msg4 = "File name downloaded: "+link['href'].split('/')[-1]
		msg5 = "Saved location: "+folder_location
		msg6 = "Full path: "+filename
		print(msg4+"\n"+msg5+"\n"+msg6+"\n\n***\n")

		count += 1

# For -1 URL
elif choice == 2:
	while count < int(counter):
		# Banner
		msg3 = "\nDownloading file number: "+str(count)
		print(msg3)

		url = "https://tanzlii.org/tz/judgment/court-appeal-tanzania/"+str(decision_year)+"/"+str(count)+"-1"

		#If there is no such folder, the script will create one automatically
		folder_location = r'{}'.format(saving_path)
		if not os.path.exists(folder_location):os.mkdir(folder_location)

		response = requests.get(url)
		soup= BeautifulSoup(response.text, "html.parser")
		for link in soup.select("a[href$='.pdf']"):
			#Name the pdf files using the last portion of each link which are unique in this case
			filename = os.path.join(folder_location,link['href'].split('/')[-1])
			with open(filename, 'wb') as f:
				f.write(requests.get(urljoin(url,link['href'])).content)

		# Banner
		msg4 = "File name downloaded: "+link['href'].split('/')[-1]
		msg5 = "Saved location: "+folder_location
		msg6 = "Full path: "+filename
		print(msg4+"\n"+msg5+"\n"+msg6+"\n\n***\n")

		count += 1

# For non hyphene URL
elif choice == 3:
	while count < int(counter):
		# Banner
		msg3 = "\nDownloading file number: "+str(count)
		print(msg3)

		url = "https://tanzlii.org/tz/judgment/court-appeal-tanzania/"+str(decision_year)+"/"+str(count)

		#If there is no such folder, the script will create one automatically
		folder_location = r'{}'.format(saving_path)
		if not os.path.exists(folder_location):os.mkdir(folder_location)

		response = requests.get(url)
		soup= BeautifulSoup(response.text, "html.parser")
		for link in soup.select("a[href$='.pdf']"):
			#Name the pdf files using the last portion of each link which are unique in this case
			filename = os.path.join(folder_location,link['href'].split('/')[-1])
			with open(filename, 'wb') as f:
				f.write(requests.get(urljoin(url,link['href'])).content)

		# Banner
		# msg4 = "File name downloaded: "+link['href'].split('/')[-1]
		msg5 = "Saved location: "+folder_location
		# msg6 = "Full path: "+filename
		# print(msg4+"\n"+msg5+"\n"+msg6+"\n\n***\n")
		print(msg5+"\n\n***\n")

		count += 1
else:
	sys.exit('\nInvalid choice')

# Banner
msg7 = "Terminating counter..."
msg8 = "Terminating web scrapping..."
msg9 = "Process Completed."
msg10 = "*** SEMA, KIMEUMANA! ***"
print(msg7+"\n"+msg8+"\n"+msg9+"\n\n"+msg10+"\n")