#!/usr/bin/env python3
import unittest
import io

import loan_aggregator


class TestCleaning(unittest.TestCase):
    def test_clean_month(self):
        input_dates = ["15-Apr-2016", "01-June-2015", "01-Apr-2016"]
        expected_output = ["Apr-2016", "June-2015", "Apr-2016"]
        actual_output = [loan_aggregator.extracted_month(d) for d in input_dates]
        self.assertEqual(expected_output, actual_output)


class TestAggregator(unittest.TestCase):
    def setUp(self):
        self.raw_data = [dict(MSISDN="27729554427", Network="'Network 1'")]

    def test_new_aggregate_correctly_initialized(self):

        data = dict(
            network="Network 1",
            month="June-2015",
            product="Loan Product 1",
            amount=100.0,
        )

        aggregator = loan_aggregator.Aggregator()
        aggregator.update_aggregate(data)
        self.assertEqual(
            aggregator.aggregates[("Network 1", "Loan Product 1", "June-2015")],
            {"amount": 100.0, "count": 1},
        )

    def test_existing_aggregate_correctly_updated(self):

        data = dict(
            network="Network 1",
            month="June-2015",
            product="Loan Product 1",
            amount=100.0,
        )

        aggregator = loan_aggregator.Aggregator()
        aggregator.update_aggregate(data)

        # change data and update
        data["amount"] = 200.0
        aggregator.update_aggregate(data)

        # amount and count should have been updated
        self.assertEqual(
            aggregator.aggregates[("Network 1", "Loan Product 1", "June-2015")],
            {"amount": 300.0, "count": 2},
        )


class TestCommandLineAggregator(unittest.TestCase):
    def setUp(self):
        self.input_file = io.StringIO()
        self.output_file = io.StringIO()
    
    def test_basic_flow(self):
        command = loan_aggregator.CommandLineAggregator(
            self.input_file,
            self.output_file
        )
        command.execute()
        


if __name__ == "__main__":
    unittest.main()
