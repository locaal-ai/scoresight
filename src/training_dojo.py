import os
import json
from PySide6.QtWidgets import (
    QDialog,
    QListWidgetItem,
    QLabel,
    QVBoxLayout,
    QLineEdit,
    QSizePolicy,
)
from PySide6.QtGui import QPixmap, QKeyEvent, QColor, QBrush, QPainter
from PySide6.QtCore import Qt
from ui_training_dojo import Ui_TrainingDojo


class AspectRatioPixmapLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setScaledContents(False)

    def setPixmap(self, pixmap):
        self.pix = pixmap
        self.update()

    def paintEvent(self, event):
        if hasattr(self, "pix"):
            painter = QPainter(self)
            painter.setRenderHint(QPainter.SmoothPixmapTransform)
            scaled_pixmap = self.pix.scaled(
                self.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation
            )
            x = (self.width() - scaled_pixmap.width()) // 2
            y = (self.height() - scaled_pixmap.height()) // 2
            painter.drawPixmap(x, y, scaled_pixmap)


class CustomLineEdit(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent_dialog = parent

    def keyPressEvent(self, event: QKeyEvent):
        if self.parent_dialog.handle_key_event(event):
            return
        super().keyPressEvent(event)


class TrainingDojo(QDialog):
    def __init__(self, folder_path):
        super().__init__()
        self.ui = Ui_TrainingDojo()
        self.ui.setupUi(self)

        self.folder_path = folder_path
        self.image_files = []
        self.current_index = -1
        self.approved_annotations = self.load_approved_annotations()
        self.show_only_undone = False

        # Replace the default QLineEdit with our CustomLineEdit
        self.custom_line_edit = CustomLineEdit(self)
        self.custom_line_edit.setObjectName("lineEdit_text")
        self.custom_line_edit.setFont(self.ui.lineEdit_text.font())
        self.ui.lineEdit_text.setParent(None)
        self.ui.lineEdit_text = self.custom_line_edit
        self.ui.verticalLayout.insertWidget(1, self.custom_line_edit)

        # Create an AspectRatioPixmapLabel for displaying the image
        # self.image_label = self.ui.label_imagePlaceholder
        self.image_label = AspectRatioPixmapLabel(self)
        self.image_label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.ui.label_imagePlaceholder.setParent(None)
        self.ui.label_imagePlaceholder = self.image_label
        self.ui.widget_image.layout().addWidget(self.image_label)

        self.load_files()
        self.setup_connections()

    def load_approved_annotations(self):
        tracking_file = os.path.join(self.folder_path, "approved_annotations.json")
        if os.path.exists(tracking_file):
            with open(tracking_file, "r") as f:
                return json.load(f)
        return {}

    def save_approved_annotations(self):
        tracking_file = os.path.join(self.folder_path, "approved_annotations.json")
        with open(tracking_file, "w") as f:
            json.dump(self.approved_annotations, f)

    def load_files(self):
        self.ui.listWidget_files.clear()  # Clear existing items
        approved_items = []
        unapproved_items = []
        for file in os.listdir(self.folder_path):
            if file.endswith(".png"):
                base_name = os.path.splitext(file)[0]
                if os.path.exists(os.path.join(self.folder_path, f"{base_name}.txt")):
                    self.image_files.append(base_name)
                    item = QListWidgetItem(base_name)
                    if base_name in self.approved_annotations:
                        item.setForeground(QBrush(QColor("green")))
                        item.setText(f"✓ {base_name}")
                        approved_items.append(item)
                    else:
                        unapproved_items.append(item)

        # Add approved items first, then unapproved items
        for item in approved_items:
            self.ui.listWidget_files.addItem(item)
        for item in unapproved_items:
            self.ui.listWidget_files.addItem(item)

        if self.image_files:
            self.current_index = 0
            self.load_current_item()

    def setup_connections(self):
        self.ui.listWidget_files.itemClicked.connect(self.load_selected_item)
        self.ui.pushButton_next.clicked.connect(self.next_image)
        self.ui.pushButton_prev.clicked.connect(self.prev_image)
        self.ui.lineEdit_text.editingFinished.connect(self.save_text)
        self.ui.pushButton_onlyUndone.clicked.connect(self.toggle_undone_filter)

    def load_current_item(self):
        if 0 <= self.current_index < len(self.image_files):
            base_name = self.image_files[self.current_index]

            # Load image
            image_path = os.path.join(self.folder_path, f"{base_name}.png")
            pixmap = QPixmap(image_path)
            self.image_label.setPixmap(pixmap)

            # Load text
            text_path = os.path.join(self.folder_path, f"{base_name}.txt")
            with open(text_path, "r") as f:
                text = f.read().strip()
            self.ui.lineEdit_text.setText(text)

            # Highlight if approved
            self.highlight_approved()

            # Highlight and scroll to current item in list
            list_index = self.ui.listWidget_files.findItems(
                base_name, Qt.MatchContains
            )[0]
            self.ui.listWidget_files.setCurrentItem(list_index)
            self.ui.listWidget_files.scrollToItem(list_index)

            # Focus on lineEdit_text
            self.ui.lineEdit_text.setFocus()
        else:
            # Clear the UI if no valid item is selected
            self.image_label.clear()
            self.ui.lineEdit_text.clear()

    def load_selected_item(self, item):
        self.current_index = self.ui.listWidget_files.row(item)
        self.load_current_item()

    def load_files(self):
        self.ui.listWidget_files.clear()  # Clear existing items
        self.image_files = []

        for file in os.listdir(self.folder_path):
            if file.endswith(".png"):
                base_name = os.path.splitext(file)[0]
                if os.path.exists(os.path.join(self.folder_path, f"{base_name}.txt")):
                    self.image_files.append(base_name)

        # Sort files by filename
        self.image_files.sort()

        self.update_list_widget()

        if self.image_files:
            self.current_index = 0
            self.load_current_item()

    def update_list_widget(self):
        self.ui.listWidget_files.clear()
        for base_name in self.image_files:
            if not self.show_only_undone or base_name not in self.approved_annotations:
                item = QListWidgetItem(base_name)
                if base_name in self.approved_annotations:
                    item.setForeground(QBrush(QColor("green")))
                    item.setText(f"✓ {base_name}")
                self.ui.listWidget_files.addItem(item)

    def toggle_undone_filter(self):
        self.show_only_undone = self.ui.pushButton_onlyUndone.isChecked()
        self.update_list_widget()
        self.update_current_index()
        self.load_current_item()

    def highlight_approved(self):
        base_name = self.image_files[self.current_index]
        if base_name in self.approved_annotations:
            self.ui.lineEdit_text.setStyleSheet("border: 2px solid green;")
            self.image_label.setStyleSheet("border: 3px solid green;")
        else:
            self.ui.lineEdit_text.setStyleSheet("")
            self.image_label.setStyleSheet("")

    def update_current_index(self):
        if self.show_only_undone:
            # Find the first undone item
            for i, base_name in enumerate(self.image_files):
                if base_name not in self.approved_annotations:
                    self.current_index = i
                    return
            # If all items are done, set current_index to -1
            self.current_index = -1
        else:
            # If there are items, set current_index to 0, otherwise -1
            self.current_index = 0 if self.image_files else -1

    def next_image(self):
        self.save_text()
        start_index = self.current_index
        while True:
            self.current_index = (self.current_index + 1) % len(self.image_files)
            if (
                not self.show_only_undone
                or self.image_files[self.current_index] not in self.approved_annotations
            ):
                break
            if self.current_index == start_index:
                # We've gone through all images and found nothing
                return
        self.load_current_item()

    def prev_image(self):
        self.save_text()
        start_index = self.current_index
        while True:
            self.current_index = (self.current_index - 1) % len(self.image_files)
            if (
                not self.show_only_undone
                or self.image_files[self.current_index] not in self.approved_annotations
            ):
                break
            if self.current_index == start_index:
                # We've gone through all images and found nothing
                return
        self.load_current_item()

    def save_text(self):
        if 0 <= self.current_index < len(self.image_files):
            base_name = self.image_files[self.current_index]
            text_path = os.path.join(self.folder_path, f"{base_name}.txt")
            with open(text_path, "w") as f:
                f.write(self.ui.lineEdit_text.text())

    def approve_annotation(self):
        if 0 <= self.current_index < len(self.image_files):
            base_name = self.image_files[self.current_index]
            self.approved_annotations[base_name] = self.ui.lineEdit_text.text()
            self.save_approved_annotations()
            self.highlight_approved()

            if self.show_only_undone:
                self.update_list_widget()
                self.next_image()
            else:
                # Update list widget item
                items = self.ui.listWidget_files.findItems(base_name, Qt.MatchContains)
                if items:
                    item = items[0]
                    item.setForeground(QBrush(QColor("green")))
                    item.setText(f"✓ {base_name}")

    def unapprove_annotation(self):
        if 0 <= self.current_index < len(self.image_files):
            base_name = self.image_files[self.current_index]
            if base_name in self.approved_annotations:
                del self.approved_annotations[base_name]
                self.save_approved_annotations()
                self.highlight_approved()

                # Update list widget item
                item = self.ui.listWidget_files.item(self.current_index)
                item.setForeground(QBrush(QColor("black")))
                item.setText(base_name)

    def handle_key_event(self, event: QKeyEvent):
        if event.key() == Qt.Key_N:
            self.next_image()
            return True
        elif event.key() == Qt.Key_B:
            self.prev_image()
            return True
        elif event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            if event.modifiers() & Qt.ShiftModifier:
                self.prev_image()
            else:
                self.approve_annotation()
                self.next_image()
            return True
        elif event.key() == Qt.Key_Up:
            if event.modifiers() & Qt.ControlModifier:
                self.jump_to_prev_unapproved()
            else:
                self.prev_image()
            return True
        elif event.key() == Qt.Key_Down:
            if event.modifiers() & Qt.ControlModifier:
                self.jump_to_next_unapproved()
            else:
                self.next_image()
            return True
        elif event.key() == Qt.Key_U:
            self.unapprove_annotation()
            return True
        return False

    def jump_to_next_unapproved(self):
        start_index = (self.current_index + 1) % len(self.image_files)
        for i in range(len(self.image_files)):
            index = (start_index + i) % len(self.image_files)
            if self.image_files[index] not in self.approved_annotations:
                self.current_index = index
                self.load_current_item()
                return
        # If we get here, all items are approved
        print("All items are approved.")

    def jump_to_prev_unapproved(self):
        start_index = (self.current_index - 1) % len(self.image_files)
        for i in range(len(self.image_files)):
            index = (start_index - i) % len(self.image_files)
            if self.image_files[index] not in self.approved_annotations:
                self.current_index = index
                self.load_current_item()
                return
        # If we get here, all items are approved
        print("All items are approved.")

    def keyPressEvent(self, event: QKeyEvent):
        if not self.handle_key_event(event):
            super().keyPressEvent(event)

    # def resizeEvent(self, event):
    #     super().resizeEvent(event)
    #     if hasattr(self, "image_label"):
    #         self.image_label.setFixedSize(self.ui.widget_image.size())
