import discord
import config
from discord.ext import commands

# Создание экземпляра бота
intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True  # Необходимо для отслеживания состояния голосовых каналов

bot = commands.Bot(command_prefix='!', intents=intents)

# Идентификатор текстового канала, куда будут отправляться сообщения
TEXT_CHANNEL_ID = 768511625014542347  # Замените на ID вашего текстового канала

# Событие при обновлении состояния голосового канала
@bot.event
async def on_voice_state_update(member, before, after):
    channel = bot.get_channel(TEXT_CHANNEL_ID)
    if channel is not None:
        if after.channel is not None and before.channel is None:
            # Пользователь зашел в голосовой канал
            await channel.send('Кто-то пришел')
        elif after.channel is None and before.channel is not None:
            # Пользователь покинул голосовой канал
            await channel.send('Кто-то ушел')

# Событие при запуске бота
@bot.event
async def on_ready():
    print(f'Мы вошли как {bot.user}')

# Запуск бота
bot.run(config.token)
