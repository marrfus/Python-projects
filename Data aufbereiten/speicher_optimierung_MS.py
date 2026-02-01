import seaborn as sns
import pandas as pd

def df_umwandeln(df):
    df_orig = df.copy()
    for i in df.columns:   
        if df[i].dtype=="float64":
            is_integer = (df[i]%1==0).all()  #if column values integer?
            if is_integer:
                # df[[i]] = df[[i]].astype('integer')
                df[[i]] = df[[i]].astype(int)
            else:
                df[[i]] = df[[i]].apply(pd.to_numeric, downcast="float")
        elif df[i].dtype=="int64":
            df[[i]] = df[[i]].apply(pd.to_numeric, downcast="integer")
        elif df[i].dtype=="object":
            df[[i]] = df[[i]].astype('category')
            # print(f"Original MemUsage von Spalte {i}={df_orig[[i]].memory_usage(deep=True)}\nOptimierte MemUsage = {df[[i]].memory_usage(deep=True)}")
            # if df[[i]].memory_usage(deep=True)>df_orig[[i]].memory_usage(deep=True):
                # df[[i]] = df[[i]].astype('object')
            # print(f"\nProzent von unique Daten in Spalte {i} mit Datatyp object: {(df[i].unique().size/len(df))*100}%")
            if df[i].unique().size/len(df)<0.5:   # weniger 50%??? oder <1
                df[[i]] = df[[i]].astype('category')
            # df[[i]] = df[[i]].astype('category')
    return df



while True:
    try:
        dataset = input("Gib mir die Name von Seaborn Dataset: ")
        df = sns.load_dataset(dataset)
        break
    except Exception as e:
        print(f"Error: {e}")
        continue

# print("\nInfo und aktuellen Speicherverbrauch:")
# print(df.info())
df_opti = df.copy()
# df["cylinders"] = df["cylinders"].astype("float64")
df_opti = df_umwandeln(df_opti)

# print("\nInfo und optimierten Speicherverbrauch:")
# print(f"{df_opti.info()}\n")

print("-"*30)

print(f"War: {df.memory_usage(deep=True).sum()}\nJetzt: {df_opti.memory_usage(deep=True).sum()}")
#Reduction
reduction = (df.memory_usage(deep=True).sum()-df_opti.memory_usage(deep=True).sum())/df.memory_usage(deep=True).sum()
print("-"*30)
print(f"Reduktion um: {reduction*100:0.2f}%")

vergleich_tabelle = pd.DataFrame({
    "column": df.columns,
    "dtype": df.dtypes.values,
    "dtype_opti": df_opti.dtypes.values
})

print(f"\nVergleichtabelle:\n{vergleich_tabelle}")







