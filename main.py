from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationPipeline
from textSummarizer.pipeline.stage_03_data_transformation import DataTransformationPipeline
from textSummarizer.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from textSummarizer.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline
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


STAGE_NAME = 'Data Transformation Stage'

try:
    Logger.info(f'>>>>>>>> Stage {STAGE_NAME} started <<<<<<<<')
    data_transformation = DataTransformationPipeline()
    data_transformation.main()
    Logger.info(f'>>>>>>>> Stage {STAGE_NAME} completed <<<<<<')
except Exception as e:
    Logger.exception(e)
    raise e


# STAGE_NAME = "Model Trainer stage"

# try:
#     Logger.info(f'>>>>>>>> Stage {STAGE_NAME} started <<<<<<<<')
#     model_trainer = ModelTrainerTrainingPipeline()
#     model_trainer.main()
#     Logger.info(f'>>>>>>>> Stage {STAGE_NAME} completed <<<<<<')
# except Exception as e:
#     Logger.exception(e)
#     raise e


STAGE_NAME = "Model Evaluation stage"
try:
    Logger.info(f"*******************")
    Logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    model_evaluation = ModelEvaluationTrainingPipeline()
    model_evaluation.main()
    Logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    Logger.exception(e)
    raise e
