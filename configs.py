# (c) @RoyalKrrishna

import os
# from dotenv import load_dotenv

# load_dotenv()


class Config(object):
    API_ID = int(os.getenv("API_ID", 12345))
    API_HASH = os.getenv("API_HASH", "11e54802bd7a2f8069aa20ae42e9d6b2")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "5741017438:AAEaZNvqQNHeh20CZU_BHJPiz2EBvunnuTE")
    BOT_SESSION_NAME = os.getenv("BOT_SESSION_NAME", "MdiskSearchRobot")
    USER_SESSION_STRING = os.getenv("USER_SESSION_STRING", "1BVtsOJUBu3SmSRZ72xzcgMTNYgghsjfu9pYABblvfmhk329Aqe9R-N6sqyPqCMo2ODSj2X6X77CfxNMfVAMWmqEqMefPEdPyF_P0ob8GQbbN3VQ_3Cthz1rq82TuVIpHp9eU7gMH7TIikaZfbXYOz8MQRGLJW9NjFJCo0g4v3Ke4Qn97FhWCN6F_sBensqp2mJdac7eftmFNVD2FChwj03WSmC6yHYaBOfvKkPTvfWILEm-XtxfNmxQ6n79ET_HZZUcO41oJo79ttAxf0r-BSvdJLlBN9TeQNQUcM3F6Y74iStkzbLIWjb7iRGThd777TS90LRusGhGsUF1UbU2eKRO_hO3x0YY=")
    CHANNEL_ID = int(os.getenv("CHANNEL_ID", -100))
    BOT_USERNAME = os.getenv("BOT_USERNAME")
    BOT_OWNER = int(os.getenv("BOT_OWNER"))
#    OWNER_USERNAME = os.getenv("OWNER_USERNAME")
    BACKUP_CHANNEL = os.getenv("BACKUP_CHANNEL")
#    GROUP_USERNAME = os.getenv("GROUP_USERNAME")
    START_MSG = os.getenv("START_MSG", '''Hᴇʏ, {}! 😃

I Aᴍ A Sɪᴍᴘʟᴇ Mᴏᴠɪᴇ Sᴇᴀʀᴄʜ Bᴏᴛ. 😅

Yᴏᴜ Cᴀɴ Aᴅᴅ Mᴇ Oɴ Yᴏᴜʀ Gʀᴏᴜᴘ As Aᴅᴍɪɴ 🤪

Nᴏᴛᴇ - ɪ ᴄᴀɴ Pʀᴏᴠɪᴅᴇ Yᴏᴜʀ Mᴏᴠɪᴇs Lɪɴᴋs Iɴ Yᴏᴜʀ Gʀᴏᴜᴘ 😜

Fᴏʀ ᴍᴏʀᴇ ɪɴғᴏ Cʟɪᴄᴋ Oɴ Hᴇʟᴘ. ✅''')
    START_PHOTO = os.getenv("START_PHOTO")
    HOME_TEXT = os.getenv("HOME_TEXT", '''Hᴇʏ,{}! 😃

I Aᴍ A Sɪᴍᴘʟᴇ Mᴏᴠɪᴇ Sᴇᴀʀᴄʜ Bᴏᴛ. 😅

Yᴏᴜ Cᴀɴ Aᴅᴅ Mᴇ Oɴ Yᴏᴜʀ Gʀᴏᴜᴘ As Aᴅᴍɪɴ 🤪

Nᴏᴛᴇ - ɪ ᴄᴀɴ Pʀᴏᴠɪᴅᴇ Yᴏᴜʀ Mᴏᴠɪᴇs Lɪɴᴋs Iɴ Yᴏᴜʀ Gʀᴏᴜᴘ 😜

Fᴏʀ ᴍᴏʀᴇ ɪɴғᴏ Cʟɪᴄᴋ Oɴ Hᴇʟᴘ. ✅''')
    UPDATES_CHANNEL = os.getenv("UPDATES_CHANNEL", None)
    DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://ShareDisk:ShareDisk@cluster0.hazejtk.mongodb.net/?retryWrites=true&w=majority")
    LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", "-1001541802204"))
    RESULTS_COUNT = int(os.getenv("RESULTS_COUNT", 5))
    BROADCAST_AS_COPY = os.getenv("BROADCAST_AS_COPY", "True")
    UPDATES_CHANNEL_USERNAME = os.getenv("UPDATES_CHANNEL_USERNAME", "MY_Update")
    FORCE_SUB = os.getenv("FORCE_SUB", "False")
    AUTO_DELETE_TIME = int(os.getenv("AUTO_DELETE_TIME", 300))
    MDISK_API = os.getenv("MDISK_API", "12334")
    VERIFIED_TIME  = int(os.getenv("VERIFIED_TIME", "30"))
    ABOUT_BOT_TEXT = os.getenv("ABOUT_TEXT", '''<b>Hᴇʏ, Bᴜᴅᴅʏ 😃

Tʜɪs Is Mʏ Aʙᴏᴜᴛ Sᴇᴄᴛɪᴏɴ 🙂</b>

<b>✯ Mʏ Nᴀᴍᴇ : </b>

<b>✯ Cʀᴇᴀᴛᴏʀ : <a href=https://t.me/Kavya_Choudhary_08>Kavya</a></b>

<b>✯ Oᴜʀ Cʜᴀɴɴᴇʟ: <a href=https://t.me/MY_Update>My Update</a></b>

<b>✯ Mᴏᴠɪᴇ Rᴇǫᴜᴇsᴛ Gʀᴏᴜᴘ : @MOVIES_CHAT_ROOM_08</b>''')
    ABOUT_HELP_TEXT = os.getenv("HELP_TEXT", '''🍓 RᴇQᴜɪʀᴇᴍᴇɴᴛ ᴛᴏ ᴜꜱᴇ ᴛʜɪꜱ ʙᴏᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ!

🍓 Sᴛᴇᴘ 1 - Aᴘᴋᴏ ᴇᴋ ɢʀᴏᴜᴘ ᴋɪ ᴊᴀʀᴜʀᴀᴛ ʜᴏɢɪ, ᴊɪꜱᴍᴇ ᴍᴇᴍʙᴇʀꜱ ʙʜɪ ʜᴏ, ᴀᴜʀ ᴇᴋ ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀɴɴᴇʟ ᴋɪ ᴊᴀʀᴜʀᴀᴛ ʜᴏɢɪ, ᴊɪꜱᴍᴇ ᴀᴘᴋᴇ ꜱᴀʀᴇ ᴘᴏꜱᴛ ʜᴏɴɢᴇ!

🍓 Sᴛᴇᴘ 2 - ʙᴏᴛ ᴋᴏ ᴀᴘɴᴇ ɢʀᴏᴜᴘ ᴀᴜʀ ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀɴɴᴇʟ ᴋᴀ ᴀᴅᴍɪɴ ʙᴀɴᴀɴᴀ ʜᴏɢᴀ.

🍓 Sᴛᴇᴘ 3 - ɢʀᴏᴜᴘ ᴍᴇ "/Verify" ᴛʏᴘᴇ ᴋᴀʀ ᴋᴇ ꜱᴇɴᴅ ᴋᴀʀɴᴀ ʜᴏɢᴀ!
ꜰɪʀ ʙᴏᴛ ᴋᴇ ᴏᴡɴᴇʀ ᴀᴘᴋᴀ ʏᴇ ʀᴇQᴜᴇꜱᴛ ᴀᴄᴄᴇᴘᴛ ᴋᴀʀ ʟᴇɴɢᴇ. @Kavya_Choudhary_08

🍓 Sᴛᴇᴘ 4 - ɢʀᴏᴜᴘ ᴍᴇ "/db - ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀɴɴᴇʟ ɪᴅ" ᴛʏᴘᴇ ᴋᴀʀ ᴋᴇ ꜱᴇɴᴅ ᴋᴀʀɴᴀ ʜᴏɢᴀ.
ꜰɪʀ ʙᴏᴛ ᴋᴇ ᴏᴡɴᴇʀ ᴀᴘᴋᴀ ʏᴇ ʀᴇQᴜᴇꜱᴛ ʙʜɪ ᴀᴄᴄᴇᴘᴛ ᴋᴀʀ ʟᴇɴɢᴇ @Kavya_Choudhary_08

🍓 Sᴛᴇᴘ 5 - ᴀʙ ᴀᴘᴋᴏ ᴀᴘɴᴇ ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀɴɴᴇʟ ᴍᴇ ᴘᴏꜱᴛ ᴅᴀʟɴɪ ʜᴏɢɪ,
ᴊɪꜱꜱᴇ ᴋɪ ᴀɢᴀʀ ɢʀᴏᴜᴘ ᴍᴇ ᴋᴏɪ ᴜꜱᴇʀ ꜱᴇᴀʀᴄʜ ᴋᴀʀᴇ ᴛᴏ ʏᴇ ʙᴏᴛ ᴜɴ ᴜꜱᴇʀ ᴋᴇ Qᴜᴀʀʏ ᴋᴏ ꜱᴀᴍᴀᴊʜ ᴋᴇ ᴀᴘᴋᴇ ᴄʜᴀɴɴᴇʟ ꜱᴇ ᴘᴏꜱᴛ ᴜᴛʜᴀ ᴋᴇ ᴜɴʜᴇ ᴅᴇ ᴘᴀʏᴇ.

🍓 Nᴏᴛᴇ : Bᴏᴛ ᴀᴅᴍɪɴ ᴀᴘᴋᴇ ᴄʜᴀɴɴᴇʟ ᴍᴇ ᴊᴏɪɴ ʜᴏɴᴇ ᴄʜᴀʜɪʏᴇ,
ᴀɢᴀʀ ʙᴏᴛ ᴀᴅᴍɪɴ ᴀᴘᴋᴀ ʀᴇQᴜᴇꜱᴛ ᴀᴄᴄᴇᴘᴛ ɴʜɪ ᴋᴀʀ ʀᴀʜᴇ ʜᴀɪɴ ᴛᴏ ᴜɴʜᴇ ᴘᴇʀꜱᴏɴᴀʟ ᴍꜱɢ ᴋᴀʀᴇɴ.
👉 @Kavya_Choudhary_08''')
