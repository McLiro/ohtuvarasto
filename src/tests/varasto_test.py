import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)
        saatu_maara = self.varasto.ota_varastosta(2)
        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)
        self.varasto.ota_varastosta(2)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_nollatilavuus_nollataan(self):
        varasto = Varasto(0)
        self.assertAlmostEqual(varasto.tilavuus, 0)
        self.assertAlmostEqual(varasto.saldo, 0)

    def test_negatiivinen_alku_saldo_nollataan(self):
        varasto = Varasto(10, -5)
        self.assertAlmostEqual(varasto.saldo, 0)

    def test_alku_saldo_suurempi_kuin_tilavuus_rajoitetaan(self):
        varasto = Varasto(10, 20)
        self.assertAlmostEqual(varasto.saldo, 10)

    def test_negatiivinen_lisays_ei_muuta_saldoa(self):
        self.varasto.lisaa_varastoon(-1)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_lisays_ylittaa_tilavuuden(self):
        self.varasto.lisaa_varastoon(20)
        self.assertAlmostEqual(self.varasto.saldo, 10)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 0)

    def test_negatiivinen_ottaminen_palauttaa_nollan(self):
        self.varasto.lisaa_varastoon(5)
        self.assertAlmostEqual(self.varasto.ota_varastosta(-1), 0)
        self.assertAlmostEqual(self.varasto.saldo, 5)

    def test_ottaminen_yli_saldon_palauttaa_koko_saldon(self):
        self.varasto.lisaa_varastoon(5)
        self.assertAlmostEqual(self.varasto.ota_varastosta(10), 5)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_str(self):
        self.assertEqual(str(self.varasto), "saldo = 0, vielä tilaa 10")
