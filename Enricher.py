import datetime
from collections import defaultdict


def calc_subnet(address, subnet_class):
    if address is None or subnet_class not in ("A", "B", "C"):
        return None
    subnet = str(address).split(".")
    if subnet_class == "A":
        return ".".join(subnet[:1] + (3 * ["0"]))
    if subnet_class == "B":
        return ".".join(subnet[:2] + (2 * ["0"]))
    if subnet_class == "C":
        return ".".join(subnet[:3] + (1 * ["0"]))


def get_iso_time_now():
    return datetime.datetime.now().isoformat()


class Field:
    def __init__(self, name):
        self.name = name

    def create_value(self, record: defaultdict):
        pass


class SubnetField(Field):
    def __init__(self, name, subnet_class="A", relevant_address="srcip"):
        super().__init__(name)
        self.subnet_class = subnet_class
        self.relevant_address = relevant_address

    def create_value(self, record: defaultdict):
        return calc_subnet(record[self.relevant_address], self.subnet_class)


class TimeField(Field):
    def __init__(self, name):
        super().__init__(name)

    def create_value(self, record: defaultdict):
        return get_iso_time_now()


class Enricher:
    DEFAULT_FIELDS = (SubnetField("srcsubA", "A", "srcip"),
                      SubnetField("srcsubB", "B", "srcip"),
                      SubnetField("srcsubC", "C", "srcip"),
                      SubnetField("dstsubA", "A", "dstip"),
                      SubnetField("dstsubB", "B", "dstip"),
                      SubnetField("dstsubC", "C", "dstip"),
                      TimeField("processstarttime"))

    def __init__(self, fields=DEFAULT_FIELDS):
        self.fields = list(fields)

    def add_field(self, field: Field):
        self.fields.append(field)

    def remove_field(self, name: str):
        self.fields = list(filter(lambda field: field.name != name, self.fields))

    def enrich(self, records_list: list[defaultdict]):
        for i, record in enumerate(records_list):
            for field in self.fields:
                records_list[i][field.name] = field.create_value(record)
