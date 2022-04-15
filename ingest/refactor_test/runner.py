from ingest.refactor_test import PipelineCustom
from utils import expand, set_env


# TODO – Developer: Update path to data and/or configuration files as needed.
if __name__ == "__main__":
    set_env()
    pipeline = PipelineCustom(
        expand("config/pipeline_config_refactor_test.yml", __file__),
        expand("config/storage_config_refactor_test.yml", __file__),
    )
    pipeline.run(expand("tests/data/input/data.csv", __file__))
