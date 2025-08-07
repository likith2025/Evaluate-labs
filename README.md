 Task-1 :# Calculator CLI App

A simple command-line interface (CLI) calculator that allows you to perform basic arithmetic operations: addition, subtraction, multiplication, and division.

## Features

- Perform addition, subtraction, multiplication, and division
- Takes user input via terminal/command line
- Continues running until user chooses to exit
- Handles division by zero gracefully
- Easy to use and minimal interface

## Installation

Clone this repository to your local machine:

Task-2 : # Console-Based To-Do List Application

A simple command-line To-Do List app in Python that allows you to add, remove, and view tasks. Tasks are persisted in a text file, so your to-do list is saved between sessions.

Features
Add a task: Add new tasks to your to-do list

Remove a task: Remove existing tasks by task number

View tasks: List all your to-do items with numbering

Persistent storage: All tasks are stored in a text file (tasks.txt) for future use

Task-3 : # News Headlines Web Scraper

This Python project automates the process of collecting top news headlines from a public news website. It uses the `requests` and `BeautifulSoup` libraries to fetch, parse, and save the latest headlines to a text file.

## Features

- Scrapes top news headlines automatically
- Easy customization for any news site (default: BBC News)
- Saves headlines to a `headlines.txt` file for later use

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library

Install dependencies with:

```bash
pip install requests beautifulsoup4
```

## Usage

1. Clone this repository or copy the script.
2. Edit the `url` in the script to your preferred news website (optional).
3. Run the script:

   ```bash
   python script.py
   ```

4. Check the output in the `headlines.txt` file.

## How It Works

- Fetches the HTML content of the specified news website.
- Parses the HTML to extract headlines (by default, from all `` tags).
- Writes each headline to a new line in `headlines.txt`.

## Customization

- Change the `url` variable to scrape a different news website.
- Adjust the HTML tag or class in the script if the site uses tags other than `` for headlines.

## Example Output

```
Top headline one
Top headline two
Top headline three
...
```

## Disclaimer

This scraper is for educational purposes and is intended for use on publicly accessible sites. Respect the target website's `robots.txt` and terms of service.

You can copy and paste this block into your `README.md` file on GitHub. Let me know if you want to customize it further!
