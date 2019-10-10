
# coding: utf-8

# ## Student Details
# 
# When submitting, fill your name and ID in this cell. Note that this is a markdown cell.
# 
# Student Name and ID: Deshpande, Anirudh [axr8193]

# # Programming Assignment 1: 
# # Exploratory Analysis over census data for salaries from the year 1994
# 

# # Assignment Details
# 
# In this assignment, you will conduct a guided exploration over census1994 Dataset. You will learn and use some of the most common exploration/aggregation/descriptive operations. This should also help you learn most of the key functionalities in Pandas.
# 
# You will also learn how to use visualization libraries to identify patterns in data that will help in your further data analysis. You will also explore most popular chart types and how to use different libraries and styles to make your visualizations more attractive.

# # Dataset Details
# 
# In this assignment, you will work on census1994 dataset. This data was extracted from the census bureau database.
# Extraction was done by Barry Becker from the 1994 Census database. The objective of the survey was to determine whether a person makes over 50K a year or not. 
# 
# ### census 1994 Dataset
# 
# ## >50K, <=50K.
# ## age: continuous.
# ## workclass: Private, Self-emp-not-inc, Self-emp-inc, Federal-gov, Local-gov, State-gov, Without-pay, Never-worked.
# ## fnlwgt: continuous.
# ## education: Bachelors, Some-college, 11th, HS-grad, Prof-school, Assoc-acdm, Assoc-voc, 9th, 7th-8th, 12th, Masters, 1st-4th, 10th, Doctorate, 5th-6th, Preschool.
# ## education-num: continuous.
# ## marital-status: Married-civ-spouse, Divorced, Never-married, Separated, Widowed, Married-spouse-absent, Married-AF-spouse.
# ## occupation: Tech-support, Craft-repair, Other-service, Sales, Exec-managerial, Prof-specialty, Handlers-cleaners, Machine-op-inspct, Adm-clerical, Farming-fishing, Transport-moving, Priv-house-serv, Protective-serv, Armed-Forces.
# ## relationship: Wife, Own-child, Husband, Not-in-family, Other-relative, Unmarried.
# ## race: White, Asian-Pac-Islander, Amer-Indian-Eskimo, Other, Black.
# ## gender: Female, Male.
# ## capital-gain: continuous.
# ## capital-loss: continuous.
# ## hours-per-week: continuous.
# ## native-country: United-States, Cambodia, England, Puerto-Rico, Canada, Germany, Outlying-US(Guam-USVI-etc), India, Japan, Greece, South, China, Cuba, Iran, Honduras, Philippines, Italy, Poland, Jamaica, Vietnam, Mexico, Portugal, Ireland, France, Dominican-Republic, Laos, Ecuador, Taiwan, Haiti, Columbia, Hungary, Guatemala, Nicaragua, Scotland, Thailand, Yugoslavia, El-Salvador, Trinadad&Tobago, Peru, Hong, Holand-Netherlands.

# # Required Python Packages
# You will use the packages imported below in this assignment. 
# You will not require any other packages. 

# In[1]:


# special IPython command to prepare the notebook for matplotlib
get_ipython().run_line_magic('matplotlib', 'inline')

#Array processing
import numpy as np
#Data analysis, wrangling and common exploratory operations
import pandas as pd
from pandas import Series, DataFrame

#For visualization. Matplotlib for basic viz and seaborn for more stylish figures
import matplotlib.pyplot as plt
import seaborn as sns
# import seaborn as sns

#For some of the date operations
import datetime
#import datetime


# # Reading Dataset
# The Python code below reads the census1994 dataset into a Pandas data frame with the name df_census. 
# For this code to work, the file 'census1994.csv' must be in the same folder as the notebook.
# 

# In[2]:


#read the csv file into a Pandas data frame
df_census = pd.read_csv('census1994.csv')

#return the first 5 rows of the dataset
df_census.head(10)


# # Task 1: Statistical Exploratory Data Analysis
# Let us start with getting know the dataset. Your first task will be to get some basic information by using Pandas features.

# In[3]:


#For each task below, look for a Pandas function to do the task.
#Replace None in each task with your code.

#Before starting with the tasks in the assignment, we need to remove the rows with missing values
#write the code for it here and save the new data frame with the same name as df_census.
###################begin your code.
#df_census = df.dropna()
df_census_new = df_census.replace(regex='\?', value=np.nan)
df_new_census = df_census_new.dropna()
#print(df_new_census.shape)


###################end your code.


#Task 1-a: Print the details of the df_census data frame (information such as number of rows,columns, name of columns, etc)
print("Task 1-a: Details of df_census data frame are: \n", df_new_census)

#census1994.csv.info(verbose=None, buf=None, max_cols=None, memory_usage=None, null_counts=None)

#Task 1-b: Find the number of rows and columns in the df_census data frame.
num_rows = df_new_census.shape[0]
num_cols = df_new_census.shape[1]
print("\n\nTask 1-b: Number of rows:%s and number of columns:%s" % (num_rows, num_cols)) 


#Task 1-c: Print the descriptive details (min, max, quartiles etc) for 'Age' column of the df_census
print("\n\nTask 1-c: Descriptive details of age is \n", df_new_census['Age'].describe())


#Task 1-d: Print the number of unique values for 'education_num' and 'hours_per_week' columns
num_uniq_1 = df_new_census['education-num'].unique()
num_uniq_2 = df_new_census['hours-per-week'].unique()
print("\n\nTask 1-d: The number of unique 1### :", num_uniq_1)
print("Task 1-d: The number of unique 2### :", num_uniq_2)


# # Task 2: Aggregation & Filtering & Rank
# In this task, we will perform some very high level aggregation and filtering operations. Then, we will apply ranking on the results for some tasks. Pandas has a convenient and powerful syntax for aggregation, filtering, and ranking. DO NOT write a for loop. Pandas has built-in functions for all tasks. 

# In[4]:


#Task 2-a: Find out the sum of Captial Gain for people with education level as Bachelors and HS-Grad.
new_df = df_new_census.groupby('education')['capital-gain']
hd = new_df.groups

hs_grad = new_df.get_group(' HS-grad')
bach_grad = new_df.get_group(' Bachelors')


#print(mdf)
#print(s['education'][0])
#print(g.query('education == "Bachelors" '))
   
    
sum_capital_gain_bachelors = bach_grad.sum()
sum_capital_gain_HS_Grad = hs_grad.sum()


print ("Task 2-a: The sum of capital gain for education level as bachelors is %s and as HS-Grad is %s"% (sum_capital_gain_bachelors, sum_capital_gain_HS_Grad))


#Task 2-b: Find out the total number of people surveyed in months may, october and december.
#Create a new column for 'Survey_Month' by using 'Date' column
#write the code for extracting the month from the date column here

###############begin your code here

df_new_census['Survey_Month'] = pd.DatetimeIndex(df_new_census['Date']).month
#print(df_new_census)
may_surveys = df_new_census[df_new_census['Survey_Month'] == 5]
october_surveys = df_new_census[df_new_census['Survey_Month'] == 10]
#df_new_census[(df_new_census['Survey_Month'] == 9)&(df_new_census['Age'] < 50) & (df_new_census['WorkClass'] == ' Private')]
december_surveys = df_new_census[df_new_census['Survey_Month'] == 8]

#print(october_surveys)
#print(december_surveys)

###############send you code here

num_surveys_may = may_surveys.shape[0]
num_surveys_october = october_surveys.shape[0]
num_surveys_december = december_surveys.shape[0]
print ("\n\nTask 2-b: The total number of surveys in may is %s, in october is %s, and in december is %s" % (num_surveys_may, num_surveys_october, num_surveys_december))


#Task 2-c: Let us now use multiple filtering criteria
# Find out the total number of surveys in september and november with workclass as private and age less than 50.
september_survey = df_new_census[(df_new_census['Survey_Month'] == 9)&(df_new_census['Age'] < 50) & (df_new_census['WorkClass'] == ' Private')]
november_survey = df_new_census[(df_new_census['Survey_Month'] == 11)&(df_new_census['Age'] < 50) & (df_new_census['WorkClass'] == ' Private')]
#print("November suyrvey is as following: ", november_survey.shape)
#for k,v in septe
num_surveys_september = september_survey.shape[0]
num_surveys_november = november_survey.shape[0]
print ("\n\nTask 2-c: The total number of surveys that meet the given conditions in september is %s and in november is %s" % (num_surveys_september, num_surveys_november))


#Task 2-d: Find out 3 least surveyed education categories, print their names and corresponding number of surveys for periods January-June and July-December.
Jan_June_survey = df_new_census[(df_new_census['Survey_Month'] >= 1)&(df_new_census['Survey_Month'] <= 6)]
July_December_survey = df_new_census[(df_new_census['Survey_Month'] >= 7)&(df_new_census['Survey_Month'] <= 12)]
JD_survey = July_December_survey.groupby('education')['Survey_Month']
JJ_survey = Jan_June_survey.groupby('education')['Survey_Month']
#print(JD_survey)
cbmn_dic = []
lokp_dic = []
kj_sur = JJ_survey.count() # JJ
jd_sur = JD_survey.count() # JD
lok = pd.Series(jd_sur) #JD
cgf = pd.Series(kj_sur) #JJ
for ktb, bhej in lok.items():
    cbmn_dic.append((bhej, ktb)) #JD
cbmn_dic.sort()
for kth, bhejio in cgf.items():
    lokp_dic.append((bhejio, ktb)) #JJ
lokp_dic.sort()
jj_lis = lokp_dic[:3]
jd_lis = cbmn_dic[:3]

#print(cbmn_dic)

#jj_lis = JJ_li[:3]
#jd_lis = JD_li[:3]
top3_least_surveyed_Jan_June = jj_lis
top3_least_surveyed_July_December = jd_lis
print ("\n\nTask 2-d: \nThe top 3 least surveyed education categories in January-June: \n%s \n\nThe top 3 least surveyed education categories in July-December: \n%s" % (top3_least_surveyed_Jan_June,top3_least_surveyed_July_December))


#Task 2-e: Find out top 5 native-countries besides United-States, print their names and number of surveys belonging to each.
com_dic = {}
nyc_li, myc_li = [], []
opt = df_new_census[['native-country', 'class']]
#plad = opt[ksl['class'] == ' >50K']
grp_lk = opt.groupby('native-country')['class']
cmr = pd.Series(grp_lk.count())
for khb, bhj in cmr.items():
    com_dic[khb] = bhj
del com_dic[' United-States']
#print(com_dic)
#print(c_dic)
c_lop_li = []
for iexd_c, vla_c in com_dic.items():
    tup = (vla_c, iexd_c)
    #tup.append(val_c)
    c_lop_li.append(tup)

c_lop_li.sort(reverse=True)
#print(c_omg_li)
#c_omg_li.remove('United States')
t_51 = dict(c_lop_li[:5])
#print(top_five)
for gh,gk in t_51.items():
    nyc_li.append(gk)
    myc_li.append(gh)
#print(nyc_li)
top5_most_surveyed_native_countries = nyc_li
print ("\n\nTask 2-e: \nThe top 5 most surveyed native countries : \n%s" % (top5_most_surveyed_native_countries))


#Task 2-f: Find out Top-5 native-countries with the most number of samples belonging to class >50K
c_dic = {}
myk_li, mkj_li = [], []
ksl = df_new_census[['native-country', 'class']]
pol = ksl[ksl['class'] == ' >50K']
grt_df = pol.groupby('native-country')['class']
cdr = pd.Series(grt_df.count())
for ke, be in cdr.items():
    c_dic[ke] = be
#print(c_dic)
c_pol_li = []
for iex_c, vl_c in c_dic.items():
    tup = (vl_c, iex_c)
    #tup.append(val_c)
    c_pol_li.append(tup)

c_pol_li.sort(reverse=True)
t_5 = dict(c_pol_li[:5])
#print(top_five)
for gh,gk in t_5.items():
    myk_li.append(gk)
    mkj_li.append(gh)
#print(val_li)
#print(myk_li)
top5_native_countries = myk_li
print ("\n\nTask 2-f: \nThe top 5 native countries with the most number of surveys with class >50K: \n%s"  % (top5_native_countries))


# # Task 3: Visualization
# In this task, you will perform a number of visualization tasks to get some intuition about the data. Visualization is a key component of exploration. You can choose to use either Matplotlib or Seaborn for plotting. The default figures generated from Matplotlib might look a bit ugly. So you might want to try Seaborn to get better figures. Seaborn has a variety of styles. Feel free to experiment with them and choose the one you like. We have earmarked 10 points for the aesthetics of your visualizations.

# In[12]:


#Task 3-a: Draw a histogram for total number of surveys taken each month. Dislpay months with their corresponding numbers(Eg: January is 1) 
#########################begin code for Task 3-a
#import seaborn as sns

df_new_census['Total'] = df_new_census['Survey_Month'].count()
mydf = df_new_census[['Survey_Month', 'Total']]
#print(mydf)
'''
'''
#sns.set(style="darkgrid")
#comment this line to get the output of any of the visualization.
#ax = sns.countplot(x="Survey_Month", data=mydf)
#print(ax)
#########################end code for Task 3-a


#Task 3-b: Draw a vertical bar chart for total number of surveys taken for each gender for each month. Display months with their corresponding names.
# Remember to make the bar chart into a vertical bar chart
#########################begin code for Task 3-b
mdf = df_new_census[['Survey_Month', 'gender']]
nums = mdf.count()
#print("The nums is: ", nums)
newli = []
main_month = df_new_census['Survey_Month']
#print(main_month)
for j in np.nditer(main_month):
    if(j == 1):
        newli.append('January')
    elif(j == 2):
        newli.append('Febuary')
    elif(j == 3):
        newli.append('March')
    elif(j == 4):
        newli.append('April')
    elif(j == 5):
        newli.append('May')
    elif(j == 6):
        newli.append('June')
    elif(j == 7):
        newli.append('July')
    elif(j == 8):
        newli.append('August')
    elif(j == 9):
        newli.append('September')
    elif(j == 10):
        newli.append('October')
    elif(j == 11):
        newli.append('November')
    elif(j == 12):
        newli.append('December')
    else:
        break

        
#print(newli)
mdf['Month'] = newli
mdf['Total'] = mdf['gender'].count()
mdf['Month'] = mdf['Month']
#print(mdf)
uniarr = np.unique(newli)
plt.figure(figsize=(20,11))
#cx = sns.barplot(x="Month", y="Total", data=mdf, ci=90, order=uniarr)





#########################end code for Task 3-b

#Task 3-c: Draw a horizontal bar chart for number of surveys taken with respect to age feature keeping the age interval as 15.
# Remember to make the bar chart into a horizontal bar chart
#########################begin code for Task 3-c
df_new_census['New_total'] = df_new_census['Age'].count()
#print("total: ", df_new_census)
minimum_age = df_new_census['Age'].min()
maximum_age = df_new_census['Age'].max()
rangelist = []
rng = []
for k in range(minimum_age, maximum_age+1, 15):
    rng.append(k)

for i in np.nditer(df_new_census['Age']):
    rangelist.append(i+15)
    
out = pd.cut(df_new_census['Age'], bins=rng)
ax = out.value_counts(sort=False).plot.barh(rot=0, color="b", figsize=(10,4))
plt.show()



#########################end code for Task 3-c


#Task 3-d: Draw a "vertical" bar chart that lists the top-5 native-countries based on the number of samples with class >50K.
# Remember to make the bar chart into a vertical bar chart
#########################begin code for Task 3-d
count_dict = {}
key_li, val_li = [], []
kdf = df_new_census[['native-country', 'class']]
hdf = kdf[kdf['class'] == ' >50K']
grouped_df = hdf.groupby('native-country')['class']
c = pd.Series(grouped_df.count())
for key, b in c.items():
    count_dict[key] = b
print(count_dict)
countli = []
for index_c, val_c in count_dict.items():
    tup = (val_c, index_c)
    #tup.append(val_c)
    countli.append(tup)

countli.sort(reverse=True)
top_five = dict(countli[:5])
#print(top_five)
for j,k in top_five.items():
    key_li.append(k)
    val_li.append(j)
#print(val_li)

#print(type(c))
kld = pd.DataFrame()
kld['Countries'] = key_li
kld['>50K Surveys'] = val_li
#print(kld)
#count_x = sns.barplot(x="Countries", y=">50K Surveys", data=kld)

#print(grouped_df)


#print(count_li)
#print(hy)
#print(hy)

'''
Mean = grp50.count()
print(Mean)
countli = []
for lm in np.nditer(Mean):
    countli.append(lm)
'''

        
    
#print(grop)

#########################end code for Task 3-d+



#Task 3-e: Now repeat Task 3-d based on education (again top-5)
#########################begin code for Task 3-e
mydic = {}
k_li, v_li = [], []
education = df_new_census[['education', 'class']]
retdf = education[education['class'] == ' >50K']
groups_df = retdf.groupby('education')['class']
c1 = pd.Series(groups_df.count())
for ky, ce in c1.items():
    mydic[ky] = ce
print(mydic)
mycountli = []
for i_c, v_c in mydic.items():
    tup = (v_c, i_c)
    #tup.append(val_c)
    mycountli.append(tup)

mycountli.sort(reverse=True)
my_top_five = dict(mycountli[:5])
#print(top_five)
for j,k in my_top_five.items():
    k_li.append(k)
    v_li.append(j)
#print(val_li)

#print(type(c))
kmd = pd.DataFrame()
kmd['education'] = k_li
kmd['>50K Surveys'] = v_li
kmx = sns.barplot(x="education", y=">50K Surveys", data=kmd)

#########################end code for Task 3-e


#Task 3-f: Draw a scatter plot for age vs hours per week.
#########################begin code for Task 3-f
'''
Just uncomment this comment to get the output.
x = df_new_census['Age']
y = df_new_census['hours-per-week']
plt.scatter(x,y)
plt.show()
'''
df_new_census.plot(kind='scatter', x='Age', y='hours-per-week', c=['darkgray'], s=1)
#########################end code for Task 3-f


#Task 3-g: Draw a line chart showing average capital gain for each education category.
# X-axis : education category, Y-axis : the avg capital gain
#########################begin code for Task 3-g
kdf = df_new_census.groupby('education')['capital-gain']
hd = kdf.groups
key_li = []
values_li = []
for t in hd.keys():
    key_li.append(t)
for l in np.nditer(kdf.mean()):
    values_li.append(l)

    

kl = kdf.mean()
#print(type(kl))
#print(kl)
plt.figure(figsize=(20,11))
plt.plot(sorted(df_new_census['education'].unique()), values_li)
plt.show()
#########################end code for Task 3-g


#Task 3-h: Draw a 'horizontal' bar chart for the top-5 most common occupation. 
#########################begin code for Task 3-h
dic = {}
index_li, value_li = [], []
occu = df_new_census[['occupation', 'Total']]
#retdf = education[education['class'] == ' >50K']
groups_df = occu.groupby('occupation')['Total']
education = groups_df.count()

cn = pd.Series(education)
for ki, ci in cn.items():
    dic[ki] = ci
print(dic)
cli = []
for id_c, vl_c in dic.items():
    tup = (vl_c, id_c)
    #tup.append(val_c)
    cli.append(tup)

cli.sort(reverse=True)
myt = dict(cli[:5])
#print(top_five)
for j,k in myt.items():
    index_li.append(k)
    value_li.append(j)
#print(val_li)

#print(type(c))
ksd = pd.DataFrame()
ksd['occupation'] = index_li
ksd['Popularity_number'] = value_li
jhg = sns.barplot(x="Popularity_number", y="occupation", data=ksd)
#Popularity_number
#########################end code for Task 3-h


#Task 3-i: Draw a 'horizontal' bar chart for the top-5 most common workclass. 
#########################begin code for Task 3-i
di = {}
ind_li, va_li = [], []
work = df_new_census[['WorkClass', 'Total']]
#retdf = education[education['class'] == ' >50K']
work_grp = work.groupby('WorkClass')['Total']
work_class = work_grp.count()

nb = pd.Series(work_class)
for ka, ca in nb.items():
    di[ka] = ca
print(di)
cl = []
for idx_c, vla_c in di.items():
    tup = (vla_c, idx_c)
    #tup.append(val_c)
    cl.append(tup)

cl.sort(reverse=True)
myd = dict(cl[:5])
#print(top_five)
for kv,kd in myd.items():
    ind_li.append(kd)
    va_li.append(kv)
#print(val_li)

#print(type(c))
kjb = pd.DataFrame()
kjb['WorkClass'] = ind_li
kjb['Popularity_number'] = va_li
#print(kjb)
jhg = sns.barplot(x="Popularity_number", y="WorkClass", data=kjb)
#kmx = sns.barplot(x="education", y=">50K Surveys", data=kmd)

#########################end code for Task 3-i




# # Task 4: 
# Find out an interesting information from your census1994 dataset. Create a visualization for it. 
# This task is worth 20 points. Your result will be judged based on the uniqueness and quality of your work (having a meaningful result and an aesthetic visulization). 

# In[6]:


#########################begin code for Task 4
com_dic = {}
nyc_li, myc_li = [], []
opt = df_new_census[['native-country', 'class']]
#plad = opt[ksl['class'] == ' >50K']
grp_lk = opt.groupby('native-country')['class']
cmr = pd.Series(grp_lk.count())
for khb, bhj in cmr.items():
    com_dic[khb] = bhj
del com_dic[' United-States']
#print(com_dic)
#print(c_dic)
c_lop_li = []
for iexd_c, vla_c in com_dic.items():
    tup = (vla_c, iexd_c)
    #tup.append(val_c)
    c_lop_li.append(tup)

c_lop_li.sort(reverse=True)
#print(c_omg_li)
#c_omg_li.remove('United States')
t_51 = dict(c_lop_li[:5])
#print(top_five)
for gh,gk in t_51.items():
    nyc_li.append(gk)
    myc_li.append(gh)
#print(nyc_li)
#print(nyc_li)

labels = nyc_li
sizes = myc_li
colors = ['yellowgreen', 'red', 'Blue', 'green', '#990000']
patches, texts = plt.pie(sizes, colors=colors, startangle=90)
plt.legend(patches, labels, loc="best")
plt.axis('equal')
plt.title('Top five countries above 50K')
plt.tight_layout()
plt.show()

#########################end code for Task 4


# # Grading
# 
# Task 1: 10 points
# Task 2: 30 points
# Task 3: 40 points
# Task 4: 20 points
# 
