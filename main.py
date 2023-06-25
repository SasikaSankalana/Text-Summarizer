from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionPipeline
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
