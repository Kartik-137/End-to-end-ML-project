from dataclasses import dataclass
from pathlib import Path

# Use a dataclass to automatically generate boilerplate code 
# such as __init__, __repr__, and __eq__ methods.
@dataclass(frozen=True)  # 'frozen=True' makes the instance immutable.
class DataIngestionConfig:
    # Root directory where all data ingestion artifacts will be stored.
    root_dir: Path

    # URL of the data source to be downloaded.
    source_URL: str

    # Local path where the downloaded raw data file will be saved.
    local_data_file: Path

    # Directory where the downloaded file will be extracted/unzipped.
    unzip_dir: Path
