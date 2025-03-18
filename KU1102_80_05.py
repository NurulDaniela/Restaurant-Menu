# Program_PembelianMakananOnline
# Menerima masukan pilihan Restaurant dengan aplikasi AMEN
# memilih makanan yang akan di beli

# KAMUS
# MenuPilihan, TitikPinpoint, PilihanResto, a, b, c  : int
# Restaurant, MenuKFC, MenuMcDonald, MenuMixue, MenuHipotesa, MenuAGBebas, MenuDominos, MenuSateTaichan, MenuElThizy : arr of str
# MenuKFC, MenuMcDonald, MenuMixue, MenuHipotesa, MenuAGBebas, MenuDominos, MenuSateTaichan, MenuElThizy : arr of int
# ArrayTT, ArrayHarga, ArrayHarga1, ArrayHarga2, ArrayHarga3, ArrayTT, ArrayTT1, ArrayTT2, ArrayTT3, ArrayLaris, Hargalaris, ArrayAwal, Hargafix, HasilResto : arr of arr
# Definisi fungsi restaurant terdekat
def Restau(PilihanResto,TitikPinpoint):
    # menghasikan pilihan restau dari suatu prosedur

    # KAMUS LOKAL 1
    # i                                                                           : int
    # TempatMakan, Menu, Menufix, ArrayMenu, ArrayMenu1, ArrayMenu2, ArrayMenu3   : array of str (array of array)

    #ALGORITMA LOKAL 1
    print("------------------------------------")
    ArrayMenu1      = [MenuMcDonald , MenuMixue , MenuRMIkonyo]
    ArrayMenu2      = [MenuKFC, MenuHipotesa , MenuAGBebas]
    ArrayMenu3      = [MenuDominos, MenuSateTaichan, MenuElThizy]
    ArrayMenu       = [ArrayMenu1, ArrayMenu2, ArrayMenu3]
    TempatMakan     = ArrayTT[TitikPinpoint-1]
    print("Menu dari" , TempatMakan[PilihanResto-1])
    Menu = ArrayMenu[TitikPinpoint-1]
    Menufix = Menu[PilihanResto-1]
    return Menufix
# Definisi fungsi restaurant terlaris
def Restaularis(PilihanResto):
    # menghasilkan pilihan Restaularis dari prosedur

    # KAMUS LOKAL 2 
    # i                        : int
    # Menufix, Menularis       : array of str (array of array)
    # Hargafix, Hargalaris     : array of int (array of array)

    # ALGORITMA LOKAL 2
    Menularis       = [MenuMixue, MenuSateTaichan, MenuElThizy , MenuDominos , MenuAGBebas]
    print("------------------------------------")
    print("Menu dari" , ArrayLaris[PilihanResto-1])
    Menufix = Menularis[PilihanResto-1]
    return Menufix
# Defini prosedur pembayaran
def Pembayaran (HasilResto,Hargafix):
    # menghasilkan total pembayaran dari prosedur

    # KAMUS LOKAL 3
    # PilihanMenuRestau, BerapaBanyak, Bayar, Total, i : int
    # pilih_ulang_Pilihan                              : str
    # PilihanBayar                                     : arr of str
    # sum                                              : 0

    # ALGORITMA LOKAL 3
    for i in range(5):
        print (i+1 ,'.' , HasilResto[i] , "  ............   Rp." , Hargafix[i])
    print("------------------------------------")
    PilihanBayar  = ["Gopay", "Debit card", "Tunai"]
    PilihanMenuRestau = int(input("Pilih salah satu menu : "))
    BerapaBanyak = int(input("Berapa banyak  yang anda inginkan? : "))
    pilih_ulang_Pilihan = str(input("Apakah akan memilih kembali (y/n) : "))
    Total = BerapaBanyak*Hargafix[PilihanMenuRestau-1]
    sum = 0
    sum = sum + Total
    while pilih_ulang_Pilihan!="n":
        PilihanMenuRestau = int(input("Pilih salah satu menu : "))
        BerapaBanyak = int(input("Berapa banyak yang Anda inginkan? : "))
        Total = BerapaBanyak*Hargafix[PilihanMenuRestau-1]
        sum = sum + Total 
        pilih_ulang_Pilihan = str(input("Apakah Anda akan memilih kembali (y/n) : "))
    else:
        print("Harga total yang harus Anda bayar sebesar Rp." + str(sum))
        print("\t\t\t==============================================\t\t\t")
        print("\t\t\t\t     Pilih Pembayaran     \t\t\t\t")
        print("\t\t   Gopay  \t\t Debit card   \t\t Tunai \t\t")
        print("\t\t     1      \t   \t    2       \t\t 3        \t\t")
        print("\t\t\t==============================================\t\t\t")
        Bayar = int(input("Anda ingin bayar melalui apa : "))
        print ("Total Pembayaran Anda Rp." + str(sum) + ". Anda akan membayar melalui " + PilihanBayar[Bayar-1])
        if Bayar ==1:
            print("\t\t\t --- ! Selamat, Anda mendapatkan promo AMEN dari Go-pay ! --- \t\t\t")
            TerimaPromo = str(input("Apakah anda akan menerimanya (y/n) : "))
            if TerimaPromo == "y":
                HargaPromo = sum - sum*(0.3)
                print ("Anda mendapatkan promo sebesar 30%. Anda hanya perlu membayar Rp." + str(HargaPromo))
                print("\t\t   ===    Terima Kasih telah berbelanja di AMEN FOOD      ===\t\t")
            else :
                print ("Total Pembayaran Anda Rp." + str(sum) + ". Anda akan membayar melalui Rp." + PilihanBayar[Bayar-1])
                print("\t\t   ===    Terima Kasih telah berbelanja di AMEN FOOD      ===\t\t")
        else:
             print("\t\t   ===    Terima Kasih telah berbelanja di AMEN FOOD      ===\t\t")
    return

# ALGORITMA UTAMA
# Mengoutputkan bentuk awal aplikasi
print("-------------------------------------------------------------------------------------------------------")
print("\t\t\t        Selamat datang di AMEN FOOD           \t\t\t")
print("-------------------------------------------------------------------------------------------------------")
print("\t\t\t\t         Pilih Menu          \t\t\t\t")
print("\t\t\t  Terdekat  \t\t\t  Terlaris   \t\t\t")
print("\t\t\t     1      \t\t\t     2       \t\t\t")
#   Memasukkan menu pilihan
MenuPilihan = int (input("\t\t\t\t    Masukkan Pilihan anda  "))
print("\t\t\t==============================================\t\t\t")
# Mengisi Array yang akan digunakan
Restaurant      = ["KFC" , "McDonald " , "Mixue" , "Rumah Padang Ikonyo" , "Hipotesa", "Ayam Geprek Bebas", "Dominos", "Sate Taichan", "ElThizy" ]
# Array KFC
MenuKFC         = ["Nasi Ayam" , "Spagethi" , "Yakiniku" , "Float" , "Kebab"]
HargaKFC        = [ 17000 , 12000 , 16000 , 15000 , 10000 ]
# Array McDonald
MenuMcDonald    = ["Ayam Panas" , "Big Mac" , "Cheese Burger" , "McFlury" , "Kentang"]
HargaMcDonald   = [ 18000 , 28000 , 22000 , 15000 , 10000 ]
# Array Mixue
MenuMixue       = ["Mi Shake Strawberry" , "Smoothies with ice cream" , "Mi Sundae" , "Lucky Sundae" , "Boba Sundae"]
HargaMixue      = [ 18000 , 18000 , 18000 , 18000 , 18000 ]
# Array RMIkonyo
MenuRMIkonyo    = ["Paket Ayam Bakar" , "Paket Ayam Gulai" , "Paket Dendeng Merah" , "Paket Gulai Cincang", "Paket Gulai Kikil"]
HargaRMIkonyo   = [ 27000 , 27000 , 25000 , 25000 , 35500 ]
# Array Hipotesa
MenuHipotesa    = ["Nasi Goreng" , "Nasi Ayam Suir" , "Nasi Kornet" , "Ayam Goreng" ,"Ayam Suir"]
HargaHipotesa   = [ 11000 , 16500 , 14000 , 10000 , 10000 ]
# Array AGBebas
MenuAGBebas     = ["Ayam Geprek Original" , "Menu Paket Nasi" , "Nasi Ayam Geprek" , "Ayam Geprek Sambal Matah" , "Ayam Geprek Sambal Bawang"]
HargaAGBebas    = [ 16000 ,24000 ,21000 ,18000 ,16000 ]
# Array Dominos
MenuDominos     = ["Medium Premium Pizza", "Lima Pizza" , "Extravaganza Pizza", "BBQ Meatball Potato Bake", "Meatzza Pizza"]
HargaDominos    = [ 45000 , 210000 , 83000 , 36500 , 83000 ]
# Array SateTaichan
MenuSateTaichan = ["Sate Taichan Ori/Pedas", "Sate Campur Ori/Pedas", "Sate telur puyuh", "Sate Usus", "Nasi"]
HargaSateTaichan= [ 17000 , 15000 , 2500 , 12000 , 4000 ]
# Array ElThizy
MenuElThizy     = ["Ayam Teriyaki", "Ayam El Rich", "Cumi Black Pepper", "Ayam Asam Manis", "Sop ayam/daging"]
HargaElThizy    = [ 15000 , 15000 , 16000 , 14000 , 15000 ]
# Array untuk masuk ke array lain
ArrayHarga1     = [HargaMcDonald , HargaMixue , HargaRMIkonyo]
ArrayHarga2     = [HargaKFC, HargaHipotesa , HargaAGBebas]
ArrayHarga3     = [HargaDominos, HargaSateTaichan, HargaElThizy]
ArrayTT1        = [Restaurant[1],Restaurant[2],Restaurant[3]]
ArrayTT2        = [Restaurant[0],Restaurant[4],Restaurant[5]]
ArrayTT3        = [Restaurant[6],Restaurant[7],Restaurant[8]]
ArrayLaris      = [Restaurant[2], Restaurant[7],Restaurant[8],Restaurant[6],Restaurant[5]]
ArrayTT         = [ArrayTT1 , ArrayTT2 ,ArrayTT3]
ArrayHarga      = [ArrayHarga1, ArrayHarga2, ArrayHarga3]
Hargalaris      = [HargaMixue, HargaSateTaichan, HargaElThizy , HargaDominos , HargaAGBebas]


# Jika menu pilihan yang dipilih adalah 1
if MenuPilihan == 1:
    print("\t\t\t\t     Titik Pin Point     \t\t\t\t")
    print("\t\t   ITB  \t Universitas Padjajaran   \t IPDN \t\t")
    print("\t\t     1      \t\t    2    \t\t    3   \t\t")
    TitikPinpoint = int (input("\t\t\t\t    Masukkan Pilihan anda  ")) # Memasukkan TitikPinpoint pengguna berada
    print("\t\t\t==============================================\t\t\t")
    print("Restoran di dekat Anda ")
    ArrayAwal = ArrayTT[TitikPinpoint-1]
    for a in range (0,3):
        print (a+1 ,'.' , ArrayAwal[a] )
    PilihanResto = int(input("Pilihan Anda : "))
    Harga = ArrayHarga[TitikPinpoint-1]
    Hargafix = Harga[PilihanResto-1]
    HasilResto = Restau(PilihanResto,TitikPinpoint)
    Pembayaran (HasilResto,Hargafix)
else: # Jika menu pilihan yang dipilih adalah 2
    print ("Restoran terlaris daerah Jatinangor :")
    for a in range (0,5):
        print (a+1 ,'.' , ArrayLaris[a])
    PilihanResto = int(input("Pilihan Anda : "))
    Hargafix = Hargalaris[PilihanResto-1]
    HasilResto = Restaularis(PilihanResto)
    Pembayaran (HasilResto,Hargafix)
