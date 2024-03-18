import logger as log
import numpy as np
import re

class Validate:
    #
    # Six different types of validations, each called as needed.
    def valid_namesof_region_prdt_catg(self, val):
        if len(val) < 40:
            return True
        else:
            return False
    
    def valid_nameof_cust(self, val):
        if len(val) < 40 and len(val.split()) > 1:
            return True
        else:
            return False
        
    def valid_addr(self, val):
        if len(val) < 200:
            return True
        else:
            return False
    
    def valid_email(self, val):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if (re.fullmatch(regex, val)):
            return True
        else:
            return False

    def valid_regid(self, val):
        if 0 <= val <= 255:
            return True
        else:
            return False

    def valid_pid_cid_sid_prc(self, val):
        if (0 <= val <= 65535):
            return True
        else:
            return False
    
    #
    # This method calls other methods according to type of column.
    def valid_all(self, table, row):
        if table=="regions":
            eval = [self.valid_regid(row[0]),
                    self.valid_namesof_region_prdt_catg(row[1])]
            if all(eval):
                return True
            else:
                return False
        
        elif table=="products":
            eval = [self.valid_pid_cid_sid_prc(row[0]),
                    self.valid_namesof_region_prdt_catg(row[1]),
                    self.valid_namesof_region_prdt_catg(row[2]),
                    self.valid_pid_cid_sid_prc(row[3])]
            if all(eval):
                return True
            else:
                return False
        
        elif table=="customers":
            eval = [self.valid_pid_cid_sid_prc(row[0]),
                    self.valid_namesof_region_prdt_catg(row[1]),
                    self.valid_email(row[2]),
                    self.valid_addr(row[3])]
            if all(eval):
                    return True
            else:
                return False
            
        else:
            eval = [self.valid_pid_cid_sid_prc(row[0]),
                    self.valid_pid_cid_sid_prc(row[1]),
                    self.valid_pid_cid_sid_prc(row[2]),
                    self.valid_regid(row[4]),
                    ]
            if all(eval):
                return True
            else:
                return False