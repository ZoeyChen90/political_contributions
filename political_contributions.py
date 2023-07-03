import pandas as pd

df_2008 = pd.read_csv('2008_政治獻金.csv')
revenue_2008_df = df_2008[['姓名','總收入']]
revenue_2008_df

df_2012 = pd.read_csv('2012_政治獻金.csv')
revenue_2012_df = df_2012[['姓名','總收入']]
revenue_2012_df

df_2016 = pd.read_csv('2016_政治獻金.csv')
revenue_2016_df = df_2016[['姓名','總收入']]
revenue_2016_df

# 合併表格
merged_df1 = pd.merge(revenue_2008_df, revenue_2012_df, on = '姓名', how = 'inner')
merged_df2 = pd.merge(merged_df1, revenue_2016_df, on = '姓名', how = 'inner')
merged_df2

# 更改欄位名稱
merged_df2 = merged_df2.rename(columns = {'總收入_x' : '2008年_政治獻金', '總收入_y' : '2012年_政治獻金', '總收入' : '2016年_政治獻金'})
merged_df2.head()

# 判斷政治獻金是否連兩屆成長
import numpy as np

merged_df2['政治獻金連兩屆成長'] = np.where((merged_df2['2012年_政治獻金'] > merged_df2['2008年_政治獻金']) & (merged_df2['2016年_政治獻金'] > merged_df2['2012年_政治獻金']), '是', '否')
merged_df2.head()

# 政治獻金連兩屆成長的名單
merged_df3 = merged_df2[merged_df2['政治獻金連兩屆成長'] == '是']
merged_df3

# 標註 2016 是否連任
elected_2016_df = df_2016[['姓名', '當選註記', '是否現任']]
elected_2016_df['2016年是否連任'] = np.where((elected_2016_df['當選註記'] == '*') & (elected_2016_df['是否現任'] == '是'), '是', '否')
elected_2016_df

# 合併表格
merged_df4 = pd.merge(merged_df3, elected_2016_df, on = '姓名', how = 'inner')
merged_df5 = merged_df4[['姓名', '2008年_政治獻金', '2012年_政治獻金', '2016年_政治獻金', '政治獻金連兩屆成長', '2016年是否連任']]

sorted_df = merged_df5.sort_values(by = '2016年是否連任', ascending = False)
sorted_df

# 連兩屆政治獻金成長候選人之 2016 年連任占比
import matplotlib.pyplot as plt

re_elected = merged_df5['2016年是否連任'].value_counts()

plt.pie(re_elected, autopct = '%1.1f%%', startangle = 90)
plt.axis('equal')
plt.show()


