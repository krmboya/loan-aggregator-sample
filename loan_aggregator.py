#!/usr/bin/env python3
from collections import OrderedDict
import csv


def extracted_month(date_str):
    """Returns the month extracted from `date_str`

    e.g. '15-Apr-2016' -> 'Apr-2016' """

    return "-".join(date_str.split("-")[1:])


class Aggregator(object):
    def __init__(self):
        self.aggregates = OrderedDict()
        self.output_fieldnames = ["Network", "Product", "Month", "Amount", "Count"]

    def update_aggregate(self, data):
        """Updates aggregates with data in `data`"""

        running_total = self.aggregates.setdefault(
            (data["network"], data["product"], data["month"]),
            {"amount": 0.0, "count": 0}
        )

        running_total["amount"] += data["amount"]
        running_total["count"] += 1


class CommandLineAggregator(object):
    def __init__(self, input_file, output_file):
        self.aggregator = Aggregator()
        self.reader = csv.DictReader(input_file)
        self.writer = csv.DictWriter(
            output_file,
            self.aggregator.output_fieldnames
        )
    
    def execute(self):
        self.read_input()
        self.write_output()

    def read_input(self):
        for row in self.reader:
            # transform
            data = {
                "network": row["Network"],
                "product": row["Product"],
                "month": extracted_month(row["Date"]),
                "amount": float(row["Amount"])
            }

            self.aggregator.update_aggregate(data)


    def write_output(self):
        pass
