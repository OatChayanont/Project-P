def weapon_info_list(name):
    if name.lower() == "polar star":
        lst = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/4/44/Weapon_Polar_Star.png/revision/latest/scale-to-width-down/256?cb=20211013042349", \
        'his':"ธนูไร้มลทินที่แหลมคม ราวกับแท่งน้ำแข็งในฤดูหนาวที่แสนยาวนาน", 'type':"Bow", 'stat':["608", "33.1%", "CRIT Rate"], \
        'ascen':"**[✦-----]**:10,000 Mora, Mask of the Wicked Lieutenant x5, Concealed Claw x5, Spectral Husk x3\n \
        **[✦✦----]**:20,000 Mora, Mask of the Tiger's Bite x5, Concealed Claw x18, Spectral Husk x12\n \
        **[✦✦✦---]**:30,000 Mora, Mask of the Tiger's Bite x9, Concealed Unguis x9, Spectral Heart x9\n \
        **[✦✦✦✦--]**:45,000 Mora, Mask of the One-Horned x5, Concealed Unguis x18, Spectral Heart x14\n \
        **[✦✦✦✦✦-]**:55,000 Mora, Mask of the One-Horned x9, Concealed Talon x14, Spectral Nucleus x9\n \
        **[✦✦✦✦✦✦]**:65,000 Mora, Mask of the Kijin x6, Concealed Talon x27, Spectral Nucleus x18", 'name':"Polar Star"}
        return lst
    elif name.lower() == "thundering pulse":
        lst2 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/7/77/Weapon_Thundering_Pulse.png/revision/latest/scale-to-width-down/256?cb=20210811094805", \
        'his':"A longbow that was a gift from the Shogun. Eternal lightning crackles all around it.", 'type':"Bow", 'stat':["608", "66.2%", "CRIT DMG"], \
        'ascen':"**[✦-----]**:10,000 Mora, Narukami's Wisdom x5, Dismal Prism x5, Firm Arrowhead x3\n \
        **[✦✦----]**:20,000 Mora, Narukami's Joy x5, Dismal Prism x18, Firm Arrowhead x12\n \
        **[✦✦✦---]**:30,000 Mora, Narukami's Joy x9, Crystal Prism x9, Sharp Arrowhead x9\n \
        **[✦✦✦✦--]**:45,000 Mora, Narukami's Affection x5, Crystal Prism x18, Sharp Arrowhead x14\n \
        **[✦✦✦✦✦-]**:55,000 Mora, Narukami's Affection x9, Polarizing Prism x14, Weathered Arrowhead x9\n \
        **[✦✦✦✦✦✦]**:65,000 Mora, Narukami's Valor x6, Polarizing Prism x27, Weathered Arrowhead x18", 'name':"Thundering Pulse"}
        return lst2
    elif name.lower() == "elegy for the end":
        lst3 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/a/a5/Weapon_Elegy_for_the_End.png/revision/latest/scale-to-width-down/256?cb=20210317075424", \
        'his':"A bow as lovely as any bard's lyre, its arrows pierce the heart like a lamenting sigh.", 'type':"Bow", 'stat':["608", "55.1%", "Energy Recharge"], \
        'ascen':"**[✦-----]**:10,000 Mora, Boreal Wolf's Milk Tooth x5, Heavy Horn x5, Recruit's Insignia x3\n \
        **[✦✦----]**:20,000 Mora, Boreal Wolf's Cracked Tooth x5, Heavy Horn x18, Recruit's Insignia x12\n \
        **[✦✦✦---]**:30,000 Mora, Boreal Wolf's Cracked Tooth x9, Black Bronze Horn x9, Sergeant's Insignia x9\n \
        **[✦✦✦✦--]**:45,000 Mora, Boreal Wolf's Broken Fang x5, Black Bronze Horn x18, Sergeant's Insignia x14\n \
        **[✦✦✦✦✦-]**:55,000 Mora, Boreal Wolf's Broken Fang x9, Black Crystal Horn x14, Black Crystal Horn x9\n \
        **[✦✦✦✦✦✦]**:65,000 Mora, Boreal Wolf's Nostalgia x6, Black Crystal Horn x27, Black Crystal Horn x18", 'name':"Elegy for the End"}
        return lst3
    elif name.lower() == "skyward harp":
        lst4 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/1/19/Weapon_Skyward_Harp.png/revision/latest/scale-to-width-down/256?cb=20201116035246", \
        'his':"A greatbow that symbolizes Dvalin's affiliation with the Anemo Archon. The sound of the bow firing is music to the Anemo Archon's ears. It contains the power of the sky and wind within.", 
        'type':"Bow", 'stat':["674", "22.1%", "CRIT Rate"], \
        'ascen':"**[✦-----]**:10,000 Mora, Boreal Wolf's Milk Tooth x5, Dead Ley Line Branch x5, Firm Arrowhead x3\n \
        **[✦✦----]**:20,000 Mora, Boreal Wolf's Cracked Tooth x5, Dead Ley Line Branch x18, Firm Arrowhead x12\n \
        **[✦✦✦---]**:30,000 Mora, Boreal Wolf's Cracked Tooth x9, Dead Ley Line Leaves x9, Sharp Arrowhead x9\n \
        **[✦✦✦✦--]**:45,000 Mora, Boreal Wolf's Broken Fang x5, Dead Ley Line Leaves x18, Sharp Arrowhead x14\n \
        **[✦✦✦✦✦-]**:55,000 Mora, Boreal Wolf's Broken Fang x9, Ley Line Sprout x14, Weathered Arrowhead x9\n \
        **[✦✦✦✦✦✦]**:65,000 Mora, Boreal Wolf's Nostalgia x6, Ley Line Sprout x27, Weathered Arrowhead x18", 'name':"Skyward Harp"}
        return lst4
    elif name.lower() == "amos' bow":
        lst5 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/d/de/Weapon_Amos%27_Bow.png/revision/latest/scale-to-width-down/256?cb=20201120010513", \
        'his':"An extremely ancient bow that has retained its power despite its original master being long gone. It draws power from everyone and everything in the world, and the further away you are from that which your heart desires, the more powerful it is.", \
        'type':"Bow", 'stat':["608", "49.6%", "ATK"], \
        'ascen':"**[✦-----]**:10,000 Mora, Fetters of the Dandelion Gladiator x5, Chaos Device x5, Slime Condensate x3\n \
        **[✦✦----]**:20,000 Mora, Chains of the Dandelion Gladiator x5, Chaos Device x18, Slime Condensate x12\n \
        **[✦✦✦---]**:30,000 Mora, Chains of the Dandelion Gladiator x9, Chaos Circuit x9, Slime Secretions x9\n \
        **[✦✦✦✦--]**:45,000 Mora, Shackles of the Dandelion Gladiator x5, Chaos Circuit x18, Slime Secretions x14\n \
        **[✦✦✦✦✦-]**:55,000 Mora, Shackles of the Dandelion Gladiator x9, Chaos Core x14, Slime Concentrate x9\n \
        **[✦✦✦✦✦✦]**:65,000 Mora, Dream of the Dandelion Gladiator x6, Chaos Core x27, Slime Concentrate x18", 'name':"Amos' Bow"}
        return lst5
    elif name.lower() == "lost prayer to the sacred winds":
        lst6 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/9/98/Weapon_Lost_Prayer_to_the_Sacred_Winds.png/revision/latest/scale-to-width-down/256?cb=20201116034132", \
        'his':"An educational tome written by anonymous early inhabitants who worshiped the wind. It has been blessed by the wind for its faithfulness and influence over the millennia.", \
        'type':"Catalyst", 'stat':["608", "33.1%", "CRIT Rate"], \
        'ascen':"**[✦-----]**:10,000 Mora, Fetters of the Dandelion Gladiator x5, Chaos Device x5, Slime Condensate x3\n \
        **[✦✦----]**:20,000 Mora, Chains of the Dandelion Gladiator x5, Chaos Device x18, Slime Condensate x12\n \
        **[✦✦✦---]**:30,000 Mora, Chains of the Dandelion Gladiator x9, Chaos Circuit x9, Slime Secretions x9\n \
        **[✦✦✦✦--]**:45,000 Mora, Shackles of the Dandelion Gladiator x5, Chaos Circuit x18, Slime Secretions x14\n \
        **[✦✦✦✦✦-]**:55,000 Mora, Shackles of the Dandelion Gladiator x9, Chaos Core x14, Slime Concentrate x9\n \
        **[✦✦✦✦✦✦]**:65,000 Mora, Dream of the Dandelion Gladiator x6, Chaos Core x27, Slime Concentrate x18", 'name':"Lost Prayer to the Sacred Winds"}
        return lst6
    elif name.lower() == "skyward atlas":
        lst7 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/3/33/Weapon_Skyward_Atlas.png/revision/latest/scale-to-width-down/256?cb=20201116035225", \
        'his':"A cloud atlas symbolizing Dvalin and its former master, the Anemo Archon. It details the winds and clouds of the northern regions and contains the powers of the sky and wind.", \
        'type':"Catalyst", 'stat':["674", "33.1%", "ATK"], \
        'ascen':"**[✦-----]**:10,000 Mora, Boreal Wolf's Milk Tooth x5, Dead Ley Line Branch x5, Firm Arrowhead x3\n \
        **[✦✦----]**:20,000 Mora, Boreal Wolf's Cracked Tooth x5, Dead Ley Line Branch x18, Firm Arrowhead x12\n \
        **[✦✦✦---]**:30,000 Mora, Boreal Wolf's Cracked Tooth x9, Dead Ley Line Leaves x9, Sharp Arrowhead x9\n \
        **[✦✦✦✦--]**:45,000 Mora, Boreal Wolf's Broken Fang x5, Dead Ley Line Leaves x18, Sharp Arrowhead x14\n \
        **[✦✦✦✦✦-]**:55,000 Mora, Boreal Wolf's Broken Fang x9, Ley Line Sprout x14, Weathered Arrowhead x9\n \
        **[✦✦✦✦✦✦]**:65,000 Mora, Boreal Wolf's Nostalgia x6, Ley Line Sprout x27, Weathered Arrowhead x18", 'name':"Skyward Atlas"}
        return lst7
    elif name.lower() == "everlasting moonglow":
        lst8 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/e/e1/Weapon_Everlasting_Moonglow.png/revision/latest/scale-to-width-down/256?cb=20210921104126", \
        'his':"A string of lovely jasper from the deep sea. It shines with a pure radiance like that of the moon, and just as ever-distant.", \
        'type':"Catalyst", 'stat':["608", "49.6%", "HP"], \
        'ascen':"**[✦-----]**:10,000 Mora, Coral Branch of a Distant Sea x5, Dismal Prism x5, Spectral Husk x3\n \
        **[✦✦----]**:20,000 Mora, Jeweled Branch of a Distant Sea x5, Dismal Prism x18, Spectral Husk x12\n \
        **[✦✦✦---]**:30,000 Mora, Jeweled Branch of a Distant Sea x9, Crystal Prism x9, Spectral Heart x9\n \
        **[✦✦✦✦--]**:45,000 Mora, Jade Branch of a Distant Sea x5, Crystal Prism x18, Spectral Heart x14\n \
        **[✦✦✦✦✦-]**:55,000 Mora, Jade Branch of a Distant Sea x9, Polarizing Prism x14, Spectral Nucleus x9\n \
        **[✦✦✦✦✦✦]**:65,000 Mora, Golden Branch of a Distant Sea x6, Polarizing Prism x27, Spectral Nucleus x18", 'name':"Everlasting Moonglow"}
        return lst8
    elif name.lower() == "memory of dust":
        lst9 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/c/ca/Weapon_Memory_of_Dust.png/revision/latest/scale-to-width-down/256?cb=20201119232148", \
        'his':"A stone dumbbell containing distant memories. Its endless transformations reveal the power within.", \
        'type':"Catalyst", 'stat':["608", "49.6%", "ATK"], \
        'ascen':"**[✦-----]**:10,000 Mora, Grain of Aerosiderite x5, Fragile Bone Shard x5, Damaged Mask x3\n \
        **[✦✦----]**:20,000 Mora, Piece of Aerosiderite x5, Fragile Bone Shard x18, Damaged Mask x12\n \
        **[✦✦✦---]**:30,000 Mora, Piece of Aerosiderite x9, Sturdy Bone Shard x9, Stained Mask x9\n \
        **[✦✦✦✦--]**:45,000 Mora, Bit of Aerosiderite x5, Sturdy Bone Shard x18, Stained Mask x14\n \
        **[✦✦✦✦✦-]**:55,000 Mora, Bit of Aerosiderite x9, Fossilized Bone Shard x14, Ominous Mask x9\n \
        **[✦✦✦✦✦✦]**:65,000 Mora, Chunk of Aerosiderite x6, Fossilized Bone Shard x27, Ominous Mask x18", 'name':"Memory of Dust"}
        return lst9
    elif name.lower() == "wolf's gravestone":
        lst10 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/4/4f/Weapon_Wolf%27s_Gravestone.png/revision/latest/scale-to-width-down/256?cb=20201116035623", \
        'his':"A longsword used by the Wolf Knight. Originally just a heavy sheet of iron given to the knight by a blacksmith from the city, it became endowed with legendary power owing to his friendship with the wolves.", \
        'type':"Claymore", 'stat':["608", "49.6%", "ATK"], \
        'ascen':"**[✦-----]**:10,000 Mora, Fetters of the Dandelion Gladiator x5, Chaos Device x5, Divining Scroll x3\n \
        **[✦✦----]**:20,000 Mora, Chains of the Dandelion Gladiator x5, Chaos Device x18, Divining Scroll x12\n \
        **[✦✦✦---]**:30,000 Mora, Chains of the Dandelion Gladiator x9, Chaos Circuit x9, Sealed Scroll x9\n \
        **[✦✦✦✦--]**:45,000 Mora, Shackles of the Dandelion Gladiator x5, Chaos Circuit x18, Sealed Scroll x14\n \
        **[✦✦✦✦✦-]**:55,000 Mora, Shackles of the Dandelion Gladiator x9, Chaos Core x14, Forbidden Curse Scroll x9\n \
        **[✦✦✦✦✦✦]**:65,000 Mora, Dream of the Dandelion Gladiator x6, Chaos Core x27, Forbidden Curse Scroll x18", 'name':"Wolf's Gravestone"}
        return lst10
    elif name.lower() == "skyward pride":
        lst11 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/0/0b/Weapon_Skyward_Pride.png/revision/latest/scale-to-width-down/256?cb=20201116035255", \
        'his':"A claymore that symbolizes the pride of Dvalin soaring through the skies. When swung, it emits a deep hum as the full force of Dvalin's command of the sky and the wind is unleashed.", \
        'type':"Claymore", 'stat':["674", "36.8%", "Energy Recharge"], \
        'ascen':"**[✦-----]**:10,000 Mora, Boreal Wolf's Milk Tooth x5, Dead Ley Line Branch x5, Slime Condensate x3\n \
        **[✦✦----]**:20,000 Mora, Boreal Wolf's Cracked Tooth x5, Dead Ley Line Branch x18, Slime Condensate x12\n \
        **[✦✦✦---]**:30,000 Mora, Boreal Wolf's Cracked Tooth x9, Dead Ley Line Leaves x9, Slime Secretions x9\n \
        **[✦✦✦✦--]**:45,000 Mora, Boreal Wolf's Broken Fang x5, Dead Ley Line Leaves x18, Slime Secretions x14\n \
        **[✦✦✦✦✦-]**:55,000 Mora, Boreal Wolf's Broken Fang x9, Ley Line Sprout x14, Slime Concentrate x9\n \
        **[✦✦✦✦✦✦]**:65,000 Mora, Boreal Wolf's Nostalgia x6, Ley Line Sprout x27, Slime Concentrate x18", 'name':"Skyward Pride"}
        return lst11
    elif name.lower() == "the unforged":
        lst12 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/f/f7/Weapon_The_Unforged.png/revision/latest/scale-to-width-down/256?cb=20201129060814", \
        'his':"Capable of driving away evil spirits and wicked people alike, this edgeless claymore seems to possess divine might.", \
        'type':"Claymore", 'stat':["608", "49.6%", "ATK"], \
        'ascen':"**[✦-----]**:10,000 Mora, Mist Veiled Lead Elixir x5, Mist Grass Pollen x5, Treasure Hoarder Insignia x3\n \
        **[✦✦----]**:20,000 Mora, Mist Veiled Mercury Elixir x5, Mist Grass Pollen x18, Treasure Hoarder Insignia x12\n \
        **[✦✦✦---]**:30,000 Mora, Mist Veiled Mercury Elixir x9, Mist Grass x9, Silver Raven Insignia x9\n \
        **[✦✦✦✦--]**:45,000 Mora, Mist Veiled Gold Elixir x5, Mist Grass x18, Silver Raven Insignia x14\n \
        **[✦✦✦✦✦-]**:55,000 Mora, Mist Veiled Gold Elixir x9, Mist Grass Wick x14, Golden Raven Insignia x9\n \
        **[✦✦✦✦✦✦]**:65,000 Mora, Mist Veiled Primo Elixir x6, Mist Grass Wick x27, Golden Raven Insignia x18", 'name':"The Unforged"}
        return lst12
    elif name.lower() == "song of broken pines":
        lst13 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/d/dd/Weapon_Song_of_Broken_Pines.png/revision/latest/scale-to-width-down/256?cb=20210518151739", \
        'his':"A greatsword as light as the sigh of grass in the breeze, yet as merciless to the corrupt as a typhoon.", \
        'type':"Claymore", 'stat':["741", "20.7%", "Physical DMG Bonus"], \
        'ascen':"**[✦-----]**:10,000 Mora, Tile of Decarabian's Tower x5, Heavy Horn x5, Damaged Mask x3\n \
        **[✦✦----]**:20,000 Mora, Debris of Decarabian's City x5, Heavy Horn x18, Damaged Mask x12\n \
        **[✦✦✦---]**:30,000 Mora, Debris of Decarabian's City x9, Black Bronze Horn x9, Stained Mask x9\n \
        **[✦✦✦✦--]**:45,000 Mora, Fragment of Decarabian's Epic x5, Black Bronze Horn x18, Stained Mask x14\n \
        **[✦✦✦✦✦-]**:55,000 Mora, Fragment of Decarabian's Epic x9, Black Crystal Hornx14, Ominous Mask x9\n \
        **[✦✦✦✦✦✦]**:65,000 Mora, Scattered Piece of Decarabian's Dream x6, Black Crystal Horn x27, Ominous Mask x18", 'name':"Song of Broken Pines"}
        return lst13
    elif name.lower() == "engulfing lightning":
        lst14 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/2/21/Weapon_Engulfing_Lightning.png/revision/latest/scale-to-width-down/256?cb=20210901044846", \
        'his':'A naginata used to "cut grass." Any army that stands before this weapon will probably be likewise cut down...', \
        'type':"Polearm", 'stat':["608", "55.1%", "Energy Recharge"], \
        'ascen':"**[✦-----]**:10,000 Mora, Mask of the Wicked Lieutenant x5, Chaos Gear x5, Old Handguard x3\n \
        **[✦✦----]**:20,000 Mora, Mask of the Tiger's Bite x5, Chaos Gear x18, Old Handguard x12\n \
        **[✦✦✦---]**:30,000 Mora, Mask of the Tiger's Bite x9, Chaos Axis x9, Kageuchi Handguard x9\n \
        **[✦✦✦✦--]**:45,000 Mora, Mask of the One-Horned x5, Chaos Axis x18, Kageuchi Handguard x14\n \
        **[✦✦✦✦✦-]**:55,000 Mora, Mask of the One-Horned x9, Chaos Oculus x14, Famed Handguard x9\n \
        **[✦✦✦✦✦✦]**:65,000 Mora, Mask of the Kijin x6, Chaos Oculus x27, Famed Handguard x18", 'name':"Engulfing Lightning"}
        return lst14
    elif name.lower() == "skyward spine":
        lst15 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/6/69/Weapon_Skyward_Spine.png/revision/latest/scale-to-width-down/256?cb=20201116035301", \
        'his':"A polearm that symbolizes Dvalin's fire resolve. The upright shaft of this weapon points towards the heavens, clad in the might of sky and wind.", \
        'type':"Polearm", 'stat':["674", "36.8%", "Energy Recharge"], \
        'ascen':"**[✦-----]**:10,000 Mora, Fetters of the Dandelion Gladiator x5, Chaos Device x5, Divining Scroll x3\n \
        **[✦✦----]**:20,000 Mora, Chains of the Dandelion Gladiator x5, Chaos Device x18, Divining Scroll x12\n \
        **[✦✦✦---]**:30,000 Mora, Chains of the Dandelion Gladiator x9, Chaos Circuit x9, Sealed Scroll x9\n \
        **[✦✦✦✦--]**:45,000 Mora, Shackles of the Dandelion Gladiator x5, Chaos Circuit x18, Sealed Scroll x14\n \
        **[✦✦✦✦✦-]**:55,000 Mora, Shackles of the Dandelion Gladiator x9, Chaos Core x14, Forbidden Curse Scroll x9\n \
        **[✦✦✦✦✦✦]**:65,000 Mora, Dream of the Dandelion Gladiator x6, Chaos Core x27, Forbidden Curse Scroll x18", 'name':"Skyward Spine"}
        return lst15
    elif name.lower() == "primordial jade winged-spear":
        lst16 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/8/80/Weapon_Primordial_Jade_Winged-Spear.png/revision/latest/scale-to-width-down/256?cb=20201116152024", \
        'his':"A jade polearm made by the archons, capable of slaying ancient beasts.", \
        'type':"Polearm", 'stat':["674", "22.1%", "CRIT Rate"], \
        'ascen':"**[✦-----]**:10,000 Mora, Luminous Sands from Guyun x5, Hunter's Sacrificial Knife x5, Recruit's Insignia x3\n \
        **[✦✦----]**:20,000 Mora, Lustrous Stone from Guyun x5, Hunter's Sacrificial Knife x18, Recruit's Insignia x12\n \
        **[✦✦✦---]**:30,000 Mora, Lustrous Stone from Guyun x9, Agent's Sacrificial Knife x9, Sergeant's Insignia x9\n \
        **[✦✦✦✦--]**:45,000 Mora, Relic from Guyun x5, Agent's Sacrificial Knife x18, Sergeant's Insignia x14\n \
        **[✦✦✦✦✦-]**:55,000 Mora, Relic from Guyun x9, Inspector's Sacrificial Knife x14, Lieutenant's Insignia x9\n \
        **[✦✦✦✦✦✦]**:65,000 Mora, Divine Body from Guyun x6, Inspector's Sacrificial Knife x27, Lieutenant's Insignia x18", 'name':"Primordial Jade Winged-Spear"}
        return lst16
    elif name.lower() == "staff of homa":
        lst17 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/1/17/Weapon_Staff_of_Homa.png/revision/latest/scale-to-width-down/256?cb=20210225200935", \
        'his':'A "firewood staff" that was once used in ancient and long-lost rituals.', \
        'type':"Polearm", 'stat':["608", "66.2%", "CRIT DMG"], \
        'ascen':"**[✦-----]**:10,000 Mora, Grain of Aerosiderite x5, Dead Ley Line Branch x5, Slime Condensate x3\n \
        **[✦✦----]**:20,000 Mora, Piece of Aerosiderite x5, Dead Ley Line Branch x18, Slime Condensate x12\n \
        **[✦✦✦---]**:30,000 Mora, Piece of Aerosiderite x9, Dead Ley Line Leaves x9, Slime Secretions x9\n \
        **[✦✦✦✦--]**:45,000 Mora, Bit of Aerosiderite x5, Dead Ley Line Leaves x18, Slime Secretions x14\n \
        **[✦✦✦✦✦-]**:55,000 Mora, Bit of Aerosiderite x9, Ley Line Sprout x14, Slime Concentrate x9\n \
        **[✦✦✦✦✦✦]**:65,000 Mora, Chunk of Aerosiderite x6, Ley Line Sprout x27, Slime Concentrate x18", 'name':"Staff of Homa"}
        return lst17
    elif name.lower() == "vortex vanquisher":
        lst18 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/d/d6/Weapon_Vortex_Vanquisher.png/revision/latest/scale-to-width-down/256?cb=20201129060822", \
        'his':"This sharp polearm can seemingly pierce through anything. When swung, one can almost see the rift it tears in the air.", \
        'type':"Polearm", 'stat':["608", "49.6%", "ATK"], \
        'ascen':"**[✦-----]**:10,000 Mora, Grain of Aerosiderite x5, Fragile Bone Shard x5, Treasure Hoarder Insignia x3\n \
        **[✦✦----]**:20,000 Mora, Piece of Aerosiderite x5, Fragile Bone Shard x18, Treasure Hoarder Insignia x12\n \
        **[✦✦✦---]**:30,000 Mora, Piece of Aerosiderite x9, Sturdy Bone Shard x9, Silver Raven Insignia x9\n \
        **[✦✦✦✦--]**:45,000 Mora, Bit of Aerosiderite x5, Sturdy Bone Shard x18, Silver Raven Insignia x14\n \
        **[✦✦✦✦✦-]**:55,000 Mora, Bit of Aerosiderite x9, Fossilized Bone Shard x14, Golden Raven Insignia x9\n \
        **[✦✦✦✦✦✦]**:65,000 Mora, Chunk of Aerosiderite x6, Fossilized Bone Shard x27, Golden Raven Insignia x18", 'name':"Vortex Vanquisher"}
        return lst18
    elif name.lower() == "mistsplitter reforged":
        lst19 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/0/09/Weapon_Mistsplitter_Reforged.png/revision/latest/scale-to-width-down/350?cb=20210721035408", \
        'his':'A sword that blazes with a fierce violet light. The name "Reforged" comes from it having been broken once before.', \
        'type':"Sword", 'stat':["674", "44.1%", "CRIT DMG"], \
        'ascen':"**[✦-----]**:10,000 Mora, Coral Branch of a Distant Sea x5, Chaos Gear x5, Old Handguard x3\n \
        **[✦✦----]**:20,000 Mora, Jeweled Branch of a Distant Sea x5, Chaos Gear x18, Old Handguard x12\n \
        **[✦✦✦---]**:30,000 Mora, Jeweled Branch of a Distant Sea x9, Chaos Axis x9, Kageuchi Handguard x9\n \
        **[✦✦✦✦--]**:45,000 Mora, Jade Branch of a Distant Sea x5, Chaos Axis x18, Kageuchi Handguard x14\n \
        **[✦✦✦✦✦-]**:55,000 Mora, Jade Branch of a Distant Sea x9, Chaos Oculus x14, Famed Handguard x9\n \
        **[✦✦✦✦✦✦]**:65,000 Mora, Golden Branch of a Distant Sea x6, Chaos Oculus x27, Famed Handguard x18", 'name':"Mistsplitter Reforged	"}
        return lst19
    elif name.lower() == "aquila favonia":
        lst20 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/6/6a/Weapon_Aquila_Favonia.png/revision/latest/scale-to-width-down/256?cb=20201120002750", \
        'his':"The soul of the Knights of Favonius. Millennia later, it still calls on the winds of swift justice to vanquish all evil—just like the last heroine who wielded it.", \
        'type':"Sword", 'stat':["674", "41.3%", "Physical DMG"], \
        'ascen':"**[✦-----]**:10,000 Mora, Tile of Decarabian's Tower x5, Heavy Horn x5, Firm Arrowhead x3\n \
        **[✦✦----]**:20,000 Mora, Debris of Decarabian's City x5, Heavy Horn x18, Firm Arrowhead x12\n \
        **[✦✦✦---]**:30,000 Mora, Debris of Decarabian's City x9, Black Bronze Horn x9, Sharp Arrowhead x9\n \
        **[✦✦✦✦--]**:45,000 Mora, Fragment of Decarabian's Epic x5, Black Bronze Horn x18, Sharp Arrowhead x14\n \
        **[✦✦✦✦✦-]**:55,000 Mora, Fragment of Decarabian's Epic x9, Black Crystal Horn x14, Weathered Arrowhead x9\n \
        **[✦✦✦✦✦✦]**:65,000 Mora, Scattered Piece of Decarabian's Dream x6, Black Crystal Horn x27, Weathered Arrowhead x18", 'name':"Aquila Favonia"}
        return lst20
    elif name.lower() == "summit shaper":
        lst21 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/c/ca/Weapon_Summit_Shaper.png/revision/latest/scale-to-width-down/256?cb=20201223042936", \
        'his':"A symbol of a legendary pact, this sharp blade once cut off the peak of a mountain.", \
        'type':"Sword", 'stat':["608", "49.6%", "CRIT Rate"], \
        'ascen':"**[✦-----]**:10,000 Mora, Luminous Sands from Guyun x5, Hunter's Sacrificial Knife x5, Damaged Mask x3\n \
        **[✦✦----]**:20,000 Mora, Lustrous Stone from Guyun x5, Hunter's Sacrificial Knife x18, Damaged Mask x12\n \
        **[✦✦✦---]**:30,000 Mora, Lustrous Stone from Guyun x9, Agent's Sacrificial Knife x9, Stained Mask x9\n \
        **[✦✦✦✦--]**:45,000 Mora, Relic from Guyun x5, Agent's Sacrificial Knife x18, Stained Mask x14\n \
        **[✦✦✦✦✦-]**:55,000 Mora, Relic from Guyun x9, Inspector's Sacrificial Knife x14, Ominous Mask x9\n \
        **[✦✦✦✦✦✦]**:65,000 Mora, Divine Body from Guyun x6, Inspector's Sacrificial Knife x27, Ominous Mask x18", 'name':"Summit Shaper"}
        return lst21
    elif name.lower() == "skyward blade":
        lst22 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/0/03/Weapon_Skyward_Blade.png/revision/latest/scale-to-width-down/256?cb=20201116035239", \
        'his':"The sword of a knight that symbolizes the restored honor of Dvalin. The blessings of the Anemo Archon rest on the fuller of the blade, imbuing the sword with the powers of the sky and the wind.", \
        'type':"Sword", 'stat':["608", "55.1%", "Energy Recharge"], \
        'ascen':"**[✦-----]**:10,000 Mora, Boreal Wolf's Milk Tooth x5, Dead Ley Line Branch x5, Slime Condensate x3\n \
        **[✦✦----]**:20,000 Mora, Boreal Wolf's Cracked Tooth x5, Dead Ley Line Branch x18, Slime Condensate x12\n \
        **[✦✦✦---]**:30,000 Mora, Boreal Wolf's Cracked Tooth x9, Dead Ley Line Leaves x9, Slime Secretions x9\n \
        **[✦✦✦✦--]**:45,000 Mora, Boreal Wolf's Broken Fang x5, Dead Ley Line Leaves x18, Slime Secretions x14\n \
        **[✦✦✦✦✦-]**:55,000 Mora, Boreal Wolf's Broken Fang x9, Ley Line Sprout x14, Slime Concentrate x9\n \
        **[✦✦✦✦✦✦]**:65,000 Mora, Boreal Wolf's Nostalgia x6, Ley Line Sprout x27, Slime Concentrate x18", 'name':"Skyward Blade"}
        return lst22
    elif name.lower() == "freedom-sworn":
        lst23 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/3/39/Weapon_Freedom-Sworn.png/revision/latest/scale-to-width-down/256?cb=20210629202549", \
        'his':"A straight sword, azure as antediluvian song, and as keen as the oaths of freedom taken in the Land of Wind.", \
        'type':"Sword", 'stat':["608", "198", "Elemental Mastery"], \
        'ascen':"**[✦-----]**:10,000 Mora, Fetters of the Dandelion Gladiator x5, Chaos Device x5, Divining Scroll x3\n \
        **[✦✦----]**:20,000 Mora, Chains of the Dandelion Gladiator x5, Chaos Device x18, Divining Scroll x12\n \
        **[✦✦✦---]**:30,000 Mora, Chains of the Dandelion Gladiator x9, Chaos Circuit x9, Sealed Scroll x9\n \
        **[✦✦✦✦--]**:45,000 Mora, Shackles of the Dandelion Gladiator x5, Chaos Circuit x18, Sealed Scroll x14\n \
        **[✦✦✦✦✦-]**:55,000 Mora, Shackles of the Dandelion Gladiator x9, Chaos Core x14, Forbidden Curse Scroll x9\n \
        **[✦✦✦✦✦✦]**:65,000 Mora, Dream of the Dandelion Gladiator x6, Chaos Core x27, Forbidden Curse Scroll x18", 'name':"Freedom-Sworn"}
        return lst23
    elif name.lower() == "primordial jade cutter":
        lst24 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/2/2a/Weapon_Primordial_Jade_Cutter.png/revision/latest/scale-to-width-down/256?cb=20210319202419", \
        'his':"A ceremonial sword masterfully carved from pure jade. There almost seems to be an audible sigh in the wind as it is swung.", \
        'type':"Sword", 'stat':["542", "44.1%", "CRIT Rate"], \
        'ascen':"**[✦-----]**:10,000 Mora, Mist Veiled Lead Elixir x5, Mist Grass Pollen x5, Treasure Hoarder Insignia x3\n \
        **[✦✦----]**:20,000 Mora, Mist Veiled Mercury Elixir x5, Mist Grass Pollen x18, Treasure Hoarder Insignia x12\n \
        **[✦✦✦---]**:30,000 Mora, Mist Veiled Mercury Elixir x9, Mist Grass x9, Silver Raven Insignia x9\n \
        **[✦✦✦✦--]**:45,000 Mora, Mist Veiled Gold Elixir x5, Mist Grass x18, Silver Raven Insignia x14\n \
        **[✦✦✦✦✦-]**:55,000 Mora, Mist Veiled Gold Elixir x9, Mist Grass Wick x14, Golden Raven Insignia x9\n \
        **[✦✦✦✦✦✦]**:65,000 Mora, Mist Veiled Primo Elixir x6, Mist Grass Wick x27, Golden Raven Insignia x18", 'name':"Primordial Jade Cutter"}
        return lst24
    elif name.lower() == "alley hunter":
        lst25 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/0/0a/Weapon_Alley_Hunter.png/revision/latest/scale-to-width-down/256?cb=20210413212830", \
        'his':"ธนูยาวที่ดูสวยงามประณีต ครั้งหนึ่งเคยเป็นของจอมโจรผู้รักความยุติธรรมและยังไม่เคยถูกจับได้", \
        'type':"Bow", 'stat':["565", "27.6%", "ATK"], \
        'ascen':"**[✦-----]**:5,000 Mora, Fetters of the Dandelion Gladiator x3, Chaos Device x3, Slime Condensate x2\n \
        **[✦✦----]**:15,000 Mora, Chains of the Dandelion Gladiator x3, Chaos Device x12, Slime Condensate x8\n \
        **[✦✦✦---]**:20,000 Mora, Chains of the Dandelion Gladiator x6, Chaos Circuit x6, Slime Secretions x6\n \
        **[✦✦✦✦--]**:30,000 Mora, Shackles of the Dandelion Gladiator x3, Chaos Circuit x12, Slime Secretions x9\n \
        **[✦✦✦✦✦-]**:35,000 Mora, Shackles of the Dandelion Gladiator x6, Chaos Core x9, Slime Concentrate x6\n \
        **[✦✦✦✦✦✦]**:45,000 Mora, Dream of the Dandelion Gladiator x4, Chaos Core x18, Slime Concentrate x12", 'name':"Alley Hunter"}
        return lst25
    elif name.lower() == "the viridescent hunt":
        lst26 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/f/ff/Weapon_The_Viridescent_Hunt.png/revision/latest/scale-to-width-down/256?cb=20201120010331", \
        'his':"ธนูล่าสัตว์สีขาวบริสุทธิ์ ครั้งหนึ่งเคยเป็นของใครบางคนที่ออกล่าอยู่ในป่า", \
        'type':"Bow", 'stat':["510", "27.6%", "CRIT Rate"], \
        'ascen':"**[✦-----]**:5,000 Mora, Tile of Decarabian's Tower x3, Heavy Horn x3, Firm Arrowhead x2\n \
        **[✦✦----]**:15,000 Mora, Debris of Decarabian's City x3, Heavy Horn x12, Firm Arrowhead x8\n \
        **[✦✦✦---]**:20,000 Mora, Debris of Decarabian's City x6, Black Bronze Horn x6, Sharp Arrowhead x6\n \
        **[✦✦✦✦--]**:30,000 Mora, Fragment of Decarabian's Epic x3, Black Bronze Horn x12, Sharp Arrowhead x9\n \
        **[✦✦✦✦✦-]**:35,000 Mora, Fragment of Decarabian's Epic x6, Black Crystal Horn x9, Weathered Arrowhead x6\n \
        **[✦✦✦✦✦✦]**:45,000 Mora, Scattered Piece of Decarabian's Dream x4, Black Crystal Horn x18, Weathered Arrowhead x12", 'name':"The Viridescent Hunt"}
        return lst26
    elif name.lower() == "the stringless":
        lst27 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/7/71/Weapon_The_Stringless.png/revision/latest/scale-to-width-down/256?cb=20201116035406", \
        'his':"คันธนูที่ครั้งหนึ่งเคยเป็นเครื่องตนตรีที่แสนวิเศษ แต่ในตอนนี้มันไม่สามารถทำให้ผู้คนลุกขึ้นเพื่อเต้นร่าได้อีกต่อไปแล้ว", \
        'type':"Bow", 'stat':["510", "165", "Elemental Mastery"], \
        'ascen':"**[✦-----]**:5,000 Mora, Tile of Decarabian's Tower x3, Heavy Horn x3, Firm Arrowhead x2\n \
        **[✦✦----]**:15,000 Mora, Debris of Decarabian's City x3, Heavy Horn x12, Firm Arrowhead x8\n \
        **[✦✦✦---]**:20,000 Mora, Debris of Decarabian's City x6, Black Bronze Horn x6, Sharp Arrowhead x6\n \
        **[✦✦✦✦--]**:30,000 Mora, Fragment of Decarabian's Epic x3, Black Bronze Horn x12, Sharp Arrowhead x9\n \
        **[✦✦✦✦✦-]**:35,000 Mora, Fragment of Decarabian's Epic x6, Black Crystal Horn x9, Weathered Arrowhead x6\n \
        **[✦✦✦✦✦✦]**:45,000 Mora, Scattered Piece of Decarabian's Dream x4, Black Crystal Horn x18, Weathered Arrowhead x12", 'name':"The Stringless"}
        return lst27
    elif name.lower() == "sacrificial bow":
        lst28 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/e/ec/Weapon_Sacrificial_Bow.png/revision/latest/scale-to-width-down/256?cb=20201120002607", \
        'his':"คันธนูนักล่าที่ตกแต่งสวยงาม และกลายเป็นหินด้วยกาลเวลา ของที่ตกแต่งคันธนูยังคงเห็นได้อยู่ และมันให้พลังกับผู้ใช้เพื่อรับมือกับสายลมแห่งเวลา", \
        'type':"Bow", 'stat':["565", "30.6%", "Energy Recharge"], \
        'ascen':"**[✦-----]**:5,000 Mora, Boreal Wolf's Milk Tooth x3, Dead Ley Line Branch x3, Slime Condensate x2\n \
        **[✦✦----]**:15,000 Mora, Boreal Wolf's Cracked Tooth x3, Dead Ley Line Branch x12, Slime Condensate x8\n \
        **[✦✦✦---]**:20,000 Mora, Boreal Wolf's Cracked Tooth x6, Dead Ley Line Leaves x6, Slime Secretions x6\n \
        **[✦✦✦✦--]**:30,000 Mora, Boreal Wolf's Broken Fang x3, Dead Ley Line Leaves x12, Slime Secretions x9\n \
        **[✦✦✦✦✦-]**:35,000 Mora, Boreal Wolf's Broken Fang x6, Ley Line Sprout x9, Slime Concentrate x6\n \
        **[✦✦✦✦✦✦]**:45,000 Mora, Boreal Wolf's Nostalgia x4, Ley Line Sprout x18, Slime Concentrate x12", 'name':"Sacrificial Bow"}
        return lst28
    elif name.lower() == "rust":
        lst29 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/1/1c/Weapon_Rust.png/revision/latest/scale-to-width-down/256?cb=20201120002437", \
        'his':"คันธนูเหล็กขนาดใหญ่ที่เต็มไปด้วยสนิมซึ่งคนธรรมดานั้นไม่สามารถยกขึ้นได้เลย คงไม่ต้องพูดถึงการใช้มันเพื่อยิงธนูหรอกนะ", \
        'type':"Bow", 'stat':["510", "41.3%", "ATK"], \
        'ascen':"**[✦-----]**:5,000 Mora, Luminous Sands from Guyun x3, Hunter's Sacrificial Knife x3, Damaged Mask x2\n \
        **[✦✦----]**:15,000 Mora, Lustrous Stone from Guyun x3, Hunter's Sacrificial Knife x12, Damaged Mask x8\n \
        **[✦✦✦---]**:20,000 Mora, Lustrous Stone from Guyun x6, Agent's Sacrificial Knife x6, Stained Mask x6\n \
        **[✦✦✦✦--]**:30,000 Mora, Relic from Guyun x3, Agent's Sacrificial Knife x12, Stained Mask x9\n \
        **[✦✦✦✦✦-]**:35,000 Mora, Relic from Guyun x6, Inspector's Sacrificial Knife x9, Ominous Mask x6\n \
        **[✦✦✦✦✦✦]**:45,000 Mora, Divine Body from Guyun x4, Inspector's Sacrificial Knife x18, Ominous Mask x12", 'name':"Rust"}
        return lst29
    elif name.lower() == "royal row":
        lst30 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/9/99/Weapon_Royal_Bow.png/revision/latest/scale-to-width-down/256?cb=20201120002134", \
        'his':"คันธนูยาวสภาพเก่าแก่ของชนชั้นสูงผู้ที่ครั้งหนึ่งเคยปกครอง Mondstadt มาก่อน แม้ว่าเวลาผ่านไปหลายยุคหลายสมัยแต่สายเอ็นของธนูก็ยังคงแข็งตึงและสามารถยิงลูกธนูออกไปได้อย่างรุนแรง", \
        'type':"Bow", 'stat':["510", "41.3%", "ATK"], \
        'ascen':"**[✦-----]**:5,000 Mora, Fetters of the Dandelion Gladiator x3, Chaos Device x3, Slime Condensate x2\n \
        **[✦✦----]**:15,000 Mora, Chains of the Dandelion Gladiator x3, Chaos Device x12, Slime Condensate x8\n \
        **[✦✦✦---]**:20,000 Mora, Chains of the Dandelion Gladiator x6, Chaos Circuit x6, Slime Secretions x6\n \
        **[✦✦✦✦--]**:30,000 Mora, Shackles of the Dandelion Gladiator x3, Chaos Circuit x12, Slime Secretions x9\n \
        **[✦✦✦✦✦-]**:35,000 Mora, Shackles of the Dandelion Gladiator x6, Chaos Core x9, Slime Concentrate x6\n \
        **[✦✦✦✦✦✦]**:45,000 Mora, Dream of the Dandelion Gladiator x4, Chaos Core x18, Slime Concentrate x12", 'name':"Royal Bow"}
        return lst30
    elif name.lower() == "predator":
        lst31 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/f/fe/Weapon_The_Predator.png/revision/latest/scale-to-width-down/256?cb=20210901042402", \
        'his':"ธนูที่มีสไตล์การออกแบบที่ค่อนข้างเป็นเอกลักษณ์ ดูแล้วไม่น่าจะเป็นสิ่งของของโลกใบนี้", \
        'type':"Bow", 'stat':["510", "41.3%", "ATK"], \
        'ascen':"**[✦-----]**:5,000 Mora, Narukami's Wisdom x3, Dismal Prism x3, Firm Arrowhead x2\n \
        **[✦✦----]**:15,000 Mora, Narukami's Joy x3, Dismal Prism x12, Firm Arrowhead x8\n \
        **[✦✦✦---]**:20,000 Mora, Narukami's Joy x6, Crystal Prism x6, Sharp Arrowhead x6\n \
        **[✦✦✦✦--]**:30,000 Mora, Narukami's Affection x3, Crystal Prism x12, Sharp Arrowhead x9\n \
        **[✦✦✦✦✦-]**:35,000 Mora, Narukami's Affection x6, Polarizing Prism x9, Weathered Arrowhead x6\n \
        **[✦✦✦✦✦✦]**:45,000 Mora, Narukami's Valor x4, Polarizing Prism x18, Weathered Arrowhead x12", 'name':"Predator"}
        return lst31
    elif name.lower() == "prototype crescent":
        lst32 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/4/43/Weapon_Prototype_Crescent.png/revision/latest/scale-to-width-down/256?cb=20201116034737", \
        'his':"คันธนูยาวต้นแบบที่ค้นพบใน Blackcliff Forge ลูกธนูยิงออกมาจากธนูนี้เปล่งประกายราวกับแสงจันทร์", \
        'type':"Bow", 'stat':["510", "41.3%", "ATK"], \
        'ascen':"**[✦-----]**:5,000 Mora, Mist Veiled Lead Elixir x3, Mist Grass Pollen x3, Treasure Hoarder Insignia x2\n \
        **[✦✦----]**:15,000 Mora, Mist Veiled Mercury Elixir x3, Mist Grass Pollen x12, Treasure Hoarder Insignia x8\n \
        **[✦✦✦---]**:20,000 Mora, Mist Veiled Mercury Elixir x6, Mist Grass x6, Silver Raven Insignia x6\n \
        **[✦✦✦✦--]**:30,000 Mora, Mist Veiled Gold Elixir x3, Mist Grass x12, Silver Raven Insignia x9\n \
        **[✦✦✦✦✦-]**:35,000 Mora, Mist Veiled Gold Elixir x6, Mist Grass Wick x9, Golden Raven Insignia x6\n \
        **[✦✦✦✦✦✦]**:45,000 Mora, Mist Veiled Primo Elixir x4, Mist Grass Wick x18, Golden Raven Insignia x12", 'name':"Prototype Crescent"}
        return lst32
    elif name.lower() == "mouun's moon":
        lst33 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/4/42/Weapon_Mouun%27s_Moon.png/revision/latest/scale-to-width-down/256?cb=20211106232751", \
        'his':"ธนูสงครามอันงดงามที่ทำขึ้นจากเปลือกหอยและปะการัง ประกายอันเศร้าสร้อยอาบไว้ไปบนคันธนูสีแสงจันทร์", \
        'type':"Bow", 'stat':["565", "27.6%", "ATK"], \
        'ascen':"**[✦-----]**:5,000 Mora, Narukami's Wisdom x3, Dismal Prism x3, Spectral Husk x2\n \
        **[✦✦----]**:15,000 Mora, Narukami's Joy x3, Dismal Prism x12, Spectral Husk x8\n \
        **[✦✦✦---]**:20,000 Mora, Narukami's Joy x6, Crystal Prism x6, Spectral Heart x6\n \
        **[✦✦✦✦--]**:30,000 Mora, Narukami's Affection x3, Crystal Prism x12, Spectral Heart x9\n \
        **[✦✦✦✦✦-]**:35,000 Mora, Narukami's Affection x6, Polarizing Prism x9, Spectral Nucleus x6\n \
        **[✦✦✦✦✦✦]**:45,000 Mora, Narukami's Valor x4, Polarizing Prism x18, Spectral Nucleus x12", 'name':"Mouun's Moon"}
        return lst33
    elif name.lower() == "mitternachts waltz":
        lst34 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/7/77/Weapon_Mitternachts_Waltz.png/revision/latest/scale-to-width-down/256?cb=20210611013556", \
        'his':"คันธนูที่มีสีดั่งค่ำคืนแห่งบาปและความเพ้อฝัน", \
        'type':"Bow", 'stat':["510", "51.7%", "Physical DMG Bonus"], \
        'ascen':"**[✦-----]**:5,000 Mora, Tile of Decarabian's Tower x3, Heavy Horn x3, Treasure Hoarder Insignia x2\n \
        **[✦✦----]**:15,000 Mora, Debris of Decarabian's City x3, Heavy Horn x12, Treasure Hoarder Insignia x8\n \
        **[✦✦✦---]**:20,000 Mora, Debris of Decarabian's City x6, Black Bronze Horn x6, Silver Raven Insignia x6\n \
        **[✦✦✦✦--]**:30,000 Mora, Fragment of Decarabian's Epic x3, Black Bronze Horn x12, Silver Raven Insignia x9\n \
        **[✦✦✦✦✦-]**:35,000 Mora, Fragment of Decarabian's Epic x6, Black Crystal Horn x9, Golden Raven Insignia x6\n \
        **[✦✦✦✦✦✦]**:45,000 Mora, Scattered Piece of Decarabian's Dream x4, Black Crystal Horn x18, Golden Raven Insignia x12", 'name':"Mitternachts Waltz"}
        return lst34
    elif name.lower() == "hamayumi":
        lst35 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/d/d9/Weapon_Hamayumi.png/revision/latest/scale-to-width-down/256?cb=20210726032818", \
        'his':"หญิงสาวในศาลเจ้าบางคนเคยเป็นเจ้าของวอร์โบว์นี้ มันถูกสร้างขึ้นด้วยทักษะที่เหนือกว่าและมีทั้งที่ซับซ้อนและทนทาน", \
        'type':"Bow", 'stat':["454", "55.1%", "ATK"], \
        'ascen':"**[✦-----]**:5,000 Mora, Narukami's Wisdom x3, Dismal Prism x3, Firm Arrowhead x2\n \
        **[✦✦----]**:15,000 Mora, Narukami's Joy x3, Dismal Prism x12, Firm Arrowhead x8\n \
        **[✦✦✦---]**:20,000 Mora, Narukami's Joy x6, Crystal Prism x6, Sharp Arrowhead x6\n \
        **[✦✦✦✦--]**:30,000 Mora, Narukami's Affection x3, Crystal Prism x12, Sharp Arrowhead x9\n \
        **[✦✦✦✦✦-]**:35,000 Mora, Narukami's Affection x6, Polarizing Prism x9, Weathered Arrowhead x6\n \
        **[✦✦✦✦✦✦]**:45,000 Mora, Narukami's Valor x4, Polarizing Prism x18, Weathered Arrowhead x12", 'name':"Hamayumi"}
        return lst35
    elif name.lower() == "favonius warbow":
        lst36 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/8/85/Weapon_Favonius_Warbow.png/revision/latest/scale-to-width-down/256?cb=20201120003145", \
        'his':"ธนูปลายโค้งกลับแบบทั่วไปที่ใช้งานโดยกองอัศวินแห่ง Favonius มีเพียงยอดนักธนูเท่านั้นที่จะดึงพลังสูงสุดของมันออกมาได้", \
        'type':"Bow", 'stat':["454", "61.3%", "Energy Recharge"], \
        'ascen':"**[✦-----]**:5,000 Mora, Fetters of the Dandelion Gladiator x3, Chaos Device x3, Whopperflower Nectar x2\n \
        **[✦✦----]**:15,000 Mora, Chains of the Dandelion Gladiator x3, Chaos Device x12, Whopperflower Nectar x8\n \
        **[✦✦✦---]**:20,000 Mora, Chains of the Dandelion Gladiator x6, Chaos Circuit x6, Shimmering Nectar x6\n \
        **[✦✦✦✦--]**:30,000 Mora, Shackles of the Dandelion Gladiator x3, Chaos Circuit x12, Shimmering Nectar x9\n \
        **[✦✦✦✦✦-]**:35,000 Mora, Shackles of the Dandelion Gladiator x6, Chaos Core x9, Energy Nectar x6\n \
        **[✦✦✦✦✦✦]**:45,000 Mora, Dream of the Dandelion Gladiator x4, Chaos Core x18, Energy Nectar x12", 'name':"Favonius Warbow"}
        return lst36
    elif name.lower() == "":
        lst25 = {'thum':"", \
        'his':"", \
        'type':"Bow", 'stat':["510", "51.7%", "Physical DMG Bonus"], \
        'ascen':"**[✦-----]**:5,000 Mora,  x3,  x3,  x2\n \
        **[✦✦----]**:15,000 Mora,  x3,  x12,  x8\n \
        **[✦✦✦---]**:20,000 Mora,  x6,  x6,  x6\n \
        **[✦✦✦✦--]**:30,000 Mora,  x3,   x12,  x9\n \
        **[✦✦✦✦✦-]**:35,000 Mora,  x6,  x9,  x6\n \
        **[✦✦✦✦✦✦]**:45,000 Mora,  x4,  x18,  x12", 'name':""}
        return lst25
    elif name.lower() == "":
        lst25 = {'thum':"", \
        'his':"", \
        'type':"Bow", 'stat':["510", "51.7%", "Physical DMG Bonus"], \
        'ascen':"**[✦-----]**:5,000 Mora,  x3,  x3,  x2\n \
        **[✦✦----]**:15,000 Mora,  x3,  x12,  x8\n \
        **[✦✦✦---]**:20,000 Mora,  x6,  x6,  x6\n \
        **[✦✦✦✦--]**:30,000 Mora,  x3,   x12,  x9\n \
        **[✦✦✦✦✦-]**:35,000 Mora,  x6,  x9,  x6\n \
        **[✦✦✦✦✦✦]**:45,000 Mora,  x4,  x18,  x12", 'name':""}
        return lst25
    elif name.lower() == "":
        lst25 = {'thum':"", \
        'his':"", \
        'type':"Bow", 'stat':["510", "51.7%", "Physical DMG Bonus"], \
        'ascen':"**[✦-----]**:5,000 Mora,  x3,  x3,  x2\n \
        **[✦✦----]**:15,000 Mora,  x3,  x12,  x8\n \
        **[✦✦✦---]**:20,000 Mora,  x6,  x6,  x6\n \
        **[✦✦✦✦--]**:30,000 Mora,  x3,   x12,  x9\n \
        **[✦✦✦✦✦-]**:35,000 Mora,  x6,  x9,  x6\n \
        **[✦✦✦✦✦✦]**:45,000 Mora,  x4,  x18,  x12", 'name':""}
        return lst25
    elif name.lower() == "":
        lst25 = {'thum':"", \
        'his':"", \
        'type':"Bow", 'stat':["510", "51.7%", "Physical DMG Bonus"], \
        'ascen':"**[✦-----]**:5,000 Mora,  x3,  x3,  x2\n \
        **[✦✦----]**:15,000 Mora,  x3,  x12,  x8\n \
        **[✦✦✦---]**:20,000 Mora,  x6,  x6,  x6\n \
        **[✦✦✦✦--]**:30,000 Mora,  x3,   x12,  x9\n \
        **[✦✦✦✦✦-]**:35,000 Mora,  x6,  x9,  x6\n \
        **[✦✦✦✦✦✦]**:45,000 Mora,  x4,  x18,  x12", 'name':""}
        return lst25

                               
                   