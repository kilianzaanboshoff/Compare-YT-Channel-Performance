import streamlit as st
import googleapiclient.discovery
import datetime
import dateutil.relativedelta

# Add image and disclaimer
st.image('file path here')
with st.expander('ℹ️ How it works'):
    st.write('This app allows you to retrieve YouTube channel metrics (views, subscribers, and likes) for a specified time range. Enter your YouTube Data API key and a comma-separated list of channel IDs, select a start and end date, and click the "Get data" button to retrieve and visualize the data.')


def millions(x, pos):
    'The two args are the value and tick position'
    return '%1.1fM' % (x * 1e-6)


def get_youtube_data(api_key, channel_ids, start_date, end_date):
    # Create a YouTube Data API client
    youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=api_key)

    # Split the comma-separated list of channel IDs into a list
    channel_id_list = channel_ids.split(',')

    # Create empty lists to store data for the chart
    views = []
    labels = []

    for channel_id in channel_id_list:
        # Call the search().list method to retrieve the videos uploaded in the specified time range
        video_response = youtube.search().list(
            part='id',
            channelId=channel_id,
            publishedAfter=start_date + 'T00:00:00Z',
            publishedBefore=end_date + 'T23:59:59Z',
            type='video',
            maxResults=150,  # You can adjust this value to retrieve more or fewer videos
        ).execute()

        # Extract the video IDs from the response
        video_ids = [item['id']['videoId'] for item in video_response['items']]

        # Call the videos().list method to retrieve the view counts for the videos
        view_response = youtube.videos().list(
            part='statistics',
            id=','.join(video_ids),
        ).execute()

        # Extract the view counts from the response and sum them up
        view_count = sum(int(item['statistics']['viewCount']) for item in view_response['items'])

        # Call the channels().list method to retrieve the channel name
        channel_response = youtube.channels().list(
            part='snippet',
            id=channel_id,
        ).execute()

        # Extract the channel name from the response
        channel_name = channel_response['items'][0]['snippet']['title']

        # Append the data to the lists
        labels.append(channel_name)
        views.append(view_count)

    # Sort the data by views in descending order
    views, labels = zip(*sorted(zip(views, labels), reverse=True))

    return views, labels


st.title('Comparing YouTube Channel Metrics')

# Replace YOUR_API_KEY with your actual API key
api_key = st.text_input('Enter your YouTube Data API key', type='password')

# Replace CHANNEL_IDS with a comma-separated list of channel IDs
channel_ids = st.text_input('Enter comma-separated YouTube channel IDs')
import streamlit as st
import googleapiclient.discovery
import datetime
import dateutil.relativedelta

# Add image and disclaimer
st.image('/Users/kilianboshoff/Pictures/banter.jpg')
with st.expander('ℹ️ How it works'):
    st.write('This app allows you to retrieve YouTube channel metrics (views, subscribers, and likes) for a specified time range. Enter your YouTube Data API key and a comma-separated list of channel IDs, select a start and end date, and click the "Get data" button to retrieve and visualize the data.')


def millions(x, pos):
    'The two args are the value and tick position'
    return '%1.1fM' % (x * 1e-6)


def get_youtube_data(api_key, channel_ids, start_date, end_date):
    # Create a YouTube Data API client
    youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=api_key)

    # Split the comma-separated list of channel IDs into a list
    channel_id_list = channel_ids.split(',')

    # Create empty lists to store data for the chart
    views = []
    labels = []

    for channel_id in channel_id_list:
        # Call the search().list method to retrieve the videos uploaded in the specified time range
        video_response = youtube.search().list(
            part='id',
            channelId=channel_id,
            publishedAfter=start_date + 'T00:00:00Z',
            publishedBefore=end_date + 'T23:59:59Z',
            type='video',
            maxResults=150,  # You can adjust this value to retrieve more or fewer videos
        ).execute()

        # Extract the video IDs from the response
        video_ids = [item['id']['videoId'] for item in video_response['items']]

        # Call the videos().list method to retrieve the view counts for the videos
        view_response = youtube.videos().list(
            part='statistics',
            id=','.join(video_ids),
        ).execute()

        # Extract the view counts from the response and sum them up
        view_count = sum(int(item['statistics']['viewCount']) for item in view_response['items'])

        # Call the channels().list method to retrieve the channel name
        channel_response = youtube.channels().list(
            part='snippet',
            id=channel_id,
        ).execute()

        # Extract the channel name from the response
        channel_name = channel_response['items'][0]['snippet']['title']

        # Append the data to the lists
        labels.append(channel_name)
        views.append(view_count)

    # Sort the data by views in descending order
    views, labels = zip(*sorted(zip(views, labels), reverse=True))

    return views, labels


st.title('Comparing YouTube Channel Metrics')

# Replace YOUR_API_KEY with your actual API key
api_key = st.text_input('Enter your YouTube Data API key', type='password')

# Replace CHANNEL_IDS with a comma-separated list of channel IDs
channel_ids = st.text_input('Enter comma-separated YouTube channel IDs')

# Allow the user to select the start and end date
end_date = st.date_input('End date', datetime.date.today())
start_date = st.date_input('Start date', end_date - dateutil.relativedelta.relativedelta(months=1))

# Convert the start and end dates to strings
start_date_str = start_date.strftime('%Y-%m-%d')
end_date_str = end_date.strftime('%Y-%m-%d')



# Call the function to retrieve data from the YouTube API
if st.button('Get data'):
    views, labels = get_youtube_data(api_key, channel_ids, start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d'))

    # Sort the views and labels lists by views in descending order
    sorted_views_labels = sorted(zip(views, labels), reverse=True)

    # Create a dictionary of the sorted data for the bar chart
    chart_data = {label: view for view, label in sorted_views_labels}
    st.bar_chart(chart_data)


# Allow the user to select the start and end date
end_date = st.date_input('End date', datetime.date.today())
start_date = st.date_input('Start date', end_date - dateutil.relativedelta.relativedelta(months=1))

# Convert the start and end dates to strings
start_date_str = start_date.strftime('%Y-%m-%d')
end_date_str = end_date.strftime('%Y-%m-%d')



# Call the function to retrieve data from the YouTube API
if st.button('Get data'):
    views, labels = get_youtube_data(api_key, channel_ids, start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d'))

    # Sort the views and labels lists by views in descending order
    sorted_views_labels = sorted(zip(views, labels), reverse=True)

    # Create a dictionary of the sorted data for the bar chart
    chart_data = {label: view for view, label in sorted_views_labels}
    st.bar_chart(chart_data)

