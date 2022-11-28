import unittest
from ostoskori import Ostoskori
from tuote import Tuote


class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_ja_tavaroiden_arvot_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_yhden_tuotteen_lisaaminen(self):
        maito = Tuote("Maito", 2)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_ostoskorin_hinta_lisaamisen_jalkeen(self):
        maito = Tuote("Maito", 2)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.hinta(), 2)

    def test_kahden_tuotteen_lisaamisen_jalkeinen_maara_korissa(self):
        maito = Tuote("Maito", 2)
        limu = Tuote("Limu", 4)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(limu)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_tuotteen_lisaamisen_jalkeinen_hintakorissa(self):
        maito = Tuote("Maito", 2)
        limu = Tuote("Limu", 4)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(limu)

        self.assertEqual(self.kori.hinta(), 6)

    def test_kaksi_samaa_tuotetta_maara_oikein(self):
        maito = Tuote("Maito", 2)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kaksi_samaa_tuotetta_hinta_oikein(self):
        maito = Tuote("Maito", 2)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.hinta(), 4)

    def test_ostoskorissa_yksi_tuote(self):
        maito = Tuote("Maito", 2)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(len(self.kori.ostokset()), 1)

    def test_ostoskorissa_yksi_tuote_sen_lisaamisen_jalkeen(self):
        maito = Tuote("Maito", 2)
        self.kori.lisaa_tuote(maito)

        ostos = self.kori.ostokset()[0]

        self.assertEqual(ostos.tuotteen_nimi(), "Maito")
        self.assertEqual(ostos.lukumaara(), 1)

    def test_ostoskorissa_kaksi_tuotetta(self):
        maito = Tuote("Maito", 2)
        limu = Tuote("Limu", 4)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(limu)

        self.assertEqual(len(self.kori.ostokset()), 2)

    def test_ostoskorissa_yksi_ostus_mutta_2_tuotetta(self):
        maito = Tuote("Maito", 2)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(len(self.kori.ostokset()), 1)

    def test_ostoskorissa_kaksi_samaa_tuotetta(self):
        maito = Tuote("Maito", 2)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        ostos = self.kori.ostokset()[0]

        self.assertEqual(ostos.tuotteen_nimi(), "Maito")
        self.assertEqual(ostos.lukumaara(), 2)

    def test_ostoskorissa_yksi_tuote_kun_toinen_poistetaan(self):
        maito = Tuote("Maito", 2)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.kori.poista_tuote(maito)

        ostos = self.kori.ostokset()[0]

        self.assertEqual(ostos.tuotteen_nimi(), "Maito")
        self.assertEqual(ostos.lukumaara(), 1)

    