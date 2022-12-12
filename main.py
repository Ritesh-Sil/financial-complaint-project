from finance_complaint.pipeline.training import TrainingPipeline
from finance_complaint.config.pipeline.training import FinanceConfig


if __name__ == "__main__":
    tp = TrainingPipeline(FinanceConfig())
    tp.start_data_ingestion()




