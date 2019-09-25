

import sys
import durum
from PyQt5.QtWidgets import  QWidget,QPushButton, QGridLayout,QApplication,QHBoxLayout,QVBoxLayout, QDialog,QLabel

class Pencere(QWidget):
    def __init__(self):
      super().__init__()
      self.git()

    def git(self):

        self.liste=[]
        self.sol_bulunanlar_listesi=[]
        self.sag_bulunanlar_listesi = []
        self.yukari_bulunanlar_listesi = []
        self.yan_bulunanlar_listesi = []
        self.setFixedWidth(300)  # sabit genişlik ayarı
        self.setFixedHeight(300)
        self.birincioyuncudami=True
        self.toplam=0
        self.toplam2=0
        self.toplamPasifButonSayisi=0
        self.yazi=QLabel("0")
        self.kullanici1=QLabel("1.Kullanici:")
        self.arabosluk=QLabel("                          ")
        self.kullanici2= QLabel("2.Kullanici:")
        self.yazi2 = QLabel("0")
        h_box=QHBoxLayout()
        h_box.addWidget(self.kullanici1)
        h_box.addWidget(self.yazi)
        h_box.addWidget(self.arabosluk)
        h_box.addWidget(self.kullanici2)
        h_box.addWidget(self.yazi2)
        h_box.addStretch()
        v_box=QVBoxLayout()
        #v_box.addWidget(self.yazi)
        self.izgara = QGridLayout()
        for i in range(0, 12):
            for j in range(0, 9):
                self.buton=QPushButton()
                self.izgara.addWidget(self.buton,i,j)
                self.buton.setObjectName(str(i+1)+"."+str(j+1))
                self.izgara.setSpacing(0)
                self.buton.clicked.connect(self.Tikla)

        v_box.addLayout(h_box)
        v_box.addLayout(self.izgara)
        self.setLayout(v_box)
        self.show()

    def Tikla(self):
        self.gonderenButon= self.sender()
        self.dialog = QDialog()
        self.dialog.setWindowTitle("X -O Seçme Alanı ")
        h_box = QHBoxLayout()
        self.butonX=QPushButton("X")
        self.butonO=QPushButton("O")
        h_box.addWidget(self.butonX)
        h_box.addWidget(self.butonO)
        self.butonX.clicked.connect(self.fonk)
        self.butonO.clicked.connect(self.fonk)
        self.dialog.setLayout(h_box)
        self.dialog.exec()


    def fonk(self):
        hangiButon=self.sender()
        self.gonderenButon.setText(hangiButon.text())
        self.gonderenButon.setEnabled(False)
        ayrilacak_parca=self.gonderenButon.objectName().split(".")
        nesne=durum.harf(ayrilacak_parca[0],ayrilacak_parca[1],hangiButon.text())
        self.liste.append(nesne.goster())
        self.dialog.hide()
        self.kontrol(-1,-1,1,1,self.sol_bulunanlar_listesi)
        self.kontrol(-1, 1, 1, -1, self.sag_bulunanlar_listesi)
        self.kontrol(-1, 0, 1, 0, self.yukari_bulunanlar_listesi)
        self.kontrol(0, -1, 0, 1, self.yan_bulunanlar_listesi)
        self.birincioyuncudami=not self.birincioyuncudami
        self.toplamPasifButonSayisi+=1
        if(self.toplamPasifButonSayisi==108):
            if(self.toplam>self.toplam2):
                print("Birinci oyuncu kazandı..")
            elif(self.toplam2>self.toplam):
                print("İkinci oyuncu kazandı.")

            else:
                print("Berabere bitti.")



    def kontrol(self,deger1,b,c,d,gonder_liste):
        sayi = 0
        for i in range(0, len(self.liste)):

            if self.liste[i][2] == "O":

                ilk_deger = int(self.liste[i][0])
                ikinci_deger = int(self.liste[i][1])

                for i in range(0, len(self.liste)):
                    if (int(self.liste[i][0]) == ilk_deger+deger1 and int(self.liste[i][1]) == ikinci_deger +b and
                            self.liste[i][2] == "X"):
                        sayi += 1
                    if (int(self.liste[i][0]) == ilk_deger+c and int(self.liste[i][1]) == ikinci_deger + d and
                            self.liste[i][2] == "X"):
                        sayi += 1

                    if (sayi == 2):
                        nesne = durum.harf(self.liste[i][0], self.liste[i][1], self.liste[i][2])
                        a = nesne.goster()

                        sayi = 0
                        if a not in gonder_liste:

                            #self.toplam += 1
                            #self.yazi.setText(str(self.toplam))
                            gonder_liste.append(a)
                            if self.birincioyuncudami:
                                self.toplam += 1
                                self.yazi.setText(str(self.toplam))
                            else:
                                self.toplam2 += 1
                                self.yazi2.setText(str(self.toplam2))


                sayi = 0


app=QApplication(sys.argv)
pencere=Pencere()
sys.exit(app.exec_())

