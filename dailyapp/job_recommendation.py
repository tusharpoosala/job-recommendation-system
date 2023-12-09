import json #  json package iteratively parse the json file instead of reading it all in at once
import sys
import pandas as pd
import numpy as np
from pandas import DataFrame
from IPython.display import Image
from collections import Counter

filename = "datasets/data_science_extract.json"


def js_data(filename):
    # open JSON file and parse contents
    with open(filename, 'r', encoding="utf-8") as f_in:
        objects = json.load(f_in)
        columns = objects
    return columns


# Reformat columns to dictionary with profile id as key
def reformat_to_dict(columns):
    profiles = {}
    for c in columns:
        profiles[c['id']] = c 
    return profiles

# Given profile ID
def profile_id(columns):
    profile_ids = [c['id'] for c in columns]
    return profile_ids


#https://medium.com/@gis10kwo/converting-nested-json-data-to-csv-using-python-pandas-dc6eddc69175    
if __name__ == "__main__":
    columns = js_data(filename)
    profiles = reformat_to_dict(columns)
    #print profiles[1]

    selected_row = []   
    for row in columns:
        selected_row.append(row)
    column_headers= len(selected_row)
    #print column_headers
    all_rows = []
    for i in selected_row:
        all_rows.append(i)
    #print all_rows[0:3]



# print profile_id(columns)
# print "The length of the column is equal to the total number of profile_id within the dataset {}".format(len(columns))
# msgs =json_normalize(columns)
# msgs.dtypes
# print selected_row[0]['careerjunction_za_skills']
# print selected_row[5]['careerjunction_za_skills']

def new_source(dict_l):
    good_columns = ["id","careerjunction_za_courses", "careerjunction_za_skills",
                "careerjunction_za_recent_jobtitles","careerjunction_za_primary_jobtitle"]
    n = {}
    k = 'id'
    for k,v in dict_l.items():
        for i in good_columns:
            if i==k:
                n[k] = v
    return n
new_source(all_rows[3])

# extracting and making the list from the all_rows
def extract_values(count_lst_id):
    return count_lst_id.values()

value_lst_count0 = extract_values(all_rows[0])
value_lst_count1 = extract_values(all_rows[1])
value_lst_count2 = extract_values(all_rows[2])
value_lst_count3 = extract_values(all_rows[3])
value_lst_count4 = extract_values(all_rows[4])
value_lst_count5 = extract_values(all_rows[5])


# pro_id_5 = value_lst_count5[-1]
# pro_id_4 = value_lst_count4[-1]
# pro_id_3 = value_lst_count3[-1]
# pro_id_2 = value_lst_count2[-1]
# pro_id_1 = value_lst_count1[-1]
# pro_id_0 = value_lst_count0[-1]




print("[%s]" % ", ".join(map(str, value_lst_count0)) )

def extract_dict_keys(dict_keys):
    return map(str,dict_keys.keys())

dict_keys = extract_dict_keys(profiles[2]) # remove the u' unicode
#print dict_keys
#print map(str, dict_keys)



def subsequence_counts_2(sequences):
    counts = Counter()
    for sequence in sequences:
        input = "".join(sequence)
        for j in range(1,len(input)+1):
    #this involves copying across the whole contents of counts into the new object.
            counts.update(input[i:i+j] for i in range(len(input)-(j-1)))
    return counts


from math import *


def jaccard_similarity(x, y):
    intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
    union_cardinality = len(set.union(*[set(x), set(y)]))
    return intersection_cardinality / float(union_cardinality)


# Function to check profile similiarities
from collections import defaultdict


class DictionaryIntersection(object):
    def __init__(self, dictA, dictB):
        self.dictA = dictA
        self.dictB = dictB

    def __getitem__(self, attr):
        if attr not in self.dictA or attr not in self.dictB:
            raise KeyError('Not in both dictionaries,key: %s' % attr)
        # for c in dictA[attr];
        #   if c == 2:
        #      return dictA[attr]
        return self.dictA[attr], self.dictB[attr]


# Getting the profile_ID and element and grouped using the profile ID
# Getting the profile_ID and element and grouped using the profile ID
# Given profile ID
def get_profile__id(id):
    prof_id = []
    for i in profile_id(columns):
        if i == id:
            return id


def similar(data_a, data_b):
    third_dict = {}
    for k, v in data_b.items():
        vals = []
        if isinstance(v, list):  # check the nested list in dictionary
            for i in v:
                # print i
                vals.append(data_a.get(i))  # grab all values in dict and add
        else:
            vals.append(data_a.get(v))
            return "similar"
        if not vals:
            return "not similar"
        third_dict[k] = vals
    return third_dict


# finding next job title

def next_jobtitle(profile):
    recent_job = []
    for k, val in profile.items():
        if k == 'careerjunction_za_future_jobtitles':
            recent_job.append(val)
        elif k == '':
            return "no record"
    return recent_job


def current_jobtitle(profile):
    recent_job = []
    for k, val in profile.items():
        if k == 'careerjunction_za_primary_jobtitle':
            recent_job.append(val)
        elif k == '':
            return "no record"
    return recent_job


def course(profile):
    recent_job = []
    for k, val in profile.items():
        if k == 'careerjunction_za_courses':
            recent_job.append(val)
        elif k == '':
            return "no course record"
    return recent_job


# Compare first profile against second profile
# Using the profile ID to check if profile dictionary is 100% identical
def compare_profile(profile_id, other_profiles):
    # We exempt this in the dictionary
    def compare(data_a, data_b):
        if (type(data_a) is dict):
            # is [data_b] a dictionary?
            if (type(data_b) != dict):
                return False
            # iterate over dictionary keys
            for dict_key, dict_value in data_a.items():
                # check if key exists in [data_b] dictionary, and same value?
                if ((dict_key not in data_b) or (not compare(dict_value, data_b[dict_key]))):
                    return False
            # dictionary identical
            return True
        # simple value - compare both value and type for equality
        return ((data_a == data_b) and (type(data_a) is type(data_b)))

    # compare a to b, then b to a
    return (compare(profile_id, other_profiles) and compare(other_profiles, profile_id))


def finding_similar(profile_id, profiles):
    result = []
    for profile in profiles:
        bool(compare_profile(profile_id, profiles))
        if True:
            result.append(profiles["id"])
        else:
            return "cannot be found"
    return result


# find similar skills in candidate profiles
def skill_similar(selected_row1, selected_row2):
    get_similar = []
    get_not_similar = []
    cnt = 0
    for i in selected_row1:
        if i in selected_row2:
            get_similar.append(i)
            cnt = +1
        elif i not in selected_row2:
            get_not_similar.append(i)
            cnt = +1
        else:
            return
    return get_similar, get_not_similar


# Comparing list in the row of each column
def compare_listcomp(row_x, row_y):
    print ([i for i, j in zip(row_x, row_y) if i == j])
#print compare_listcomp(selected_row[3]['careerjunction_za_recent_jobtitles'], selected_row[7]['careerjunction_za_recent_jobtitles'])


# print compare_listcomp(selected_row[3]['careerjunction_za_recent_jobtitles'], selected_row[7]['careerjunction_za_recent_jobtitles'])


# find skil or course intersection
def compare_intersect(row_x, row_y):
    return frozenset(row_x).intersection(row_y)


# print compare_intersect(selected_row[3]['careerjunction_za_skills'], selected_row[7]['careerjunction_za_skills'])

# Check if profile are not the same and the merge profile.
def dict_diff(d1, d2, NO_KEY=''):
    set_d1 = set(d1.keys())
    set_d2 = set(d2.keys())
    both = set_d1 & set_d2
    diff = {k: (d1[k], d2[k]) for k in both if d1[k] != d2[k]}
    diff.update({k: (d1[k], NO_KEY) for k in set_d1 - both})
    diff.update({k: (NO_KEY, d2[k]) for k in set_d2 - both})
    return diff


print (jaccard_similarity([0,1,2,5,6],[0,2,3,5,7,9]))
print("\n")
print('Job seekers profile is not 100% identical: {0}'.format(compare_profile(profiles[1],profiles[2])))
print ('\n')
print ("His/her currnet job title:", current_jobtitle(profiles[9]))
print ('\n')
job_seeker_intersect = DictionaryIntersection(profiles[get_profile__id(9)],profiles[get_profile__id(3)])
jobseeker = job_seeker_intersect['careerjunction_za_recent_jobtitles']
print ("We see that profile id {} is".format(get_profile__id(9)), similar(profiles[get_profile__id(3)],profiles[get_profile__id(3)]),"to profile {}".format(get_profile__id(9)),"jobseeker.")
print ("Since there is something in common between this profile. The recommender suggests that the next job title is either", next_jobtitle(profiles[get_profile__id(9)]),". Hence, the profile is recommend to him(or her).")
print ('\n')
print ("His/Her next job title can be:", next_jobtitle(profiles[get_profile__id(9)]))
print ('\n')
print ("His/Her skill set will include:", skill_similar(selected_row[9]['careerjunction_za_skills'],selected_row[3]['careerjunction_za_skills']))
print ('\n')
print ("His/Her current courses include:", course(profiles[get_profile__id(9)]))


#print "Combine profile:", dict_diff(profiles[3], profiles[7], NO_KEY='Profile ID not found')

def extract_recentjob(dict_1, dict_2):
    extract = []
    for i, v in dict_1.iteritems():

        vals = []
        if isinstance(v, list):
            for i in v:
                if i in dict_2 and i == 'careerjunction_za_recent_jobtitles':
                    vals.append(dict_2.get(i))
                else:
                    vals.append(dict_2.get(v))

    return vals

# extract_recentjob(profiles[3],profiles[7])

def next_jobtile(profile):
    for k, val in profile.iteritems():
        for i in "x_keys":
            if i == "careerjunction_za_recent_jobtitles":
                print ("")
                return i
            if i == 'careerjunction_za_future_jobtitles':
                print ("Your next job are:", i)
            if i == 'careerjunction_za_skills':
                return i
            else:
                print("No profile")
                #recent_job.append(val)
    #return recent_job
next_jobtitle(profiles[1])

def next_jobtitle(profile):
    next_job = []
    for k, val in profile.items():
        if k == 'careerjunction_za_future_jobtitles':
            print (k)
            next_job.append(val)
        else:
            return "No profile"
    return "Your next job are:", next_job
next_jobtitle(profiles[1])


def intersect_dict(dict_a,dict_b):
    keys_a = set(dict_a.keys())
    keys_b = set(dict_b.keys())
    intersection = keys_a & keys_b # '&' operator is used for set intersection
    return intersection

