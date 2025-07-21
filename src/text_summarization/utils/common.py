# import os
# import yaml
# from box.exceptions import BoxValueError
# # from ensure import ensure_annotations
# from box import ConfigBox
# from typing import Any
# from pathlib import Path
# from text_summarization.logging import logger

# # @ensure_annotations
# def read_yaml(path_to_yaml: Path) -> ConfigBox:
#     try:
#         with open(path_to_yaml, 'r', encoding='utf-8') as yaml_file:
#             content = yaml.safe_load(yaml_file)
#             logger.info(f"YAML file {path_to_yaml} read successfully.")
#             return ConfigBox(content)
#     except BoxValueError:
#         # logger.error(f"Error reading YAML file: {e}")
#         raise ValueError(f'yaml file is empty')
#     except Exception as e:
#         raise e
    
# # @ensure_annotations
# def create_directories(paths: list, verbose: True):

#     for path in paths:
#         try:
#             os.makedirs(path, exist_ok=True)
#             logger.info(f"Directory {path} created successfully.")
#         except Exception as e:
#             logger.error(f"Error creating directory {path}: {e}")
#             raise e
        
# # @ensure_annotations
# def get_size(path: Path) -> int:

#     if not path.exists():
#         raise FileNotFoundError(f"The path {path} does not exist.")
    
#     size_in_kb=round(path.stat().st_size / 1024, 2)
#     # logger.info(f"Size of {path} is {size_in_kb} KB.")
#     return f"{size_in_kb} KB"



import os
from box.exceptions import BoxValueError
import yaml
from text_summarization.logging import logger
# from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any



# @ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:

    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    


# @ensure_annotations
def create_directories(path_to_directories: list, verbose=True):

    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")



# @ensure_annotations
def get_size(path: Path) -> str:

    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"

    