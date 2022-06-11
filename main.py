import os
import sys
import pandas as pd
import warnings
from death import murder_graph
from death import kill_count
from death import kill_count_total
from death import cause_count
from death import cause_count_total
from death import death_list_combiner

warnings.simplefilter(action='ignore', category=FutureWarning)

os.chdir(os.path.dirname(sys.argv[0]))

# Create the required folders
if not os.path.isdir('graphs'):
    os.mkdir('graphs')

# Load data
attack_on_titan = pd.read_csv('death_lists/attack_on_titan.csv')
jojos_bizarre_adventure = pd.read_csv('death_lists/jojos_bizarre_adventure.csv')
demon_slayer = pd.read_csv('death_lists/demon_slayer.csv')

# Create graphs
murder_graph(attack_on_titan).write_html('graphs/attack_on_titan_who_killed_who_graph.html')
murder_graph(jojos_bizarre_adventure).write_html('graphs/jojos_bizarre_adventure_who_killed_who_graph.html')
murder_graph(demon_slayer).write_html('graphs/demon_slayer_who_killed_who_graph.html')

# Create kill counts
kill_count(attack_on_titan).to_csv('kill_counts/attack_on_titan_top_killers.csv')
kill_count(jojos_bizarre_adventure).to_csv('kill_counts/jojos_bizarre_adventure_top_killers.csv')
kill_count(demon_slayer).to_csv('kill_counts/demon_slayer_top_killers.csv')

# Create kill counts total
kill_count_total([attack_on_titan,jojos_bizarre_adventure,demon_slayer],
    ['attack_on_titan','jojos_bizarre_adventure','demon_slayer']).to_csv('kill_counts/top_killers.csv')

# Create cause counts
cause_count(attack_on_titan).to_csv('cause_counts/attack_on_titan_top_causes.csv')
cause_count(jojos_bizarre_adventure).to_csv('cause_counts/jojos_bizarre_adventure_top_causes.csv')
cause_count(demon_slayer).to_csv('cause_counts/demon_slayer_top_causes.csv')

# Create cause counts total
cause_count_total([attack_on_titan,jojos_bizarre_adventure,demon_slayer]).to_csv('cause_counts/top_causes.csv')

# Combine death lists
death_list_combiner([attack_on_titan,jojos_bizarre_adventure,demon_slayer],
    ['attack_on_titan','jojos_bizarre_adventure','demon_slayer']).to_csv('death_lists/death_list.csv')