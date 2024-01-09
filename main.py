import requests
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import xml.etree.ElementTree as ET
import xml.dom.minidom
from datetime import datetime
from email import utils


nltk.download('vader_lexicon')

def fetch_top_stories():
    print("Fetching hacker news frontpage...")
    response = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json')
    top_stories_ids = response.json()
    top_stories = []
    
    for story_id in top_stories_ids[:30]:  # Fetch details of top 30 stories for example
        print("Fetching story:", story_id)
        story_response = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{story_id}.json')
        story_data = story_response.json()
        top_stories.append(story_data)

    return top_stories

def analyze_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    sentiment = sia.polarity_scores(text)
    return sentiment['compound']  # Return the compound score

def filter_positive_stories(stories):
    positive_stories = []
    negative_stories = []

    for story in stories:
        id = story.get('id', '')
        title = story.get('title', '')
        text = story.get('text', '')

        print(f"Analyzing story: {id} ({title})")

        # Check sentiment of title and text (if available)
        title_sentiment = analyze_sentiment(title)
        text_sentiment = analyze_sentiment(text) if text else 0

        # Consider a story positive if either title or text is positive
        if title_sentiment >= 0 and text_sentiment >= 0:
            print(f"Result: {id} is positive. ({title})")
            positive_stories.append(story)
        else:
            print(f"Result: {id} is negative. ({title})")
            negative_stories.append(story)

    return {
        "positive": positive_stories,
        "negative": negative_stories
    }

def format_rfc2822(timestamp):
    """ Converts Unix timestamp to an RFC 2822 formatted string """
    dt = datetime.fromtimestamp(timestamp)
    return utils.format_datetime(dt)

def create_rss_feed(positive_stories):
    """ Creates an RSS feed from the list of positive stories """
    rss = ET.Element("rss", version="2.0")
    channel = ET.SubElement(rss, "channel")

    ET.SubElement(channel, "title").text = "Positive HackerNews"
    ET.SubElement(channel, "description").text = "The Positive Hacker News RSS Feed"
    ET.SubElement(channel, "language").text = "en"
    ET.SubElement(channel, "link").text = "https://garritfra.github.io/positive_hackernews/feed.xml"
    ET.SubElement(channel, "lastBuildDate").text = utils.format_datetime(datetime.now())

    for story in positive_stories:
        item = ET.SubElement(channel, "item")
        ET.SubElement(item, "title").text = story.get('title', 'No Title')
        ET.SubElement(item, "link").text = story.get('url', f"https://news.ycombinator.com/item?id={story.get('id')}")
        ET.SubElement(item, "description").text = story.get('text', 'No Text')
        ET.SubElement(item, "guid").text = str(story.get('id', 'No ID'))
        ET.SubElement(item, "comments").text = f"https://news.ycombinator.com/item?id={str(story.get('id', 'No ID'))}"
        ET.SubElement(item, "pubDate").text = format_rfc2822(story.get('time', 0))

    # Convert to a string
    rough_string = ET.tostring(rss, encoding='unicode')

    # Pretty Print
    reparsed = xml.dom.minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

def write_to_file(string, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(string)

def main():
    top_stories = fetch_top_stories()
    analyzed_stories = filter_positive_stories(top_stories)

    rss_feed = create_rss_feed(analyzed_stories["positive"])
    filename = "feed.xml"
    write_to_file(rss_feed, filename)

    print(f"RSS feed written to file: {filename}")




if __name__ == "__main__":
    main()