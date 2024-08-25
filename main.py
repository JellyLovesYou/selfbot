from discord.ext import commands
import json
import asyncio
import os
import random
import string
import importlib
import sys


# Self bot made with love from discord... jk from legolovesyou


with open('config.json') as f:
    config = json.load(f)


token = config.get('token')
prefix = config.get('prefix')
user_id = int(config.get('user_id'))
delay = int(config.get('delay'))


Lego = commands.Bot(command_prefix=prefix, self_bot=True)


send_task = None


@Lego.event
async def on_ready():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(
        f'\033[38;5;196mLogged in as \033[38;5;46m{Lego.user.name}\033[0m'
    )


@Lego.event
async def on_command_error(ctx, error):
    print(f"An error occurred: {error}")


@Lego.command()
async def ping(ctx):
    if ctx.author.id != user_id:
        print(f"Unauthorized user {ctx.author.id} tried to use ping.")
        return
    await ctx.send('pong')
    await ctx.message.delete()


@Lego.command()
async def send(ctx, *, text: str = None):
    if ctx.author.id != user_id:
        print(f"Unauthorized user {ctx.author.id} tried to use send.")
        return

    global send_task

    if text is None:
        length = 10
        characters = string.ascii_letters + string.digits

        if send_task and not send_task.done():
            await ctx.send("I'm busy.")
            await ctx.message.delete()
            return

        async def send_messages():
            while True:
                try:
                    new_text = ''.join(random.choices(characters, k=length))
                    await ctx.send(new_text)
                    await asyncio.sleep(delay)
                except Exception as e:
                    print(f"Error while sending messages: {e}")
                    break

        send_task = asyncio.create_task(send_messages())
        await ctx.message.delete()
    else:
        if send_task and not send_task.done():
            await ctx.send("I'm busy.")
            await ctx.message.delete()
            return

        async def send_messages():
            while True:
                try:
                    await ctx.send(text)
                    await asyncio.sleep(delay)
                except Exception as e:
                    print(f"Error while sending messages: {e}")
                    break

        send_task = asyncio.create_task(send_messages())
        await ctx.message.delete()


@Lego.command()
async def stop(ctx):
    if ctx.author.id != user_id:
        print(f"Unauthorized user {ctx.author.id} tried to use stop.")
        return

    global send_task

    if send_task and not send_task.done():
        send_task.cancel()
        send_task = None
        await ctx.send("Okay, I'll stop...")
    else:
        await ctx.send("I wasn't doing anything.")

    await ctx.message.delete()


@Lego.command()
async def restart(ctx):
    if ctx.author.id != user_id:
        print(f"Unauthorized user {ctx.author.id} tried to use restart.")
        return

    try:
        importlib.reload(sys.modules[__name__])
        await ctx.send("I'm back!")
    except Exception as e:
        print(f"Error while restarting: {e}")
        await ctx.send("Damn that didn't work right.")


@Lego.command()
async def clear(ctx, limit: int):
    if ctx.author.id != user_id:
        print(f"Unauthorized user {ctx.author.id} tried to use clear.")
        return

    if limit < 1 or limit > 1000:
        print("Please specify a number between 1 and 1000.")
        return

    deleted_count = 0
    delete_delay = 1

    async for message in ctx.channel.history(limit=limit):
        if message.author == ctx.author:
            try:
                await message.delete()
                deleted_count += 1
                await asyncio.sleep(delete_delay)
            except Exception as e:
                print(f"Error deleting a message: {e}")

    await ctx.send("Deleted.")
    await ctx.message.delete()


if __name__ == "__main__":
    Lego.run(token)
