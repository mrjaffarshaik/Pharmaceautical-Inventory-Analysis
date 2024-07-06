import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

df = pd.read_excel("D:/project_191 [pharmaceutical inventory analysis]/DATA SET/Data Set.xlsx")

df

df.describe()

df.info()

df.head() # first 5 rows will be shown

df.tail() # last 5 rows will be shown

print(df.dtypes)

df.columns # all the column name will be shown

df.shape # total number of rows and columns

null = df.isna()


# Rename a column name

df = df.rename(columns = {"Movement Type" : "Movement_Type", "Material Description" : "Material_Description", "Storage Location" : "Storage_Location",
                          "Storage Location" : "Storage_Location", "Posting Date" : "Posting_Date", "Qty in Un. of Entry" : "Qty_in_Un_of_Entry",
                          "Unit of Entry" : "Unit_of_Entry", "Movement Type Text" : "Movement_Type_Text",
                          "Document Date" : "Document_Date", "Qty in OPUn" : "Qty_in_OPUn", "Order Price Unit" : "Order_Price_Unit",
                          "Order Unit" : "Order_Unit", "Qty in order unit" : "Qty_in_order_unit", "Entry Date" : "Entry_Date",
                          "Amount in LC" : "Amount_in_LC", "Purchase Order" : "Purchase_Order", "Movement indicator" : "Movement_indicator",
                          "Base Unit of Measure" : "Base_Unit_of_Measure", "Material Doc. Year" : "Material_Doc_Year", "Debit/Credit ind" : "Debit/Credit_ind",
                          "Trans./Event Type" : "Trans_/Event_Type", "Material Type" : "Material_Type", "Vendor Code" : "Vendor_Code"})


# remove duplicates

duplicate = df.duplicated()  # no duplicates in this dataset
duplicate

sum(duplicate)


df = df.drop_duplicates()
df

numeric_columns = ["Material", "Plant", "Movement_Type","Qty_in_Un_of_Entry", "Qty_in_OPUn", "Qty_in_order_unit",
                     "Amount_in_LC", "Purchase_Order", "Quantity", "Material_Doc_Year", "Vendor_Code"]
df [numeric_columns]


########## MISSING VALUES #################


total_rows = len(df)



missing_values_movement_type = df["Movement_Type"].isna()
sum(missing_values_movement_type)

count_missing1 = sum(missing_values_movement_type)

# Calculate the percentage of missing values
percentage_missing = (count_missing1 / total_rows) * 100

print(percentage_missing)





missing_value_Qty_in_Un_of_Entry = df["Qty_in_Un_of_Entry"].isna()
sum(missing_value_Qty_in_Un_of_Entry)

count_missing2 = sum(missing_value_Qty_in_Un_of_Entry)

# Calculate the percentage of missing values
percentage_missing = (count_missing2 / total_rows) * 100

print(percentage_missing)






missing_value_Qty_in_OPUn = df["Qty_in_OPUn"].isna()
sum(missing_value_Qty_in_OPUn)


count_missing3 = sum(missing_value_Qty_in_OPUn)

# Calculate the percentage of missing values
percentage_missing = (count_missing3 / total_rows) * 100

print(percentage_missing)





missing_value_Qty_in_order_unit = df["Qty_in_order_unit"].isna()
sum(missing_value_Qty_in_order_unit)

count_missing4 = sum(missing_value_Qty_in_order_unit)

# Calculate the percentage of missing values
percentage_missing = (count_missing4 / total_rows) * 100

print(percentage_missing)





missing_value_Amount_in_LC = df["Amount_in_LC"].isna()
sum(missing_value_Amount_in_LC)

count_missing5 = sum(missing_value_Amount_in_LC)

# Calculate the percentage of missing values
percentage_missing = (count_missing5 / total_rows) * 100

print(percentage_missing)






missing_value_Purchase_Order = df["Purchase_Order"].isna()
sum(missing_value_Purchase_Order)

count_missing6 = sum(missing_value_Purchase_Order)

# Calculate the percentage of missing values
percentage_missing = (count_missing6 / total_rows) * 100

print(percentage_missing)






missing_value_Quantity = df["Quantity"].isna()
sum(missing_value_Quantity)

count_missing7 = sum(missing_value_Quantity)

# Calculate the percentage of missing values
percentage_missing = (count_missing7 / total_rows) * 100

print(percentage_missing)






missing_value_Material_Doc_Year = df["Material_Doc_Year"].isna()
sum(missing_value_Material_Doc_Year)

count_missing8 = sum(missing_value_Material_Doc_Year)

# Calculate the percentage of missing values
percentage_missing = (count_missing8 / total_rows) * 100

print(percentage_missing)






missing_value_Vendor_Code = df["Vendor_Code"].isna()
sum(missing_value_Vendor_Code)

count_missing9 = sum(missing_value_Vendor_Code)

# Calculate the percentage of missing values
percentage_missing = (count_missing9 / total_rows) * 100

print(percentage_missing)





# correlation


# Select only numeric columns for correlation calculation

numeric_df = df.select_dtypes(include=['number'])

# Calculate correlation matrix

correlation_matrix = numeric_df.corr()

# Identify highly correlated columns

highly_correlated_columns = set()
for i in range(len(correlation_matrix.columns)):
    for j in range(i):
        if abs(correlation_matrix.iloc[i, j]) > 0.9:  # You can adjust this threshold as needed
            colname = correlation_matrix.columns[i]
            highly_correlated_columns.add(colname)

print("Highly correlated columns:", highly_correlated_columns)


# correlation


# Select only numeric columns for correlation calculation
numeric_data = df.select_dtypes(include=['number'])

# Select only numeric columns
numeric_data = df.select_dtypes(include=['float64', 'int64'])

# Compute the correlation matrix
correlation_matrix = numeric_df.corr()

# Display the correlation matrix
print(correlation_matrix)






####### FIRST MOMENT BUSINESS DECISION ##########

######### MEASURE OF CENTRAL TENDENCY ###########


######### MEAN ###########

df[numeric_columns].mean()

######## MEADIAN #########

df[numeric_columns].median()

######## MODE ############

df[numeric_columns].mode()



############ SECOND MOMENT BUSINESS DECISION ##########

############ MEASURE OF DISPERSION #############


###### VARIANCE #######

df[numeric_columns].var()

######## STANDARD DEVIATION ###########

df[numeric_columns].std()

####### RANGE ##########

df[numeric_columns].max() - df[numeric_columns].min()



############## THIRD MOMENT BUSINESS DECISION #############

############ MEASURE OF ASSEMETRY #############


###### SKEWNESS ########

df[numeric_columns].skew()



############ FOURTH MOMENT BUSINESS DECISION ###########

######## MEASURE OF PEAKNESS ##########


######### KURTOSIS #######

df[numeric_columns].kurt() 



#histogram

plt.hist(df['Material'], color = 'blue', edgecolor = "brown")
plt.title('histogram of material data')
plt.xlabel('numerical data')
plt.ylabel('frequency')
plt.show()

plt.hist(df['Plant'], color = 'black', edgecolor = "yellow")
plt.title('histogram of plant data')
plt.xlabel('numerical data')
plt.ylabel('frequency')
plt.show()

plt.hist(df['Movement_Type'], color = 'red', edgecolor = "black")
plt.title('histogram of Movement_Type data')
plt.xlabel('numerical data')
plt.ylabel('frequency')
plt.show()

plt.hist(df['Qty_in_Un_of_Entry'], color = 'Orange', edgecolor = "blue")
plt.title('histogram of Qty_in_Un_of_Entry data')
plt.xlabel('numerical data')
plt.ylabel('frequency')
plt.show()

plt.hist(df['Qty_in_OPUn'], color = 'red', edgecolor = "black")
plt.title('histogram of Qty_in_OPUn data')
plt.xlabel('numerical data')
plt.ylabel('frequency')
plt.show()

plt.hist(df['Qty_in_order_unit'], color = 'grey', edgecolor = "pink")
plt.title('histogram of Qty_in_order_unit data')
plt.xlabel('numerical data')
plt.ylabel('frequency')
plt.show()

plt.hist(df['Amount_in_LC'], color = 'blue', edgecolor = "brown")
plt.title('histogram of Amount_in_LC data')
plt.xlabel('numerical data')
plt.ylabel('frequency')
plt.show()

plt.hist(df['Quantity'], color = 'purple', edgecolor = "black")
plt.title('histogram of Quantity data')
plt.xlabel('numerical data')
plt.ylabel('frequency')
plt.show()

plt.hist(df['Purchase_Order'], color = 'brown', edgecolor = "blue")
plt.title('histogram of Purchase_Order')
plt.xlabel('numerical data')
plt.ylabel('frequency')
plt.show()


plt.hist(df['Material_Doc_Year'], color = 'brown', edgecolor = "blue")
plt.title('histogram of Material_Doc_Year data')
plt.xlabel('numerical data')
plt.ylabel('frequency')
plt.show()

plt.hist(df['Vendor_Code'], color = 'brown', edgecolor = "blue")
plt.title('histogram of Vendor_Code data')
plt.xlabel('numerical data')
plt.ylabel('frequency')
plt.show()


#BOX PLOT

sns.boxplot(df['Material'])
plt.title('boxplot of Material data')
plt.xlabel('numerical data')
plt.ylabel('frequency')
plt.show()

sns.boxplot(df['Plant'])
plt.title('boxplot of Plant data')
plt.xlabel('numerical data')
plt.ylabel('frequency')
plt.show()

sns.boxplot(df['Movement_Type'])
plt.title('boxplot of Movement_Type data')
plt.xlabel('numerical data')
plt.ylabel('frequency')
plt.show()


sns.boxplot(df['Qty_in_Un_of_Entry'])
plt.title('boxplot of Qty_in_Un_of_Entry data')
plt.xlabel('numerical data')
plt.ylabel('frequency')
plt.show()


sns.boxplot(df['Qty_in_OPUn'])
plt.title('boxplot of Qty_in_OPUn data')
plt.xlabel('numerical data')
plt.ylabel('frequency')
plt.show()

sns.boxplot(df['Qty_in_order_unit'])
plt.title('boxplot of Qty_in_order_unit data')
plt.xlabel('numerical data')
plt.ylabel('frequency')
plt.show()


sns.boxplot(df['Amount_in_LC'])
plt.title('boxplot of Amount_in_LC data')
plt.xlabel('numerical data')
plt.ylabel('frequency')
plt.show()

sns.boxplot(df['Purchase_Order'])
plt.title('boxplot of Purchase_Order data')
plt.xlabel('numerical data')
plt.ylabel('frequency')
plt.show()


sns.boxplot(df['Quantity'])
plt.title('boxplot of Quantity')
plt.xlabel('numerical data')
plt.ylabel('frequency')
plt.show()


sns.boxplot(df['Material_Doc_Year'])
plt.title('boxplot of Material_Doc_Year')
plt.xlabel('numerical data')
plt.ylabel('frequency')
plt.show()


sns.boxplot(df['Vendor_Code'])
plt.title('boxplot of Vendor_Code data')
plt.xlabel('numerical data')
plt.ylabel('frequency')
plt.show()



# Scatter plot


plt.scatter(x = df['Qty_in_Un_of_Entry'],y = df['Quantity'], edgecolors="green")  
plt.show()

plt.scatter(x = df['Qty_in_OPUn'],y = df['Quantity'], edgecolors="green")   
plt.show()

plt.scatter(x = df['Qty_in_order_unit'],y = df['Quantity'], edgecolors="green")
plt.show()

plt.scatter(x = df['Quantity'],y = df['Purchase_Order'], edgecolors="green")
plt.show()

plt.scatter(x = df['Qty_in_Un_of_Entry'],y = df['Purchase_Order'], edgecolors="green")
plt.show()

plt.scatter(x = df['Qty_in_OPUn'],y = df['Purchase_Order'], edgecolors="green")
plt.show()

plt.scatter(x = df['Qty_in_order_unit'],y = df['Purchase_Order'], edgecolors="green")
plt.show()





### DISTPLOT ####


fig, ax = plt.subplots(1, 2)

sns.distplot(df['Quantity'], hist = True, kde = True,
             kde_kws = {'shade': True},
             label = "Non-Normal", color = "green", ax = ax[0])

sns.distplot(df.Qty_in_order_unit, hist = True, kde = True,
             kde_kws = {'shade': True},
             label = "Normal", color = "green", ax = ax[1])

plt.legend(loc = "upper right")



sns.distplot(df['Plant'], hist = True, kde = True,
             kde_kws = {'shade': True},
             label = "Non-Normal", color = "green")




sns.distplot(df['Vendor_Code'], hist = True, kde = True,
             kde_kws = {'shade': True},
             label = "Non-Normal", color = "green")




sns.distplot(df['Amount_in_LC'], hist = True, kde = True,
             kde_kws = {'shade': True},
             label = "Non-Normal", color = "green")




sns.distplot(df['Material_Doc_Year'], hist = True, kde = True,
             kde_kws = {'shade': True},
             label = "Non-Normal", color = "green")




sns.distplot(df['Document_Date'], hist = True, kde = True,
             kde_kws = {'shade': True},
             label = "Non-Normal", color = "green")




fig, ax = plt.subplots(1, 2)

sns.distplot(df['Quantity'], hist = True, kde = True,
             kde_kws = {'shade': True},
             label = "Non-Normal", color = "green", ax = ax[0])

sns.distplot(df.Qty_in_OPUn, hist = True, kde = True,
             kde_kws = {'shade': True},
             label = "Normal", color = "green", ax = ax[1])

plt.legend(loc = "upper right")






fig, ax = plt.subplots(1, 2)

sns.distplot(df['Quantity'], hist = True, kde = True,
             kde_kws = {'shade': True},
             label = "Non-Normal", color = "green", ax = ax[0])

sns.distplot(df.Qty_in_un_of_Entry, hist = True, kde = True,
             kde_kws = {'shade': True},
             label = "Normal", color = "green", ax = ax[1])

plt.legend(loc = "upper right")




fig, ax = plt.subplots(1, 2)

sns.distplot(df['Qty_in_order_unit'], hist = True, kde = True,
             kde_kws = {'shade': True},
             label = "Non-Normal", color = "green", ax = ax[0])

sns.distplot(df.Purchase_Order, hist = True, kde = True,
             kde_kws = {'shade': True},
             label = "Normal", color = "green", ax = ax[1])

plt.legend(loc = "upper right")





fig, ax = plt.subplots(1, 2)

sns.distplot(df['Qty_in_Un_of_Entry'], hist = True, kde = True,
             kde_kws = {'shade': True},
             label = "Non-Normal", color = "green", ax = ax[0])

sns.distplot(df.Purchase_Order, hist = True, kde = True,
             kde_kws = {'shade': True},
             label = "Normal", color = "green", ax = ax[1])

plt.legend(loc = "upper right")





fig, ax = plt.subplots(1, 2)

sns.distplot(df['Qty_in_OPUn'], hist = True, kde = True,
             kde_kws = {'shade': True},
             label = "Non-Normal", color = "green", ax = ax[0])

sns.distplot(df.Purchase_Order, hist = True, kde = True,
             kde_kws = {'shade': True},
             label = "Normal", color = "green", ax = ax[1])

plt.legend(loc = "upper right")



fig, ax = plt.subplots(1, 2)

sns.distplot(df['Quantity'], hist = True, kde = True,
             kde_kws = {'shade': True},
             label = "Non-Normal", color = "green", ax = ax[0])

sns.distplot(df.Purchase_Order, hist = True, kde = True,
             kde_kws = {'shade': True},
             label = "Normal", color = "green", ax = ax[1])

plt.legend(loc = "upper right")



# Q-Q Plot

import scipy.stats as stats
import pylab

stats.probplot(df.Quantity, dist = "norm", plot = pylab)

stats.probplot(df.Movement_Type, dist = "norm", plot = pylab)

stats.probplot(df.Qty_in_Un_of_Entry, dist = "norm", plot = pylab)

stats.probplot(df.Qty_in_OPUn, dist = "norm", plot = pylab)

stats.probplot(df.Qty_in_order_unit, dist = "norm", plot = pylab)

stats.probplot(df.Amount_in_LC, dist = "norm", plot = pylab)

stats.probplot(df.Purchase_Order, dist = "norm", plot = pylab)

stats.probplot(df.Material_Doc_Year, dist = "norm", plot = pylab)

stats.probplot(df.Vendor_Code, dist = "norm", plot = pylab)



#### HEAT MAP

# Compute the correlation matrix
correlation_matrix = df[numeric_columns].corr()

# Plot the heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()






# auto eda

#sweetviz
# pip install sweetviz
import sweetviz as sv
 
s = sv.analyze(df)
s.show_html()


# D-Tale

#pip install dtale
import dtale

d = dtale.show(df)
d.open_browser()








