# excel-to-sql

Purpose:

This script will convert a column of IDs in an Excel to a string ('id1','id2'...'idn') which it can be later used as part of an SQL query where customeraccountno in ('id1','id2'...'idn')

Prerequisites:

Install Python https://www.python.org/downloads/release/python-383/
Open the command prompt CMD and type: pip install pandas , then click enter

Instructions:

The input needs to be 1 column in list-sql.xlsx with header Target-Convert (you can add more columns but the one with Target-Convert should contain the values you want to convert to string)

Once you had completed the step above then double click on run-me.py

The output will be on sql-output.txt
