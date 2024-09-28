import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
df['overweight'] = round(df['weight']/(df['height']/100)**2,)
df['overweight'] = np.where(df['overweight'] > 25, 1, 0)

# 3
df['cholesterol'] = np.where(df['cholesterol'] > 1, 1, 0)
df['gluc'] = np.where(df['gluc'] > 1, 1, 0)

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(
        df,
        id_vars=['cardio'],
        value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'],
        var_name='variable',
        value_name='value'
    )

    # 6
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')

    

    # 7

    graph = sns.catplot(
            x='variable', 
            y='total', 
            hue='value', 
            col='cardio', 
            data=df_cat, 
            kind='bar'
        )


    # 8
    fig = graph.fig


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[
        (df['height'] >= df['height'].quantile(0.025)) & 
        (df['height'] <= df['height'].quantile(0.975)) & 
        (df['weight'] >= df['weight'].quantile(0.025)) & 
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))



    # 14
    fig, ax = plt.subplots(figsize=(12, 10))

    # 15
    sns.heatmap(np.abs(corr), mask=mask,)


    # 16
    fig.savefig('heatmap.png')
    return fig
