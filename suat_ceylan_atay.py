def giris_bilgisi():
    print("— Welcome to İSTİNYE Bank (v.0.1) —")
    choose = input("""
        1.Login
        2.Exit
        """)
    if choose == "1":
        print("İSTİNYE Bank")
    elif choose =="2":
        print("Istinye Bank wishes you a good day..")


giris_bilgisi()

ahmetaccount={
    "Name":"Ahmet",
    "Surname":"Sevgi",
    "Password":1234,
    "Balance":1000} #ahmetaccount ile bir dict. oluşturdum ve ahmet'e ait bilgileri içerisine atadım.

zeynepaccount={
    "Name":"Zeynep",
    "Surname":"Düş",
    "Password":4321,
    "Balance":1000}#zeynepaccount ile bir dict. oluşturdum ve zeynep'e ait bilgileri içerisine atadım.

def menu(name):# menü adında bir fonksiyon oluşturdum aynı zamanda giris fonksiyonu içerisinde bulunan "name"i burada tanıttığım için, bu fonk. içerisinde kullanabileceğim.
    global ahmetaccount
    global zeynepaccount
    print(f'-Welcome {name}! Please enter the number of the service:')#giris fonksiyonundaki kullanılan "name" burada görünecektir
    choose2=input("""
    1. Withdraw Money
    2. Deposit Money
    3. Transfer Money
    4. My Account Information
    5. Logout""") #choose2 adında değişken tanımlayıp, input ile kullanıcının göreceği menuyu içerisine yazdım.
    if choose2=="1":#eğer 1.seçenek seçilirse aşağıdaki işlemler gerçekleşecek
        if (name=="Ahmet"):#eğer name=ahmet ise if okunacak, değilse diğer if'e gidilecektir.
            Miktar1=int(input("Lütfen çekmek istediğiniz miktarı giriniz: "))#kullanıcıdan ne kadar nakit istediği soruluyor.
            if (ahmetaccount.get("Balance")<Miktar1):#eğer istenen para, kişinin mevcut parasından daha azsa diye kontrol ediliyor.
                print("Yetersiz bakiye.Güncel bakiyeniz:",ahmetaccount.get("Balance"))#bakiye yetersiz olduğu için, isteğe bağlı olarak kişi ana menüye yönlendirilecektşr.
                guidance()#bu def, kullanıcıyı ana menüye tekrar döndürmektedir.
            else:
                ahmetaccount['Balance']=ahmetaccount.get("Balance")-Miktar1
                print("Geriye kalan bakinez {} Tl dir. İşleminiz başarıyla gerçekleşmiştir. Ana menüye dönmek için 'q' tuşuna basınız.".format(ahmetaccount['Balance']))
                choose4 = input("q")
                if choose4 == "q":
                    menu(name)
        elif (name=="Zeynep"):
            Miktar2=int(input("Lütfen çekmek istediğiniz miktarı giriniz: "))
            if zeynepaccount.get("Balance")<Miktar2:
                print("Yetersiz bakiye. Ana menuye donmek için q'ye tıklayınız")
                choose3 = input("q")
                if choose3 == "q":
                    menu(name)
            else:
                zeynepaccount['Balance']=zeynepaccount.get("Balance")-Miktar2
                print("Geriye kalan bakinez {} Tl dir. İşleminiz başarıyla gerçekleşmiştir. Ana menüye dönmek için 'q' tuşuna basınız. ".format(zeynepaccount['Balance']))
                choose4 = input("q")
                if choose4 == "q":
                    menu(name)
    if choose2=="2":
        if (name == "Ahmet"):
            Miktar1= int(input("lütfen yatırılacak tutarı giriniz"))
            ahmetaccount['Balance'] = ahmetaccount.get("Balance") + Miktar1
            print("Geriye kalan bakinez {} Tl dir.İşleminiz başarıyla gerçekleşmiştir. Ana menüye dönmek için 'q'yu tuşlayınız. ".format(ahmetaccount['Balance']))
            choose4 = input("q")
            if choose4 == "q":
                menu(name)
        if (name == "Zeynep"):
            Miktar2 = int(input("lütfen yatırılacak tutarı giriniz"))
            zeynepaccount['Balance'] = zeynepaccount.get("Balance") + Miktar2
            print("Geriye kalan bakinez {} Tl dir.İşleminiz başarıyla gerçekleşmiştir. Ana menüye dönmek için q'yu tuşlayınız. ".format(zeynepaccount['Balance']))
            choose4 = input("q")
            if choose4 == "q":
                menu(name)
    if choose2=="3":
        if (name=="Ahmet"):
            eft1=int(input("Göndermek istediğiniz mik. giriniz."))
            if ahmetaccount.get("Balance")<eft1:
                print("Yetersiz bakiye, güncel bakiyeniz:", ahmetaccount.get("Balance"))
                print("Ana menüye dönmek için q'yu tuşlayınız.")
                choose4 = input("q")
                if choose4 == "q":
                    menu(name)
            elif ahmetaccount.get("Balance")>=eft1:
                zeynepaccount["Balance"]+=eft1
                ahmetaccount["Balance"] -= eft1
                print("işleminiz tamamlandı, yeni bakiyeniz:",ahmetaccount.get("Balance"))
                print("İşleminiz başarıyla gerçekleşmiştir. Ana menüye dönmek için q'yu tuşlayınız.")
                choose4 = input("q")
                if choose4 == "q":
                    menu(name)
        elif (name=="Zeynep"):
            eft2 = int(input("Göndermek istediğiniz mik. giriniz."))
            if zeynepaccount.get("Balance") < eft2:
                print("Yetersiz bakiye, güncel bakiyeniz:",zeynepaccount.get("Balance"))
                print("Ana menüye dönmek için q'yu tuşlayınız.")
                choose4 = input("q")
                if choose4 == "q":
                    menu(name)
            elif zeynepaccount.get("Balance") >= eft2:
                ahmetaccount["Balance"] += eft2
                zeynepaccount["Balance"] -= eft2
                print("işleminiz tamamlandı, yeni bakiyeniz:", zeynepaccount.get("Balance"))
                print("Ana menüye dönmek için q'yu tuşlayınız.")
                choose4 = input("q")
                if choose4 == "q":
                    menu(name)
    if choose2=="4":
        if name=="Ahmet":
            zaman()
            ahmet_bank_account_information()
            print("Ana menüye dönmek için q'yu tuşlayınız.")
            choose4 = input("q")
            if choose4 == "q":
                menu(name)
        elif name=="Zeynep":
            zaman()
            zeynep_bank_account_information()
            guidance()
    if choose2=="5":
        print("Istinye Bank wishes you a good day..")


def zaman():
    import datetime #1İmport ne işe yarar ?projeye harici modül dahil ederken kullanılır. 2.İmport ile time modülünü aktif ediyoruz.
    time = datetime.datetime.now() #tarih, saat ve milisaniye verileri time değişkenine tanımlanıyor.
    print("—— İSTİNYE Bank ——")
    print(time)#time değişkeni çağırılıyor.

def ahmet_bank_account_information():#ahmetin bilgilerini dict. üzerinden çeker. hemen value hem de key'i çekiyor.
    print("Hesap Bilgileriniz")
    for hesapbilgileri1 in ahmetaccount:
        print(hesapbilgileri1,ahmetaccount[hesapbilgileri1])

def zeynep_bank_account_information():
    print("Hesap Bilgileriniz")
    for hesapbilgileri2 in zeynepaccount:
        print(hesapbilgileri2, zeynepaccount[hesapbilgileri2])
#calistir2=menu(name)
#print(calistir2)

def guidance():#yönlendirme amaçlı oluşturulmuştur. Aynı kodu çok kez yazmamak için def içerisine aldım.
    choose3 = input("""
    1.Press "q" to return to the main menu.
    2.Press "e" to exit.""")
    if choose3 == "q":
        giris()
    else:
        print("Istinye Bank wishes you a good day..")


def giris():#kullanıcının giriş yaptığı bölüm
    name = input("User Name:")
    pasword = input("Password:")
    while not (((name == "Ahmet") and (pasword == "1234")) or ((name == "Zeynep") and (pasword == "4321"))):
        print("The username or password is invalid. Please try again.")
        name = input("User Name:")
        pasword = input("Password:")
        print(f'-Welcome {name} to İSTİNYE Bank (v.0.1)-')
    menu(name)


calistir=giris()


