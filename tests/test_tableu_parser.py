import os
import shutil
import pytest
from src.extractors.tableu_parser import TableauTWBXExtractor
import logging
# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), '../test_data')

@pytest.mark.parametrize("twbx_file", [
    "Product Adoption Scorecard and Analysis.twbx",
])
def test_extract_metadata(tmp_path, twbx_file):
    # Copy test file to temp dir
    src_file = os.path.join(TEST_DATA_DIR, twbx_file)
    temp_file = tmp_path / twbx_file
    shutil.copy(src_file, temp_file)

    # Extractor
    extractor = TableauTWBXExtractor(str(temp_file), extract_dir=str(tmp_path / "extracted"))
    extractor.unzip_twbx()
    metadata = extractor.extract_metadata()
    # print a few keys from the metadata for debugging
    logger.info(f"Extracted metadata keys: {list(metadata.keys())[:5]}")
    # Check if metadata is a dictionary
    assert isinstance(metadata, dict), "Metadata should be a dictionary"
    # Check if metadata is not empty
    assert metadata, "Metadata should not be empty"

