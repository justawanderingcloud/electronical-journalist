# reads .csv file with event info (event type, event name, event date) and generates an article

import random
import pandas as pd

# read csv with event info into pandas dataframe and count all events
event_frame = pd.read_csv("events.csv")
events_name = event_frame.event_name.to_list()
events_total_count = len(events_name)

# set up multiple pandas dataframes with events according to their types
cinema_event_frame = event_frame[event_frame.event_type == "cinema"]
theatre_event_frame = event_frame[event_frame.event_type == "theatre"]

# load various dataframe columns into lists and count events
cinema_event_name = cinema_event_frame.event_name.to_list()
cinema_event_date = cinema_event_frame.event_date.to_list()
cinema_event_total_count = len(cinema_event_name)

theatre_event_name = theatre_event_frame.event_name.to_list()
theatre_event_date = theatre_event_frame.event_date.to_list()
theatre_event_total_count = len(theatre_event_name)

# parts of articles as templates
templates_0_cinema = ["Fancy watching a movie?", "Wanna see a movie?", "Hungry for some popcorn?"]
templates_0_theatre = ["Long time since your last theatre visit?", "Why not go see a theatre show?",
                       "Time for a formal attire!"]
templates_1 = ["Why not go out to {}.", "Take a friend and go see {}.",
               "Dont just sit on your couch and head out for {}."]
templates_2 = ["You can see it on {}.", "It is going to happen on {}.", "Be there on {}."]
templates_3 = ["You will have the time of your life.", "You might have a nice time.", "Why not enjoy a night out?"]

# select random templates into lists
select_templates_0_cinema = random.sample(templates_0_cinema, cinema_event_total_count)
select_templates_0_theatre = random.sample(templates_0_theatre, theatre_event_total_count)
select_templates_1 = random.sample(templates_1, events_total_count)
select_templates_2 = random.sample(templates_2, events_total_count)
select_templates_3 = random.sample(templates_3, events_total_count)

# article build

if cinema_event_total_count > 0:
    print("Total Cinema Shows:", cinema_event_total_count)
    for pre_intro, intro, event, date_item, \
        event_date_info, outro in zip(select_templates_0_cinema, select_templates_1, cinema_event_name,
                                      select_templates_2, cinema_event_date, select_templates_3):
        print(pre_intro, intro.format(event), date_item.format(event_date_info), outro.format(outro))
else:
    print("No Cinema Shows")

if theatre_event_total_count > 0:
    print("Total Theatre Shows:", theatre_event_total_count)
    for pre_intro, intro, event, date_item, \
        event_date_info, outro in zip(select_templates_0_theatre, select_templates_1, theatre_event_name,
                                      select_templates_2, theatre_event_date, select_templates_3):
        print(pre_intro, intro.format(event), date_item.format(event_date_info), outro.format(outro))
else:
    print("No Theatre Shows")
