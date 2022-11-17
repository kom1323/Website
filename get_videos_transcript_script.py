
from youtube_transcript_api import YouTubeTranscriptApi
import urllib.request
import json
from config import api_key


# destiny_channel_id = "UC554eY5jNUfDq3yDOJYirOQ"


# def get_all_video_in_channel(channel_id):

#     base_video_url = 'https://www.youtube.com/watch?v='
#     base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

#     first_url = base_search_url+'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(api_key, channel_id)

#     video_links = []
#     url = first_url
#     while True:
#         inp = urllib.request.urlopen(url)
#         resp = json.load(inp)

#         for i in resp['items']:
#             if i['id']['kind'] == "youtube#video":
#                 video_links.append(i['id']['videoId'])

#         try:
#             next_page_token = resp['nextPageToken']
#             url = first_url + '&pageToken={}'.format(next_page_token)
#         except:
#             break
#     return video_links



# lst = get_all_video_in_channel(destiny_channel_id)

# with open("videos_id.txt", "w") as f:
    
#     for i in lst:
#         f.write("{}\n".format(i))




# assigning srt variable with the list of dictonaries
# obtained by the .get_transcript() function
# and this time it gets only the subtitles that
# are of english langauge.

with open("videos_id.txt", "r") as f:
    lst = f.read().splitlines()

# print(lst)


#for i in lst:

    #try:

srt = YouTubeTranscriptApi.get_transcript(lst[0],
                                    languages=['en'])
print("----------------------------------------------------------")

print(type(srt))
print(srt)
print("----------------------------------------------------------")

    #    with open("videos_data/subtitles{}.txt".format(i), "w") as f:
        
            
    #             # iterating through each element of list srt
    #         for i in srt:
    #             # writing each element of srt on a new line
    #             f.write("{}\n".format(i))
    # except:
    #     pass