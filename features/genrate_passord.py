import secrets
import string




def generate_password():
        lower =  string.ascii_lowercase 
        upper = string.ascii_uppercase 
        ponct = string.punctuation
        digit = string.digits 
        password =[
            secrets.choice(lower),
            secrets.choice(upper),
            secrets.choice(ponct),
            secrets.choice(digit)]
        all_char = lower + upper + ponct + digit
        
        for _ in range(8) :
            password += [secrets.choice(all_char)]
        secrets.SystemRandom().shuffle(password)
        return ''.join(password) 