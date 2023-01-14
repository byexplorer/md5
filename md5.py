import hashlib 

print("""
---------------------------


         byexplorer.xyz

 Md5 & Sha256 Çevirme Toolu


----------------------------

""")

print("Yazıyı Md5'e Çevirme = 1")
print("\n")
print("Yazıyı Sha256'ya Çevirme= 2")
print("\n")
while True:
    a=int(input("Yapmak İstediğiniz İşlemi Giriniz: "))
    if a==1:
        print("Yazıyı md5'e çevirme")
        m=input("Lütfen Bir Yazı Giriniz: ")
        md5=hashlib.md5(m.encode('utf-8')).hexdigest()
        print("md5 Şifreniz: ",md5)
    elif a==2:
        print("yazıyı sha256'ya çevirme")
        s=input("bir yazı giriniz: ")
        sha256=hashlib.sha256(s.encode('utf-8')).hexdigest()
        print("sha256 şifreniz:" ,sha256)
    else:
        print("Geçersiz Seçim..")


