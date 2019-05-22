from extract_func.extract_tweets import extract_tweets
from extract_func.extract_tweets import extract_counts
from extract_func.extract_tweets_api import extract_tweets_api
from extract_func.extract_tweets_api import extract_counts_api
from extract_func.got_supplement_API_data import get_API_data
import pandas as pd
import numpy as np
from TwitterAPI import TwitterAPI
from TwitterAPI import TwitterPager
import json
import networkx as nx
from ast import literal_eval

# define a user object
class User():


# function to build a messaging network from a set of tweets
def build_msg_net(tweet_df):
    def _leval(x):
        try:
            return literal_eval(x)
        except:
            return None

    # transform dict/list strings to actual dict/list objects
    tweet_df['user_mentions'] = tweet_df['user_mentions'].apply(_leval)
    tweet_df['rt_names'] = tweet_df['rt_names'].apply(_leval)

    # get unique list of tagged and author accounts
    # authors - just take unique values of data frame
    authors = tweet_df.author_name.unique().tolist()

    # mentions - need to manipulate some because there are multiple mentions per tweet sometimes
    mentions = tweet_df['user_mentions'].values.tolist()
    # flatten list
    mentions = [i for j in mentions for i in j]

    # retweeting users
    retweeters = tweet_df['rt_names'].values.tolist()
    # remove None values
    retweeters = [i for i in retweeters if i]
    # flatten list
    retweeters = [i.replace('@','') for j in retweeters for i in j]

    # combine and dedup all the different interacting users
    users = mentions + authors + retweeters
    unique_nodes = list(set(users))
    edge_pairs=[]
    edge_attrib = []
    # draw edges between users mentioning other users
    for i, row in tweet_df.iterrows():
        for j in row['user_mentions']:
            edge_pairs.append([row.author_name, j])
            # add edge attributes
            edge_attrib.append({'favorites':row['favorite_count'],
                'retweets':row['retweet_count']})
        # draw edges between users replying to them
        if row['rt_names'] is not None:
            for j in row['rt_names']:
                edge_pairs.append([row.author_name, j])

    # create networkx network
    G= nx.DiGraph()
    G.add_nodes_from(unique_nodes)
    G.add_edges_from(edge_pairs)
    import pdb; pdb.set_trace()
    # add node characteristics
    # number of followers
    #replyer_nums =
    nx.classes.function.set_node_attributes(G)
    return(G)
