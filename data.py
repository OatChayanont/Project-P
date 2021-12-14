"""รวมข้อมูลแยกในหน้านี้ แล้วให้ Function หลังดึงไปใช้มันจะได้ไม่รก"""
def character_info_list(name):
    if name.lower() == "list":
        charlist = ["<:albedo:910108780442812457> **[5★]** Albedo",
                    "<:aloy:910108780954517514> **[5★]** Aloy",
                    "<:amber:910108707080245248> **[4★]** Amber",
                    "<:barbara:910108780585418782> **[4★]** Barbara",
                    "<:beidou:910108780627390494> **[4★]** Beidou",
                    "<:bennett:910108780618977290> **[4★]** Bennett",
                    "<:chongyun:910108780593811496> **[4★]** Chongyun",
                    "<:diluc:910108780610596894> **[5★]** Diluc",
                    "<:diona:910108780426051626> **[4★]** Diona",
                    "<:eula:910108780631588956> **[5★]** Eula",
                    "<:fischl:910108780598030347> **[4★]** Fischl",
                    "<:ganyu:910108781428506676> **[5★]** Ganyu",
                    "<:hutao:910108780291850274> **[5★]** Hu Tao",
                    "<:jean:910107170031431690> **[5★]** Jean",
                    "<:kazuha:910108780388298793> **[5★]** Kaedehara Kazuha",
                    "<:kaeya:910108780652539924> **[4★]** Kaeya",
                    "<:ayaka:910108780660924466> **[5★]** Kamisato Ayaka",
                    "<:keqing:910108780686090241> **[5★]** Keqing",
                    "<:klee:910108780941950976> **[5★]** Klee",
                    "<:sara:910108882351833138> **[4★]** Kujou Sara",
                    "<:lisa:910108780619001856> **[4★]** Lisa",
                    "<:mona:910108882137931776> **[5★]** Mona",
                    "<:ningguang:910108881940795423> **[4★]** Ningguang",
                    "<:noelle:910108882246971432> **[4★]** Noelle",
                    "<:qiqi:910108882129526815> **[5★]** Qiqi",
                    "<:raiden:910108882175660063> **[5★]** Raiden Shogun",
                    "<:razors:910108881919807520> **[4★]** Razor",
                    "<:rosaria:910108882100183051> **[4★]** Rosaria",
                    "<:kokomi:910108780925161503> **[5★]** Sangonomiya Kokomi",
                    "<:sayu:910108881882083339> **[4★]** Sayu",
                    "<:sucrose:910108882188255322> **[4★]** Sucrose",
                    "<:tartaglia:910108882553163836> **[5★]** Tartaglia",
                    "<:thoma:910108881995321395> **[4★]** Thoma",
                    "<:lumine:910114534289731634><:aether:910114478488690698>**[5★]** Traveler",
                    "<:venti:910108882196627496> **[5★]** Venti",
                    "<:xiangling:910108881798189067> **[4★]** Xiangling",
                    "<:xiao:910108882129547314> **[5★]** Xiao",
                    "<:xingqiu:910108882142126130> **[4★]** Xingqiu",
                    "<:xinyan:910108881907253260> **[4★]** Xinyan",
                    "<:yanfei:910108882188271626> **[4★]** Yanfei",
                    "<:yoimiya:910108882213404672> **[5★]** Yoimiya",
                    "<:zhongli:910108882196627526> **[5★]** Zhongli"]
        for i in range(len(charlist)):
            charlist[i] = "**%d.** " % (i+1) + charlist[i]
        return charlist
    elif name.lower() == "albedo" or name.lower() == "1":
        albedo = {'name':'Albedo', 'his1':'Albedo (ภาษาไทย: อัลเบโด้) เป็นตัวละครชายธาตุหินใช้อาวุธดาบที่สามารถเล่นได้ในเกม Genshin Impact\n\n\
            ไม่ว่าจะ "อัจฉริยะ", "องค์ชายชอล์กขาว" หรือ "หัวหน้าฝ่ายสืบสวน" \
                        เขาไม่สนใจในเรื่องของลาภยศและชื่อเสียงเท่าไหร่ แต่มุ่งเน้นไปที่หัวข้อการวิจัยเท่านั้น ความมั่งคั่งและเส้นสายไม่ใช่เป้าหมายของเขา \
                        สิ่งที่เขาปรารถนาที่จะควบคุมนั้น ก็คือความรู้อันไม่มีที่สิ้นสุด ซึ่งซ่อนอยู่ในจิตใจของมนุษย์มาตั้งแต่สมัยโบราณจนถึงปัจจุบัน',
                        'stat':['13,226', '251', '876', '28.8%', '(Geo DMG Bonus)'],
                        'ascen':'**[✦-----]**:20,000 Mora, Prithiva Topaz Sliver x1, Cecilia x3, Divining Scroll x3\n \
                        **[✦✦----]**:40,000 Mora, Prithiva Topaz Fragment x3, Basalt Pilar x2, Cecilia x10, Divining Scroll x15\n \
                        **[✦✦✦---]**:60,000 Mora, Prithiva Topaz Fragment x6, Basalt Pilar x4, Cecilia x20, Sealed Scroll x12\n \
                        **[✦✦✦✦--]**:80,000 Mora, Prithiva Topaz Chunk x3, Basalt Pilar x8, Cecilia x30, Sealed Scroll x18\n \
                        **[✦✦✦✦✦-]**:100,000 Mora, Prithiva Topaz Chunk x6, Basalt Pilar x12, Cecilia x45, Forbidden Curse Scroll x12\n \
                        **[✦✦✦✦✦✦]**:120,000 Mora, Prithiva Topaz Gemstone x6, Basalt Pilar x20, Cecilia x60, Forbidden Curse Scroll x24',
                        'thum':'https://static.wikia.nocookie.net/genshin-impact/images/0/00/Character_Albedo_Thumb.png/revision/latest/scale-to-width-down/50?cb=20210515115757&path-prefix=th', 'star':'[★★★★★]'
                            ,'detail':['<:swords:909805198048886825> ดาบ', 'Mondstadt', '13 กันยายน', '<:geo:909771888413257769> หิน']}
        return albedo
    elif name.lower() == "aloy" or name.lower() == "2":
        aloy = {'name':'Aloy', 'his1':'Aloy เป็นนางเอกจากเกม Horizon Zero Dawn ถูกสร้างขึ้นมาเป็นตัวละครข้ามเกมและโปรเจ็กต์ประสานงานระหว่างสตูดิโอ Guerrilla Games และ miHoYo',
                        'stat':['10,899', '234', '676', '28.8%', '(Cryo DMG Bonus)'],
                        'ascen':'**[✦-----]**:20,000 Mora, Shivada Jade Sliver x1, Crystal Marrow x3, Spectral Husk x3\n \
                        **[✦✦----]**:40,000 Mora, Shivada Jade Fragment x3, Crystalline Bloom x2, Crystal Marrow x10, Spectral Husk x15\n \
                        **[✦✦✦---]**:60,000 Mora, Shivada Jade Fragment x6, Crystalline Bloom x4, Crystal Marrow x20, Spectral Heart x12\n \
                        **[✦✦✦✦--]**:80,000 Mora, Shivada Jade Chunk x3, Crystalline Bloom x8, Crystal Marrow x30, Spectral Heart x18\n \
                        **[✦✦✦✦✦-]**:100,000 Mora, Shivada Jade Chunk x6, Crystalline Bloom x12, Crystal Marrow x45, Spectral Nucleus x12\n \
                        **[✦✦✦✦✦✦]**:120,000 Mora, Shivada Jade Gemstone x6, Crystalline Bloom x20, Crystal Marrow x60, Spectral Nucleus x24',
                        'thum':'https://static.wikia.nocookie.net/genshin-impact/images/6/6a/Character_Aloy_Thumb.png/revision/latest/scale-to-width-down/50?cb=20210902150457&path-prefix=th', 'star':'[★★★★★]'
                        ,'detail':['<:bows:909806179427942400> ธนู', 'ไม่มี(มาจากเกมอื่น)', '4 เมษายน', '<:cryo:909772269474160650> น้ำแข็ง']}
        return aloy
    elif name.lower() == "amber" or name.lower() == "3":
        amber = {'name':'Amber', 'his1':'Amber (ภาษาไทย: แอมเบอร์) เป็นตัวละครหญิงธาตุไฟใช้อาวุธธนูที่สามารถเล่นได้ใน Genshin Impact\n\n\
            สาวน้อยผู้สดใสและซื่อตรงและหนึ่งในพลคุ้มกันของกองอัศวินแห่ง Favonius เธอเป็นยอดนักร่อนเวหา และยังเป็น "แชมปันักร่อนเวหา" \
                        ของเมือง Monstadt ที่จัดขึ้นทุกปิติดต่อกันถึงสามสมัยในฐานะดาวรุ่งของกองอัศวินแห่ง Favonius วันนี้ Amber ก็ยังคงพร้อมรับภารกิจท้าทายอยู่เสมอ',
                        'stat':['9,461', '223', '601', '24.0%', '(ATK Bonus)'],\
                        'ascen':'**[✦-----]**:20,000 Mora, Agnidus Agate Sliver x1, Small Lamp Grass x3, Firm Arrowhead x3\n \
                        **[✦✦----]**:40,000 Mora, Agnidus Agate Fragment x3, Everflame Seed x2, Small Lamp Grass x10, Firm Arrowhead x15\n \
                        **[✦✦✦---]**:60,000 Mora, Agnidus Agate Fragment x6, Everflame Seed x4, Small Lamp Grass x20, Sharp Arrowhead x12\n \
                        **[✦✦✦✦--]**:80,000 Mora, Agnidus Agate Chunk x3, Everflame Seed x8, Small Lamp Grass x30, Sharp Arrowhead x18\n \
                        **[✦✦✦✦✦-]**:100,000 Mora, Agnidus Agate Chunk x6, Everflame Seed x12, Small Lamp Grass x45, Weathered Arrowhead x12\n \
                        **[✦✦✦✦✦✦]**:120,000 Mora, Agnidus Agate Gemstone x6, Everflame Seed x20, Small Lamp Grass x60, Weathered Arrowhead x24',
                        'thum':'https://static.wikia.nocookie.net/genshin-impact/images/c/c6/Character_Amber_Thumb.png/revision/latest/scale-to-width-down/50?cb=20210515115827&path-prefix=th', 'star':'[★★★★]'
                        ,'detail':['<:bows:909806179427942400> ธนู', 'Mondstadt', '10 สิงหาคม', '<:pyro:909772346922008606> ไฟ']}
        return amber
    elif name.lower() == "barbara" or name.lower() == "4":
        barbara = {'name':'Barbara', 'his1':'Barbara (ภาษาไทย: บาร์บาร่า) เป็นตัวละครหญิงธาตุน้ำใช้สื่อเวทที่เล่นได้ในเกม Genshin Impact\n\n\
            Barbara เป็นผู้แสวงบุญแห่งโบสถ์ Favonius และเป็นดาราจรัสแสงของ Monstadt ชาวเมืองจะคุ้นชินกับนักดนตรีพเนจรมากกว่าดารา แต่ไม่ว่าอย่างไรพวกเขาก็รัก Barbara อย่างไม่ต้องสงสัย "ฉันมีวันนี้ได้เพราะจิตวิญญาณของเมืองแห่งอิสระนี้" Barbara พูดถึงความเป็นที่นิยมของเธอ',\
                        'stat':['9,787', '159', '669', '24.0%', '(HP Bonus)'],\
                        'ascen':'**[✦-----]**:20,000 Mora, Varunada Lazurite Sliver x1, Philanemo Mushroom x3, Divining Scroll x3\n \
                        **[✦✦----]**:40,000 Mora, Varunada Lazurite Fragment x3, Cleansing Heart x2, Philanemo Mushroom x10, Divining Scroll x15\n \
                        **[✦✦✦---]**:60,000 Mora, Varunada Lazurite Fragment x6, Cleansing Heart x4, Philanemo Mushroom x20, Sealed Scroll x12\n \
                        **[✦✦✦✦--]**:80,000 Mora, Varunada Lazurite Chunk x3, Cleansing Heart x8, Philanemo Mushroom x30, Sealed Scroll x18\n \
                        **[✦✦✦✦✦-]**:100,000 Mora, Varunada Lazurite Chunk x6, Cleansing Heart x12, Philanemo Mushroom x45, Forbidden Curse Scroll x12\n \
                        **[✦✦✦✦✦✦]**:120,000 Mora, Varunada Lazurite Gemstone x6, Cleansing Heart x20, Philanemo Mushroom x60, Forbidden Curse Scroll x24',\
                        'thum':'https://static.wikia.nocookie.net/genshin-impact/images/7/72/Character_Barbara_Thumb.png/revision/latest/scale-to-width-down/50?cb=20210515121106&path-prefix=th','star':'[★★★★]'
                        ,'detail':['<:catalysts:909806179616702485> สื่อเวทย์', 'Mondstadt', '10 สิงหาคม', '<:hydro:909772393852071936> น้้ำ']}
        return barbara
    elif name.lower() == "beidou" or name.lower() == "5":
        beidou = {'name':'Beidou', 'his1':'Beidou (ภาษาจีน: 北斗 Běidǒu, "กระบวยใหญ่"; ภาษาไทย: เป๋ยโต่ว) เป็นตัวละครหญิงธาตุไฟฟ้าใช้อาวุธดาบใหญ่ที่สามารถเล่นได้ในเกม Genshin Impact\n\n\
            กัปตันเรือแห่งกองทัพเรือ Cruxอันเลื่องชื่อ นอกไปจากชื่อเสียงในการนำกองเรือและพละกำลังอันน่าเกรงขามแล้ว เป๋ยโต่วยังเป็นที่กล่าวขานในหมู่ชาวหลีเยว่ว่าไม่เกรงกลัวเศรษฐินีหนิงกวงผู้เป็นเทียนเฉวียนแห่งเจ็ดดารา นิสัยที่คู่กรณีไม่ติดใจ แต่ก็รำคาญเป็นบางที',
                        'stat':['13,050', '225', '648', '24.0%', '(Electro DMG Bonus)'],
                        'ascen':'**[✦-----]**:20,000 Mora, Vajrada Amethyst Sliver x1, Noctilucous Jade x3, Treasure Hoarder Insignia x3\n \
                        **[✦✦----]**:40,000 Mora, Vajrada Amethyst Fragment x3, Lightning Prism x2, Noctilucous Jade x10, Treasure Hoarder Insignia x15\n \
                        **[✦✦✦---]**:60,000 Mora, Vajrada Amethyst Fragment x6, Lightning Prism x4, Noctilucous Jade x20, Silver Raven Insignia x12\n \
                        **[✦✦✦✦--]**:80,000 Mora, Vajrada Amethyst Chunk x3, Lightning Prism x8, Noctilucous Jade x30, Silver Raven Insignia x18\n \
                        **[✦✦✦✦✦-]**:100,000 Mora, Vajrada Amethyst Chunk x6, Lightning Prism x12, Noctilucous Jade x45, Golden Raven Insignia x12\n \
                        **[✦✦✦✦✦✦]**:120,000 Mora, Vajrada Amethyst Gemstone x6, Lightning Prism x20, Noctilucous Jade x60, Golden Raven Insignia x24',
                        'thum':'https://static.wikia.nocookie.net/genshin-impact/images/6/61/Character_Beidou_Thumb.png/revision/latest/scale-to-width-down/50?cb=20210515121112&path-prefix=th', 'star':'[★★★★]'
                        ,'detail':['<:claymores:909806179205664810> ดาบใหญ่', 'Liyue', '14 กุมภาพันธ์', '<:electro:909772113970364466> ไฟฟ้า']}
        return beidou
    elif name.lower() == "bennett" or name.lower() == "6":
        bennett = {'name':'Bennett', 'his1':'Bennett (ภาษาไทย: เบนเน็ตต์) เป็นตัวละครชายธาตุไฟใช้อาวุธดาบที่สามารถเล่นได้ใน Genshin Impact\n\n\
            เด็กผู้กำพร้าตั้งแต่ทารกก่อนจะถูกพบโดยนักผจญภัยอาวุโส และเติบโตมาภายในกิลด์นักผจญภัยโดยมีนามว่าเบนเน็ตต์ และเป็นสมาชิกเพียงหนึ่งเดียวของ "กลุ่มนักผจญภัยของ Benny" ในขณะที่คนอื่น ๆ ลาออกจากทีมไปจนหมดหลังจากประสบความโชคร้ายที่ตามติดเขามาโดยตลอด',
                        'stat':['12,397', '191', '191', '26.7%', '(Energy Recharge)'],
                        'ascen':'**[✦-----]**:20,000 Mora, Agnidus Agate Sliver x1, Windwheel Aster x3, Treasure Hoarder Insignia x3\n \
                        **[✦✦----]**:40,000 Mora, Agnidus Agate Fragment x3, Everflame Seed x2, Windwheel Aster x10, Treasure Hoarder Insignia x15\n \
                        **[✦✦✦---]**:60,000 Mora, Agnidus Agate Fragment x6, Everflame Seed x4, Windwheel Aster x20, Silver Raven Insignia x12\n \
                        **[✦✦✦✦--]**:80,000 Mora, Agnidus Agate Chunk x3, Everflame Seed x8, Windwheel Aster x30, Silver Raven Insignia x18\n \
                        **[✦✦✦✦✦-]**:100,000 Mora, Agnidus Agate Chunk x6, Everflame Seed x12, Windwheel Aster x45, Golden Raven Insignia x12\n \
                        **[✦✦✦✦✦✦]**:120,000 Mora, Agnidus Agate Gemstone x6, Everflame Seed x20, Windwheel Aster x60, Golden Raven Insignia x24',
                        'thum':'https://static.wikia.nocookie.net/genshin-impact/images/7/7b/Character_Bennett_Thumb.png/revision/latest/scale-to-width-down/50?cb=20210515121202&path-prefix=th', 'star':'[★★★★]'
                        ,'detail':['<:bows:909806179427942400> ดาบ', 'Mondstadt', '29 กุมภาพันธ์', '<:pyro:909772346922008606> ไฟ']}
        return bennett
    elif name.lower() == "choungyun" or name.lower() == "7":
        choungyun = {'name':'Choungyun', 'his1':'Chongyun (ภาษาจีน: 重云 Chóngyún; ภาษาไทย: ฉงอวิ๋น) เป็นตัวละครชายธาตุน้ำแข็งใช้อาวุธดาบใหญ่ที่สามารถเล่นได้ใน Genshin Impact\n\n\
            นักปราบปีศาจผู้ใช้ Liyue เป็นศูนย์กลางและทำการปราบปีศาจไปทั่วทุกแห่งหน ในฐานะที่เป็นทายาทของตระกูลนักปราบปีศาจ เขาจึงมีความสามารถพิเศษนี้มาตั้งแต่เด็ก— ทว่าความสามารถพิเศษนี้เขาไม่ได้ร่ำเรียนมาจากอาจารย์ท่านไหน แต่เป็นความสามารถที่มีมาตั้งแต่เกิด "ร่างกายแห่งหยางบริสุทธิ์',\
                        'stat':['12,397', '191', '191', '26.7%', '(Energy Recharge)'],
                        'ascen':'**[✦-----]**:20,000 Mora, Shivada Jade Sliver x1, Cor Lapis x3, Damaged Mask x3\n \
                        **[✦✦----]**:40,000 Mora, Shivada Jade Fragment x3, Hoarfrost Core x2, Cor Lapis x10, Damaged Mask x15\n \
                        **[✦✦✦---]**:60,000 Mora, Shivada Jade Fragment x6, Hoarfrost Core x4, Cor Lapis x20, Stained Mask x12\n \
                        **[✦✦✦✦--]**:80,000 Mora, Shivada Jade Chunk x3, Hoarfrost Core x8, Cor Lapis x30, Stained Mask x18\n \
                        **[✦✦✦✦✦-]**:100,000 Mora, Shivada Jade Chunk x6, Hoarfrost Core x12, Cor Lapis x45, Ominous Mask x12\n \
                        **[✦✦✦✦✦✦]**:120,000 Mora, Shivada Jade Gemstone x6, Hoarfrost Core x20, Cor Lapis x60, Ominous Mask x24',
                        'thum':'https://static.wikia.nocookie.net/genshin-impact/images/6/68/Character_Chongyun_Thumb.png/revision/latest/scale-to-width-down/50?cb=20210515121158&path-prefix=th', 'star':'[★★★★]'
                        ,'detail':['<:claymores:909806179205664810> ดาบใหญ่', 'Liyue', '7 กันยายน', '<:cryo:909772269474160650> น้ำแข็ง']}
        return choungyun
    elif name.lower() == "diluc" or name.lower() == "8":
        diluc = {'name':'Diluc', 'his1':'Diluc (ภาษาไทย: ดิลุค) เป็นตัวละครชายธาตุไฟใช้อาวุธดาบใหญ่ที่สามารถเล่นได้ในเกม Genshin Impact\n\n\
            อดีตเคยเป็นหนึ่งในอัศวินแห่งฟาโวเนียส ดิลุคลาออกจากทัพอัศวินมาเนื่องจากความผิดหวังในระบบ ปัจจุบันรับมรดก Dawn Winery จากพ่อและผันตัวเป็นพ่อค้าไวน์ในเวลากลางวัน \
                ในขณะที่ในยามวิกาลออกปราบอธรรมและคอยพิทักษ์พลเมือง Mondstadt จากภยันตรายทั้งมวล',
                'stat':['12,981', '335', '784', '19.2%', '(CRIT Rate)'],
                'ascen':'**[✦-----]**:20,000 Mora, Agnidus Agate Sliver x1, Small Lamp Grass x3, Recruit\'s Insignia x3\n \
                        **[✦✦----]**:40,000 Mora, Agnidus Agate Fragment x3, Everflame Seed x2, Small Lamp Grass x10, Recruit\'s Insignia x15\n \
                        **[✦✦✦---]**:60,000 Mora, Agnidus Agate Fragment x6, Everflame Seed x4, Small Lamp Grass x20, Sergeant\'s Insignia x12\n \
                        **[✦✦✦✦--]**:80,000 Mora, Agnidus Agate Chunk x3, Everflame Seed x8, Small Lamp Grass x30, Sergeant\'s Insignia x18\n \
                        **[✦✦✦✦✦-]**:100,000 Mora, Agnidus Agate Chunk x6, Everflame Seed x12, Small Lamp Grass x45, Lieutenant\'s Insignia x12\n \
                        **[✦✦✦✦✦✦]**:120,000 Mora, Agnidus Agate Gemstone x6, Everflame Seed x20, Small Lamp Grass x60, Lieutenant\'s Insignia x24',
                        'thum':'https://static.wikia.nocookie.net/genshin-impact/images/0/02/Character_Diluc_Thumb.png/revision/latest/scale-to-width-down/50?cb=20210515140346&path-prefix=th', 'star':'[★★★★★]'
                        ,'detail':['<:claymores:909806179205664810> ดาบใหญ่', 'Mondstadt', '30 เมษายน', '<:pyro:909772346922008606> ไฟ']}
        return diluc
    elif name.lower() == "diona" or name.lower() == "9":
        diona = {'name':'Diona', 'his1':'Diona (ภาษาไทย: ดีโอน่า) เป็นตัวละครหญิงธาตุน้ำแข็งใช้อาวุธธนูที่สามารถเล่นได้ใน Genshin Impact\n\n\
            บาร์เทนเดอร์ชื่อดังแห่งร้าน Cat\'s Tail ดาวดวงใหม่แห่งวงการเครื่องดื่มของ Mondstadt ผู้ท้าชิงอันแข็งแกร่งในวงการเครื่องดื่มแอลกอฮอล์สาวน้อยที่มีหูแมวและหางแมวที่เกิดใน Springvale ตราบใดที่เครื่องดื่มแก้วนั้นได้รับการปรุงแต่งโดย Diona มันก็จะกลายเป็นเครื่องดื่มรสเลิศที่ไม่อาจจินตนาการได้เสมอ',
                'stat':['9,570', '212', '601', '24.0%', '(Cryo DMG Bonus)'],
                'ascen':'**[✦-----]**:20,000 Mora, Shivada Jade Sliver x1, Calla Lily x3, Firm Arrowhead x3\n \
                        **[✦✦----]**:40,000 Mora, Shivada Jade Fragment x3, Everflame Seed x2, Calla Lily x10, Firm Arrowhead x15\n \
                        **[✦✦✦---]**:60,000 Mora, Shivada Jade Fragment x6, Everflame Seed x4, Calla Lily x20, Sharp Arrowhead x12\n \
                        **[✦✦✦✦--]**:80,000 Mora, Shivada Jade Chunk x3, Everflame Seed x8, Calla Lily x30, Sharp Arrowhead x18\n \
                        **[✦✦✦✦✦-]**:100,000 Mora, Shivada Jade Chunk x6, Everflame Seed x12, Calla Lily x45, Weathered Arrowhead x12\n \
                        **[✦✦✦✦✦✦]**:120,000 Mora, Shivada Jade Gemstone x6, Everflame Seed x20, Calla Lily x60, Weathered Arrowhead x24',
                        'thum':'https://static.wikia.nocookie.net/gensin-impact/images/b/b9/Character_Diona_Thumb.png/revision/latest/scale-to-width-down/50?cb=20210213163131', 'star':'[★★★★]'
                        ,'detail':['<:bows:909806179427942400> ธนู', 'Mondstadt', '18 มกราคม', '<:cryo:909772269474160650> น้ำแข็ง']}
        return diona
    elif name.lower() == "eula" or name.lower() == "10":
        eula = {'name':'Eula', 'his1':'Eula (ภาษาไทย: ยูล่า) เป็นตัวละครหญิงธาตุน้ำแข็งใช้อาวุธดาบใหญ่ที่สามารถเล่นได้ใน Genshin Impact\n\n\
            ยูล่า ลอว์เรนซ์ เป็นทายาทของตระกูลขุนนางลอว์เรนซ์ที่เคยปกครองเมืองมอนด์ชดัตท์ดั่งทรราชย์ใจเหี้ยมเมื่อกาลก่อน \
                ยูล่าเลือกที่จะสมัครเข้าเป็นหนึ่งในอัศวินฟาโวเนียส ศัตรูคู่แค้นที่โค่นล้มตระกูลตัวเอง และไต่เต้าขึ้นมาเป็นถึงหัวหน้ากองสอดแนม \
                    ทำให้ยูล่าถูกตัดขาดจากตระกูลลอว์เรนซ์เนื่องจากทางเดินชีวิตใหม่ และซ้ำร้ายยังถูกเดียดฉันท์จากชาวเมืองเนื่องจากต้นกำเนิดเดิมที่พยายามหนีออกมา',
                'stat':['13,226', '342', '751', '38.4%', '(CRIT Rate)'],
                'ascen':'**[✦-----]**:20,000 Mora, Shivada Jade Sliver x1, Dandelion Seed x3, Damaged Mask x3\n \
                        **[✦✦----]**:40,000 Mora, Shivada Jade Fragment x3, Crystalline Bloom x2, Dandelion Seed x10, Damaged Mask x15\n \
                        **[✦✦✦---]**:60,000 Mora, Shivada Jade Fragment x6, Crystalline Bloom x4, Dandelion Seed x20, Stained Mask x12\n \
                        **[✦✦✦✦--]**:80,000 Mora, Shivada Jade Chunk x3, Crystalline Bloom x8, Dandelion Seed x30, Stained Mask x18\n \
                        **[✦✦✦✦✦-]**:100,000 Mora, Shivada Jade Chunk x6, Crystalline Bloom x12, Dandelion Seed x45, Ominous Mask x12\n \
                        **[✦✦✦✦✦✦]**:120,000 Mora, Shivada Jade Gemstone x6, Crystalline Bloom x20, Dandelion Seed x60, Ominous Mask x24',
                        'thum':'https://static.wikia.nocookie.net/genshin-impact/images/d/d3/Character_Eula_Thumb.png/revision/latest/scale-to-width-down/50?cb=20210523123929&path-prefix=th', 'star':'[★★★★★]'
                        ,'detail':['<:claymores:909806179205664810> ดาบใหญ่', 'Mondstadt', '25 ตุลาคม', '<:cryo:909772269474160650> น้ำแข็ง']}
        return eula
    elif name.lower() == "fischl" or name.lower() == "amy" or name.lower() == "11":
        amy = {'name':'Fischl', 'his1':'Fischl von Luftschloss Narfidort, ชื่อจริง Amy เป็นตัวละครหญิงธาตุไฟฟ้าใช้อาวุธธนูที่สามารถเล่นได้ในเกม Genshin Impact\n\n\
            นักสืบสาวจินตนาการล้นโลกประจำกิลด์นักผจญภัยแห่งมอนด์ชตัดต์ ฟิชเชิลกล่าวว่าตนนั้นมีที่มาโลกอื่นอันมิใช่ Teyvat พร้อมกับอีการาตรีนามว่า ออซ ฟิชเชิลชอบตั้งทฤษฎีแปลกประหลาดที่สุดท้ายแล้วกลับกลายเป็นความจริงอย่างคาดไม่ถึงอยู่บ่อยครั้ง',
                'stat':['9,189', '244', '594', '24.0%', '(ATK Bonus)'],
                'ascen':'**[✦-----]**:20,000 Mora, Vajrada Amethyst Sliver x1, Small Lamp Grass x3, Firm Arrowhead x3\n \
                        **[✦✦----]**:40,000 Mora, Vajrada Amethyst Fragment x3, Lightning Prism x2, Dandelion Seed x10, Firm Arrowhead x15\n \
                        **[✦✦✦---]**:60,000 Mora, Vajrada Amethyst Fragment x6, Lightning Prism x4, Dandelion Seed x20, Sharp Arrowhead x12\n \
                        **[✦✦✦✦--]**:80,000 Mora, Vajrada Amethyst Chunk x3, Lightning Prism x8, Dandelion Seed x30, Sharp Arrowhead x18\n \
                        **[✦✦✦✦✦-]**:100,000 Mora, Vajrada Amethyst Chunk x6, Lightning Prism x12, Dandelion Seed x45, Weathered Arrowhead x12\n \
                        **[✦✦✦✦✦✦]**:120,000 Mora, Vajrada Amethyst Gemstone x6, Lightning Prism x20, Dandelion Seed x60, Weathered Arrowhead x24',
                        'thum':'https://static.wikia.nocookie.net/genshin-impact/images/1/14/Character_Fischl_Thumb.png/revision/latest/scale-to-width-down/50?cb=20210515120053&path-prefix=th', 'star':'[★★★★]'
                        ,'detail':['<:bows:909806179427942400> ธนู', 'Mondstadt', '27 พฤศภาคม', '<:electro:909772113970364466> ไฟฟ้า']}
        return amy
    elif name.lower() == "ganyu" or name.lower() == "12":
        ganyu = {'name':'Ganyu', 'his1':'Eula (ภาษาไทย: ยูล่า) เป็นตัวละครหญิงธาตุน้ำแข็งใช้อาวุธดาบใหญ่ที่สามารถเล่นได้ใน Genshin Impact\n\n\
            ยูล่า ลอว์เรนซ์ เป็นทายาทของตระกูลขุนนางลอว์เรนซ์ที่เคยปกครองเมืองมอนด์ชดัตท์ดั่งทรราชย์ใจเหี้ยมเมื่อกาลก่อน \
                ยูล่าเลือกที่จะสมัครเข้าเป็นหนึ่งในอัศวินฟาโวเนียส ศัตรูคู่แค้นที่โค่นล้มตระกูลตัวเอง และไต่เต้าขึ้นมาเป็นถึงหัวหน้ากองสอดแนม \
                    ทำให้ยูล่าถูกตัดขาดจากตระกูลลอว์เรนซ์เนื่องจากทางเดินชีวิตใหม่ และซ้ำร้ายยังถูกเดียดฉันท์จากชาวเมืองเนื่องจากต้นกำเนิดเดิมที่พยายามหนีออกมา',
                'stat':['9,797', '335', '630', '38.4%', '(CRIT DMG)'],
                'ascen':'**[✦-----]**:20,000 Mora, Shivada Jade Sliver x1, Qingxin x3, Whopperflower Nectar x3\n \
                        **[✦✦----]**:40,000 Mora, Shivada Jade Fragment x3, Hoarfrost Core x2, Qingxin x10, Whopperflower Nectar x15\n \
                        **[✦✦✦---]**:60,000 Mora, Shivada Jade Fragment x6, Hoarfrost Core x4, Qingxin x20, Shimmering Nectar x12\n \
                        **[✦✦✦✦--]**:80,000 Mora, Shivada Jade Chunk x3, Hoarfrost Core x8, Qingxin x30, Shimmering Nectar x18\n \
                        **[✦✦✦✦✦-]**:100,000 Mora, Shivada Jade Chunk x6, Hoarfrost Core x12, Qingxin x45, Elemental Nectar x12\n \
                        **[✦✦✦✦✦✦]**:120,000 Mora, Shivada Jade Gemstone x6, Hoarfrost Core x20, Qingxin x60, Elemental Nectar x24',
                        'thum':'https://static.wikia.nocookie.net/genshin-impact/images/0/0a/Character_Ganyu_Thumb.png/revision/latest/scale-to-width-down/50?cb=20210515120051&path-prefix=th', 'star':'[★★★★★]'
                        ,'detail':['<:bows:909806179427942400> ธนู', 'Liyue', '2 ธันวาคม', '<:cryo:909772269474160650> น้ำแข็ง']}
        return ganyu
    elif name.lower() == "hu tao" or name.lower() == "hutao" or name.lower() == "13":
        hutao = {'name':'Hu Tao', 'his1':'Hu Tao (ภาษาจีน: 胡桃 Hú Táo, "วอลนัท"; ภาษาไทย: หู เถา) เป็นตัวละครหญิงธาตุไฟใช้อาวุธหอกที่สามารถเล่นได้ใน Genshin Impact\n\n\
            Hu Tao - หัวหน้า "โถงแห่งการเกิดใหม่ Wangsheng" สมัยที่ 77 เป็นบุคคลสำคัญที่รับผิดชอบพิธีงานศพใน Liyue อุทิศตนเพื่อประกอบพิธีอำลาแด่ผู้คนที่จากไปให้สมบูรณ์ เพื่อรักษาสมดุลระหว่างหยินและหยางของโลก',
                'stat':['15,552', '106', '876', '38.4%', '(CRIT DMG)'],
                'ascen':'**[✦-----]**:20,000 Mora, Agnidus Agate Sliver x1, Silk Flower x3, Whopperflower Nectar x3\n \
                        **[✦✦----]**:40,000 Mora, Agnidus Agate Fragment x3, Juvenile Jade x2, Silk Flower x10, Whopperflower Nectar x15\n \
                        **[✦✦✦---]**:60,000 Mora, Agnidus Agate Fragment x6, Juvenile Jade x4, Silk Flower x20, Shimmering Nectar x12\n \
                        **[✦✦✦✦--]**:80,000 Mora, Agnidus Agate Chunk x3, Juvenile Jade x8, Silk Flower x30, Shimmering Nectar x18\n \
                        **[✦✦✦✦✦-]**:100,000 Mora, Agnidus Agate Chunk x6, Juvenile Jade x12, Silk Flower x45, Elemental Nectar x12\n \
                        **[✦✦✦✦✦✦]**:120,000 Mora, Agnidus Agate Gemstone x6, Juvenile Jade x20, Silk Flower x60, Elemental Nectar x24',
                        'thum':'https://static.wikia.nocookie.net/genshin-impact/images/a/a4/Character_Hu_Tao_Thumb.png/revision/latest/scale-to-width-down/50?cb=20210515120520&path-prefix=th', 'star':'[★★★★★]'
                        ,'detail':['<:polearms:909806179348267069> หอก', 'Liyue', '15 กรกฎาคม', '<:pyro:909772346922008606> ไฟ']}
        return hutao
    elif name.lower() == "jean" or name.lower() == "14":
        jean = {'name':'Jean', 'his1':'Jean (ภาษาไทย: จีน) เป็นตัวละครหญิงธาตุลมใช้อาวุธดาบที่สามารถเล่นได้ในเกม Genshin Impact\n\n\
            พี่สาวของบาบาร่าผู้กำลังดำรงตำแหน่งรักษาการณ์ผู้บัญชาการอัศวินแห่งฟาโวเนียส จีนเป็นคนขยันขันแข็ง มุ่งมั่นในการรักษาสันติสุขให้แก่ประชาชนแห่งเมืองมอนด์ชดัตท์',
                'stat':['14,695', '239', '769', '22.2%', '(Healing Bonus)'],
                'ascen':'**[✦-----]**:20,000 Mora, Vayuda Turquoise Sliver x1, Dandelion Seed x3, Damaged Mask x3\n \
                        **[✦✦----]**:40,000 Mora, Vayuda Turquoise Fragment x3, Hurricane Seed x2, Dandelion Seed x10, Damaged Mask x15\n \
                        **[✦✦✦---]**:60,000 Mora, Vayuda Turquoise Fragment x6, Hurricane Seed x4, Dandelion Seed x20, Stained Mask x12\n \
                        **[✦✦✦✦--]**:80,000 Mora, Vayuda Turquoise Chunk x3, Hurricane Seed x8, Dandelion Seed x30, Stained Mask x18\n \
                        **[✦✦✦✦✦-]**:100,000 Mora, Vayuda Turquoise Chunk x6, Hurricane Seed x12, Dandelion Seed x45, Ominous Mask x12\n \
                        **[✦✦✦✦✦✦]**:120,000 Mora, Vayuda Turquoise Gemstone x6, Hurricane Seed x20, Dandelion Seed x60, Ominous Mask x24',
                        'thum':'https://static.wikia.nocookie.net/genshin-impact/images/8/89/Character_Jean_Thumb.png/revision/latest/scale-to-width-down/50?cb=20210515120531&path-prefix=th', 'star':'[★★★★★]'
                        ,'detail':['<:bows:909806179427942400> ดาบ', 'Mondstadt', '14 มีนาคม', '<:anemo:909772060753018921> ลม']}
        return jean
    elif name.lower() == "kaedehara kazuha" or name.lower() == "kazuha" or name.lower() == "kaedehara" or name.lower() == "15":
        kazuha = {'name':'Kaedehara Kazuha', 'his1':'Kaedehara Kazuha (ภาษาไทย: คาเอเดะฮาระ คาซึฮะ; ภาษาญี่ปุ่น: 楓かえで原はら万かず葉は) เป็นตัวละครชายธาตุลมใช้อาวุธดาบที่สามารถเล่นได้ใน Genshin Impact\n\n\
            เขาเป็นซามูไรพเนจรของตระกูล Kaedehara ที่เคยโด่งดัง, และเป็นลูกเรือชั่วคราวของกองทัพเรือ Crux',
                'stat':['13,348', '297', '807', '115.2', '(Elemental Mastery)'],
                'ascen':'**[✦-----]**:20,000 Mora, Vayuda Turquoise Sliver x1, Sea Ganoderma x3, Treasure Hoarder Insignia x3\n \
                        **[✦✦----]**:40,000 Mora, Vayuda Turquoise Fragment x3, Marionette Core x2, Sea Ganoderma x10, Treasure Hoarder Insignia x15\n \
                        **[✦✦✦---]**:60,000 Mora, Vayuda Turquoise Fragment x6, Marionette Core x4, Sea Ganoderma x20, Silver Raven Insignia x12\n \
                        **[✦✦✦✦--]**:80,000 Mora, Vayuda Turquoise Chunk x3, Marionette Core x8, Sea Ganoderma x30, Silver Raven Insignia x18\n \
                        **[✦✦✦✦✦-]**:100,000 Mora, Vayuda Turquoise Chunk x6, Marionette Core x12, Sea Ganoderma x45, Golden Raven Insignia x12\n \
                        **[✦✦✦✦✦✦]**:120,000 Mora, Vayuda Turquoise Gemstone x6, Marionette Core x20, Sea Ganoderma x60, Golden Raven Insignia x24',
                        'thum':'https://static.wikia.nocookie.net/genshin-impact/images/f/f0/Character_Kaedehara_Kazuha_Thumb.png/revision/latest/scale-to-width-down/50?cb=20210722145202&path-prefix=th', 'star':'[★★★★★]'
                        ,'detail':['<:bows:909806179427942400> ดาบ', 'Inazuma', '29 ตุลาคม', '<:anemo:909772060753018921> ลม']}
        return kazuha
    elif name.lower() == "kaeya" or name.lower() == "16":
        kaeya = {'name':'kaeya', 'his1':'Kaeya (ภาษาไทย: ไคยะ) เป็นตัวละครชายธาตุน้ำแข็งใช้อาวุธดาบที่สามารถเล่นได้ใน Genshin Impact\n\n\
            ในหน่วยอัศวินแห่ง Favonius จะมี Kaeya เป็นหัวหน้าอัศวินที่มีความรับผิดชอบมากที่สุด ไม่ว่าหน้าที่ใดเขาก็ทำให้ลุล่วงได้ทั้งสิ้น เขาเป็นที่นิยมในหมู่ประชาชนของเมือง Monstadt อย่างมาก แต่อัศวินผู้นี้ก็มีความลับที่ซ่อนอยู่เช่นกัน',
                'stat':['11,636', '223', '792', '26.7%', '(Energy Recharge)'],
                'ascen':'**[✦-----]**:20,000 Mora, Shivada Jade Sliver x1, Calla Lily x3, Treasure Hoarder Insignia x3\n \
                        **[✦✦----]**:40,000 Mora, Shivada Jade Fragment x3, Hoarfrost Core x2, Calla Lily x10, Treasure Hoarder Insignia x15\n \
                        **[✦✦✦---]**:60,000 Mora, Shivada Jade Fragment x6, Hoarfrost Core x4, Calla Lily x20, Silver Raven Insignia x12\n \
                        **[✦✦✦✦--]**:80,000 Mora, Shivada Jade Chunk x3, Hoarfrost Core x8, Calla Lily x30, Silver Raven Insignia x18\n \
                        **[✦✦✦✦✦-]**:100,000 Mora, Shivada Jade Chunk x6, Hoarfrost Core x12, Calla Lily x45, Golden Raven Insignia x12\n \
                        **[✦✦✦✦✦✦]**:120,000 Mora, Shivada Jade Gemstone x6, Hoarfrost Core x20, Calla Lily x60, Golden Raven Insignia x24',
                        'thum':'https://static.wikia.nocookie.net/genshin-impact/images/3/33/Character_Kaeya_Thumb.png/revision/latest/scale-to-width-down/50?cb=20210515140405&path-prefix=th', 'star':'[★★★★]'
                        ,'detail':['<:bows:909806179427942400> ดาบ', 'Mondstadt, Khaenri\'ah', '30 พฤศจิกายน', '<:cryo:909772269474160650> น้ำแข็ง']}
        return kaeya
    elif name.lower() == "kamisato ayaka" or name.lower() == "kamisato" or name.lower() == "ayaka" or name.lower() == "17":
        ayaka = {'name':'Kamisato Ayaka', 'his1':'Kaedehara Kazuha (ภาษาไทย: คาเอเดะฮาระ คาซึฮะ; ภาษาญี่ปุ่น: 楓かえで原はら万かず葉は)[Note 1] เป็นตัวละครชายธาตุลมใช้อาวุธดาบที่สามารถเล่นได้ใน Genshin Impact\n\n\
            เขาเป็นซามูไรพเนจรของตระกูล Kaedehara ที่เคยโด่งดัง, และเป็นลูกเรือชั่วคราวของกองทัพเรือ Crux',
                'stat':['12,858', '342', '784', '38.4%', '(CRIT Rate)'],
                'ascen':'**[✦-----]**:20,000 Mora, Shivada Jade Sliver x1, Sakura Bloom x3, Old Handguard x3\n \
                        **[✦✦----]**:40,000 Mora, Shivada Jade Fragment x3, Perpetual Heart x2, Sakura Bloom x10, Old Handguard x15\n \
                        **[✦✦✦---]**:60,000 Mora, Shivada Jade Fragment x6, Perpetual Heart x4, Sakura Bloom x20, Kageuchi Handguard x12\n \
                        **[✦✦✦✦--]**:80,000 Mora, Shivada Jade Chunk x3, Perpetual Heart x8, Sakura Bloom x30, Kageuchi Handguard x18\n \
                        **[✦✦✦✦✦-]**:100,000 Mora, Shivada Jade Chunk x6, Perpetual Heart x12, Sakura Bloom x45, Famed Handguard x12\n \
                        **[✦✦✦✦✦✦]**:120,000 Mora, Shivada Jade Gemstone x6, Perpetual Heart x20, Sakura Bloom x60, Famed Handguard x24',
                        'thum':'https://static.wikia.nocookie.net/genshin-impact/images/f/fd/Character_Kamisato_Ayaka_Thumb.png/revision/latest/scale-to-width-down/50?cb=20210726062342&path-prefix=th', 'star':'[★★★★★]'
                        ,'detail':['<:bows:909806179427942400> ดาบ', 'Inazuma', '28 พฤศจิกายน', '<:cryo:909772269474160650> น้ำแข็ง']}
        return ayaka
    elif name.lower() == "keqing" or name.lower() == "18":
        keq = {'name':'Keqing', 'his1':'Keqing (ภาษาจีน: 刻晴 Kèqíng; ภาษาไทย: เค่อฉิง) เป็นตัวละครหญิงธาตุไฟฟ้าใช้อาวุธดาบที่สามารถเล่นได้ในเกม Genshin Impact\n\n\
            Yuheng ประจำเจ็ดดาราแห่งหลีเยว่ผู้ทำงานตัวเป็นเกลียว เค่อฉิงเป็นหญิงสาวใจอิสระผู้เลือกเส้นทางเดินด้วยพลังและความสามารถที่ตนเองมี ไม่คิดจะปล่อยให้เหล่าทวยเทพกำหนดชะตากรร',
                'stat':['13,103', '323', '799', '38.4%', '(CRIT DMG)'],
                'ascen':'**[✦-----]**:20,000 Mora, Vajrada Amethyst Sliver x1, Cor Lapis x3, Whopperflower Nectar x3\n \
                        **[✦✦----]**:40,000 Mora, Vajrada Amethyst Fragment x3, Perpetual Heart x2, Cor Lapis x10, Whopperflower Nectar x15\n \
                        **[✦✦✦---]**:60,000 Mora, Vajrada Amethyst Fragment x6, Perpetual Heart x4, Cor Lapis x20, Shimmering Nectar x12\n \
                        **[✦✦✦✦--]**:80,000 Mora, Vajrada Amethyst Chunk x3, Perpetual Heart x8, Cor Lapis x30, Shimmering Nectar x18\n \
                        **[✦✦✦✦✦-]**:100,000 Mora, Vajrada Amethyst Chunk x6, Perpetual Heart x12, Cor Lapis x45, Elemental Nectar x12\n \
                        **[✦✦✦✦✦✦]**:120,000 Mora, Vajrada Amethyst Gemstone x6, Perpetual Heart x20, Cor Lapis x60, Elemental Nectar x24',
                        'thum':'https://static.wikia.nocookie.net/genshin-impact/images/0/06/Character_Keqing_Thumb.png/revision/latest/scale-to-width-down/50?cb=20210515120525&path-prefix=th', 'star':'[★★★★★]'
                        ,'detail':['<:bows:909806179427942400> ดาบ', 'Liyue', '20 พฤศจิกายน', '<:electro:909772113970364466> ไฟฟ้า']}
        return keq
    elif name.lower() == "klee" or name.lower() == "19":
        klee = {'name':'Klee', 'his1':'Klee (ภาษาไทย: เคล) เป็นตัวละครหญิงธาตุไฟใช้อาวุธสื่อเวทที่สามารถเล่นได้ใน Genshin Impact\n\n\
            เคล หรืออัศวินผกาเพลิง เป็นบุตรสาวของนักผจญภัยใจกล้านามว่า อลิซ และติดนิสัยพลังงานสูงและความเป็นมือระเบิดไม่ต่างกับผู้เป็นแม่ เคลชื่นชอบการสร้างวัตถุระเบิด \
                ตามมาด้วยการเขวี้ยงวัตถุระเบิดซึ่งมักจะเป็นที่ปวดหัวยิ่งนักให้กับเจ้าสำนักรักษาการณ์จีน ผู้ซึ่งทำหน้าที่เป็นผู้ดูแลจำเป็น',
                'stat':['10,287', '311', '615', '28.8%', '(Pyro DMG Bonus)'],
                'ascen':'**[✦-----]**:20,000 Mora, Agnidus Agate Sliver x1, Philanemo Mushroom x3, Divining Scroll x3\n \
                        **[✦✦----]**:40,000 Mora, Agnidus Agate Fragment x3, Everflame Seed x2, Philanemo Mushroom x10, Divining Scroll x15\n \
                        **[✦✦✦---]**:60,000 Mora, Agnidus Agate Fragment x6, Everflame Seed x4, Philanemo Mushroom x20, Sealed Scroll x12\n \
                        **[✦✦✦✦--]**:80,000 Mora, Agnidus Agate Chunk x3, Everflame Seed x8, Philanemo Mushroom x30, Sealed Scroll x18\n \
                        **[✦✦✦✦✦-]**:100,000 Mora, Agnidus Agate Chunk x6, Everflame Seed x12, Philanemo Mushroom x45, Forbidden Curse Scroll x12\n \
                        **[✦✦✦✦✦✦]**:120,000 Mora, Agnidus Agate Gemstone x6, Everflame Seed x20, Philanemo Mushroom x60, Forbidden Curse Scroll x24',
                        'thum':'https://static.wikia.nocookie.net/genshin-impact/images/c/c3/Character_Klee_Thumb.png/revision/latest/scale-to-width-down/50?cb=20210515120422&path-prefix=th', 'star':'[★★★★★]'
                        ,'detail':['<:catalysts:909806179616702485> สื่อเวทย์', 'Mondstadt', '27 กรกฎาคม', '<:pyro:909772346922008606> ไฟ']}
        return klee
    elif name.lower() == "kujou sara" or name.lower() == "kujou" or name.lower() == "sara" or name.lower() == "20":
        kujo = {'name':'Kujou Sara', 'his1':'Kujou Sara (ภาษาไทย: คุโจ ซาระ; ภาษาญี่ปุ่น: 九く条じょう裟さ羅ら Kujou Sara) คือตัวละครหญิงธาตุไฟฟ้าใช้อาวุธธนูที่สามารถเล่นได้ในเกม Genshin Impact\n\n\
            เท็งงุพันธุ์แท้ผู้เป็นบุตรบุญธรรมจากตระกูลคุโจ และแม่ทัพผู้เด็ดเดี่ยวในพระนางโชกุนอสนีบาตผู้ยึดมั่นในหน้าที่และคำสัตย์เหนือทุกสิ่ง \
                แม่ทัพซาระนำยุทธการด้วยตนเองและพร้อมจะเสี่ยงชีวิตกับไพร่พลกลางสมรภูมิ ทุกที่ ทุกเมื่อ และทุกเวลาที่พระประสงค์ของพระนางโชกุนนำพาไป โดยไร้ซึ่งความเคลือบแคลงแม้เพียงเสี้ยว',\
                        'stat':['9,570', '195', '628', '24.0%', '(ATK Bonus)'],
                        'ascen':'**[✦-----]**:20,000 Mora, Vajrada Amethyst Sliver x1, Dendrobium x3, Damaged Mask x3\n \
                        **[✦✦----]**:40,000 Mora, Vajrada Amethyst Fragment x3, Storm Beads x2, Dendrobium x10, Damaged Mask x15\n \
                        **[✦✦✦---]**:60,000 Mora, Vajrada Amethyst Fragment x6, Storm Beads x4, Dendrobium x20, Stained Mask x12\n \
                        **[✦✦✦✦--]**:80,000 Mora, Vajrada Amethyst Chunk x3, Storm Beads x8, Dendrobium x30, Stained Mask x18\n \
                        **[✦✦✦✦✦-]**:100,000 Mora, Vajrada Amethyst Chunk x6, Storm Beads x12, Dendrobium x45, Ominous Mask x12\n \
                        **[✦✦✦✦✦✦]**:120,000 Mora, Vajrada Amethyst Gemstone x6, Storm Beads x20, Dendrobium x60, Ominous Mask x24',
                        'thum':'https://static.wikia.nocookie.net/genshin-impact/images/9/96/Character_Kujou_Sara_Thumb.png/revision/latest/scale-to-width-down/50?cb=20210902012107&path-prefix=th', 'star':'[★★★★]'
                        ,'detail':['<:bows:909806179427942400> ธนู', 'Inazuma', '14 กรกฎาคม', '<:electro:909772113970364466> ไฟฟ้า']}
        return kujo
    elif name.lower() == "lisa" or name.lower() == "21":
        lisa = {'name':'Lisa', 'his1':'Lisa (ภาษาไทย: ลิซ่า) เป็นตัวละครหญิงธาตุไฟฟ้าใช้อาวุธสื่อเวทที่สามารถเล่นได้ในเกม Genshin Impact\n\n\
            นักเวทย์อดอัจฉริยะผู้เป็นสุดยอดนักปราชญ์ที่เคยจบจากวิทยาลัยสุเมรุมาในระยะเวลา 200 ปี ลิซ่าได้เดินทางกลับมาเมืองมอนด์ชตัดท์เพื่อทำอาชีพเป็นบรรณารักษ์ตัวเล็ก ๆ ให้กับกองอัศวินแห่ง Favonius',\
                        'stat':['9,570', '232', '573', '96', '(Elemental Mastery)'],
                        'ascen':'**[✦-----]**:20,000 Mora, Vajrada Amethyst Sliver x1, Valberry x3, Slime Condensate x3\n \
                        **[✦✦----]**:40,000 Mora, Vajrada Amethyst Fragment x3, Lightning Prism x2, Valberry x10, Slime Condensate x15\n \
                        **[✦✦✦---]**:60,000 Mora, Vajrada Amethyst Fragment x6, Lightning Prism x4, Valberry x20, Slime Secretions x12\n \
                        **[✦✦✦✦--]**:80,000 Mora, Vajrada Amethyst Chunk x3, Lightning Prism x8, Valberry x30, Slime Secretions x18\n \
                        **[✦✦✦✦✦-]**:100,000 Mora, Vajrada Amethyst Chunk x6, Lightning Prism x12, Valberry x45, Slime Concentrate x12\n \
                        **[✦✦✦✦✦✦]**:120,000 Mora, Vajrada Amethyst Gemstone x6, Lightning Prism x20, Valberry x60, Slime Concentrate x24',
                        'thum':'https://static.wikia.nocookie.net/genshin-impact/images/5/51/Character_Lisa_Thumb.png/revision/latest/scale-to-width-down/50?cb=20210515120431&path-prefix=th', 'star':'[★★★★]'
                        ,'detail':['<:catalysts:909806179616702485> สื่อเวทย์', 'Mondstadt', '9 มิถุนายน', '<:electro:909772113970364466> ไฟฟ้า']}
        return lisa
    elif name.lower() == "mona" or name.lower() == "22":
        mona = {'name':'Astrologist Mona Megistus', 'his1':'Astrologist Mona Megistus (ภาษาไทย: โมนา เมจิสตัส) เป็นตัวละครหญิงธาตุน้ำใช้อาวุธสื่อเวทที่สามารถเล่นได้ในเกม Genshin Impact\n\n\
            โหรสาวมากความสามารถและมากความหยิ่งผู้จนตลอดกาล โมนาระหกระเหินมาหาที่อยู่ในเมืองมอนด์ชตัดท์เพื่อหนีโทสะท่านอาจารย์ที่ตัวเองเผลอไปอ่านบันทึกประจำวันเข้า',
                'stat':['10,409', '287', '653', '32.0%', '(Energy Recharge)'],
                'ascen':'**[✦-----]**:20,000 Mora, Varunada Lazurite Sliver x1, Philanemo Mushroom x3, Whopperflower Nectar x3\n \
                        **[✦✦----]**:40,000 Mora, Varunada Lazurite Fragment x3, Cleansing Heart x2, Philanemo Mushroom x10, Whopperflower Nectar x15\n \
                        **[✦✦✦---]**:60,000 Mora, Varunada Lazurite Fragment x6, Cleansing Heart x4, Philanemo Mushroom x20, Shimmering Nectar x12\n \
                        **[✦✦✦✦--]**:80,000 Mora, Varunada Lazurite Chunk x3, Cleansing Heart x8, Philanemo Mushroom x30, Shimmering Nectar x18\n \
                        **[✦✦✦✦✦-]**:100,000 Mora, Varunada Lazurite Chunk x6, Cleansing Heart x12, Philanemo Mushroom x45, Elemental Nectar x12\n \
                        **[✦✦✦✦✦✦]**:120,000 Mora, Varunada Lazurite Gemstone x6, Cleansing Heart x20, Philanemo Mushroom x60, Elemental Nectar x24',
                        'thum':'https://static.wikia.nocookie.net/genshin-impact/images/a/a0/Character_Mona_Thumb.png/revision/latest/scale-to-width-down/50?cb=20210515120940&path-prefix=th', 'star':'[★★★★★]'
                        ,'detail':['<:catalysts:909806179616702485> สื่อเวทย์', 'Mondstadt', '31 สิงหาคม', '<:hydro:909772393852071936> น้้ำ']}
        return mona
    elif name.lower() == "ningguang" or name.lower() == "23":
        ning = {'name':'Ningguang', 'his1':'Ningguang (ภาษาจีน: 凝光 Níngguāng; ภาษาไทย: หนิงกวง) เป็นตัวละครหญิงธาตุหินใช้อาวุธสื่อเวทที่สามารถเล่นได้ในเกม Genshin Impact\n\n\
            เศรษฐินีผู้ทรงอิทธิพลและเทียนเฉวียนในบรรดาเจ็ดดารา มีฐานะทางการเงินอันมั่งคั่งเหนือกว่าผู้ใดใน Teyvat \
                หนิงกวงมีความสำเร็จอันมากมายถึงขั้นที่สามารถก่อสร้างผลงานชิ้นเอกอันมีชื่อว่าอารามหยก อาคารสำนักงานและป้อมปราการลอยฟ้าอันคอยปกปักษ์ท้องนภาเหนือเมืองหลีเยว่',
                'stat':['9,787', '212', '573', '24.0%', '(Geo DMG Bonus)'],
                'ascen':'**[✦-----]**:20,000 Mora, Prithiva Topaz Sliver x1, Glaze Lily x3, Recruit\'s Insignia x3\n \
                        **[✦✦----]**:40,000 Mora, Prithiva Topaz Fragment x3, Basalt Pillar x2, Glaze Lily x10, Recruit\'s Insignia x15\n \
                        **[✦✦✦---]**:60,000 Mora, Prithiva Topaz Fragment x6, Basalt Pillar x4, Glaze Lily x20, Sergeant\'s Insignia x12\n \
                        **[✦✦✦✦--]**:80,000 Mora, Prithiva Topaz Chunk x3, Basalt Pillar x8, Glaze Lily x30, Sergeant\'s Insignia x18\n \
                        **[✦✦✦✦✦-]**:100,000 Mora, Prithiva Topaz Chunk x6, Basalt Pillar x12, Glaze Lily x45, Lieutenant\'s Insignia x12\n \
                        **[✦✦✦✦✦✦]**:120,000 Mora, Prithiva Topaz Gemstone x6, Basalt Pillar x20, Glaze Lily x60, Lieutenant\'s Insignia x24',
                        'thum':'https://static.wikia.nocookie.net/genshin-impact/images/2/2b/Character_Ningguang_Thumb.png/revision/latest/scale-to-width-down/50?cb=20210515120449&path-prefix=th', 'star':'[★★★★★]'
                        ,'detail':['<:catalysts:909806179616702485> สื่อเวทย์', 'Liyue', '26 สิงหาคม', '<:geo:909771888413257769> หิน']}
        return ning
    elif name.lower() == "noelle" or name.lower() == "24":
        noel = {'name':'Noelle', 'his1':'Noelle (ภาษาไทย: โนเอลล์) เป็นตัวละครหญิงธาตุหินใช้อาวุธดาบใหญ่ที่สามารถเล่นได้ในเกม Genshin Impact\n\n\
            อัศวินฝึกหัดจอมทรหดและแม่บ้านผู้ไร้เทียมทานประจำกองอัศวินแห่งฟาโวเนียส โนเอลล์มีความฝันว่าสักวันหนึ่งตนจะได้ขึ้นมาเป็นอัศวินเต็มตัวและช่วยเหลือพลเมืองมอนด์ชตัดต์ให้ดียิ่ง ๆ ขึ้นไป',\
                'stat':['12,071', '191', '799', '30.0%', '(DEF Bonus)'],
                'ascen':'**[✦-----]**:20,000 Mora, Prithiva Topaz Sliver x1, Valberry x3, Damaged Mask x3\n \
                        **[✦✦----]**:40,000 Mora, Prithiva Topaz Fragment x3, Basalt Pillar x2, Valberry x10, Damaged Mask x15\n \
                        **[✦✦✦---]**:60,000 Mora, Prithiva Topaz Fragment x6, Basalt Pillar x4, Valberry x20, Stained Mask x12\n \
                        **[✦✦✦✦--]**:80,000 Mora, Prithiva Topaz Chunk x3, Basalt Pillar x8, Valberry x30, Stained Mask x18\n \
                        **[✦✦✦✦✦-]**:100,000 Mora, Prithiva Topaz Chunk x6, Basalt Pillar x12, Valberry x45, Ominous Mask x12\n \
                        **[✦✦✦✦✦✦]**:120,000 Mora, Prithiva Topaz Gemstone x6, Basalt Pillar x20, Valberry x60, Ominous Mask x24',
                        'thum':'https://static.wikia.nocookie.net/genshin-impact/images/a/ab/Character_Noelle_Thumb.png/revision/latest/scale-to-width-down/50?cb=20210515120454&path-prefix=th', 'star':'[★★★★]'
                        ,'detail':['<:claymores:909806179205664810> ดาบใหญ่', 'Mondstadt', '21 มีนาคม', '<:geo:909771888413257769> หิน']}
        return noel
    elif name.lower() == "qiqi" or name.lower() == "25":
        qiqi = {'name':'Qiqi', 'his1':'Qiqi (ภาษาไทย: ชีชี; ภาษาจีน: 七七 Qīqī, "เจ็ด เจ็ด") เป็นตัวละครหญิงธาตุน้ำแข็งใช้อาวุธดาบที่สามารถเล่นได้ในเกม Genshin Impact\n\n\
            เด็กสาวที่มีเหล่าเซียนชุบชีวิตขึ้นมาเป็นผีดิบ เธอได้ Baizhu เป็นผู้ปกครองและทำงานอยู่กับ Bubu Pharmacy ในท่าเรือ Liyue',
                'stat':['12,368', '287', '922', '22.2%', '(Healing Bonus)'],
                'ascen':'**[✦-----]**:20,000 Mora, Shivada Jade Sliver x1, Violetgrass x3, Divining Scroll x3\n \
                        **[✦✦----]**:40,000 Mora, Shivada Jade Fragment x3, Hoarfrost Core x2, Violetgrass x10, Divining Scroll x15\n \
                        **[✦✦✦---]**:60,000 Mora, Shivada Jade Fragment x6, Hoarfrost Core x4, Violetgrass x20, Sealed Scroll x12\n \
                        **[✦✦✦✦--]**:80,000 Mora, Shivada Jade Chunk x3, Hoarfrost Core x8, Violetgrass x30, Sealed Scroll x18\n \
                        **[✦✦✦✦✦-]**:100,000 Mora, Shivada Jade Chunk x6, Hoarfrost Core x12, Violetgrass x45, Forbidden Curse Scroll x12\n \
                        **[✦✦✦✦✦✦]**:120,000 Mora, Shivada Jade Gemstone x6, Hoarfrost Core x20, Violetgrass x60, Forbidden Curse Scroll x24',
                        'thum':'https://static.wikia.nocookie.net/genshin-impact/images/d/d5/Character_Qiqi_Thumb.png/revision/latest/scale-to-width-down/50?cb=20210515120459&path-prefix=th', 'star':'[★★★★★]'
                        ,'detail':['<:swords:909805198048886825> ดาบ', 'Liyue', '3 มีนาคม', '<:cryo:909772269474160650> น้ำแข็ง']}
        return qiqi
    elif name.lower() == "raiden shogun" or name.lower() == "raiden" or name.lower() == "shogun" or name.lower() == "ei" or name.lower() == "26":
        raiden = {'name':'Raiden Shogun(Raiden Ei)', 'his1':'Raiden Shogun (ภาษาญี่ปุ่น: 雷電将軍 โชกุน ไรเดน) คือตัวละครหญิงธาตุไฟฟ้าใช้อาวุธหอกที่สามารถเล่นได้ในเกม Genshin Impact\n\n\
            พระนางไรเด็น เอย์ ผู้เป็นเทพีเบเอลเซบูลทรงปกครองแผ่นดินอินาสึมะผ่านภาชนะกายหยาบที่เรียกกันว่าพระนางโชกุน \
                ให้หุ่นเชิดอันสร้างจากเทคโนโลยีโบราณบริหารราชการแทนพระนางเอย์ผู้ทรงหลบหนีความอนิจจังไปประทับอยู่ในดินแดนแห่งใจที่บริสุทธิ์ แยกตัวพระนางออกห่างความทุกข์แห่งโลกเข้าสู่วิถีนิรันดร์',
                'stat':['12,907', '337', '789', '32.0%', '(Energy Recharge)'],    
                'ascen':'**[✦-----]**:20,000 Mora, Vajrada Amethyst Sliver x1, Amakumo Fruit x3, Old Handguard x3\n \
                        **[✦✦----]**:40,000 Mora, Vajrada Amethyst Fragment x3, Storm Beads x2, Amakumo Fruit x10, Old Handguard x15\n \
                        **[✦✦✦---]**:60,000 Mora, Vajrada Amethyst Fragment x6, Storm Beads x4, Amakumo Fruit x20, Kageuchi Handguard x12\n \
                        **[✦✦✦✦--]**:80,000 Mora, Vajrada Amethyst Chunk x3, Storm Beads x8, Amakumo Fruit x30, Kageuchi Handguard x18\n \
                        **[✦✦✦✦✦-]**:100,000 Mora, Vajrada Amethyst Chunk x6, Storm Beads x12, Amakumo Fruit x45, Famed Handguard x12\n \
                        **[✦✦✦✦✦✦]**:120,000 Mora, Vajrada Amethyst Gemstone x6, Storm Beads x20, Amakumo Fruit x60, Famed Handguard x24',
                        'thum':'https://static.wikia.nocookie.net/genshin-impact/images/5/52/Character_Raiden_Shogun_Thumb.png/revision/latest/scale-to-width-down/50?cb=20210902012044&path-prefix=th', 'star':'[★★★★★]'
                        ,'detail':['<:polearms:909806179348267069> หอก', 'Inazuma', '26 มิถุนายน', '<:electro:909772113970364466> ไฟฟ้า']}
        return raiden
    elif name.lower() == "razor" or name.lower() == "27":
        razor = {'name':'Razor', 'his1':'Razor (ภาษาไทย: เรเซอร์) เป็นตัวละครชายธาตุไฟฟ้าใช้อาวุธดาบใหญ่ที่สามารถเล่นได้ใน Genshin Impact\n\n\
            Razor ถูกทอดทิ้งตั้งแต่ยังเป็นทารก เขาถูกเลี้ยงดูโดยหมาป่าแห่งทิศเหนือ, แอนเดรียส และฝูงหมาป่าของเขาใน Wolvendom หลังจากมีโอกาสพบกับ Varka \
                ผู้บัญชาการคนปัจจุบันของ กองอัศวินแห่ง Favonius และ อัศวินแห่ง Boreas เขาได้หลอมรวมเข้ากับมนุษย์อย่างช้า ๆ',\
                'stat':['11,962', '234', '751', '30.0%', '(Physical DMG Bonus)'],
                'ascen':'**[✦-----]**:20,000 Mora, Vajrada Amethyst Sliver x1, Wolfhook x3, Damaged Mask x3\n \
                        **[✦✦----]**:40,000 Mora, Vajrada Amethyst Fragment x3, Lightning Prism x2, Wolfhook x10, Damaged Mask x15\n \
                        **[✦✦✦---]**:60,000 Mora, Vajrada Amethyst Fragment x6, Lightning Prism x4, Wolfhook x20, Stained Mask x12\n \
                        **[✦✦✦✦--]**:80,000 Mora, Vajrada Amethyst Chunk x3, Lightning Prism x8, Wolfhook x30, Stained Mask x18\n \
                        **[✦✦✦✦✦-]**:100,000 Mora, Vajrada Amethyst Chunk x6, Lightning Prism x12, Wolfhook x45, Ominous Mask x12\n \
                        **[✦✦✦✦✦✦]**:120,000 Mora, Vajrada Amethyst Gemstone x6, Lightning Prism x20, Wolfhook x60, Ominous Mask x24',
                        'thum':'https://static.wikia.nocookie.net/genshin-impact/images/1/1d/Character_Razor_Thumb.png/revision/latest/scale-to-width-down/50?cb=20210515120504&path-prefix=th', 'star':'[★★★★]'
                        ,'detail':['<:claymores:909806179205664810> ดาบใหญ่', 'Mondstadt', '9 กันยายน', '<:electro:909772113970364466> ไฟฟ้า']}
        return razor
    elif name.lower() == "rosaria" or name.lower() == "28":
        rosa = {'name':'Rosaria', 'his1':'Rosaria (ภาษาไทย: โรซาเรีย) เป็นตัวละครหญิงธาตุน้ำแข็งใช้อาวุธหอกที่สามารถเล่นได้ใน Genshin Impact\n\n\
            Rosaria หนึ่งในซิสเตอร์ของ Favonius Church แห่ง Mondstadtซิสเตอร์ที่นอกจากการแต่งกายแล้ว ไม่มีสิ่งที่ดูเหมือนสมาชิกทางศาสนาเลย ซิสเตอร์ผู้แสนแปลกแยก เย็นชา และเชือดเฉือน หญิงสาวที่คมราวกับใบมีด',
                'stat':['12,289', '240', '710', '24.0%', '(ATK Bonus)'],
                'ascen':'**[✦-----]**:20,000 Mora, Prithiva Topaz Sliver x1, Glaze Lily x3, Recruit\'s Insignia x3\n \
                        **[✦✦----]**:40,000 Mora, Prithiva Topaz Fragment x3, Basalt Pillar x2, Glaze Lily x10, Recruit\'s Insignia x15\n \
                        **[✦✦✦---]**:60,000 Mora, Prithiva Topaz Fragment x6, Basalt Pillar x4, Glaze Lily x20, Sergeant\'s Insignia x12\n \
                        **[✦✦✦✦--]**:80,000 Mora, Prithiva Topaz Chunk x3, Basalt Pillar x8, Glaze Lily x30, Sergeant\'s Insignia x18\n \
                        **[✦✦✦✦✦-]**:100,000 Mora, Prithiva Topaz Chunk x6, Basalt Pillar x12, Glaze Lily x45, Lieutenant\'s Insignia x12\n \
                        **[✦✦✦✦✦✦]**:120,000 Mora, Prithiva Topaz Gemstone x6, Basalt Pillar x20, Glaze Lily x60, Lieutenant\'s Insignia x24',
                        'thum':'https://static.wikia.nocookie.net/genshin-impact/images/f/f6/Character_Rosaria_Thumb.png/revision/latest/scale-to-width-down/50?cb=20210515120554&path-prefix=th', 'star':'[★★★★]'
                        ,'detail':['<:polearms:909806179348267069> หอก', 'Mondstadt', '24 มกราคม', '<:cryo:909772269474160650> น้ำแข็ง']}
        return rosa
    elif name.lower() == "Sangonomiya Kokomi" or name.lower() == "sangonomiya" or name.lower() == "kokomi" or name.lower() == "29":
        kokomi = {'name':'Sangonomiya Kokomi', 'his1':'Sangonomiya Kokomi (ภาษาญี่ปุ่น: 珊さん瑚ご宮のみや心ここ海み) เป็นตัวละครหญิงธาตุน้ำใช้อาวุธสื่อเวทที่สามารถเล่นได้ในเกม Genshin Impact\n\n\
            กุนซือสมองเพชรและนักพรตหญิงศักดิ์สิทธิ์ศูนย์รวมจิตใจชาวบ้านเกาะวาทัตสึมิผู้เป็นทายาทของตระกูลซังโกโนมิยะอันเก่าแก่ \
                โคโคมิคือสุดยอดความหวังสุดท้ายของกลุ่มกบฎในสงครามต่อต้านรัฐบาลโชกุน เด็กสาวตัวเล็ก ๆ ที่ต้องแบกรับภาระความรับผิดชอบอันหนักอึ้งเพื่อค้ำชูความหวังและความสุขของราษฎรชาวเกาะไม่ว่าตนเองจะเหน็ดเหนื่อยเกินอายุเพียงใด',
                'stat':['13,471', '234', '657', '28.8%', '(Hydro DMG Bonus)'],    
                'ascen':'**[✦-----]**:20,000 Mora, Varunada Lazurite Sliver x1, Sango Pearl x3, Spectral Husk x3\n \
                        **[✦✦----]**:40,000 Mora, Varunada Lazurite Fragment x3, Dew of Repudiation x2, Sango Pearl x10, Spectral Husk x15\n \
                        **[✦✦✦---]**:60,000 Mora, Varunada Lazurite Fragment x6, Dew of Repudiation x4, Sango Pearl x20, Spectral Heart x12\n \
                        **[✦✦✦✦--]**:80,000 Mora, Varunada Lazurite Chunk x3, Dew of Repudiation x8, Sango Pearl x30, Spectral Heart x18\n \
                        **[✦✦✦✦✦-]**:100,000 Mora, Varunada Lazurite Chunk x6, Dew of Repudiation x12, Sango Pearl x45, Spectral Nucleus x12\n \
                        **[✦✦✦✦✦✦]**:120,000 Mora, Varunada Lazurite Gemstone x6, Dew of Repudiation x20, Sango Pearl x60, Spectral Nucleus x24',
                        'thum':'https://static.wikia.nocookie.net/genshin-impact/images/c/cc/Character_Sangonomiya_Kokomi_Thumb.png/revision/latest/scale-to-width-down/50?cb=20210921133136&path-prefix=th', 'star':'[★★★★★]'
                        ,'detail':['<:catalysts:909806179616702485> สื่อเวทย์', 'Inazuma', '22 กุมภาพันธ์', '<:hydro:909772393852071936> น้้ำ']}
        return kokomi
    elif name.lower() == "sayu" or name.lower() == "30":
        sayu = {'name':'Sayu', 'his1':'Sayu (ภาษาไทย: ซายุ; ภาษาญี่ปุ่น: 早さ柚ゆ) เป็นตัวละครหญิงธาตุลมใช้อาวุธดาบใหญ่ที่สามารถเล่นได้ในเกม Genshin Impact\n\n\
            นินจาสาวน้อยจากสำนักชูมัตสึบันผู้นอนกินวันกินคืน ซายุเชื่อว่ายิ่งนอนมากจะยิ่งช่วยให้ตัวยืดขึ้น และมักจะใช้ฝีมือวิชานินจาเพื่อหลบสายตาไปหาที่นอนอยู่เป็นประจำ',
                'stat':['11,854', '244', '745', '96', '(Elemental Mastery)'],
                'ascen':'**[✦-----]**:20,000 Mora, Vayuda Turquoise Sliver x1, Crystal Marrow x3, Whopperflower Nectar x3\n \
                        **[✦✦----]**:40,000 Mora, Vayuda Turquoise Fragment x3, Marionette Core x2, Crystal Marrow x10, Whopperflower Nectar x15\n \
                        **[✦✦✦---]**:60,000 Mora, Vayuda Turquoise Fragment x6, Marionette Core x4, Crystal Marrow x20, Shimmering Nectar x12\n \
                        **[✦✦✦✦--]**:80,000 Mora, Vayuda Turquoise Chunk x3, Marionette Core x8, Crystal Marrow x30, Shimmering Nectar x18\n \
                        **[✦✦✦✦✦-]**:100,000 Mora, Vayuda Turquoise Chunk x6, Marionette Core x12, Crystal Marrow x45, Elemental Nectar x12\n \
                        **[✦✦✦✦✦✦]**:120,000 Mora, Vayuda Turquoise Gemstone x6, Marionette Core x20, Crystal Marrow x60, Elemental Nectar x24',
                        'thum':'https://static.wikia.nocookie.net/genshin-impact/images/e/ec/Character_Sayu_Thumb.png/revision/latest/scale-to-width-down/50?cb=20210810173357&path-prefix=th', 'star':'[★★★★]'
                        ,'detail':['<:claymores:909806179205664810> ดาบใหญ่', 'Inazuma', '19 ตุลาคม', '<:anemo:909772060753018921> ลม']}
        return sayu
    elif name.lower() == "sucrose" or name.lower() == "31":
        sucrose = {'name':'Sucrose', 'his1':'Sucrose (ภาษาไทย: ซูโครส) เป็นตัวละครหญิงธาตุลมใช้อาวุธสื่อเวทที่สามารถเล่นได้ในเกม Genshin Impact\n\n\
            นักเล่นแร่แปรธาตุผู้เชี่ยวชาญในการเล่นแร่แปรธาตุชีวภาพ และทำหน้าที่เป็นผู้ช่วยของ Albedo หัวหน้านักเล่นแร่แปรธาตุแห่งกองอัศวินแห่ง Favonius',
                'stat':['9,243', '170', '703', '24.0%', '(Anemo DMG Bonus)'],
                'ascen':'**[✦-----]**:20,000 Mora, Vayuda Turquoise Sliver x1, Windwheel Aster x3, Whopperflower Nectar x3\n \
                        **[✦✦----]**:40,000 Mora, Vayuda Turquoise Fragment x3, Hurricane Seed x2, Windwheel Aster x10, Whopperflower Nectar x15\n \
                        **[✦✦✦---]**:60,000 Mora, Vayuda Turquoise Fragment x6, Hurricane Seed x4, Windwheel Aster x20, Shimmering Nectar x12\n \
                        **[✦✦✦✦--]**:80,000 Mora, Vayuda Turquoise Chunk x3, Hurricane Seed x8, Windwheel Aster x30, Shimmering Nectar x18\n \
                        **[✦✦✦✦✦-]**:100,000 Mora, Vayuda Turquoise Chunk x6, Hurricane Seed x12, Windwheel Aster x45, Elemental Nectar x12\n \
                        **[✦✦✦✦✦✦]**:120,000 Mora, Vayuda Turquoise Gemstone x6, Hurricane Seed x20, Windwheel Aster x60, Elemental Nectar x24',
                        'thum':'https://static.wikia.nocookie.net/genshin-impact/images/6/61/Character_Sucrose_Thumb.png/revision/latest/scale-to-width-down/50?cb=20210515120600&path-prefix=th', 'star':'[★★★★]'
                        ,'detail':['<:catalysts:909806179616702485> สื่อเวทย์', 'Mondstadt', '26 พฤศจิกายน', '<:anemo:909772060753018921> ลม']}
        return sucrose
    elif name.lower() == "tartaglia" or name.lower() == "childe" or name.lower() == "32":
        chi = {'name':'Tartaglia or Childe(Ajax)', 'his1':'Tartaglia (ภาษาไทย: ตาร์ตาลยา)เป็นตัวละครชายธาตุน้ำใช้อาวุธธนูที่สามารถเล่นได้ใน Genshin Impact\n\n\
            Tartaglia ผู้มีนามแฝงว่า Childe (ไชลด์) เป็นอ้ายหนุ่มน้องใหม่และเลือดเดือดที่สุดในหมู่สิบเอ็ดผู้บริหารแห่งฟาทุอิ ไล่หาเรื่องภัยพาลไปทุกที่ที่ปรากฎ \
                กระเหี้ยนกระหือรือที่จะประชันดาบและไล่ตามความท้าทายใหม่ๆอยู่ตลอดเวลา กลายมาเป็นยอดตัวอันตรายในหมู่เจ้าหน้าที่บริหารขัดกับความหน้าละอ่อนของมัน',
                'stat':['13,103', '301', '815', '28.8%', '(Hydro DMG Bonus)'],
                'ascen':'**[✦-----]**:20,000 Mora, Varunada Lazurite Sliver x1, Starconch x3, Recruit\'s Insignia x3\n \
                        **[✦✦----]**:40,000 Mora, Varunada Lazurite Fragment x3, Cleansing Heart x2, Starconch x10, Recruit\'s Insignia x15\n \
                        **[✦✦✦---]**:60,000 Mora, Varunada Lazurite Fragment x6, Cleansing Heart x4, Starconch x20, Sergeant\'s Insignia x12\n \
                        **[✦✦✦✦--]**:80,000 Mora, Varunada Lazurite Chunk x3, Cleansing Heart x8, Starconch x30, Sergeant\'s Insignia x18\n \
                        **[✦✦✦✦✦-]**:100,000 Mora, Varunada Lazurite Chunk x6, Cleansing Heart x12, Starconch x45, Lieutenant\'s Insignia x12\n \
                        **[✦✦✦✦✦✦]**:120,000 Mora, Varunada Lazurite Gemstone x6, Cleansing Heart x20, Starconch x60, Lieutenant\'s Insignia x24',
                        'thum':'https://static.wikia.nocookie.net/genshin-impact/images/5/53/Character_Tartaglia_Thumb.png/revision/latest/scale-to-width-down/50?cb=20210515121211&path-prefix=th', 'star':'[★★★★★]'
                        ,'detail':['<:bows:909806179427942400> ธนู', 'Snezhnaya', '20 กรกฎาคม', '<:hydro:909772393852071936> น้ำ']}
        return chi
    elif name.lower() == "thoma" or name.lower() == "33":
        tho = {'name':'Thoma', 'his1':'Thoma (ภาษาไทย: โทมะ; ภาษาญี่ปุ่น: トーマ Tooma) เป็นตัวละครชายธาตุไฟใช้อาวุธหอกที่สามารถเล่นได้ในเกม Genshin Impact\n\n\
            คนต่างแดนจากประเทศมอนด์ชตัดท์ โทมะทำงานเป็นพ่อบ้านประจำตระกูลคามิซาโตะในแดนอินาสึมะ ขึ้นชื่อในเรื่องความเอาการเอางานไหวและมีไหวพริบฉับไวเป็นเยี่ยม',
                'stat':['10,331', '202', '751', '24.0%', '(ATK Bonus)'],
                'ascen':'**[✦-----]**:20,000 Mora, Agnidus Agate Sliver x1, Fluorescent Fungus x3, Treasure Hoarder Insignia x3\n \
                        **[✦✦----]**:40,000 Mora, Agnidus Agate Fragment x3, Smoldering Pearl x2, Fluorescent Fungus x10, Treasure Hoarder Insignia x15\n \
                        **[✦✦✦---]**:60,000 Mora, Agnidus Agate Fragment x6, Smoldering Pearl x4, Fluorescent Fungus x20, Silver Raven Insignia x12\n \
                        **[✦✦✦✦--]**:80,000 Mora, Agnidus Agate Chunk x3, Smoldering Pearl x8, Fluorescent Fungus x30, Silver Raven Insignia x18\n \
                        **[✦✦✦✦✦-]**:100,000 Mora, Agnidus Agate Chunk x6, Smoldering Pearl x12, Fluorescent Fungus x45, Golden Raven Insignia x12\n \
                        **[✦✦✦✦✦✦]**:120,000 Mora, Agnidus Agate Gemstone x6, Smoldering Pearl x20, Fluorescent Fungus x60, Golden Raven Insignia x24',
                        'thum':'https://static.wikia.nocookie.net/genshin-impact/images/8/8a/Character_Thoma_Thumb.png/revision/latest/scale-to-width-down/50?cb=20211017122820&path-prefix=th', 'star':'[★★★★]'
                        ,'detail':['<:polearms:909806179348267069> หอก', 'Inazuma', '9 มกราคม', '<:pyro:909772346922008606> ไฟ']}
        return tho
    elif name.lower() == "venti" or name.lower() == "barbatos" or name.lower() == "35":
        ven = {'name':'Venti(Barbatos)', 'his1':'Venti (ภาษาไทย: เวนติ) เป็นตัวละครชายธาตุลมใช้อาวุธธนูที่สามารถเล่นได้ใน Genshin Impact\n\n\
            นักกวีพเนจรลึกลับ บางเวลาก็ร้องเพลงที่เก่าแก่ บางเวลากลับบรรเลงบทเพลงแปลกใหม่ที่ไม่มีใครเคยได้ฟัง ชอบแอปเปิ้ลและบรรยาการที่คึกคัก \
                เกลียดชีสและของทุกชนิดที่เหนียวหนึบ เมื่อรวบรวมพลังที่เป็นองค์ประกอบของ "ลม" รูปร่างของธาตุนั้นมักจะแสดงออกมาในรูปแบบของขนนก เพราะเขาชอบสิ่งที่ดูเบา ๆ มาก',\
                        'stat':['10,531', '263', '669', '32.0%', '(Energy Recharge)'],
                        'ascen':'**[✦-----]**:20,000 Mora, Vayuda Turquoise Sliver x1, Cecilia x3, Slime Condensate x3\n \
                        **[✦✦----]**:40,000 Mora, Vayuda Turquoise Fragment x3, Hurricane Seed x2, Cecilia x10, Slime Condensate x15\n \
                        **[✦✦✦---]**:60,000 Mora, Vayuda Turquoise Fragment x6, Hurricane Seed x4, Cecilia x20, Slime Secretions x12\n \
                        **[✦✦✦✦--]**:80,000 Mora, Vayuda Turquoise Chunk x3, Hurricane Seed x8, Cecilia x30, Slime Secretions x18\n \
                        **[✦✦✦✦✦-]**:100,000 Mora, Vayuda Turquoise Chunk x6, Hurricane Seed x12, Cecilia x45, Slime Concentrate x12\n \
                        **[✦✦✦✦✦✦]**:120,000 Mora, Vayuda Turquoise Gemstone x6, Hurricane Seed x20, Cecilia x60, Slime Concentrate x24',
                        'thum':'https://static.wikia.nocookie.net/genshin-impact/images/8/8d/Character_Venti_Thumb.png/revision/latest/scale-to-width-down/50?cb=20210515120608&path-prefix=th', 'star':'[★★★★★]'
                        ,'detail':['<:bows:909806179427942400> ธนู', 'Mondstadt', '16 กรกฎาคม', '<:anemo:909772060753018921> ลม']}
        return ven
    elif name.lower() == "xiangling" or name.lower() == "mao" or name.lower() == "chef" or name.lower() == "36":
        xiang = {'name':'Mao Xiangling', 'his1':'Mao Xiangling (ภาษาจีน: 卯香菱 Mǎo Xiānglíng; ภาษาไทย: เซียงหลิง) เป็นตัวละครหญิงธาตุไฟใช้อาวุธหอกที่สามารถเล่นได้ในเกม Genshin Impact\n\n\
            หัวหน้าแม่ครัวแห่งภัตตาคาร Wanmin ในฐานะแม่ครัว เซียงหลิงไม่เคยกลัวที่จะลองสูตรอาหารต่างๆ หรือส่วนผสมที่ "แปลกใหม่"... และการทำอาหารที่บางครั้งก็ไม่เหมือนใคร',\
                        'stat':['10,875', '225', '669', '96', '(Elemental Mastery)'],
                        'ascen':'**[✦-----]**:20,000 Mora, Agnidus Agate Sliver x1, Jueyun Chili x3, Slime Condensate x3\n \
                        **[✦✦----]**:40,000 Mora, Agnidus Agate Fragment x3, Everflame Seed x2, Jueyun Chili x10, Slime Condensate x15\n \
                        **[✦✦✦---]**:60,000 Mora, Agnidus Agate Fragment x6, Everflame Seed x4, Jueyun Chili x20, Slime Secretions x12\n \
                        **[✦✦✦✦--]**:80,000 Mora, Agnidus Agate Chunk x3, Everflame Seed x8, Jueyun Chili x30, Slime Secretions x18\n \
                        **[✦✦✦✦✦-]**:100,000 Mora, Agnidus Agate Chunk x6, Everflame Seed x12, Jueyun Chili x45, Slime Concentrate x12\n \
                        **[✦✦✦✦✦✦]**:120,000 Mora, Agnidus Agate Gemstone x6, Everflame Seed x20, Jueyun Chili x60, Slime Concentrate x24',
                        'thum':'https://static.wikia.nocookie.net/genshin-impact/images/a/a0/Character_Xiangling_Thumb.png/revision/latest/scale-to-width-down/50?cb=20210515120729&path-prefix=th', 'star':'[★★★★]'
                        ,'detail':['<:polearms:909806179348267069> หอก', 'Liyue', '2 พฤศจิกายน', '<:pyro:909772346922008606> ไฟ']}
        return xiang
    elif name.lower() == "xiao" or name.lower() == "alatus" or name.lower() == "37":
        xiao = {'name':'Xiao', 'his1':'Xiao (ภาษาไทย: เซียว; ภาษาจีน: 魈 Xiāo, "ปีศาจภูเขา") เป็นตัวละครชายธาตุลมใช้อาวุธหอกที่สามารถเล่นได้ในเกม Genshin Impact\n\n\
            เขาเป็นเซียน, ภายใต้นามว่า Alatus, และเป็นสมาชิกคนเดียวที่เหลืออยู่ในห้ายักษา ที่ Morax ส่งมาเพื่อปราบวิญญาณปีศาจที่ก่อกวน Liyue ปัจจุบันเขาอาศัยอยู่ที่ Wangshu Inn และส่วนใหญ่แยกตัวจากฝูงชนและการปฏิสัมพันธ์ของมนุษย์',\
                        'stat':['12,736', '349', '799', '19.2%', '(CRIT Rate)'],
                        'ascen':'**[✦-----]**:20,000 Mora, Vayuda Turquoise Sliver x1, Qingxin x3, Slime Condensate x3\n \
                        **[✦✦----]**:40,000 Mora, Vayuda Turquoise Fragment x3, Juvenile Jade x2, Qingxin x10, Slime Condensate x15\n \
                        **[✦✦✦---]**:60,000 Mora, Vayuda Turquoise Fragment x6, Juvenile Jade x4, Qingxin x20, Slime Secretions x12\n \
                        **[✦✦✦✦--]**:80,000 Mora, Vayuda Turquoise Chunk x3, Juvenile Jade x8, Qingxin x30, Slime Secretions x18\n \
                        **[✦✦✦✦✦-]**:100,000 Mora, Vayuda Turquoise Chunk x6, Juvenile Jade x12, Qingxin x45, Slime Concentrate x12\n \
                        **[✦✦✦✦✦✦]**:120,000 Mora, Vayuda Turquoise Gemstone x6, Juvenile Jade x20, Qingxin x60, Slime Concentrate x24',
                        'thum':'https://static.wikia.nocookie.net/genshin-impact/images/b/b9/Character_Xiao_Thumb.png/revision/latest/scale-to-width-down/50?cb=20210515120804&path-prefix=th', 'star':'[★★★★★]'
                        ,'detail':['<:polearms:909806179348267069> หอก', 'Liyue', '17 เมษายน', '<:anemo:909772060753018921> ลม']}
        return xiao
    elif name.lower() == "xingqiu" or name.lower() == "38":
        xin = {'name':'Xingqiu', 'his1':'Xingqiu (ภาษาจีน: 行秋 Xíngqiū; ภาษาไทย: สิงชิว) เป็นตัวละครชายธาตุน้ำใช้อาวุธดาบที่สามารถเล่นได้ใน Genshin Impact\n\n\
            Xingqiu (ภาษาจีน: 行秋 Xíngqiū; ภาษาไทย: สิงชิว) เป็นตัวละครชายธาตุน้ำใช้อาวุธดาบที่สามารถเล่นได้ใน Genshin Impact',\
                'stat':['10,223', '202', '758', '24.0%', '(ATK Bonus)'],
                'ascen':'**[✦-----]**:20,000 Mora, Varunada Lazurite Sliver x1, Silk Flower x3, Damaged Mask x3\n \
                        **[✦✦----]**:40,000 Mora, Varunada Lazurite Fragment x3, Cleansing Heart x2, Silk Flower x10, Damaged Mask x15\n \
                        **[✦✦✦---]**:60,000 Mora, Varunada Lazurite Fragment x6, Cleansing Heart x4, Silk Flower x20, Stained Mask x12\n \
                        **[✦✦✦✦--]**:80,000 Mora, Varunada Lazurite Chunk x3, Cleansing Heart x8, Silk Flower x30, Stained Mask x18\n \
                        **[✦✦✦✦✦-]**:100,000 Mora, Varunada Lazurite Chunk x6, Cleansing Heart x12, Silk Flower x45, Ominous Mask x12\n \
                        **[✦✦✦✦✦✦]**:120,000 Mora, Varunada Lazurite Gemstone x6, Cleansing Heart x20, Silk Flower x60, Ominous Mask x24',
                        'thum':'https://static.wikia.nocookie.net/genshin-impact/images/4/4a/Character_Xingqiu_Thumb.png/revision/latest/scale-to-width-down/50?cb=20210515120809&path-prefix=th', 'star':'[★★★★]'
                        ,'detail':['<:swords:909805198048886825> ดาบ', 'Liyue', '9 ตุลาคม', '<:hydro:909772393852071936> น้ำ']}
        return xin
    elif name.lower() == "xinyan" or name.lower() == "39":
        xiny = {'name':'Xinyan', 'his1':'Xinyan (ภาษาจีน: 辛焱 Xīnyàn; ภาษาไทย: ซินเยี่ยน) เป็นตัวละครหญิงธาตุไฟใช้อาวุธดาบใหญ่ที่สามารถเล่นได้ใน Genshin Impact\n\n\
            ร็อกแอนด์โรลถือเป็นศิลปะรูปแบบใหม่ใน Liyue และ Xinyan เป็นผู้บุกเบิกศิลปะแนวนี้ \
                เธอใช้บทเพลงและความหลงใหลในการร้องเพลงต่อต้าน "ความอคติ" เพื่อปลุกจิตวิญญาณที่เหนื่อยล้าของผู้คนบนโลกใบนี้',
                'stat':['11,201', '249', '799', '24.0%', '(ATK Bonus)'],
                'ascen':'**[✦-----]**:20,000 Mora, Agnidus Agate Sliver x1, Violetgrass x3, Treasure Hoarder Insignia x3\n \
                        **[✦✦----]**:40,000 Mora, Agnidus Agate Fragment x3, Everflame Seed x2, Violetgrass x10, Treasure Hoarder Insignia x15\n \
                        **[✦✦✦---]**:60,000 Mora, Agnidus Agate Fragment x6, Everflame Seed x4, Violetgrass x20, Silver Raven Insignia x12\n \
                        **[✦✦✦✦--]**:80,000 Mora, Agnidus Agate Chunk x3, Everflame Seed x8, Violetgrass x30, Silver Raven Insignia x18\n \
                        **[✦✦✦✦✦-]**:100,000 Mora, Agnidus Agate Chunk x6, Everflame Seed x12, Violetgrass x45, Golden Raven Insignia x12\n \
                        **[✦✦✦✦✦✦]**:120,000 Mora, Agnidus Agate Gemstone x6, Everflame Seed x20, Violetgrass x60, Golden Raven Insignia x24',
                        'thum':'https://static.wikia.nocookie.net/genshin-impact/images/9/9d/Character_Xinyan_Thumb.png/revision/latest/scale-to-width-down/50?cb=20210515120814&path-prefix=th', 'star':'[★★★★]'
                        ,'detail':['<:claymores:909806179205664810> ดาบใหญ่', 'Liyue', '16 ตุลาคม', '<:pyro:909772346922008606> ไฟ']}
        return xiny
    elif name.lower() == "yanfei" or name.lower() == "40":
        yanfei = {'name':'Yanfei', 'his1':'Yanfei (ภาษาจีน: 烟绯 Yānfēi; ภาษาไทย: เยียนเฟย) เป็นตัวละครหญิงธาตุไฟใช้อาวุธสื่อเวทที่สามารถเล่นได้ในเกม Genshin Impact\n\n\
            Yanfei - ผู้เป็นลูกครึ่งเซียน และเป็นที่ปรึกษากฎหมายชั้นนำ เธอพบความสมดุลที่สมบูรณ์แบบระหว่างการปฏิบัติตามกฎ สนองต่อเหตุการณ์อย่างยึดหยุ่น \
                อาศัยเอกลักษณ์เฉพาะในฐานะที่ปรึกษากฎหมายทั้งในเรื่องประสบการณ์และวิธีการ เพื่อการรักษาสมดุลของพันธสัญญาของ Liyue อย่างระมัดระวัง',
                'stat':['9,352', '240', '587', '24.0%', '(Pyro DMG Bonus)'],
                'ascen':'**[✦-----]**:20,000 Mora, Agnidus Agate Sliver x1, Noctilucous Jade x3, Treasure Hoarder Insignia x3\n \
                        **[✦✦----]**:40,000 Mora, Agnidus Agate Fragment x3, Noctilucous Jade x2, Noctilucous Jade x10, Treasure Hoarder Insignia x15\n \
                        **[✦✦✦---]**:60,000 Mora, Agnidus Agate Fragment x6, Noctilucous Jade x4, Noctilucous Jade x20, Silver Raven Insignia x12\n \
                        **[✦✦✦✦--]**:80,000 Mora, Agnidus Agate Chunk x3, Noctilucous Jade x8, Noctilucous Jade x30, Silver Raven Insignia x18\n \
                        **[✦✦✦✦✦-]**:100,000 Mora, Agnidus Agate Chunk x6, Noctilucous Jade x12, Noctilucous Jade x45, Golden Raven Insignia x12\n \
                        **[✦✦✦✦✦✦]**:120,000 Mora, Agnidus Agate Gemstone x6, Noctilucous Jade x20, Noctilucous Jade x60, Golden Raven Insignia x24',
                        'thum':'https://static.wikia.nocookie.net/genshin-impact/images/1/1f/Character_Yanfei_Thumb.png/revision/latest/scale-to-width-down/50?cb=20210515120821&path-prefix=th', 'star':'[★★★★]'
                        ,'detail':['<:catalysts:909806179616702485> สื่อเวทย์', 'Liyue', '28 กรกฎาคม', '<:pyro:909772346922008606> ไฟ']}
        return yanfei
    elif name.lower() == "naganohara yoimiya" or name.lower() == "naganohara" or name.lower() == "yoimiya" or name.lower() == "41":
        yoi = {'name':'Naganohara Yoimiya', 'his1':'Naganohara Yoimiya (ภาษาไทย: นากาโนะฮาระ โยอิมิยะ; ภาษาญี่ปุ่น: 長なが野の原はら宵よい宮みや) เป็นตัวละครหญิงธาตุไฟใช้อาวุธธนูที่สามารถเล่นได้ในเกม Genshin Impact\n\n\
            เด็กสาวร่าเริงพลังงานสูงผู้ชื่นชอบแสงสีวิจิตรตระการตาของดอกไม้ไฟยิ่งกว่าสิ่งใด โยอิมิยะทำกิจการร้านดอกไม้ไฟนากาโนะฮาระร่วมกับผู้เป็นพ่อ \
                นายนาโกโนะฮาระ เรียวโนะสึเกะ และเป็นที่รักของชาวอินาสึมะทั่วบ้านทั่วเมืองในฐานะ "องค์หญิงแห่งเทศกาลฤดูร้อน"',
                'stat':['10,164', '323', '615', '19.2%', '(CRIT Rate)'],
                'ascen':'**[✦-----]**:20,000 Mora, Agnidus Agate Sliver x1, Naku Weed x3, Divining Scroll x3\n \
                        **[✦✦----]**:40,000 Mora, Agnidus Agate Fragment x3, Smoldering Pearl x2, Naku Weed x10, Divining Scroll x15\n \
                        **[✦✦✦---]**:60,000 Mora, Agnidus Agate Fragment x6, Smoldering Pearl x4, Naku Weed x20, Sealed Scroll x12\n \
                        **[✦✦✦✦--]**:80,000 Mora, Agnidus Agate Chunk x3, Smoldering Pearl x8, Naku Weed x30, Sealed Scroll x18\n \
                        **[✦✦✦✦✦-]**:100,000 Mora, Agnidus Agate Chunk x6, Smoldering Pearl x12, Naku Weed x45, Forbidden Curse Scroll x12\n \
                        **[✦✦✦✦✦✦]**:120,000 Mora, Agnidus Agate Gemstone x6, Smoldering Pearl x20, Naku Weed x60, Forbidden Curse Scroll x24',
                        'thum':'https://static.wikia.nocookie.net/genshin-impact/images/0/05/Character_Yoimiya_Thumb.png/revision/latest/scale-to-width-down/50?cb=20210807091631&path-prefix=th', 'star':'[★★★★★]'
                        ,'detail':['<:bows:909806179427942400> ธนู', 'Inazuma', '21 มิถุนายน', '<:pyro:909772346922008606> ไฟ']}
        return yoi
    elif name.lower() == "zhongli" or name.lower() == "morax" or name.lower() == "42":
        zhon = {'name':'Zhongli(Morax)', 'his1':'Zhongli (ภาษาจีน: 钟离 Zhōnglí; ภาษาไทย: จงหลี) เป็นตัวละครชายธาตุหินใช้อาวุธหอกที่สามารถเล่นได้ในเกม Genshin Impact\n\n\
            เขาปรากฎตัวครั้งแรกในเควสต์เทพเจ้า บทที่ 1:ฉากที่ 2 - ลาก่อน เทพโบราณ ซึ่งภายหลังเปิดเผยว่าเป็นร่างปัจจุบันของเทพแห่งหินผา Morax ผู้ซึ่งได้ตัดสินใจสัมผัสโลกจากมุมมองของมนุษย์ \
                หลังจากสละโนซิสไป เขาได้เกษียณตนเอง และกลับสู่ตัวตนเดิมในฐานะเซียน แม้จะยังอยู่ภายใต้การปลอมตัวเป็นมนุษย์ก็ตาม ปัจจุบันเขาทำงานเป็นที่ปรึกษาของโถงแห่งการเกิดใหม่ Wangsheng',\
                        'stat':['14,695', '251', '738', '28.8%', '(Geo DMG Bonus)'],
                        'ascen':'**[✦-----]**:20,000 Mora, Prithiva Topaz Sliver x1, Cor Lapis x3, Slime Condensate x3\n \
                        **[✦✦----]**:40,000 Mora, Prithiva Topaz Fragment x3, Basalt Pillar x2, Cor Lapis x10, Slime Condensate x15\n \
                        **[✦✦✦---]**:60,000 Mora, Prithiva Topaz Fragment x6, Basalt Pillar x4, Cor Lapis x20, Slime Secretions x12\n \
                        **[✦✦✦✦--]**:80,000 Mora, Prithiva Topaz Chunk x3, Basalt Pillar x8, Cor Lapis x30, Slime Secretions x18\n \
                        **[✦✦✦✦✦-]**:100,000 Mora, Prithiva Topaz Chunk x6, Basalt Pillar x12, Cor Lapis x45, Slime Concentrate x12\n \
                        **[✦✦✦✦✦✦]**:120,000 Mora, Prithiva Topaz Gemstone x6, Basalt Pillar x20, Cor Lapis x60, Slime Concentrate x24',
                        'thum':'https://static.wikia.nocookie.net/genshin-impact/images/c/c2/Character_Zhongli_Thumb.png/revision/latest/scale-to-width-down/50?cb=20210515120825&path-prefix=th', 'star':'[★★★★★]'
                        ,'detail':['<:polearms:909806179348267069> หอก', 'Liyue', '31 ธันวาคม', '<:geo:909771888413257769> หิน']}
        return zhon
    elif name.lower() == "traveler" or name.lower() == "aether" or name.lower() == "lumine" or name.lower() == "34":
        tra = {'name':'Aether/Lumine', 'his1':'นักเดินทาง เป็นตัวละครเอกที่สามารถเลือกเล่นในเกม Genshin Impact ในช่วงเลือกตัวละครเริ่มต้น อีเธอร์เป็นพี่น้องฝาแฝดจากอีกโลกหนึ่งที่ออกเดินทางทั่วโลก \
            จนกระทั่งวันหนึ่งทั้งสองเข้าปะทะ Unknown God และพ่ายแพ้อย่างหมดรูป แฝดคนนึงถูกผนึกเอาไว้ ส่วนอีกคนถูกส่งลงมาที่โลก Teyvat จนใช้ชีวิตไปสักพักหนึ่ง จนกระทั่งได้พบเจอเพื่อนร่วมเดินทางที่บังเอิญเจอกัน \
                "ไพม่อน" จากนั้นทั้งสองจับพลัดจับผลูร่วมการผจญภัยนับตั้งแต่นั้นมา\n\n\
            แม้ว่าผู้เล่นจะสามารถเลือกชื่อที่ต้องการให้ถูกกล่าวถึงได้ แต่ฝาแฝดของนักเดินทาง (คู่แฝดคนใดที่ไม่ได้เลือกตั้งแต่เริ่มต้นเกม) จะหมายถึง นักเดินทาง โดยจะเป็น Aether หรือ Lumine (ขึ้นอยู่กับเพศที่ผู้เล่นเลือกจากคู่แฝด) โดยจะไม่คำนึงถึงชื่อที่ตั้งขึ้นมาเอง',\
                'stat':['10,875', '212', '683', '24.0%', '(ATK Bonus)'],
                'ascen':'**[✦-----]**:20,000 Mora, Brilliant Diamond Sliver x1, Windwheel Aster x3, Damaged Mask x3\n \
                        **[✦✦----]**:40,000 Mora, Brilliant Diamond Fragment x3, Windwheel Aster x10, Damaged Mask x15\n \
                        **[✦✦✦---]**:60,000 Mora, Brilliant Diamond Fragment x6, Windwheel Aster x20, Stained Mask x12\n \
                        **[✦✦✦✦--]**:80,000 Mora, Brilliant Diamond Chunk x3, Windwheel Aster x30, Stained Mask x18\n \
                        **[✦✦✦✦✦-]**:100,000 Mora, Brilliant Diamond Chunk x6, Windwheel Aster x45, Ominous Mask x12\n \
                        **[✦✦✦✦✦✦]**:120,000 Mora, Brilliant Diamond Gemstone x6, Windwheel Aster x60, Ominous Mask x24',
                        'thum':'https://static.wikia.nocookie.net/genshin-impact/images/7/71/Character_Traveler_Thumb.png/revision/latest/scale-to-width-down/50?cb=20210515140422&path-prefix=th', 'star':'[★★★★★]'
                        ,'detail':['<:swords:909805198048886825> ดาบ', 'ออกเดินทางไปทุกที่ไม่มีที่เป็นหลักแหล่ง', 'ผู้เล่นเป็นคนเลือก', '<:anemo:909772060753018921><:geo:909771888413257769><:electro:909772113970364466> ลม,หิน,ไฟฟ้า']}
        return tra
