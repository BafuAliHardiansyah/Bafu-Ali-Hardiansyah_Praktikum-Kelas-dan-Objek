class Lingkaran(object):
   def __init__(self, phi, r):
      self.phi = phi
      self.jarijari = r
   def hitungLuaslingkaran(self):
      return self.phi * self.jarijari * self.jarijari

def main():
   # membuat objek pertama
   Luli1= Lingkaran(3.14, 5)

   # menggunakan objek pertama
   print('Objek Luli1')
   print('phi\t: ', Luli1.phi)
   print('jarijari\t: ', Luli1.jarijari)
   print('luas\t: ', Luli1.hitungLuaslingkaran())
   

   # membuat objek kedua
   Luli2 = Lingkaran(3.14, 1)

   # menggunakan objek kedua
   print('Objek Luli2')
   print('phi\t: ', Luli2.phi)
   print('jarijari\t: ', Luli2.jarijari)
   print('Luas\t= ', Luli2.hitungLuaslingkaran())

if __name__ == "__main__":
   main()
