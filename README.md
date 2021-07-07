# Kaspien Code Challenge

This repository has the solution for the Kaspien Code Challenge presented to the author. The task description is in the file task.txt and the code with the solution is in the file reports.py

## Solution explanation

The following steps were considered to provide the soltution to the task:

* The input file was read into the "sales" dataframe
* The "ORDER_DATE" was converted into datetime time
* Two new dataframes were created as outputs: one for the average and another for the total. Both of them were gouped by the "PRODUCT_ID" and, in a higher level, by the "ORDER_DATE", configured as weeks
* Both dataframes were formated to show the collums in a specific order ("ORDER_DATE", "PRODUCT_ID", "UNITS_ORDERED"). After that, the "UNITS_ORDERED" column was renamed on both dataframes, one for "AVG_UNITS_ORDERED" and the other for "TOTAL_UNITS_ORDERED"
* Finally, the dataframes are printed and the output files are generated

## Running the code

To launch the solution, just run the command below.

```bash
python reports.py
```

The file data_engineering_data.csv must be in the same folder. The files output_avg.csv and output_total.csv are also generated after the program finishes.

## Author

Matheus Bandini (matheusbandini@gmail.com)
