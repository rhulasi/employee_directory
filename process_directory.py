# run this first to parse the pdf
# java -jar tabula-0.9.1-jar-with-dependencies.jar Mailbox\ Employee\ Listing.pdf -c 100,250 -p all > directory.csv


import pandas as pd
df = pd.read_csv('directory.csv')
df.columns=['Mailbox', 'Employee Name', 'Department']
print df.shape

# modify this list to specify which words / phrases indicate that a row should be discarded (headers / footers etc)
remove_filter ={'Employee Name': ['Number of Employees using Mailbo'], 'Mailbox': ['Mailbo','Friday, Octob']}
for field, filters in remove_filter.iteritems():
  for value in filters:
      print field, value
      df.drop(df[df[field]==value].index, inplace=True)
  print df.shape
df['Mailbox'] = df['Mailbox'].ffill()
df.to_csv('usable_directory.csv', index=False)