# ##################################################################################################
#   MIT License                                                                                    #
#                                                                                                  #
#   Copyright (c) 2023 Jon Duea                                                                    #
#                                                                                                  #
#   Permission is hereby granted, free of charge, to any person obtaining a copy                   #
#   of this software and associated documentation files (the "Software"), to deal                  #
#   in the Software without restriction, including without limitation the rights                   #
#   to use, copy, modify, merge, publish, distribute, sublicense, and/or sell                      #
#   copies of the Software, and to permit persons to whom the Software is                          #
#   furnished to do so, subject to the following conditions:                                       #
#                                                                                                  #
#   The above copyright notice and this permission notice shall be included in all                 #
#   copies or substantial portions of the Software.                                                #
#                                                                                                  #
#   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR                     #
#   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,                       #
#   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE                    #
#   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER                         #
#   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,                  #
#   OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE                  #
#   SOFTWARE.                                                                                      #
# ##################################################################################################
from asyncio import Lock
from collections import namedtuple

from nuitka.utils import Utils
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Property, QLocale, QModelIndex, QObject, QPoint, QRect, QSize, Qt, Signal
from PySide6.QtGui import (QColor, QFont, QFontMetrics, QIcon, QPainter, QPalette, QPen, QStandardItem,
                           QStandardItemModel, QTextDocument)
from PySide6.QtWidgets import (QAbstractItemView, QFrame, QHeaderView, QScrollBar, QStyle, QStyledItemDelegate,
                               QStyleOptionViewItem, QVBoxLayout, QWidget)


class TableViewCorner(QWidget):
    def __init__(self, table_view, parent=None):
        super().__init__(parent)
        self._table_view = table_view

    def paintEvent(self, event):
        super().paintEvent(event)

        if self._table_view.verticalHeader() and self._table_view.verticalHeader().isVisible():
            painter = QPainter(self)

            painter.setBrush(self.palette().brush(QPalette.Button))
            painter.fillRect(self.rect().adjusted(1, 1, 0, 0), self.palette().brush(QPalette.Button))

            painter.setPen(Utils.pen(self.palette().color(QPalette.Mid)))
            painter.drawLine(self.rect().right(), self.rect().top(), self.rect().right(), self.rect().bottom())
            painter.drawLine(self.rect().left(), self.rect().bottom(), self.rect().right(), self.rect().bottom())


class FrozenTableView(TableViewBase):
    sg_checkedCellChanged = Signal(QModelIndex, bool)

    def __init__(self, base, parent=None):
        super().__init__(parent)
        self._base = base
        self._request_resize = False
        self.init()

    def init(self):
        assert self._base is not None
        self.setFrameShape(QFrame.NoFrame)

        self.setItemDelegate(ItemDelegate(self, self._base, self._base, self))
        self._base.sg_checkedCellChanged.connect(self.sg_checkedCellChanged)

        self.verticalHeader().sectionResized.connect(self.requestResizeRowsToContents)
        self.requestResizeRowsToContents()

    def rootHeaderItem(self, orientation):
        return self._base.rootHeaderItem(orientation)

    def frozenGroupCount(self):
        return self._base.frozenGroupCount()

    def setFrozenGroupCount(self, count):
        self._base.setFrozenGroupCount(count)

    def sizeHintForRow(self, row):
        return self._base.sizeHintForRow(row)

    def isAutoShrink(self):
        return self._base.isAutoShrink()

    def shrinkMinimumRowCount(self):
        return self._base.shrinkMinimumRowCount()

    def shrinkMaximumRowCount(self):
        return self._base.shrinkMaximumRowCount()

    def isAutoResizeRowsHeight(self):
        return self._base.isAutoResizeRowsHeight()

    def cellCheckColumns(self, level=-1):
        return self._base.cellCheckColumns(level)

    def setCellCheckColumn(self, logical_index, visible, enabled, level=-1):
        self._base.setCellCheckColumn(logical_index, visible, enabled, level)

    def isCellChecked(self, index):
        return self._base.isCellChecked(index)

    def setCellChecked(self, index, checked):
        self._base.setCellChecked(index, checked)

    def checkedCells(self):
        return self._base.checkedCells()

    def clearCheckedCells(self):
        self._base.clearCheckedCells()

    def base(self):
        return self._base

    def horizontalHeaderHeight(self):
        return self._base.horizontalHeaderHeight()

    def onColumnResized(self, column, oldWidth, newWidth):
        if self._request_resize:
            return
        self._request_resize = True
        super().onColumnResized(column, oldWidth, newWidth)
        self._base.onColumnResized(column, oldWidth, newWidth)
        self._request_resize = False

    def onColumnsDragging(self, from_begin, from_end, to, to_hidden, left, allow):
        super().onColumnsDragging(from_begin, from_end, to, to_hidden, left, allow)

    def onColumnsDragFinished(self):
        super().onColumnsDragFinished()

    def paintEvent(self, event):
        super().paintEvent(event)


class TableViewScrollBar(QScrollBar):
    def __init__(self, orientation, parent=None):
        super().__init__(orientation, parent)

    def hack_sliderChange(self):
        pass

    def privatePtr(self):
        return None


class CheckBoxPanel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._view = parent
        self._ignore_group_check = False
        self._is_group_checked = False
        self.setMouseTracking(True)

    def paintEvent(self, e):
        super().paintEvent(e)

    def mouseMoveEvent(self, e):
        super().mouseMoveEvent(e)

    def mousePressEvent(self, e):
        super().mousePressEvent(e)

    def mouseReleaseEvent(self, e):
        super().mouseReleaseEvent(e)

    def wheelEvent(self, event):
        super().wheelEvent(event)


HtmlNode = namedtuple('HtmlNode', ['type', 'text'])


class HtmlNodes:
    def __init__(self):
        self._nodes = []
        self._isCorrect = True
        self._hasHtmlNodes = False

    def toPlain(self):
        pass
        # Implementation

    def nodes(self):
        return self._nodes

    def isCorrect(self):
        return self._isCorrect

    def isHasHtmlNodes(self):
        return self._hasHtmlNodes


class HtmlTools:
    _mutex = Lock()
    _parsedCorrect = None
    _parsedPlain = None
    _parsed = None
    _supportedHtmlTags = {"!doctype", "style", "ag", "a", "address", "b", "big", "blockquote", "body", "br", "center",
                          "cite", "code", "dd", "dfn", "div", "dl", "dt", "em", "font", "h1", "h2", "h3", "h4", "h5",
                          "h6", "head", "hr", "html", "i", "img", "kbd", "meta", "li", "nobr", "ol", "p", "pre", "qt",
                          "s", "samp", "small", "span", "strong", "sub", "sup", "table", "tbody", "td", "tfoot", "th",
                          "thead", "title", "tr", "tt", "u", "ul", "var"}
    _escapedTags = {"zuid"}
    Z_HTML_REPLACE_OPEN = "\""
    Z_HTML_REPLACE_CLOSE = "\""

    def __init__(self):
        pass

    @staticmethod
    def plain(s, keepNewLine=True):
        pass
        # Implementation

    @staticmethod
    def plainIfHtml(s, keepNewLine=True):
        pass
        # Implementation

    @staticmethod
    def isHtml(s):
        pass
        # Implementation

    @staticmethod
    def correct(s):
        pass
        # Implementation

    @staticmethod
    def correctIfHtml(s):
        pass
        # Implementation

    @staticmethod
    def correct():
        pass
        # Implementation

    @staticmethod
    def color(s, color):
        return f"<font color=\"{color.name()}\">{s}</font>"

    @staticmethod
    def bold(s):
        return f"<b>{s}</b>"

    @staticmethod
    def italic(s):
        return f"<i>{s}</i>"

    @staticmethod
    def font(s, size):
        return f"<span style=\" font-size:{size}pt;\">{s}</span>"

    @staticmethod
    def table(rows):
        pass
        # Implementation

    @staticmethod
    def parse(html):
        pass
        # Implementation

    @staticmethod
    def underline(s):
        return f"<span style=\" text-decoration: underline;\">{s}</span>"

    @staticmethod
    def align(s, align):
        pass
        # Implementation


class HeaderView(QtWidgets.QHeaderView):
    MimeType = 'application/x-ZFHeaderView'

    def __init__(self, orientation, parent=None):
        super().__init__(orientation, parent)
        self._reload_data_from_root_item_timer = QtCore.QTimer(self)
        self._reload_data_from_root_item_timer.setSingleShot(True)
        self._reload_data_from_root_item_timer.setInterval(0)
        self._reload_data_from_root_item_timer.timeout.connect(self.reloadDataFromRootItemHelper)

        if orientation == QtCore.Qt.Horizontal:
            self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
            self.setSectionsMovable(True)
            self.setDragEnabled(True)
            self.setAcceptDrops(True)
            self.setDropIndicatorShown(True)
            self.setDragDropMode(QtWidgets.QHeaderView.InternalMove)
            self.setMinimumSectionSize(max(22, QtGui.qApp.fontMetrics().averageCharWidth() * 2))
            self.setSortIndicatorShown(True)
            self.setSortIndicator(-1, QtCore.Qt.AscendingOrder)
        else:
            self.setVisible(False)
            doc = QtGui.QTextDocument()
            doc.setPlainText('X')
            default_row_height = max(int(doc.size().height()) + 1, QtGui.qApp.fontMetrics().xHeight() + 4)
            default_row_height = max(22, default_row_height)
            self.setMinimumSectionSize(default_row_height)
            self.setDefaultSectionSize(default_row_height)

        self.sectionResized.connect(self.sl_sectionResized)
        self.customContextMenuRequested.connect(
            lambda pos: self.sg_configMenuRequested(pos) if self._allow_config else None)
        self.setJoinedModel(ItemViewHeaderModel(orientation, self))

    def __del__(self):
        pass

    def setModel(self, m):
        self._block_change_header_items_counter += 1
        self._model.setSourceModel(m)
        self._block_change_header_items_counter -= 1
        super().setModel(m)

    def indexAt(self, pos):
        rows = self.orientation() == QtCore.Qt.Horizontal ? self.rootItem().levelSpan(): self.model().rowCount()
        cols = self.model().columnCount()
        logicalIdx = self.logicalIndexAt(pos)
        delta = 0

        if self.orientation() == QtCore.Qt.Horizontal:
            for row in range(rows):
                item = self.model().item(row, logicalIdx, True)
                if item is None:
                    return super().indexAt(pos)
                cellIndex = self.model().index(row, logicalIdx)
                if row == rows - 1:
                    return cellIndex
                delta += item.levelSize()
                if pos.y() <= delta:
                    return cellIndex
        else:
            for col in range(cols):
                item = self.model().item(logicalIdx, col, True)
                if item is None:
                    return super().indexAt(pos)
                cellIndex = self.model().index(logicalIdx, col)
                delta += item.levelSize()
                if pos.x() <= delta:
                    return cellIndex

        return QtCore.QModelIndex()

    def headerData(self, section, orientation, role):
        if not self.model():
            return None

        if orientation == self.orientation():
            if role == QtCore.Qt.DisplayRole:
                return self.rootItem().headerData(section)
            if role == QtCore.Qt.ToolTipRole:
                return self.rootItem().toolTip(section)
            if role == QtCore.Qt.StatusTipRole:
                return self.rootItem().statusTip(section)
            if role == QtCore.Qt.FontRole:
                return self.rootItem().font(section)
            if role == QtCore.Qt.TextAlignmentRole:
                return self.rootItem().textAlignment(section)
            if role == QtCore.Qt.BackgroundColorRole:
                return self.rootItem().backgroundColor(section)
            if role == QtCore.Qt.TextColorRole:
                return self.rootItem().textColor(section)
            if role == QtCore.Qt.CheckStateRole:
                return self.rootItem().checkState(section)

        return super().headerData(section, orientation, role)

    def setHeaderData(self, section, orientation, value, role):
        if not self.model():
            return False

        if orientation == self.orientation():
            if role == QtCore.Qt.DisplayRole:
                return self.rootItem().setHeaderData(section, value)
            if role == QtCore.Qt.ToolTipRole:
                return self.rootItem().setToolTip(section, value)
            if role == QtCore.Qt.StatusTipRole:
                return self.rootItem().setStatusTip(section, value)
            if role == QtCore.Qt.FontRole:
                return self.rootItem().setFont(section, value)
            if role == QtCore.Qt.TextAlignmentRole:
                return self.rootItem().setTextAlignment(section, value)
            if role == QtCore.Qt.BackgroundColorRole:
                return self.rootItem().setBackgroundColor(section, value)
            if role == QtCore.Qt.TextColorRole:
                return self.rootItem().setTextColor(section, value)
            if role == QtCore.Qt.CheckStateRole:
                return self.rootItem().setCheckState(section, value)

        return super().setHeaderData(section, orientation, value, role)

    def data(self, index, role):
        if not index.isValid():
            return None

        item = index.internalPointer()

        if role == QtCore.Qt.DisplayRole:
            return item.text(index.column())
        if role == QtCore.Qt.ToolTipRole:
            return item.toolTip(index.column())
        if role == QtCore.Qt.StatusTipRole:
            return item.statusTip(index.column())
        if role == QtCore.Qt.FontRole:
            return item.font(index.column())
        if role == QtCore.Qt.TextAlignmentRole:
            return item.textAlignment(index.column())
        if role == QtCore.Qt.BackgroundColorRole:
            return item.backgroundColor(index.column())
        if role == QtCore.Qt.TextColorRole:
            return item.textColor(index.column())
        if role == QtCore.Qt.CheckStateRole:
            return item.checkState(index.column())

        return None

    def setData(self, index, value, role):
        if not index.isValid():
            return False

        item = index.internalPointer()

        if role == QtCore.Qt.DisplayRole:
            return item.setText(index.column(), value)
        if role == QtCore.Qt.ToolTipRole:
            return item.setToolTip(index.column(), value)
        if role == QtCore.Qt.StatusTipRole:
            return item.setStatusTip(index.column(), value)
        if role == QtCore.Qt.FontRole:
            return item.setFont(index.column(), value)
        if role == QtCore.Qt.TextAlignmentRole:
            return item.setTextAlignment(index.column(), value)
        if role == QtCore.Qt.BackgroundColorRole:
            return item.setBackgroundColor(index.column(), value)
        if role == QtCore.Qt.TextColorRole:
            return item.setTextColor(index.column(), value)
        if role == QtCore.Qt.CheckStateRole:
            return item.setCheckState(index.column(), value)

        return False

    def rowCount(self, parent):
        parent_item = None
        if not parent.isValid():
            parent_item = self.rootItem()
        else:
            parent_item = parent.internalPointer()

        return parent_item.childCount()

    def columnCount(self, parent):
        return self.rootItem().columnCount()

    def index(self, row, column, parent):
        if not self.hasIndex(row, column, parent):
            return QtCore.QModelIndex()

        parent_item = None
        if not parent.isValid():
            parent_item = self.rootItem()
        else:
            parent_item = parent.internalPointer()

        child_item = parent_item.child(row)
        if child_item:
            return self.createIndex(row, column, child_item)

        return QtCore.QModelIndex()

    def parent(self, index):
        if not index.isValid():
            return QtCore.QModelIndex()

        child_item = index.internalPointer()
        parent_item = child_item.parentItem()

        if parent_item == self.rootItem():
            return QtCore.QModelIndex()

        return self.createIndex(parent_item.row(), 0, parent_item)


class CheckableHeaderView(QtWidgets.QHeaderView):
    def __init__(self, orientation, parent=None):
        super().__init__(orientation, parent)
        self._is_select_column = False
        self._is_press_shift_key = False
        self._is_press_ctrl_key = False
        self._is_resize_enabled = True
        self._selection = QtGui.QPainterPath()
        self._selection_bounding_rect = QtCore.QRect()
        self._selection_start_pos = QtCore.QPoint()
        self._selection_end_pos = QtCore.QPoint()
        self._selection_last_pos = QtCore.QPoint()
        self._selection_start_section = -1
        self._selection_end_section = -1
        self._selection_last_section = -1

        self.setSectionsMovable(True)
        self.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.setHighlightSections(True)
        self.setDefaultAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self._init_action()

    def _init_action(self):
        self._act_resize = QtWidgets.QAction(self)
        self._act_resize.setCheckable(True)
        self._act_resize.setChecked(True)
        self._act_resize.setText("Resize")
        self._act_resize.triggered.connect(self._on_act_resize)

        self._act_select_column = QtWidgets.QAction(self)
        self._act_select_column.setCheckable(True)
        self._act_select_column.setText("Select columns")
        self._act_select_column.triggered.connect(self._on_act_select_column)

    def _on_act_resize(self, checked):
        self._is_resize_enabled = checked

    def _on_act_select_column(self, checked):
        self._is_select_column = checked

    def paintEvent(self, e):
        super().paintEvent(e)
        painter = QtGui.QPainter(self.viewport())
        painter.setPen(QtGui.QPen(QtGui.QBrush(QtGui.QColor(128, 128, 255)), 2))
        painter.setBrush(QtGui.QBrush(QtGui.QColor(128, 128, 255, 128)))
        painter.drawPath(self._selection)

    def mousePressEvent(self, e):
        if e.buttons() == QtCore.Qt.LeftButton and self._is_select_column:
            self._selection_start_pos = e.pos()
            self._selection_start_section = self.logicalIndexAt(self._selection_start_pos)
            self._selection_last_pos = self._selection_start_pos
            self._selection_last_section = self._selection_start_section
            self._selection_end_pos = self._selection_start_pos
            self._selection_end_section = self._selection_start_section
            self._update_selection()
        else:
            super().mousePressEvent(e)

    def mouseMoveEvent(self, e):
        if self._is_select_column and not self._selection_start_pos.isNull():
            self._selection_end_pos = e.pos()
            self._selection_end_section = self.logicalIndexAt(self._selection_end_pos)
            self._update_selection()
        else:
            super().mouseMoveEvent(e)

    def mouseReleaseEvent(self, e):
        if self._is_select_column and not self._selection_start_pos.isNull():
            self._selection_start_pos = QtCore.QPoint()
            self._selection_last_pos = QtCore.QPoint()
            self._selection_end_pos = QtCore.QPoint()
            self._selection_start_section = -1
            self._selection_last_section = -1
            self._selection_end_section = -1
            self._selection = QtGui.QPainterPath()
            self._selection_bounding_rect = QtCore.QRect()
            self.viewport().update()
        else:
            super().mouseReleaseEvent(e)

    def _update_selection(self):
        self._selection = QtGui.QPainterPath()
        rect = QtCore.QRect(self._selection_start_pos, self._selection_end_pos).normalized()
        self._selection.addRect(rect)
        self._selection_bounding_rect = rect
        self.viewport().update(rect)

        if self._selection_last_section != self._selection_end_section:
            self._selection_last_section = self._selection_end_section
            self._select_columns()

    def _select_columns(self):
        model = self.model()
        if model is None:
            return

        selection_model = self.selectionModel()
        if selection_model is None:
            return

        start_section = min(self._selection_start_section, self._selection_end_section)
        end_section = max(self._selection_start_section, self._selection_end_section)
        selection = QtCore.QItemSelection()
        for section in range(start_section, end_section + 1):
            logical_index = self.logicalIndex(section)
            selection.append(QtCore.QItemSelectionRange(model.index(0, logical_index),
                                                        model.index(model.rowCount() - 1, logical_index)))

        selection_model.select(selection, QtCore.QItemSelectionModel.Columns |
                               QtCore.QItemSelectionModel.ClearAndSelect)


class SortFilterHeaderView(CheckableHeaderView):
    def __init__(self, orientation, parent=None):
        super().__init__(orientation, parent)
        self._filter_widget = None
        self._filter_widget_visible = False
        self._filter_widget_section = -1
        self._filter_widget_pos = QtCore.QPoint()

    def set_filter_widget(self, widget):
        self._filter_widget = widget

    def show_filter_widget(self, section):
        if self._filter_widget is None or section < 0 or section >= self.count():
            return

        self._filter_widget_section = section
        self._filter_widget_pos = self.sectionViewportPosition(section)
        rect = self._section_rect(section)
        self._filter_widget.setGeometry(rect)
        self._filter_widget.setVisible(True)
        self._filter_widget.setFocus()
        self._filter_widget_visible = True

    def hide_filter_widget(self):
        if self._filter_widget is not None and self._filter_widget_visible:
            self._filter_widget.setVisible(False)
            self._filter_widget_visible = False
            self._filter_widget_section = -1
            self._filter_widget_pos = QtCore.QPoint()

    def _section_rect(self, section):
        if section < 0 or section >= self.count():
            return QtCore.QRect()

        pos = self.sectionViewportPosition(section)
        size = self.sectionSize(section)
        return QtCore.QRect(pos, 0, size, self.height())

    def resizeEvent(self, e):
        super().resizeEvent(e)
        if self._filter_widget_visible:
            rect = self._section_rect(self._filter_widget_section)
            self._filter_widget.setGeometry(rect)

    def scrollContentsBy(self, dx, dy):
        super().scrollContentsBy(dx, dy)
        if self._filter_widget_visible and dx != 0:
            self._filter_widget.move(self._filter_widget.pos() + QtCore.QPoint(dx, 0))
            self._filter_widget_pos += QtCore.QPoint(dx, 0)


class StyledItemDelegateWithoutFocus(QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super().initStyleOption(option, index)
        option.state &= ~QtCore.Qt.ItemIsFocusable
        option.state &= ~QtCore.Qt.ItemIsFocused


class EditableHeaderView(CheckableHeaderView):
    def __init__(self, orientation, parent=None):
        super().__init__(orientation, parent)
        self._edit_widget = None
        self._edit_widget_visible = False
        self._edit_widget_section = -1
        self._edit_widget_pos = QtCore.QPoint()
        self._section_size_hint = None

    def set_edit_widget(self, widget):
        self._edit_widget = widget

    def show_edit_widget(self, section):
        if self._edit_widget is None or section < 0 or section >= self.count():
            return

        self._edit_widget_section = section
        self._edit_widget_pos = self.sectionViewportPosition(section)
        rect = self._section_rect(section)
        self._edit_widget.setGeometry(rect)
        self._edit_widget.setVisible(True)
        self._edit_widget.setFocus()
        self._edit_widget_visible = True

    def hide_edit_widget(self):
        if self._edit_widget is not None and self._edit_widget_visible:
            self._edit_widget.setVisible(False)
            self._edit_widget_visible = False
            self._edit_widget_section = -1
            self._edit_widget_pos = QtCore.QPoint()

    def _section_rect(self, section):
        if section < 0 or section >= self.count():
            return QtCore.QRect()

        pos = self.sectionViewportPosition(section)
        size = self.sectionSize(section)
        return QtCore.QRect(pos, 0, size, self.height())

    def resizeEvent(self, e):
        super().resizeEvent(e)
        if self._edit_widget_visible:
            rect = self._section_rect(self._edit_widget_section)
            self._edit_widget.setGeometry(rect)

    def scrollContentsBy(self, dx, dy):
        super().scrollContentsBy(dx, dy)
        if self._edit_widget_visible and dx != 0:
            self._edit_widget.move(self._edit_widget.pos() + QtCore.QPoint(dx, 0))
            self._edit_widget_pos += QtCore.QPoint(dx, 0)

    def sectionSizeHint(self, section):
        if self._section_size_hint is not None:
            return self._section_size_hint

        return super().sectionSizeHint(section)

    def set_section_size_hint(self, size_hint):
        self._section_size_hint = size_hint


class FilterHeaderView(EditableHeaderView):
    def __init__(self, orientation, parent=None):
        super().__init__(orientation, parent)
        self._filter_widget = None
        self._filter_widget_visible = False
        self._filter_widget_section = -1
        self._filter_widget_pos = QtCore.QPoint()
        self._section_size_hint = None

    def set_filter_widget(self, widget):
        self._filter_widget = widget

    def show_filter_widget(self, section):
        if self._filter_widget is None or section < 0 or section >= self.count():
            return

        self._filter_widget_section = section
        self._filter_widget_pos = self.sectionViewportPosition(section)
        rect = self._section_rect(section)
        self._filter_widget.setGeometry(rect)
        self._filter_widget.setVisible(True)
        self._filter_widget.setFocus()
        self._filter_widget_visible = True

    def hide_filter_widget(self):
        if self._filter_widget is not None and self._filter_widget_visible:
            self._filter_widget.setVisible(False)
            self._filter_widget_visible = False
            self._filter_widget_section = -1
            self._filter_widget_pos = QtCore.QPoint()

    def _section_rect(self, section):
        if section < 0 or section >= self.count():
            return QtCore.QRect()

        pos = self.sectionViewportPosition(section)
        size = self.sectionSize(section)
        return QtCore.QRect(pos, 0, size, self.height())

    def resizeEvent(self, e):
        super().resizeEvent(e)
        if self._filter_widget_visible:
            rect = self._section_rect(self._filter_widget_section)
            self._filter_widget.setGeometry(rect)

    def scrollContentsBy(self, dx, dy):
        super().scrollContentsBy(dx, dy)
        if self._filter_widget_visible and dx != 0:
            self._filter_widget.move(self._filter_widget.pos() + QtCore.QPoint(dx, 0))
            self._filter_widget_pos += QtCore.QPoint(dx, 0)

    def sectionSizeHint(self, section):
        if self._section_size_hint is not None:
            return self._section_size_hint

        return super().sectionSizeHint(section)

    def set_section_size_hint(self, size_hint):
        self._section_size_hint = size_hint


class SortType:
    NormalSort = 0
    DescSort = 1
    AscSort = 2


class ShowType:
    NormalShow = 0
    HideShow = 1


class OrderType:
    NormalOrder = 0
    DescOrder = 1
    AscOrder = 2


class ResizeType:
    FixedResize = 0
    ContentResize = 1
    FreeResize = 2


class ZFHeaderView(QHeaderView):
    sort_color_changed = Signal()
    is_sort_enabled_changed = Signal()
    is_menu_enabled_changed = Signal()

    def __init__(self, orientation: Qt.Orientation, parent=None):
        super().__init__(orientation, parent)


class ZFHeaderView(QHeaderView):
    # ... Existing code ...

    @Property(QColor, notify=sort_color_changed)
    def sort_color(self):
        # Implementation needed
        pass

    @sort_color.setter
    def sort_color(self, color: QColor):
        # Implementation needed
        pass

    @Property(bool, notify=is_sort_enabled_changed)
    def is_sort_enabled(self) -> bool:
        # Implementation needed
        return False

    @is_sort_enabled.setter
    def is_sort_enabled(self, is_enabled: bool):
        # Implementation needed
        pass

    @Property(bool, notify=is_menu_enabled_changed)
    def is_menu_enabled(self) -> bool:
        # Implementation needed
        return False

    @is_menu_enabled.setter
    def is_menu_enabled(self, is_enabled: bool):
        # Implementation needed
        pass

    # Additional methods
    # ...

    sorted = Signal(int, Qt.SortOrder)
    section_order_changed = Signal(int, int)
    section_resize_changed = Signal(int, ResizeType)
    section_show_changed = Signal(int, ShowType)
    section_sort_changed = Signal(int, SortType)


# Translating the initial part of the C++ code into Python
# Including necessary imports and class/enum definitions

from typing import List, Optional
from threading import RLock


class HtmlNode:
    class Type:
        Tag = 0  # Correct HTML tag
        BadTag = 1  # Incorrect HTML tag
        Escaped = 2  # Needs to be escaped when outputting to HTML
        Data = 3  # Regular data

    def __init__(self, type: Type, text: str):
        self.type = type
        self.text = text


class HtmlNodes:
    def __init__(self):
        self._nodes: List[HtmlNode] = []
        self._is_correct = True
        self._has_html_nodes = False

    def to_plain(self) -> str:
        # To be implemented
        pass

    @property
    def nodes(self) -> List[HtmlNode]:
        return self._nodes

    @property
    def is_correct(self) -> bool:
        return self._is_correct

    @property
    def has_html_nodes(self) -> bool:
        return self._has_html_nodes


class HtmlTools:
    _mutex = RLock()
    _parsed_correct: Optional[str] = None
    _parsed_plain: Optional[str] = None
    _parsed: Optional[HtmlNodes] = None

    def __init__(self):
        pass

        # Other methods and attributes to be implemented

        # Constants to be defined

        # Supported HTML tags
        SUPPORTED_HTML_TAGS = {"!doctype", "style", "ag", "a", "address", "b", "big", "blockquote", "body", "br",
                               "center", "cite", "code",
                               "dd", "dfn", "div", "dl", "dt", "em", "font", "h1", "h2", "h3", "h4", "h5", "h6", "head",
                               "hr", "html",
                               "i", "img", "kbd", "meta", "li", "nobr", "ol", "p", "pre", "qt", "s", "samp", "small",
                               "span", "strong",
                               "sub", "sup", "table", "tbody", "td", "tfoot", "th", "thead", "title", "tr", "tt", "u",
                               "ul", "var"}

        # Escaped tags
        ESCAPED_TAGS = {"zuid"}

    # Private method to get plain text
    def _plain(self, keep_new_line: bool = True) -> str:
        assert self._parsed is not None
        if not self._parsed_plain:
            self._parsed_plain = ""
            for n in self._parsed.nodes:
                if n.type == HtmlNode.Type.Tag and (n.text == "<br>" or n.text == "<hr>"):
                    if keep_new_line:
                        self._parsed_plain += "\n"
                    else:
                        self._parsed_plain += ","
                elif n.type in (HtmlNode.Type.Escaped, HtmlNode.Type.BadTag, HtmlNode.Type.Data):
                    self._parsed_plain += n.text
        return self._parsed_plain

    # Private method to check if parsed content is HTML
    def _is_html(self) -> bool:
        assert self._parsed is not None
        return self._parsed.is_correct and self._parsed.has_html_nodes

    # Private method to correct HTML
    def _correct(self) -> str:
        assert self._parsed is not None
        self._parsed_correct = ""
        for n in self._parsed.nodes:
            s = n.text if n.type != HtmlNode.Type.BadTag else f"\"{n.text[1:-1]}\""
            s = s.toHtmlEscaped() if n.type == HtmlNode.Type.Escaped else s
            self._parsed_correct += s
        return self._parsed_correct

    # Method to parse HTML
    def parse(self, html: str) -> HtmlNodes:
        with self._mutex:
            self._parsed_correct = None
            self._parsed_plain = None
            self._parsed = HtmlNodes()

            text = ""
            tag_found = False

            if html != "p, li { white-space: pre-wrap; }":  # Specific condition from C++ code
                for i in range(len(html)):
                    if html[i] == '<':
                        if tag_found:
                            text = f"<{text}{html[i]}"
                            self._parsed._is_correct = False
                            tag_found = False
                        else:
                            if text:
                                node = HtmlNode(HtmlNode.Type.Data, text)
                                self._parsed._nodes.append(node)
                                text = ""
                            tag_found = True
                    elif html[i] == '>':
                        if not tag_found:
                            text += html[i]
                            self._parsed._is_correct = False
                        else:
                            # Parsing tag logic (to be implemented)
                            pass
                            # Additional parsing logic will be added here
                    else:
                        text += html[i]

            if tag_found:
                self._parsed._is_correct = False

            if text:
                node = HtmlNode(HtmlNode.Type.Data, text)
                self._parsed._nodes.append(node)

            return self._parsed

        # Define constants for replacing open and close tags
        Z_HTML_REPLACE_OPEN = "\""
        Z_HTML_REPLACE_CLOSE = "\""

        # Method to underline text

    @staticmethod
    def underline(s: str) -> str:
        return f"<span style=\" text-decoration: underline;\">{s}</span>"

    # Method to align text
    @staticmethod
    def align(s: str, align: Qt.Alignment) -> str:
        alignment = ""
        if align == Qt.AlignLeft:
            alignment = "left"
        elif align == Qt.AlignRight:
            alignment = "right"
        elif align == Qt.AlignCenter:
            alignment = "center"
        else:
            assert False
        return f"<p align=\"{alignment}\">{s}</p>"

    # Parsing logic for tags (part of the `parse` method)
    def _parse_tag(self, text: str) -> None:
        tag = text
        if tag and tag[0] == '/':
            tag = tag[1:]
        space_pos = tag.find(' ')
        if space_pos >= 0:
            tag = tag[:space_pos]
        tag_prepared = tag.lower().strip()

        if tag and tag_prepared in SUPPORTED_HTML_TAGS:
            node = HtmlNode(HtmlNode.Type.Tag, f"<{text}>")
            self._parsed._nodes.append(node)
            self._parsed._has_html_nodes = True
        elif tag and tag_prepared in ESCAPED_TAGS:
            node = HtmlNode(HtmlNode.Type.Escaped, f"<{text}>")
            self._parsed._nodes.append(node)
        else:
            node = HtmlNode(HtmlNode.Type.BadTag, f"<{text}>")
            self._parsed._nodes.append(node)
            self._parsed._is_correct = False

    # Updated method to parse HTML (including tag parsing logic)
    def parse(self, html: str) -> HtmlNodes:
        # ... Previous logic ...
        if html[i] == '>':
            if not tag_found:
                text += html[i]
                self._parsed._is_correct = False
            else:
                self._parse_tag(text)
                text = ""
                tag_found = False

    # Method to escape HTML characters
    def escape(self, s: str) -> str:
        return s.replace('<', "&lt;").replace('>', "&gt;")

    # Method to remove HTML characters
    def remove(self, s: str) -> str:
        with self._mutex:
            s = self.escape(s)
            s = self.plain(s, True)
            s = s.replace(Z_HTML_REPLACE_OPEN, "<").replace(Z_HTML_REPLACE_CLOSE, ">")
            return s

    @staticmethod
    def link(s: str, url: str, target: str = '_blank'):
        return f'<a href="{url}" target="{target}">{s}</a>'

    @staticmethod
    def image(url: str, title: str = ''):
        return f'<img src="{url}" title="{title}"/>'

    @staticmethod
    def font_family(s: str, family: str):
        return f'<span style="font-family:{family};">{s}</span>'

    @staticmethod
    def correct_invalid_chars(s: str):
        s = s.replace('<', Z_HTML_REPLACE_OPEN)
        s = s.replace('>', Z_HTML_REPLACE_CLOSE)
        s = s.replace('&lt;', '<')
        s = s.replace('&gt;', '>')
        return s

    class HtmlNode:
        pass

    class HtmlNodes:
        pass

    class Error:
        pass

    class HtmlTools:
        _mutex = QRecursiveMutex()
        _parsedCorrect = None
        _parsedPlain = None
        _parsed = None

        _supportedHtmlTags = {"!doctype", "style", "ag", "a", "address", "b", "big", "blockquote", "body", "br",
                              "center",
                              "cite", "code", "dd", "dfn", "div", "dl", "dt", "em", "font", "h1", "h2", "h3", "h4",
                              "h5",
                              "h6", "head", "hr", "html", "i", "img", "kbd", "meta", "li", "nobr", "ol", "p", "pre",
                              "qt",
                              "s", "samp", "small", "span", "strong", "sub", "sup", "table", "tbody", "td", "tfoot",
                              "th",
                              "thead", "title", "tr", "tt", "u", "ul", "var"}

        _escapedTags = {"zuid"}

        def __init__(self):
            pass

        @staticmethod
        def plain(s: str, keepNewLine: bool = True) -> str:
            pass

        @staticmethod
        def plain_if_html(s: str, keepNewLine: bool = True) -> bool:
            pass

        @staticmethod
        def is_html(s: str) -> bool:
            pass

        @staticmethod
        def correct(s: str) -> str:
            pass

        @staticmethod
        def correct_if_html(s: str) -> bool:
            pass

        @staticmethod
        def parse(html: str):
            pass

        @staticmethod
        def color(s: str, color: QColor) -> str:
            pass

        @staticmethod
        def bold(s: str) -> str:
            pass

        @staticmethod
        def italic(s: str) -> str:
            pass

        @staticmethod
        def underline(s: str) -> str:
            pass

        @staticmethod
        def align(s: str, align: Qt.Alignment) -> str:
            pass

        @staticmethod
        def font(s: str, size: int) -> str:
            pass

        @staticmethod
        def table(rows: List[str]) -> str:
            pass

        @staticmethod
        def _plain(keepNewLine: bool = True) -> str:
            pass

        @staticmethod
        def _is_html() -> bool:
            pass

        @staticmethod
        def _correct() -> str:
            pass

    class I_CellColumnCheck:
        def cell_check_columns(self, level: int = -1) -> Dict[int, bool]:
            pass

        def set_cell_check_column(self, logical_index: int, visible: bool, enabled: bool, level: int = -1):
            pass

        def is_cell_checked(self, index) -> bool:
            pass

        def set_cell_checked(self, index, checked: bool):
            pass

        def checked_cells(self) -> List:
            pass

        def clear_checked_cells(self):
            pass

        def sg_checked_cell_changed(self, index, checked: bool):
            pass


class HintItemDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        super().__init__(parent)

    def displayText(self, value: QVariant, locale: QLocale) -> str:
        return super().displayText(value, locale)


class MultiLineItemDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        super().__init__(parent)

    def paint(self, painter, option, index):
        options = QStyleOptionViewItem(option)
        self.initStyleOption(options, index)

        painter.save()
        text = index.data()
        document = QTextDocument()
        document.setHtml(text)
        painter.translate(options.rect.left(), options.rect.top())
        document.drawContents(painter)
        painter.restore()

    def sizeHint(self, option, index):
        text = index.data()
        document = QTextDocument()
        document.setHtml(text)
        return QSize(document.idealWidth(), document.size().height())


# Other helper functions and implementations go here


class CheckItemDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        super().__init__(parent)

    def paint(self, painter, option, index):
        # Custom painting logic for checkboxes
        options = QStyleOptionViewItem(option)
        self.initStyleOption(options, index)

        checked = index.data(Qt.CheckStateRole) == Qt.Checked
        if checked:
            options.text = "Checked"
        else:
            options.text = "Unchecked"

        self.parent().style().drawControl(QStyle.CE_ItemViewItem, options, painter)

    def sizeHint(self, option, index):
        return self.parent().style().sizeFromContents(QStyle.CT_ItemViewItem, option, QSize(), index)


# Other helper functions and implementations go here
class ItemDelegate(QStyledItemDelegate):
    def __init__(self, view):
        super().__init__(view)
        self._view = view

    def paint(self, painter, option, index):
        super().paint(painter, option, index)

        # Implement the painting logic here similar to C++ code.

    def editorEvent(self, event, model, option, index):
        result = super().editorEvent(event, model, option, index)

        # Implement the editor event logic here similar to C++ code.

        return result

    def createEditor(self, parent, option, index):
        editor = super().createEditor(parent, option, index)

        # Implement the createEditor logic here similar to C++ code.

        return editor

    def setEditorData(self, editor, index):
        pass
        # Implement the setEditorData logic here similar to C++ code.

    def setModelData(self, editor, model, index):
        pass
        # Implement the setModelData logic here similar to C++ code.

    def updateEditorGeometry(self, editor, option, index):
        pass
        # Implement the updateEditorGeometry logic here similar to C++ code.


class ItemViewDrawHelp(QObject):
    def __init__(self, view):
        super().__init__(view)
        self._view = view
        self._d = ItemViewDrawHelpPrivate()

    def draw_row_number(self, painter, rect, row_num):
        font_metrics = QFontMetrics(self._d.row_num_font)
        text_rect = font_metrics.boundingRect(str(row_num))
        text_rect.moveCenter(rect.center())
        painter.save()
        painter.setFont(self._d.row_num_font)
        painter.setPen(self._d.row_num_color)
        painter.fillRect(rect, self._d.row_num_bg_color)
        painter.drawText(text_rect, self._d.row_num_text_flags, str(row_num))
        painter.restore()

    def draw_empty_message(self, painter, rect, text):
        font_metrics = QFontMetrics(self._d.empty_msg_font)
        text_rect = font_metrics.boundingRect(rect, self._d.empty_msg_text_flags, text)
        text_rect.moveCenter(rect.center())
        painter.save()
        painter.setFont(self._d.empty_msg_font)
        painter.setPen(self._d.empty_msg_color)
        painter.drawText(text_rect, self._d.empty_msg_text_flags, text)
        painter.restore()

    def draw_error_message(self, painter, rect, text):
        font_metrics = QFontMetrics(self._d.error_msg_font)
        text_rect = font_metrics.boundingRect(rect, self._d.error_msg_text_flags, text)
        text_rect.moveCenter(rect.center())
        painter.save()
        painter.setFont(self._d.error_msg_font)
        painter.setPen(self._d.error_msg_color)
        painter.drawText(text_rect, self._d.error_msg_text_flags, text)
        painter.restore()

    def draw_hint(self, painter, rect, text, icon=None):
        font_metrics = QFontMetrics(self._d.hint_font)
        icon_size = self._d.hint_icon.actualSize(rect.size())
        text_rect = font_metrics.boundingRect(rect, self._d.hint_text_flags, text)
        text_rect.moveCenter(rect.center())
        icon_rect = QRect(text_rect.topLeft(), icon_size)
        icon_rect.moveCenter(rect.center())
        painter.save()
        painter.setFont(self._d.hint_font)
        painter.setPen(self._d.hint_color)
        if icon:
            painter.drawPixmap(icon_rect.topLeft(), icon.pixmap(icon_size))
        painter.drawText(text_rect, self._d.hint_text_flags, text)
        painter.restore()

    def draw_frozen_selection(self, painter, rect):
        painter.save()
        painter.setPen(QPen(self._d.frozen_selection_border_color, self._d.frozen_selection_border_width))
        painter.setBrush(self._d.frozen_selection_bg_color)
        painter.drawRect(rect)
        painter.restore()

    def set_row_number_font(self, font):
        self._d.row_num_font = font

    def set_row_number_color(self, color):
        self._d.row_num_color = color

    def set_row_number_bg_color(self, color):
        self._d.row_num_bg_color = color

    # You can add more setter methods for other attributes as needed.


class ItemViewDrawHelpPrivate:
    def __init__(self):
        self.row_num_font = QFont("Arial", 10, QFont.Bold)
        self.row_num_color = QColor(Qt.black)
        self.row_num_bg_color = QColor(Qt.gray)
        self.row_num_text_flags = Qt.AlignCenter

        self.empty_msg_font = QFont("Arial", 10, QFont.Normal)
        self.empty_msg_color = QColor(Qt.darkGray)
        self.empty_msg_text_flags = Qt.AlignCenter | Qt.TextWordWrap

        self.error_msg_font = QFont("Arial", 10, QFont.Bold)
        self.error_msg_color = QColor(Qt.red)
        self.error_msg_text_flags = Qt.AlignCenter | Qt.TextWordWrap

        self.hint_font = QFont("Arial", 10, QFont.Normal)
        self.hint_color = QColor(Qt.darkGray)
        self.hint_text_flags = Qt.AlignCenter | Qt.TextWordWrap
        self.hint_icon = QIcon()

        self.frozen_selection_border_color = QColor(Qt.red)
        self.frozen_selection_border_width = 2
        self.frozen_selection_bg_color = QColor(255, 0, 0, 50)


class ItemViewDrawHelp(QObject):
    def __init__(self, parent: QAbstractItemView):
        super().__init__(parent)
        self._d = ItemViewDrawHelpPrivate()
        self._view = parent

    def draw_row_numbers(self, painter: QPainter, option: QStyleOptionViewItem, index: QModelIndex):
        rect = option.rect
        text = str(index.row() + 1)
        painter.save()
        painter.setFont(self._d.row_num_font)
        painter.setPen(self._d.row_num_color)
        painter.fillRect(rect, self._d.row_num_bg_color)
        painter.drawText(rect, self._d.row_num_text_flags, text)
        painter.restore()

    def draw_empty_message(self, painter: QPainter, rect: QRect, text: str):
        painter.save()
        painter.setFont(self._d.empty_msg_font)
        painter.setPen(self._d.empty_msg_color)
        painter.drawText(rect, self._d.empty_msg_text_flags, text)
        painter.restore()

    def draw_error_message(self, painter: QPainter, rect: QRect, text: str):
        painter.save()
        painter.setFont(self._d.error_msg_font)
        painter.setPen(self._d.error_msg_color)
        painter.drawText(rect, self._d.error_msg_text_flags, text)
        painter.restore()

    def draw_hint(self, painter: QPainter, rect: QRect, text: str):
        painter.save()
        painter.setFont(self._d.hint_font)
        painter.setPen(self._d.hint_color)
        text_rect = painter.boundingRect(rect, self._d.hint_text_flags, text)
        text_rect.moveCenter(rect.center())
        if not self._d.hint_icon.isNull():
            icon_size = self._d.hint_icon.actualSize(text_rect.size())
            icon_rect = QRect(QPoint(0, 0), icon_size)
            icon_rect.moveCenter(QPoint(text_rect.left(), text_rect.center().y()))
            self._d.hint_icon.paint(painter, icon_rect)
            text_rect.moveLeft(icon_rect.right() + 5)
        painter.drawText(text_rect, self._d.hint_text_flags, text)
        painter.restore()

    def draw_frozen_selection(self, painter: QPainter, rect: QRect):
        painter.save()
        painter.setPen(QPen(self._d.frozen_selection_border_color, self._d.frozen_selection_border_width))
        painter.setBrush(self._d.frozen_selection_bg_color)
        painter.drawRect(rect)
        painter.restore()


class ZfItemViewHeaderItem(QStandardItem):
    def __init__(self, text: str, icon: str, section: int, orientation: Qt.Orientation):
        super().__init__(text)
        assert section >= 0, "Section must be non-negative"
        self._section = section
        self._orientation = orientation
        self.setToolTip(text)
        if icon:
            self.setIcon(QIcon(icon))
        self.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

    def orientation(self) -> Qt.Orientation:
        return self._orientation

    def section(self) -> int:
        return self._section

    def set_section(self, section: int):
        assert section >= 0, "Section must be non-negative"
        self._section = section

    def set_orientation(self, orientation: Qt.Orientation):
        self._orientation = orientation


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self._table_model = QStandardItemModel(COL_COUNT, ROW_COUNT, self)
        for row in range(ROW_COUNT):
            for col in range(COL_COUNT):
                self._table_model.setData(self._table_model.index(row, col),
                                          f"Row <b>{row + 1}</b>, <i>Column {col + 1}</i>", Qt.EditRole)

        self._tree_model = QStandardItemModel(COL_COUNT, 0, self)
        for row in range(ROW_COUNT):
            items = [QStandardItem(f"Row {row + 1}, Column {col + 1}") for col in range(COL_COUNT)]
            self._tree_model.invisibleRootItem().appendRow(items)

            for c_row in range(10):
                c_items = [QStandardItem(f"Child row {c_row + 1}, Column {col + 1}") for col in range(COL_COUNT)]
                items[0].appendRow(c_items)

                for c_row1 in range(10):
                    c_items1 = [QStandardItem(f"Child row {c_row1 + 1}, Column {col + 1}") for col in range(COL_COUNT)]
                    c_items[0].appendRow(c_items1)

        self._shrink_table_model = QStandardItemModel(COL_COUNT, 0, self)
        self.add_shrink_row(5)

        self._table_view = TableView()
        self._table_view.setAutoResizeRowsHeight(False)
        self._table_view.setSortingEnabled(True)
        self._table_view.setModel(self._table_model)
        self.configure_header(self._table_view.horizontalRootHeaderItem())

        self._tree_view = TreeView()
        self._tree_view.setModel(self._tree_model)
        self.configure_header(self._tree_view.rootHeaderItem())

        self._shrink_table_view = TableView()
        self._shrink_table_view.setAutoResizeRowsHeight(False)
        self._shrink_table_view.setSortingEnabled(True)
        self._shrink_table_view.setShrinkMinimumRowCount(5)
        self._shrink_table_view.setShrinkMaximumRowCount(10)
        self._shrink_table_view.setAutoShring(True)
        self._shrink_table_view.setModel(self._shrink_table_model)
        self.configure_header(self._shrink_table_view.horizontalRootHeaderItem())

        layout = QVBoxLayout(self)
        layout.addWidget(self._table_view)
        layout.addWidget(self._tree_view)
        layout.addWidget(self._shrink_table_view)
        self.setLayout(layout)

    def configure_header(self, parent: HeaderItem):
        for col in range(COL_COUNT // 2):
            h_name = "The quick brown fox jumps over a lazy dog" if col == 2 else f"Header {col + 1}"
            item = parent.append(h_name)
            item.append("Child header 1")

            if parent.bottomCount() == 3:
                item.append("Not movable").setMovable(False)
            else:
                item.append("Child header 2")

    def add_shrink_row(self, count: int):
        for _ in range(count):
            row = self._shrink_table_model.rowCount() - 1
            items = [QStandardItem(f"Row {row + 1}, Column {col + 1}") for col in range(COL_COUNT)]
            self._shrink_table_model.appendRow(items)

    def remove_shrink_row(self):
        if self._shrink_table_model.rowCount() > 0:
            self._shrink_table_model.removeRows(self._shrink_table_model.rowCount() - 1, 1)

    def on_auto_height_clicked(self):
        self._table_view.setAutoResizeRowsHeight(not self._table_view.isAutoResizeRowsHeight())

    def on_frozen_clicked(self):
        if self._table_view.frozenGroupCount() == 0:
            self._table_view.setFrozenGroupCount(2)
        else:
            self._table_view.setFrozenGroupCount(0)

    def on_check_panel_clicked(self):
        self._table_view.showCheckRowPanel(not self._table_view.isShowCheckRowPanel())
        self._tree_view.showCheckRowPanel(not self._tree_view.isShowCheckRowPanel())

    def on_check_cell_clicked(self):
        if not self._table_view.cellCheckColumns():
            self._table_view.setCellCheckColumn(2, True, True)
        else:
            self._table_view.setCellCheckColumn(2, False, False)

        if not self._tree_view.cellCheckColumns(0):
            self._tree_view.setCellCheckColumn(2, True, True, 0)
            self._tree_view.setCellCheckColumn(2, True, True, 2)
        else:
            self._tree_view.setCellCheckColumn(2, False, False, 0)
            self._tree_view.setCellCheckColumn(2, False, False, 2)

    def on_add_row_clicked(self):
        self.add_shrink_row(1)

    def on_remove_row_clicked(self):
        self.remove_shrink_row()
