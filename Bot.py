from pyrogram import Client
from pyrogram import filters

from pyrogram.types import Message

from pyrogram.errors.exceptions.bad_request_400 import MsgIdInvalid

# Edit lines 11, 12, 15, 16 before running the bot

# variables
api_id = 12345678 # <-- Put Your API_ID Here
api_hash = "api_hash" # <-- Put Your API_HASH Here

texts = {
    "First Comment": "first_comment_text", # <-- Put Your First Comment Text Here
    "Comment": "comment_text", # <-- Put Your Comment Text Here
    }
 
# Create a client
app = Client("comment", api_id, api_hash)

@app.on_message(filters.channel)
async def send_comment(client, message: Message):
            # Leave a comment under the post
            try:    
                count = await app.get_discussion_replies_count(message.chat.id, message.id)
                post_cm = await app.get_discussion_message(message.chat.id, message.id)
                if count == 0:
                    await post_cm.reply_text(texts["First Comment"])
                elif count > 0:
                    await post_cm.reply_text(texts["Comment"])
            except MsgIdInvalid:
                pass
            except UnboundLocalError:
                pass

app.run()