
# YouTube Batch Audio Extractor 

A robust and lightweight automation script to batch download YouTube videos and convert them directly to MP3 format. Built specifically to streamline audio data collection for AI pipelines and personal utility.

# Features
- **Batch Processing:** Reads multiple YouTube URLs from a text file (`list.txt`) and downloads them sequentially.
- **High-Quality Audio:** Automatically extracts the best audio quality and converts it to MP3 (VBR 0).
- **Standalone Capability:** Can be compiled into a single `.exe` file for use on machines without Python installed.
- **Smart Pathing:** Dynamically resolves file paths, preventing "file not found" errors whether run as a script or an executable.

- 
# Prerequisites
Before running the script, ensure you have the following installed:
1. **Python 3.x**
2. **FFmpeg:** Required for audio conversion. 
   - Download `ffmpeg.exe` and place it in the same directory as the script.

# Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/residue43/mp3downloader.git
   cd mp3downloader
