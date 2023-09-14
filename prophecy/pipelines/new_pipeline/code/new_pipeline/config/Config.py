from prophecy.config import ConfigBase


class Config(ConfigBase):

    def __init__(self, table_name: str=None, db_name: str=None, **kwargs):
        self.spark = None
        self.update(table_name, db_name)

    def update(self, table_name: str="abc", db_name: str="def", **kwargs):
        prophecy_spark = self.spark
        self.table_name = table_name
        self.db_name = db_name
        pass
