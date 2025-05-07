from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

class TableWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(TableWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("Таблица Менделеева")
        self.setWindowIcon(QIcon(dir_path + r"\res\ico\table.ico"))

        self.nonmetalls_btn = QPushButton(self)
        self.nonmetalls_btn.setFixedSize(QSize(60, 20))
        self.nonmetalls_btn.setStyleSheet("background-color: #7CFC00")
        self.nonmetalls_btn.move(QPoint(1180, 60))
        self.nonmetalls_label = QLabel("- неметаллы", self)
        self.nonmetalls_label.move(QPoint(1250, 55))

        self.inert_gas_btn = QPushButton(self)
        self.inert_gas_btn.setFixedSize(QSize(60, 20))
        self.inert_gas_btn.setStyleSheet("background-color: #9370DB")
        self.inert_gas_btn.move(QPoint(1180, 90))
        self.inert_gas_label = QLabel("- инертные газы", self)
        self.inert_gas_label.move(QPoint(1250, 85))

        self.halogen_btn = QPushButton(self)
        self.halogen_btn.setFixedSize(QSize(60, 20))
        self.halogen_btn.setStyleSheet("background-color: #FF6347")
        self.halogen_btn.move(QPoint(1180, 120))
        self.halogen_label = QLabel("- галогены", self)
        self.halogen_label.setFixedWidth(100)
        self.halogen_label.move(QPoint(1250, 115))

        self.metalls_btn = QPushButton(self)
        self.metalls_btn.setFixedSize(QSize(60, 20))
        self.metalls_btn.setStyleSheet("background-color: #4682B4")
        self.metalls_btn.move(QPoint(1360, 60))
        self.metalls_label = QLabel("- металлы", self)
        self.metalls_label.setFixedWidth(100)
        self.metalls_label.move(QPoint(1430, 55))

        self.alkali_btn = QPushButton(self)
        self.alkali_btn.setFixedSize(QSize(60, 20))
        self.alkali_btn.setStyleSheet("background-color: #4169E1")
        self.alkali_btn.move(QPoint(1360, 90))
        self.alkali_label = QLabel("- щелочные металлы", self)
        self.alkali_label.setFixedWidth(300)
        self.alkali_label.move(QPoint(1430, 85))

        self.alkali_earth_btn = QPushButton(self)
        self.alkali_earth_btn.setFixedSize(QSize(60, 20))
        self.alkali_earth_btn.setStyleSheet("background-color: #20B2AA")
        self.alkali_earth_btn.move(QPoint(1360, 120))
        self.alkali_earth_label = QLabel("- щелочноземельные металлы", self)
        self.alkali_earth_label.setFixedWidth(300)
        self.alkali_earth_label.move(QPoint(1430, 115))

        self.lantanoid_btn = QPushButton(self)
        self.lantanoid_btn.setFixedSize(QSize(60, 20))
        self.lantanoid_btn.setStyleSheet("background-color: #3CB371")
        self.lantanoid_btn.move(QPoint(1360, 150))
        self.lantanoid_label = QLabel("- лантаноиды", self)
        self.lantanoid_label.setFixedWidth(200)
        self.lantanoid_label.move(QPoint(1430, 145))

        self.aktinoid_btn = QPushButton(self)
        self.aktinoid_btn.setFixedSize(QSize(60, 20))
        self.aktinoid_btn.setStyleSheet("background-color: #228B22")
        self.aktinoid_btn.move(QPoint(1360, 180))
        self.aktinoid_label = QLabel("- актиноиды", self)
        self.aktinoid_label.setFixedWidth(100)
        self.aktinoid_label.move(QPoint(1430, 175))

        self.unknown_btn = QPushButton(self)
        self.unknown_btn.setFixedSize(QSize(60, 20))
        self.unknown_btn.setStyleSheet("background-color: #696969")
        self.unknown_btn.move(QPoint(1550, 60))
        self.unknown_label = QLabel("- элементы с неизвестными химическими\n свойствами", self)
        self.unknown_label.setFixedWidth(300)
        self.unknown_label.move(QPoint(1620, 55))

        self.period = QLabel("ПЕРИОД", self)
        self.period.move(QPoint(10, 30))

        self.period_1 = QLabel("1 период", self)
        self.period_1.move(QPoint(10, 80))

        self.period_2 = QLabel("2 период", self)
        self.period_2.move(QPoint(10, 140))

        self.period_3 = QLabel("3 период", self)
        self.period_3.move(QPoint(10, 220))

        self.period_4 = QLabel("4 период", self)
        self.period_4.move(QPoint(10, 320))

        self.period_5 = QLabel("5 период", self)
        self.period_5.move(QPoint(10, 470))

        self.period_6 = QLabel("6 период", self)
        self.period_6.move(QPoint(10, 600))

        self.period_7 = QLabel("7 период", self)
        self.period_7.move(QPoint(10, 750))

        self.group = QLabel("ГРУППА", self)
        self.group.move(QPoint(10, 10))

        self.group_1 = QLabel("I группа", self)
        self.group_1.move(QPoint(120, 10))

        self.group_2 = QLabel("II группа", self)
        self.group_2.move(QPoint(200, 90))

        self.group_3 = QLabel("III группа", self)
        self.group_3.move(QPoint(300, 90))

        self.group_4 = QLabel("IV группа", self)
        self.group_4.move(QPoint(400, 90))

        self.group_5 = QLabel("V группа", self)
        self.group_5.move(QPoint(500, 90))

        self.group_6 = QLabel("VI группа", self)
        self.group_6.move(QPoint(600, 90))

        self.group_7 = QLabel("VII группа", self)
        self.group_7.move(QPoint(700, 90))

        self.group_8 = QLabel("VIII группа", self)
        self.group_8.move(QPoint(800, 10))

        self.hygrogen = QPushButton("H\nВодород\n1,0079", self)
        self.hygrogen.setStyleSheet("background-color: #7CFC00")
        self.hygrogen.setFixedSize(QSize(100, 70))
        self.hygrogen.move(QPoint(80, 60))

        self.helium = QPushButton("He\nГелий\n4,0026", self)
        self.helium.setStyleSheet("background-color: #9370DB")
        self.helium.setFixedSize(QSize(100, 70))
        self.helium.move(QPoint(780, 60))

        self.litium = QPushButton("Li\nЛитий\n6,941", self)
        self.litium.setStyleSheet("background-color: #4169E1")
        self.litium.setFixedSize(QSize(100, 70))
        self.litium.move(QPoint(80, 130))

        self.berillium = QPushButton("Be\nБериллий\n9,0121", self)
        self.berillium.setStyleSheet("background-color: #20B2AA")
        self.berillium.setFixedSize(QSize(100, 70))
        self.berillium.move(QPoint(180, 130))

        self.borum = QPushButton("B\nБор\n10,811", self)
        self.borum.setStyleSheet("background-color: #7CFC00")
        self.borum.setFixedSize(QSize(100, 70))
        self.borum.move(QPoint(280, 130))

        self.carbon = QPushButton("C\nУглерод\n12,011", self)
        self.carbon.setStyleSheet("background-color: #7CFC00")
        self.carbon.setFixedSize(QSize(100, 70))
        self.carbon.move(QPoint(380, 130))

        self.nitrogen = QPushButton("N\nАзот\n14,0067", self)
        self.nitrogen.setStyleSheet("background-color: #7CFC00")
        self.nitrogen.setFixedSize(QSize(100, 70))
        self.nitrogen.move(QPoint(480, 130))
        
        self.oxygen = QPushButton("O\nКислород\n15,9994", self)
        self.oxygen.setStyleSheet("background-color: #7CFC00")
        self.oxygen.setFixedSize(QSize(100, 70))
        self.oxygen.move(QPoint(580, 130))

        self.fluorum = QPushButton("F\nФтор\n18,9984", self)
        self.fluorum.setStyleSheet("background-color: #FF6347")
        self.fluorum.setFixedSize(QSize(100, 70))
        self.fluorum.move(QPoint(680, 130))
        
        self.neon = QPushButton("Ne\nНеон\n20,179", self)
        self.neon.setStyleSheet("background-color: #9370DB")
        self.neon.setFixedSize(QSize(100, 70))
        self.neon.move(QPoint(780, 130))

        self.natrium = QPushButton("Na\nНатрий\n22,9897", self)
        self.natrium.setStyleSheet("background-color: #4169E1")
        self.natrium.setFixedSize(QSize(100, 70))
        self.natrium.move(QPoint(80, 200))

        self.magnium = QPushButton("Mg\nМагний\n24,305", self)
        self.magnium.setStyleSheet("background-color: #20B2AA")
        self.magnium.setFixedSize(QSize(100, 70))
        self.magnium.move(QPoint(180, 200))

        self.aluminium = QPushButton("Al\nАлюминий\n26,9815", self)
        self.aluminium.setStyleSheet("background-color: #4682B4")
        self.aluminium.setFixedSize(QSize(100, 70))
        self.aluminium.move(QPoint(280, 200))

        self.silicium = QPushButton("Si\nКремний\n28,0855", self)
        self.silicium.setStyleSheet("background-color: #7CFC00")
        self.silicium.setFixedSize(QSize(100, 70))
        self.silicium.move(QPoint(380, 200))

        self.phosphorus = QPushButton("P\nФосфор\n30,9737", self)
        self.phosphorus.setStyleSheet("background-color: #7CFC00")
        self.phosphorus.setFixedSize(QSize(100, 70))
        self.phosphorus.move(QPoint(480, 200))

        self.sulfur = QPushButton("S\nСера\n32,066", self)
        self.sulfur.setStyleSheet("background-color: #7CFC00")
        self.sulfur.setFixedSize(QSize(100, 70))
        self.sulfur.move(QPoint(580, 200))

        self.chlorum = QPushButton("Cl\nХлор\n35,453", self)
        self.chlorum.setStyleSheet("background-color: #FF6347")
        self.chlorum.setFixedSize(QSize(100, 70))
        self.chlorum.move(QPoint(680, 200))

        self.argon = QPushButton("Ar\nАргон\n39,948", self)
        self.argon.setStyleSheet("background-color: #9370DB")
        self.argon.setFixedSize(QSize(100, 70))
        self.argon.move(QPoint(780, 200))

        self.kalium = QPushButton("K\nКалий\n39,0983", self)
        self.kalium.setStyleSheet("background-color: #4169E1")
        self.kalium.setFixedSize(QSize(100, 70))
        self.kalium.move(QPoint(80, 270))

        self.calcium = QPushButton("Ca\nКальций\n40,078", self)
        self.calcium.setStyleSheet("background-color: #20B2AA")
        self.calcium.setFixedSize(QSize(100, 70))
        self.calcium.move(QPoint(180, 270))

        self.scandium = QPushButton("Sc\nСкандий\n44,9559", self)
        self.scandium.setStyleSheet("background-color: #4682B4")
        self.scandium.setFixedSize(QSize(100, 70))
        self.scandium.move(QPoint(280, 270))

        self.titanium = QPushButton("Ti\nТитан\n47,88", self)
        self.titanium.setStyleSheet("background-color: #4682B4")
        self.titanium.setFixedSize(QSize(100, 70))
        self.titanium.move(QPoint(380, 270))

        self.vanadium = QPushButton("V\nВанадий\n50,9415", self)
        self.vanadium.setStyleSheet("background-color: #4682B4")
        self.vanadium.setFixedSize(QSize(100, 70))
        self.vanadium.move(QPoint(480, 270))

        self.chromium = QPushButton("Cr\nХром\n51,9961", self)
        self.chromium.setStyleSheet("background-color: #4682B4")
        self.chromium.setFixedSize(QSize(100, 70))
        self.chromium.move(QPoint(580, 270))

        self.manganum = QPushButton("Mn\nМарганец\n64,9370", self)
        self.manganum.setStyleSheet("background-color: #4682B4")
        self.manganum.setFixedSize(QSize(100, 70))
        self.manganum.move(QPoint(680, 270))
        
        self.ferrum = QPushButton("Fe\nЖелезо\n55,847", self)
        self.ferrum.setStyleSheet("background-color: #4682B4")
        self.ferrum.setFixedSize(QSize(100, 70))
        self.ferrum.move(QPoint(780, 270))

        self.cobaltum = QPushButton("Co\nКобальт\n58,9332", self)
        self.cobaltum.setStyleSheet("background-color: #4682B4")
        self.cobaltum.setFixedSize(QSize(100, 70))
        self.cobaltum.move(QPoint(880, 270))

        self.niccolum = QPushButton("Ni\nНикель\n58,69", self)
        self.niccolum.setStyleSheet("background-color: #4682B4")
        self.niccolum.setFixedSize(QSize(100, 70))
        self.niccolum.move(QPoint(980, 270))

        self.cuprum = QPushButton("Cu\nМедь\n63,546", self)
        self.cuprum.setStyleSheet("background-color: #4682B4")
        self.cuprum.setFixedSize(QSize(100, 70))
        self.cuprum.move(QPoint(80, 340))

        self.zincum = QPushButton("Zn\nЦинк\n65,39", self)
        self.zincum.setStyleSheet("background-color: #4682B4")
        self.zincum.setFixedSize(QSize(100, 70))
        self.zincum.move(QPoint(180, 340))

        self.gallium = QPushButton("Ga\nГаллий\n69,723", self)
        self.gallium.setStyleSheet("background-color: #4682B4")
        self.gallium.setFixedSize(QSize(100, 70))
        self.gallium.move(QPoint(280, 340))

        self.germanium = QPushButton("Ge\nГерманий\n72,59", self)
        self.germanium.setStyleSheet("background-color: #4682B4")
        self.germanium.setFixedSize(QSize(100, 70))
        self.germanium.move(QPoint(380, 340))

        self.arsenicum = QPushButton("As\nМышьяк\n74,9216", self)
        self.arsenicum.setStyleSheet("background-color: #7CFC00")
        self.arsenicum.setFixedSize(QSize(100, 70))
        self.arsenicum.move(QPoint(480, 340))

        self.selenium = QPushButton("Se\nСелен\n78,96", self)
        self.selenium.setStyleSheet("background-color: #7CFC00")
        self.selenium.setFixedSize(QSize(100, 70))
        self.selenium.move(QPoint(580, 340))

        self.bromum = QPushButton("Br\nБром\n79,904", self)
        self.bromum.setStyleSheet("background-color: #FF6347")
        self.bromum.setFixedSize(QSize(100, 70))
        self.bromum.move(QPoint(680, 340))
        
        self.kripton = QPushButton("Kr\nКриптон\n83,70", self)
        self.kripton.setStyleSheet("background-color: #9370DB")
        self.kripton.setFixedSize(QSize(100, 70))
        self.kripton.move(QPoint(780, 340))

        self.rubidium = QPushButton("Rb\nРубидий\n85,4678", self)
        self.rubidium.setStyleSheet("background-color: #4169E1")
        self.rubidium.setFixedSize(QSize(100, 70))
        self.rubidium.move(QPoint(80, 410))

        self.stroncium = QPushButton("Sr\nСтронций\n87,62", self)
        self.stroncium.setStyleSheet("background-color: #20B2AA")
        self.stroncium.setFixedSize(QSize(100, 70))
        self.stroncium.move(QPoint(180, 410))

        self.yttrium = QPushButton("Y\nИттрий\n88,9059", self)
        self.yttrium.setStyleSheet("background-color: #4682B4")
        self.yttrium.setFixedSize(QSize(100, 70))
        self.yttrium.move(QPoint(280, 410))

        self.zirkonium = QPushButton("Zr\nЦирконий\n91,22", self)
        self.zirkonium.setStyleSheet("background-color: #4682B4")
        self.zirkonium.setFixedSize(QSize(100, 70))
        self.zirkonium.move(QPoint(380, 410))

        self.niobium = QPushButton("Nb\nНиобий\n92,9064", self)
        self.niobium.setStyleSheet("background-color: #4682B4")
        self.niobium.setFixedSize(QSize(100, 70))
        self.niobium.move(QPoint(480, 410))

        self.molybdaenum = QPushButton("Mo\nМолибден\n95,94", self)
        self.molybdaenum.setStyleSheet("background-color: #4682B4")
        self.molybdaenum.setFixedSize(QSize(100, 70))
        self.molybdaenum.move(QPoint(580, 410))

        self.tecnecium = QPushButton("Tc\nТехнеций\n(98)", self)
        self.tecnecium.setStyleSheet("background-color: #4682B4")
        self.tecnecium.setFixedSize(QSize(100, 70))
        self.tecnecium.move(QPoint(680, 410))

        self.rutenium = QPushButton("Ru\nРутений\n101,07", self)
        self.rutenium.setStyleSheet("background-color: #4682B4")
        self.rutenium.setFixedSize(QSize(100, 70))
        self.rutenium.move(QPoint(780, 410))
        
        self.rhodium = QPushButton("Rh\nРодий\n102,9055", self)
        self.rhodium.setStyleSheet("background-color: #4682B4")
        self.rhodium.setFixedSize(QSize(100, 70))
        self.rhodium.move(QPoint(880, 410))

        self.palladium = QPushButton("Pd\nПалладий\n106,42", self)
        self.palladium.setStyleSheet("background-color: #4682B4")
        self.palladium.setFixedSize(QSize(100, 70))
        self.palladium.move(QPoint(980, 410))

        self.argentum = QPushButton("Ag\nСеребро\n107,8682", self)
        self.argentum.setStyleSheet("background-color: #4682B4")
        self.argentum.setFixedSize(QSize(100, 70))
        self.argentum.move(QPoint(80, 480))

        self.cadmium = QPushButton("Cd\nКадмий\n112,41", self)
        self.cadmium.setStyleSheet("background-color: #4682B4")
        self.cadmium.setFixedSize(QSize(100, 70))
        self.cadmium.move(QPoint(180, 480))

        self.indium = QPushButton("In\nИндий\n114,82", self)
        self.indium.setStyleSheet("background-color: #4682B4")
        self.indium.setFixedSize(QSize(100, 70))
        self.indium.move(QPoint(280, 480))

        self.stannum = QPushButton("Sn\nОлово\n118,710", self)
        self.stannum.setStyleSheet("background-color: #4682B4")
        self.stannum.setFixedSize(QSize(100, 70))
        self.stannum.move(QPoint(380, 480))

        self.stibium = QPushButton("Sb\nСурьма\n121,75", self)
        self.stibium.setStyleSheet("background-color: #4682B4")
        self.stibium.setFixedSize(QSize(100, 70))
        self.stibium.move(QPoint(480, 480))

        self.tellurium = QPushButton("Te\nТеллур\n127,60", self)
        self.tellurium.setStyleSheet("background-color: #7CFC00")
        self.tellurium.setFixedSize(QSize(100, 70))
        self.tellurium.move(QPoint(580, 480))

        self.iodum = QPushButton("I\nИод\n126,9045", self)
        self.iodum.setStyleSheet("background-color: #FF6347")
        self.iodum.setFixedSize(QSize(100, 70))
        self.iodum.move(QPoint(680, 480))

        self.xenon = QPushButton("Xe\nКсенон\n131,29", self)
        self.xenon.setStyleSheet("background-color: #9370DB")
        self.xenon.setFixedSize(QSize(100, 70))
        self.xenon.move(QPoint(780, 480))

        self.cesium = QPushButton("Cs\nЦезий\n132,9054", self)
        self.cesium.setStyleSheet("background-color: #4169E1")
        self.cesium.setFixedSize(QSize(100, 70))
        self.cesium.move(QPoint(80, 550))

        self.barium = QPushButton("Ba\nБарий\n137,33", self)
        self.barium.setStyleSheet("background-color: #20B2AA")
        self.barium.setFixedSize(QSize(100, 70))
        self.barium.move(QPoint(180, 550))

        self.la_lu = QPushButton("La-Lu\nЛантаноиды", self)
        self.la_lu.setStyleSheet("background-color: #3CB371")
        self.la_lu.setFixedSize(QSize(100, 70))
        self.la_lu.move(QPoint(280, 550))

        self.lantan = QPushButton("La\nЛантан\n138,81", self)
        self.lantan.setStyleSheet("background-color: #3CB371")
        self.lantan.setFixedSize(QSize(90, 70))
        self.lantan.move(QPoint(80, 850))

        self.cerium = QPushButton("Ce\nЦерий\n140,9077", self)
        self.cerium.setStyleSheet("background-color: #3CB371")
        self.cerium.setFixedSize(QSize(90, 70))
        self.cerium.move(QPoint(170, 850))

        self.praseodim = QPushButton("Pr\nПразеодим\n140,9077", self)
        self.praseodim.setStyleSheet("background-color: #3CB371")
        self.praseodim.setFixedSize(QSize(90, 70))
        self.praseodim.move(QPoint(260, 850))
        
        self.neodim = QPushButton("Nd\nНеодим\n144,24", self)
        self.neodim.setStyleSheet("background-color: #3CB371")
        self.neodim.setFixedSize(QSize(90, 70))
        self.neodim.move(QPoint(350, 850))

        self.prometium = QPushButton("Pm\nПрометий\n(145)", self)
        self.prometium.setStyleSheet("background-color: #3CB371")
        self.prometium.setFixedSize(QSize(90, 70))
        self.prometium.move(QPoint(440, 850))

        self.samarium = QPushButton("Sm\nСамарий\n150,35", self)
        self.samarium.setStyleSheet("background-color: #3CB371")
        self.samarium.setFixedSize(QSize(90, 70))
        self.samarium.move(QPoint(530, 850))

        self.europium = QPushButton("Eu\nЕвропий\n151,96", self)
        self.europium.setStyleSheet("background-color: #3CB371")
        self.europium.setFixedSize(QSize(90, 70))
        self.europium.move(QPoint(620, 850))

        self.gadolinium = QPushButton("Gd\nГадолиний\n157,25", self)
        self.gadolinium.setStyleSheet("background-color: #3CB371")
        self.gadolinium.setFixedSize(QSize(90, 70))
        self.gadolinium.move(QPoint(710, 850))

        self.terbium = QPushButton("Tb\nТербий\n158,9254", self)
        self.terbium.setStyleSheet("background-color: #3CB371")
        self.terbium.setFixedSize(QSize(90, 70))
        self.terbium.move(QPoint(800, 850))

        self.dysprozium = QPushButton("Dy\nДиспрозий\n162,50", self)
        self.dysprozium.setStyleSheet("background-color: #3CB371")
        self.dysprozium.setFixedSize(QSize(90, 70))
        self.dysprozium.move(QPoint(890, 850))

        self.holmium = QPushButton("Ho\nГольмий\n164,9304", self)
        self.holmium.setStyleSheet("background-color: #3CB371")
        self.holmium.setFixedSize(QSize(90, 70))
        self.holmium.move(QPoint(980, 850))

        self.erbium = QPushButton("Er\nЭрбий\n167,26", self)
        self.erbium.setStyleSheet("background-color: #3CB371")
        self.erbium.setFixedSize(QSize(90, 70))
        self.erbium.move(QPoint(1070, 850))

        self.tulium = QPushButton("Tm\nТулий\n168,9342", self)
        self.tulium.setStyleSheet("background-color: #3CB371")
        self.tulium.setFixedSize(QSize(90, 70))
        self.tulium.move(QPoint(1160, 850))

        self.ytterbium = QPushButton("Yb\nИттербий\n173,04", self)
        self.ytterbium.setStyleSheet("background-color: #3CB371")
        self.ytterbium.setFixedSize(QSize(90, 70))
        self.ytterbium.move(QPoint(1250, 850))

        self.lutecium = QPushButton("Lu\nЛютеций\n174,967", self)
        self.lutecium.setStyleSheet("background-color: #3CB371")
        self.lutecium.setFixedSize(QSize(90, 70))
        self.lutecium.move(QPoint(1340, 850))

        self.hafnium = QPushButton("Hf\nГафний\n178,49", self)
        self.hafnium.setStyleSheet("background-color: #4682B4")
        self.hafnium.setFixedSize(QSize(100, 70))
        self.hafnium.move(QPoint(380, 550))

        self.tantal = QPushButton("Ta\nТантал\n170,9479", self)
        self.tantal.setStyleSheet("background-color: #4682B4")
        self.tantal.setFixedSize(QSize(100, 70))
        self.tantal.move(QPoint(480, 550))

        self.wolfram = QPushButton("W\nВольфрам\n183,85", self)
        self.wolfram.setStyleSheet("background-color: #4682B4")
        self.wolfram.setFixedSize(QSize(100, 70))
        self.wolfram.move(QPoint(580, 550))

        self.renium = QPushButton("Re\nРений\n186,207", self)
        self.renium.setStyleSheet("background-color: #4682B4")
        self.renium.setFixedSize(QSize(100, 70))
        self.renium.move(QPoint(680, 550))

        self.osmium = QPushButton("Os\nОсмий\n190,23", self)
        self.osmium.setStyleSheet("background-color: #4682B4")
        self.osmium.setFixedSize(QSize(100, 70))
        self.osmium.move(QPoint(780, 550))

        self.irridium = QPushButton("Ir\nИрридий\n192,22", self)
        self.irridium.setStyleSheet("background-color: #4682B4")
        self.irridium.setFixedSize(QSize(100, 70))
        self.irridium.move(QPoint(880, 550))

        self.platinum = QPushButton("Pt\nПлатина\n195,08", self)
        self.platinum.setStyleSheet("background-color: #4682B4")
        self.platinum.setFixedSize(QSize(100, 70))
        self.platinum.move(QPoint(980, 550))

        self.aurum = QPushButton("Au\nЗолото\n196,9665", self)
        self.aurum.setStyleSheet("background-color: #4682B4")
        self.aurum.setFixedSize(QSize(100, 70))
        self.aurum.move(QPoint(80, 620))

        self.hydrargyrum = QPushButton("Hg\nРтуть\n200,59", self)
        self.hydrargyrum.setStyleSheet("background-color: #4682B4")
        self.hydrargyrum.setFixedSize(QSize(100, 70))
        self.hydrargyrum.move(QPoint(180, 620))

        self.tallium = QPushButton("Tl\nТаллий\n204,383", self)
        self.tallium.setStyleSheet("background-color: #4682B4")
        self.tallium.setFixedSize(QSize(100, 70))
        self.tallium.move(QPoint(280, 620))

        self.plumbum = QPushButton("Pb\nСвинец\n207,2", self)
        self.plumbum.setStyleSheet("background-color: #4682B4")
        self.plumbum.setFixedSize(QSize(100, 70))
        self.plumbum.move(QPoint(380, 620))

        self.bismuthum = QPushButton("Bi\nВисмут\n208,98", self)
        self.bismuthum.setStyleSheet("background-color: #4682B4")
        self.bismuthum.setFixedSize(QSize(100, 70))
        self.bismuthum.move(QPoint(480, 620))

        self.polonium = QPushButton("Po\nПолоний\n(209)", self)
        self.polonium.setStyleSheet("background-color: #4682B4")
        self.polonium.setFixedSize(QSize(100, 70))
        self.polonium.move(QPoint(580, 620))

        self.astatium = QPushButton("At\nАстат\n(210)", self)
        self.astatium.setStyleSheet("background-color: #FF6347")
        self.astatium.setFixedSize(QSize(100, 70))
        self.astatium.move(QPoint(680, 620))

        self.radon = QPushButton("Rn\nРадон\n (222)", self)
        self.radon.setStyleSheet("background-color: #9370DB")
        self.radon.setFixedSize(QSize(100, 70))
        self.radon.move(QPoint(780, 620))

        self.francium = QPushButton("Fr\nФранций\n(223)", self)
        self.francium.setStyleSheet("background-color: #4169E1")
        self.francium.setFixedSize(QSize(100, 70))
        self.francium.move(QPoint(80, 690))

        self.radium = QPushButton("Ra\nРадий\n(226)", self)
        self.radium.setStyleSheet("background-color: #20B2AA")
        self.radium.setFixedSize(QSize(100, 70))
        self.radium.move(QPoint(180, 690))

        self.ac_lr = QPushButton("Ac-Lr\nАктиноиды", self)
        self.ac_lr.setStyleSheet("background-color: #228B22")
        self.ac_lr.setFixedSize(QSize(100, 70))
        self.ac_lr.move(QPoint(280, 690))

        self.actinium = QPushButton("Ac\nАктиний\n(227)", self)
        self.actinium.setStyleSheet("background-color: #228B22")
        self.actinium.setFixedSize(QSize(90, 70))
        self.actinium.move(QPoint(80, 920))

        self.thorium = QPushButton("Th\nТорий\n232,0381", self)
        self.thorium.setStyleSheet("background-color: #228B22")
        self.thorium.setFixedSize(QSize(90, 70))
        self.thorium.move(QPoint(170, 920))

        self.proaktinium = QPushButton("Pa\nПроактиний\n231,04", self)
        self.proaktinium.setStyleSheet("background-color: #228B22")
        self.proaktinium.setFixedSize(QSize(90, 70))
        self.proaktinium.move(QPoint(260, 920))

        self.uranium = QPushButton("U\nУран\n238,0289", self)
        self.uranium.setStyleSheet("background-color: #228B22")
        self.uranium.setFixedSize(QSize(90, 70))
        self.uranium.move(QPoint(350, 920))

        self.neptunium = QPushButton("Np\nНептуний\n(237)", self)
        self.neptunium.setStyleSheet("background-color: #228B22")
        self.neptunium.setFixedSize(QSize(90, 70))
        self.neptunium.move(QPoint(440, 920))

        self.plutonium = QPushButton("Pu\nПлутоний\n(244)", self)
        self.plutonium.setStyleSheet("background-color: #228B22")
        self.plutonium.setFixedSize(QSize(90, 70))
        self.plutonium.move(QPoint(530, 920))

        self.americium = QPushButton("Am\nАмериций\n(243)", self)
        self.americium.setStyleSheet("background-color: #228B22")
        self.americium.setFixedSize(QSize(90, 70))
        self.americium.move(QPoint(620, 920))

        self.curium = QPushButton("Cm\nКюрий\n(247)", self)
        self.curium.setStyleSheet("background-color: #228B22")
        self.curium.setFixedSize(QSize(90, 70))
        self.curium.move(QPoint(710, 920))

        self.berklium = QPushButton("Bk\nБерклий\n(247)", self)
        self.berklium.setStyleSheet("background-color: #228B22")
        self.berklium.setFixedSize(QSize(90, 70))
        self.berklium.move(QPoint(800, 920))

        self.californium = QPushButton("Cf\nКалифорний\n(251)", self)
        self.californium.setStyleSheet("background-color: #228B22")
        self.californium.setFixedSize(QSize(90, 70))
        self.californium.move(QPoint(890, 920))

        self.eynshteynium = QPushButton("Es\nЭйнштейний\n(252)", self)
        self.eynshteynium.setStyleSheet("background-color: #228B22")
        self.eynshteynium.setFixedSize(QSize(90, 70))
        self.eynshteynium.move(QPoint(980, 920))

        self.fermium = QPushButton("Fm\nФермий\n(257)", self)
        self.fermium.setStyleSheet("background-color: #228B22")
        self.fermium.setFixedSize(QSize(90, 70))
        self.fermium.move(QPoint(1070, 920))
        
        self.mendeleevium = QPushButton("Md\nМенделеевий\n(258)", self)
        self.mendeleevium.setStyleSheet("background-color: #228B22")
        self.mendeleevium.setFixedSize(QSize(90, 70))
        self.mendeleevium.move(QPoint(1160, 920))

        self.nobelium = QPushButton("No\nНобелий\n(259)", self)
        self.nobelium.setStyleSheet("background-color: #228B22")
        self.nobelium.setFixedSize(QSize(90, 70))
        self.nobelium.move(QPoint(1250, 920))

        self.lourencium = QPushButton("Lr\nЛоуренсий\n(260)", self)
        self.lourencium.setStyleSheet("background-color: #228B22")
        self.lourencium.setFixedSize(QSize(90, 70))
        self.lourencium.move(QPoint(1340, 920))

        self.reserfordium = QPushButton("Rf\nРезерфордий\n(261)", self)
        self.reserfordium.setStyleSheet("background-color: #4682B4")
        self.reserfordium.setFixedSize(QSize(100, 70))
        self.reserfordium.move(QPoint(380, 690))

        self.dubnium = QPushButton("Db\nДубний\n(262)", self)
        self.dubnium.setStyleSheet("background-color: #4682B4")
        self.dubnium.setFixedSize(QSize(100, 70))
        self.dubnium.move(QPoint(480, 690))

        self.siborgium = QPushButton("Sg\nСиборгий\n(266)", self)
        self.siborgium.setStyleSheet("background-color: #4682B4")
        self.siborgium.setFixedSize(QSize(100, 70))
        self.siborgium.move(QPoint(580, 690))

        self.bhorium = QPushButton("Bh\nБорий\n(267)", self)
        self.bhorium.setStyleSheet("background-color: #4682B4")
        self.bhorium.setFixedSize(QSize(100, 70))
        self.bhorium.move(QPoint(680, 690))

        self.hassium = QPushButton("Hs\nХассий\n(269)", self)
        self.hassium.setStyleSheet("background-color: #4682B4")
        self.hassium.setFixedSize(QSize(100, 70))
        self.hassium.move(QPoint(780, 690))

        self.meytnerium = QPushButton("Mt\nМейтнерий\n(268)", self)
        self.meytnerium.setStyleSheet("background-color: #696969")
        self.meytnerium.setFixedSize(QSize(100, 70))
        self.meytnerium.move(QPoint(880, 690))

        self.darmstadtium = QPushButton("Ds\nДармштадтий\n(271)", self)
        self.darmstadtium.setStyleSheet("background-color: #696969")
        self.darmstadtium.setFixedSize(QSize(100, 70))
        self.darmstadtium.move(QPoint(980, 690))

        self.rentgenium = QPushButton("Rg\nРентгений\n(282)", self)
        self.rentgenium.setStyleSheet("background-color: #696969")
        self.rentgenium.setFixedSize(QSize(100, 70))
        self.rentgenium.move(QPoint(80, 760))

        self.copernicium = QPushButton("Cn\nКоперниций\n(285)", self)
        self.copernicium.setStyleSheet("background-color: #4682B4")
        self.copernicium.setFixedSize(QSize(100, 70))
        self.copernicium.move(QPoint(180, 760))

        self.nihonium = QPushButton("Nh\nНихоний\n(286)", self)
        self.nihonium.setStyleSheet("background-color: #696969")
        self.nihonium.setFixedSize(QSize(100, 70))
        self.nihonium.move(QPoint(280, 760))

        self.flerovium = QPushButton("Fl\nФлеровий\n(289)", self)
        self.flerovium.setStyleSheet("background-color: #696969")
        self.flerovium.setFixedSize(QSize(100, 70))
        self.flerovium.move(QPoint(380, 760))

        self.moscovium = QPushButton("Mc\nМосковий\n(288)", self)
        self.moscovium.setStyleSheet("background-color: #696969")
        self.moscovium.setFixedSize(QSize(100, 70))
        self.moscovium.move(QPoint(480, 760))

        self.livermorium = QPushButton("Lv\nЛиверморий\n(293)", self)
        self.livermorium.setStyleSheet("background-color: #696969")
        self.livermorium.setFixedSize(QSize(100, 70))
        self.livermorium.move(QPoint(580, 760))

        self.tennesine = QPushButton("Ts\nТеннессин\n(294)", self)
        self.tennesine.setStyleSheet("background-color: #FF6347")
        self.tennesine.setFixedSize(QSize(100, 70))
        self.tennesine.move(QPoint(680, 760))

        self.oganeson = QPushButton("Og\nОганесон\n(294)", self)
        self.oganeson.setStyleSheet("background-color: #9370DB")
        self.oganeson.setFixedSize(QSize(100, 70))
        self.oganeson.move(QPoint(780, 760))




        





