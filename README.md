# MyBigNumber API using Flask

To use an API for the `sum` function in Python using Flask. Below is an example of how you can do this:

## Installation

First, install Flask using pip:

```bash
pip install flask
```

## Running the Application

Run the application by executing:
```bash
python app.py
```

The application will run on http://127.0.0.1:5000/. Now you can send a POST request to /sum to receive the result and operation history.

### Example POST request using CURL:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"str1": "1234", "str2": "897"}' http://127.0.0.1:5000/sum
```





