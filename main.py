from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationPipeline
from textSummarizer.logging import Logger

STAGE_NAME = 'Data Ingestion Stage'

try:
    Logger.info(f'>>>>>>>> Stage {STAGE_NAME} started <<<<<<<<')
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    Logger.info(f'>>>>>>>> Stage {STAGE_NAME} completed <<<<<<')
except Exception as e:
    Logger.exception(e)
    raise e


STAGE_NAME = 'Data Validation Stage'

try:
    Logger.info(f'>>>>>>>> Stage {STAGE_NAME} started <<<<<<<<')
    data_validation = DataValidationPipeline()
    data_validation.main()
    Logger.info(f'>>>>>>>> Stage {STAGE_NAME} completed <<<<<<')
except Exception as e:
    Logger.exception(e)
    raise e
