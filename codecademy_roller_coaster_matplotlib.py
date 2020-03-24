# Created by: Ma. Celyn Joyce Raquel

import pandas as pd
import matplotlib.pyplot as plt

# load rankings data here:
steel = pd.read_csv('Golden_Ticket_Award_Winners_Steel.csv')
wood = pd.read_csv('Golden_Ticket_Award_Winners_Wood.csv')
steel = steel.rename(columns = {'Rank': 'ranks', 'Name': 'name', 'Park': 'park', 'Location': 'location', 'Supplier': 'supplier', 'Year Built': 'year_built', 'Points': 'points', 'Year of Rank': 'year_of_rank'})
wood = wood.rename(columns = {'Rank': 'ranks', 'Name': 'name', 'Park': 'park', 'Location': 'location', 'Supplier': 'supplier', 'Year Built': 'year_built', 'Points': 'points', 'Year of Rank': 'year_of_rank'})

# write function to plot rankings over time for 1 roller coaster here:
def ranking_plot_1rc(name, park, ranking_df):
    rankings = ranking_df[(ranking_df.name == name) & (ranking_df.park == park)]
    years = [i for i in rankings.year_of_rank]
    ranks = [i for i in rankings.ranks]
    ax = plt.subplot()
    ax.plot(years,ranks, marker = 'o')
    ax.set_xticks(years)
    ax.set_yticks(ranks)
    ax.invert_yaxis()
    plt.title('{}\'s Rankings from {} to {}'.format(name, years[0], years[-1]))
    plt.xlabel('Years')
    plt.ylabel('Rankings')
    plt.show()

#ranking_plot_1rc('El Toro', 'Six Flags Great Adventure', wood)
plt.clf()

# write function to plot rankings over time for 2 roller coasters here:
def ranking_plot_2rc(name1, park1, name2, park2, ranking_df):
    rankings1 = ranking_df[(ranking_df.name == name1) & (ranking_df.park == park1)]
    years1 = [i for i in rankings1.year_of_rank]
    ranks1 = [i for i in rankings1.ranks]
    print(rankings1)
    rankings2 = ranking_df[(ranking_df.name == name2) & (ranking_df.park == park2)]
    years2 = [i for i in rankings2.year_of_rank]
    ranks2 = [i for i in rankings2.ranks]
    ax = plt.subplot()
    ax.plot(years1,ranks1, marker = 'o', color = 'blue', label = name1)
    ax.plot(years2,ranks2, marker = 'o', color = 'orange', label = name2)
    ax.invert_yaxis()
    plt.title('{}\'s vs. {}\'s Rankings'.format(name1, name2))
    plt.xlabel('Years')
    plt.ylabel('Rankings')
    plt.legend()
    plt.show()
    
#ranking_plot_2rc('El Toro', 'Six Flags Great Adventure', 'Boulder Dash', 'Lake Compounce', wood)
plt.clf()

# write function to plot top n rankings over time here:
def rankings_top_n(n, ranking_df):
    top_n = ranking_df[ranking_df.ranks <= n]
    fig, ax = plt.subplots(figsize = (10,10))
    for rc in set(top_n.name):
        rankings = top_n[top_n.name == rc]
        years = [i for i in rankings.year_of_rank]
        ranks = [i for i in rankings.ranks]
        ax.plot(years, ranks, label = rc)
    ax.invert_yaxis()
    ax.set_yticks(range(n+1)[1:])
    plt.title('Top {} Roller Coasters'.format(n))
    plt.xlabel('Years')
    plt.ylabel('Rankings')
    plt.legend(loc = 4)
    plt.show()
        
#rankings_top_n(5,wood)
plt.clf()

# load roller coaster data here:
roller_coasters = pd.read_csv('roller_coasters.csv')
roller_coasters = roller_coasters.rename(columns = {'num_inversions': 'inversions'})

# write function to plot histogram of column values here:
def hist_coaster(df, column):
    plt.hist(roller_coasters[column].dropna())
    plt.title('Histogram of Roller Coaster {}'.format(column.capitalize()))
    plt.xlabel(column.capitalize())
    plt.ylabel('Frequency')
    plt.show()

#hist_coaster(roller_coasters, 'speed')
#hist_coaster(roller_coasters, 'length')
#hist_coaster(roller_coasters, 'inversions')
plt.clf()

# write function to plot inversions by coaster at a park here:
def inversions(df, park):
    park_data = df[df.park == park]
    park_data = park_data.sort_values('inversions', ascending=False)
    coasters = park_data['name']
    num_inversions = park_data['inversions']
    fig, ax = plt.subplots()
    ax.bar(range(len(coasters)), num_inversions)
    ax.set_xticks(range(len(coasters)))
    ax.set_xticklabels(coasters, rotation = 90)
    plt.title('No. of Inversions By Coaster in {}'.format(park))
    plt.xlabel('Coasters')
    plt.ylabel('Inversions')
    plt.show()

#inversions(roller_coasters, 'Six Flags Great Adventure')
plt.clf()

# write function to plot pie chart of operating status here:
def status(df):
    operating = df[df.status == 'status.operating']
    closed = df[df.status == 'status.closed.definitely']
    counts = [operating.name.count(), closed.name.count()]
    labels = ['Operating', 'Closed']
    fig, ax = plt.subplots(figsize = (7,5.5))
    plt.pie(counts, autopct = '%0.1f%%')
    plt.title('Status of Roller Coasters')
    plt.legend(labels, loc = 4)
    plt.show()

#status(roller_coasters)
plt.clf()

# write function to create scatter plot of any two numeric columns here:
def scatter_2c(df, column1, column2):
    plt.scatter(df[column1], df[column2])
    plt.title('{} vs. {}'.format(column2.capitalize(), column1.capitalize()))
    plt.xlabel(column1.capitalize())
    plt.ylabel(column2.capitalize())
    plt.show()
     
#scatter_2c(roller_coasters, 'height', 'speed')
plt.clf()

#scatter plot with filtering condition
def scatter_2c_filter(df, column1, column2, col, condition, val):
    if condition == 'below':
        df_filtered = df[df[col] < val]
    elif condition == 'above':
        df_filtered = df[df[col] < val]
    plt.scatter(df_filtered[column1], df_filtered[column2])
    plt.title('{} vs. {}'.format(column2.capitalize(), column1.capitalize()))
    plt.xlabel(column1.capitalize())
    plt.ylabel(column2.capitalize())
    plt.show()
    
#scatter_2c_filter(roller_coasters, 'height', 'speed', 'height', 'below', 140)
plt.clf()