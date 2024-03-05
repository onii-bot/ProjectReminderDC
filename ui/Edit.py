import discord
from utils.utils import isTimeValid, get_project_id_from_author, get_reminder_id_from_title
from server.editors import edit_user_reminder

class Edit(discord.ui.Modal, title='Edit'):
    def __init__(self, embed):
        super().__init__()
        self.embed = embed
        self.embed_values = {}
        for field in embed.fields:
            self.embed_values[field.name] = field.value

    async def on_submit(self, interaction: discord.Interaction):
        if interaction.user.name != self.embed_values['Username']:
            await interaction.response.send_message(f'You are not authorized to edit this reminder')
            return
        
        reminder_time, frequency, progress = [item.value for item in self.children]
        # Validating Time
        if not isTimeValid(reminder_time):
            await interaction.response.send_message(f"Your Provided time format is wrong. -> {reminder_time}")
            return
        
        # Frequency
        if not frequency.lower() in ["daily", "weekly", "monthly"]:
            await interaction.response.send_message(f"Frequency can only be daily, weekly or monthly. -> {frequency}")
            return
        username, project, reminder_id = self.embed_values["Username"], get_project_id_from_author(self.embed.author.name), get_reminder_id_from_title(self.embed.title)
        res = edit_user_reminder(username=username, reminder_time=reminder_time, frequency=frequency, progress=progress, project=project, reminder_id=reminder_id)
        self.embed.set_field_at(index=1, name="Reminder Time", value=f"{reminder_time}")
        self.embed.set_field_at(index=2, name="Frequency", value=f"{frequency}", inline=False)
        self.embed.set_field_at(index=3, name="Progress", value=f"{progress}")
        await interaction.response.edit_message(embed=self.embed)