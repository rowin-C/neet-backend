# NEET Counseling Tool Backend 🏫

This is the backend part of the NEET Counseling Tool, built with Python and Flask, and hosted on PythonAnywhere.

# NEET Counseling Tool 🏫

Welcome to the NEET Counseling Tool! This tool helps NEET students figure out which colleges they can get into based on their rank. The idea was inspired by a [Reddit post](https://www.reddit.com/r/indianmedschool/comments/15f1oqz/i_have_created_a_collection_of_college_wise_final/) by [u/CarbonylChloride](https://www.reddit.com/user/CarbonylChloride/) that shared a collection of 400+ colleges with their opening and closing ranks.

## Features

- Scan through 400+ colleges to find eligible ones based on your rank.
- Simple Python script 🐍 scans PDFs for keywords.
- Takes about 3 minutes ⏳ to provide results.

## Features

- Simple Python script 🐍 that scans PDFs for keywords.
- Provides a list of eligible colleges based on NEET rank.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/rowin-C/neet-backend.git
   cd neet-counseling-tool-backend
   ```
1. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

1. **Run the Flask server:**

   ```bash
    flask --app server run
   ```

## Usage

- The backend receives rank and category inputs from the frontend.
- Scans PDFs to find eligible colleges.
- Sends back the list of eligible colleges to the frontend.

## Contributing

Feel free to fork the repository and submit pull requests. Contributions to improve the backend are welcome!

## Feedback

We'd love to hear your feedback! Please share your thoughts and suggestions by creating an issue or contributing directly.
