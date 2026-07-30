"""
file_reader.py

Utility module for reading different file formats.

Supported Formats:
- PDF
- DOCX
- TXT

Author: Raju Nalla
"""

from pathlib import Path

import pdfplumber
from docx import Document

from modules.logger import get_logger

logger = get_logger(__name__)


class FileReader:
    """
    Reads text from PDF, DOCX and TXT files.
    """

    def __init__(self):
        self.supported_extensions = [".pdf", ".docx", ".txt"]

    # ----------------------------------------------------------
    # Public Method
    # ----------------------------------------------------------

    def read(self, file_path: str) -> str:
        """
        Reads a file and returns its text.

        Parameters
        ----------
        file_path : str
            Path to the input file.

        Returns
        -------
        str
            Extracted text.
        """

        path = Path(file_path)

        if not path.exists():
            logger.error(f"File not found: {file_path}")
            raise FileNotFoundError(file_path)

        extension = path.suffix.lower()

        logger.info(f"Reading file: {path.name}")

        if extension == ".pdf":
            return self._read_pdf(path)

        elif extension == ".docx":
            return self._read_docx(path)

        elif extension == ".txt":
            return self._read_txt(path)

        else:
            logger.error(f"Unsupported file format: {extension}")
            raise ValueError(
                f"Unsupported file format: {extension}"
            )

    # ----------------------------------------------------------
    # Private Methods
    # ----------------------------------------------------------

    def _read_pdf(self, file_path: Path) -> str:
        """
        Reads PDF files.
        """

        logger.info("Reading PDF document...")

        text = ""

        with pdfplumber.open(file_path) as pdf:

            for page in pdf.pages:

                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

        logger.info("PDF successfully read.")

        return text.strip()

    def _read_docx(self, file_path: Path) -> str:
        """
        Reads DOCX files.
        """

        logger.info("Reading DOCX document...")

        document = Document(file_path)

        paragraphs = []

        for paragraph in document.paragraphs:
            if paragraph.text.strip():
                paragraphs.append(paragraph.text)

        logger.info("DOCX successfully read.")

        return "\n".join(paragraphs)

    def _read_txt(self, file_path: Path) -> str:
        """
        Reads TXT files.
        """

        logger.info("Reading TXT document...")

        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()

        logger.info("TXT successfully read.")

        return text.strip()