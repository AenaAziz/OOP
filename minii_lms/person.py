import re
class Person:
    def __init__(self, name, age=None, date_of_birth=None, gender=None, email=None, phone_no=None):
        if isinstance(name, Person):
            self._name = name._name
            self._age = name._age
            self._date_of_birth = name._date_of_birth
            self._gender = name._gender
            self._email = name._email
            self._phone_no = name._phone_no
        elif isinstance(name, str):
            self._name, self._age, self._date_of_birth, self._gender, self._email, self._phone_no = self._validation(name, age, date_of_birth, gender, email, phone_no)    
        else:
            raise TypeError("invalid type for the person data")   

    @property
    def name(self): return self._name    
    @name.setter
    def name(self, new_name):
        self._name = self._name_validation(new_name)

    @property
    def age(self): return self._age
    @age.setter
    def age(self, new_age):
        self._age = self._age_validation(new_age)

    @property
    def date_of_birth(self): return self._date_of_birth
    @date_of_birth.setter
    def date_of_birth(self, new_date_of_birth):
        self._date_of_birth = self._birth_date_validation(new_date_of_birth)

    @property
    def gender(self): return self._gender
    @gender.setter
    def gender(self, new_gender):
        self._gender = self._gender_validation(new_gender)

    @property
    def email(self): return self._email
    @email.setter
    def email(self, new_email):
        self._email = self._email_validation(new_email)

    @property
    def phone_no(self): return self._phone_no
    @phone_no.setter
    def phone_no(self, new_phone_no):
        self._phone_no = self._phone_no_validation(new_phone_no)

    def __str__(self):
        return (f" Name is {self._name}\n"
                f" Age is {self._age}\n"
                f" Date of Birth is {self._date_of_birth}\n"
                f" Gender is {self._gender}\n"
                f" Email is {self._email}\n"
                f" Phone number is {self._phone_no}")    

    def __repr__(self):
        return (f" Name:{self._name}\n"
               f" Age: {self._age}\n"
               f" Date of Birth: {self._date_of_birth}\n"
               f" Gender: {self._gender}\n" 
               f" Email: {self._email}\n"
               f" Phone number: {self._phone_no}")     
         
    def _name_validation(self, name):
        if not isinstance(name, str): raise TypeError("Invalid name type")
        if not name.isalpha(): raise TypeError("name must only contain letters")
        return name.rstrip().capitalize() 

    def _age_validation(self, age):
        if isinstance(age, str) and age.isdigit():
            age = int(age)
        elif isinstance(age, int):
            if age < 0: raise ValueError("Age must be positive")
        else:
            raise TypeError("Invalid age type")    
        return age
        
    def _birth_date_validation(self, date_of_birth):
        if not isinstance(date_of_birth, str): raise TypeError("Invalid date of birth")
        parts = re.split(r"[-/]", date_of_birth)
        if not len(parts) == 3: raise TypeError("Invalid date_of_birth")  

        if not parts[1] in [f"{i:02}" for i in range(1,13)]: raise ValueError("Invalid Month number for the birth data")
        self._date_validation(parts)
        self._year_validation(parts)
        return date_of_birth
          
    def _date_validation(self, parts):
        if not parts[0].isdigit(): raise ValueError("Invalid Date for the birth data")
        date = int(parts[0])
        if date > 31: raise ValueError("date must be 1-31")
        if date == 31 and parts[1] in ['04', '06', '09', '11']: raise ValueError("date '31st' does not come with this month")
        if parts[1] == '02' and date > 29:
            raise ValueError("Feb has max 29 days")

    def _year_validation(self, parts):
        year = int(parts[2])
        if year > 2025: raise ValueError("Future birth year not allowed")         

    def _gender_validation(self, gender):
        if not isinstance(gender, str): raise TypeError("Invalid gender type")
        if not gender in ["Female", "Male", "Non-Binary"]: raise TypeError("Invalid gender")
        return gender
        
    def _email_validation(self, email):
        if not isinstance(email, str): raise TypeError("Invalid email type")
        parts = list(email)

        if not parts[0].isalpha():
            raise TypeError("email must start with a letter")
        if ' ' in email: raise TypeError("Email can not contain space")
        if '@' not in email:
            raise TypeError("email must contain'@'")
        if not email.endswith(('.com' , '.org', '.pk', '.edu.pk', '.net.pk', '.gov.pk')):
            raise TypeError("email must end with a valid domain")
        return email
        
    def _phone_no_validation(self, phone_no):
        if not isinstance(phone_no, str): raise TypeError("Invalid phone number")
        self._phone_numbers_validation(phone_no)
        self._phone_no_length_validation(phone_no)
        self._choose_no(phone_no)
        return phone_no
    
    def _phone_numbers_validation(self, phone_no):
        if phone_no.startswith("+"):
            numbers = phone_no[1:]
        else:
            numbers = phone_no    
        if not numbers.isdigit():    
            raise ValueError("phone no must contain digits only except(leading '+')")
            
    def _phone_no_length_validation(self, phone_no):  
        if not (len(phone_no) == 11 or len(phone_no) == 13):
            raise ValueError("phone number must contain 'eleven' or 'thirteen' digits")  

    def _normal_phone_no_validation(self, phone_no, companies_phone_no):
         if not phone_no.startswith(companies_phone_no):
              raise ValueError("Pak phone number must start with a valid code")
         if not len(phone_no) == 11: raise ValueError("phone number contains 'eleven' digits")

    def _whatsapp_no_validation(self, phone_no, companies_phone_no):  
        whatsapp_no = tuple(code.replace("0", "+92", 1) for code in companies_phone_no)
        if not phone_no.startswith(whatsapp_no):
            raise ValueError("Pak whatsapp number must start with valid SIM code")
        if not len(phone_no) == 13: raise ValueError("whatsapp phone number contains 'thirteen' digits") 

    def _choose_no(self, phone_no):  
        companies_phone_no = ("0300","0301","0302","0303","0304","0305","0320","0321","0322","0323","0324","0325","0310","0311","0312","0313","0314","0315","0316","0317","0318","0319", "0340","0341","0342","0343","0344","0345","0346","0347","0348","0349","0330","0331","0332","0333","0334","0335","0336","0337","0338","0339")  
        
        if phone_no.startswith('0'):
            self._normal_phone_no_validation(phone_no, companies_phone_no)
            
        elif phone_no.startswith('+92'): 
            self._whatsapp_no_validation(phone_no, companies_phone_no)
        else:
            raise ValueError("Pak phone number code starts with '0' or '+92' with valid SIM code")   
            
    def _validation(self, name, age, dob, gender, email, phone_no):
        name = self._name_validation(name)
        age = self._age_validation(age)
        dob = self._birth_date_validation(dob)
        gender = self._gender_validation(gender)
        email = self._email_validation(email)
        phone_no = self._phone_no_validation(phone_no)
        return name, age, dob, gender, email, phone_no
    

        


                    







            






    