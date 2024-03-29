import discord
from server.fetchers import get_projects
import re

def create_embeds_reminder(data):
    embeds = []
    projects = get_projects()
    total = len(data)
    for index, item in enumerate(data):
        embed = discord.Embed(title=f"Reminder ID: {item['id']}", color=discord.Color.blurple())
        embed.set_author(name=f"Project ID: {projects[item['project']]['id']}")
        embed.add_field(name="Username", value=item['username'], inline=True)
        embed.add_field(name="Reminder Time", value=item['reminder_time'], inline=True)
        embed.add_field(name="Frequency", value=item['frequency'], inline=False)
        embed.add_field(name="Progress", value=item['progress'], inline=True)
        embed.add_field(name="Project", value=projects[item['project']]["project_name"], inline=True)
        if projects[item['project']]["tasks"]:
            embed.add_field(name="Tasks", value=projects[item['project']]["tasks"], inline=True)
        else:
            embed.add_field(name="Tasks", value="None", inline=True)
        if projects[item['project']]["image_link"]:
            embed.set_thumbnail(url=projects[item['project']]["image_link"])
        embed.set_footer(text=f"Page: {index+1}/{total}")
        embeds.append(embed)

    return embeds

def create_embeds_project(projects):
    embeds = []
    total = len(projects)
    for index, item in enumerate(projects.values()):
        embed = discord.Embed(title=f"Project ID: {item['id']}", color=discord.Color.blurple())
        embed.add_field(name="Project Name", value=item['project_name'], inline=True)
        embed.add_field(name="Tier", value=item['tier'], inline=True)
        embed.add_field(name="Cost to Farm", value=item['cost_to_farm'], inline=True)
        embed.add_field(name="Airdrop Status", value=item['airdrop_status'], inline=True)
        embed.add_field(name="Priority", value=item['priority'], inline=True)
        embed.add_field(name="Funding", value=item['funding'], inline=True)
        embed.add_field(name="Stage", value=item['stage'], inline=True)
        embed.add_field(name="Type", value=item['type'], inline=True)
        embed.add_field(name="Chain", value=item['chain'], inline=True)
        if item["tasks"]:
            embed.add_field(name="Tasks", value=item["tasks"], inline=False)
        else:
            embed.add_field(name="Tasks", value="None", inline=False)
        if item["image_link"]:
            embed.set_thumbnail(url=item["image_link"])
        embed.add_field(name="Twitter Guide", value=item["twitter_guide"], inline=False)
        embed.add_field(name="Discord Link", value=item["discord_link"], inline=False)
        embed.add_field(name="Twitter Link", value=item["twitter_link"], inline=False)
        embed.add_field(name="Frequency", value=item["frequency"], inline=True)
        embed.set_footer(text=f"Page: {index+1}/{total}")
        embeds.append(embed)

    return embeds


def get_project_id_from_author(text):
    match = re.search(r'Project ID: (\d+)', text)
    if match:
        project_id = int(match.group(1))
        return project_id
    else:
        return 0

def get_reminder_id_from_title(text):
    match = re.search(r'Reminder ID: (\d+)', text)
    if match:
        reminder_id = int(match.group(1))
        return reminder_id
    else:
        return 0

def isTimeValid(time):
    time_pattern = re.compile(r'^(0?[1-9]|1[0-2])(:[0-5]\d)?[ap]m$', re.IGNORECASE)
    return time_pattern.match(time)


        