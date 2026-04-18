import os
import re
import socket
import time
from imap_tools import MailBox, AND

# --- CONFIGURATION ---
USERNAME = 'something@yahoo.com'
PASSWORD = 'something' 
IMAP_SERVER = 'imap.mail.yahoo.com'
DOWNLOAD_FOLDER = r'D:\Ma Yahoo Mail\Has attachments'
TARGET_FOLDER = 'Has attachments' 

def clean_filename(filename):
    filename = re.sub(r'[\r\n\t]+', ' ', filename)
    filename = re.sub(r'[<>:"/\\|?*]', '_', filename)
    return filename.strip()

def download_attachments():
    if not os.path.exists(DOWNLOAD_FOLDER):
        os.makedirs(DOWNLOAD_FOLDER)

    socket.setdefaulttimeout(120) 
    download_count = 0
    total_found = 0
    
    try:
        print(f"\nConnecting to Yahoo...")
        with MailBox(IMAP_SERVER).login(USERNAME, PASSWORD) as mailbox:
            
            print(f"Opening folder: '{TARGET_FOLDER}'...")
            mailbox.folder.set(TARGET_FOLDER)
            
            # REMOVED size_gt filter to find ALL attachments
            print(f"Scanning for ALL files in '{TARGET_FOLDER}'...")

            for msg in mailbox.fetch():
                for att in msg.attachments:
                    total_found += 1
                    safe_name = clean_filename(att.filename)
                    size_mb = round(att.size / (1024 * 1024), 2)
                    
                    file_path = os.path.join(DOWNLOAD_FOLDER, safe_name)
                    
                    # If file already exists, we don't need to download it again
                    if os.path.exists(file_path):
                        print(f"  - Found: {safe_name} ({size_mb} MB) [Already on D: Drive]")
                        continue

                    print(f"  [{download_count + 1}] Saving: {safe_name} ({size_mb} MB) from {msg.from_}")
                    
                    try:
                        with open(file_path, 'wb') as f:
                            f.write(att.payload)
                        download_count += 1
                    except Exception as e:
                        print(f"  ! Error saving {safe_name}: {e}")
            
            print(f"\n--- SCAN COMPLETE ---")
            print(f"Total attachments detected: {total_found}")
            print(f"New files saved to D: drive: {download_count}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    download_attachments()