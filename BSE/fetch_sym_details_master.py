#!/usr/bin/env python3
"""
FYERS Symbol Master Downloader
Downloads symbol master JSON files from FYERS public API
"""

import requests
import os
from datetime import datetime
import time

def download_file(url, filename):
    """Download a file from URL and save it locally"""
    try:
        print(f"Downloading {filename}...")
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        
        with open(filename, 'wb') as file:
            file.write(response.content)
        
        file_size = os.path.getsize(filename)
        print(f"[OK] {filename} downloaded successfully ({file_size:,} bytes)")
        return True
        
    except requests.RequestException as e:
        print(f"[ERROR] Failed to download {filename}: {e}")
        return False
    except Exception as e:
        print(f"[ERROR] Error saving {filename}: {e}")
        return False

def main():
    """Main function to download all symbol master JSON files"""
    
    # Symbol master JSON URLs from FYERS
    json_files = {
        'NSE_CD_sym_master.json': 'https://public.fyers.in/sym_details/NSE_CD_sym_master.json',      # NSE Currency Derivatives
        'NSE_FO_sym_master.json': 'https://public.fyers.in/sym_details/NSE_FO_sym_master.json',      # NSE Equity Derivatives
        'NSE_COM_sym_master.json': 'https://public.fyers.in/sym_details/NSE_COM_sym_master.json',    # NSE Commodity
        'NSE_CM_sym_master.json': 'https://public.fyers.in/sym_details/NSE_CM_sym_master.json',      # NSE Capital Market
        'BSE_CM_sym_master.json': 'https://public.fyers.in/sym_details/BSE_CM_sym_master.json',      # BSE Capital Market
        'BSE_FO_sym_master.json': 'https://public.fyers.in/sym_details/BSE_FO_sym_master.json',      # BSE Equity Derivatives
        'MCX_COM_sym_master.json': 'https://public.fyers.in/sym_details/MCX_COM_sym_master.json'     # MCX Commodity
    }
    
    print("=" * 50)
    print("FYERS Symbol Master Downloader")
    print("=" * 50)
    print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    successful_downloads = 0
    total_files = len(json_files)
    
    for filename, url in json_files.items():
        if download_file(url, filename):
            successful_downloads += 1
        # Small delay between downloads to be respectful to the server
        time.sleep(1)
        print()
    
    print("=" * 50)
    print(f"Download Summary:")
    print(f"Successfully downloaded: {successful_downloads}/{total_files} files")
    print(f"Completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 50)
    
    if successful_downloads == total_files:
        print("All JSON files downloaded successfully!")
    else:
        print(f"Warning: {total_files - successful_downloads} files failed to download")
    
    return successful_downloads == total_files

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nDownload interrupted by user")
    except Exception as e:
        print(f"Unexpected error: {e}")