# This Python file uses the following encoding: utf-8
import sys
import sys , os
import json
import urllib
import urllib.request
import PySide2
from PySide2.QtWidgets import QApplication
import PySide2.QtQml
from PySide2.QtQuick import QQuickView
from PySide2.QtCore import QStringListModel, Qt, QUrl
from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtCore import QObject, Slot

from os.path import abspath, dirname, join
#from WeatherForcast import Time

if __name__ == "__main__":
    #app = QApplication([])
    data_list = "Test"

    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    # Instance of the Python object

    # Expose the Python object to QML
    context = engine.rootContext()
    context.setContextProperty("con", data_list)
    #context.setContextProperty("tim", time)

    # Get the path of the current directory, and then add the name
    # of the QML file, to load it.
    qmlFile = join(dirname(__file__), 'main.qml')
    engine.load(abspath(qmlFile))

    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec_())
    sys.exit(app.exec_())
