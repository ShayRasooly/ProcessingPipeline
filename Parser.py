from collections import defaultdict
import json


class Parser:
    def parse(self) -> list[defaultdict]:
        pass


class JSONParser(Parser):

    def __init__(self, file_path):
        self.file_path = file_path

    def parse(self) -> list[defaultdict]:
        with open(self.file_path, 'r') as f:
            records_list = json.load(f)
            for i, record in enumerate(records_list):
                records_list[i] = defaultdict(lambda: None, record)
        return records_list
