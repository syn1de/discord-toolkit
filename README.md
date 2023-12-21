
# Discord Toolkit 🛠️

![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)

## Overview

This toolkit includes two Python scripts:
- [Discord Ripper](#discord-ripper-)
- [Discord Downloader](#discord-downloader-)

## Discord Ripper 🚀

Discord Ripper is a Python script that allows you to collect links (attachments, images, and videos) from a specified Discord channel. The script interacts with the Discord API to fetch messages and extract links from them.

### 📋 Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

### 🚀 Getting Started

#### Prerequisites

- Python 3.x
- pip (Python package installer)

#### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/syn1de/discord-toolkit

2. Navigate to the project directory:

   ```bash
   cd discord-toolkit
   ```

### 🎮 Usage

1. **Discord Ripper:**
   - Double-click the Python file or run it through the terminal.

     ```bash
       discord_ripper.py
     ```

   - Enter your Discord token when prompted.
   - Enter the Discord channel ID from which you want to collect links.
   - The script will fetch messages from the specified channel and save the links to a text file (`channel_id_links.txt`).

2. **Discord Downloader:**
   - Double-click the Python file or run it through the terminal.

     ```bash
      discord_downloader.py
     ```

   - Enter the path to the text file containing the list of URLs when prompted.
   - Enter the path to the output folder where the downloaded files will be saved.
   - The script will download the files and display a progress bar for each download.

### 🤝 Contributing

Contributions are welcome! Feel free to open issues and pull requests.

### 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### 🙏 Acknowledgments

- Special thanks to the [Discord API](https://discord.com/developers/docs/intro) for providing the platform to interact with Discord servers.
