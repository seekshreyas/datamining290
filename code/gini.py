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
elecDonations = {'candidate' : '', 'donationFrom' :''}


for row in csv.reader(fileinput.input()):
    if not fileinput.isfirstline():
        ###
        # TODO: replace line below with steps to save information to calculate
        # Gini Index
        #row[cand_nm], row[contbr_zip]
        ##/
        # cand = row[cand_nm]

        ## candidate name normalization
        candName = row[cand_nm].split(',')[0] #take only the last name
        candName = candName.lower() # convert to lowercase

        if 'candName' in elecDonations:
        	elecDonations[candName].append(row[contbr_zip])
        else:
        	elecDonations[candName] = row[contbr_zip]


print elecDonations.keys()

###
# TODO: calculate the values below:
gini = 0  # current Gini Index using candidate name as the class
split_gini = 0  # weighted average of the Gini Indexes using candidate names, split up by zip code
##/

print "Gini Index: %s" % gini
print "Gini Index after split: %s" % split_gini
