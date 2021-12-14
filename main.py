# 897133833424605224 client
# ODk3MTMzODMzNDI0NjA1MjI0.YWRO_Q.8lH1q0zOWnm-nF4V4tnbQbydhN8 token
# 156766824512

import discord
from discord import colour
from discord.ext import commands
from datetime import datetime, timedelta
#ดึงข้อมูลมาจากไฟล์ data
from data import character_info_list
from data2 import weapon_info_list
from gacha import wish10pull,  wish1pull, garantee5
from dungeon import dungeon_list
from asyncio import sleep
from discord.ui import Button, View

bot = commands.Bot(command_prefix="!")
bot.remove_command("help")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    await bot.change_presence(activity=discord.Game(name="!menu เพื่อดูคำสั่งทั้งหมด"))
    
@bot.command()
async def menu(ctx):
    await ctx.channel.purge(limit=1)
    text = discord.Embed(title="Paimon Bot Menu", description="อยากให้ Paimon ใช้คำสั่งอะไรบ้างล่ะ? **{0}**" .format(ctx.author.display_name), colour=0xCFF1E3)
    text.add_field(name="`!char <list หรือ [character|number]>`", value="List Character ทั้งหมด\nตัวอย่างเช่น\n- !char list - !char hu tao - !char 13", inline=False)
    text.add_field(name="`!weapon <list หรือ [weapon|type]>`", value="List Weapon ทั้งหมด\nตัวอย่างเช่น\n- !weapon list - !weapon bows - !weapon polar star", inline=False)
    text.add_field(name="`!gacha <wish10 หรือ wish1>`", value="สุ่มกาชาจำลอง", inline=False)
    text.add_field(name="`!resin <your resin>`", value="คำนวณระยะเวลาที่ Resin ของคุณจะเต็มและเต็มตอนกี่โมง", inline=False)
    text.add_field(name="`!dungeon <today หรือ monday, ... , sunday>`", value="Meterials อัพตัวละครที่ดรอปในดันแต่ละวัน", inline=False)
    text.add_field(name="`!clear <amount>`", value="ลบข้อความ [จำนวน]", inline=False)
    text.set_image(url="https://img-comment-fun.9cache.com/media/aVOWQnP/a0Na7Bq2_700w_0.jpg")
    await ctx.channel.send(embed=text)

@bot.command()
async def clear(ctx, amount):
    await ctx.channel.purge(limit=int(amount)+1)

@bot.command()
async def dungeon(ctx, day):
    await ctx.channel.purge(limit=1)
    if day == "today": #ถ้าใช้ !dungeon today
        today = datetime.today() - timedelta(hours=3) #เพราะว่า Dungeon รีตี 3 เวลาไทย เลยต้องลบเวลาไปก่อน 3 ชั่วโมงเพื่อให้เวลาเดินช้าลง **ในเซิฟต้องใช้ +4
        print(today)
        today = today.weekday() #คืนค่าเป็นเลข 0-6 เริ่มที่ Monday = 0
        dun_info = dungeon_list(today) #ดึง List ข้อมูลตามวันมาใส่
    else: #ถ้าใช้ !dungeon monday, tuesday , ... บลาๆ
        day_list = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
        today = day_list.index(day)
        dun_info = dungeon_list(today)
    colour_list = {0:0xffd700, 1:0xff80ed, 2:0x5ac18e, 3:0xffa500, 4:0x66ccff, 5:0x8a2be2, 6:0xff0000} #สีตามวัน
    text = discord.Embed(title="Dungeon {0}" .format(dun_info["day"]), description="", colour=colour_list[today])
    for position in range(1, len(dun_info)):
        text.add_field(name="{0} -- `{1}`" .format(dun_info[position]["name"], dun_info[position]["dunbook"]), value="{0}" .format("\n".join(dun_info[position]["charlist"])), inline=False)
    await ctx.channel.send(embed=text)

class RemindButton(View):
    def __init__(self, ctx, time):
        super().__init__(timeout=60)
        self.ctx = ctx
        self.beforefull = (time-8)*60
        self.full = time*60

    @discord.ui.button(label="ตั้งเวลา!", style=discord.ButtonStyle.green, emoji=None)
    async def button_callback(self, button, interaction):
        for x in self.children:
            x.disabled = True
        await interaction.response.edit_message(view=self)
        await interaction.followup.send("{0} เราได้ตั้งเวลาแจ้งเตือนเมื่อ Resin เต็มสำหรับคุณแล้ว" .format(self.ctx.author.mention))
        await sleep(self.beforefull)
        for _ in range(5):
            await self.ctx.author.send("{0} Resin ใกล้จะเต็มแล้ว อย่าลืมไปใช้ด้วยนะ!" .format(self.ctx.author.mention))
        await sleep(480)
        for _ in range(5):
            await self.ctx.author.send("{0} Resin เต็มแล้ว!!!!!" .format(self.ctx.author.mention))

    @discord.ui.button(label="ไม่!", style=discord.ButtonStyle.danger, emoji=None)
    async def no_button_callback(self, button, interaction):
        self.clear_items()
        await interaction.response.edit_message(view=self)

    async def interaction_check(self, interaction):
        if interaction.user != self.ctx.author:
            await interaction.response.send_message("คุณกดปุ่มนี้ไม่ได้", ephemeral=True)
            return False
        else:
            return True

    async def on_error(self, error, item, interaction):
        await interaction.response.send_message(str(error))

@bot.command()
async def resin(ctx, resin_number): #หาเวลาที่ Resin จะเต็ม
    await ctx.channel.purge(limit=1)
    resin_number = int(resin_number)
    if resin_number < 0:
        resin_number = 0
        resin_left = 160
    elif resin_number > 160:
        resin_left = 0
    else:
        resin_left = 160-(resin_number) #Resin ที่ไม่มี
    min_left_all = resin_left*8 #นาทีที่เหลือทั้งหมด
    min_left = min_left_all%60 #ชั่วโมง
    hour_left = min_left_all//60 #นาที
    datetofull = datetime.now() + timedelta(hours=hour_left+7, minutes=min_left) # +7 ไปเพราะ Timezone ใน Web ที่เปิดมันไม่ใช่ของไทย ทำให้เวลา Output มันผิด
    timetofull = str(datetofull)
    text = discord.Embed(title="Resin Calculator", description="**{0}** มี `{1}` Resin\n" .format(ctx.author.display_name, resin_number), color=0x2ADADA)
    text.add_field(name="เหลือเวลาก่อนที่ Resin จะเต็ม", value="{0} ชั่วโมง {1} นาที" .format(hour_left, min_left), inline=False)
    text.add_field(name="Resin จะเต็มที่เวลาประมาณ", value="%.10s | %s" %(datetofull, timetofull[10:19]), inline=False)
    text.set_thumbnail(url="https://i.ytimg.com/vi/jkd2YHd8NpQ/maxresdefault.jpg")
    text.set_footer(text="!!!!!ตั้งเวลาแจ้งเตือน Resin เต็ม กรุณากดปุ่มด้านล่าง!!!!!")
    #ปุ่มกด
    view = RemindButton(ctx, min_left_all)
    await ctx.channel.send(embed=text, view=view)

@bot.command()
async def gacha(ctx, userinput):
    # CHARACTERS and WEAPONS from STANDARD BANNER
    if userinput == 'wish10': #!gacha wish10
        await ctx.channel.purge(limit=1)
        wish = wish10pull()
        wish_embed = discord.Embed(title="Gacha Result", color=0x1155FF)
        wish_embed.add_field(name="----------------------------------------------------", value="{0}" .format("\n".join(wish)))
        wish_embed.add_field(name="----------------------------------------------------", value="You're {0} rolls away from guaranteed five stars." .format(90-garantee5), inline=False)
        wish_check = " ".join(wish)
        if wish_check.count("5★") >= 1:
            wish_embed.set_image(url="https://c.tenor.com/boSsE56i-F8AAAAC/genshin-wish.gif")
        else:
            wish_embed.set_image(url="https://c.tenor.com/7pBGCuD2JHcAAAAd/genshin.gif")
        wish
        await ctx.channel.send(embed=wish_embed)

    elif userinput == 'wish1': #!gacha wish1
        await ctx.channel.purge(limit=1)
        wish = wish1pull()
        wish_embed = discord.Embed(title="Gacha Result", color=0x1155FF)
        wish_embed.add_field(name="----------------------------------------------------", value="{0}" .format(*wish))
        wish_embed.add_field(name="----------------------------------------------------", value="You're {0} rolls away from guaranteed five stars." .format(90-garantee5), inline=False)
        wish_check = " ".join(wish) #เอาไว้ Check ว่ามีกี่ ★ จะได้ใส่ภาพใน Embed ถูก
        if wish_check.count("5★") == 1:
            wish_embed.set_image(url="https://c.tenor.com/boSsE56i-F8AAAAC/genshin-wish.gif")
        elif wish_check.count("4★") == 1:
            wish_embed.set_image(url="https://c.tenor.com/7pBGCuD2JHcAAAAd/genshin.gif")
        else:
            wish_embed.set_image(url="https://cdn.fbsbx.com/v/t59.2708-21/249061080_3251962895037057_6263778793211452194_n.gif?_nc_cat=107&fallback=1&ccb=1-5&_nc_sid=041f46&_nc_eui2=AeH7Hug5jW-SkoN1Zx3Xx7Yo0QhXCU1U0m_RCFcJTVTSb14fAagtRnGK3myERsKlqAEvgrX2vRJjfzbEDpk6JAAX&_nc_ohc=zSzQXXqjmzIAX-EPoKZ&_nc_ht=cdn.fbsbx.com&oh=d68f65b4397e31e10f49c8d0a55df91c&oe=618A6BB8")
        await ctx.channel.send(embed=wish_embed)

@bot.command()
async def char(ctx, *, name):
    if name != "list":
        character_info = character_info_list(name)
        send = discord.Embed(title="Overview", description="", colour=0xb24cd8)
        send.set_thumbnail(url=character_info['thum'])
        send.add_field(name="{1} {0}".format(character_info['name'], character_info['star']), value="{0}".format(character_info['his1']), inline=False)
        send.add_field(name='---------- Details ----------', value="**ประเภทอาวุธ :** {0}\n**สังกัดที่ :** {1}\n**วันเกิด :** {2}\n**ธาตุ :** {3}".format(character_info['detail'][0], character_info['detail'][1], character_info['detail'][2], character_info['detail'][3]), inline=False)
        send.add_field(name='---------- Stats [Lv.90] ----------', value="**Base HP: **{0}\n**Base ATK: **{1}\n**Base DEF: **{2}\n**Special Stats {3}: **{4}"\
        .format(character_info['stat'][0], character_info['stat'][1], character_info['stat'][2], character_info['stat'][4], character_info['stat'][3]), inline=False)
        send.add_field(name='---------- Ascension Cost ----------',value='{0}'.format(character_info['ascen']))
        await ctx.channel.purge(limit=1)
        await ctx.channel.send(embed=send)
    elif name == "list":
        charlist = character_info_list(name)
        send = discord.Embed(title="Character List", description="{0}" .format("\n".join(charlist)), colour=0xffd700)
        send.set_thumbnail(url="https://scontent.fbkk2-7.fna.fbcdn.net/v/t1.6435-9/120373944_377298110314470_5457606321061026205_n.png?_nc_cat=108&ccb=1-5&_nc_sid=730e14&_nc_ohc=c7i92be5JSkAX-0rHI5&_nc_ht=scontent.fbkk2-7.fna&oh=9b044e4a8446b9310b3fc34798d26ae2&oe=61B8F4BD")
        await ctx.channel.purge(limit=1)
        await ctx.channel.send(embed=send)

@bot.command()
async def weapon(ctx, *, name):
    weapon_type = ["bows", "claymores", "polearms", "catalysts", "swords"]
    if name == "list" or name.lower() in weapon_type:
        weaponlist = weapon_info_list(name)
        send = discord.Embed(title="Weapon List", description="{0}" .format("\n".join(weaponlist)), colour=0xed4b6f)
        send.set_thumbnail(url="https://ih1.redbubble.net/image.1942540739.9959/st,small,507x507-pad,600x600,f8f8f8.jpg")
        if name == "list":
            send.set_footer(text="เลือกชนิดของอาวุธที่ต้องการแล้วพิมพ์ !weapon [type]")
        else:
            send.set_footer(text="เลือกอาวุธที่ต้องการแล้วพิมพ์ !weapon [name]")
        await ctx.channel.purge(limit=1)
        await ctx.channel.send(embed=send)
    elif name != "list" and name not in weapon_type:
        weapon_info = weapon_info_list(name)
        send = discord.Embed(title="Overview", description="", colour=0x52eb80)
        send.set_thumbnail(url= weapon_info['thum'])
        send.add_field(name="{0} {1}".format(weapon_info['star'], weapon_info['name']), value="{0}" .format(weapon_info['his']), inline=False)
        send.add_field(name="---------- Details ----------", value="**Class:** {0}" .format(weapon_info['type']), inline=False)
        send.add_field(name="---------- Stats [Lv.90] ----------", value="**Base ATK:** {0}\n**{1}:** {2}" .format(weapon_info['stat'][0], weapon_info['stat'][2], weapon_info['stat'][1]), inline=False)
        send.add_field(name="---------- {0} ----------" .format(weapon_info["skill"][0]), value="{0}" .format(weapon_info["skill"][1]), inline=False)
        send.add_field(name='---------- Ascension Cost ----------',value='{0}' .format(weapon_info['ascen']))
        await ctx.channel.purge(limit=1)
        await ctx.channel.send(embed=send)

bot.run("ODk3MTMzODMzNDI0NjA1MjI0.YWRO_Q.8lH1q0zOWnm-nF4V4tnbQbydhN8")
