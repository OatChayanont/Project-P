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

def dungeon_list(day): #เลขด้านหน้าคือ Emoji รูปตัวละครแต่ละตัว โดยอัพ  Emoji ลงใน Server Discord ว่างๆแล้วก็พิมพ์ \:emoji: เพื่อเอา ID มาใส่
    if day == 0 or day == 3:
        dun = ["Monday", ["Forsaken Rift", "Freedom", ["<:aloy:910108780954517514> Aloy", "<:amber:910108707080245248> Amber", 
                "<:barbara:910108780585418782> Barbara", "<:diona:910108780426051626> Diona", "<:klee:910108780941950976> Klee", 
                "<:sucrose:910108882188255322> Sucrose", "<:tartaglia:910108882553163836> Tartaglia", "<:lumine:910114534289731634> Traveler[Anemo]", 
                "<:aether:910114478488690698> Traveler[Geo]"]],
                ["Taishan Mansion", "Prosperity", ["<:keqing:910108780686090241> Keqing", "<:ningguang:910108881940795423> Ningguang", 
                "<:qiqi:910108882129526815> Qiqi", "<:aether:910114478488690698> Traveler[Geo]", "<:xiao:910108882129547314> Xiao"]],
                ["Violet Court", "Transience", ["<:kokomi:910108780925161503> Kokomi", "<:thoma:910108881995321395> Thoma", 
                "<:lumine:910114534289731634> Traveler[Electro]", "<:yoimiya:910108882213404672> Yoimiya"]]]
        if day == 3:
            dun[0] = "Thursday"
    elif day == 1 or day == 4:
        dun = ["Tuesday", ["Forsaken Rift", "Resistance", ["<:bennett:910108780618977290> Bennett", "<:diluc:910108780610596894> Diluc", 
                "<:eula:910108780631588956> Eula", "<:jean:910107170031431690> Jean", "<:mona:910108882137931776> Mona", 
                "<:noelle:910108882246971432> Noelle", "<:razors:910108881919807520> Razor", "<:lumine:910114534289731634> Traveler[Anemo]", 
                "<:aether:910114478488690698> Traveler[Geo]"]],
                ["Taishan Mansion", "Diligence", ["<:chongyun:910108780593811496> Chongyun", "<:ganyu:910108781428506676> Ganyu", 
                "<:hutao:910108780291850274> Hu Tao", "<:kazuha:910108780388298793> Kazuha", "<:aether:910114478488690698> Traveler[Geo]", 
                "<:xiangling:910108881798189067> Xiangling"]],
                ["Violet Court", "Elegance", ["<:ayaka:910108780660924466> Ayaka", "<:sara:910108882351833138> Kujou Sara", 
                "<:lumine:910114534289731634> Traveler[Electro]"]]]
        if day == 4:
            dun[0] = "Friday"
    elif day == 2 or day == 5:
        dun = ["Wednesday", ["Forsaken Rift", "Ballad", ["<:albedo:910108780442812457> Albedo", "<:venti:910108882196627496> Venti", 
                "<:fischl:910108780598030347> Fischl", "<:kaeya:910108780652539924> Kaeya", "<:lisa:910108780619001856> Lisa", 
                "<:rosaria:910108882100183051> Rosaria", "<:lumine:910114534289731634> Traveler[Anemo]", "<:aether:910114478488690698> Traveler[Geo]"]],
                ["Taishan Mansion", "Gold", ["<:zhongli:910108882196627526> Zhongli", "<:beidou:910108780627390494> Beidou", 
                "<:xingqiu:910108882142126130> Xingqiu", "<:xinyan:910108881907253260> Xinyan", "<:aether:910114478488690698> Traveler[Geo]", 
                "<:yanfei:910108882188271626> Yanfei"]],
                ["Violet Court", "Elegance", ["<:raiden:910108882175660063> Raiden Shogun", "<:sayu:910108881882083339> Sayu", 
                "<:lumine:910114534289731634> Traveler[Electro]"]]]
        if day == 5:
            dun[0] = "Saturday"
    elif day == 6:
        dun = ["Sunday", ["All Dungeon is open", "All Meterial", ["All Character"]]]
    return dun

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
    min_left_all = resin_left*8
    min_left = min_left_all%60
    hour_left = min_left_all//60
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

###list char###
def character_info_list(name):
    if name.lower() == "list":
        charlist = ["<:albedo:910108780442812457> **[5★]** Albedo", "<:aloy:910108780954517514> **[5★]** Aloy", "<:amber:910108707080245248> **[4★]** Amber", 
                    "<:barbara:910108780585418782> **[4★]** Barbara", "<:beidou:910108780627390494> **[4★]** Beidou", "<:bennett:910108780618977290> **[4★]** Bennett",
                    "<:chongyun:910108780593811496> **[4★]** Chongyun", "<:diluc:910108780610596894> **[5★]** Diluc", "<:diona:910108780426051626> **[4★]** Diona",
                    "<:eula:910108780631588956> **[5★]** Eula", "<:fischl:910108780598030347> **[4★]** Fischl", "<:ganyu:910108781428506676> **[5★]** Ganyu",
                    "<:hutao:910108780291850274> **[5★]** Hu Tao", "<:jean:910107170031431690> **[5★]** Jean", "<:kazuha:910108780388298793> **[5★]** Kaedehara Kazuha",
                    "<:kaeya:910108780652539924> **[4★]** Kaeya", "<:ayaka:910108780660924466> **[5★]** Kamisato Ayaka", "<:keqing:910108780686090241> **[5★]** Keqing",
                    "<:klee:910108780941950976> **[5★]** Klee", "<:sara:910108882351833138> **[4★]** Kujou Sara", "<:lisa:910108780619001856> **[4★]** Lisa", 
                    "<:mona:910108882137931776> **[5★]** Mona", "<:ningguang:910108881940795423> **[4★]** Ningguang", "<:noelle:910108882246971432> **[4★]** Noelle",
                    "<:qiqi:910108882129526815> **[5★]** Qiqi", "<:raiden:910108882175660063> **[5★]** Raiden Shogun", "<:razors:910108881919807520> **[4★]** Razor", 
                    "<:rosaria:910108882100183051> **[4★]** Rosaria", "<:kokomi:910108780925161503> **[5★]** Sangonomiya Kokomi", "<:sayu:910108881882083339> **[4★]** Sayu",
                    "<:sucrose:910108882188255322> **[4★]** Sucrose", "<:tartaglia:910108882553163836> **[5★]** Tartaglia", "<:thoma:910108881995321395> **[4★]** Thoma",
                    "<:lumine:910114534289731634><:aether:910114478488690698>**[5★]** Traveler",  "<:venti:910108882196627496> **[5★]** Venti", "<:xiangling:910108881798189067> **[4★]** Xiangling",
                    "<:xiao:910108882129547314> **[5★]** Xiao", "<:xingqiu:910108882142126130> **[4★]** Xingqiu", "<:xinyan:910108881907253260> **[4★]** Xinyan",
                    "<:yanfei:910108882188271626> **[4★]** Yanfei", "<:yoimiya:910108882213404672> **[5★]** Yoimiya", "<:zhongli:910108882196627526> **[5★]** Zhongli"]
        return charlist
    elif name.lower() == "albedo":
        albedo = ['Albedo - นักเล่นแร่แปรธาตุที่ตอนนี้ตั้งรกรากอยู่ใน Mondstadt และทำงานให้กับกองอัศวินแห่ง Favonius\nไม่ว่าจะ "อัจฉริยะ", \
                    "องค์ชายชอล์กขาว" หรือ "หัวหน้าฝ่ายสืบสวน" \
                    เขาไม่สนใจในเรื่องของลาภยศและชื่อเสียงเท่าไหร่ แต่มุ่งเน้นไปที่หัวข้อการวิจัยเท่านั้น ความมั่งคั่งและเส้นสายไม่ใช่เป้าหมายของเขา \
                    สิ่งที่เขาปรารถนาที่จะควบคุมนั้น ก็คือความรู้อันไม่มีที่สิ้นสุด ซึ่งซ่อนอยู่ในจิตใจของมนุษย์มาตั้งแต่สมัยโบราณจนถึงปัจจุบัน',
                    ['13,226', '251', '876', '28.8%', '(Geo DMG Bonus)'],
                    '**[✦-----]**:20,000 Mora, Prithiva Topaz Sliver x1, Cecilia x3, Divining Scroll x3\n \
                    **[✦✦----]**:40,000 Mora, Prithiva Topaz Fragment x3, Basalt Pilar x2, Cecilia x10, Divining Scroll x15\n \
                    **[✦✦✦---]**:60,000 Mora, Prithiva Topaz Fragment x6, Basalt Pilar x4, Cecilia x20, Sealed Scroll x12\n \
                    **[✦✦✦✦--]**:80,000 Mora, Prithiva Topaz Chunk x3, Basalt Pilar x8, Cecilia x30, Sealed Scroll x18\n \
                    **[✦✦✦✦✦-]**:100,000 Mora, Prithiva Topaz Chunk x6, Basalt Pilar x12, Cecilia x45, Forbidden Curse Scroll x12\n \
                    **[✦✦✦✦✦✦]**:120,000 Mora, Prithiva Topaz Gemstone x6, Basalt Pilar x20, Cecilia x60, Forbidden Curse Scroll x24',
                    'https://static.wikia.nocookie.net/genshin-impact/images/0/00/Character_Albedo_Thumb.png/revision/latest/scale-to-width-down/50?cb=20210515115757&path-prefix=th', '[★★★★★]']
        return albedo
    elif name.lower() == "aloy":
        aloy = [['Aloy เป็นนางเอกจากเกม Horizon Zero Dawn ถูกสร้างขึ้นมาเป็นตัวละครข้ามเกมและโปรเจ็กต์ประสานงานระหว่างสตูดิโอ Guerrilla Games และ miHoYo'],
                    ['10,899', '234', '676', '28.8%', '(Cryo DMG Bonus)'],
                    '**[✦-----]**:20,000 Mora, Shivada Jade Sliver x1, Crystal Marrow x3, Spectral Husk x3\n \
                    **[✦✦----]**:40,000 Mora, Shivada Jade Fragment x3, Crystalline Bloom x2, Crystal Marrow x10, Spectral Husk x15\n \
                    **[✦✦✦---]**:60,000 Mora, Shivada Jade Fragment x6, Crystalline Bloom x4, Crystal Marrow x20, Spectral Heart x12\n \
                    **[✦✦✦✦--]**:80,000 Mora, Shivada Jade Chunk x3, Crystalline Bloom x8, Crystal Marrow x30, Spectral Heart x18\n \
                    **[✦✦✦✦✦-]**:100,000 Mora, Shivada Jade Chunk x6, Crystalline Bloom x12, Crystal Marrow x45, Spectral Nucleus x12\n \
                    **[✦✦✦✦✦✦]**:120,000 Mora, Shivada Jade Gemstone x6, Crystalline Bloom x20, Crystal Marrow x60, Spectral Nucleus x24',\
                    'https://static.wikia.nocookie.net/genshin-impact/images/6/6a/Character_Aloy_Thumb.png/revision/latest/scale-to-width-down/50?cb=20210902150457&path-prefix=th', '[★★★★★]']
        return aloy
    elif name.lower() == "amber":
        amber = [['Amber (ภาษาไทย: แอมเบอร์) เป็นตัวละครหญิงธาตุไฟใช้อาวุธธนูที่สามารถเล่นได้ใน Genshin Impact',
                    'สาวน้อยผู้สดใสและซื่อตรงและหนึ่งในพลคุ้มกันของกองอัศวินแห่ง Favonius เธอเป็นยอดนักร่อนเวหา และยังเป็น "แชมปันักร่อนเวหา" \
                    ของเมือง Monstadt ที่จัดขึ้นทุกปิติดต่อกันถึงสามสมัยในฐานะดาวรุ่งของกองอัศวินแห่ง Favonius วันนี้ Amber ก็ยังคงพร้อมรับภารกิจท้าทายอยู่เสมอ'],
                    ['9,461', '223', '601', '24.0%', '(ATK Bonus)'],\
                    '**[✦-----]**:20,000 Mora, Agnidus Agate Sliver x1, Small Lamp Grass x3, Firm Arrowhead x3\n \
                    **[✦✦----]**:40,000 Mora, Agnidus Agate Fragment x3, Everflame Seed x2, Small Lamp Grass x10, Firm Arrowhead x15\n \
                    **[✦✦✦---]**:60,000 Mora, Agnidus Agate Fragment x6, Everflame Seed x4, Small Lamp Grass x20, Sharp Arrowhead x12\n \
                    **[✦✦✦✦--]**:80,000 Mora, Agnidus Agate Chunk x3, Everflame Seed x8, Small Lamp Grass x30, Sharp Arrowhead x18\n \
                    **[✦✦✦✦✦-]**:100,000 Mora, Agnidus Agate Chunk x6, Everflame Seed x12, Small Lamp Grass x45, Weathered Arrowhead x12\n \
                    **[✦✦✦✦✦✦]**:120,000 Mora, Agnidus Agate Gemstone x6, Everflame Seed x20, Small Lamp Grass x60, Weathered Arrowhead x24',
                    'https://static.wikia.nocookie.net/genshin-impact/images/c/c6/Character_Amber_Thumb.png/revision/latest/scale-to-width-down/50?cb=20210515115827&path-prefix=th', '[★★★★]']
        return amber
    elif name.lower() == "barbara":
        barbara = [['Barbara (ภาษาไทย: บาร์บาร่า) เป็นตัวละครหญิงธาตุน้ำใช้สื่อเวทที่เล่นได้ในเกม Genshin Impact',
                    'Barbara เป็นผู้แสวงบุญแห่งโบสถ์ Favonius และเป็นดาราจรัสแสงของ Monstadt ชาวเมืองจะคุ้นชินกับนักดนตรีพเนจรมากกว่าดารา แต่ไม่ว่าอย่างไรพวกเขาก็รัก Barbara อย่างไม่ต้องสงสัย "ฉันมีวันนี้ได้เพราะจิตวิญญาณของเมืองแห่งอิสระนี้" Barbara พูดถึงความเป็นที่นิยมของเธอ'],\
                    ['9,787', '159', '669', '24.0%', '(HP Bonus)'],\
                    '**[✦-----]**:20,000 Mora, Varunada Lazurite Sliver x1, Philanemo Mushroom x3, Divining Scroll x3\n \
                    **[✦✦----]**:40,000 Mora, Varunada Lazurite Fragment x3, Cleansing Heart x2, Philanemo Mushroom x10, Divining Scroll x15\n \
                    **[✦✦✦---]**:60,000 Mora, Varunada Lazurite Fragment x6, Cleansing Heart x4, Philanemo Mushroom x20, Sealed Scroll x12\n \
                    **[✦✦✦✦--]**:80,000 Mora, Varunada Lazurite Chunk x3, Cleansing Heart x8, Philanemo Mushroom x30, Sealed Scroll x18\n \
                    **[✦✦✦✦✦-]**:100,000 Mora, Varunada Lazurite Chunk x6, Cleansing Heart x12, Philanemo Mushroom x45, Forbidden Curse Scroll x12\n \
                    **[✦✦✦✦✦✦]**:120,000 Mora, Varunada Lazurite Gemstone x6, Cleansing Heart x20, Philanemo Mushroom x60, Forbidden Curse Scroll x24',\
                    'https://static.wikia.nocookie.net/genshin-impact/images/7/72/Character_Barbara_Thumb.png/revision/latest/scale-to-width-down/50?cb=20210515121106&path-prefix=th', '[★★★★]']
        return barbara
    elif name.lower() == "beidou":
        beidou = [['Beidou (ภาษาจีน: 北斗 Běidǒu, "กระบวยใหญ่"; ภาษาไทย: เป๋ยโต่ว) เป็นตัวละครหญิงธาตุไฟฟ้าใช้อาวุธดาบใหญ่ที่สามารถเล่นได้ในเกม Genshin Impact',
                    'กัปตันเรือแห่งกองทัพเรือ Cruxอันเลื่องชื่อ นอกไปจากชื่อเสียงในการนำกองเรือและพละกำลังอันน่าเกรงขามแล้ว เป๋ยโต่วยังเป็นที่กล่าวขานในหมู่ชาวหลีเยว่ว่าไม่เกรงกลัวเศรษฐินีหนิงกวงผู้เป็นเทียนเฉวียนแห่งเจ็ดดารา นิสัยที่คู่กรณีไม่ติดใจ แต่ก็รำคาญเป็นบางที'],\
                    ['13,050', '225', '648', '24.0%', '(Electro DMG Bonus)'],\
                    '**[✦-----]**:20,000 Mora, Vajrada Amethyst Sliver x1, Noctilucous Jade x3, Treasure Hoarder Insignia x3\n \
                    **[✦✦----]**:40,000 Mora, Vajrada Amethyst Fragment x3, Lightning Prism x2, Noctilucous Jade x10, Treasure Hoarder Insignia x15\n \
                    **[✦✦✦---]**:60,000 Mora, Vajrada Amethyst Fragment x6, Lightning Prism x4, Noctilucous Jade x20, Silver Raven Insignia x12\n \
                    **[✦✦✦✦--]**:80,000 Mora, Vajrada Amethyst Chunk x3, Lightning Prism x8, Noctilucous Jade x30, Silver Raven Insignia x18\n \
                    **[✦✦✦✦✦-]**:100,000 Mora, Vajrada Amethyst Chunk x6, Lightning Prism x12, Noctilucous Jade x45, Golden Raven Insignia x12\n \
                    **[✦✦✦✦✦✦]**:120,000 Mora, Vajrada Amethyst Gemstone x6, Lightning Prism x20, Noctilucous Jade x60, Golden Raven Insignia x24',\
                    'https://static.wikia.nocookie.net/genshin-impact/images/6/61/Character_Beidou_Thumb.png/revision/latest/scale-to-width-down/50?cb=20210515121112&path-prefix=th', '[★★★★]']
        return beidou
    elif name.lower() == "bennett":
        bennett = [['Bennett (ภาษาไทย: เบนเน็ตต์) เป็นตัวละครชายธาตุไฟใช้อาวุธดาบที่สามารถเล่นได้ใน Genshin Impact',
                    'เด็กผู้กำพร้าตั้งแต่ทารกก่อนจะถูกพบโดยนักผจญภัยอาวุโส และเติบโตมาภายในกิลด์นักผจญภัยโดยมีนามว่าเบนเน็ตต์ และเป็นสมาชิกเพียงหนึ่งเดียวของ "กลุ่มนักผจญภัยของ Benny" ในขณะที่คนอื่น ๆ ลาออกจากทีมไปจนหมดหลังจากประสบความโชคร้ายที่ตามติดเขามาโดยตลอด'],\
                    ['12,397', '191', '191', '26.7%', '(Energy Recharge)'],\
                    '**[✦-----]**:20,000 Mora, Agnidus Agate Sliver x1, Windwheel Aster x3, Treasure Hoarder Insignia x3\n \
                    **[✦✦----]**:40,000 Mora, Agnidus Agate Fragment x3, Everflame Seed x2, Windwheel Aster x10, Treasure Hoarder Insignia x15\n \
                    **[✦✦✦---]**:60,000 Mora, Agnidus Agate Fragment x6, Everflame Seed x4, Windwheel Aster x20, Silver Raven Insignia x12\n \
                    **[✦✦✦✦--]**:80,000 Mora, Agnidus Agate Chunk x3, Everflame Seed x8, Windwheel Aster x30, Silver Raven Insignia x18\n \
                    **[✦✦✦✦✦-]**:100,000 Mora, Agnidus Agate Chunk x6, Everflame Seed x12, Windwheel Aster x45, Golden Raven Insignia x12\n \
                    **[✦✦✦✦✦✦]**:120,000 Mora, Agnidus Agate Gemstone x6, Everflame Seed x20, Windwheel Aster x60, Golden Raven Insignia x24',\
                    'https://static.wikia.nocookie.net/genshin-impact/images/7/7b/Character_Bennett_Thumb.png/revision/latest/scale-to-width-down/50?cb=20210515121202&path-prefix=th', '[★★★★]']
        return bennett
    elif name.lower() == "choungyun":
        choungyun = [['Chongyun (ภาษาจีน: 重云 Chóngyún; ภาษาไทย: ฉงอวิ๋น) เป็นตัวละครชายธาตุน้ำแข็งใช้อาวุธดาบใหญ่ที่สามารถเล่นได้ใน Genshin Impact',
                    'นักปราบปีศาจผู้ใช้ Liyue เป็นศูนย์กลางและทำการปราบปีศาจไปทั่วทุกแห่งหน ในฐานะที่เป็นทายาทของตระกูลนักปราบปีศาจ เขาจึงมีความสามารถพิเศษนี้มาตั้งแต่เด็ก— ทว่าความสามารถพิเศษนี้เขาไม่ได้ร่ำเรียนมาจากอาจารย์ท่านไหน แต่เป็นความสามารถที่มีมาตั้งแต่เกิด "ร่างกายแห่งหยางบริสุทธิ์'],\
                    ['12,397', '191', '191', '26.7%', '(Energy Recharge)'],\
                    '**[✦-----]**:20,000 Mora, Shivada Jade Sliver x1, Cor Lapis x3, Damaged Mask x3\n \
                    **[✦✦----]**:40,000 Mora, Shivada Jade Fragment x3, Hoarfrost Core x2, Cor Lapis x10, Damaged Mask x15\n \
                    **[✦✦✦---]**:60,000 Mora, Shivada Jade Fragment x6, Hoarfrost Core x4, Cor Lapis x20, Stained Mask x12\n \
                    **[✦✦✦✦--]**:80,000 Mora, Shivada Jade Chunk x3, Hoarfrost Core x8, Cor Lapis x30, Stained Mask x18\n \
                    **[✦✦✦✦✦-]**:100,000 Mora, Shivada Jade Chunk x6, Hoarfrost Core x12, Cor Lapis x45, Ominous Mask x12\n \
                    **[✦✦✦✦✦✦]**:120,000 Mora, Shivada Jade Gemstone x6, Hoarfrost Core x20, Cor Lapis x60, Ominous Mask x24',\
                    'https://static.wikia.nocookie.net/genshin-impact/images/6/68/Character_Chongyun_Thumb.png/revision/latest/scale-to-width-down/50?cb=20210515121158&path-prefix=th', '[★★★★]']
        return choungyun
###list char###

@bot.command()
async def char(ctx, *, name):
    if name != "list":
        character_info = character_info_list(name)
        send = discord.Embed(title="Overview", description="", colour=0xb24cd8)
        send.set_thumbnail(url=character_info[3])
        send.add_field(name="{1} {0}".format(name.capitalize(), character_info[4]), value="{0}".format(character_info[0]), inline=False)
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
        
@bot.command()
async def men(ctx):
    text = discord.Embed(title="Test {0}" .format(ctx.author.mention), description="Test")
    await ctx.channel.send(ctx.author.mention)
    await ctx.channel.send(embed=text+ctx.author.mention)

bot.run("ODk3MTMzODMzNDI0NjA1MjI0.YWRO_Q.8lH1q0zOWnm-nF4V4tnbQbydhN8")
