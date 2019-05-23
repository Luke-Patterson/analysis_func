import pandas as pd
import numpy as np
import networkx as nx
from datetime import datetime

# function to calculate reach of a messaging network
def get_reach(G, start_date = datetime(2006,1,1), end_date = datetime.now()):
    # create subgraph of links within specified time frame
    sub_G = nx.DiGraph()
    sub_G.add_nodes_from(G.nodes.items())
    subsect_edges = [(i[0],i[1],attrdict) for i,attrdict in G.edges.items() if
         pd.Timestamp.to_pydatetime(attrdict['date'])>= start_date and
         pd.Timestamp.to_pydatetime(attrdict['date'])<=end_date]
    sub_G.add_edges_from(subsect_edges)
    # remove isolated nodes from subgraph
    isolates = [i for i in nx.isolates(sub_G)]
    sub_G.remove_nodes_from(isolates)

    # impressions - number of people this appeared in their time line for
    # followers of original authors + followers of retweeters
    # this is sum of followers amongst nodes with out degree > 1
    sub_G2 = sub_G.subgraph([i for i,j in sub_G.out_degree if j > 0])
    follower_nums = [attr['follower_count'] for i,attr in sub_G2.nodes.items()]
    impressions = np.nansum(follower_nums, dtype = 'int')

    # interactions - number of people that directly interacted with tweets
    # retweeting or favoriting are the only interactions we have a direct view of
    # so simple sum of those amongst edges
    interactions = np.nansum([attr['favorites'] for i,attr in G.edges.items()] +
        [attr['retweets'] for i,attr in G.edges.items()], dtype = 'int')

    return({'impressions':impressions, 'interactions':interactions})


# function to create a graph of reach over time
def reach_graph(tweet_df, start_date = None, end_date = None, time_step = 'days'):
    return(reach_graph)
