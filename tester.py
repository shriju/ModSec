import unittest
import validator

class Test_Validator(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.obj = validator.Validate()
        pass
    
    @classmethod
    def tearDownClass(cls):
        del cls.obj
        pass
    
    def test_email(self):
        self.assertEqual(True, self.obj.valid_email("abc@gmail.com"))
        self.assertEqual(False, self.obj.valid_email("Abc@.com"))
        self.assertEqual(False, self.obj.valid_email("1@7@company.com"))

    def test_name(self):
        self.assertEqual(True, self.obj.valid_nameof_cust("Abc Def"))
        self.assertEqual(False, self.obj.valid_nameof_cust("Abc"))
    
    def test_reg_id(self):
        self.assertEqual(True, self.obj.valid_regid(125))
        self.assertEqual(False, self.obj.valid_regid(280))
    
if __name__ == "__main__":
    unittest.main()