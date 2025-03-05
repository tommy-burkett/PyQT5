from PyQt5 import QtWidgets as qtw
import sys

from src.analysis import RandomDataAnalysis
from src.plots import SimpleScatter
from src.qtcomponents import WindowWithFigureAbove, ButtonBox, configure_button

class DataDashboard(qtw.QApplication):
    def __init__(self):
        super().__init__([])

        self.engine = RandomDataAnalysis()
        self.display = SimpleScatter()

        self.configure_main_window()

        self.main_window.show()
        