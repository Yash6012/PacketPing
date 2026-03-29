from packetping.components.data_ingestion import DataIngestion
from packetping.components.data_validation import DataValidation
from packetping.components.data_transformation import DataTransformation
from packetping.exception.exception import NetworkSecurityException
from packetping.logging.logger import logging
from packetping.entity.config_entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig
from packetping.entity.config_entity import TrainingPipelineConfig
import sys

if __name__ == "__main__":
    try:
        trainingpipelineconfig = TrainingPipelineConfig()
        dataingestionconfig = DataIngestionConfig(trainingpipelineconfig)
        data_ingestion = DataIngestion(dataingestionconfig)
        logging.info("Initiate the data ingestion")
        dataingestionartifact = data_ingestion.initiate_data_ingestion()
        logging.info("Data Initiation completed")
        print(dataingestionartifact)
        datavalidationconfig = DataValidationConfig(trainingpipelineconfig)
        data_validation = DataValidation(dataingestionartifact, datavalidationconfig)
        logging.info("Initiate the data validation")
        data_validation_artifact = data_validation.initiate_data_validation()
        logging.info("Data validation completed")
        print(data_validation_artifact)
        data_transformation_config = DataTransformationConfig(trainingpipelineconfig)
        logging.info("Data Transformation Started")
        data_transformation = DataTransformation(data_validation_artifact, data_transformation_config)
        data_transformation_artifact = data_transformation.initiate_data_transfrormation()
        print(data_transformation_artifact)
        logging.info("Data Transformation Completed")

    except Exception as e:
        raise NetworkSecurityException(e, sys)

