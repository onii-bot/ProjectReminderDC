import discord
from discord import app_commands
from discord.ext import commands
import os
from typing import Literal
from dotenv import load_dotenv
from utils.utils import create_embeds_reminder, isTimeValid, create_embeds_project
from ui.Button import ReminderButtons, ProjectButtons
from server.fetchers import get_projects, get_user_reminders
from server.setters import set_user_reminder

load_dotenv()


intents = discord.Intents.all()
intents.members = True

client = commands.Bot(intents=intents, command_prefix=".", case_insensitive=True)


@client.event
async def on_ready():
    try:
        synced = await client.tree.sync()
        print(f"Synced {len(synced)} commands")
    except Exception as e:
        print(e)
    print("logged in")


"""

Part for setting reminder

"""

@client.tree.command(name="reminder", description="Set reminder for a certain project")
@app_commands.describe(project='Select a project', reminder_time="Select a time for reminder(end with am/pm)", frequency="Select how often u want to be reminded")
async def set_reminder(interaction: discord.Interaction, project:str, reminder_time:str, frequency:Literal["daily", "weekly", "monthly"]):
    if not isTimeValid(reminder_time):
        await interaction.response.send_message(f"Your Provided time format is wrong. -> {reminder_time}")
        return
    try:
        res = set_user_reminder(username=interaction.user.name, reminder_time=reminder_time, frequency=frequency, progress="None", project=project)
        await interaction.response.send_message(f"Successfully Set reminder")
    except Exception as e:
        await interaction.response.send_message("Server Error")
        print(e)
    

@set_reminder.autocomplete('project')
async def autocomplete_callback(interaction: discord.Interaction, current: str):
    projects = get_projects()
    return [app_commands.Choice(name=f'{projects[id]['project_name']}', value=f'{id}') for id in projects.keys()]

"""

Part for fetching reminder for a user

"""

@client.tree.command()
@app_commands.describe(user="Select a user whose reminders you want to fetch")
async def show_reminders(interaction: discord.Interaction, user: discord.Member = None):
    if user is None:
        user = interaction.user.name
    data = get_user_reminders(user)
    if data:
        embeds = create_embeds_reminder(data)
        view= ReminderButtons(data)
        await interaction.response.send_message(embed=embeds[0],view=view)
    else:
        await interaction.response.send_message("You have no reminders set. Please start by using /set_reminder")

"""

Part for fetching projects

"""
@client.tree.command()
async def show_projects(interaction: discord.Interaction):
    projects = get_projects()
    if projects:
        embeds = create_embeds_project(projects)
        view= ProjectButtons(projects)
        await interaction.response.send_message(embed=embeds[0],view=view)
    else:
        await interaction.response.send_message("You have no reminders set. Please start by using /set_reminder")


client.run(os.environ["DISCORD_TOKEN"])