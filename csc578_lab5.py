class JXWUtil:
    allowable_key_chars = ['2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 
                           'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'p', 
                           'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    @staticmethod
    def check_licence(email, key):
        key = key.strip().lower()
        if JXWUtil.test_key(email, key):
            return True
        
        if '@' in email:
            company_name = email.split('@')[1]
            if JXWUtil.test_key(company_name, key):
                return True
            
            while '.' in company_name:
                company_name = company_name.split('.')[1]
                if JXWUtil.test_key(company_name, key):
                    return True
                
        return False

    
    @staticmethod
    def test_key(licence_name, key):
        return key == JXWUtil.generate_code(licence_name, True) or key == JXWUtil.generate_code(licence_name, False)

    @staticmethod
    def generate_code(seed, force_lower_case=True):
        bloop = seed.strip()
        if force_lower_case:
            bloop = bloop.lower()
        hash_value = JXWUtil.calculate_hash(bloop)
        return 'jx' + JXWUtil.hash_to_licence_string(hash_value)

    @staticmethod
    def hash_to_licence_string(seed):
        v_number = ""
        for _ in range(6):
            c = JXWUtil.allowable_key_chars[seed & 0x1F]
            v_number = c + v_number
            seed >>= 5
        return v_number

    @staticmethod
    def calculate_hash(input_str):
        h = 0
        for char in input_str:
            h = 31 * h + ord(char)
        return h


def generate_valid_key(email):
    key = JXWUtil.generate_code(email)
    return key

def register():
    email = input("Enter your email address: ")
    generated_key = generate_valid_key(email)
    if JXWUtil.check_licence(email, generated_key):
        print(f"You have registered JXWorkBench.\nPlease restart JXplorer.")
        print(f"Success!")
        print(f"Your license key is: {generated_key}")

if __name__ == "__main__":
    register()

