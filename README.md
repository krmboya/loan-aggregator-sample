# loan-aggregator

A command that aggregates loans by network, product and month

## Usage

This script requires does not require any third party packages. It only
expects python 3 to be installed (tested in python 3.6)

To test, run the following in the project root:

`python3 loan_aggregator.py Loans.csv Output.csv`

A file named `Output.csv` will be created with the aggregated results.

Sample input:

```
MSISDN,Network,Date,Product,Amount
27729554427,'Network 1','12-Mar-2016','Loan Product 1',1000
27722342551,'Network 2','16-Mar-2016','Loan Product 1',1122
27725544272,'Network 3','17-Mar-2016','Loan Product 2',2084
27725326345,'Network 1','18-Mar-2016','Loan Product 2',3098
27729234533,'Network 2','01-Apr-2016','Loan Product 1',5671
27723453455,'Network 3','12-Apr-2016','Loan Product 3',1928
27725678534,'Network 2','15-Apr-2016','Loan Product 3',1747
27729554427,'Network 1','16-Apr-2016','Loan Product 2',1801
27729234533,'Network 2','01-Apr-2016','Loan Product 1',5671
27723453455,'Network 3','12-Apr-2016','Loan Product 3',1928
27725678534,'Network 2','15-Apr-2016','Loan Product 3',1747
27729554427,'Network 1','16-Apr-2016','Loan Product 2',1801
27723453455,'Network 3','12-Apr-2016','Loan Product 3',1928
27725678534,'Network 2','15-Apr-2016','Loan Product 3',1747
```

Sample output:

```
Network,Product,Month,Amount,Count
Network 1,Loan Product 1,Mar-2016,1000.00,1
Network 2,Loan Product 1,Mar-2016,1122.00,1
Network 3,Loan Product 2,Mar-2016,2084.00,1
Network 1,Loan Product 2,Mar-2016,3098.00,1
Network 2,Loan Product 1,Apr-2016,11342.00,2
Network 3,Loan Product 3,Apr-2016,5784.00,3
Network 2,Loan Product 3,Apr-2016,5241.00,3
Network 1,Loan Product 2,Apr-2016,3602.00,2
```

## Running tests

Run the following command in the project root:

`python3 tests.py`


## Some assumptions made

- All dates are in a uniform format
- The msisdn column is not required in the aggregated output
- The format `<month>-<year>` is sufficient to uniquely identify a month
- The output amount is standardized to two decimal places

This task is implemented in Python, as it's a high-level dynamic language with
a large standard library that enables rapid prototyping and development.
No third party packages are required to execute this script.

At the core is an ordered dictionary (hashtable) that is used to aggregate
values. 

A hashtable is suitable because the required tuple of network, product and
month can be used as a unique key over with the input data rows are aggregated,
and access to each key in the dictionary is O(1)

Performance by time will therefore grow by O(n) with `n` being the number of rows
in the input file. Memory requirements will grow according the to pattern of
data, the total possible combinations of network by product by month
(Frequency of validation is two months) as only this amount of state
is retained in the ordered dictionary

The Ordered dictionary is used in case it is desirable to preserve the
order in which each (network, product, month) tuple is encountered in the
input file.

Automated tests have been included to test the correctness of the functionality.
Code is auto-formatted using [black](https://github.com/ambv/black)

In case it is not desirable to run this directly as a commandline application,
the class `CommandLineAggregator` is provided, which can be imported and only
requires that the input and output file handles are supplied.
