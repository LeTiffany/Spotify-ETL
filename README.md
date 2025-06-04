# Song Popularity and Music Metrics

![Image](https://github.com/user-attachments/assets/c676e307-c59b-4def-b58f-42de03fec705)

Data is extracted from Spotify using the Spotify API and from the Million Song Subset from the Million Song Database. Methods from the Spotipy package are used for data exchange with the Spotify database in extracting top song data in JSON format. The Million Song Subset is downloaded from GitHub as a CSV file and imported into a Google Sheets document where it can be read from a Jupyter Notebook.

The Million Song Database includes data from Echo Nest on the most popular contemporary songs including technical data on musical measures and metrics of individual songs. The Spotify database includes data for over a hundred million songs on the platform including categorical data on the identifying information of songs and quantitative data on the popularity of music. These datasets are joined, creating a dataset that allows for greater insight on music patterns and popularity. The resulting dataframe is normalized and aggregated to reduce redundancy, group related columns and rollup data into a more usable format. This dataset is pushed to an AWS SQL database where it may be interacted with through a Streamlit dashboard.

[![Top Songs: Rolled Up and Wrapped!](https://ytcards.demolab.com/?id=8XV-8EQ7HhI&title=Top+Songs:+Rolled+Up+and+Wrapped!&lang=en&timestamp=1733616000&background_color=%230d1117&title_color=%23ffffff&stats_color=%23dedede&max_title_lines=1&width=250&border_radius=5&duration=296 "Top Songs: Rolled Up and Wrapped!")](https://youtu.be/8XV-8EQ7HhI?feature=shared)
