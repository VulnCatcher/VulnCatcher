path = "project path"

#Example of use
function."name_of_function" (path) # (see function.py file)

# Step 1 Compile the data7 utility and get the xmls from each dataset



# Step 2 extract the commits of vulnerabilities contained in the xml files from their hashes.(data7 tool)
# For this we use the file commit.py


# 3rd Step extract other corrected bugs

# The data tool7 does not directly extract the commits contennats all the corrected bugs must:
# ------- Perform a "git log --oneline | grep -e" bug "-e" fix "-i> fix.txt" in the corresponding data folder (openssl, wireshark, linux_kernel, systemd)


# 4th Step Parsing to extract the features
#call the "features extraction()" function with the path parameters and the nature of the features


#5th extract logs of each commits


#6th Extract IDF of each log


#Apply OneClass and Co-Training fuction on CSV extracted









