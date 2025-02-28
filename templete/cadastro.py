from PySide6 import QtCore

qrc_data = b"""
<!DOCTYPE RCC><RCC version="1.0">
<qresource prefix="atualizar">
    <file>icons/browse.svg</file>
    <file>icons/delete.svg</file>
    <file>icons/document.svg</file>
    <file>icons/forward.svg</file>
    <file>icons/line.jpg</file>
    <file>icons/pen.svg</file>
    <file>icons/personal.svg</file>
    <file>icons/search.svg</file>
</qresource>
</RCC>
"""

qrc_buffer = QtCore.QBuffer()
qrc_buffer.open(QtCore.QIODevice.WriteOnly)
qrc_buffer.write(qrc_data)
qrc_buffer.close()

QtCore.qRegisterResourceData(0, qrc_buffer.data(), None, None)