import pandas as pd
import numpy as np

class Bayes:
    def __init__(self, gejala):
        self.df = pd.read_excel('DataSet.xlsx', header=0)
        # print(self.df)
        self.gejala = gejala
        self.Positif()
        self.Negatif()
    def Positif(self):
        demam = self.df[(self.df['Demam'] == self.gejala[0]) & (self.df['Diagnosa'] == 'POSITIF')].__len__() / self.df[
            self.df['Diagnosa'] == 'POSITIF'].__len__()
        batuk = self.df[(self.df['Batuk Kering'] == self.gejala[1]) & (self.df['Diagnosa'] == 'POSITIF')].__len__() / self.df[
            self.df['Diagnosa'] == 'POSITIF'].__len__()
        tenggorokan = self.df[(self.df['Sakit Tenggorokan'] == self.gejala[2]) & (self.df['Diagnosa'] == 'POSITIF')].__len__() / self.df[
            self.df['Diagnosa'] == 'POSITIF'].__len__()
        kepala = self.df[(self.df['Sakit Kepala'] == self.gejala[3]) & (self.df['Diagnosa'] == 'POSITIF')].__len__() / self.df[
            self.df['Diagnosa'] == 'POSITIF'].__len__()
        lemas = self.df[(self.df['Lemas'] == self.gejala[4]) & (self.df['Diagnosa'] == 'POSITIF')].__len__() / self.df[
            self.df['Diagnosa'] == 'POSITIF'].__len__()
        sesak = self.df[(self.df['Sesak Nafas'] == self.gejala[5]) & (self.df['Diagnosa'] == 'POSITIF')].__len__() / self.df[
            self.df['Diagnosa'] == 'POSITIF'].__len__()
        diagnosa = self.df[self.df['Diagnosa'] == 'POSITIF'].__len__() / self.df['Diagnosa'].__len__()

        self.positifVal = demam * batuk * tenggorokan * kepala * lemas * sesak * diagnosa
        print("Nilai Kemunculan Positif = ", self.positifVal)
    def Negatif(self):
        demam = self.df[(self.df['Demam'] == self.gejala[0]) & (self.df['Diagnosa'] == 'NEGATIF')].__len__() / self.df[
            self.df['Diagnosa'] == 'NEGATIF'].__len__()
        batuk = self.df[(self.df['Batuk Kering'] == self.gejala[1]) & (self.df['Diagnosa'] == 'NEGATIF')].__len__() / self.df[
            self.df['Diagnosa'] == 'NEGATIF'].__len__()
        tenggorokan = self.df[(self.df['Sakit Tenggorokan'] == self.gejala[2]) & (self.df['Diagnosa'] == 'NEGATIF')].__len__() / self.df[
            self.df['Diagnosa'] == 'NEGATIF'].__len__()
        kepala = self.df[(self.df['Sakit Kepala'] == self.gejala[3]) & (self.df['Diagnosa'] == 'NEGATIF')].__len__() / self.df[
            self.df['Diagnosa'] == 'NEGATIF'].__len__()
        lemas = self.df[(self.df['Lemas'] == self.gejala[4]) & (self.df['Diagnosa'] == 'NEGATIF')].__len__() / self.df[
            self.df['Diagnosa'] == 'NEGATIF'].__len__()
        sesak = self.df[(self.df['Sesak Nafas'] == self.gejala[5]) & (self.df['Diagnosa'] == 'NEGATIF')].__len__() / self.df[
            self.df['Diagnosa'] == 'NEGATIF'].__len__()
        diagnosa = self.df[self.df['Diagnosa'] == 'NEGATIF'].__len__() / self.df['Diagnosa'].__len__()

        self.negatifVal = demam * batuk * tenggorokan * kepala * lemas * sesak * diagnosa
        print("Nilai Kemunculan Negatif = ", self.negatifVal)

    def Likelihood(self):
        ProPos = self.positifVal / (self.positifVal + self.negatifVal)
        ProNeg = self.negatifVal / (self.positifVal + self.negatifVal)
        Hasil = np.array([self.positifVal, self.negatifVal]).argmax()
        print(Hasil)
        if Hasil == 0:
            print("HASIL POSITIF DENGAN PROBALITAS : ", ProPos)
        else:
            print("HASIL NEGATIF DENGAN PROBALITAS : ", ProNeg)

if __name__ == '__main__':
    demam = input("DEMAM YA/TIDAK : ").upper()
    batuk = input("Batuk YA/TIDAK : ").upper()
    tenggorokan = input("Sakit Tenggorokan YA/TIDAK : ").upper()
    kepala = input("Sakit Kepala YA/TIDAK : ").upper()
    lemas = input("Badan Lemas YA/TIDAK : ").upper()
    Sesak = input("Sesak Nafas YA/TIDAK : ").upper()
    Main = Bayes([demam, batuk, tenggorokan, kepala, lemas, Sesak])
    Main.Likelihood()