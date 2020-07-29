import random 
class Fake_User:
      def __init__(self):
           pass
      def name(self):
          return [ 
                  'Aksa' 'Arion', 'Aliando', 'Deago',
						'Arvin','Aliando', 'Axelle', 'Azada',         
						'Adhitama','Azura','Abhimanyu', 'Abayomi',            
						'Azri',  'Alvaro','Arkana',
						 'Arrayan','Andhra','Aydin' 'Abrisam',      
						'Achazia', 'Nana Cans', 'Endak Soeahgarman',
						'Didi soeahrto', 'MarkZelfof', 'Bagas', 'Dwi Arsa',
						'Windia Chan', 'Agus', 'Ivaa', 'Aric Prtama',
						'Wibu', 'Sheilan', 'Amelia', 'Isma', 'Wuiq',
						 'Abimanyu chan', 'ucup', 'otong', 'marfel',
						 'Donat Trump', 'Satiawan', 'Jodi', 'Misba',
						 'Sgiri', 'Zero Twon', 'Joni', 'Jarjit Sight',
						 'Jarjit', 'Petrtick', 'Sodek Monata', 'Sarmani',
						'Abinaya', 'Juliana', 'Aryo Susanto', 'Aryono',
						 'Abimanyi', 'Asep', 'Angita', 'jamrud', 'iswa',
						 'abi kusini', 'Johan Prasetyo', 'Bahul', 'Munir',
						 ]
      @property
      def fake_name(self):
      	  a  = self.name()
      	  return random.choice(a)
      def email(self):
           return [
           'aditiya@gmail.com', 'Joni@gmail.com',
           'Aksa@gamil.com', 'Arion@yahoo.com', 'Axelle@yahoo.com',
           'Abinaya@yahoo.com', 'Kang_Nolep@gmail.com',
            'TertawA.@gmail.com', 'Tio@yahoo.com',
           'bondan@yahoo.com', 'Telaso@gmail.com',
            'Jonoku@gmail.com', 'Miftahul@gmail.com',
            'Kangcosplay@gamil.com', 'praksos@gamil.com',
           'Lio@yahho.com', 'Apapun@gamil.com', 'Jangalah@gamil.com',
           'spotifay@gmail.com', 'rxking@gmail.com',
           'sanmicrosys@yahho.com', 'Jordianan@yahoo.com',
           'angita@gmail.com', 'adiman@gmail.com',
           'siyakan@gmail.com', 'denisan@gmail.com',
          'denisan@yahoo.com', 'bimakan@gmail.com',
          'jasawanan@yahoo.com', 'alfa@gmail.com'
           ]
      @property
      def fake_email(self):
           a = self.email()
           return random.choice(a)
           
Fake = Fake_User()    	  
if __name__ == '__main__':
	A = Fake_User()
	for i in range(5):
	    print(A.fake_email)
	    print(A.fake_name)