from Parser import JSONParser
from Enricher import Enricher
from Filter import Filter, EqualRule, NotEqualRule, InListRule, NotInListRule
from Publisher import PrintPublisher


def main():
    entries_list = JSONParser('sample_data.json').parse()
    Enricher().enrich(entries_list)
    rules = [NotEqualRule("dstport", 37771),
             EqualRule("srcsubA", "10.0.0.0"),
             EqualRule("dstsubA", "10.0.0.0"),
             InListRule("protocol", [1, 17]),
             NotEqualRule("dstport", 443),
             NotEqualRule("dstport", 80),
             EqualRule(None, "*")]
    Filter(rules).filter(entries_list)
    PrintPublisher().publish(entries_list)


if __name__ == '__main__':
    main()
