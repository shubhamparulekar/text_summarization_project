from text_summarization.logging import logger
from text_summarization.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from text_summarization.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from text_summarization.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline



STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage Data Ingestion started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage Data Ingestion completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e



STAGE_NAME = "Data Validation stage"
try:
   logger.info(f">>>>>> stage Data Validation started <<<<<<") 
   data_validation = DataValidationTrainingPipeline()
   data_validation.main()
   logger.info(f">>>>>> stage Data Validation completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Data Transformation stage"
try:
   logger.info(f">>>>>> stage Data Transformation started <<<<<<") 
   data_transformation = DataTransformationTrainingPipeline()
   data_transformation.main()
   logger.info(f">>>>>> stage Data Transformation completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
