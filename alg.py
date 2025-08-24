#Name: Erick Hambardzumyan
#Date: 23 August 2025
#Course: Automate Cybersecurity Tasks with Python Module 4- Python in practice
#Assignment: Activity create another algorithm


'''
Purpose: You are a security professional working at a health care company. As part of your job, you're required to regularly update a file that identifies the
employees who can access restricted content. The contents of the file are based on who is working with personal patient records. Employees are restricted access based
on their IP address. There is an allow list for IP addresses permitted to sign into the restricted subnetwork. There's also a remove list that identifies which
employees you must remove from this allow list. Your task is to create an algorithm that uses Python code to check whether the allow list contains any
IP addresses identified on the remove list. If so, you should remove those IP addresses from the file containing the allow list.
'''



# Create and initialize file variables
allow_file = "allow_list.txt"
remove_file = "remove_list.txt"

# Define function to convert file to a list object
def toList(imp_file):
    with open(imp_file, "r") as file:
        ip_addresses = file.read()
    ip_addresses = ip_addresses.split('\n')
    return ip_addresses  # Return list object

# Define a function to join back list to string object and write to file
def toString(file_name, aList):
    content = "\n".join(aList)
    with open(file_name, "w") as file:
        file.write(content)
    return content  # Return the string object

# Define function to format list by printing each list entry on newline
def formatList(aList):
    for element in aList:
        print(element)

# Convert list files to actual list object in Python
allow_list = toList(allow_file)
remove_list = toList(remove_file)

# Print initial allow_list list
print("Allow List:", allow_list)
separator_length = len("Allow List: " + str(allow_list))  # Dynamic length based on the print line
print("-" * separator_length)
print("--------------------------------------")  # Optional fixed length for consistency

# Format and print initial allow_list list
print("Formatted Allow List:\n")
formatList(allow_list)
separator_length = max(separator_length, len("Formatted Allow List:"))  # Update for the new longest line
print("-" * separator_length)
print("--------------------------------------")  # Optional fixed length for consistency

# Print remove_list list
print("Remove List:", remove_list)
separator_length = len("Remove List: " + str(remove_list))  # Dynamic length based on the print line
print("-" * separator_length)
print("--------------------------------------")  # Optional fixed length for consistency

# Format and print remove list
print("Formatted Remove List:\n")
formatList(remove_list)
separator_length = max(separator_length, len("Formatted Remove List:"))  # Update for the new longest line
print("-" * separator_length)
print("--------------------------------------")  # Optional fixed length for consistency

# Algorithm for removing any IP address from remove_list that is in allow_list
for element in allow_list:  #for any IP address in the allow_list
    if element in remove_list and element != "ip_addresses":    #if the IP address is in remove_list and is not the entry "ip_addresses"
        allow_list.remove(element)  #remove the IP address from allow_list

# Convert `allow_list` back to a string and write to file
allow_string = toString(allow_file, allow_list)

# Format and print updated allow_list (converted back to list for formatting)
print("Updated Allow List:\n")
formatList(allow_list)  # Use original allow_list for consistency
separator_length = max(separator_length, len("Formatted Updated Allow List:"))  # Update for the new longest line
print("-" * separator_length)
print("--------------------------------------")  # Optional fixed length for consistency