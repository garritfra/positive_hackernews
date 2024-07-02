# Positive Hacker News RSS Feed

Enjoy a more positive news-reading experience with the Positive Hacker News RSS Feed! 🌟

A writeup of this project can be found [here](https://garrit.xyz/posts/2023-11-24-positive-hackernews).

## Overview

In a world where tech news can often be overwhelmingly negative, this RSS feed serves as a breath of fresh air. It selectively presents stories that have a positive sentiment, making your news-reading experience more enjoyable and less stressful.

This project provides a unique RSS feed for Hacker News, focusing exclusively on positive news. By utilizing sentiment analysis, this feed filters out negative stories, offering a curated selection of content that is more uplifting and encouraging compared to the standard Hacker News feed.

## Comparison

Here's an example of the HackerNews feed provided by [hnrss.github.io](https://hnrss.github.io/):

![Before](/assets/feed_regular.png)

And here's the filtered, positive-only feed:

![After](/assets/feed_positive.png)

## How to subscribe

The feed is updated regularly and deployed via GitHub pages. Simply add this link to your RSS reader of choice:

https://garritfra.github.io/positive_hackernews/feed.xml

## Setup Instructions

### Prerequisites
- Python 3.8 or above
- `pip` for Python package management
- `nltk` for Natural Language Processing

### Local Setup

1. **Clone the Repository**
   - Clone this repository to your local machine using `git clone <repository-url>`.

2. **Install Dependencies**
   - Navigate to the project directory and install the required Python packages:
     ```bash
     pip install -r requirements.txt
     ```

3. **Run the Script**
   - Execute the main script to generate a new RSS feed:
     ```bash
     python main.py
     ```

## Contributing

Feel free to contribute to this project! Whether it's by suggesting features, improving the sentiment analysis, or enhancing the RSS feed format, your input is always welcome.

## License

[MIT](./LICENSE)
