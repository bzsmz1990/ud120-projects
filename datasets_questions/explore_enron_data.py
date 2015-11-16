#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

##############################################################
people_num = len(enron_data)
print "The number of people in the file ", people_num, "\n"


##############################################################
poi_count = 0
for people, feature in enron_data.iteritems():
    if feature["poi"] == 1:
        poi_count += 1

print "The number of people are interested: ", poi_count, "\n"


##############################################################
poi_name_file = open('../final_project/poi_names.txt','r')
poi_name_lines = poi_name_file.readlines()
total_poi = len(poi_name_lines[2:])
print "Total number of POI ", total_poi, "\n"


##############################################################
stock_value = enron_data["PRENTICE JAMES"]["total_stock_value"]
print "Total number of stock that James Prentice had ", stock_value, "\n"


##############################################################
email_messages = enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]
print "Total number of email messages we have from Wesley Colwell to persons of interest ", email_messages, "\n"


##############################################################
stock_value_exercised = enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]
print "Total the value of stock options exercised by Jeffrey Skilling", stock_value_exercised, "\n"


##############################################################
total_payment1 = enron_data["LAY KENNETH L"]["total_payments"]
total_payment2 = enron_data["SKILLING JEFFREY K"]["total_payments"]
total_payment3 = enron_data["FASTOW ANDREW S"]["total_payments"]
print "Total the value of payment by LAY KENNETH L", total_payment1, "\n"
print "Total the value of payment by SKILLING JEFFREY K", total_payment2, "\n"
print "Total the value of payment by FASTOW ANDREW S", total_payment3, "\n"


##############################################################
salary_num = 0
email_num = 0
for people, feature in enron_data.iteritems():
    if feature["salary"] != "NaN":
        salary_num += 1
    if feature["email_address"] != "NaN":
        email_num += 1

print "The number of folks in this dataset have a quantified salary: ", salary_num, "\n"
print "The number of folks in this dataset known email address: ", email_num, "\n"


##############################################################
num_people = 0
for people, feature in enron_data.iteritems():
    if feature["total_payments"] == "NaN":
        num_people += 1

print "The number of people  have NaN for their total payments: ", num_people, "\n"
print "The percentage : ", (num_people + 0.0) / (people_num + 0.0), "\n"


##############################################################
num_poi_people = 0
for people, feature in enron_data.iteritems():
    if feature["total_payments"] == "NaN" and feature["poi"] == 1:
        num_poi_people += 1

print "The number of POI people have NaN for their total payments: ", num_poi_people, "\n"
print "The percentage : ", (num_poi_people + 0.0) / (people_num + 0.0), "\n"
