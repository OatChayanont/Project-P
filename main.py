# 897133833424605224 client
# ODk3MTMzODMzNDI0NjA1MjI0.YWRO_Q.8lH1q0zOWnm-nF4V4tnbQbydhN8 token
# 156766824512

import discord
from discord import colour
from discord.ext import commands
from datetime import datetime, timedelta
import random
from data import character_info_list, dungeon_list #ดึงข้อมูลมาจากไฟล์ data

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
    text.add_field(name="`!char <list หรือ [character]>`", value="List Character ทั้งหมด\nตัวอย่างเช่น\n!char list\n!char hu tao", inline=False)
    text.add_field(name="`!weapon <list หรือ [weapon]>`", value="List Weapon ทั้งหมด\nตัวอย่างเช่น\n!weapon list\n!weapon polar star", inline=False)
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
    text = discord.Embed(title="Dungeon {0}" .format(dun_info[0]), description="", colour=colour_list[today])
    for position in range(1, len(dun_info)):
        text.add_field(name="{0} -- `{1}`" .format(dun_info[position][0], dun_info[position][1]), value="{0}" .format("\n".join(dun_info[position][2])), inline=False)
    await ctx.channel.send(embed=text)
    
    
@bot.command()
async def resin(ctx, resin_number): #หาเวลาที่ Resin จะเต็ม
    await ctx.channel.purge(limit=1)
    resin_left = 160-int(resin_number)
    min_left_all = resin_left*8 #นาทีที่เหลือทั้งหมด
    min_left = min_left_all%60 #ชั่วโมง
    hour_left = min_left_all//60 #นาที
    datetofull = datetime.now() + timedelta(hours=hour_left+7, minutes=min_left) # +7 ไปเพราะ Timezone ใน Web ที่เปิดมันไม่ใช่ของไทย ทำให้เวลา Output มันผิด
    timetofull = str(datetofull)
    text = discord.Embed(title="Resin Calculator", description="**{0}** have `{1}` Resin\n" .format(ctx.author.display_name, resin_number), color=0x2ADADA)
    text.add_field(name="Time remaining untill your Resin is full", value="{0} hours {1} minutes" .format(hour_left, min_left), inline=False)
    text.add_field(name="Resin will be full around", value="%.10s | %s" %(datetofull, timetofull[10:19]), inline=False)
    text.set_thumbnail(url="https://i.ytimg.com/vi/jkd2YHd8NpQ/maxresdefault.jpg")
    await ctx.channel.send(embed=text)

def wish10pull():
    wish = []
    global garantee5
    global garantee4
    for _ in range(0, 10):
        if garantee5 >= 89:
            wish.append(get(5))
            garantee5 = 0
            garantee4 = 0
        elif garantee4 >= 9:
            wish.append(get(4))
            garantee5 += 1
            garantee4 = 0
        else:
            rate = random.uniform(0, 100)
            if rate <= 0.6:
                wish.append(get(5))
                garantee5 = 0
            elif rate <= 5.1:
                wish.append(get(4))
                garantee5 += 1
                garantee4 = 0
            else:
                wish.append(get(3))
                garantee5 += 1
                garantee4 += 1
    wish.sort(reverse=True)
    return wish

def get(rarity):
    if rarity == 5:  # 0.6%
        if random.random() < 0.5:
            return '[5★] ' + random.choice(five_star_char)
        else:
            return '[5★] ' + random.choice(five_star_weapon)
    elif rarity == 4:  # 5.1%
        if random.random() < 0.5:
            return '[4★] ' + random.choice(four_star_char)
        else:
            return '[4★] ' + random.choice(four_star_weapon)
    elif rarity == 3:  # 94.3%s
        return '[3★] ' + random.choice(three_star_weapon)

def wish1pull():
    wish = []
    global garantee5
    global garantee4
    for _ in range(1):
        if garantee5 >= 89:
            wish.append(get(5))
            garantee5 = 0
            garantee4 = 0
        elif garantee4 >= 9:
            wish.append(get(4))
            garantee5 += 1
            garantee4 = 0
        else:
            rate = random.uniform(0, 100)
            if rate <= 0.6:
                wish.append(get(5))
                garantee5 = 0
            elif rate <= 5.1:
                wish.append(get(4))
                garantee5 += 1
                garantee4 = 0
                
            else:
                wish.append(get(3))
                garantee5 += 1
                garantee4 += 1
    return wish

global five_star_char
five_star_char = ['Jean', 'Qiqi', 'Keqing', 'Mona', 'Dilluc']
global four_star_char
four_star_char = ['Sayu', 'Sucrose', 'Rosaria', 'Diona', 'Chonyun', 'Kaeya', 'Kujou Sara', 'Fischl', 'Beidou', 'Razor',
                'Lisa', 'Nolle', 'Ningguang', 'Xingqiu', 'Barbara', 'Yanfei', 'Xinyan', 'Bennett', 'Xiangling', 'Amber']
global five_star_weapon
five_star_weapon = ['Skyward Harp', 'Amos\' Bow', 'Skyward Atlas', 'Lost Prayer to the Sacred Winds', 'Skyward Pride',
                    'Wolf\'s Gravestone', 'Skyward Spine', 'Primordial Jade Winged-Spear', 'Skyward Balde', 'Aqulia Favonia']
global four_star_weapon
four_star_weapon = ['Favonius Warbow', 'Sacrificial Bow', 'The Stringless', 'Rust', 'Favonius Codex', 'Sacrificial Fragments', 'The Widsith', 'Eye of Perception',
                    'Favonius Greatsword', 'Sacrificial Greatsword', 'The Bell', 'Rainslasher', 'Favonius Lance', 'Dragon\'s Bane', 'Favonius Sword', 'Sacrificial Sword', 'The Flute', 'Lion\'s Roar']
global three_star_weapon
three_star_weapon = ['Slingshot', 'Sharpshooter\'s Oath', 'Raven Bow', 'Emerald Orb', 'Thrilling Tales of Dragon Slayers', 'Magic Guide',
                    'Debate Club', 'Bloodtainted Greatsword', 'Ferrous Shadow', 'Black Tassel', 'Skyrider Sword', 'Harbinger of Dawn', 'Cool Steel']
global garantee5
garantee5 = 0
global garantee4
garantee4 = 0
    
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
async def test(ctx, *, par):
    await ctx.channel.send("You are fucking noob {0}" .format(par))

@bot.event
async def on_message(message):
    if message.content == "Hi":
        await message.channel.purge(limit=1)
    elif message.content == "เสือก":
        await message.channel.send("แล้วมึงควยไรไอ้หน้าหี")
    elif message.content == "sad":
        await message.channel.send(str(message.author.display_name) + " มึง sad เหี้ยไร เศร้ามากก็ไปตายไอ้ควาย")
    await bot.process_commands(message)


@bot.command()
async def char(ctx, *, name):
    if name != "list":
        character_info = character_info_list(name)
        send = discord.Embed(title="Overview", description="", colour=0xb24cd8)
        send.set_thumbnail(url=character_info[3])
        send.add_field(name="{1} {0}".format(name.capitalize(), character_info[4]), value="{0}\n\n{1}".format(character_info[0][0],character_info[0][1]), inline=False)
        send.add_field(name='---------- Stats [Lv.90] ----------', value="**Base HP: **{2}\n**Base ATK: **{3}\n**Base DEF: **{4}\n**Special Stats {0}: **{1}"\
        .format(character_info[1][4], character_info[1][3], character_info[1][0], character_info[1][1], character_info[1][2]), inline=False)
        send.add_field(name='---------- Ascension Cost ----------',value='{0}'.format(character_info[2]))
        await ctx.channel.purge(limit=1)
        await ctx.channel.send(embed=send)
    elif name == "list":
        charlist = character_info_list(name)
        send = discord.Embed(title="Character List", description="{0}" .format("\n".join(charlist)), colour=0xffd700)
        send.set_thumbnail(url="https://scontent.fbkk2-7.fna.fbcdn.net/v/t1.6435-9/120373944_377298110314470_5457606321061026205_n.png?_nc_cat=108&ccb=1-5&_nc_sid=730e14&_nc_ohc=c7i92be5JSkAX-0rHI5&_nc_ht=scontent.fbkk2-7.fna&oh=9b044e4a8446b9310b3fc34798d26ae2&oe=61B8F4BD")
        await ctx.channel.purge(limit=1)
        await ctx.channel.send(embed=send)

bot.run("ODk3MTMzODMzNDI0NjA1MjI0.YWRO_Q.8lH1q0zOWnm-nF4V4tnbQbydhN8")
