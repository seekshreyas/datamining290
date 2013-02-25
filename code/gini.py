#!/usr/bin/python
"""Script can be used to calculate the Gini Index of a column in a CSV file.

Classes are strings."""

import fileinput
import csv

(cmte_id, cand_id, cand_nm, contbr_nm, contbr_city, contbr_st, contbr_zip,
contbr_employer, contbr_occupation, contb_receipt_amt, contb_receipt_dt,
receipt_desc, memo_cd, memo_text, form_tp, file_num, tran_id, election_tp) = range(18)


############### Set up variables
# TODO: declare datastructures

############### Read through files

## defining a dictionary data structure for holding candidate data
elecDonations = {}


for row in csv.reader(fileinput.input()):
    if not fileinput.isfirstline():
        ###
        # TODO: replace line below with steps to save information to calculate
        # Gini Index
        #row[cand_nm], row[contbr_zip]
        ##/
        # cand = row[cand_nm]
        
        ## zip codes normalization (I a guessing the characters after 6 digits
        ## are for the post box which we dont need). 
        ## So I will just slice them off
		# zipCode = row[contbr_zip]

        ## candidate name normalization
        # take only last name and covert to lowercase
        candName = row[cand_nm].split(',')[0].lower()
        zipCode = row[contbr_zip]
        zipCode = zipCode[0:6]

       
        if candName in elecDonations:
        	elecDonations[candName].append(zipCode)
        else:
        	elecDonations.setdefault(candName, []).append(zipCode)
        	
     

# print elecDonations['obama']
## printing the Gini Index of Candidate Names
totalDonationNum = 0
for candidate in elecDonations:
	totalDonationNum = totalDonationNum + len(elecDonations[candidate])
	# print candidate, len(elecDonations[candidate])

sumfrac = 0
for candidate in elecDonations:
	frac = float(len(elecDonations[candidate])) / float(totalDonationNum)
	frac = frac ** 2

	print candidate, frac
	sumfrac = sumfrac + frac

###
# TODO: calculate the values below:

gini = 1- sumfrac  # current Gini Index using candidate name as the class
split_gini = 0  # weighted average of the Gini Indexes using candidate names, split up by zip code
##/

print "Total Donations %s" % totalDonationNum
print "Gini Index: %s" % gini
print "Gini Index after split: %s" % split_gini
