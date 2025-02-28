from PySide6 import QtCore, QtGui, QtWidgets

# Dados do recurso no formato binário
qrc_data = b"""
<!DOCTYPE RCC><RCC version="1.0">
<qresource prefix="iconprincipal">
    <file>icons/browse.svg</file>
    <file>icons/delete.svg</file>
    <file>icons/document.svg</file>
    <file>icons/forward.svg</file>
    <file>icons/pen.svg</file>
    <file>icons/personal.svg</file>
    <file>icons/search.svg</file>
</qresource>
</RCC>
"""

# Criar o buffer e registrar os recursos
qrc_buffer = QtCore.QBuffer()
qrc_buffer.open(QtCore.QIODevice.WriteOnly)
qrc_buffer.write(qrc_data)
qrc_buffer.close()

QtCore.qRegisterResourceData(0, qrc_buffer.data(), None, None)

# Iniciar o aplicativo
app = QtWidgets.QApplication([])

# Carregar um ícone do recurso
pixmap = QtGui.QPixmap(":/iconprincipal/icons/search.svg")

# Exibir o ícone em um QLabel
label = QtWidgets.QLabel()
label.setPixmap(pixmap)
label.show()

# Iniciar o loop de evento
app.exec()
