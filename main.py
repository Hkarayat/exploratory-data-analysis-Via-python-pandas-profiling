from profile import Profile
import pandas as pd
from pandas_profiling import ProfileReport




# importing the data from csv
df = pd.read_csv("winemag-data-130k-v2.csv")

# generating the report

report = ProfileReport(df)

# Exporting the report to file in HTML
report.to_file(output_file = "report.html" )

