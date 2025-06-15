import zipfile
import os
import xmltodict
import logging
# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)



class TableauTWBXExtractor:
    def __init__(self, file_path: str, extract_dir: str = "extracted"):
        self.file_path = file_path
        self.extract_dir = extract_dir
        self.xml_data = None

    def unzip_twbx(self):
        with zipfile.ZipFile(self.file_path, 'r') as z:
            z.extractall(self.extract_dir)

    def extract_metadata(self):
        twb_files = [f for f in os.listdir(self.extract_dir) if f.endswith('.twb')]
        logger.info(f"Found {len(twb_files)} .twb files in the extracted directory.")
        if not twb_files:
            raise FileNotFoundError("No .twb file found inside the .twbx")

        twb_path = os.path.join(self.extract_dir, twb_files[0])
        with open(twb_path, 'rb') as f:
            logger.info(f"Parsing .twb file: {twb_path}")
            self.xml_data = xmltodict.parse(f.read())

        return self._parse_twb_metadata()

    def cleanup(self):
        if os.path.exists(self.extract_dir):
            logger.info(f"Cleaning up extracted directory: {self.extract_dir}")
            for root, dirs, files in os.walk(self.extract_dir, topdown=False):
                for name in files:
                    os.remove(os.path.join(root, name))
                for name in dirs:
                    os.rmdir(os.path.join(root, name))
            os.rmdir(self.extract_dir)

    
    def _parse_twb_metadata(self):
        workbook = self.xml_data.get("workbook", {})
        metadata = workbook
        return metadata