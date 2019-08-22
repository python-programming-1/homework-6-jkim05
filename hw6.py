#!/usr/bin/env python
# coding: utf-8

# In[7]:


import nbconvert

import csv
import pprint


def get_video_data():
    """this function reads from a .csv file and converts the data into a list of dictionaries.
     each item in the list is a dictionary of a specific videos and their attributes."""

    vid_data = []
    with open('USvideos.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            if len(row) == 16:
                vid_dict = {'video_id': row[0],
                            'trending_date': row[1],
                            'title': row[2],
                            'channel_title': row[3],
                            'category_id': row[4],
                            'publish_times': row[5],
                            'tags': row[6],
                            'views': row[7],
                            'likes': row[8],
                            'dislikes': row[9],
                            'comment_count': row[10],
                            'thumbnail_link': row[11],
                            'comments_disabled': row[12],
                            'ratings_disabled': row[13],
                            'video_error': row[14],
                            'description': row[15]
                            }
                vid_data.append(vid_dict)
    return vid_data


def print_data(data):
    for entry in data:
        pprint.pprint(entry)

#################################### Homework Part Starts Here ########################################

# Note to Stefan

'''

Note 1: offset .csv file

the .csv file i'm reading, for some reason, is getting messed up slightly.
when i open the .csv file with a .csv reader in Jupyter, 
some rows are getting offset. for example, in the third row of data, 
the title "Racist Superman | Rudy Mancuso, King Bach, & Lele Pons"
gets split up at "Racist Superman | Rudy Mancuso".
the second half of the title "King Bach, & Lele Pons" then gets shifted one cell over to the right,
and becomes the channel_title.

the actual channel_title "Rudy Mancuso" then becomes the category_id, 
then the actual category_id shifts right one cell to become the publish_time...

due to this, i get an ValueError error in the for loop, 
because the loop can't += the views since some rows are returning a string, 
and not an integer value.

so i added in a try/except to just pass over those instances.

but while the my_max functions are working properly, 
the my_min function is getting stuck because the rows with the offset data essentially have 0 views, 
and is preventing me from seeing the actual correct least_popular_channel.

i think the code should be correct, and should be getting the proper answers 
if it read an unbroken .csv file.

just wanted to note that, please test my hw with a good .csv file.

'''


def my_max(dictionary):
    return_dict = {'views': 0, 'channel': None}

    for k,v in dictionary.items():
        if int(v) > return_dict['views']:
            return_dict['channel'] = k
            return_dict['views'] = int(v)
    return return_dict

def my_min(dictionary):
    return_dict = {'views': float('Inf'), 'channel': None}
    for k,v in dictionary.items():
        if k == 'Unspecified':
            continue
        if int(v) < return_dict['views']:
            return_dict['channel'] = k
            return_dict['views'] = int(v)
    return return_dict
    
def get_most_popular_and_least_popular_channel(data):
    """ fill in the Nones for the dictionary below using the vid data """
    most_popular_and_least_popular_channel = {'most_popular_channel': None, 'least_popular_channel': None, 'most_pop_num_views': None,
                                              'least_pop_num_views': None}
    channel_views_dictionary = {}
    
    for item in data[1:]:
        try:
            channel_views_dictionary.setdefault(item['channel_title'], 0)
            channel_views_dictionary[item['channel_title']] += int(item['views'])
        except:
            pass

    most_views_channel = my_max(channel_views_dictionary)
    least_views_channel = my_min(channel_views_dictionary)

    most_popular_and_least_popular_channel['most_popular_channel'] = most_views_channel['channel']
    most_popular_and_least_popular_channel['most_pop_num_views'] = most_views_channel['views']
    most_popular_and_least_popular_channel['least_popular_channel'] = least_views_channel['channel']
    most_popular_and_least_popular_channel['least_pop_num_views'] = least_views_channel['views']
    
    return most_popular_and_least_popular_channel
    
def get_most_liked_and_disliked_channel(data):
    """ fill in the Nones for the dictionary below using the bar party data """
    most_liked_and_disliked_channel = {'most_liked_channel': None, 'num_likes': None, 'most_disliked_channel': None, 'num_dislikes': None}

    channel_likes_dictionary = {}
    channel_dislikes_dictionary = {}
    
    for item in data[1:]:
        try:
            channel_likes_dictionary.setdefault(item['channel_title'], 0)
            channel_likes_dictionary[item['channel_title']] += int(item['likes'])
        except:
            pass
        
    for item in data[1:]:
        try:
            channel_dislikes_dictionary.setdefault(item['channel_title'], 0)
            channel_dislikes_dictionary[item['channel_title']] += int(item['dislikes'])
        except:
            pass

    most_upvoted_channel = my_max(channel_likes_dictionary)
    most_downvoted_channel = my_max(channel_dislikes_dictionary)
    
    most_liked_and_disliked_channel['most_liked_channel'] = most_upvoted_channel['channel']
    most_liked_and_disliked_channel['num_likes'] = most_upvoted_channel['views']
    most_liked_and_disliked_channel['most_disliked_channel'] = most_downvoted_channel['channel']
    most_liked_and_disliked_channel['num_dislikes'] = most_downvoted_channel['views']
                                                                                
    return most_liked_and_disliked_channel

##################################### Homework Part Ends Here #########################################

if __name__ == '__main__':
    vid_data = get_video_data()

    # uncomment the line below to see what the data looks like
    # print_data(vid_data)

    popularity_metrics = get_most_popular_and_least_popular_channel(vid_data)

    like_dislike_metrics = get_most_liked_and_disliked_channel(vid_data)

    print('Popularity Metrics: {}'.format(popularity_metrics))
    print('Like Dislike Metrics: {}'.format(like_dislike_metrics))


# In[ ]:




