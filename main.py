import logging
import asyncio
from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram.error import TelegramError

# Вставь сюда свой токен
BOT_TOKEN = "YOUR_BOT_TOKEN"
# Вставь сюда свой Telegram User ID (число)
OWNER_ID = 123456789  # Замени на свой реальный ID

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Отправляет приветственное сообщение."""
    user = update.effective_user
    await update.message.reply_html(
        f"Привет, {user.mention_html()}!\n"
        f"Я бот для демонстрации отправки сообщений. Используй команду:\n"
        f"/spam <user_id_цели> <количество_сообщений> <текст_сообщения>\n"
        f"<b>Пример:</b> /spam 987654321 5 Привет, это тест!"
    )

async def spam_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Команда для 'спама' сообщениями."""
    chat_id = update.message.chat_id
    sender_id = update.message.from_user.id

    if sender_id != OWNER_ID:
        await update.message.reply_text("У вас нет прав для использования этой команды.")
        logger.warning(f"Попытка использования /spam от неавторизованного пользователя {sender_id}")
        return

    args = context.args
    if len(args) < 3:
        await update.message.reply_text(
            "Неверное использование. Формат: /spam <user_id_цели> <количество> <текст сообщения>\n"
            "Пример: /spam 987654321 5 Привет!"
        )
        return

    try:
        target_user_id = int(args[0])
        count = int(args[1])
        message_text = " ".join(args[2:])
    except ValueError:
        await update.message.reply_text("User ID цели и количество сообщений должны быть числами.")
        return

    if count <= 0:
        await update.message.reply_text("Количество сообщений должно быть положительным.")
        return
    
    if count > 20: 
        await update.message.reply_text("Слишком много сообщений. Максимум 20 для этой демонстрации.")
        count = 20

    await update.message.reply_text(f"Начинаю отправку {count} сообщений пользователю {target_user_id}...")
    logger.info(f"Начало отправки {count} сообщений пользователю {target_user_id} от {sender_id}")

    sent_count = 0
    failed_count = 0

    for i in range(count):
        try:
            await context.bot.send_message(chat_id=target_user_id, text=f"({i+1}/{count}) {message_text}")
            sent_count += 1
            logger.info(f"Сообщение {i+1} отправлено {target_user_id}")
            await asyncio.sleep(1.1) 
        except TelegramError as e:
            failed_count += 1
            logger.error(f"Ошибка при отправке сообщения {i+1} пользователю {target_user_id}: {e}")
            if "bot was blocked by the user" in str(e).lower():
                await update.message.reply_text(f"Пользователь {target_user_id} заблокировал бота. Отправка остановлена.")
                break
            elif "chat not found" in str(e).lower():
                 await update.message.reply_text(f"Чат с пользователем {target_user_id} не найден. Возможно, неверный ID или пользователь не начинал диалог с ботом.")
                 break
            elif "Retry after" in str(e):
                retry_after_seconds = int(str(e).split()[-1])
                await update.message.reply_text(f"Превышен лимит API. Повторная попытка через {retry_after_seconds} сек. Отправка приостановлена.")
                await asyncio.sleep(retry_after_seconds + 1)
            else:
                await asyncio.sleep(5) 
        except Exception as e: 
            failed_count += 1
            logger.error(f"Непредвиденная ошибка при отправке сообщения {i+1} пользователю {target_user_id}: {e}")
            await update.message.reply_text(f"Произошла непредвиденная ошибка. Отправка может быть неполной.")
            break 

    summary_message = f"Завершено. Отправлено: {sent_count}. Не удалось отправить: {failed_count}."
    await update.message.reply_text(summary_message)
    logger.info(summary_message)


def main() -> None:
    """Запускает бота."""
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("spam", spam_command))

    logger.info("Бот запущен...")
    application.run_polling()

if __name__ == '__main__':
    main()
