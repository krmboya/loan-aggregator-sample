# loan-aggregator

A command that aggregates loans by network, product and month

## Usage

This script requires does not require any third party packages. It only
expects python 3 to be installed (tested in python 3.6)

To test, run the following in the project root:

`python3 loan_aggregator.py Loans.csv Output.csv`

An file named `Output.csv` will be created with the aggregated results.

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


## Assumptions

- All dates are in a standard format

## TODO

- Decimal in the place of float
