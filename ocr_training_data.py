import tempfile
import zipfile
from PySide6.QtWidgets import QDialog, QFileDialog, QMessageBox
import cv2
from numpy import ndarray
from platformdirs import user_data_dir
import os
import uuid

from sc_logging import logger
from text_detection_target import TextDetectionResult, TextDetectionTargetWithResult
from ui_ocr_training_data_dialog import Ui_OCRTrainingDataDialog
from storage import fetch_data, store_data, subscribe_to_data


class OCRTrainingDataOptions:
    def __init__(self):
        self.save_ocr_training_data = fetch_data(
            "scoresight.json", "save_ocr_training_data", False
        )
        subscribe_to_data(
            "scoresight.json", "save_ocr_training_data", self.set_save_ocr_training_data
        )
        self.ocr_training_data_folder = fetch_data(
            "scoresight.json",
            "ocr_training_data_folder",
            os.path.join(user_data_dir("scoresight"), "ocr_training_data"),
        )
        subscribe_to_data(
            "scoresight.json",
            "ocr_training_data_folder",
            self.set_ocr_training_data_folder,
        )
        self.ocr_training_data_max_size = fetch_data(
            "scoresight.json", "ocr_training_data_max_size", 10
        )
        subscribe_to_data(
            "scoresight.json",
            "ocr_training_data_max_size",
            self.set_ocr_training_data_max_size,
        )

    def set_save_ocr_training_data(self, value):
        self.save_ocr_training_data = value

    def set_ocr_training_data_folder(self, value):
        self.ocr_training_data_folder = value

    def set_ocr_training_data_max_size(self, value):
        self.ocr_training_data_max_size = value

    def save_ocr_result_to_folder(
        self, image: ndarray, image_gray: ndarray, result: TextDetectionResult
    ):
        if self.save_ocr_training_data:
            # create the folder if it doesn't exist
            if not os.path.exists(self.ocr_training_data_folder):
                os.makedirs(self.ocr_training_data_folder)

        if (
            result.state == TextDetectionTargetWithResult.ResultState.SameNoChange
            or result.state == TextDetectionTargetWithResult.ResultState.Empty
            or result.text == ""
        ):
            return

        # generate a name for the image and text file using uuid
        uuid_for_image = uuid.uuid4()
        image_name = f"{uuid_for_image}.png"
        image_gray_name = f"{uuid_for_image}_gray.png"
        text_name = f"{uuid_for_image}.txt"

        # write the image to the folder
        cv2.imwrite(os.path.join(self.ocr_training_data_folder, image_name), image)
        cv2.imwrite(
            os.path.join(self.ocr_training_data_folder, image_gray_name), image_gray
        )

        # write the text to the folder
        with open(
            os.path.join(self.ocr_training_data_folder, text_name), "w"
        ) as text_file:
            text_file.write(result.text)


ocr_training_data_options = OCRTrainingDataOptions()


def zip_folder(folder_path, zip_path):
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, folder_path)
                zipf.write(file_path, arcname)


class OCRTrainingDataDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_OCRTrainingDataDialog()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.save_settings)
        self.ui.buttonBox.rejected.connect(self.close)
        self.ui.toolButton_chooseSaveFolder.clicked.connect(self.choose_save_folder)
        self.ui.lineEdit_saveFolder.setText(
            ocr_training_data_options.ocr_training_data_folder
        )
        self.ui.spinBox_maxSize.setValue(
            ocr_training_data_options.ocr_training_data_max_size
        )
        self.ui.pushButton_openFolder.clicked.connect(self.open_folder)
        self.ui.pushButton_saveZipFile.clicked.connect(self.save_zip_file)

    def save_zip_file(self):
        logger.debug("Saving OCR training data zip file")
        folder = self.ui.lineEdit_saveFolder.text()
        if folder:
            # Create a temporary file to store the zip
            with tempfile.NamedTemporaryFile(suffix=".zip", delete=False) as temp_zip:
                temp_zip_path = temp_zip.name
            # Zip the folder
            try:
                zip_folder(folder, temp_zip_path)
            except Exception as e:
                QMessageBox.critical(
                    None, "Error", f"Failed to create zip file: {str(e)}"
                )
                os.unlink(temp_zip_path)
                return

            # Ask user where to save the zip file
            save_path, _ = QFileDialog.getSaveFileName(
                None, "Save Zip File", "", "Zip Files (*.zip)"
            )
            if save_path:
                if not save_path.endswith(".zip"):
                    save_path += ".zip"
                try:
                    # Copy the temp zip to the chosen location
                    with open(temp_zip_path, "rb") as src, open(save_path, "wb") as dst:
                        dst.write(src.read())
                    logger.info(f"Zip file saved to {save_path}")
                except Exception as e:
                    QMessageBox.critical(
                        None, "Error", f"Failed to save zip file: {str(e)}"
                    )
            else:
                logger.info("Zip file was not saved.")

            # Clean up the temporary file
            os.unlink(temp_zip_path)

        else:
            logger.error("No OCR training data folder set")

    def open_folder(self):
        logger.debug("Opening OCR training data save folder")
        folder = self.ui.lineEdit_saveFolder.text()
        if folder:
            os.startfile(folder)

    def choose_save_folder(self):
        logger.debug("Choosing OCR training data save folder")
        folder = self.ui.lineEdit_saveFolder.text()
        folder = QFileDialog.getExistingDirectory(
            self, "Choose OCR training data save folder", folder
        )
        if folder:
            self.ui.lineEdit_saveFolder.setText(folder)

    def save_settings(self):
        logger.debug("Saving OCR training data")
        store_data(
            "scoresight.json",
            "ocr_training_data_save_folder",
            self.ui.lineEdit_saveFolder.text(),
        )
        store_data(
            "scoresight.json",
            "ocr_training_data_max_size",
            self.ui.spinBox_maxSize.value(),
        )
        self.close()
