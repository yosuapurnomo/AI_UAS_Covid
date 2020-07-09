from builtins import float

import pandas as pd
import numpy as np


class Bayes:
    def __init__(self, gejala):
        self.df = pd.read_excel('DataSet.xlsx', header=0)
        print(self.df.head(5))
        self.gejala = gejala
        self.Positif()
        self.Negatif()

    def Positif(self):
        if self.df[(self.df['Usia'] == self.gejala[0]) & (self.df['Diagnosa'] == 'POSITIF')].__len__() != 0:
            print('Data Usia ada')
            usia = self.df[(self.df['Usia'] == self.gejala[0]) & (self.df['Diagnosa'] == 'POSITIF')].__len__() / \
                   self.df[self.df['Diagnosa'] == 'POSITIF'].__len__()
        else:
            print('Data Usia Tidak ada')
            if self.gejala[0] <= 25:
                usia = self.df[(self.df['Usia'] <= 25) & (self.df['Diagnosa'] == 'POSITIF')].__len__() / \
                       self.df[self.df['Diagnosa'] == 'POSITIF'].__len__()
            else:
                usia = self.df[(self.df['Usia'] > 25) & (self.df['Diagnosa'] == 'POSITIF')].__len__() / \
                       self.df[self.df['Diagnosa'] == 'POSITIF'].__len__()

        print(usia)
        demam = self.df[(self.df['Demam'] == self.gejala[1]) & (self.df['Diagnosa'] == 'POSITIF')].__len__() / self.df[
            self.df['Diagnosa'] == 'POSITIF'].__len__()
        print('demam : ', demam)
        batuk = self.df[(self.df['Batuk Kering'] == self.gejala[2]) & (self.df['Diagnosa'] == 'POSITIF')].__len__() / \
                self.df[self.df['Diagnosa'] == 'POSITIF'].__len__()
        print('batuk : ', batuk)
        tenggorokan = self.df[(self.df['Sakit Tenggorokan'] == self.gejala[3]) & (
                    self.df['Diagnosa'] == 'POSITIF')].__len__() / self.df[self.df['Diagnosa'] == 'POSITIF'].__len__()
        print('tengg : ', tenggorokan)
        kepala = self.df[(self.df['Sakit Kepala'] == self.gejala[4]) & (self.df['Diagnosa'] == 'POSITIF')].__len__() / \
                 self.df[self.df['Diagnosa'] == 'POSITIF'].__len__()
        print('kepala : ', kepala)
        lemas = self.df[(self.df['Lemas'] == self.gejala[5]) & (self.df['Diagnosa'] == 'POSITIF')].__len__() / self.df[
            self.df['Diagnosa'] == 'POSITIF'].__len__()
        print('lemas : ', lemas)
        sesak = self.df[(self.df['Sesak Nafas'] == self.gejala[6]) & (self.df['Diagnosa'] == 'POSITIF')].__len__() / \
                self.df[self.df['Diagnosa'] == 'POSITIF'].__len__()
        print('sesak : ', sesak)
        diagnosa = self.df[self.df['Diagnosa'] == 'POSITIF'].__len__() / self.df['Diagnosa'].__len__()
        print('Diagnosa : ', diagnosa)
        self.positifVal = usia * demam * batuk * tenggorokan * kepala * lemas * sesak * diagnosa
        print("Nilai Kemunculan Positif = ", self.positifVal)

    def Negatif(self):
        if self.df[(self.df['Usia'] == self.gejala[0]) & (self.df['Diagnosa'] == 'NEGATIF')].__len__() != 0:
            Usia = self.df[(self.df['Usia'] == self.gejala[0]) & (self.df['Diagnosa'] == 'NEGATIF')].__len__() / \
                   self.df[
                       self.df['Diagnosa'] == 'NEGATIF'].__len__()
        else:
            if self.gejala[0] <= 25:
                Usia = self.df[(self.df['Usia'] <= 25) & (self.df['Diagnosa'] == 'NEGATIF')].__len__() / \
                       self.df[
                           self.df['Diagnosa'] == 'NEGATIF'].__len__()
            else:
                Usia = self.df[(self.df['Usia'] > 25) & (self.df['Diagnosa'] == 'NEGATIF')].__len__() / \
                       self.df[
                           self.df['Diagnosa'] == 'NEGATIF'].__len__()

        print(Usia)
        demam = self.df[(self.df['Demam'] == self.gejala[1]) & (self.df['Diagnosa'] == 'NEGATIF')].__len__() / self.df[
            self.df['Diagnosa'] == 'NEGATIF'].__len__()
        batuk = self.df[(self.df['Batuk Kering'] == self.gejala[2]) & (self.df['Diagnosa'] == 'NEGATIF')].__len__() / \
                self.df[
                    self.df['Diagnosa'] == 'NEGATIF'].__len__()
        tenggorokan = self.df[(self.df['Sakit Tenggorokan'] == self.gejala[3]) & (
                    self.df['Diagnosa'] == 'NEGATIF')].__len__() / self.df[
                          self.df['Diagnosa'] == 'NEGATIF'].__len__()
        kepala = self.df[(self.df['Sakit Kepala'] == self.gejala[4]) & (self.df['Diagnosa'] == 'NEGATIF')].__len__() / \
                 self.df[
                     self.df['Diagnosa'] == 'NEGATIF'].__len__()
        lemas = self.df[(self.df['Lemas'] == self.gejala[5]) & (self.df['Diagnosa'] == 'NEGATIF')].__len__() / self.df[
            self.df['Diagnosa'] == 'NEGATIF'].__len__()
        sesak = self.df[(self.df['Sesak Nafas'] == self.gejala[6]) & (self.df['Diagnosa'] == 'NEGATIF')].__len__() / \
                self.df[
                    self.df['Diagnosa'] == 'NEGATIF'].__len__()
        diagnosa = self.df[self.df['Diagnosa'] == 'NEGATIF'].__len__() / self.df['Diagnosa'].__len__()

        self.negatifVal = Usia * demam * batuk * tenggorokan * kepala * lemas * sesak * diagnosa
        print("Nilai Kemunculan Negatif = ", self.negatifVal)

    def Likelihood(self):
        ProPos = self.positifVal / (self.positifVal + self.negatifVal)
        ProNeg = self.negatifVal / (self.positifVal + self.negatifVal)
        Hasil = np.array([ProPos, ProNeg]).argmax()
        print('Hasil Positif : ', ProPos, '\n', 'Hasil Negatif : ', ProNeg)
        if Hasil == 0:
            print("HASIL Akhir Menunjukan POSITIF DENGAN PROBALITAS : ", ProPos)
        else:
            print("HASIL Akhir Menunjukan NEGATIF DENGAN PROBALITAS : ", ProNeg)


if __name__ == '__main__':
    Usia = int(input("UMUR : "))
    demam = input("DEMAM YA/TIDAK : ").upper()
    batuk = input("Batuk YA/TIDAK : ").upper()
    tenggorokan = input("Sakit Tenggorokan YA/TIDAK : ").upper()
    kepala = input("Sakit Kepala YA/TIDAK : ").upper()
    lemas = input("Badan Lemas YA/TIDAK : ").upper()
    Sesak = input("Sesak Nafas YA/TIDAK : ").upper()
    Main = Bayes([Usia, demam, batuk, tenggorokan, kepala, lemas, Sesak])
    Main.Likelihood()
