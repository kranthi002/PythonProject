# import pandas as pd

# tsv_file = 'D:/Files total/Hadoop/DataProject/Movies/title.basics.tsv/data.tsv'

# csv_table = pd.read_table(tsv_file, sep='\t')

# csv_table.to_csv('D:/Files total/Hadoop/DataProject/Movies/title.basics.tsv/data.csv', index= False)

# print("Successfully converted into csv file format")


# Python program to convert .tsv file to .csv file
# importing pandas library
import pandas as pd

tsv_file='D:/Files total/Hadoop/DataProject/Movies/title.basics.tsv/data.tsv'

# reading given tsv file
csv_table=pd.read_table(tsv_file,sep='\t')

# converting tsv file into csv
csv_table.to_csv('D:/Files total/Hadoop/DataProject/Movies/title.basics.tsv/data.csv',index=False)

# output
print("Successfully made csv file")
