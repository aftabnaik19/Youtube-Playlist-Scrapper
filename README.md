
**YouTube Playlist to Excel Exporter**

This Python project is a simple yet powerful tool for extracting video titles and links from a YouTube playlist and exporting them to an Excel spreadsheet. It's a handy utility for content creators, researchers, and anyone who wants to organize and analyze YouTube playlists more efficiently.

**Features:**

- Utilizes popular Python libraries such as BeautifulSoup (bs4), PyTube, Pandas, and Requests.
- Accepts a YouTube playlist link as input.
- Scrapes video titles and video links from the provided playlist.
- Exports the collected data to an Excel spreadsheet in the same folder as the script.

**Usage:**

1. Clone or download this repository.
2. Install the required libraries if you haven't already (`bs4`, `pytube`, `pandas`, `requests`).
3. Run the Python script, providing a YouTube playlist link as an argument.
4. The script will scrape the playlist and create an Excel file in the same directory with the collected data.

**Dependencies:**

- BeautifulSoup (bs4)
- PyTube
- Pandas
- Requests

**Installation:**

You can install the required libraries using pip:

```bash
pip install beautifulsoup4 pytube pandas requests
```

**Usage Example:**

```bash
python scrapper.py "https://www.youtube.com/playlist?list=YOUR_PLAYLIST_ID"
```

Replace `"https://www.youtube.com/playlist?list=YOUR_PLAYLIST_ID"` with the actual YouTube playlist link you want to process.

**Contributing:**

Contributions and suggestions are welcome! Feel free to open issues and submit pull requests to improve this project.

---

Feel free to customize this description to your liking and provide additional details as needed.
