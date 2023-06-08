#!/usr/bin/env python3

# Author:      Abdou Rockikz
# Description: Python script for scanning a URL for XSS vulnerabilities.
# Date:        2023-06-08
# Modified by: [Your Name]

# Import libraries
import requests  # Library for making HTTP requests
from pprint import pprint  # Library for pretty-printing data structures
from bs4 import BeautifulSoup as bs  # Library for parsing HTML content
from urllib.parse import urljoin  # Library for constructing absolute URLs

# Declare functions

def get_all_forms(url):
    # Retrieve the HTML content of the specified URL and parse it with BeautifulSoup
    soup = bs(requests.get(url).content, "html.parser")
    # Find all the <form> elements in the HTML and return them as a list
    return soup.find_all("form")

def get_form_details(form):
    details = {}
    # Get the value of the "action" attribute of the form element and convert it to lowercase
    action = form.attrs.get("action").lower()
    # Get the value of the "method" attribute of the form element and convert it to lowercase,
    # defaulting to "get" if the attribute is not specified
    method = form.attrs.get("method", "get").lower()
    inputs = []
    # Iterate over all <input> elements within the form
    for input_tag in form.find_all("input"):
        # Get the value of the "type" attribute of the input element, defaulting to "text" if not specified
        input_type = input_tag.attrs.get("type", "text")
        # Get the value of the "name" attribute of the input element
        input_name = input_tag.attrs.get("name")
        # Append a dictionary containing the input type and name to the "inputs" list
        inputs.append({"type": input_type, "name": input_name})
    # Store the form details in a dictionary
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details

def submit_form(form_details, url, value):
    # Construct the target URL by joining the base URL and the form's action URL
    target_url = urljoin(url, form_details["action"])
    inputs = form_details["inputs"]
    data = {}
    # Process each input in the form
    for input in inputs:
        # If the input type is "text" or "search", set the input value to the specified value
        if input["type"] == "text" or input["type"] == "search":
            input["value"] = value
        # Get the input name and value
        input_name = input.get("name")
        input_value = input.get("value")
        # If the input has a name and a value, add it to the data dictionary
        if input_name and input_value:
            data[input_name] = input_value

    # Make an HTTP request to the target URL using either POST or GET method based on the form's method attribute
    if form_details["method"] == "post":
        return requests.post(target_url, data=data)
    else:
        return requests.get(target_url, params=data)

def scan_xss(url):
    # Get all the forms present on the specified URL
    forms = get_all_forms(url)
    # Print the number of detected forms
    print(f"[+] Detected {len(forms)} forms on {url}.")
    # Define the JavaScript code that will cause an XSS vulnerability (alert prompt with some text)
    js_script = '<
