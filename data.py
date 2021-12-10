"""รวมข้อมูลแยกในหน้านี้ แล้วให้ Function หลังดึงไปใช้มันจะได้ไม่รก"""
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
        albedo = {'his1':'Albedo (ภาษาไทย: อัลเบโด้) เป็นตัวละครชายธาตุหินใช้อาวุธดาบที่สามารถเล่นได้ในเกม Genshin Impact', 
                        'his2':'ไม่ว่าจะ "อัจฉริยะ", "องค์ชายชอล์กขาว" หรือ "หัวหน้าฝ่ายสืบสวน" \
                        เขาไม่สนใจในเรื่องของลาภยศและชื่อเสียงเท่าไหร่ แต่มุ่งเน้นไปที่หัวข้อการวิจัยเท่านั้น ความมั่งคั่งและเส้นสายไม่ใช่เป้าหมายของเขา \
                        สิ่งที่เขาปรารถนาที่จะควบคุมนั้น ก็คือความรู้อันไม่มีที่สิ้นสุด ซึ่งซ่อนอยู่ในจิตใจของมนุษย์มาตั้งแต่สมัยโบราณจนถึงปัจจุบัน',
                        'stat':['13,226', '251', '876', '28.8%', '(Geo DMG Bonus)'],
                        'ascen':'**[✦-----]**:20,000 Mora, Prithiva Topaz Sliver x1, Cecilia x3, Divining Scroll x3\n \
                        **[✦✦----]**:40,000 Mora, Prithiva Topaz Fragment x3, Basalt Pilar x2, Cecilia x10, Divining Scroll x15\n \
                        **[✦✦✦---]**:60,000 Mora, Prithiva Topaz Fragment x6, Basalt Pilar x4, Cecilia x20, Sealed Scroll x12\n \
                        **[✦✦✦✦--]**:80,000 Mora, Prithiva Topaz Chunk x3, Basalt Pilar x8, Cecilia x30, Sealed Scroll x18\n \
                        **[✦✦✦✦✦-]**:100,000 Mora, Prithiva Topaz Chunk x6, Basalt Pilar x12, Cecilia x45, Forbidden Curse Scroll x12\n \
                        **[✦✦✦✦✦✦]**:120,000 Mora, Prithiva Topaz Gemstone x6, Basalt Pilar x20, Cecilia x60, Forbidden Curse Scroll x24',
                        'thum':'https://static.wikia.nocookie.net/genshin-impact/images/0/00/Character_Albedo_Thumb.png/revision/latest/scale-to-width-down/50?cb=20210515115757&path-prefix=th', 'star':'[★★★★★]'}
        return albedo
    elif name.lower() == "aloy":
        aloy = {'his1':'Aloy เป็นนางเอกจากเกม Horizon Zero Dawn ถูกสร้างขึ้นมาเป็นตัวละครข้ามเกมและโปรเจ็กต์ประสานงานระหว่างสตูดิโอ Guerrilla Games และ miHoYo','his2':'',
                        'stat':['10,899', '234', '676', '28.8%', '(Cryo DMG Bonus)'],
                        'ascen':'**[✦-----]**:20,000 Mora, Shivada Jade Sliver x1, Crystal Marrow x3, Spectral Husk x3\n \
                        **[✦✦----]**:40,000 Mora, Shivada Jade Fragment x3, Crystalline Bloom x2, Crystal Marrow x10, Spectral Husk x15\n \
                        **[✦✦✦---]**:60,000 Mora, Shivada Jade Fragment x6, Crystalline Bloom x4, Crystal Marrow x20, Spectral Heart x12\n \
                        **[✦✦✦✦--]**:80,000 Mora, Shivada Jade Chunk x3, Crystalline Bloom x8, Crystal Marrow x30, Spectral Heart x18\n \
                        **[✦✦✦✦✦-]**:100,000 Mora, Shivada Jade Chunk x6, Crystalline Bloom x12, Crystal Marrow x45, Spectral Nucleus x12\n \
                        **[✦✦✦✦✦✦]**:120,000 Mora, Shivada Jade Gemstone x6, Crystalline Bloom x20, Crystal Marrow x60, Spectral Nucleus x24',\
                        'thum':'https://static.wikia.nocookie.net/genshin-impact/images/6/6a/Character_Aloy_Thumb.png/revision/latest/scale-to-width-down/50?cb=20210902150457&path-prefix=th', 'star':'[★★★★★]'}
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


