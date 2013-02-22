#!/usr/bin/python
"""Script can be used to calculate the Gini Index of a set of contributions
based on the candidate name."""

import fileinput
import csv
from collections import Counter
from collections import defaultdict

(cmte_id, cand_id, cand_nm, contbr_nm, contbr_city, contbr_st, contbr_zip,
contbr_employer, contbr_occupation, contb_receipt_amt, contb_receipt_dt,
receipt_desc, memo_cd, memo_text, form_tp, file_num, tran_id, election_tp) = range(18)

############### Set up variables
gini = 0
zipcode = defaultdict(Counter)
classes = Counter()

############### Read through files
for row in csv.reader(fileinput.input()):
    if not fileinput.isfirstline():
        classes[row[cand_nm]] += 1
        zipcode[row[contbr_zip]][row[cand_nm]] += 1

def gini_index(classes):
    """Calculates the Gini Index given a dictionary of class names to counts"""

    total = sum(classes.values())
    return 1 - sum( (float(c)/total)**2 for c in classes.values())

gini = gini_index(classes)
total = sum(cnt for zp in zipcode.values() for cnt in zp.values())
split_gini = sum( sum(cl.values()) * gini_index(cl) for cl in zipcode.values()) / total
#for zp, cnts in zipcode.iteritems():
#   print "%s %s" % (zp, gini_index(cnts))

print "Gini Index: %s" % gini
print "Gini Index after split: %s" % split_gini
print "debug: %r" % classes
