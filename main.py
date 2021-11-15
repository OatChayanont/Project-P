# 897133833424605224 client
# ODk3MTMzODMzNDI0NjA1MjI0.YWRO_Q.8lH1q0zOWnm-nF4V4tnbQbydhN8 token
# 156766824512

import discord
from discord import colour
from discord.ext import commands
from datetime import datetime, timedelta
import random

bot = commands.Bot(command_prefix="!")
bot.remove_command("help")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    await bot.change_presence(activity=discord.Game(name="!menu to show all menu"))
    
@bot.command()
async def menu(ctx):
    await ctx.channel.purge(limit=1)
    text = discord.Embed(title="Paimon Bot Menu", description="What command do you want Paimon to do? **{0}**" .format(ctx.author.name), colour=0xCFF1E3)
    text.add_field(name="`!char <list, [character]>`", value="All Character List\nExample\n!char list\n!char hu tao", inline=False)
    text.add_field(name="`!weapon <list, [weapon]>`", value="All Weapon List\nExample\n!weapon list\n!weapon polar star", inline=False)
    text.add_field(name="`!gacha <wish10, wish1>`", value="Gacha Simulator", inline=False)
    text.add_field(name="`!resin <your resin>`", value="Resin Calculator", inline=False)
    text.add_field(name="`!dungeon <today|monday, ... , sunday>`", value="Meterials can be obtained in dungeon by day", inline=False)
    text.add_field(name="`!clear <amount>`", value="Clear bot messages above for [amount] messages", inline=False)
    text.set_image(url="https://img-comment-fun.9cache.com/media/aVOWQnP/a0Na7Bq2_700w_0.jpg")
    await ctx.channel.send(embed=text)

@bot.command()
async def clear(ctx, amount):
    await ctx.channel.purge(limit=int(amount)+1)

def dungeon_list(day):
    if day == 0 or day == 3:
        dun = ["Monday", ["Forsaken Rift", "Freedom", ["Aloy", "Amber", "Barbara", "Diona", "Klee", "Sucrose", "Tartaglia", "Traveler[Anemo]", "Traveler[Geo]"]],
                ["Taishan Mansion", "Prosperity", ["Keqing", "Ningguang", "Qiqi", "Traveler[Geo]", "Xiao"]],
                ["Violet Court", "Transience", ["Kokomi", "Thoma", "Traveler[Electro]", "Yoimiya"]]]
        if day == 3:
            dun[0] = "Thursday"
    elif day == 1 or day == 4:
        dun = ["Tuesday", ["Forsaken Rift", "Resistance", ["Bennett", "Diluc", "Eula", "Jean", "Mona", "Noelle", "Razor", "Traveler[Anemo]", "Traveler[Geo]"]],
                ["Taishan Mansion", "Diligence", ["Chongyun", "Ganyu", "Hu Tao", "Kazuha", "Traveler[Geo]", "Xiangling"]],
                ["Violet Court", "Elegance", ["Ayaka", "Kujou Sara", "Traveler[Electro]"]]]
        if day == 4:
            dun[0] = "Friday"
    elif day == 2 or day == 5:
        dun = ["Wednesday", ["Forsaken Rift", "Ballad", ["Albedo", "Venti", "Fischl", "Kaeya", "Lisa", "Rosaria", "Traveler[Anemo]", "Traveler[Geo]"]],
                ["Taishan Mansion", "Gold", ["Zhongli", "Beidou", "Xingqiu", "Xinyan", "Traveler[Geo]", "Yanfei"]],
                ["Violet Court", "Elegance", ["Raiden Shogun", "Sayu", "Traveler[Electro]"]]]
        if day == 5:
            dun[0] = "Saturday"
    elif day == 6:
        dun = ["Sunday", ["All Dungeon is open", "All Meterial", ["All Character"]]]
    return dun

@bot.command()
async def dungeon(ctx, day):
    if day == "today":
        today = datetime.today() - timedelta(hours=3) #เพราะว่า Dungeon รีตี 3 เวลาไทย เลยต้องลบเวลาไปก่อน 3 ชั่วโมงเพื่อให้เวลาเดินช้าลง
        print(today)
        today = today.weekday()
        dun_info = dungeon_list(today)
    else:
        day_list = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
        today = day_list.index(day)
        dun_info = dungeon_list(today)
    colour_list = {0:0xffd700, 1:0xff80ed, 2:0x5ac18e, 3:0xffa500, 4:0x66ccff, 5:0x8a2be2, 6:0xff0000} #สีตามวัน
    text = discord.Embed(title="Dungeon {0}" .format(dun_info[0]), description="", colour=colour_list[today])
    for position in range(1, len(dun_info)):
        text.add_field(name="{0} -- `{1}`" .format(dun_info[position][0], dun_info[position][1]), value="{0}" .format("\n".join(dun_info[position][2])), inline=False)
    await ctx.channel.send(embed=text)
    
    
@bot.command()
async def resin(ctx, resin_number):
    await ctx.channel.purge(limit=1)
    resin_left = 160-int(resin_number)
    min_left_all = resin_left*8
    min_left = min_left_all%60
    hour_left = min_left_all//60
    datetofull = datetime.now() + timedelta(hours=hour_left+7, minutes=min_left) # +7 ไปเพราะ Timezone ใน Web ที่เปิดมันไม่ใช่ของไทย ทำให้เวลา Output มันผิด
    timetofull = str(datetofull)
    text = discord.Embed(title="Resin Calculator", description="**{0}** have `{1}` Resin\n" .format(ctx.author.name, resin_number), color=0x2ADADA)
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
        await message.channel.send(str(message.author.name) + " มึง sad เหี้ยไร เศร้ามากก็ไปตายไอ้ควาย")
    await bot.process_commands(message)

###list char###
def character_info_list(name):
    if name.lower() == "list":
        charlist = ["**[5★]** Albedo", "**[5★]** Aloy", "**[4★]** Amber", "**[4★]** Barbara", "**[4★]** Beidou", 
                    "**[4★]** Bennett", "**[4★]** Chongyun", "**[5★]** Diluc", "**[4★]** Diona", "**[5★]** Eula", 
                    "**[4★]** Fischl", "**[5★]** Ganyu", "**[5★]** Hu Tao", "**[5★]** Jean", "**[5★]** Kaedehara Kazuha",
                    "**[4★]** Kaeya", "**[5★]** Kamisato Ayaka", "**[5★]** Keqing", "**[5★]** Klee", "**[4★]** Kujou Sara",
                    "**[4★]** Lisa", "**[5★]** Mona", "**[4★]** Ningguang", "**[4★]** Noelle", "**[5★]** Qiqi",
                    "**[5★]** Raiden Shogun", "**[4★]** Razor", "**[4★]** Rosaria", "**[5★]** Sangonomiya Kokomi", "**[4★]** Sayu",
                    "**[4★]** Sucrose", "**[5★]** Tartaglia", "**[4★]** Thoma", "**[5★]** Traveler",  "**[5★]** Venti",
                    "**[4★]** Xiangling", "**[5★]** Xiao", "**[4★]** Xingqiu", "**[4★]** Xinyan", "**[4★]** Yanfei",
                    "**[5★]** Yoimiya", "**[5★]** Zhongli"]
        return charlist
    elif name.lower() == "albedo":
        albedo = [['Albedo, also known as the "Kreideprinz" is a playable Geo character in Genshin Impact.',
        'The mysterious Albedo is the Chief Alchemist and Captain of the Investigation Team of the Knights of Favonius \
        through a recommendation from the adventurer Alice, with Sucrose as his assistant. He holds an infinite desire to learn about the world of Teyvat, \
        carefully studying every object around him'],\
        ['13,226', '251', '876', '28.8%', '(Geo DMG Bonus)'],\
        '**[✦-----]**:20,000 Mora, Prithiva Topaz Sliver x1, Cecilia x3, Divining Scroll x3\n \
        **[✦✦----]**:40,000 Mora, Prithiva Topaz Fragment x3, Basalt Pilar x2, Cecilia x10, Divining Scroll x15\n \
        **[✦✦✦---]**:60,000 Mora, Prithiva Topaz Fragment x6, Basalt Pilar x4, Cecilia x20, Sealed Scroll x12\n \
        **[✦✦✦✦--]**:80,000 Mora, Prithiva Topaz Chunk x3, Basalt Pilar x8, Cecilia x30, Sealed Scroll x18\n \
        **[✦✦✦✦✦-]**:100,000 Mora, Prithiva Topaz Chunk x6, Basalt Pilar x12, Cecilia x45, Forbidden Curse Scroll x12\n \
        **[✦✦✦✦✦✦]**:120,000 Mora, Prithiva Topaz Gemstone x6, Basalt Pilar x20, Cecilia x60, Forbidden Curse Scroll x24',\
        'https://pbs.twimg.com/media/Epu_dv9XIAE9TJt.png']
        return albedo
    elif name.lower() == "aloy":
        aloy = [['Aloy is a playable Cryo crossover character in Genshin Impact.',
        'She is the heroine from Horizon Zero Dawn and is introduced as a collaboration and crossover character between Guerrilla Games and miHoYo.'],\
        ['10,899', '234', '676', '28.8%', '(Cryo DMG Bonus)'],\
        '**[✦-----]**:20,000 Mora, Shivada Jade Sliver x1, Crystal Marrow x3, Spectral Husk x3\n \
        **[✦✦----]**:40,000 Mora, Shivada Jade Fragment x3, Crystalline Bloom x2, Crystal Marrow x10, Spectral Husk x15\n \
        **[✦✦✦---]**:60,000 Mora, Shivada Jade Fragment x6, Crystalline Bloom x4, Crystal Marrow x20, Spectral Heart x12\n \
        **[✦✦✦✦--]**:80,000 Mora, Shivada Jade Chunk x3, Crystalline Bloom x8, Crystal Marrow x30, Spectral Heart x18\n \
        **[✦✦✦✦✦-]**:100,000 Mora, Shivada Jade Chunk x6, Crystalline Bloom x12, Crystal Marrow x45, Spectral Nucleus x12\n \
        **[✦✦✦✦✦✦]**:120,000 Mora, Shivada Jade Gemstone x6, Crystalline Bloom x20, Crystal Marrow x60, Spectral Nucleus x24',\
        'https://preview.redd.it/avoo8sta65t71.png?auto=webp&s=a4a0401e3e99203a08155a339b5c57f01eb941ee']
        return aloy
    elif name.lower() == "amber":
        amber = [['Amber is a playable Pyro character in Genshin Impact.',
        'As the only remaining Outrider of the Knights of Favonius, she is always ready to help the citizens of Mondstadt — whether it be something simple or perhaps a more challenging task.\n\nShe can be obtained for free in the Prologue Act I: The Outlander Who Caught the Wind during the quest Winds of the Past.'],\
        ['9,461', '223', '601', '24.0%', '(ATK Bonus)'],\
        '**[✦-----]**:20,000 Mora, Agnidus Agate Sliver x1, Small Lamp Grass x3, Firm Arrowhead x3\n \
        **[✦✦----]**:40,000 Mora, Agnidus Agate Fragment x3, Everflame Seed x2, Small Lamp Grass x10, Firm Arrowhead x15\n \
        **[✦✦✦---]**:60,000 Mora, Agnidus Agate Fragment x6, Everflame Seed x4, Small Lamp Grass x20, Sharp Arrowhead x12\n \
        **[✦✦✦✦--]**:80,000 Mora, Agnidus Agate Chunk x3, Everflame Seed x8, Small Lamp Grass x30, Sharp Arrowhead x18\n \
        **[✦✦✦✦✦-]**:100,000 Mora, Agnidus Agate Chunk x6, Everflame Seed x12, Small Lamp Grass x45, Weathered Arrowhead x12\n \
        **[✦✦✦✦✦✦]**:120,000 Mora, Agnidus Agate Gemstone x6, Everflame Seed x20, Small Lamp Grass x60, Weathered Arrowhead x24',\
        'https://i.pinimg.com/originals/1f/d0/dc/1fd0dcd6665c8cad00dba0235a9bf54a.png']
        return amber
###list char###

@bot.command()
async def char(ctx, *, name):
    if name != "list":
        character_info = character_info_list(name)
        send = discord.Embed(title="Overview", description="", colour=0xb24cd8)
        send.set_thumbnail(url= character_info[3])
        send.add_field(name="About {0}".format(name.capitalize()), value="{0} \n\n {1}".format(character_info[0][0],character_info[0][1]), inline=False)
        send.add_field(name='Stats', value="**Special Stat {0} (Lv.90): **{1}\n**Base Hp (Lv.90): **{2}\n**Base ATK (Lv.90): **{3}\n**Base DEF (Lv.90): **{4}"\
        .format(character_info[1][4], character_info[1][3], character_info[1][0], character_info[1][1], character_info[1][2]), inline=False)
        send.add_field(name='Ascension Cost',value='{0}'.format(character_info[2]))
        await ctx.channel.purge(limit=1)
        await ctx.channel.send(embed=send)
    elif name == "list":
        charlist = character_info_list(name)
        send = discord.Embed(title="Character List", description="{0}" .format("\n".join(charlist)), colour=0xffd700)
        send.set_thumbnail(url="https://scontent.fbkk2-7.fna.fbcdn.net/v/t1.6435-9/120373944_377298110314470_5457606321061026205_n.png?_nc_cat=108&ccb=1-5&_nc_sid=730e14&_nc_ohc=c7i92be5JSkAX-0rHI5&_nc_ht=scontent.fbkk2-7.fna&oh=9b044e4a8446b9310b3fc34798d26ae2&oe=61B8F4BD")
        await ctx.channel.purge(limit=1)
        await ctx.channel.send(embed=send)

bot.run("ODk3MTMzODMzNDI0NjA1MjI0.YWRO_Q.8lH1q0zOWnm-nF4V4tnbQbydhN8")
