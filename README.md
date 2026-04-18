# Yahoo Mail Attachment Downloader

This is a Python script developed to automate the cleanup of a Yahoo Mail inbox. It connects to the email account via IMAP and downloads all attachments from a specified folder directly to a local hard drive. 

## Features
* [cite_start]**Bulk Extraction:** Automatically scans a specific email folder (e.g., 'Has attachments') and extracts all attached files[cite: 2, 3].
* [cite_start]**Smart Downloading:** Checks if a file already exists on the local drive before downloading to prevent duplicates and save time[cite: 5].
* [cite_start]**Safe Filenames:** Automatically cleans attachment filenames by removing special characters (`< > : " / \ | ? *`) that could cause operating system errors[cite: 3].
* [cite_start]**Progress Tracking:** Prints real-time console updates showing the filename, file size in MB, and the sender's email address[cite: 4, 6].

## Prerequisites
You will need to install the following Python library to handle the IMAP connection:
`pip install imap-tools`

## Configuration
Before running the script, update the `USERNAME` and `PASSWORD` variables with your Yahoo Mail credentials. You may need to generate an "App Password" in your Yahoo account security settings if you have Two-Factor Authentication enabled.

[cite_start]Update the `DOWNLOAD_FOLDER` variable to set your preferred local destination path[cite: 1].

## Disclaimer
Be careful when downloading bulk attachments from the internet. Ensure you trust the senders to avoid saving malicious files to your local drive.
```
