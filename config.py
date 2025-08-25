from typing import List, Dict
import os
from dotenv import load_dotenv


load_dotenv()

# Bot Configuration
BOT_TOKEN = os.getenv("BOT_TOKEN", "8315130283:AAGC68T9jTt9U5eYgG4lbxOPuL2yEGM1VL8")
API_ID = int(os.getenv("API_ID", "26880349"))
API_HASH = os.getenv("API_HASH", "236f4017f1652b0415c63d120b53d544")

OWNER_ID = int(os.getenv("OWNER_ID", "5254302308"))

# Database Configuration
MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://fixmayart834:FMWwXBd4JJYMs2Iv@cluster0.ltpube9.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = os.getenv("DATABASE_NAME", "filestore")

# Channel Configuration 
DB_CHANNEL_ID = int(os.getenv("DB_CHANNEL_ID", "-1002955857749"))
FORCE_SUB_CHANNEL = int(os.getenv("FORCE_SUB_CHANNEL", "0"))  # Can’t be a URL. Use channel ID.
FORCE_SUB_CHANNEL_2 = int(os.getenv("FORCE_SUB_CHANNEL_2", "0"))
FORCE_SUB_CHANNEL_3 = int(os.getenv("FORCE_SUB_CHANNEL_3", "0"))
FORCE_SUB_CHANNEL_4 = int(os.getenv("FORCE_SUB_CHANNEL_4", "0"))

# Channel Links (as string URLs)
CHANNEL_LINK = os.getenv("CHANNEL_LINK", "https://t.me/Heisenberg_Universe")
CHANNEL_LINK_2 = os.getenv("CHANNEL_LINK_2", "https://t.me/HeisenbergBackupZone")
CHANNEL_LINK_3 = os.getenv("CHANNEL_LINK_3", "")
CHANNEL_LINK_4 = os.getenv("CHANNEL_LINK_4", "")

# Start photo
START_PHOTO = os.getenv("START_PHOTO", "https://telegra.ph/Extractor-Bot-08-25")

# Bot Information
BOT_USERNAME = os.getenv("BOT_USERNAME", "@Shin_Chan_Robot")
BOT_NAME = os.getenv("BOT_NAME", "Shinchan")
BOT_VERSION = "2.0"

# Privacy Mode Configuration and auto delete time
PRIVACY_MODE = os.getenv("PRIVACY_MODE", "off").lower() == "on"
AUTO_DELETE_TIME = int(os.getenv("AUTO_DELETE_TIME", "30"))

# Modiji API Key
MODIJI_API_KEY = os.getenv("MODIJI_API_KEY")
if not MODIJI_API_KEY:
    print("⚠️ Warning: MODIJI_API_KEY not set in environment variables")

# Links
DEVELOPER_LINK = os.getenv("DEVELOPER_LINK", "https://t.me/Heisenberg_Universe")
SUPPORT_LINK = os.getenv("SUPPORT_LINK", "https://t.me/HeisenbergBackupZone")

# For Koyeb/Render
WEB_SERVER = os.getenv("WEB_SERVER", "True").lower() == "true"
PING_URL = os.getenv("PING_URL", "")  # Your deploy URL
PING_TIME = int(os.getenv("PING_TIME", "5"))  # Timeout in seconds

# Admin IDs
ADMIN_IDS: List[int] = [
    int(admin_id.strip())
    for admin_id in os.getenv("ADMIN_IDS", "").split()
    if admin_id.strip().isdigit()
]

# File size limit (4GB)
MAX_FILE_SIZE = 4000 * 1024 * 1024
 

# Supported file types and extensions
SUPPORTED_TYPES = [
    "document",
    "video",
    "audio",
    "photo",
    "voice",
    "video_note",
    "animation"
]

SUPPORTED_EXTENSIONS = [
    # Documents
    "pdf", "txt", "doc", "docx", "xls", "xlsx", "ppt", "pptx",
    # Programming Files
    "py", "js", "html", "css", "json", "xml", "yaml", "yml",
    # Archives
    "zip", "rar", "7z", "tar", "gz", "bz2",
    # Media Files
    "mp4", "mp3", "m4a", "wav", "avi", "mkv", "flv", "mov",
    "webm", "3gp", "m4v", "ogg", "opus",
    # Images
    "jpg", "jpeg", "png", "gif", "webp", "bmp", "ico",
    # Applications
    "apk", "exe", "msi", "deb", "rpm",
    # Other
    "txt", "text", "log", "csv", "md", "srt", "sub"
]

SUPPORTED_MIME_TYPES = [
    "application/pdf",
    "application/msword",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    "application/zip",
    "application/x-rar-compressed",
    "application/x-7z-compressed",
    "video/mp4",
    "audio/mpeg",
    "audio/mp4",
    "image/jpeg",
    "image/png",
    "image/gif",
    "application/vnd.android.package-archive",
    "application/x-executable",
]

class Messages:
    START_TEXT = """
🎉 **Welcome to {bot_name}!** 🎉

Hello {user_mention}! I'm your secure file sharing assistant!

📢 Join @Heisenberg_Universe for updates!
👨‍💻 Contact @Heisenbergsells for support

Use /help to see available commands!
"""

    HELP_TEXT = """
📚 **Available Commands**  

👤 **User Commands:**  
• `/start` - Start the bot  
• `/help` - Show this menu  
• `/about` - Bot details  
• `/short [url]` - Shorten a link (e.g., `/short example.com`)  
/repo 

👑 **Admin Commands:**  
• `/upload` - Upload a file (reply to a file)  
• `/stats` - View bot statistics  
• `/bcast` - Send a message to all users  
• `/auto_del` - Set auto-delete timer  


🗑 **Auto-Delete System:**  
• Files auto-delete after a set time.  
• Modify timer using From Repo.  

🔗 **Batch System:**  
• `/batch` - Group multiple files into one link.  
• Forward files & reply with `/batch`.  


🛠 **Open Source:**  
🔗 [GitHub](https://github.com/utkarshdubey2008/alphashare)  

⚠️ **Need Help?** Contact [AlphaBotz](https://t.me/alphabotzchat)  
"""

    ABOUT_TEXT = """
ℹ️ 𝙰𝚋𝚘𝚞𝚝 {bot_name}

𝚅𝚎𝚛𝚜𝚒𝚘𝚗: {version}
𝙳𝚎𝚟𝚎𝚕𝚘𝚙𝚎𝚛: @Heisenbergsells
𝙻𝚊𝚗𝚐𝚞𝚊𝚐𝚎: 𝙿𝚢𝚝𝚑𝚘𝚗
𝙵𝚛𝚊𝚖𝚎𝚠𝚘𝚛𝚔: 𝙿𝚢𝚛𝚘𝚐𝚛𝚊𝚖

📢 𝚄𝚙𝚍𝚊𝚝𝚎𝚜: @Heisenberg_Universe
🛠 𝚂𝚞𝚙𝚙𝚘𝚛𝚝: @HeisenbergBackupZone

use /repo to know more info
"""

    FILE_TEXT = """
📁 **File Details**

**Name:** `{file_name}`
**Size:** {file_size}
**Type:** {file_type}
**Downloads:** {downloads}
**Uploaded:** {upload_time}
**By:** {uploader}

🔗 **Share Link:**
`{share_link}`
"""

    FORCE_SUB_TEXT = """
⚠️ **𝙰𝚌𝚌𝚎𝚜𝚜 𝚁𝚎𝚜𝚝𝚛𝚒𝚌𝚝𝚎𝚍!**

𝙷𝚎𝚢 𝚢𝚘𝚞 𝚌𝚊𝚗'𝚝 𝚊𝚌𝚌𝚎𝚜𝚜 𝚝𝚑𝚒𝚜 𝚏𝚒𝚕𝚎𝚜 𝚞𝚗𝚝𝚒𝚕𝚕 𝚊𝚗𝚍 𝚞𝚗𝚕𝚎𝚜𝚜 𝚢𝚘𝚞 𝚓𝚘𝚒𝚗 𝚝𝚑𝚎 𝚌𝚑𝚊𝚗𝚗𝚎𝚕𝚜 𝚋𝚎𝚕𝚘𝚠 👇 
𝙲𝚕𝚒𝚌𝚔 𝚋𝚞𝚝𝚝𝚘𝚗 𝚋𝚎𝚕𝚘𝚠, 𝚝𝚑𝚎𝚗 𝚝𝚛𝚢 𝚊𝚐𝚊𝚒𝚗!
"""

class Buttons:
    def start_buttons() -> List[List[Dict[str, str]]]:
        return [
            [
                {"text": "Help 📚", "callback_data": "help"},
                {"text": "About ℹ️", "callback_data": "about"}
            ],
            [
                {"text": "Channel 📢", "url": CHANNEL_LINK},
                {"text": "Developer 👨‍💻", "url": DEVELOPER_LINK}
            ]
        ]

    def help_buttons() -> List[List[Dict[str, str]]]:
        return [
            [
                {"text": "Home 🏠", "callback_data": "home"},
                {"text": "About ℹ️", "callback_data": "about"}
            ],
            [
                {"text": "Channel 📢", "url": CHANNEL_LINK}
            ]
        ]

    def about_buttons() -> List[List[Dict[str, str]]]:
        return [
            [
                {"text": "Home 🏠", "callback_data": "home"},
                {"text": "Help 📚", "callback_data": "help"}
            ],
            [
                {"text": "Channel 📢", "url": CHANNEL_LINK}
            ]
        ]

    def file_buttons(file_uuid: str) -> List[List[Dict[str, str]]]:
        return [
            [
                {"text": "Download 📥", "callback_data": f"download_{file_uuid}"},
                {"text": "Share 🔗", "callback_data": f"share_{file_uuid}"}
            ],
            [
                {"text": "Channel 📢", "url": CHANNEL_LINK}
            ]
        ]


class Progress:
    PROGRESS_BAR = "█"
    EMPTY_PROGRESS_BAR = "░"
    PROGRESS_TEXT = """
**{0}** {1}% 

**⚡️ Speed:** {2}/s
**💫 Done:** {3}
**💭 Total:** {4}
**⏰ Time Left:** {5}
"""
