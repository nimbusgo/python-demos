from prophecy.config import ConfigBase


class Config(ConfigBase):

    def __init__(self, param1: str=None, **kwargs):
        self.spark = None
        self.update(param1)

    def update(self, param1: str="xyz", **kwargs):
        prophecy_spark = self.spark
        self.param1 = param1
        pass
