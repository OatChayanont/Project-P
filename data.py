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
                        'thum':'https://static.wikia.nocookie.net/genshin-impact/images/0/00/Character_Albedo_Thumb.png/revision/latest/scale-to-width-down/50?cb=20210515115757&path-prefix=th', 'star':'[★★★★★]'}
        return albedo
    elif name.lower() == "aloy":
        aloy = {'name':'Aloy', 'his1':'Aloy เป็นนางเอกจากเกม Horizon Zero Dawn ถูกสร้างขึ้นมาเป็นตัวละครข้ามเกมและโปรเจ็กต์ประสานงานระหว่างสตูดิโอ Guerrilla Games และ miHoYo',
                        'stat':['10,899', '234', '676', '28.8%', '(Cryo DMG Bonus)'],
                        'ascen':'**[✦-----]**:20,000 Mora, Shivada Jade Sliver x1, Crystal Marrow x3, Spectral Husk x3\n \
                        **[✦✦----]**:40,000 Mora, Shivada Jade Fragment x3, Crystalline Bloom x2, Crystal Marrow x10, Spectral Husk x15\n \
                        **[✦✦✦---]**:60,000 Mora, Shivada Jade Fragment x6, Crystalline Bloom x4, Crystal Marrow x20, Spectral Heart x12\n \
                        **[✦✦✦✦--]**:80,000 Mora, Shivada Jade Chunk x3, Crystalline Bloom x8, Crystal Marrow x30, Spectral Heart x18\n \
                        **[✦✦✦✦✦-]**:100,000 Mora, Shivada Jade Chunk x6, Crystalline Bloom x12, Crystal Marrow x45, Spectral Nucleus x12\n \
                        **[✦✦✦✦✦✦]**:120,000 Mora, Shivada Jade Gemstone x6, Crystalline Bloom x20, Crystal Marrow x60, Spectral Nucleus x24',
                        'thum':'https://static.wikia.nocookie.net/genshin-impact/images/6/6a/Character_Aloy_Thumb.png/revision/latest/scale-to-width-down/50?cb=20210902150457&path-prefix=th', 'star':'[★★★★★]'}
        return aloy
    elif name.lower() == "amber":
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
                        'thum':'https://static.wikia.nocookie.net/genshin-impact/images/c/c6/Character_Amber_Thumb.png/revision/latest/scale-to-width-down/50?cb=20210515115827&path-prefix=th', 'star':'[★★★★]'}
        return amber
    elif name.lower() == "barbara":
        barbara = {'name':'Barbara', 'his1':'Barbara (ภาษาไทย: บาร์บาร่า) เป็นตัวละครหญิงธาตุน้ำใช้สื่อเวทที่เล่นได้ในเกม Genshin Impact\n\n\
            Barbara เป็นผู้แสวงบุญแห่งโบสถ์ Favonius และเป็นดาราจรัสแสงของ Monstadt ชาวเมืองจะคุ้นชินกับนักดนตรีพเนจรมากกว่าดารา แต่ไม่ว่าอย่างไรพวกเขาก็รัก Barbara อย่างไม่ต้องสงสัย "ฉันมีวันนี้ได้เพราะจิตวิญญาณของเมืองแห่งอิสระนี้" Barbara พูดถึงความเป็นที่นิยมของเธอ',\
                        'stat':['9,787', '159', '669', '24.0%', '(HP Bonus)'],\
                        'ascen':'**[✦-----]**:20,000 Mora, Varunada Lazurite Sliver x1, Philanemo Mushroom x3, Divining Scroll x3\n \
                        **[✦✦----]**:40,000 Mora, Varunada Lazurite Fragment x3, Cleansing Heart x2, Philanemo Mushroom x10, Divining Scroll x15\n \
                        **[✦✦✦---]**:60,000 Mora, Varunada Lazurite Fragment x6, Cleansing Heart x4, Philanemo Mushroom x20, Sealed Scroll x12\n \
                        **[✦✦✦✦--]**:80,000 Mora, Varunada Lazurite Chunk x3, Cleansing Heart x8, Philanemo Mushroom x30, Sealed Scroll x18\n \
                        **[✦✦✦✦✦-]**:100,000 Mora, Varunada Lazurite Chunk x6, Cleansing Heart x12, Philanemo Mushroom x45, Forbidden Curse Scroll x12\n \
                        **[✦✦✦✦✦✦]**:120,000 Mora, Varunada Lazurite Gemstone x6, Cleansing Heart x20, Philanemo Mushroom x60, Forbidden Curse Scroll x24',\
                        'thum':'https://static.wikia.nocookie.net/genshin-impact/images/7/72/Character_Barbara_Thumb.png/revision/latest/scale-to-width-down/50?cb=20210515121106&path-prefix=th','star':'[★★★★]'}
        return barbara
    elif name.lower() == "beidou":
        beidou = {'name':'Beidou', 'his1':'Beidou (ภาษาจีน: 北斗 Běidǒu, "กระบวยใหญ่"; ภาษาไทย: เป๋ยโต่ว) เป็นตัวละครหญิงธาตุไฟฟ้าใช้อาวุธดาบใหญ่ที่สามารถเล่นได้ในเกม Genshin Impact\n\n\
            กัปตันเรือแห่งกองทัพเรือ Cruxอันเลื่องชื่อ นอกไปจากชื่อเสียงในการนำกองเรือและพละกำลังอันน่าเกรงขามแล้ว เป๋ยโต่วยังเป็นที่กล่าวขานในหมู่ชาวหลีเยว่ว่าไม่เกรงกลัวเศรษฐินีหนิงกวงผู้เป็นเทียนเฉวียนแห่งเจ็ดดารา นิสัยที่คู่กรณีไม่ติดใจ แต่ก็รำคาญเป็นบางที',
                        'stat':['13,050', '225', '648', '24.0%', '(Electro DMG Bonus)'],
                        'ascen':'**[✦-----]**:20,000 Mora, Vajrada Amethyst Sliver x1, Noctilucous Jade x3, Treasure Hoarder Insignia x3\n \
                        **[✦✦----]**:40,000 Mora, Vajrada Amethyst Fragment x3, Lightning Prism x2, Noctilucous Jade x10, Treasure Hoarder Insignia x15\n \
                        **[✦✦✦---]**:60,000 Mora, Vajrada Amethyst Fragment x6, Lightning Prism x4, Noctilucous Jade x20, Silver Raven Insignia x12\n \
                        **[✦✦✦✦--]**:80,000 Mora, Vajrada Amethyst Chunk x3, Lightning Prism x8, Noctilucous Jade x30, Silver Raven Insignia x18\n \
                        **[✦✦✦✦✦-]**:100,000 Mora, Vajrada Amethyst Chunk x6, Lightning Prism x12, Noctilucous Jade x45, Golden Raven Insignia x12\n \
                        **[✦✦✦✦✦✦]**:120,000 Mora, Vajrada Amethyst Gemstone x6, Lightning Prism x20, Noctilucous Jade x60, Golden Raven Insignia x24',
                        'thum':'https://static.wikia.nocookie.net/genshin-impact/images/6/61/Character_Beidou_Thumb.png/revision/latest/scale-to-width-down/50?cb=20210515121112&path-prefix=th', 'star':'[★★★★]'}
        return beidou
    elif name.lower() == "bennett":
        bennett = {'name':'Bennett', 'his1':'Bennett (ภาษาไทย: เบนเน็ตต์) เป็นตัวละครชายธาตุไฟใช้อาวุธดาบที่สามารถเล่นได้ใน Genshin Impact\n\n\
            เด็กผู้กำพร้าตั้งแต่ทารกก่อนจะถูกพบโดยนักผจญภัยอาวุโส และเติบโตมาภายในกิลด์นักผจญภัยโดยมีนามว่าเบนเน็ตต์ และเป็นสมาชิกเพียงหนึ่งเดียวของ "กลุ่มนักผจญภัยของ Benny" ในขณะที่คนอื่น ๆ ลาออกจากทีมไปจนหมดหลังจากประสบความโชคร้ายที่ตามติดเขามาโดยตลอด',
                        'stat':['12,397', '191', '191', '26.7%', '(Energy Recharge)'],
                        'ascen':'**[✦-----]**:20,000 Mora, Agnidus Agate Sliver x1, Windwheel Aster x3, Treasure Hoarder Insignia x3\n \
                        **[✦✦----]**:40,000 Mora, Agnidus Agate Fragment x3, Everflame Seed x2, Windwheel Aster x10, Treasure Hoarder Insignia x15\n \
                        **[✦✦✦---]**:60,000 Mora, Agnidus Agate Fragment x6, Everflame Seed x4, Windwheel Aster x20, Silver Raven Insignia x12\n \
                        **[✦✦✦✦--]**:80,000 Mora, Agnidus Agate Chunk x3, Everflame Seed x8, Windwheel Aster x30, Silver Raven Insignia x18\n \
                        **[✦✦✦✦✦-]**:100,000 Mora, Agnidus Agate Chunk x6, Everflame Seed x12, Windwheel Aster x45, Golden Raven Insignia x12\n \
                        **[✦✦✦✦✦✦]**:120,000 Mora, Agnidus Agate Gemstone x6, Everflame Seed x20, Windwheel Aster x60, Golden Raven Insignia x24',
                        'thum':'https://static.wikia.nocookie.net/genshin-impact/images/7/7b/Character_Bennett_Thumb.png/revision/latest/scale-to-width-down/50?cb=20210515121202&path-prefix=th', 'star':'[★★★★]'}
        return bennett
    elif name.lower() == "choungyun":
        choungyun = {'name':'Choungyun', 'his1':'Chongyun (ภาษาจีน: 重云 Chóngyún; ภาษาไทย: ฉงอวิ๋น) เป็นตัวละครชายธาตุน้ำแข็งใช้อาวุธดาบใหญ่ที่สามารถเล่นได้ใน Genshin Impact\n\n\
            นักปราบปีศาจผู้ใช้ Liyue เป็นศูนย์กลางและทำการปราบปีศาจไปทั่วทุกแห่งหน ในฐานะที่เป็นทายาทของตระกูลนักปราบปีศาจ เขาจึงมีความสามารถพิเศษนี้มาตั้งแต่เด็ก— ทว่าความสามารถพิเศษนี้เขาไม่ได้ร่ำเรียนมาจากอาจารย์ท่านไหน แต่เป็นความสามารถที่มีมาตั้งแต่เกิด "ร่างกายแห่งหยางบริสุทธิ์',\
                        'stat':['12,397', '191', '191', '26.7%', '(Energy Recharge)'],
                        'ascen':'**[✦-----]**:20,000 Mora, Shivada Jade Sliver x1, Cor Lapis x3, Damaged Mask x3\n \
                        **[✦✦----]**:40,000 Mora, Shivada Jade Fragment x3, Hoarfrost Core x2, Cor Lapis x10, Damaged Mask x15\n \
                        **[✦✦✦---]**:60,000 Mora, Shivada Jade Fragment x6, Hoarfrost Core x4, Cor Lapis x20, Stained Mask x12\n \
                        **[✦✦✦✦--]**:80,000 Mora, Shivada Jade Chunk x3, Hoarfrost Core x8, Cor Lapis x30, Stained Mask x18\n \
                        **[✦✦✦✦✦-]**:100,000 Mora, Shivada Jade Chunk x6, Hoarfrost Core x12, Cor Lapis x45, Ominous Mask x12\n \
                        **[✦✦✦✦✦✦]**:120,000 Mora, Shivada Jade Gemstone x6, Hoarfrost Core x20, Cor Lapis x60, Ominous Mask x24',
                        'thum':'https://static.wikia.nocookie.net/genshin-impact/images/6/68/Character_Chongyun_Thumb.png/revision/latest/scale-to-width-down/50?cb=20210515121158&path-prefix=th', 'star':'[★★★★]'}
        return choungyun
    elif name.lower() == "diluc":
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
                        'thum':'https://static.wikia.nocookie.net/genshin-impact/images/0/02/Character_Diluc_Thumb.png/revision/latest/scale-to-width-down/50?cb=20210515140346&path-prefix=th', 'star':'[★★★★★]'}
        return diluc
    elif name.lower() == "diona":
        diona = {'name':'Diona', 'his1':'Diona (ภาษาไทย: ดีโอน่า) เป็นตัวละครหญิงธาตุน้ำแข็งใช้อาวุธธนูที่สามารถเล่นได้ใน Genshin Impact\n\n\
            บาร์เทนเดอร์ชื่อดังแห่งร้าน Cat\'s Tail ดาวดวงใหม่แห่งวงการเครื่องดื่มของ Mondstadt ผู้ท้าชิงอันแข็งแกร่งในวงการเครื่องดื่มแอลกอฮอล์สาวน้อยที่มีหูแมวและหางแมวที่เกิดใน Springvale ตราบใดที่เครื่องดื่มแก้วนั้นได้รับการปรุงแต่งโดย Diona มันก็จะกลายเป็นเครื่องดื่มรสเลิศที่ไม่อาจจินตนาการได้เสมอ',
                'stat':['9,570', '212', '601', '24.0%', '(Cryo DMG Bonus)'],
                'ascen':'**[✦-----]**:20,000 Mora, Shivada Jade Sliver x1, Calla Lily x3, Firm Arrowhead x3\n \
                        **[✦✦----]**:40,000 Mora, Shivada Jade Fragment x3, Everflame Seed x2, Calla Lily x10, Firm Arrowhead x15\n \
                        **[✦✦✦---]**:60,000 Mora, Shivada Jade Fragment x6, Everflame Seed x4, Calla Lily x20, Sharp Arrowhead x12\n \
                        **[✦✦✦✦--]**:80,000 Mora, Shivada Jade Chunk x3, Everflame Seed x8, Calla Lily x30, Sharp Arrowhead x18\n \
                        **[✦✦✦✦✦-]**:100,000 Mora, Shivada Jade Chunk x6, Everflame Seed x12, Calla Lily x45, Weathered Arrowhead x12\n \
                        **[✦✦✦✦✦✦]**:120,000 Mora, Shivada Jade Gemstone x6, Everflame Seed x20, Calla Lily x60, Weathered Arrowhead x24',
                        'thum':'https://static.wikia.nocookie.net/gensin-impact/images/b/b9/Character_Diona_Thumb.png/revision/latest/scale-to-width-down/50?cb=20210213163131', 'star':'[★★★★]'}
        return diona
    elif name.lower() == "eula":
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
                        'thum':'https://static.wikia.nocookie.net/genshin-impact/images/d/d3/Character_Eula_Thumb.png/revision/latest/scale-to-width-down/50?cb=20210523123929&path-prefix=th', 'star':'[★★★★★]'}
        return eula
    elif name.lower() == "fischl" or name.lower() == "amy":
        amy = {'name':'Fischl', 'his1':'Fischl von Luftschloss Narfidort, ชื่อจริง Amy เป็นตัวละครหญิงธาตุไฟฟ้าใช้อาวุธธนูที่สามารถเล่นได้ในเกม Genshin Impact\n\n\
            นักสืบสาวจินตนาการล้นโลกประจำกิลด์นักผจญภัยแห่งมอนด์ชตัดต์ ฟิชเชิลกล่าวว่าตนนั้นมีที่มาโลกอื่นอันมิใช่ Teyvat พร้อมกับอีการาตรีนามว่า ออซ ฟิชเชิลชอบตั้งทฤษฎีแปลกประหลาดที่สุดท้ายแล้วกลับกลายเป็นความจริงอย่างคาดไม่ถึงอยู่บ่อยครั้ง',
                'stat':['9,189', '244', '594', '24.0%', '(ATK Bonus)'],
                'ascen':'**[✦-----]**:20,000 Mora, Vajrada Amethyst Sliver x1, Small Lamp Grass x3, Firm Arrowhead x3\n \
                        **[✦✦----]**:40,000 Mora, Vajrada Amethyst Fragment x3, Lightning Prism x2, Dandelion Seed x10, Firm Arrowhead x15\n \
                        **[✦✦✦---]**:60,000 Mora, Vajrada Amethyst Fragment x6, Lightning Prism x4, Dandelion Seed x20, Sharp Arrowhead x12\n \
                        **[✦✦✦✦--]**:80,000 Mora, Vajrada Amethyst Chunk x3, Lightning Prism x8, Dandelion Seed x30, Sharp Arrowhead x18\n \
                        **[✦✦✦✦✦-]**:100,000 Mora, Vajrada Amethyst Chunk x6, Lightning Prism x12, Dandelion Seed x45, Weathered Arrowhead x12\n \
                        **[✦✦✦✦✦✦]**:120,000 Mora, Vajrada Amethyst Gemstone x6, Lightning Prism x20, Dandelion Seed x60, Weathered Arrowhead x24',
                        'thum':'https://static.wikia.nocookie.net/genshin-impact/images/1/14/Character_Fischl_Thumb.png/revision/latest/scale-to-width-down/50?cb=20210515120053&path-prefix=th', 'star':'[★★★★]'}
        return amy
    elif name.lower() == "ganyu":
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
                        'thum':'https://static.wikia.nocookie.net/genshin-impact/images/0/0a/Character_Ganyu_Thumb.png/revision/latest/scale-to-width-down/50?cb=20210515120051&path-prefix=th', 'star':'[★★★★★]'}
        return ganyu
    elif name.lower() == "hu tao":
        hutao = {'name':'Hu Tao', 'his1':'Hu Tao (ภาษาจีน: 胡桃 Hú Táo, "วอลนัท"; ภาษาไทย: หู เถา) เป็นตัวละครหญิงธาตุไฟใช้อาวุธหอกที่สามารถเล่นได้ใน Genshin Impact\n\n\
            Hu Tao - หัวหน้า "โถงแห่งการเกิดใหม่ Wangsheng" สมัยที่ 77 เป็นบุคคลสำคัญที่รับผิดชอบพิธีงานศพใน Liyue อุทิศตนเพื่อประกอบพิธีอำลาแด่ผู้คนที่จากไปให้สมบูรณ์ เพื่อรักษาสมดุลระหว่างหยินและหยางของโลก',
                'stat':['15,552', '106', '876', '38.4%', '(CRIT DMG)'],
                'ascen':'**[✦-----]**:20,000 Mora, Agnidus Agate Sliver x1, Silk Flower x3, Whopperflower Nectar x3\n \
                        **[✦✦----]**:40,000 Mora, Agnidus Agate Fragment x3, Juvenile Jade x2, Silk Flower x10, Whopperflower Nectar x15\n \
                        **[✦✦✦---]**:60,000 Mora, Agnidus Agate Fragment x6, Juvenile Jade x4, Silk Flower x20, Shimmering Nectar x12\n \
                        **[✦✦✦✦--]**:80,000 Mora, Agnidus Agate Chunk x3, Juvenile Jade x8, Silk Flower x30, Shimmering Nectar x18\n \
                        **[✦✦✦✦✦-]**:100,000 Mora, Agnidus Agate Chunk x6, Juvenile Jade x12, Silk Flower x45, Elemental Nectar x12\n \
                        **[✦✦✦✦✦✦]**:120,000 Mora, Agnidus Agate Gemstone x6, Juvenile Jade x20, Silk Flower x60, Elemental Nectar x24',
                        'thum':'https://static.wikia.nocookie.net/genshin-impact/images/a/a4/Character_Hu_Tao_Thumb.png/revision/latest/scale-to-width-down/50?cb=20210515120520&path-prefix=th', 'star':'[★★★★★]'}
        return hutao
    elif name.lower() == "jean":
        jean = {'name':'Jean', 'his1':'Jean (ภาษาไทย: จีน) เป็นตัวละครหญิงธาตุลมใช้อาวุธดาบที่สามารถเล่นได้ในเกม Genshin Impact\n\n\
            พี่สาวของบาบาร่าผู้กำลังดำรงตำแหน่งรักษาการณ์ผู้บัญชาการอัศวินแห่งฟาโวเนียส จีนเป็นคนขยันขันแข็ง มุ่งมั่นในการรักษาสันติสุขให้แก่ประชาชนแห่งเมืองมอนด์ชดัตท์',
                'stat':['14,695', '239', '769', '22.2%', '(Healing Bonus)'],
                'ascen':'**[✦-----]**:20,000 Mora, Vayuda Turquoise Sliver x1, Dandelion Seed x3, Damaged Mask x3\n \
                        **[✦✦----]**:40,000 Mora, Vayuda Turquoise Fragment x3, Hurricane Seed x2, Dandelion Seed x10, Damaged Mask x15\n \
                        **[✦✦✦---]**:60,000 Mora, Vayuda Turquoise Fragment x6, Hurricane Seed x4, Dandelion Seed x20, Stained Mask x12\n \
                        **[✦✦✦✦--]**:80,000 Mora, Vayuda Turquoise Chunk x3, Hurricane Seed x8, Dandelion Seed x30, Stained Mask x18\n \
                        **[✦✦✦✦✦-]**:100,000 Mora, Vayuda Turquoise Chunk x6, Hurricane Seed x12, Dandelion Seed x45, Ominous Mask x12\n \
                        **[✦✦✦✦✦✦]**:120,000 Mora, Vayuda Turquoise Gemstone x6, Hurricane Seed x20, Dandelion Seed x60, Ominous Mask x24',
                        'thum':'https://static.wikia.nocookie.net/genshin-impact/images/8/89/Character_Jean_Thumb.png/revision/latest/scale-to-width-down/50?cb=20210515120531&path-prefix=th', 'star':'[★★★★★]'}
        return jean
    elif name.lower() == "kaedehara kazuha" or name.lower() == "kazuha" or name.lower() == "kaedehara":
        kazuha = {'name':'Kaedehara Kazuha', 'his1':'Kaedehara Kazuha (ภาษาไทย: คาเอเดะฮาระ คาซึฮะ; ภาษาญี่ปุ่น: 楓かえで原はら万かず葉は) เป็นตัวละครชายธาตุลมใช้อาวุธดาบที่สามารถเล่นได้ใน Genshin Impact\n\n\
            เขาเป็นซามูไรพเนจรของตระกูล Kaedehara ที่เคยโด่งดัง, และเป็นลูกเรือชั่วคราวของกองทัพเรือ Crux',
                'stat':['13,348', '297', '807', '115.2', '(Elemental Mastery)'],
                'ascen':'**[✦-----]**:20,000 Mora, Vayuda Turquoise Sliver x1, Sea Ganoderma x3, Treasure Hoarder Insignia x3\n \
                        **[✦✦----]**:40,000 Mora, Vayuda Turquoise Fragment x3, Marionette Core x2, Sea Ganoderma x10, Treasure Hoarder Insignia x15\n \
                        **[✦✦✦---]**:60,000 Mora, Vayuda Turquoise Fragment x6, Marionette Core x4, Sea Ganoderma x20, Silver Raven Insignia x12\n \
                        **[✦✦✦✦--]**:80,000 Mora, Vayuda Turquoise Chunk x3, Marionette Core x8, Sea Ganoderma x30, Silver Raven Insignia x18\n \
                        **[✦✦✦✦✦-]**:100,000 Mora, Vayuda Turquoise Chunk x6, Marionette Core x12, Sea Ganoderma x45, Golden Raven Insignia x12\n \
                        **[✦✦✦✦✦✦]**:120,000 Mora, Vayuda Turquoise Gemstone x6, Marionette Core x20, Sea Ganoderma x60, Golden Raven Insignia x24',
                        'thum':'https://static.wikia.nocookie.net/genshin-impact/images/f/f0/Character_Kaedehara_Kazuha_Thumb.png/revision/latest/scale-to-width-down/50?cb=20210722145202&path-prefix=th', 'star':'[★★★★★]'}
        return kazuha
    elif name.lower() == "kaeya":
        kaeya = {'name':'kaeya', 'his1':'Kaeya (ภาษาไทย: ไคยะ) เป็นตัวละครชายธาตุน้ำแข็งใช้อาวุธดาบที่สามารถเล่นได้ใน Genshin Impact\n\n\
            ในหน่วยอัศวินแห่ง Favonius จะมี Kaeya เป็นหัวหน้าอัศวินที่มีความรับผิดชอบมากที่สุด ไม่ว่าหน้าที่ใดเขาก็ทำให้ลุล่วงได้ทั้งสิ้น เขาเป็นที่นิยมในหมู่ประชาชนของเมือง Monstadt อย่างมาก แต่อัศวินผู้นี้ก็มีความลับที่ซ่อนอยู่เช่นกัน',
                'stat':['11,636', '223', '792', '26.7%', '(Energy Recharge)'],
                'ascen':'**[✦-----]**:20,000 Mora, Shivada Jade Sliver x1, Calla Lily x3, Treasure Hoarder Insignia x3\n \
                        **[✦✦----]**:40,000 Mora, Shivada Jade Fragment x3, Hoarfrost Core x2, Calla Lily x10, Treasure Hoarder Insignia x15\n \
                        **[✦✦✦---]**:60,000 Mora, Shivada Jade Fragment x6, Hoarfrost Core x4, Calla Lily x20, Silver Raven Insignia x12\n \
                        **[✦✦✦✦--]**:80,000 Mora, Shivada Jade Chunk x3, Hoarfrost Core x8, Calla Lily x30, Silver Raven Insignia x18\n \
                        **[✦✦✦✦✦-]**:100,000 Mora, Shivada Jade Chunk x6, Hoarfrost Core x12, Calla Lily x45, Golden Raven Insignia x12\n \
                        **[✦✦✦✦✦✦]**:120,000 Mora, Shivada Jade Gemstone x6, Hoarfrost Core x20, Calla Lily x60, Golden Raven Insignia x24',
                        'thum':'https://static.wikia.nocookie.net/genshin-impact/images/3/33/Character_Kaeya_Thumb.png/revision/latest/scale-to-width-down/50?cb=20210515140405&path-prefix=th', 'star':'[★★★★]'}
        return kaeya
    elif name.lower() == "kamisato ayaka" or name.lower() == "kamisato" or name.lower() == "ayaka":
        ayaka = {'name':'Kamisato Ayaka', 'his1':'Kaedehara Kazuha (ภาษาไทย: คาเอเดะฮาระ คาซึฮะ; ภาษาญี่ปุ่น: 楓かえで原はら万かず葉は)[Note 1] เป็นตัวละครชายธาตุลมใช้อาวุธดาบที่สามารถเล่นได้ใน Genshin Impact\n\n\
            เขาเป็นซามูไรพเนจรของตระกูล Kaedehara ที่เคยโด่งดัง, และเป็นลูกเรือชั่วคราวของกองทัพเรือ Crux',
                'stat':['12,858', '342', '784', '38.4%', '(CRIT Rate)'],
                'ascen':'**[✦-----]**:20,000 Mora, Shivada Jade Sliver x1, Sakura Bloom x3, Old Handguard x3\n \
                        **[✦✦----]**:40,000 Mora, Shivada Jade Fragment x3, Perpetual Heart x2, Sakura Bloom x10, Old Handguard x15\n \
                        **[✦✦✦---]**:60,000 Mora, Shivada Jade Fragment x6, Perpetual Heart x4, Sakura Bloom x20, Kageuchi Handguard x12\n \
                        **[✦✦✦✦--]**:80,000 Mora, Shivada Jade Chunk x3, Perpetual Heart x8, Sakura Bloom x30, Kageuchi Handguard x18\n \
                        **[✦✦✦✦✦-]**:100,000 Mora, Shivada Jade Chunk x6, Perpetual Heart x12, Sakura Bloom x45, Famed Handguard x12\n \
                        **[✦✦✦✦✦✦]**:120,000 Mora, Shivada Jade Gemstone x6, Perpetual Heart x20, Sakura Bloom x60, Famed Handguard x24',
                        'thum':'https://static.wikia.nocookie.net/genshin-impact/images/f/fd/Character_Kamisato_Ayaka_Thumb.png/revision/latest/scale-to-width-down/50?cb=20210726062342&path-prefix=th', 'star':'[★★★★★]'}
        return ayaka
    elif name.lower() == "keqing":
        keq = {'name':'Keqing', 'his1':'Keqing (ภาษาจีน: 刻晴 Kèqíng; ภาษาไทย: เค่อฉิง) เป็นตัวละครหญิงธาตุไฟฟ้าใช้อาวุธดาบที่สามารถเล่นได้ในเกม Genshin Impact\n\n\
            Yuheng ประจำเจ็ดดาราแห่งหลีเยว่ผู้ทำงานตัวเป็นเกลียว เค่อฉิงเป็นหญิงสาวใจอิสระผู้เลือกเส้นทางเดินด้วยพลังและความสามารถที่ตนเองมี ไม่คิดจะปล่อยให้เหล่าทวยเทพกำหนดชะตากรร',
                'stat':['13,103', '323', '799', '38.4%', '(CRIT DMG)'],
                'ascen':'**[✦-----]**:20,000 Mora, Vajrada Amethyst Sliver x1, Cor Lapis x3, Whopperflower Nectar x3\n \
                        **[✦✦----]**:40,000 Mora, Vajrada Amethyst Fragment x3, Perpetual Heart x2, Cor Lapis x10, Whopperflower Nectar x15\n \
                        **[✦✦✦---]**:60,000 Mora, Vajrada Amethyst Fragment x6, Perpetual Heart x4, Cor Lapis x20, Shimmering Nectar x12\n \
                        **[✦✦✦✦--]**:80,000 Mora, Vajrada Amethyst Chunk x3, Perpetual Heart x8, Cor Lapis x30, Shimmering Nectar x18\n \
                        **[✦✦✦✦✦-]**:100,000 Mora, Vajrada Amethyst Chunk x6, Perpetual Heart x12, Cor Lapis x45, Elemental Nectar x12\n \
                        **[✦✦✦✦✦✦]**:120,000 Mora, Vajrada Amethyst Gemstone x6, Perpetual Heart x20, Cor Lapis x60, Elemental Nectar x24',
                        'thum':'https://static.wikia.nocookie.net/genshin-impact/images/0/06/Character_Keqing_Thumb.png/revision/latest/scale-to-width-down/50?cb=20210515120525&path-prefix=th', 'star':'[★★★★★]'}
        return keq
    elif name.lower() == "klee":
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
                        'thum':'https://static.wikia.nocookie.net/genshin-impact/images/c/c3/Character_Klee_Thumb.png/revision/latest/scale-to-width-down/50?cb=20210515120422&path-prefix=th', 'star':'[★★★★★]'}
        return klee
    elif name.lower() == "kujou sara" or name.lower() == "kujou" or name.lower() == "sara":
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
                        'thum':'https://static.wikia.nocookie.net/genshin-impact/images/9/96/Character_Kujou_Sara_Thumb.png/revision/latest/scale-to-width-down/50?cb=20210902012107&path-prefix=th', 'star':'[★★★★]'}
        return kujo
    elif name.lower() == "lisa":
        lisa = {'name':'Lisa', 'his1':'Lisa (ภาษาไทย: ลิซ่า) เป็นตัวละครหญิงธาตุไฟฟ้าใช้อาวุธสื่อเวทที่สามารถเล่นได้ในเกม Genshin Impact\n\n\
            นักเวทย์อดอัจฉริยะผู้เป็นสุดยอดนักปราชญ์ที่เคยจบจากวิทยาลัยสุเมรุมาในระยะเวลา 200 ปี ลิซ่าได้เดินทางกลับมาเมืองมอนด์ชตัดท์เพื่อทำอาชีพเป็นบรรณารักษ์ตัวเล็ก ๆ ให้กับกองอัศวินแห่ง Favonius',\
                        'stat':['9,570', '232', '573', '96', '(Elemental Mastery)'],
                        'ascen':'**[✦-----]**:20,000 Mora, Vajrada Amethyst Sliver x1, Valberry x3, Slime Condensate x3\n \
                        **[✦✦----]**:40,000 Mora, Vajrada Amethyst Fragment x3, Lightning Prism x2, Valberry x10, Slime Condensate x15\n \
                        **[✦✦✦---]**:60,000 Mora, Vajrada Amethyst Fragment x6, Lightning Prism x4, Valberry x20, Slime Secretions x12\n \
                        **[✦✦✦✦--]**:80,000 Mora, Vajrada Amethyst Chunk x3, Lightning Prism x8, Valberry x30, Slime Secretions x18\n \
                        **[✦✦✦✦✦-]**:100,000 Mora, Vajrada Amethyst Chunk x6, Lightning Prism x12, Valberry x45, Slime Concentrate x12\n \
                        **[✦✦✦✦✦✦]**:120,000 Mora, Vajrada Amethyst Gemstone x6, Lightning Prism x20, Valberry x60, Slime Concentrate x24',
                        'thum':'https://static.wikia.nocookie.net/genshin-impact/images/5/51/Character_Lisa_Thumb.png/revision/latest/scale-to-width-down/50?cb=20210515120431&path-prefix=th', 'star':'[★★★★]'}
        return lisa
    elif name.lower() == "mona":
        mona = {'name':'Astrologist Mona Megistus', 'his1':'Astrologist Mona Megistus (ภาษาไทย: โมนา เมจิสตัส) เป็นตัวละครหญิงธาตุน้ำใช้อาวุธสื่อเวทที่สามารถเล่นได้ในเกม Genshin Impact\n\n\
            โหรสาวมากความสามารถและมากความหยิ่งผู้จนตลอดกาล โมนาระหกระเหินมาหาที่อยู่ในเมืองมอนด์ชตัดท์เพื่อหนีโทสะท่านอาจารย์ที่ตัวเองเผลอไปอ่านบันทึกประจำวันเข้า',
                'stat':['10,409', '287', '653', '32.0%', '(Energy Recharge)'],
                'ascen':'**[✦-----]**:20,000 Mora, Varunada Lazurite Sliver x1, Philanemo Mushroom x3, Whopperflower Nectar x3\n \
                        **[✦✦----]**:40,000 Mora, Varunada Lazurite Fragment x3, Cleansing Heart x2, Philanemo Mushroom x10, Whopperflower Nectar x15\n \
                        **[✦✦✦---]**:60,000 Mora, Varunada Lazurite Fragment x6, Cleansing Heart x4, Philanemo Mushroom x20, Shimmering Nectar x12\n \
                        **[✦✦✦✦--]**:80,000 Mora, Varunada Lazurite Chunk x3, Cleansing Heart x8, Philanemo Mushroom x30, Shimmering Nectar x18\n \
                        **[✦✦✦✦✦-]**:100,000 Mora, Varunada Lazurite Chunk x6, Cleansing Heart x12, Philanemo Mushroom x45, Elemental Nectar x12\n \
                        **[✦✦✦✦✦✦]**:120,000 Mora, Varunada Lazurite Gemstone x6, Cleansing Heart x20, Philanemo Mushroom x60, Elemental Nectar x24',
                        'thum':'https://static.wikia.nocookie.net/genshin-impact/images/a/a0/Character_Mona_Thumb.png/revision/latest/scale-to-width-down/50?cb=20210515120940&path-prefix=th', 'star':'[★★★★★]'}
        return mona
    elif name.lower() == "ningguang":
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
                        'thum':'https://static.wikia.nocookie.net/genshin-impact/images/2/2b/Character_Ningguang_Thumb.png/revision/latest/scale-to-width-down/50?cb=20210515120449&path-prefix=th', 'star':'[★★★★★]'}
        return ning
    elif name.lower() == "noelle":
        noel = {'name':'Noelle', 'his1':'Noelle (ภาษาไทย: โนเอลล์) เป็นตัวละครหญิงธาตุหินใช้อาวุธดาบใหญ่ที่สามารถเล่นได้ในเกม Genshin Impact\n\n\
            อัศวินฝึกหัดจอมทรหดและแม่บ้านผู้ไร้เทียมทานประจำกองอัศวินแห่งฟาโวเนียส โนเอลล์มีความฝันว่าสักวันหนึ่งตนจะได้ขึ้นมาเป็นอัศวินเต็มตัวและช่วยเหลือพลเมืองมอนด์ชตัดต์ให้ดียิ่ง ๆ ขึ้นไป',\
                'stat':['12,071', '191', '799', '30.0%', '(DEF Bonus)'],
                'ascen':'**[✦-----]**:20,000 Mora, Prithiva Topaz Sliver x1, Valberry x3, Damaged Mask x3\n \
                        **[✦✦----]**:40,000 Mora, Prithiva Topaz Fragment x3, Basalt Pillar x2, Valberry x10, Damaged Mask x15\n \
                        **[✦✦✦---]**:60,000 Mora, Prithiva Topaz Fragment x6, Basalt Pillar x4, Valberry x20, Stained Mask x12\n \
                        **[✦✦✦✦--]**:80,000 Mora, Prithiva Topaz Chunk x3, Basalt Pillar x8, Valberry x30, Stained Mask x18\n \
                        **[✦✦✦✦✦-]**:100,000 Mora, Prithiva Topaz Chunk x6, Basalt Pillar x12, Valberry x45, Ominous Mask x12\n \
                        **[✦✦✦✦✦✦]**:120,000 Mora, Prithiva Topaz Gemstone x6, Basalt Pillar x20, Valberry x60, Ominous Mask x24',
                        'thum':'https://static.wikia.nocookie.net/genshin-impact/images/a/ab/Character_Noelle_Thumb.png/revision/latest/scale-to-width-down/50?cb=20210515120454&path-prefix=th', 'star':'[★★★★]'}
        return noel
    elif name.lower() == "qiqi":
        qiqi = {'name':'Qiqi', 'his1':'Qiqi (ภาษาไทย: ชีชี; ภาษาจีน: 七七 Qīqī, "เจ็ด เจ็ด") เป็นตัวละครหญิงธาตุน้ำแข็งใช้อาวุธดาบที่สามารถเล่นได้ในเกม Genshin Impact\n\n\
            เด็กสาวที่มีเหล่าเซียนชุบชีวิตขึ้นมาเป็นผีดิบ เธอได้ Baizhu เป็นผู้ปกครองและทำงานอยู่กับ Bubu Pharmacy ในท่าเรือ Liyue',
                'stat':['12,368', '287', '922', '22.2%', '(Healing Bonus)'],
                'ascen':'**[✦-----]**:20,000 Mora, Shivada Jade Sliver x1, Violetgrass x3, Divining Scroll x3\n \
                        **[✦✦----]**:40,000 Mora, Shivada Jade Fragment x3, Hoarfrost Core x2, Violetgrass x10, Divining Scroll x15\n \
                        **[✦✦✦---]**:60,000 Mora, Shivada Jade Fragment x6, Hoarfrost Core x4, Violetgrass x20, Sealed Scroll x12\n \
                        **[✦✦✦✦--]**:80,000 Mora, Shivada Jade Chunk x3, Hoarfrost Core x8, Violetgrass x30, Sealed Scroll x18\n \
                        **[✦✦✦✦✦-]**:100,000 Mora, Shivada Jade Chunk x6, Hoarfrost Core x12, Violetgrass x45, Forbidden Curse Scroll x12\n \
                        **[✦✦✦✦✦✦]**:120,000 Mora, Shivada Jade Gemstone x6, Hoarfrost Core x20, Violetgrass x60, Forbidden Curse Scroll x24',
                        'thum':'https://static.wikia.nocookie.net/genshin-impact/images/d/d5/Character_Qiqi_Thumb.png/revision/latest/scale-to-width-down/50?cb=20210515120459&path-prefix=th', 'star':'[★★★★★]'}
        return qiqi
    elif name.lower() == "raiden shogun" or name.lower() == "raiden" or name.lower() == "shogun" or name.lower() == "ei" or name.lower() == "raiden ei":
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
                        'thum':'https://static.wikia.nocookie.net/genshin-impact/images/5/52/Character_Raiden_Shogun_Thumb.png/revision/latest/scale-to-width-down/50?cb=20210902012044&path-prefix=th', 'star':'[★★★★★]'}
        return raiden
    elif name.lower() == "razor":
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
                        'thum':'https://static.wikia.nocookie.net/genshin-impact/images/1/1d/Character_Razor_Thumb.png/revision/latest/scale-to-width-down/50?cb=20210515120504&path-prefix=th', 'star':'[★★★★]'}
        return razor
    elif name.lower() == "rosaria":
        rosa = {'name':'Rosaria', 'his1':'Rosaria (ภาษาไทย: โรซาเรีย) เป็นตัวละครหญิงธาตุน้ำแข็งใช้อาวุธหอกที่สามารถเล่นได้ใน Genshin Impact\n\n\
            Rosaria หนึ่งในซิสเตอร์ของ Favonius Church แห่ง Mondstadtซิสเตอร์ที่นอกจากการแต่งกายแล้ว ไม่มีสิ่งที่ดูเหมือนสมาชิกทางศาสนาเลย ซิสเตอร์ผู้แสนแปลกแยก เย็นชา และเชือดเฉือน หญิงสาวที่คมราวกับใบมีด',
                'stat':['12,289', '240', '710', '24.0%', '(ATK Bonus)'],
                'ascen':'**[✦-----]**:20,000 Mora, Prithiva Topaz Sliver x1, Glaze Lily x3, Recruit\'s Insignia x3\n \
                        **[✦✦----]**:40,000 Mora, Prithiva Topaz Fragment x3, Basalt Pillar x2, Glaze Lily x10, Recruit\'s Insignia x15\n \
                        **[✦✦✦---]**:60,000 Mora, Prithiva Topaz Fragment x6, Basalt Pillar x4, Glaze Lily x20, Sergeant\'s Insignia x12\n \
                        **[✦✦✦✦--]**:80,000 Mora, Prithiva Topaz Chunk x3, Basalt Pillar x8, Glaze Lily x30, Sergeant\'s Insignia x18\n \
                        **[✦✦✦✦✦-]**:100,000 Mora, Prithiva Topaz Chunk x6, Basalt Pillar x12, Glaze Lily x45, Lieutenant\'s Insignia x12\n \
                        **[✦✦✦✦✦✦]**:120,000 Mora, Prithiva Topaz Gemstone x6, Basalt Pillar x20, Glaze Lily x60, Lieutenant\'s Insignia x24',
                        'thum':'https://static.wikia.nocookie.net/genshin-impact/images/f/f6/Character_Rosaria_Thumb.png/revision/latest/scale-to-width-down/50?cb=20210515120554&path-prefix=th', 'star':'[★★★★]'}
        return rosa