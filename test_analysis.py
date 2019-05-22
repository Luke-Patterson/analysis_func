import os, sys
import pandas as pd
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))

from build_msg_net import build_msg_net
from extract_func.clean_API_output import clean_API_output
from extract_func.got_supplement_API_data import get_retweeters_names
from extract_func.get_followers import get_followers
from extract_func.get_followers import follower_time_est
import pandas as pd

df = pd.read_csv('test_input/got_test_output_full_rev_v2.csv')
df_net = build_msg_net(df)
