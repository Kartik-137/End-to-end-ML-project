import os
import urllib.request as request
import zipfile
from red_wine_quality_prediction import logger
from red_wine_quality_prediction.utils.common import get_size
from red_wine_quality_prediction.entity.config_entity import DataIngestionConfig
from pathlib import Path

# defind the data ingestion class

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config


    # Method to download the file from the source URL
    def download_file(self):
        if not os.path.exists(self.config.local_data_file): # Check if file already exists
            filename, headers = request.urlretrieve( # Download the file and return filename 
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} download! with following info: \n{headers}") # Log the download info
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")



    # Method to extract the zip file
    # zip file is in the artifact folder
    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)