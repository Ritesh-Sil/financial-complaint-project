from finance_complaint.component.training.data_ingestion import DataIngestion
from finance_complaint.config.pipeline.training import FinanceConfig



class TrainingPipeline:
    def __init__(self, finance_config : FinanceConfig):
            self.finance_config : FinanceConfig = finance_config

    def start_data_ingestion(self) :        

        try : 
            data_ingestion_config = self.finance_config.get_data_ingestion_config()
            data_ingestion = DataIngestion(data_ingestion_config = data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            return data_ingestion_artifact

        except Exception as e:
            print(e)

        