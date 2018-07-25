#!/usr/bin/env python3
import argparse
import csv
import sys
from collections import OrderedDict


def extracted_month(date_str):
    """Returns the month extracted from `date_str`

    e.g. '15-Apr-2016' -> 'Apr-2016' """

    return "-".join(date_str.split("-")[1:])


class Aggregator(object):
    def __init__(self):
        self.aggregates = OrderedDict()

    def update_aggregate(self, data):
        """Updates aggregates with data in `data`"""

        running_total = self.aggregates.setdefault(
            (data["network"], data["product"], data["month"]),
            {"amount": 0.0, "count": 0},
        )

        running_total["amount"] += data["amount"]
        running_total["count"] += 1

    def output_rows(self):
        for (network, product, month), totals in self.aggregates.items():
            row = {
                "network": network,
                "product": product,
                "month": month,
                "amount": totals["amount"],
                "count": totals["count"],
            }
            yield row


class CommandLineAggregator(object):
    def __init__(self, input_file, output_file):
        self.aggregator = Aggregator()
        self.reader = csv.DictReader(input_file, quotechar="'")
        self.writer = csv.DictWriter(
            output_file, fieldnames=["Network", "Product", "Month", "Amount", "Count"]
        )

    def execute(self):
        self.read_input()
        self.write_output()

    def read_input(self):
        for row in self.reader:

            data = {
                "network": row["Network"],
                "product": row["Product"],
                "month": extracted_month(row["Date"]),
                "amount": float(row["Amount"]),
            }

            self.aggregator.update_aggregate(data)

    def write_output(self):
        self.writer.writeheader()

        for row in self.aggregator.output_rows():
            output_row = {}
            for key, value in row.items():
                output_row[key.title()] = value
            self.writer.writerow(output_row)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="A script that aggregates loans by network, product and month",
        add_help=True,
    )

    parser.add_argument("input_file", help="Path to input file")
    parser.add_argument("output_file", help="Path to output file")
    args = parser.parse_args()

    try:
        with open(args.input_file, newline="") as input_file, open(
            args.output_file, "w", newline=""
        ) as output_file:

            aggregator = CommandLineAggregator(
                input_file, output_file
            )
            aggregator.execute()

    except IOError as e:
        sys.stderr.write("An IO error was encountered: {}\n".format(e))
        sys.exit(1)
