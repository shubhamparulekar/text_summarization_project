from text_summarization.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from text_summarization.logging import logger


try:
   logger.info(f">>>>>> stage Data Ingestion started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage Data Ingestion completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e