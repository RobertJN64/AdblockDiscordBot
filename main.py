from discord.ext import commands
import os

help_command = commands.DefaultHelpCommand(
    no_category = 'PiHole Commands'
)

with open('token.txt') as f:
    TOKEN = f.read()

bot = commands.Bot(command_prefix='!', help_command=help_command, case_insensitive=True)

#region Simple Events
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name="disable", help="Disables the pihole temporarily. Time can be customized, default is 5 minutes")
async def disable(ctx, time=15):
    print("Pihole disabled! (for", time, "minutes)")
    os.system('/usr/local/bin/pihole disable ' + str(time) + 'm')
    await ctx.send("Pihole disabled! (for " + str(time) + " minutes)")

@bot.command(name='enable', help='Reenables pihole.')
async def enable(ctx):
    print("Pihole enabled.")
    os.system('/usr/local/bin/pihole enable')
    await ctx.send("Pihole enabled!")

@bot.command(name='dm', help='Sends a dm to get easier acess to the bot.')
async def dm(ctx):
    print("DM req from", str(ctx.message.author))
    await ctx.message.author.send("Hello from home automation bot.")
    await ctx.message.author.send("Try !enable and !disable.")
    await ctx.send("DM sent.")

bot.run(TOKEN)
