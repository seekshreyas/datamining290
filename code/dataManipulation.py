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
donationToCandidate={}

for row in csv.reader(fileinput.input()):
    if not fileinput.isfirstline():
    	# take only the last name
    	candName = row[cand_nm].split(',')[0].lower()


    	amt = float(row[contb_receipt_amt])
        zipCode = row[contbr_zip]
        zipCode = zipCode[0:2]

        # recordList = {zipCode: row[contb_receipt_amt]}

        # if (candName =='obama') or (candName == 'romney'):
        # 	if candName in donationToCandidate:
        # 		donationToCandidate[candName].append(recordList)
        # 	else:
        # 		donationToCandidate.setdefault(candName, []).append(recordList)
        # else:
        # 	if 'other' in donationToCandidate:
        # 		donationToCandidate['other'].append(recordList)
        # 	else:
        # 		donationToCandidate.setdefault('other', []).append(recordList)

        
       	# print candName
        if zipCode in donationToCandidate:
        	if candName in donationToCandidate[zipCode]:
        		
        		currentamt = donationToCandidate[zipCode][candName]
  
        		currentamt = float(currentamt) + amt
        		
        		donationToCandidate[zipCode][candName] = currentamt
        	else:
        		if (candName=='obama'):
        			newRecord = {candName:amt}
        			# print newRecord
        			donationToCandidate[zipCode] = newRecord

        		elif(candName=='romney'):
        			newRecord = {candName:amt}
        			# print newRecord
        			donationToCandidate[zipCode] = newRecord
        		else:
        			# donationToCandidate[zipCode] = {'other':amt}
        			newRecord = {'other':amt}
        			# print newRecord
        			donationToCandidate[zipCode] = newRecord
        else:
        	# print candName
        	if candName =='obama':
        		# newRecord = {zipCode: {candName:amt}}
        		donationToCandidate[zipCode] = {candName:amt}
        	elif candName == 'romney':
        		donationToCandidate[zipCode] = {candName:amt}
        	else:
        		# newRecord = {zipCode: {'other':amt}}
        		# donationToCandidate.update(newRecord)	
        		donationToCandidate[zipCode] = {'other':amt} 
        		print candName, donationToCandidate[zipCode]
       	
       			

print donationToCandidate