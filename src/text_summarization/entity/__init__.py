from pathlib import Path
from dataclasses import dataclass

@dataclass(frozen=True) # frozen=True makes the dataclass immutable, very important for configuration classes, do not miss to add it
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path 
    unzip_dir: Path

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    status_file: str
    all_required_files: list