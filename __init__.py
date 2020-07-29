import random 
from Faker.Fake_Py.name import Name
from Faker.Fake_Py.email import Email

class Fake_User:
      @property
      def fake_name(self):
      	  a  = Name
      	  return random.choice(a)
      @property
      def fake_email(self):
           a = Email
           return random.choice(a)
           
Fake = Fake_User()    	  
if __name__ == '__main__':
    print(Fake.fake_name)
    print(Fake.fake_email)