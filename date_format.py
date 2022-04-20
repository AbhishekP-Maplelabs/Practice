"""
module:2
description:to convert yyyy/mm/dd format to dd/mm/yyyy format
"""
import re
def change_date_format(date_1):
    """
        returns the changed date format
    """
    return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', date_1)
DATE_1 ="2026-01-02"
print("Original date in YYY-MM-DD Format: ",DATE_1)
print("New date in DD-MM-YYYY Format: ",change_date_format(DATE_1))
