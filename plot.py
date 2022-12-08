from rng import q_9_rng, q_10_rng
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as pltlyexp

q9_df = q_9_rng()
q10_df = q_10_rng()


def plot_bar_q9():
    q9_df.set_index('countries').plot(kind='bar', rot=0, title="Plastic Waste Generated per person (2022)").set_ylabel("Plastic Waste Per Person Per Year (Kg)")
    plt.show()
    

#make user interact with tree
def plot_tree_q9():
    labels = q9_df['countries'].values
    sizes = q9_df['plastic waste per capita'].values
    fig = pltlyexp.treemap(q9_df, path=[labels], values=sizes, title="Plastic Waste Generated per person (2022)")
    fig.show()



def plot_bar_q10():
    q10_df.set_index('countries').plot(kind='bar', rot=0, title="Amount of money spent recycling plastic per country (2022)").set_ylabel("Money spent (€)")
    plt.show()


plot_tree_q9()