from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

import os

TOKEN = os.getenv("BOT_TOKEN")
AUTO_REPLY = "היי! כיף שהחלטת להצטרף לקבוצה שלנו!😁
כמו שכתבנו, ההצטרפות מותנת באימות, ואם אתה גבר אז גם בתשלום. 

אם את אישה🩷, כדי לאמת את זהותך, תשלחי תמונה שלך מחזיקה פתק שעליו כתוב "אני מעוניינת להצטרף לקבוצה של המזכירה", ונצרף אותך.
אם אתה גבר🩵, כדי לאמת את זהותך, תשלח תמונה שלך מחזיק פתק שעליו כתוב "אני מעוניין להצטרף לקבוצה של המזכירה", ובנוסף תצטרך לשלם. 
התשלום הינו על סך 200 שקלים (וכל המרבה הרי זה משובח😉)
האופציות לתשלום הן או בקוד משיכה, או דרך ארנק דיגיטלי. אם תבחר בארנק דיגיטלי נשלח לך את ההנחיות☺️. לאחר מכן תצורף לקבוצה! 

מחכות לכולכםן!❤️❤️"

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(AUTO_REPLY)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.ALL, reply))

app.run_polling()
