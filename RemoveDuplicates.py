import re                                                  #Tool Written by Jkerai1 https://github.com/jkerai1
def remove_duplicate():
    # opens txt in r mode as one long string and assigns to var
    records  = open('CLSID list.txt', 'r').read()
    # .split() removes excess whitespaces from str, return str as list
    records = re.split("\s{2,}", records)
    clean_list = []                                   # empty list to store non-duplicate e-mails
    
    for record in records:                          # for loop to append non-duplicate records to clean list
        if record not in clean_list:
            clean_list.append(record)
    return clean_list
    records.close()
CLSID_no_duplicate_records = open('CLSID_no_duplicate_records.txt', 'w')

# function to convert clean_list 'list' elements in to strings
for record in remove_duplicate():
  # .strip() method to remove commas
  #  record = record.strip(',')
    CLSID_no_duplicate_records.write(f"{record}\n")
# close CLSID_no_duplicate_records.txt file
CLSID_no_duplicate_records.close()

remove_duplicate() ## Duplicates refer to CLSIDs and not by application!
