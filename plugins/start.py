from pyrogram import Client, filters
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
import humanize
from helper.database import  insert 

@Client.on_message(filters.private & filters.command(["start"]))
async def start(client,message):
	insert(int(message.chat.id))
	await message.reply_text(text =f"""
	👋 Hey {message.from_user.first_name }
	
<b>🔰 𝘐 𝘊𝘢𝘯 𝘙𝘦𝘯𝘢𝘮𝘦 ✍️ 𝘈𝘯𝘺 𝘍𝘪𝘭𝘦 📂 & 𝘝𝘪𝘥𝘦𝘰 📽 𝘞𝘪𝘵𝘩 𝘊𝘶𝘴𝘵𝘰𝘮 𝘛𝘩𝘶𝘮𝘣𝘯𝘢𝘪𝘭 𝘚𝘶𝘱𝘱𝘰𝘳𝘵.

↗️You Can Also Use Our [ @Online_File_Streaming_Bot ].
       
➠ Contact Us : @Oxyver_Owner</b> 
	""",reply_to_message_id = message.message_id ,  
	reply_markup=InlineKeyboardMarkup(
	 [[ InlineKeyboardButton(" 🏬 Official Channel 🏬 " ,url="https://t.me/Oxyver"),InlineKeyboardButton("🎥 Movie Channel 🎥" ,url="https://t.me/Mdisk_Video_Movie_Webseries_2") ]  ]))
	


@Client.on_message(filters.private &( filters.document | filters.audio | filters.video ))
async def send_doc(client,message):
       media = await client.get_messages(message.chat.id,message.message_id)
       file = media.document or media.video or media.audio 
       filename = file.file_name
       filesize = humanize.naturalsize(file.file_size)
       fileid = file.file_id
       await message.reply_text(
       f"""__𝘞𝘩𝘢𝘵 𝘋𝘰 𝘠𝘰𝘶 𝘞𝘢𝘯𝘵 𝘔𝘦 𝘛𝘰 𝘋𝘰 𝘞𝘪𝘵𝘩 𝘛𝘩𝘪𝘴 𝘍𝘪𝘭𝘦?<br>__\n**File Name** :- {filename}\n**File Size** :- {filesize}"""
       ,reply_to_message_id = message.message_id,
       reply_markup = InlineKeyboardMarkup([[ InlineKeyboardButton("Rename 📝",callback_data = "rename")
       ,InlineKeyboardButton("Cancel ❌",callback_data = "cancel")  ]]))
