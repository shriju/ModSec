import logger as log
import re
#------------------------------importing complete-----------------------------------

class Validate:

    # Six different types of validations, each called by valid_all() as needed.
    
    def valid_namesof_region_prdt_catg(self, val):
        condition = [(len(v) < 40) for v in val]
        return True if all(condition) else False

    def valid_nameof_cust(self, val):
        condition = (len(val) < 40) and (len(val.split()) > 1)
        return True if condition else False
        
    def valid_addr(self, val):
        condition = (len(val) < 200)
        return True if condition else False
    
    def valid_email(self, val):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

        condition = re.fullmatch(regex, val)
        return True if condition else False

    def valid_regid(self, val):
        condition = (0 <= val <= 255)
        return True if condition else False

    def valid_pid_cid_sid_prc(self, val):
        condition = [(0 <= v <= 65535) for v in val]
        return True if all(condition) else False
    
    #
    # This method calls other methods according to type of column.
    
    def valid_all(self, table, row):
        if table=="regions":
            eval = [self.valid_regid(row[0]),
                    self.valid_namesof_region_prdt_catg((row[1],))]
            return True if all(eval) else False
        
        elif table=="products":
            eval = [self.valid_pid_cid_sid_prc((row[0], row[3])),
                    self.valid_namesof_region_prdt_catg((row[1], row[2]))]
            return True if all(eval) else False
        
        elif table=="customers":
            eval = [self.valid_pid_cid_sid_prc((row[0],)),
                    self.valid_namesof_region_prdt_catg((row[1],)),
                    self.valid_email(row[2]),
                    self.valid_addr(row[3])]
            return True if all(eval) else False
            
        else:
            eval = [self.valid_pid_cid_sid_prc((row[0], row[1], row[2])),
                    self.valid_regid(row[4])]
            return True if all(eval) else False