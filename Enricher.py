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

    def create_value(self, entry: defaultdict):
        pass


class SubnetField(Field):
    def __init__(self, name, subnet_class, ip_key):
        super().__init__(name)
        self.subnet_class = subnet_class
        self.ip_key = ip_key

    def create_value(self, entry: defaultdict):
        return calc_subnet(entry[self.ip_key], self.subnet_class)


class TimeField(Field):
    def create_value(self, entry: defaultdict):
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

    def enrich(self, entries_list: list[defaultdict]):
        for i, entry in enumerate(entries_list):
            for field in self.fields:
                entries_list[i][field.name] = field.create_value(entry)
