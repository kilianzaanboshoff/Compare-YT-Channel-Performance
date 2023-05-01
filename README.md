# Compare-YT-Channel-Performance

This code creates a Streamlit app that retrieves and visualizes YouTube channel metrics for a specified time range using the YouTube Data API. The app allows users to enter their YouTube Data API key, a comma-separated list of channel IDs, select a start and end date, and click the "Get data" button to retrieve and visualize the data.

The get_youtube_data() function calls the YouTube Data API to retrieve the video IDs and view counts for each video uploaded by the specified channels during the selected time range. It also calls the API to retrieve the channel name for each channel ID provided. The function returns two lists: views containing the total number of views for each channel, and labels containing the corresponding channel names.

The app displays an image and a disclaimer using the st.image() and st.expander() functions, respectively. The st.title() function sets the title of the app. The user enters their API key and channel IDs using the st.text_input() function. The st.date_input() function allows the user to select the start and end date for the data retrieval.

When the user clicks the "Get data" button, the get_youtube_data() function is called, and the returned data is sorted and plotted using the st.bar_chart() function. The millions() function is defined to format the y-axis of the chart to display the view counts in millions.

Overall, this code provides a simple and user-friendly way to retrieve and visualize YouTube channel metrics for a specified time range.
