
def get_degree(G):
    import networkx as nx
    # most prolific tweeters
    outdeg_df = pd.DataFrame([[node,val] for (node, val) in sorted(G.out_degree, key=lambda x: x[1], reverse=True)])
    outdeg_df.columns = ['Account', 'Tweets sent']

    # most prolific receivers of tweets
    indeg_df = pd.DataFrame([[node,val] for (node, val) in sorted(G.in_degree, key=lambda x: x[1], reverse=True)])
    indeg_df.columns = ['Account', 'Tweets received']
