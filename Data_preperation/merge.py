import pandas as pd

df1 = pd.read_csv('/Users/stevenzhu/PycharmProjects/LeetCodeQuestion/train_test.csv')

df2 = pd.read_csv('/Users/stevenzhu/PycharmProjects/LeetCodeQuestion/train_test1.csv')

df_combined = pd.concat([df1, df2], ignore_index=True)

df_combined.to_csv('train_test.csv', index=False)