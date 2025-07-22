import os
from text_summarization.logging import logger
from text_summarization.entity import DataValidationConfig

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_files_exist(self):
        try:
            validation_status = True
            all_files = os.listdir(os.path.join("artifacts", "data_ingestion", "samsum_dataset"))

            for files in all_files:
                if files not in self.config.all_required_files:
                    validation_status = False
                else:
                    validation_status = True

            return validation_status

        except Exception as e:
            raise e