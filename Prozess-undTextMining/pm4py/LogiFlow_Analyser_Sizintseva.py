import pandas as pd
import pm4py

# Event Log importieren
# 1. CSV laden
df = pd.read_csv(("pm4py/event_log.csv"), parse_dates=["timestamp"])

# print(df.head())

# 2. Sortieren
df = df.sort_values(["case_id", "timestamp"])

# 3. PM4Py-Format
log = pm4py.format_dataframe(
    df,
    case_id="case_id",
    activity_key="activity",
    timestamp_key="timestamp"
)

# Konvertieren in XES-Log
from pm4py.objects.log.util import dataframe_utils
log = dataframe_utils.convert_timestamp_columns_in_df(log)
log = pm4py.convert_to_event_log(log)

# # Prozess entdecken
# #Inductive Miner
# net, im, fm = pm4py.discover_petri_net_inductive(log) #induktive miner
# # net, im, fm = pm4py.discover_petri_net_heuristics(log)  #heuristic miner

# #Modell visualisieren
# pm4py.view_petri_net(net, im, fm)

# #oder als Prozessbaum
# tree = pm4py.discover_process_tree_inductive(log)
# pm4py.view_process_tree(tree)

#Bottleneck Analyse
case_durations = pm4py.get_all_case_durations(log)
# print(case_durations)

#Performance-Analyse auf Directly-Follows-Graph
dfg, start_activities, end_activities = pm4py.discover_dfg(log)
# print(dfg,"\n", start_activities,"\n", end_activities)

performance_dfg = pm4py.discover_performance_dfg(log)
pm4py.view_performance_dfg(performance_dfg, start_activities, end_activities)

# net, im, fm = pm4py.discover_petri_net_inductive(log)

# pm4py.view_petri_net(
#     net,
#     im,
#     fm,
#     log=log,
#     performance=True
# )











# # 4. In Event Log konvertieren
# event_log = pm4py.convert_to_event_log(log_df)

# # dfg, sa, ea = pm4py.discover_dfg(event_log)
# # pm4py.view_dfg(dfg, sa, ea)

# performance_dfg, sa, ea = pm4py.discover_performance_dfg(event_log)
# pm4py.view_performance_dfg(performance_dfg, sa, ea)