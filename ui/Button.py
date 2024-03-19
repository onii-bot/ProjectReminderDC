import discord
from utils.utils import create_embeds_reminder, get_reminder_id_from_title, create_embeds_project
from ui.Edit import Edit
from server.destroyers import delete_user_reminder

class ReminderButtons(discord.ui.View):
    def __init__(self, data, *, timeout=180):
        super().__init__(timeout=timeout)
        self.current_page = 0
        self.embeds = create_embeds_reminder(data)
        self.max_page = len(data)-1

    @discord.ui.button(style=discord.ButtonStyle.secondary,emoji="⬅️")
    async def left_arrow(self, interaction:discord.Interaction, button:discord.ui.Button):
        if self.current_page > 0:
            self.current_page -= 1
            await interaction.response.edit_message(embed=self.embeds[self.current_page],view=self)
        else:
            await interaction.response.send_message("You are reaching void bud", ephemeral=True)

    @discord.ui.button(style=discord.ButtonStyle.gray,emoji="➡️")
    async def right_arrow(self, interaction:discord.Interaction, button:discord.ui.Button):
        if self.current_page < self.max_page:
            self.current_page += 1
            await interaction.response.edit_message(embed=self.embeds[self.current_page],view=self)
        else:
            await interaction.response.send_message("You are reaching void bud", ephemeral=True)
    
    @discord.ui.button(style=discord.ButtonStyle.primary,label="Edit")
    async def edit_button(self, interaction:discord.Interaction, button:discord.ui.Button):
        edit = Edit(self.embeds[self.current_page])
        edit.add_item(discord.ui.TextInput(
            label='Reminder Time',
            placeholder='Enter Time here...',
            default=edit.embed_values['Reminder Time']
        ))
        edit.add_item(discord.ui.TextInput(
            label='Frequency',
            placeholder='Enter your frequency(daily,weekly,montly)...',
            default=edit.embed_values['Frequency']
        ))
        edit.add_item(discord.ui.TextInput(
            label='Progress',
            placeholder='Enter your progress...',
            default=edit.embed_values['Progress']
        ))

        await interaction.response.send_modal(edit)
    
    @discord.ui.button(style=discord.ButtonStyle.red, label="Delete")
    async def delete_button(self, interaction:discord.Interaction, button:discord.ui.Button):
        embed = self.embeds[self.current_page]
        embed_values = {}
        for field in embed.fields:
            embed_values[field.name] = field.value

        reminder_id = get_reminder_id_from_title(embed.title)
        username = embed_values['Username']
        if username != interaction.user.name:
            await interaction.response.send_message("You are not authorized to delete", ephemeral=True)
            return
        res = delete_user_reminder(username=username, reminder_id=reminder_id)
        self.embeds.pop(self.current_page)
        # self.current_page = 1
        self.max_page -= 1
        # for i in range(len(self.embeds)):
        #     self.embeds[i].set_footer(text=f"Page: {self.current_page+1}/{self.max_page}")
        await interaction.response.edit_message(embed=self.embeds[self.current_page])

class ProjectButtons(discord.ui.View):
    def __init__(self, data, *, timeout=180):
        super().__init__(timeout=timeout)
        self.current_page = 0
        self.embeds = create_embeds_project(data)
        self.max_page = len(data)-1

    @discord.ui.button(style=discord.ButtonStyle.secondary,emoji="⬅️")
    async def left_arrow(self, interaction:discord.Interaction, button:discord.ui.Button):
        if self.current_page > 0:
            self.current_page -= 1
            await interaction.response.edit_message(embed=self.embeds[self.current_page],view=self)
        else:
            await interaction.response.send_message("You are reaching void bud", ephemeral=True)

    @discord.ui.button(style=discord.ButtonStyle.gray,emoji="➡️")
    async def right_arrow(self, interaction:discord.Interaction, button:discord.ui.Button):
        if self.current_page < self.max_page:
            self.current_page += 1
            await interaction.response.edit_message(embed=self.embeds[self.current_page],view=self)
        else:
            await interaction.response.send_message("You are reaching void bud", ephemeral=True)
        