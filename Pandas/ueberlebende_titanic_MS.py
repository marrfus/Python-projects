import pandas as pd 
import seaborn as sns


df = sns.load_dataset('titanic')

df.age.value_counts()
print("Unique age:")
print(df['age'].unique())
print("Age values:")
print(df['age'].value_counts())
print("Classes:")
print(df['pclass'].unique())

print("-"*30)

#Familiengröße = parch + sibsp +1
df.insert(7, "family_size",(df.parch + df.sibsp +1) )
print(df.head())

print("-"*30)

#Alter in Kategorien
categories = ['0-11','12-17','18-25','26-35','36-50','51-70','70+']
bins = [0,12,18,26,36,51,70,120]

df['age_group'] = pd.cut(df['age'], bins=bins, labels=categories )
print(df.head())
print(df.age_group.value_counts())

#Statistiken pro Gruppe.
df_gr = df.groupby(['age_group'], as_index=False, 
                    observed=False).agg({
                                            'survived':['size', 'mean'],
                                            'fare':'mean'
                                                                        })
print(df_gr)


#Pivot table Überlebensrate Klasse vs Geschlecht

df_pivot = pd.pivot_table(
    df, 
    values='survived', 
    index='sex', 
    columns='pclass', 
    aggfunc=['mean','sum'])
df_pivot.reset_index()
print(df_pivot)


#Challenge
cat_fam_size = ['alone','family']
bins_fam_size = [0,1,15]
df['statement'] = pd.cut(
    df['family_size'], 
    bins=bins_fam_size, 
    labels=cat_fam_size)
print(df.head())

df_chall = df.groupby('statement', as_index=False, 
                    observed=False).agg({'fare':'mean'})
# df_chall = df.groupby(['statement','pclass'], as_index=False, 
                    # observed=False).agg({'fare':'mean'})
print(df_chall)