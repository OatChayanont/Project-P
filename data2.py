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
    elif name.lower() == "compound bow":
        lst37 = {'thum':"", \
        'his':"ธนูทดกำลังหายากที่ทำจากโลหะประกอบกัน ดูแลรักษายาก แต่ขึ้นศรได้ง่ายและมีพลังทำลายที่สูงมาก", \
        'type':"Bow", 'stat':["454", "69.0%", "Physical DMG Bonus"], \
        'ascen':"**[✦-----]**:5,000 Mora, Grain of Aerosiderite x3, Fragile Bone Shard x3, Recruit's Insignia x2\n \
        **[✦✦----]**:15,000 Mora, Piece of Aerosiderite x3, Fragile Bone Shard x12, Recruit's Insignia x8\n \
        **[✦✦✦---]**:20,000 Mora, Piece of Aerosiderite x6, Sturdy Bone Shard x6, Sergeant's Insignia x6\n \
        **[✦✦✦✦--]**:30,000 Mora, Bit of Aerosiderite x3, Sturdy Bone Shard x12, Sergeant's Insignia x9\n \
        **[✦✦✦✦✦-]**:35,000 Mora, Bit of Aerosiderite x6, Fossilized Bone Shard x9, Lieutenant's Insignia x6\n \
        **[✦✦✦✦✦✦]**:45,000 Mora, Chunk of Aerosiderite x4, Fossilized Bone Shard x18, Lieutenant's Insignia x12", 'name':"Compound Bow"}
        return lst37
    elif name.lower() == "blackcliff warbow":
        lst38 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/b/b8/Weapon_Blackcliff_Warbow.png/revision/latest/scale-to-width-down/256?cb=20201103093753", \
        'his':"คันธนูที่ทำจากหิน blackstone ที่มีคันศรอันแข็งแกร่ง ผู้ยิงต้องเป็นมือธนูที่กำย่ำแข็งแกร่งเท่านั้น", \
        'type':"Bow", 'stat':["565", "36.8%", "CRIT DMG"], \
        'ascen':"**[✦-----]**:5,000 Mora, Luminous Sands from Guyun x3, Hunter's Sacrificial Knife x3, Whopperflower Nectar x2\n \
        **[✦✦----]**:15,000 Mora, Lustrous Stone from Guyun x3, Hunter's Sacrificial Knife x12, Whopperflower Nectar x8\n \
        **[✦✦✦---]**:20,000 Mora, Lustrous Stone from Guyun x6, Agent's Sacrificial Knife x6, Shimmering Nectar x6\n \
        **[✦✦✦✦--]**:30,000 Mora, Relic from Guyun x3, Agent's Sacrificial Knife x12, Shimmering Nectar x9\n \
        **[✦✦✦✦✦-]**:35,000 Mora, Relic from Guyun x6, Inspector's Sacrificial Knife x9, Energy Nectar x6\n \
        **[✦✦✦✦✦✦]**:45,000 Mora, Divine Body from Guyun x4, Inspector's Sacrificial Knife x18, Energy Nectar x12", 'name':"Blackcliff Warbow"}
        return lst38
    elif name.lower() == "windblume ode":
        lst39 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/3/38/Weapon_Windblume_Ode.png/revision/latest/scale-to-width-down/256?cb=20210317075422", \
        'his':"ธนูที่ประดับตกแต่งด้วยดอกไม้นิรนาม ที่ได้แบกรับความหวังอันแรงกล้าของบุคคลนิรนามเอาไว้", \
        'type':"Bow", 'stat':["510", "165", "Elemental Mastery"], \
        'ascen':"**[✦-----]**:5,000 Mora, Fetters of the Dandelion Gladiator x3, Dead Ley Line Branch x3, Whopperflower Nectar x2\n \
        **[✦✦----]**:15,000 Mora, Chains of the Dandelion Gladiator x3, Dead Ley Line Branch x12, Whopperflower Nectar x8\n \
        **[✦✦✦---]**:20,000 Mora, Chains of the Dandelion Gladiator x6, Dead Ley Line Leaves x6, Shimmering Nectar x6\n \
        **[✦✦✦✦--]**:30,000 Mora, Shackles of the Dandelion Gladiator x3, Dead Ley Line Leaves x12, Shimmering Nectar x9\n \
        **[✦✦✦✦✦-]**:35,000 Mora, Shackles of the Dandelion Gladiator x6, Ley Line Sprout x9, Energy Nectar x6\n \
        **[✦✦✦✦✦✦]**:45,000 Mora, Dream of the Dandelion Gladiator x4, Ley Line Sprout x18, Energy Nectar x12", 'name':"Windblume Ode"}
        return lst39
    elif name.lower() == "wine and song":
        lst40 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/c/c6/Weapon_Wine_and_Song.png/revision/latest/scale-to-width-down/256?cb=20210317183126", \
        'his':"บทเพลงที่ได้รับความนิยมในยุคสมัยของชนชั้นสูง ข้อมูลของผู้แต่งนั้นไม่เป็นที่แน่ชัด สิ่งที่อยู่ในนั้นคือบันทึกเรื่องราวของจอมโจรผู้ยิ่งใหญ่", \
        'type':"Catalyst", 'stat':["565", "30.6%", "Energy Recharge"], \
        'ascen':"**[✦-----]**:5,000 Mora, Boreal Wolf's Milk Tooth x3, Dead Ley Line Branch x3, Divining Scroll x2\n \
        **[✦✦----]**:15,000 Mora, Boreal Wolf's Cracked Tooth x3, Dead Ley Line Branch x12, Divining Scroll x8\n \
        **[✦✦✦---]**:20,000 Mora, Boreal Wolf's Cracked Tooth x6, Dead Ley Line Leaves x6, Sealed Scroll x6\n \
        **[✦✦✦✦--]**:30,000 Mora, Boreal Wolf's Broken Fang x3, Dead Ley Line Leaves x12, Sealed Scroll x9\n \
        **[✦✦✦✦✦-]**:35,000 Mora, Boreal Wolf's Broken Fang x6, Ley Line Sprout x9, Forbidden Curse Scroll x6\n \
        **[✦✦✦✦✦✦]**:45,000 Mora, Boreal Wolf's Nostalgia x4, Ley Line Sprout x18, Forbidden Curse Scroll x12", 'name':"Wine and Song"}
        return lst40
    elif name.lower() == "the widsith":
        lst41 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/f/f0/Weapon_The_Widsith.png/revision/latest/scale-to-width-down/256?cb=20201119201814", \
        'his':"หนังสือบันทึกเนื้อเพลงเล่มหนา ๆ ซึ่งถึงแม้จะถูกแมลงและสายลมทำให้ผุกร่อนไปบ้าง แต่ลายมือที่เหลืออยู่ก็ยังคงเผยพลังงานให้เห็นอยู่ดี", \
        'type':"Catalyst", 'stat':["510", "55.1%", "CRIT DMG"], \
        'ascen':"**[✦-----]**:5,000 Mora, Boreal Wolf's Milk Tooth x3, Dead Ley Line Branch x3, Damaged Mask x2\n \
        **[✦✦----]**:15,000 Mora, Boreal Wolf's Cracked Tooth x3, Dead Ley Line Branch x12, Damaged Mask x8\n \
        **[✦✦✦---]**:20,000 Mora, Boreal Wolf's Cracked Tooth x6, Dead Ley Line Leaves x6, Stained Mask x6\n \
        **[✦✦✦✦--]**:30,000 Mora, Boreal Wolf's Broken Fang x3, Dead Ley Line Leaves x12, Stained Mask x9\n \
        **[✦✦✦✦✦-]**:35,000 Mora, Boreal Wolf's Broken Fang x6, Ley Line Sprout x9, Ominous Mask x6\n \
        **[✦✦✦✦✦✦]**:45,000 Mora, Boreal Wolf's Nostalgia x4, Ley Line Sprout x18, Ominous Mask x12", 'name':"The Widsith"}
        return lst41
    elif name.lower() == "solar pearl":
        lst42 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/f/fc/Weapon_Solar_Pearl.png/revision/latest/scale-to-width-down/256?cb=20201116035322", \
        'his':"มันเก็บกักพลังของแสงแห่งตะวันและจันทราไว้ เป็นไข่มุกสีทองที่คอยปล่อยคลื่นพลังอันอบอุ่นออกมา", \
        'type':"Catalyst", 'stat':["510", "27.6%", "CRIT Rate"], \
        'ascen':"**[✦-----]**:5,000 Mora, Luminous Sands from Guyun x3, Hunter's Sacrificial Knife x3, Whopperflower Nectar x2\n \
        **[✦✦----]**:15,000 Mora, Lustrous Stone from Guyun x3, Hunter's Sacrificial Knife x12, Whopperflower Nectar x8\n \
        **[✦✦✦---]**:20,000 Mora, Lustrous Stone from Guyun x6, Agent's Sacrificial Knife x6, Shimmering Nectar x6\n \
        **[✦✦✦✦--]**:30,000 Mora, Relic from Guyun x3, Agent's Sacrificial Knife x12, Shimmering Nectar x9\n \
        **[✦✦✦✦✦-]**:35,000 Mora, Relic from Guyun x6, Inspector's Sacrificial Knife x9, Energy Nectar x6\n \
        **[✦✦✦✦✦✦]**:45,000 Mora, Divine Body from Guyun x4, Inspector's Sacrificial Knife x18, Energy Nectar x12", 'name':"Solar Pearl"}
        return lst42
    elif name.lower() == "sacrificial fragments":
        lst43 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/6/6c/Weapon_Sacrificial_Fragments.png/revision/latest/scale-to-width-down/256?cb=20201116035037", \
        'his':"หนังสือสคริปต์ที่มีอายุเก่าแก่ ซึ่งไม่สามารถระบุข้อความต่าง ๆ และบทสคริปต์ข้างในได้อีกต่อไป ถูกสาปโดยการกัดเซาะของสายลมแห่งกาลเวลา", \
        'type':"Catalyst", 'stat':["454", "221", "Elemental Mastery"], \
        'ascen':"**[✦-----]**:5,000 Mora, Fetters of the Dandelion Gladiator x3, Chaos Device x3, Treasure Hoarder Insignia x2\n \
        **[✦✦----]**:15,000 Mora, Chains of the Dandelion Gladiator x3, Chaos Device x12, Treasure Hoarder Insignia x8\n \
        **[✦✦✦---]**:20,000 Mora, Chains of the Dandelion Gladiator x6, Chaos Circuit x6, Silver Raven Insignia x6\n \
        **[✦✦✦✦--]**:30,000 Mora, Shackles of the Dandelion Gladiator x3, Chaos Circuit x12, Silver Raven Insignia x9\n \
        **[✦✦✦✦✦-]**:35,000 Mora, Shackles of the Dandelion Gladiator x6, Chaos Core x9, Golden Raven Insignia x6\n \
        **[✦✦✦✦✦✦]**:45,000 Mora, Dream of the Dandelion Gladiator x4, Chaos Core x18, Golden Raven Insignia x12", 'name':"Sacrificial Fragments"}
        return lst43
    elif name.lower() == "royal grimoire":
        lst44 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/9/99/Weapon_Royal_Grimoire.png/revision/latest/scale-to-width-down/256?cb=20201120000114", \
        'his':"หนังสือที่ครั้งหนึ่งเคยเป็นของนักเวทมนตร์หลวงแห่ง Mondstadt มันได้เก็บเอาความจริงของบัญชีย้อนหลังและมนตราต่าง ๆ ไว้ภายใน", \
        'type':"Catalyst", 'stat':["565", "27.6%", "ATK"], \
        'ascen':"**[✦-----]**:5,000 Mora, Tile of Decarabian's Tower x3, Heavy Horn x3, Recruit's Insignia x2\n \
        **[✦✦----]**:15,000 Mora, Debris of Decarabian's City x3, Heavy Horn x12, Recruit's Insignia x8\n \
        **[✦✦✦---]**:20,000 Mora, Debris of Decarabian's City x6, Black Bronze Horn x6, Sergeant's Insignia x6\n \
        **[✦✦✦✦--]**:30,000 Mora, Fragment of Decarabian's Epic x3, Black Bronze Horn x12, Sergeant's Insignia x9\n \
        **[✦✦✦✦✦-]**:35,000 Mora, Fragment of Decarabian's Epic x6, Black Crystal Horn x9, Lieutenant's Insignia x6\n \
        **[✦✦✦✦✦✦]**:45,000 Mora, Scattered Piece of Decarabian's Dream x4, Black Crystal Horn x18, Lieutenant's Insignia x12", 'name':"Royal Grimoire"}
        return lst44
    elif name.lower() == "prototype amber":
        lst45 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/2/2a/Weapon_Prototype_Amber.png/revision/latest/scale-to-width-down/256?cb=20201116034808", \
        'his':"สื่อเวทอำพันที่ถูกซ่อนไว้ใน Blackcliff Forge ดูเหมือนมันส่องแสงประกายด้วยแสงจากฟากฟ้า", \
        'type':"Catalyst", 'stat':["510", "41.3%", "HP"], \
        'ascen':"**[✦-----]**:5,000 Mora, Mist Veiled Lead Elixir x3, Mist Grass Pollen x3, Firm Arrowhead x2\n \
        **[✦✦----]**:15,000 Mora, Mist Veiled Mercury Elixir x3, Mist Grass Pollen x12, Firm Arrowhead x8\n \
        **[✦✦✦---]**:20,000 Mora, Mist Veiled Mercury Elixir x6, Mist Grass x6, Sharp Arrowhead x6\n \
        **[✦✦✦✦--]**:30,000 Mora, Mist Veiled Gold Elixir x3, Mist Grass x12, Sharp Arrowhead x9\n \
        **[✦✦✦✦✦-]**:35,000 Mora, Mist Veiled Gold Elixir x6, Mist Grass Wick x9, Weathered Arrowhead x6\n \
        **[✦✦✦✦✦✦]**:45,000 Mora, Mist Veiled Primo Elixir x4, Mist Grass Wick x18, Weathered Arrowhead x12", 'name':"Prototype Amber"}
        return lst45
    elif name.lower() == "mappa mare":
        lst46 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/4/4d/Weapon_Mappa_Mare.png/revision/latest/scale-to-width-down/256?cb=20201116034208", \
        'his':"แผนที่เดินเรือที่มีบันทึกกระแสน้ำและสภาพอากาศบริเวณใกล้เคียง ช่วยให้ผู้ค้าจากต่างแดนเข้าถึงเมืองท่า Liyue ได้", \
        'type':"**[✦-----]**:5,000 Mora, Grain of Aerosiderite x3, Fragile Bone Shard x3, Slime Condensate x2\n \
        **[✦✦----]**:15,000 Mora, Piece of Aerosiderite x3, Fragile Bone Shard x12, Slime Condensate x8\n \
        **[✦✦✦---]**:20,000 Mora, Piece of Aerosiderite x6, Sturdy Bone Shard x6, Slime Secretions x6\n \
        **[✦✦✦✦--]**:30,000 Mora, Bit of Aerosiderite x3, Sturdy Bone Shard x12, Slime Secretions x9\n \
        **[✦✦✦✦✦-]**:35,000 Mora, Bit of Aerosiderite x6, Fossilized Bone Shard x9, Slime Concentrate x6\n \
        **[✦✦✦✦✦✦]**:45,000 Mora, Chunk of Aerosiderite x4, Fossilized Bone Shard x18, Slime Concentrate x12", 'name':"Mappa Mare"}
        return lst46
    elif name.lower() == "hakushin ring":
        lst47 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/e/ee/Weapon_Hakushin_Ring.png/revision/latest/scale-to-width-down/256?cb=20210723074418", \
        'his':'สื่อเวทที่แบกรับความคิดและความทรงจำของ "Kitsune Saiguu" เมื่อในอดีต แต่ความคิดและความทรงจำของเธอนั้นยิ่งใหญ่มาก ซึ่งเป็นไปไม่ได้เลยที่จะใส่ลงในภาชนะขนาดเล็กเช่นนี้ได้ทั้งหมด', \
        'type':"Catalyst", 'stat':["565", "30.6%", "Energy Recharge"], \
        'ascen':"**[✦-----]**:5,000 Mora, Coral Branch of a Distant Sea x3, Dismal Prism x3, Divining Scroll x2\n \
        **[✦✦----]**:15,000 Mora, Jeweled Branch of a Distant Sea x3, Dismal Prism x12, Divining Scroll x8\n \
        **[✦✦✦---]**:20,000 Mora, Jeweled Branch of a Distant Sea x6, Crystal Prism x6, Sealed Scroll x6\n \
        **[✦✦✦✦--]**:30,000 Mora, Jade Branch of a Distant Sea x3, Crystal Prism x12, Sealed Scroll x9\n \
        **[✦✦✦✦✦-]**:35,000 Mora, Jade Branch of a Distant Sea x6, Polarizing Prism x9, Forbidden Curse Scroll x6\n \
        **[✦✦✦✦✦✦]**:45,000 Mora, Golden Branch of a Distant Sea x4, Polarizing Prism x18, Forbidden Curse Scroll x12", 'name':"Hakushin Ring"}
        return lst47
    elif name.lower() == "frostbearer":
        lst48 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/1/1c/Weapon_Frostbearer.png/revision/latest/scale-to-width-down/256?cb=20210209065948", \
        'his':"ผลไม้ประหลาดที่มีกลิ่นอายของความเย็นและความรู้สึกที่เจ็บปวด", \
        'type':"**[✦-----]**:5,000 Mora, Fetters of the Dandelion Gladiator x3, Chaos Device x3, Whopperflower Nectar x2\n \
        **[✦✦----]**:15,000 Mora, Chains of the Dandelion Gladiator x3, Chaos Device x12, Whopperflower Nectar x8\n \
        **[✦✦✦---]**:20,000 Mora, Chains of the Dandelion Gladiator x6, Chaos Circuit x6, Shimmering Nectar x6\n \
        **[✦✦✦✦--]**:30,000 Mora, Shackles of the Dandelion Gladiator x3, Chaos Circuit x12, Shimmering Nectar x9\n \
        **[✦✦✦✦✦-]**:35,000 Mora, Shackles of the Dandelion Gladiator x6, Chaos Core x9, Energy Nectar x6\n \
        **[✦✦✦✦✦✦]**:45,000 Mora, Dream of the Dandelion Gladiator x4, Chaos Core x18, Energy Nectar x12", 'name':"Frostbearer"}
        return lst48
    elif name.lower() == "favonius codex":
        lst49 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/3/36/Weapon_Favonius_Codex.png/revision/latest/scale-to-width-down/256?cb=20201116033719", \
        'his':"ตำราลับที่เป็นของนักแปรธาตุของกองอัศวินแห่ง Favonius ภายในระบุเรื่องพลังของสิ่งต่าง ๆ และความเป็นเหตุเป็นผล รวมถึงเรื่องอื่น ๆ ด้วย", \
        'type':"Catalyst", 'stat':["510", "45.9%", "Energy Recharge"], \
        'ascen':"**[✦-----]**:5,000 Mora, Tile of Decarabian's Tower x3, Heavy Horn x3, Divining Scroll x2\n \
        **[✦✦----]**:15,000 Mora, Debris of Decarabian's City x3, Heavy Horn x12, Divining Scroll x8\n \
        **[✦✦✦---]**:20,000 Mora, Debris of Decarabian's City x6, Black Bronze Horn x6, Sealed Scroll x6\n \
        **[✦✦✦✦--]**:30,000 Mora, Fragment of Decarabian's Epic x3, Black Bronze Horn x12, Sealed Scroll x9\n \
        **[✦✦✦✦✦-]**:35,000 Mora, Fragment of Decarabian's Epic x6, Black Crystal Horn x9, Forbidden Curse Scroll x6\n \
        **[✦✦✦✦✦✦]**:45,000 Mora, Scattered Piece of Decarabian's Dream x4, Black Crystal Horn x18, Forbidden Curse Scroll x12", 'name':"Favonius Codex"}
        return lst49
    elif name.lower() == "eye of perception":
        lst50 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/6/6c/Weapon_Eye_of_Perception.png/revision/latest/scale-to-width-down/256?cb=20201116033703", \
        'his':"ลูกแก้วสีดำ ตำนานเล่าว่ามันมีพลังที่รับรู้ถึงความไร้เดียงสาของมนุษย์", \
        'type':"Catalyst", 'stat':["454", "55.1%", "ATK"], \
        'ascen':"**[✦-----]**:5,000 Mora, Mist Veiled Lead Elixir x3, Mist Grass Pollen x3, Damaged Mask x2\n \
        **[✦✦----]**:15,000 Mora, Mist Veiled Mercury Elixir x3, Mist Grass Pollen x12, Damaged Mask x8\n \
        **[✦✦✦---]**:20,000 Mora, Mist Veiled Mercury Elixir x6, Mist Grass x6, Stained Mask x6\n \
        **[✦✦✦✦--]**:30,000 Mora, Mist Veiled Gold Elixir x3, Mist Grass x12, Stained Mask x9\n \
        **[✦✦✦✦✦-]**:35,000 Mora, Mist Veiled Gold Elixir x6, Mist Grass Wick x9, Ominous Mask x6\n \
        **[✦✦✦✦✦✦]**:45,000 Mora, Mist Veiled Primo Elixir x4, Mist Grass Wick x18, Ominous Mask x12", 'name':"Eye of Perception"}
        return lst50
    elif name.lower() == "dodoco tales":
        lst51 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/5/51/Weapon_Dodoco_Tales.png/revision/latest/scale-to-width-down/256?cb=20210613085809", \
        'his':"หนังสือสำหรับเด็กที่มีหน้าปกสวยงาม เนื้อหาเป็นเรื่องสั้นที่เกี่ยวกับเด็ก 1 ทั้งหมด มันน่าอ่านจนอดใจไม่ไหว แม้แต่นักอ่านที่เป็นผู้ใหญ่พอได้อ่านเรื่องราวผจญภัยแบบเด็ก ๆ แบบนี้แล้ว ก็อดไม่ได้ที่จะหลงใหลไปกับมัน", \
        'type':"Catalyst", 'stat':["454", "55.1%", "ATK"], \
        'ascen':"**[✦-----]**:5,000 Mora, Boreal Wolf's Milk Tooth x3, Dead Ley Line Branch x3, Damaged Mask x2\n \
        **[✦✦----]**:15,000 Mora, Boreal Wolf's Cracked Tooth x3, Dead Ley Line Branch x12, Damaged Mask x8\n \
        **[✦✦✦---]**:20,000 Mora, Boreal Wolf's Cracked Tooth x6, Dead Ley Line Leaves x6, Stained Mask x6\n \
        **[✦✦✦✦--]**:30,000 Mora, Boreal Wolf's Broken Fang x3, Dead Ley Line Leaves x12, Stained Mask x9\n \
        **[✦✦✦✦✦-]**:35,000 Mora, Boreal Wolf's Broken Fang x6, Ley Line Sprout x9, Ominous Mask x6\n \
        **[✦✦✦✦✦✦]**:45,000 Mora, Boreal Wolf's Nostalgia x4, Ley Line Sprout x18, Ominous Mask x12", 'name':"Dodoco Tales"}
        return lst51
    elif name.lower() == "blackcliff agate":
        lst52 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/a/a6/Weapon_Blackcliff_Agate.png/revision/latest/scale-to-width-down/256?cb=20201119233950", \
        'his':"สื่อเวทลึกลับนี้ทำมาจากหิน blackstone มันมีสีแดงเข้มเป็นลางที่ดูเหมือนว่าจะเต้นเป็นจังหวะประสานกับแรงสั่นสะเทือนจากส่วนลึกของโลก", \
        'type':"Catalyst", 'stat':["510", "55.1%", "CRIT DMG"], \
        'ascen':"**[✦-----]**:5,000 Mora, Luminous Sands from Guyun x3, Hunter's Sacrificial Knife x3, Divining Scroll x2\n \
        **[✦✦----]**:15,000 Mora, Lustrous Stone from Guyun x3, Hunter's Sacrificial Knife x12, Divining Scroll x8\n \
        **[✦✦✦---]**:20,000 Mora, Lustrous Stone from Guyun x6, Agent's Sacrificial Knife x6, Sealed Scroll x6\n \
        **[✦✦✦✦--]**:30,000 Mora, Relic from Guyun x3, Agent's Sacrificial Knife x12, Sealed Scroll x9\n \
        **[✦✦✦✦✦-]**:35,000 Mora, Relic from Guyun x6, Inspector's Sacrificial Knife x9, Forbidden Curse Scroll x6\n \
        **[✦✦✦✦✦✦]**:45,000 Mora, Divine Body from Guyun x4, Inspector's Sacrificial Knife x18, Forbidden Curse Scroll x12", 'name':"Blackcliff Agate"}
        return lst52
    elif name.lower() == "akuoumaru":
        lst53 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/c/c5/Weapon_Akuoumaru.png/revision/latest/scale-to-width-down/256?cb=20211013044027", \
        'his':"ดาบสุดรักของ Akuou ในตำนาน ใบมีดมีขนาดใหญ่และสง่างาม แต่มันกลับกวัดแกว่งได้ง่ายดายจนคาดไม่ถึง", \
        'type':"Claymore", 'stat':["510", "41.3%", "ATK"], \
        'ascen':"**[✦-----]**:5,000 Mora, Coral Branch of a Distant Sea x3, Concealed Claw x3, Old Handguard x2\n \
        **[✦✦----]**:15,000 Mora, Jeweled Branch of a Distant Sea x3, Concealed Claw x12, Old Handguard x8\n \
        **[✦✦✦---]**:20,000 Mora, Jeweled Branch of a Distant Sea x6, Concealed Unguis x6, Kageuchi Handguard x6\n \
        **[✦✦✦✦--]**:30,000 Mora, Jade Branch of a Distant Sea x3, Concealed Unguis x12, Kageuchi Handguard x9\n \
        **[✦✦✦✦✦-]**:35,000 Mora, Jade Branch of a Distant Sea x6, Concealed Talon x9, Famed Handguard x6\n \
        **[✦✦✦✦✦✦]**:45,000 Mora, Golden Branch of a Distant Sea x4, Concealed Talon x18, Famed Handguard x12", 'name':"Akuoumaru"}
        return lst53
    elif name.lower() == "royal greatsword":
        lst54 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/b/bf/Weapon_Royal_Greatsword.png/revision/latest/scale-to-width-down/256?cb=20201116034928", \
        'his':"ดาบใหญ่สภาพเก่าแก่ของชนชั้นสูงผู้ที่ครั้งหนึ่งเคยปกครอง Mondstadt มาก่อน มันทำจากวัสดุระดับสูงที่ทนทานต่อความโหดร้ายของกาลเวลา เป็นอาวุธสำหรับต่อสู้ของชนชั้นสูง", \
        'type':"Claymore", 'stat':["565", "27.6%", "ATK"], \
        'ascen':"**[✦-----]**:5,000 Mora, Fetters of the Dandelion Gladiator x3, Chaos Device x3, Slime Condensate x2\n \
        **[✦✦----]**:15,000 Mora, Chains of the Dandelion Gladiator x3, Chaos Device x12, Slime Condensate x8\n \
        **[✦✦✦---]**:20,000 Mora, Chains of the Dandelion Gladiator x6, Chaos Circuit x6, Slime Secretions x6\n \
        **[✦✦✦✦--]**:30,000 Mora, Shackles of the Dandelion Gladiator x3, Chaos Circuit x12, Slime Secretions x9\n \
        **[✦✦✦✦✦-]**:35,000 Mora, Shackles of the Dandelion Gladiator x6, Chaos Core x9, Slime Concentrate x6\n \
        **[✦✦✦✦✦✦]**:45,000 Mora, Dream of the Dandelion Gladiator x4, Chaos Core x18, Slime Concentrate x12", 'name':"Royal Greatsword"}
        return lst54
    elif name.lower() == "whiteblind":
        lst55 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/0/04/Weapon_Whiteblind.png/revision/latest/scale-to-width-down/256?cb=20201116035607", \
        'his':"ดาบใหญ่ที่ด้านหนึ่งของตัวดามยังไม่ถูกลับเพื่อเปิดคมมีดซึ่งมาพร้อมกับผู้ทำการค้าจากต่างถิ่นที่เดินทางมาถึง Liyue มีพลังที่เหลือเชื่อเมื่ออยู่ในมือของคนที่รู้วิธีใช้มัน", \
        'type':"Claymore", 'stat':["510", "51.7%", "DEF"], \
        'ascen':"**[✦-----]**:5,000 Mora, Luminous Sands from Guyun x3, Hunter's Sacrificial Knife x3, Treasure Hoarder Insignia x2\n \
        **[✦✦----]**:15,000 Mora, Lustrous Stone from Guyun x3, Hunter's Sacrificial Knife x12, Treasure Hoarder Insignia x8\n \
        **[✦✦✦---]**:20,000 Mora, Lustrous Stone from Guyun x6, Agent's Sacrificial Knife x6, Silver Raven Insignia x6\n \
        **[✦✦✦✦--]**:30,000 Mora, Relic from Guyun x3, Agent's Sacrificial Knife x12, Silver Raven Insignia x9\n \
        **[✦✦✦✦✦-]**:35,000 Mora, Relic from Guyun x6, Inspector's Sacrificial Knife x9, Golden Raven Insignia x6\n \
        **[✦✦✦✦✦✦]**:45,000 Mora, Divine Body from Guyun x4, Inspector's Sacrificial Knife x18, Golden Raven Insignia x12", 'name':"Whiteblind"}
        return lst55
    elif name.lower() == "the bell":
        lst56 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/6/6e/Weapon_The_Bell.png/revision/latest/scale-to-width-down/256?cb=20201116035344", \
        'his':"ดาบขนาดใหญ่ที่หนักและมีนาฬิกาติดตั้งมาด้วย แต่กลไกภายในของมันนั้นพังไปนานแล้ว", \
        'type':"Claymore", 'stat':["510", "41.3%", "HP"], \
        'ascen':"**[✦-----]**:5,000 Mora, Tile of Decarabian's Tower x3, Heavy Horn x3, Whopperflower Nectar x2\n \
        **[✦✦----]**:15,000 Mora, Debris of Decarabian's City x3, Heavy Horn x12, Whopperflower Nectar x8\n \
        **[✦✦✦---]**:20,000 Mora, Debris of Decarabian's City x6, Black Bronze Horn x6, Shimmering Nectar x6\n \
        **[✦✦✦✦--]**:30,000 Mora, Fragment of Decarabian's Epic x3, Black Bronze Horn x12, Shimmering Nectar x9\n \
        **[✦✦✦✦✦-]**:35,000 Mora, Fragment of Decarabian's Epic x6, Black Crystal Horn x9, Energy Nectar x6\n \
        **[✦✦✦✦✦✦]**:45,000 Mora, Scattered Piece of Decarabian's Dream x4, Black Crystal Horn x18, Energy Nectar x12", 'name':"The Bell"}
        return lst56
    elif name.lower() == "snow-tombed starsilver":
        lst57 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/4/49/Weapon_Snow-Tombed_Starsilver.png/revision/latest/scale-to-width-down/256?cb=20201223042944", \
        'his':"ดาบใหญ่โบราณที่ซ่อนอยู่ในภาพฝาผนังนี้ หลอมขึ้นมาจากดวงดาว ดูเหมือนจะมีพลังที่สามารถฟันน้ำแข็งและหิมะได้", \
        'type':"Claymore", 'stat':["565", "34.1%", "Physical DMG Bonus"], \
        'ascen':"**[✦-----]**:5,000 Mora, Tile of Decarabian's Tower x3, Heavy Horn x3, Slime Condensate x2\n \
        **[✦✦----]**:15,000 Mora, Debris of Decarabian's City x3, Heavy Horn x12, Slime Condensate x8\n \
        **[✦✦✦---]**:20,000 Mora, Debris of Decarabian's City x6, Black Bronze Horn x6, Slime Secretions x6\n \
        **[✦✦✦✦--]**:30,000 Mora, Fragment of Decarabian's Epic x3, Black Bronze Horn x12, Slime Secretions x9\n \
        **[✦✦✦✦✦-]**:35,000 Mora, Fragment of Decarabian's Epic x6, Black Crystal Horn x9, Slime Concentrate x6\n \
        **[✦✦✦✦✦✦]**:45,000 Mora, Scattered Piece of Decarabian's Dream x4, Black Crystal Horn x18, Slime Concentrate x12", 'name':"Snow-Tombed Starsilver"}
        return lst57
    elif name.lower() == "favonius greatsword":
        lst58 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/9/9c/Weapon_Favonius_Greatsword.png/revision/latest/scale-to-width-down/256?cb=20201119235934", \
        'his':"ดาบใหญ่ที่ใช้สำหรับทำพิธีของอัศวินแห่ง Favonius มันสามารถรวบรวมพลังงานธาตุได้ง่าย และสร้างพลังทำลายได้สูง", \
        'type':"Claymore", 'stat':["454", "61.3%", "Energy Recharge"], \
        'ascen':"**[✦-----]**:5,000 Mora, Fetters of the Dandelion Gladiator x3, Chaos Device x3, Recruit's Insignia x2\n \
        **[✦✦----]**:15,000 Mora, Chains of the Dandelion Gladiator x3, Chaos Device x12, Recruit's Insignia x8\n \
        **[✦✦✦---]**:20,000 Mora, Chains of the Dandelion Gladiator x6, Chaos Circuit x6, Sergeant's Insignia x6\n \
        **[✦✦✦✦--]**:30,000 Mora, Shackles of the Dandelion Gladiator x3, Chaos Circuit x12, Sergeant's Insignia x9\n \
        **[✦✦✦✦✦-]**:35,000 Mora, Shackles of the Dandelion Gladiator x6, Chaos Core x9, Lieutenant's Insignia x6\n \
        **[✦✦✦✦✦✦]**:45,000 Mora, Dream of the Dandelion Gladiator x4, Chaos Core x18, Lieutenant's Insignia x12", 'name':"Favonius Greatsword"}
        return lst58
    elif name.lower() == "katsuragikiri nagamasa":
        lst59 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/2/2e/Weapon_Katsuragikiri_Nagamasa.png/revision/latest/scale-to-width-down/256?cb=20211103232839", \
        'his':"ดาบที่ถูกทำขึ้นใน Tatarasuna เมื่อครั้งอดีต ทั้งหนักและแข็งแรงทนทาน", \
        'type':"Claymore", 'stat':["510", "45.9%", "Energy Recharge"], \
        'ascen':"**[✦-----]**:5,000 Mora, Narukami's Wisdom x3, Chaos Gear x3, Old Handguard x2\n \
        **[✦✦----]**:15,000 Mora, Narukami's Joy x3, Chaos Gear x12, Old Handguard x8\n \
        **[✦✦✦---]**:20,000 Mora, Narukami's Joy x6, Chaos Axis x6, Kageuchi Handguard x6\n \
        **[✦✦✦✦--]**:30,000 Mora, Narukami's Affection x3, Chaos Axis x12, Kageuchi Handguard x9\n \
        **[✦✦✦✦✦-]**:35,000 Mora, Narukami's Affection x6, Chaos Oculus x9, Famed Handguard x6\n \
        **[✦✦✦✦✦✦]**:45,000 Mora, Narukami's Valor x4, Chaos Oculus x18, Famed Handguard x12", 'name':"Katsuragikiri Nagamasa"}
        return lst59
    elif name.lower() == "sacrificial greatsword":
        lst60 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/1/17/Weapon_Sacrificial_Greatsword.png/revision/latest/scale-to-width-down/256?cb=20201120004023", \
        'his':"ดาบใหญ่ที่ตกแต่งอย่างสวยงามและกลายเป็นหินไปตามกาลเวลา ของที่ตกแต่งดาบยังคงเห็นได้อยู่ และมันให้พลังกับผู้ใช้เพื่อรับมือกับสายลมแห่งเวลา", \
        'type':"Claymore", 'stat':["565", "30.6%", "Energy Recharge"], \
        'ascen':"**[✦-----]**:5,000 Mora, Boreal Wolf's Milk Tooth x3, Dead Ley Line Branch x3, Firm Arrowhead x2\n \
        **[✦✦----]**:15,000 Mora, Boreal Wolf's Cracked Tooth x3, Dead Ley Line Branch x12, Firm Arrowhead x8\n \
        **[✦✦✦---]**:20,000 Mora, Boreal Wolf's Cracked Tooth x6, Dead Ley Line Leaves x6, Sharp Arrowhead x6\n \
        **[✦✦✦✦--]**:30,000 Mora, Boreal Wolf's Broken Fang x3, Dead Ley Line Leaves x12, Sharp Arrowhead x9\n \
        **[✦✦✦✦✦-]**:35,000 Mora, Boreal Wolf's Broken Fang x6, Ley Line Sprout x9, Weathered Arrowhead x6\n \
        **[✦✦✦✦✦✦]**:45,000 Mora, Boreal Wolf's Nostalgia x4, Ley Line Sprout x18, Weathered Arrowhead x12", 'name':"Sacrificial Greatsword"}
        return lst60
    elif name.lower() == "serpent spine":
        lst61 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/8/88/Weapon_Serpent_Spine.png/revision/latest/scale-to-width-down/256?cb=20201116035126", \
        'his':"อาวุธหายากจากทะเลโบราณ เสียงของระบำดาบนั้นเป็นเหมือนดั่งเสียงของคลื่นยักษ์ในอดีตกาล", \
        'type':"Claymore", 'stat':["510", "27.6%", "CRIT Rate"], \
        'ascen':"**[✦-----]**:5,000 Mora, Grain of Aerosiderite x3, Fragile Bone Shard x3, Whopperflower Nectar x2\n \
        **[✦✦----]**:15,000 Mora, Piece of Aerosiderite x3, Fragile Bone Shard x12, Whopperflower Nectar x8\n \
        **[✦✦✦---]**:20,000 Mora, Piece of Aerosiderite x6, Sturdy Bone Shard x6, Shimmering Nectar x6\n \
        **[✦✦✦✦--]**:30,000 Mora, Bit of Aerosiderite x3, Sturdy Bone Shard x12, Shimmering Nectar x9\n \
        **[✦✦✦✦✦-]**:35,000 Mora, Bit of Aerosiderite x6, Fossilized Bone Shard x9, Energy Nectar x6\n \
        **[✦✦✦✦✦✦]**:45,000 Mora, Chunk of Aerosiderite x4, Fossilized Bone Shard x18, Energy Nectar x12", 'name':"Serpent Spine"}
        return lst61
    elif name.lower() == "blackcliff slasher":
        lst62 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/d/d7/Weapon_Blackcliff_Slasher.png/revision/latest/scale-to-width-down/256?cb=20201116033252", \
        'his':"ดาบยักษ์ของ Blackcliff Forge นั้นแข็งแกร่งไม่มีใครเทียบ ตัวดาบสีดำแดง", \
        'type':"Claymore", 'stat':["510", "55.1%", "CRIT DMG"], \
        'ascen':"**[✦-----]**:5,000 Mora, Mist Veiled Lead Elixir x3, Mist Grass Pollen x3, Recruit's Insignia x2\n \
        **[✦✦----]**:15,000 Mora, Mist Veiled Mercury Elixir x3, Mist Grass Pollen x12, Recruit's Insignia x8\n \
        **[✦✦✦---]**:20,000 Mora, Mist Veiled Mercury Elixir x6, Mist Grass x6, Sergeant's Insignia x6\n \
        **[✦✦✦✦--]**:30,000 Mora, Mist Veiled Gold Elixir x3, Mist Grass x12, Sergeant's Insignia x9\n \
        **[✦✦✦✦✦-]**:35,000 Mora, Mist Veiled Gold Elixir x6, Mist Grass Wick x9, Lieutenant's Insignia x6\n \
        **[✦✦✦✦✦✦]**:45,000 Mora, Mist Veiled Primo Elixir x4, Mist Grass Wick x18, Lieutenant's Insignia x12", 'name':"Blackcliff Slasher"}
        return lst62
    elif name.lower() == "rainslasher":
        lst63 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/d/d4/Weapon_Rainslasher.png/revision/latest/scale-to-width-down/256?cb=20201119235128", \
        'his':"ดาบใหญ่ไร้คมซึ่งส่องประกายแสงสลัว ๆ ขดขยี้ศัตรูอย่างราบคาบด้วยความแรงและความแข็งแกร่ง", \
        'type':"Claymore", 'stat':["510", "165", "Elemental Mastery"], \
        'ascen':"**[✦-----]**:5,000 Mora, Mist Veiled Lead Elixir x3, Mist Grass Pollen x3, Divining Scroll x2\n \
        **[✦✦----]**:15,000 Mora, Mist Veiled Mercury Elixir x3, Mist Grass Pollen x12, Divining Scroll x8\n \
        **[✦✦✦---]**:20,000 Mora, Mist Veiled Mercury Elixir x6, Mist Grass x6, Sealed Scroll x6\n \
        **[✦✦✦✦--]**:30,000 Mora, Mist Veiled Gold Elixir x3, Mist Grass x12, Sealed Scroll x9\n \
        **[✦✦✦✦✦-]**:35,000 Mora, Mist Veiled Gold Elixir x6, Mist Grass Wick x9, Forbidden Curse Scroll x6\n \
        **[✦✦✦✦✦✦]**:45,000 Mora, Mist Veiled Primo Elixir x4, Mist Grass Wick x18, Forbidden Curse Scroll x12", 'name':"Rainslasher"}
        return lst63
    elif name.lower() == "prototype archaic":
        lst64 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/a/ab/Weapon_Prototype_Archaic.png/revision/latest/scale-to-width-down/256?cb=20201116034721", \
        'his':"ดาบยักษ์โบราณที่ถูกซ่อนไว้ใน Blackcliff Forge ตอนที่ชูขึ้น ราวกับว่าสามารถลงดาบหั่นอากาศออกเป็นสองท่อน", \
        'type':"Claymore", 'stat':["565", "27.6%", "ATK"], \
        'ascen':"**[✦-----]**:5,000 Mora, Grain of Aerosiderite x3, Fragile Bone Shard x3, Damaged Mask x2\n \
        **[✦✦----]**:15,000 Mora, Piece of Aerosiderite x3, Fragile Bone Shard x12, Damaged Mask x8\n \
        **[✦✦✦---]**:20,000 Mora, Piece of Aerosiderite x6, Sturdy Bone Shard x6, Stained Mask x6\n \
        **[✦✦✦✦--]**:30,000 Mora, Bit of Aerosiderite x3, Sturdy Bone Shard x12, Stained Mask x9\n \
        **[✦✦✦✦✦-]**:35,000 Mora, Bit of Aerosiderite x6, Fossilized Bone Shard x9, Ominous Mask x6\n \
        **[✦✦✦✦✦✦]**:45,000 Mora, Chunk of Aerosiderite x4, Fossilized Bone Shard x18, Ominous Mask x12", 'name':"Prototype Archaic"}
        return lst64
    elif name.lower() == "luxurious sea-lord":
        lst65 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/a/ab/Weapon_Luxurious_Sea-Lord.png/revision/latest/scale-to-width-down/256?cb=20210901044903", \
        'his':"ราชาแห่งมหาสมุทร หลังจากตากอากาศจนแห้ง ก็กลายเป็นอาวุธที่แสนสะดวก และยังใช้เป็นอาหารฉุกเฉินได้อีกด้วย", \
        'type':"Claymore", 'stat':["454", "55.1%", "ATK"], \
        'ascen':"**[✦-----]**:5,000 Mora, Grain of Aerosiderite x3, Fragile Bone Shard x3, Slime Condensate x2\n \
        **[✦✦----]**:15,000 Mora, Piece of Aerosiderite x3, Fragile Bone Shard x12, Slime Condensate x8\n \
        **[✦✦✦---]**:20,000 Mora, Piece of Aerosiderite x6, Sturdy Bone Shard x6, Slime Secretions x6\n \
        **[✦✦✦✦--]**:30,000 Mora, Bit of Aerosiderite x3, Sturdy Bone Shard x12, Slime Secretions x9\n \
        **[✦✦✦✦✦-]**:35,000 Mora, Bit of Aerosiderite x6, Fossilized Bone Shard x9, Slime Concentrate x6\n \
        **[✦✦✦✦✦✦]**:45,000 Mora, Chunk of Aerosiderite x4, Fossilized Bone Shard x18, Slime Concentrate x12", 'name':"Luxurious Sea-Lord"}
        return lst65
    elif name.lower() == "lithic blade":
        lst66 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/3/3a/Weapon_Lithic_Blade.png/revision/latest/scale-to-width-down/256?cb=20210225201003", \
        'his':"ดาบหนาและหนักซึ่งถูกทำขึ้นจากแผ่นหินของ Liyue", \
        'type':"Claymore", 'stat':["510", "41.3%", "ATK"], \
        'ascen':"**[✦-----]**:5,000 Mora, Luminous Sands from Guyun x3, Hunter's Sacrificial Knife x3, Firm Arrowhead x2\n \
        **[✦✦----]**:15,000 Mora, Lustrous Stone from Guyun x3, Hunter's Sacrificial Knife x12, Firm Arrowhead x8\n \
        **[✦✦✦---]**:20,000 Mora, Lustrous Stone from Guyun x6, Agent's Sacrificial Knife x6, Sharp Arrowhead x6\n \
        **[✦✦✦✦--]**:30,000 Mora, Relic from Guyun x3, Agent's Sacrificial Knife x12, Sharp Arrowhead x9\n \
        **[✦✦✦✦✦-]**:35,000 Mora, Relic from Guyun x6, Inspector's Sacrificial Knife x9, Weathered Arrowhead x6\n \
        **[✦✦✦✦✦✦]**:45,000 Mora, Divine Body from Guyun x4, Inspector's Sacrificial Knife x18, Weathered Arrowhead x12", 'name':"Lithic Blade"}
        return lst66
    elif name.lower() == "prototype starglitter":
        lst67 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/7/7e/Weapon_Prototype_Starglitter.png/revision/latest/scale-to-width-down/256?cb=20201116034758", \
        'his':"หอกตะขอที่ถูกซ่อนไว้ใน Blackcliff Forge ที่ปลายนั้นมีแสงประกายราวกับแสงดาวบนฟากฟ้ายามราตรี", \
        'type':"Polearm", 'stat':["510", "45.9%", "Energy Recharge"], \
        'ascen':"**[✦-----]**:5,000 Mora, Grain of Aerosiderite x3, Fragile Bone Shard x3, Damaged Mask x2\n \
        **[✦✦----]**:15,000 Mora, Piece of Aerosiderite x3, Fragile Bone Shard x12, Damaged Mask x8\n \
        **[✦✦✦---]**:20,000 Mora, Piece of Aerosiderite x6, Sturdy Bone Shard x6, Stained Mask x6\n \
        **[✦✦✦✦--]**:30,000 Mora, Bit of Aerosiderite x3, Sturdy Bone Shard x12, Stained Mask x9\n \
        **[✦✦✦✦✦-]**:35,000 Mora, Bit of Aerosiderite x6, Fossilized Bone Shard x9, Ominous Mask x6\n \
        **[✦✦✦✦✦✦]**:45,000 Mora, Chunk of Aerosiderite x4, Fossilized Bone Shard x18, Ominous Mask x12", 'name':"Prototype Starglitter"}
        return lst67
    elif name.lower() == "lithic spear":
        lst68 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/2/2a/Weapon_Lithic_Spear.png/revision/latest/scale-to-width-down/256?cb=20210225200953", \
        'his':"หอกยาวที่ทำขึ้นอย่างประณีตโดยใช้แผ่นหินของป้าหิน Guyun Stone Forest ตัวหอกนั้นคมและแข็งแกร่งไร้ผู้ต้านทาน", \
        'type':"Polearm", 'stat':["565", "27.6%", "ATK"], \
        'ascen':"**[✦-----]**:5,000 Mora, Grain of Aerosiderite x3, Fragile Bone Shard x3, Firm Arrowhead x2\n \
        **[✦✦----]**:15,000 Mora, Piece of Aerosiderite x3, Fragile Bone Shard x12, Firm Arrowhead x8\n \
        **[✦✦✦---]**:20,000 Mora, Piece of Aerosiderite x6, Sturdy Bone Shard x6, Sharp Arrowhead x6\n \
        **[✦✦✦✦--]**:30,000 Mora, Bit of Aerosiderite x3, Sturdy Bone Shard x12, Sharp Arrowhead x9\n \
        **[✦✦✦✦✦-]**:35,000 Mora, Bit of Aerosiderite x6, Fossilized Bone Shard x9, Weathered Arrowhead x6\n \
        **[✦✦✦✦✦✦]**:45,000 Mora, Chunk of Aerosiderite x4, Fossilized Bone Shard x18, Weathered Arrowhead", 'name':"Lithic Spear"}
        return lst68
    elif name.lower() == "kitain cross spear":
        lst69 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/1/13/Weapon_Kitain_Cross_Spear.png/revision/latest/scale-to-width-down/256?cb=20210723074313", \
        'his':'หอกที่ครั้งหนึ่งนักรบผู้มีชื่อเสียงเคยใช้คุ้มครอง "Tatarigami" บนเกาะ Yashiori', \
        'type':"Polearm", 'stat':["565", "110", "Elemental Mastery"], \
        'ascen':"**[✦-----]**:5,000 Mora, Mask of the Wicked Lieutenant x3, Chaos Gear x3, Treasure Hoarder Insignia x2\n \
        **[✦✦----]**:15,000 Mora, Mask of the Tiger's Bite x3, Chaos Gear x12, Treasure Hoarder Insignia x8\n \
        **[✦✦✦---]**:20,000 Mora, Mask of the Tiger's Bite x6, Chaos Axis x6, Silver Raven Insignia x6\n \
        **[✦✦✦✦--]**:30,000 Mora, Mask of the One-Horned x3, Chaos Axis x12, Silver Raven Insignia x9\n \
        **[✦✦✦✦✦-]**:35,000 Mora, Mask of the One-Horned x6, Chaos Oculus x9, Golden Raven Insignia x6\n \
        **[✦✦✦✦✦✦]**:45,000 Mora, Mask of the Kijin x4, Chaos Oculus x18, Golden Raven Insignia x12", 'name':"Kitain Cross Spear"}
        return lst69
    elif name.lower() == "the catch":
        lst70 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/f/f5/Weapon_The_Catch.png/revision/latest/scale-to-width-down/256?cb=20210901044833", \
        'his':"หอกที่ครั้งหนึ่งจอมโจรแห่ง Inazuma ที่มีชื่อเสียงในอดีตชอบใช้", \
        'type':"**[✦-----]**:5,000 Mora, Mask of the Wicked Lieutenant x3, Chaos Gear x3, Spectral Husk x2\n \
        **[✦✦----]**:15,000 Mora, Mask of the Tiger's Bite x3, Chaos Gear x12, Spectral Husk x8\n \
        **[✦✦✦---]**:20,000 Mora, Mask of the Tiger's Bite x6, Chaos Axis x6, Spectral Heart x6\n \
        **[✦✦✦✦--]**:30,000 Mora, Mask of the One-Horned x3, Chaos Axis x12, Spectral Heart x9\n \
        **[✦✦✦✦✦-]**:35,000 Mora, Mask of the One-Horned x6, Chaos Oculus x9, Spectral Nucleus x6\n \
        **[✦✦✦✦✦✦]**:45,000 Mora, Mask of the Kijin x4, Chaos Oculus x18, Spectral Nucleus x12", 'name':"The Catch"}
        return lst70
    elif name.lower() == "favonius lance":
        lst71 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/5/57/Weapon_Favonius_Lance.png/revision/latest/scale-to-width-down/256?cb=20201116154512", \
        'his':"หอกมาตรฐานที่ใช้งานโดย เหล่าอัศวินแห่ง Favonius ด้ามหอกตรงดิ่ง ปลายหอกแหลมคม และพลิ้วไหวดั่งสายลม", \
        'type':"Polearm", 'stat':["565", "30.6%", "Energy Recharge"], \
        'ascen':"**[✦-----]**:5,000 Mora, Fetters of the Dandelion Gladiator x3, Chaos Device x3, Slime Condensate x2\n \
        **[✦✦----]**:15,000 Mora, Chains of the Dandelion Gladiator x3, Chaos Device x12, Slime Condensate x8\n \
        **[✦✦✦---]**:20,000 Mora, Chains of the Dandelion Gladiator x6, Chaos Circuit x6, Slime Secretions x6\n \
        **[✦✦✦✦--]**:30,000 Mora, Shackles of the Dandelion Gladiator x3, Chaos Circuit x12, Slime Secretions x9\n \
        **[✦✦✦✦✦-]**:35,000 Mora, Shackles of the Dandelion Gladiator x6, Chaos Core x9, Slime Concentrate x6\n \
        **[✦✦✦✦✦✦]**:45,000 Mora, Dream of the Dandelion Gladiator x4, Chaos Core x18, Slime Concentrate x12", 'name':"Favonius Lance"}
        return lst71
    elif name.lower() == "dragonspine spear":
        lst72 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/1/1a/Weapon_Dragonspine_Spear.png/revision/latest/scale-to-width-down/256?cb=20201223042936", \
        'his':"หอกที่สร้างจากเขี้ยวของมังกร เมื่อสัมผัสแล้วให้ความรู้สึกที่อบอุ่นอย่างน่าประหลาด", \
        'type':"Polearm", 'stat':["454", "69.0%", "Physical DMG Bonus"], \
        'ascen':"**[✦-----]**:5,000 Mora, Boreal Wolf's Milk Tooth x3, Mist Grass Pollen x3, Recruit's Insignia x2\n \
        **[✦✦----]**:15,000 Mora, Boreal Wolf's Cracked Tooth x3, Mist Grass Pollen x12, Recruit's Insignia x8\n \
        **[✦✦✦---]**:20,000 Mora, Boreal Wolf's Cracked Tooth x6, Mist Grass x6, Sergeant's Insignia x6\n \
        **[✦✦✦✦--]**:30,000 Mora, Boreal Wolf's Broken Fang x3, Mist Grass x12, Sergeant's Insignia x9\n \
        **[✦✦✦✦✦-]**:35,000 Mora, Boreal Wolf's Broken Fang x6, Mist Grass Wick x9, Lieutenant's Insignia x6\n \
        **[✦✦✦✦✦✦]**:45,000 Mora, Boreal Wolf's Nostalgia x4, Mist Grass Wick x18, Lieutenant's Insignia x12", 'name':"Dragonspine Spear"}
        return lst72
    elif name.lower() == "dragon's bane":
        lst73 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/2/24/Weapon_Dragon%27s_Bane.png/revision/latest/scale-to-width-down/256?cb=20201116033629", \
        'his':"หอกที่ตกแต่งด้วยมังกรทองพันอยู่ที่ด้าม มันทั้งเบาและคม อาวุธนี้ใช้สังหารมังกรได้อย่างดี", \
        'type':"Polearm", 'stat':["454", "221", "Elemental Mastery"], \
        'ascen':"**[✦-----]**:5,000 Mora, Mist Veiled Lead Elixir x3, Mist Grass Pollen x3, Divining Scroll x2\n \
        **[✦✦----]**:15,000 Mora, Mist Veiled Mercury Elixir x3, Mist Grass Pollen x12, Divining Scroll x8\n \
        **[✦✦✦---]**:20,000 Mora, Mist Veiled Mercury Elixir x6, Mist Grass x6, Sealed Scroll x6\n \
        **[✦✦✦✦--]**:30,000 Mora, Mist Veiled Gold Elixir x3, Mist Grass x12, Sealed Scroll x9\n \
        **[✦✦✦✦✦-]**:35,000 Mora, Mist Veiled Gold Elixir x6, Mist Grass Wick x9, Forbidden Curse Scroll x6\n \
        **[✦✦✦✦✦✦]**:45,000 Mora, Mist Veiled Primo Elixir x4, Mist Grass Wick x18, Forbidden Curse Scroll x12", 'name':"Dragon's Bane"}
        return lst73
    elif name.lower() == "deathmatch":
        lst74 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/6/69/Weapon_Deathmatch.png/revision/latest/scale-to-width-down/256?cb=20201116154647", \
        'his':"หอกคมยาวสีแดงเลือดซึ่งเคยเป็นสมบัติของนักสู่ในสมัยก่อน ปลายหอกถูกย้อมไปด้วยเลือดของสัตว์ร้ายและผู้คนนับไม่ถ้วน", \
        'type':"Polearm", 'stat':["454", "36.8%", "CRIT Rate"], \
        'ascen':"**[✦-----]**:5,000 Mora, Boreal Wolf's Milk Tooth x3, Dead Ley Line Branch x3, Whopperflower Nectar x2\n \
        **[✦✦----]**:15,000 Mora, Boreal Wolf's Cracked Tooth x3, Dead Ley Line Branch x12, Whopperflower Nectar x8\n \
        **[✦✦✦---]**:20,000 Mora, Boreal Wolf's Cracked Tooth x6, Dead Ley Line Leaves x6, Shimmering Nectar x6\n \
        **[✦✦✦✦--]**:30,000 Mora, Boreal Wolf's Broken Fang x3, Dead Ley Line Leaves x12, Shimmering Nectar x9\n \
        **[✦✦✦✦✦-]**:35,000 Mora, Boreal Wolf's Broken Fang x6, Ley Line Sprout x9, Energy Nectar x6\n \
        **[✦✦✦✦✦✦]**:45,000 Mora, Boreal Wolf's Nostalgia x4, Ley Line Sprout x18, Energy Nectar x12", 'name':"Deathmatch"}
        return lst74
    elif name.lower() == "crescent pike":
        lst75 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/4/4c/Weapon_Crescent_Pike.png/revision/latest/scale-to-width-down/256?cb=20201116033544", \
        'his':"อาวุธหายากที่มีใบมีดยาวอยู่ที่ปลายด้านบนและมีใบมีดรูปจันทร์เสี้ยวอยู่ที่ปลายด้านล่าง ถูกนำมา Liyue โดยผู้ค้าต่างถิ่น ซึ่งหากใช้งานมันได้อย่างคล่องแคล่วแล้วจะสร้างความเสียหายได้อย่างมากเลยทีเดียว", \
        'type':"Polearm", 'stat':["565", "34.5%", "Physical DMG Bonus"], \
        'ascen':"**[✦-----]**:5,000 Mora, Luminous Sands from Guyun x3, Hunter's Sacrificial Knife x3, Treasure Hoarder Insignia x2\n \
        **[✦✦----]**:15,000 Mora, Lustrous Stone from Guyun x3, Hunter's Sacrificial Knife x12, Treasure Hoarder Insignia x8\n \
        **[✦✦✦---]**:20,000 Mora, Lustrous Stone from Guyun x6, Agent's Sacrificial Knife x6, Silver Raven Insignia x6\n \
        **[✦✦✦✦--]**:30,000 Mora, Relic from Guyun x3, Agent's Sacrificial Knife x12, Silver Raven Insignia x9\n \
        **[✦✦✦✦✦-]**:35,000 Mora, Relic from Guyun x6, Inspector's Sacrificial Knife x9, Golden Raven Insignia x6\n \
        **[✦✦✦✦✦✦]**:45,000 Mora, Divine Body from Guyun x4, Inspector's Sacrificial Knife x18, Golden Raven Insignia x12", 'name':"Crescent Pike"}
        return lst75
    elif name.lower() == "blackcliff pole":
        lst76 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/d/d5/Weapon_Blackcliff_Pole.png/revision/latest/scale-to-width-down/256?cb=20201116153435", \
        'his':"อาวุธนี้ทำมาจากหิน blackstone และ aerosiderite ทั้งยังมีประกายสีแดงก่ำบนความระยิบระยับของมัน", \
        'type':"Polearm", 'stat':["510", "55.1%", "CRIT DMG"], \
        'ascen':"**[✦-----]**:5,000 Mora, Mist Veiled Lead Elixir x3, Mist Grass Pollen x3, Recruit's Insignia x2\n \
        **[✦✦----]**:15,000 Mora, Mist Veiled Mercury Elixir x3, Mist Grass Pollen x12, Recruit's Insignia x8\n \
        **[✦✦✦---]**:20,000 Mora, Mist Veiled Mercury Elixir x6, Mist Grass x6, Sergeant's Insignia x6\n \
        **[✦✦✦✦--]**:30,000 Mora, Mist Veiled Gold Elixir x3, Mist Grass x12, Sergeant's Insignia x9\n \
        **[✦✦✦✦✦-]**:35,000 Mora, Mist Veiled Gold Elixir x6, Mist Grass Wick x9, Lieutenant's Insignia x6\n \
        **[✦✦✦✦✦✦]**:45,000 Mora, Mist Veiled Primo Elixir x4, Mist Grass Wick x18, Lieutenant's Insignia x12", 'name':"Blackcliff Pole"}
        return lst76
    elif name.lower() == "wavebreaker's fin":
        lst77 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/6/66/Weapon_Wavebreaker%27s_Fin.png/revision/latest/scale-to-width-down/256?cb=20211112091108", \
        'his':"นางินาตะที่ทำจากวัสดุแวววาวที่มาจากห้วงลึกใต้ท้องทะเล ครั้งหนึ่งมันเคยเป็นสมบัติของเผ่าเท็งงุ", \
        'type':"Polearm", 'stat':["620", "13.8%", "ATK"], \
        'ascen':"**[✦-----]**:5,000 Mora, Mask of the Wicked Lieutenant x3, Chaos Gear x3, Old Handguard x2\n \
        **[✦✦----]**:15,000 Mora, Mask of the Tiger's Bite x3, Chaos Gear x12, Old Handguard x8\n \
        **[✦✦✦---]**:20,000 Mora, Mask of the Tiger's Bite x6, Chaos Axis x6, Kageuchi Handguard x6\n \
        **[✦✦✦✦--]**:30,000 Mora, Mask of the One-Horned x3, Chaos Axis x12, Kageuchi Handguard x9\n \
        **[✦✦✦✦✦-]**:35,000 Mora, Mask of the One-Horned x6, Chaos Oculus x9, Famed Handguard x6\n \
        **[✦✦✦✦✦✦]**:45,000 Mora, Mask of the Kijin x4, Chaos Oculus x18, Famed Handguard x12", 'name':"Wavebreaker's Fin"}
        return lst77
    elif name.lower() == "royal spear":
        lst78 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/f/fd/Weapon_Royal_Spear.png/revision/latest/scale-to-width-down/256?cb=20201202041704", \
        'his':"หอกของชนชั้นสูงผู้ซึ่งครั้งหนึ่งเคยปกครอง Mondstadt แม้จะผ่านมานานหลายปี แต่ก็ยังเฉียบคมอย่างไม่อาจเทียบได้", \
        'type':"Polearm", 'stat':["565", "27.6%", "ATK"], \
        'ascen':"**[✦-----]**:5,000 Mora, Mist Veiled Lead Elixir x3, Mist Grass Pollen x3, Recruit's Insignia x2\n \
        **[✦✦----]**:15,000 Mora, Mist Veiled Mercury Elixir x3, Mist Grass Pollen x12, Recruit's Insignia x8\n \
        **[✦✦✦---]**:20,000 Mora, Mist Veiled Mercury Elixir x6, Mist Grass x6, Sergeant's Insignia x6\n \
        **[✦✦✦✦--]**:30,000 Mora, Mist Veiled Gold Elixir x3, Mist Grass x12, Sergeant's Insignia x9\n \
        **[✦✦✦✦✦-]**:35,000 Mora, Mist Veiled Gold Elixir x6, Mist Grass Wick x9, Lieutenant's Insignia x6\n \
        **[✦✦✦✦✦✦]**:45,000 Mora, Mist Veiled Primo Elixir x4, Mist Grass Wick x18, Lieutenant's Insignia x12", 'name':"Royal Spear"}
        return lst78
    elif name.lower() == "the flute":
        lst79 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/6/63/Weapon_The_Flute.png/revision/latest/scale-to-width-down/256?cb=20201119203316", \
        'his':"ภายใต้สนิมนั้นมีดาบบาง ๆ ที่ตกแต่งอย่างหรูหราอยู่ คุณสามารถกวัดแกว่งมันได้อย่างรวดเร็วดั่งสายลม", \
        'type':"Sword", 'stat':["510", "41.3%", "ATK"], \
        'ascen':"**[✦-----]**:5,000 Mora, Boreal Wolf's Milk Tooth x3, Dead Ley Line Branch x3, Slime Condensate x2\n \
        **[✦✦----]**:15,000 Mora, Boreal Wolf's Cracked Tooth x3, Dead Ley Line Branch x12, Slime Condensate x8\n \
        **[✦✦✦---]**:20,000 Mora, Boreal Wolf's Cracked Tooth x6, Dead Ley Line Leaves x6, Slime Secretions x6\n \
        **[✦✦✦✦--]**:30,000 Mora, Boreal Wolf's Broken Fang x3, Dead Ley Line Leaves x12, Slime Secretions x9\n \
        **[✦✦✦✦✦-]**:35,000 Mora, Boreal Wolf's Broken Fang x6, Ley Line Sprout x9, Slime Concentrate x6\n \
        **[✦✦✦✦✦✦]**:45,000 Mora, Boreal Wolf's Nostalgia x4, Ley Line Sprout x18, Slime Concentrate x12", 'name':"The Flute"}
        return lst79
    elif name.lower() == "the black sword":
        lst80 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/c/cf/Weapon_The_Black_Sword.png/revision/latest/scale-to-width-down/256?cb=20201116035352", \
        'his':"ดาบสีดำยาวที่กระหายเพียงความขัดแย้งและฆ่าฟัน กล่าวกันว่ามันทำให้ผู้คนมัวเมาไปกับการต่อสู้ที่นองเลือด", \
        'type':"Sword", 'stat':["510", "27.6%", "CRIT Rate"], \
        'ascen':"**[✦-----]**:5,000 Mora, Boreal Wolf's Milk Tooth x3, Dead Ley Line Branch x3, Slime Condensate x2\n \
        **[✦✦----]**:15,000 Mora, Boreal Wolf's Cracked Tooth x3, Dead Ley Line Branch x12, Slime Condensate x8\n \
        **[✦✦✦---]**:20,000 Mora, Boreal Wolf's Cracked Tooth x6, Dead Ley Line Leaves x6, Slime Secretions x6\n \
        **[✦✦✦✦--]**:30,000 Mora, Boreal Wolf's Broken Fang x3, Dead Ley Line Leaves x12, Slime Secretions x9\n \
        **[✦✦✦✦✦-]**:35,000 Mora, Boreal Wolf's Broken Fang x6, Ley Line Sprout x9, Slime Concentrate x6\n \
        **[✦✦✦✦✦✦]**:45,000 Mora, Boreal Wolf's Nostalgia x4, Ley Line Sprout x18, Slime Concentrate x12", 'name':"The Black Sword"}
        return lst80
    elif name.lower() == "the alley flash":
        lst81 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/8/83/Weapon_The_Alley_Flash.png/revision/latest/scale-to-width-down/256?cb=20210317151138", \
        'his':"ดาบตรงสีดำยาว ราวกับราตรีอันมืดมิด ครั้งหนึ่งเคยเป็นของโจร ที่ร่อนเร่ไปมาในตรอกมืด", \
        'type':"Sword", 'stat':["620", "55", "Elemental Mastery"], \
        'ascen':"**[✦-----]**:5,000 Mora, Tile of Decarabian's Tower x3, Heavy Horn x3, Divining Scroll x2\n \
        **[✦✦----]**:15,000 Mora, Debris of Decarabian's City x3, Heavy Horn x12, Divining Scroll x8\n \
        **[✦✦✦---]**:20,000 Mora, Debris of Decarabian's City x6, Black Bronze Horn x6, Sealed Scroll x6\n \
        **[✦✦✦✦--]**:30,000 Mora, Fragment of Decarabian's Epic x3, Black Bronze Horn x12, Sealed Scroll x9\n \
        **[✦✦✦✦✦-]**:35,000 Mora, Fragment of Decarabian's Epic x6, Black Crystal Horn x9, Forbidden Curse Scroll x6\n \
        **[✦✦✦✦✦✦]**:45,000 Mora, Scattered Piece of Decarabian's Dream x4, Black Crystal Horn x18, Forbidden Curse Scroll x12", 'name':"The Alley Flash"}
        return lst81
    elif name.lower() == "sword of descension":
        lst82 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/1/17/Weapon_Sword_of_Descension.png/revision/latest/scale-to-width-down/256?cb=20201116035338", \
        'his':"ดาบที่มีรูปร่างอันเป็นเอกลักษณ์ ดูเหมือนว่าจะไม่ได้มาจากโลกนี้", \
        'type':"Sword", 'stat':["440", "35.2%", "ATK"], \
        'ascen':"**[✦-----]**:5,000 Mora, Boreal Wolf's Milk Tooth x3, Dead Ley Line Branch x3, Treasure Hoarder Insignia x2\n \
        **[✦✦----]**:15,000 Mora, Boreal Wolf's Cracked Tooth x3, Dead Ley Line Branch x12, Treasure Hoarder Insignia x8\n \
        **[✦✦✦---]**:20,000 Mora, Boreal Wolf's Cracked Tooth x6, Dead Ley Line Leaves x6, Silver Raven Insignia x6\n \
        **[✦✦✦✦--]**:30,000 Mora, Boreal Wolf's Broken Fang x3, Dead Ley Line Leaves x12, Silver Raven Insignia x9\n \
        **[✦✦✦✦✦-]**:35,000 Mora, Boreal Wolf's Broken Fang x6, Ley Line Sprout x9, Golden Raven Insignia x6\n \
        **[✦✦✦✦✦✦]**:45,000 Mora, Boreal Wolf's Nostalgia x4, Ley Line Sprout x18, Golden Raven Insignia x12", 'name':"Sword of Descension"}
        return lst82
    elif name.lower() == "sacrificial sword":
        lst83 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/a/a0/Weapon_Sacrificial_Sword.png/revision/latest/scale-to-width-down/256?cb=20201120010840", \
        'his':"ดาบที่ตกแต่งอย่างสวยงามและกลายเป็นหินไปตามกาลเวลา ของที่ตกแต่งดาบยังคงเห็นได้อยู่ และมันให้พลังกับผู้ใช้เพื่อรับมือกับสายลมแห่งเวลา", \
        'type':"Sword", 'stat':["454", "61.3%", "Energy Recharge"], \
        'ascen':"**[✦-----]**:5,000 Mora, Fetters of the Dandelion Gladiator x3, Chaos Device x3, Divining Scroll x2\n \
        **[✦✦----]**:15,000 Mora, Chains of the Dandelion Gladiator x3, Chaos Device x12, Divining Scroll x8\n \
        **[✦✦✦---]**:20,000 Mora, Chains of the Dandelion Gladiator x6, Chaos Circuit x6, Sealed Scroll x6\n \
        **[✦✦✦✦--]**:30,000 Mora, Shackles of the Dandelion Gladiator x3, Chaos Circuit x12, Sealed Scroll x9\n \
        **[✦✦✦✦✦-]**:35,000 Mora, Shackles of the Dandelion Gladiator x6, Chaos Core x9, Forbidden Curse Scroll x6\n \
        **[✦✦✦✦✦✦]**:45,000 Mora, Dream of the Dandelion Gladiator x4, Chaos Core x18, Forbidden Curse Scroll x12", 'name':"Sacrificial Sword"}
        return lst83
    elif name.lower() == "royal longsword":
        lst84 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/c/cd/Weapon_Royal_Longsword.png/revision/latest/scale-to-width-down/256?cb=20201116034952", \
        'his':"ดาบยาวสภาพเก่าแก่เล่มหนึ่งของชนชั้นสูงผู้ที่ครั้งหนึ่งเคยปกครอง Mondstadt มันถูกสร้างขึ้นอย่างประณีต การตกแต่งบนตัวดาบแสดงถึงสถานะของเจ้าของมัน", \
        'type':"Sword", 'stat':["510", "41.3%", "ATK"], \
        'ascen':"**[✦-----]**:5,000 Mora, Tile of Decarabian's Tower x3, Heavy Horn x3, Firm Arrowhead x2\n \
        **[✦✦----]**:15,000 Mora, Debris of Decarabian's City x3, Heavy Horn x12, Firm Arrowhead x8\n \
        **[✦✦✦---]**:20,000 Mora, Debris of Decarabian's City x6, Black Bronze Horn x6, Sharp Arrowhead x6\n \
        **[✦✦✦✦--]**:30,000 Mora, Fragment of Decarabian's Epic x3, Black Bronze Horn x12, Sharp Arrowhead x9\n \
        **[✦✦✦✦✦-]**:35,000 Mora, Fragment of Decarabian's Epic x6, Black Crystal Horn x9, Weathered Arrowhead x6\n \
        **[✦✦✦✦✦✦]**:45,000 Mora, Scattered Piece of Decarabian's Dream x4, Black Crystal Horn x18, Weathered Arrowhead x12", 'name':"Royal Longsword"}
        return lst84
    elif name.lower() == "prototype rancour":
        lst85 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/e/ef/Weapon_Prototype_Rancour.png/revision/latest/scale-to-width-down/256?cb=20201116034823", \
        'his':"ดาบยาวโบราณที่ถูกซ่อนไว้ใน Blackcliff Forge มันสามารถตัดผ่านหินได้และดาบไม่บิ่น", \
        'type':"Sword", 'stat':["565", "34.5%", "Physical DMG Bonus"], \
        'ascen':"**[✦-----]**:5,000 Mora, Mist Veiled Lead Elixir x3, Mist Grass Pollen x3, Recruit's Insignia x2\n \
        **[✦✦----]**:15,000 Mora, Mist Veiled Mercury Elixir x3, Mist Grass Pollen x12, Recruit's Insignia x8\n \
        **[✦✦✦---]**:20,000 Mora, Mist Veiled Mercury Elixir x6, Mist Grass x6, Sergeant's Insignia x6\n \
        **[✦✦✦✦--]**:30,000 Mora, Mist Veiled Gold Elixir x3, Mist Grass x12, Sergeant's Insignia x9\n \
        **[✦✦✦✦✦-]**:35,000 Mora, Mist Veiled Gold Elixir x6, Mist Grass Wick x9, Lieutenant's Insignia x6\n \
        **[✦✦✦✦✦✦]**:45,000 Mora, Mist Veiled Primo Elixir x4, Mist Grass Wick x18, Lieutenant's Insignia x12", 'name':"Prototype Rancour"}
        return lst85
    elif name.lower() == "amenoma kageuchi":
        lst86 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/e/ea/Weapon_Amenoma_Kageuchi.png/revision/latest/scale-to-width-down/256?cb=20210723074436", \
        'his':"ตามตำนานกล่าวกันว่า นี่คือดาบที่ถูกสั่งทำขึ้นเป็นพิเศษโดยซามูไรที่มีชื่อเสียง ซึ่งแม้แต่เท็งงุที่รวดเร็วดั่งสายฟ้า ก็ยังสามารถฟันให้ร่วงลงมาได้", \
        'type':"Sword", 'stat':["454", "55.1%", "ATK"], \
        'ascen':"**[✦-----]**:5,000 Mora, Coral Branch of a Distant Sea x3, Chaos Gear x3, Old Handguard x2\n \
        **[✦✦----]**:15,000 Mora, Jeweled Branch of a Distant Sea x3, Chaos Gear x12, Old Handguard x8\n \
        **[✦✦✦---]**:20,000 Mora, Jeweled Branch of a Distant Sea x6, Chaos Axis x6, Kageuchi Handguard x6\n \
        **[✦✦✦✦--]**:30,000 Mora, Jade Branch of a Distant Sea x3, Chaos Axis x12, Kageuchi Handguard x9\n \
        **[✦✦✦✦✦-]**:35,000 Mora, Jade Branch of a Distant Sea x6, Chaos Oculus x9, Famed Handguard x6\n \
        **[✦✦✦✦✦✦]**:45,000 Mora, Golden Branch of a Distant Sea x4, Chaos Oculus x18, Famed Handguard x12", 'name':"Amenoma Kageuchi"}
        return lst86
    elif name.lower() == "lion's roar":
        lst87 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/e/e6/Weapon_Lion%27s_Roar.png/revision/latest/scale-to-width-down/256?cb=20201119232745", \
        'his':"คมดาบและการสลักตกแต่งที่ไม่เข้ากันกับความคมและความทนทานของมัน เสียงในเวลาที่ตัดผ่าอากาศนั้นราวกับเสียงค่ารามของสิงโต", \
        'type':"Sword", 'stat':["510", "41.3%", "ATK"], \
        'ascen':"**[✦-----]**:5,000 Mora, Luminous Sands from Guyun x3, Hunter's Sacrificial Knife x3, Treasure Hoarder Insignia x2\n \
        **[✦✦----]**:15,000 Mora, Lustrous Stone from Guyun x3, Hunter's Sacrificial Knife x12, Treasure Hoarder Insignia x8\n \
        **[✦✦✦---]**:20,000 Mora, Lustrous Stone from Guyun x6, Agent's Sacrificial Knife x6, Silver Raven Insignia x6\n \
        **[✦✦✦✦--]**:30,000 Mora, Relic from Guyun x3, Agent's Sacrificial Knife x12, Silver Raven Insignia x9\n \
        **[✦✦✦✦✦-]**:35,000 Mora, Relic from Guyun x6, Inspector's Sacrificial Knife x9, Golden Raven Insignia x6\n \
        **[✦✦✦✦✦✦]**:45,000 Mora, Divine Body from Guyun x4, Inspector's Sacrificial Knife x18, Golden Raven Insignia x12", 'name':"Lion's Roar"}
        return lst87
    elif name.lower() == "iron sting":
        lst88 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/3/35/Weapon_Iron_Sting.png/revision/latest/scale-to-width-down/256?cb=20201116034058", \
        'his':"ดาบสำหรับแทงรูปร่างเรียวบางที่หาได้ยาก ซึ่งจะพบได้จากเหล่าผู้ค้าจากต่างแดนที่เดินทางมาถึง Liyue มันทั้งเบา คล่องแคล่ว และคม", \
        'type':"Sword", 'stat':["510", "165", "Elemental Mastery"], \
        'ascen':"**[✦-----]**:5,000 Mora, Grain of Aerosiderite x3, Fragile Bone Shard x3, Whopperflower Nectar x2\n \
        **[✦✦----]**:15,000 Mora, Piece of Aerosiderite x3, Fragile Bone Shard x12, Whopperflower Nectar x8\n \
        **[✦✦✦---]**:20,000 Mora, Piece of Aerosiderite x6, Sturdy Bone Shard x6, Shimmering Nectar x6\n \
        **[✦✦✦✦--]**:30,000 Mora, Bit of Aerosiderite x3, Sturdy Bone Shard x12, Shimmering Nectar x9\n \
        **[✦✦✦✦✦-]**:35,000 Mora, Bit of Aerosiderite x6, Fossilized Bone Shard x9, Energy Nectar x6\n \
        **[✦✦✦✦✦✦]**:45,000 Mora, Chunk of Aerosiderite x4, Fossilized Bone Shard x18, Energy Nectar x12", 'name':"Iron Sting"}
        return lst88
    elif name.lower() == "festering desire":
        lst89 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/7/70/Weapon_Festering_Desire.png/revision/latest/scale-to-width-down/256?cb=20201223042935", \
        'his':"ดามที่ชั่วร้ายนี้ดูเหมือนจะกระหายอยากเอาชีวิต มันมีพิษที่สามารถกัดกร่อนได้แม้กระทั่งมังกร", \
        'type':"Sword", 'stat':["510", "45.9%", "Energy Recharge"], \
        'ascen':"**[✦-----]**:5,000 Mora, Fetters of the Dandelion Gladiator x3, Heavy Horn x3, Recruit's Insignia x2\n \
        **[✦✦----]**:15,000 Mora, Chains of the Dandelion Gladiator x3, Heavy Horn x12, Recruit's Insignia x8\n \
        **[✦✦✦---]**:20,000 Mora, Chains of the Dandelion Gladiator x6, Black Bronze Horn x6, Sergeant's Insignia x6\n \
        **[✦✦✦✦--]**:30,000 Mora, Shackles of the Dandelion Gladiator x3, Black Bronze Horn x12, Sergeant's Insignia x9\n \
        **[✦✦✦✦✦-]**:35,000 Mora, Shackles of the Dandelion Gladiator x6, Black Crystal Horn x9, Lieutenant's Insignia x6\n \
        **[✦✦✦✦✦✦]**:45,000 Mora, Dream of the Dandelion Gladiator x4, Black Crystal Horn x18, Lieutenant's Insignia x12", 'name':"Festering Desire"}
        return lst89
    elif name.lower() == "favonius sword":
        lst90 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/9/90/Weapon_Favonius_Sword.png/revision/latest/scale-to-width-down/256?cb=20201116033811", \
        'his':"ดาบยาวมาตรฐานที่ใช้งานโดยเหล่าอัศวินแห่ง Favonius การรวบรวมพลังงานธาตุจะไม่ใช่เรื่องยากอีกต่อไปเมื่อใช้ดาบที่ทั้งคมและเบาเช่นดาบนี้!", \
        'type':"Sword", 'stat':["454", "61.3%", "Energy Recharge"], \
        'ascen':"**[✦-----]**:5,000 Mora, Tile of Decarabian's Tower x3, Heavy Horn x3, Firm Arrowhead x2\n \
        **[✦✦----]**:15,000 Mora, Debris of Decarabian's City x3, Heavy Horn x12, Firm Arrowhead x8\n \
        **[✦✦✦---]**:20,000 Mora, Debris of Decarabian's City x6, Black Bronze Horn x6, Sharp Arrowhead x6\n \
        **[✦✦✦✦--]**:30,000 Mora, Fragment of Decarabian's Epic x3, Black Bronze Horn x12, Sharp Arrowhead x9\n \
        **[✦✦✦✦✦-]**:35,000 Mora, Fragment of Decarabian's Epic x6, Black Crystal Horn x9, Weathered Arrowhead x6\n \
        **[✦✦✦✦✦✦]**:45,000 Mora, Scattered Piece of Decarabian's Dream x4, Black Crystal Horn x18, Weathered Arrowhead x12", 'name':"Favonius Sword"}
        return lst90
    elif name.lower() == "cinnabar spindle":
        lst91 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/d/dc/Weapon_Cinnabar_Spindle.png/revision/latest/scale-to-width-down/256?cb=20211125225624", \
        'his':"ดาบที่คล้ายจะไม่ได้ทำจากวัสดุบนโลกนี้ พลังของมันนั้นคงจะสามารถต้านทานได้กระทั่งพิษกัดกร่อนของมังกรเลยล่ะนะ", \
        'type':"Sword", 'stat':["454", "69.0%", "DEF"], \
        'ascen':"**[✦-----]**:5,000 Mora, Tile of Decarabian's Tower x3, Chaos Device x3, Damaged Mask x2\n \
        **[✦✦----]**:15,000 Mora, Debris of Decarabian's City x3, Chaos Device x12, Damaged Mask x8\n \
        **[✦✦✦---]**:20,000 Mora, Debris of Decarabian's City x6, Chaos Circuit x6, Stained Mask x6\n \
        **[✦✦✦✦--]**:30,000 Mora, Fragment of Decarabian's Epic x3, Chaos Circuit Horn x12, Stained Mask x9\n \
        **[✦✦✦✦✦-]**:35,000 Mora, Fragment of Decarabian's Epic x6, Chaos Core x9, Ominous Mask x6\n \
        **[✦✦✦✦✦✦]**:45,000 Mora, Scattered Piece of Decarabian's Dream x4, Chaos Core x18, Ominous Mask x12", 'name':"Cinnabar Spindle"}
        return lst91
    elif name.lower() == "blackcliff longsword":
        lst92 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/6/6f/Weapon_Blackcliff_Longsword.png/revision/latest/scale-to-width-down/256?cb=20201116033216", \
        'his':"Blackcliff ตีเหล็กจนเป็นตาบยาว สีดำของตัวดาบเผยให้เห็นประกายของเลือด", \
        'type':"Sword", 'stat':["565", "36.8%", "CRIT DMG"], \
        'ascen':"**[✦-----]**:5,000 Mora, Luminous Sands from Guyun x3, Hunter's Sacrificial Knife x3, Firm Arrowhead x2\n \
        **[✦✦----]**:15,000 Mora, Lustrous Stone from Guyun x3, Hunter's Sacrificial Knife x12, Firm Arrowhead x8\n \
        **[✦✦✦---]**:20,000 Mora, Lustrous Stone from Guyun x6, Agent's Sacrificial Knife x6, Sharp Arrowhead x6\n \
        **[✦✦✦✦--]**:30,000 Mora, Relic from Guyun x3, Agent's Sacrificial Knife x12, Sharp Arrowhead x9\n \
        **[✦✦✦✦✦-]**:35,000 Mora, Relic from Guyun x6, Inspector's Sacrificial Knife x9, Weathered Arrowhead x6\n \
        **[✦✦✦✦✦✦]**:45,000 Mora, Divine Body from Guyun x4, Inspector's Sacrificial Knife x18, Weathered Arrowhead x12", 'name':"Blackcliff Longsword"}
        return lst92
    elif name.lower() == "raven bow":
        lst93 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/d/d0/Weapon_Raven_Bow.png/revision/latest/scale-to-width-down/256?cb=20201116034840", \
        'his':"กาเป็นที่รู้จักกันว่า เป็นคนเรือข้ามฟากของคนตาย ก้านธนูถูกตกแต่งด้วยขนนกกาซึ่งเป็นต้นเหตุของการเสียชีวิตของเป้าหมาย", \
        'type':"Bow", 'stat':["448", "94", "Elemental Mastery"], \
        'ascen':"**[✦-----]**:5,000 Mora, Tile of Decarabian's Tower x2, Heavy Horn x2, Firm Arrowhead x1\n \
        **[✦✦----]**:10,000 Mora, Debris of Decarabian's City x2, Heavy Horn 8, Firm Arrowhead x5\n \
        **[✦✦✦---]**:15,000 Mora, Debris of Decarabian's City x4, Black Bronze Horn x4, Sharp Arrowhead x4\n \
        **[✦✦✦✦--]**:20,000 Mora, Fragment of Decarabian's Epic x2, Black Bronze Horn x8, Sharp Arrowhead x6\n \
        **[✦✦✦✦✦-]**:25,000 Mora, Fragment of Decarabian's Epic x4, Black Crystal Horn x6, Weathered Arrowhead x4\n \
        **[✦✦✦✦✦✦]**:30,000 Mora, Scattered Piece of Decarabian's Dream x3, Black Crystal Horn x12, Weathered Arrowhead x8", 'name':"Raven Bow"}
        return lst93
    elif name.lower() == "recurve bow":
        lst94 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/b/b5/Weapon_Recurve_Bow.png/revision/latest/scale-to-width-down/256?cb=20201120005927", \
        'his':"ว่ากันว่าธนูคันนี้สามารถ ยิงอินทรีย์ที่กำลังบินร่อนอยู่ได้ แต่ที่จริงแล้วมันขึ้นอยู่กับฝีมือของผู้ใช้งานมากกว่า", \
        'type':"Bow", 'stat':["354", "46.9%", "HP"], \
        'ascen':"**[✦-----]**:5,000 Mora, Fetters of the Dandelion Gladiator x2, Heavy Horn x2, Recruit's Insignia x1\n \
        **[✦✦----]**:10,000 Mora, Chains of the Dandelion Gladiator x2, Heavy Horn x8, Recruit's Insignia x5\n \
        **[✦✦✦---]**:15,000 Mora, Chains of the Dandelion Gladiator x4, Black Bronze Horn x4, Sergeant's Insignia x4\n \
        **[✦✦✦✦--]**:20,000 Mora, Shackles of the Dandelion Gladiator x2, Black Bronze Horn x8, Sergeant's Insignia x6\n \
        **[✦✦✦✦✦-]**:25,000 Mora, Shackles of the Dandelion Gladiator x4, Black Crystal Horn x6, Lieutenant's Insignia x4\n \
        **[✦✦✦✦✦✦]**:30,000 Mora, Dream of the Dandelion Gladiator x3, Black Crystal Horn x12, Lieutenant's Insignia x8", 'name':"Recurve Bow"}
        return lst94
    elif name.lower() == "messenger":
        lst95 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/3/38/Weapon_Messenger.png/revision/latest/scale-to-width-down/256?cb=20201116034227", \
        'his':"คันธนูแบนที่ทำขึ้นอย่างง่าย ๆ ที่ครั้งหนึ่งเคยใช้สำหรับการสื่อสารส่งข้อความ", \
        'type':"Bow", 'stat':["448", "31.2%", "CRIT DMG"], \
        'ascen':"**[✦-----]**:5,000 Mora, Mist Veiled Lead Elixir x2, Mist Grass Pollen x2, Treasure Hoarder Insignia x1\n \
        **[✦✦----]**:10,000 Mora, Mist Veiled Mercury Elixir x2, Mist Grass Pollen x8, Treasure Hoarder Insignia x5\n \
        **[✦✦✦---]**:15,000 Mora, Mist Veiled Mercury Elixir x4, Mist Grass x4, Silver Raven Insignia x4\n \
        **[✦✦✦✦--]**:20,000 Mora, Mist Veiled Gold Elixir x2, Mist Grass x8, Silver Raven Insignia x6\n \
        **[✦✦✦✦✦-]**:25,000 Mora, Mist Veiled Gold Elixir x4, Mist Grass Wick x6, Golden Raven Insignia x4\n \
        **[✦✦✦✦✦✦]**:30,000 Mora, Mist Veiled Primo Elixir x3, Mist Grass Wick x12, Golden Raven Insignia x8", 'name':"Messenger"}
        return lst95
    elif name.lower() == "sharpshooter's Oath":
        lst96 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/5/52/Weapon_Sharpshooter%27s_Oath.png/revision/latest/scale-to-width-down/256?cb=20201116035135", \
        'his':"คันธนูอันยอดเยี่ยมที่ครั้งหนึ่ง เคยเป็นของยอดนักธนู แต่มันมีกลิ่นที่แรงมาก ทำให้ไม่เหมาะกับการล่า", \
        'type':"Bow", 'stat':["401", "46.9%", "CRIT DMG"], \
        'ascen':"**[✦-----]**:5,000 Mora, Boreal Wolf's Milk Tooth x2, Dead Ley Line Branch x2, Slime Condensate x1\n \
        **[✦✦----]**:10,000 Mora, Boreal Wolf's Cracked Tooth x2, Dead Ley Line Branch x8, Slime Condensate x5\n \
        **[✦✦✦---]**:15,000 Mora, Boreal Wolf's Cracked Tooth x4, Dead Ley Line Leaves x4, Slime Secretions x4\n \
        **[✦✦✦✦--]**:20,000 Mora, Boreal Wolf's Broken Fang x2, Dead Ley Line Leaves x8, Slime Secretions x6\n \
        **[✦✦✦✦✦-]**:25,000 Mora, Boreal Wolf's Broken Fang x4, Ley Line Sprout x6, Slime Concentrate x4\n \
        **[✦✦✦✦✦✦]**:30,000 Mora, Boreal Wolf's Nostalgia x3, Ley Line Sprout x12, Slime Concentrate x8", 'name':"Sharpshooter's Oath"}
        return lst96
    elif name.lower() == "slingshot":
        lst97 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/c/ca/Weapon_Slingshot.png/revision/latest/scale-to-width-down/256?cb=20201116035308", \
        'his':"แม้มีชื่อแบบนี้ แต่แท้จริงแล้วเป็นคันธนู หลังจากพัฒนาและทดลองมานับครั้งไม่ถ้วนโดยผู้สร้างสุดยอดหนังสติ๊ก ก็พบว่าตัวเองได้สร้างธนูขึ้นมาซะแล้ว", \
        'type':"Bow", 'stat':["354", "31.2%", "CRIT Rate"], \
        'ascen':"**[✦-----]**:5,000 Mora, Luminous Sands from Guyun x2, Hunter's Sacrificial Knife x2, Damaged Mask x1\n \
        **[✦✦----]**:10,000 Mora, Lustrous Stone from Guyun x2, Hunter's Sacrificial Knife x8, Damaged Mask x5\n \
        **[✦✦✦---]**:15,000 Mora, Lustrous Stone from Guyun x4, Agent's Sacrificial Knife x4, Stained Mask x4\n \
        **[✦✦✦✦--]**:20,000 Mora, Relic from Guyun x2, Agent's Sacrificial Knife x8, Stained Mask x6\n \
        **[✦✦✦✦✦-]**:25,000 Mora, Relic from Guyun x4, Inspector's Sacrificial Knife x6, Ominous Mask x4\n \
        **[✦✦✦✦✦✦]**:30,000 Mora, Divine Body from Guyun x3, Inspector's Sacrificial Knife x12, Ominous Mask x8", 'name':"Slingshot"}
        return lst97
    elif name.lower() == "magic guide":
        lst98 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/3/39/Weapon_Magic_Guide.png/revision/latest/scale-to-width-down/256?cb=20201119232047", \
        'his':"ตีพิมพ์ครั้งที่ 12 หนังสือที่ตีพิมพ์และปรับปรงจาก 11 ครั้งที่ผ่านมา พร้อมกับเพิ่มเนื้อหาที่ได้รับ การพัฒนาแล้วด้วย", \
        'type':"Catalyst", 'stat':["354", "187", "Elemental Mastery"], \
        'ascen':"**[✦-----]**:5,000 Mora, Tile of Decarabian's Tower x2, Heavy Horn x2, Slime Condensate x1\n \
        **[✦✦----]**:10,000 Mora, Debris of Decarabian's City x2, Heavy Horn 8, Slime Condensate x5\n \
        **[✦✦✦---]**:15,000 Mora, Debris of Decarabian's City x4, Black Bronze Horn x4, Slime Secretions x4\n \
        **[✦✦✦✦--]**:20,000 Mora, Fragment of Decarabian's Epic x2, Black Bronze Horn x8, Slime Secretions x6\n \
        **[✦✦✦✦✦-]**:25,000 Mora, Fragment of Decarabian's Epic x4, Black Crystal Horn x6, Slime Concentrate x4\n \
        **[✦✦✦✦✦✦]**:30,000 Mora, Scattered Piece of Decarabian's Dream x3, Black Crystal Horn x12, Slime Concentrate x8", 'name':"Magic Guide"}
        return lst98
    elif name.lower() == "otherworldly story":
        lst99 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/1/11/Weapon_Otherworldly_Story.png/revision/latest/scale-to-width-down/256?cb=20201116034636", \
        'his':"นวนิยายแฟนตาซีง่าย ๆ ที่ไม่ได้มีคุณค่าอะไร พลังของมันที่ใช้เป็นสื่อเวท ก็คือความแฟนตาซีเพ้อฝัน ของมันนั่นเอง", \
        'type':"Catalyst", 'stat':["401", "39.0%", "Energy Recharge"], \
        'ascen':"**[✦-----]**:5,000 Mora, Fetters of the Dandelion Gladiator x2, Chaos Device x2, Damaged Mask x1\n \
        **[✦✦----]**:10,000 Mora, Chains of the Dandelion Gladiator x2, Chaos Device x8, Damaged Mask x5\n \
        **[✦✦✦---]**:15,000 Mora, Chains of the Dandelion Gladiator x4, Chaos Circuit x4, Stained Mask x4\n \
        **[✦✦✦✦--]**:20,000 Mora, Shackles of the Dandelion Gladiator x2, Chaos Circuit x8, Stained Mask x6\n \
        **[✦✦✦✦✦-]**:25,000 Mora, Shackles of the Dandelion Gladiator x4, Chaos Core x6, Ominous Mask x4\n \
        **[✦✦✦✦✦✦]**:30,000 Mora, Dream of the Dandelion Gladiator x3, Chaos Core x12, Ominous Mask x8", 'name':"Otherworldly Story"}
        return lst99
    elif name.lower() == "emerald orb":
        lst100 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/7/7c/Weapon_Emerald_Orb.png/revision/latest/scale-to-width-down/256?cb=20201120003056", \
        'his':"สื่อเวทย์สร้างจากหยกแข็งที่ สกัดจากเทือกเขาทางเหนื่อ ของ Liyue มันมีน้ำหนักที่เบาขนาดเล็ก และทนทาน", \
        'type':"Catalyst", 'stat':["448", "94%", "Elemental Mastery"], \
        'ascen':"**[✦-----]**:5,000 Mora, Luminous Sands from Guyun x2, Hunter's Sacrificial Knife x2, Treasure Hoarder Insignia x1\n \
        **[✦✦----]**:10,000 Mora, Lustrous Stone from Guyun x2, Hunter's Sacrificial Knife x8, Treasure Hoarder Insignia x5\n \
        **[✦✦✦---]**:15,000 Mora, Lustrous Stone from Guyun x4, Agent's Sacrificial Knife x4, Silver Raven Insignia x4\n \
        **[✦✦✦✦--]**:20,000 Mora, Relic from Guyun x2, Agent's Sacrificial Knife x8, Silver Raven Insignia x6\n \
        **[✦✦✦✦✦-]**:25,000 Mora, Relic from Guyun x4, Inspector's Sacrificial Knife x6, Golden Raven Insignia x4\n \
        **[✦✦✦✦✦✦]**:30,000 Mora, Divine Body from Guyun x3, Inspector's Sacrificial Knife x12, Golden Raven Insignia x8", 'name':"Emerald Orb"}
        return lst100
    elif name.lower() == "thrilling tales of dragon slayers":
        lst101 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/1/19/Weapon_Thrilling_Tales_of_Dragon_Slayers.png/revision/latest/scale-to-width-down/256?cb=20201119201736", \
        'his':"นวนิยายที่เกี่ยวกับเรื่องราวของ ฮีโร่ 5 คนที่กำลังจะเดินทางไป ล่ามังกร เขียนไว้อย่างหลวม ๆ และมีโครงเรื่องเพียงน้อยนิด แต่สิ่งสำคัญของมันคือ การสอนผู้คนให้เรียนรู้จากความผิดพลาด", \
        'type':"Catalyst", 'stat':["401", "35.2%", "HP"], \
        'ascen':"**[✦-----]**:5,000 Mora, Boreal Wolf's Milk Tooth x2, Dead Ley Line Branch x2, Divining Scroll x1\n \
        **[✦✦----]**:10,000 Mora, Boreal Wolf's Cracked Tooth x2, Dead Ley Line Branch x8, Divining Scroll x5\n \
        **[✦✦✦---]**:15,000 Mora, Boreal Wolf's Cracked Tooth x4, Dead Ley Line Leaves x4, Sealed Scroll x4\n \
        **[✦✦✦✦--]**:20,000 Mora, Boreal Wolf's Broken Fang x2, Dead Ley Line Leaves x8, Sealed Scroll x6\n \
        **[✦✦✦✦✦-]**:25,000 Mora, Boreal Wolf's Broken Fang x4, Ley Line Sprout x6, Forbidden Curse Scroll x4\n \
        **[✦✦✦✦✦✦]**:30,000 Mora, Boreal Wolf's Nostalgia x3, Ley Line Sprout x12, Forbidden Curse Scroll x8", 'name':"Thrilling Tales of Dragon Slayers"}
        return lst101
    elif name.lower() == "twin nephrite":
        lst102 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/e/e3/Weapon_Twin_Nephrite.png/revision/latest/scale-to-width-down/256?cb=20201119201412", \
        'his':"จี้หยกที่นำเอาหยกทั่วไปสองชิ้นมาประกอบเข้าด้วยกัน", \
        'type':"Catalyst", 'stat':["448", "15.6%", "CRIT Rate"], \
        'ascen':"**[✦-----]**:5,000 Mora, Mist Veiled Lead Elixir x2, Mist Grass Pollen x2, Recruit's Insignia x1\n \
        **[✦✦----]**:10,000 Mora, Mist Veiled Mercury Elixir x2, Mist Grass Pollen x8, Recruit's Insignia x5\n \
        **[✦✦✦---]**:15,000 Mora, Mist Veiled Mercury Elixir x4, Mist Grass x4, Sergeant's Insignia x4\n \
        **[✦✦✦✦--]**:20,000 Mora, Mist Veiled Gold Elixir x2, Mist Grass x8, Sergeant's Insignia x6\n \
        **[✦✦✦✦✦-]**:25,000 Mora, Mist Veiled Gold Elixir x4, Mist Grass Wick x6, Lieutenant's Insignia x4\n \
        **[✦✦✦✦✦✦]**:30,000 Mora, Mist Veiled Primo Elixir x3, Mist Grass Wick x12, Lieutenant's Insignia x8", 'name':"Twin Nephrite"}
        return lst102
    elif name.lower() == "skyrider greatsword":
        lst103 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/6/6e/Weapon_Skyrider_Greatsword.png/revision/latest/scale-to-width-down/256?cb=20201116035158", \
        'his':"ดาบเหล็กกล้าที่ดูพึ่งพาได้ ครั้งหนึ่ง Skyrider ผู้โด่งดังในตำนานพยายามมันเพื่อทะยานสู่ฟ้า", \
        'type':"Claymore", 'stat':["401", "43.9%", "Physical DMG Bonus"], \
        'ascen':"**[✦-----]**:5,000 Mora, Grain of Aerosiderite x2, Fragile Bone Shard x2, Treasure Hoarder Insignia x1\n \
        **[✦✦----]**:10,000 Mora, Piece of Aerosiderite x2, Fragile Bone Shard x8, Treasure Hoarder Insignia x5\n \
        **[✦✦✦---]**:15,000 Mora, Piece of Aerosiderite x4, Sturdy Bone Shard x4, Silver Raven Insignia x4\n \
        **[✦✦✦✦--]**:20,000 Mora, Bit of Aerosiderite x2, Sturdy Bone Shard x8, Silver Raven Insignia x6\n \
        **[✦✦✦✦✦-]**:25,000 Mora, Bit of Aerosiderite x4, Fossilized Bone Shard x6, Golden Raven Insignia x4\n \
        **[✦✦✦✦✦✦]**:30,000 Mora, Chunk of Aerosiderite x3, Fossilized Bone Shard x12, Golden Raven Insignia x8", 'name':"Skyrider Greatsword"}
        return lst103
    elif name.lower() == "debate club":
        lst104 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/7/74/Weapon_Debate_Club.png/revision/latest/scale-to-width-down/256?cb=20201116033616", \
        'his':'กระบองที่ทำจากเหล็กกล้าชั้นดีนี่คือรากฐานของ "เหตุผลที่น่าเชื่อถือ"', \
        'type':"Claymore", 'stat':["401", "35.2%", "ATK"], \
        'ascen':"**[✦-----]**:5,000 Mora, Mist Veiled Lead Elixir x2, Mist Grass Pollen x2, Damaged Mask x1\n \
        **[✦✦----]**:10,000 Mora, Mist Veiled Mercury Elixir x2, Mist Grass Pollen x8, Damaged Mask x5\n \
        **[✦✦✦---]**:15,000 Mora, Mist Veiled Mercury Elixir x4, Mist Grass x4, Stained Mask x4\n \
        **[✦✦✦✦--]**:20,000 Mora, Mist Veiled Gold Elixir x2, Mist Grass x8, Stained Mask x6\n \
        **[✦✦✦✦✦-]**:25,000 Mora, Mist Veiled Gold Elixir x4, Mist Grass Wick x6, Ominous Mask x4\n \
        **[✦✦✦✦✦✦]**:30,000 Mora, Mist Veiled Primo Elixir x3, Mist Grass Wick x12, Ominous Mask x8", 'name':"Debate Club"}
        return lst104
    elif name.lower() == "bloodtainted greatsword":
        lst105 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/4/4a/Weapon_Bloodtainted_Greatsword.png/revision/latest/scale-to-width-down/256?cb=20201119233531", \
        'his':"ดาบเหล็กกล้าที่ว่ากันว่า ได้ผ่านการชุบเลือดมังกรมา ทำให้มันทนทานต่อความเสียหายแต่ก็ไม่ได้หมายความว่า ผู้ใช้ของมันจะทนทานเหมือน ตัวดาบเสมอไป", \
        'type':"Claymore", 'stat':["354", "187", "Elemental Mastery"], \
        'ascen':"**[✦-----]**:5,000 Mora, Boreal Wolf's Milk Tooth x2, Dead Ley Line Branch x2, Firm Arrowhead x1\n \
        **[✦✦----]**:10,000 Mora, Boreal Wolf's Cracked Tooth x2, Dead Ley Line Branch x8, Firm Arrowhead x5\n \
        **[✦✦✦---]**:15,000 Mora, Boreal Wolf's Cracked Tooth x4, Dead Ley Line Leaves x4, Sharp Arrowhead x4\n \
        **[✦✦✦✦--]**:20,000 Mora, Boreal Wolf's Broken Fang x2, Dead Ley Line Leaves x8, Sharp Arrowhead x6\n \
        **[✦✦✦✦✦-]**:25,000 Mora, Boreal Wolf's Broken Fang x4, Ley Line Sprout x6, Weathered Arrowhead x4\n \
        **[✦✦✦✦✦✦]**:30,000 Mora, Boreal Wolf's Nostalgia x3, Ley Line Sprout x12, Weathered Arrowhead x8", 'name':"Bloodtainted Greatsword"}
        return lst105
    elif name.lower() == "white iron greatsword":
        lst106 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/5/56/Weapon_White_Iron_Greatsword.png/revision/latest/scale-to-width-down/256?cb=20201119201015", \
        'his':"ดาบใหญ่ที่สร้างขึ้นด้วยเหล็กขาว เพิ่มความแข็งแกร่งเมื่อใช้มันตัดด้วยน้ำหนัก แม้ผู้ที่มีความแข็งแรงระดับทั่วไปก็สามารถใช้ได้ แต่พลังของมันก็ขึ้นอยู่กับระดับความแข็งแกร่งของผู้ใช้งาน", \
        'type':"Claymore", 'stat':["401", "43.9%", "DEF"], \
        'ascen':"**[✦-----]**:5,000 Mora, Fetters of the Dandelion Gladiator x2, Chaos Device x2, Slime Condensate x1\n \
        **[✦✦----]**:10,000 Mora, Chains of the Dandelion Gladiator x2, Chaos Device x8, Slime Condensate x5\n \
        **[✦✦✦---]**:15,000 Mora, Chains of the Dandelion Gladiator x4, Chaos Circuit x4, Slime Secretions x4\n \
        **[✦✦✦✦--]**:20,000 Mora, Shackles of the Dandelion Gladiator x2, Chaos Circuit x8, Slime Secretions x6\n \
        **[✦✦✦✦✦-]**:25,000 Mora, Shackles of the Dandelion Gladiator x4, Chaos Core x6, Slime Concentrate x4\n \
        **[✦✦✦✦✦✦]**:30,000 Mora, Dream of the Dandelion Gladiator x3, Chaos Core x12, Slime Concentrate x8", 'name':"White Iron Greatsword"}
        return lst106
    elif name.lower() == "ferrous shadow":
        lst107 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/e/e9/Weapon_Ferrous_Shadow.png/revision/latest/scale-to-width-down/256?cb=20201120003242", \
        'his':"ดาบที่จำลองจากดาบชื่อดังของ Arundolyn ราชสีห์แห่งแสง จงถือให้มั่นและซึมซับพลังแห่ง ฮีโร่ในตำนาน! ข้อควรจำ: การเพ้อฝันมากไปอาจเป็นอันตรายต่อชีวิต", \
        'type':"Claymore", 'stat':["401", "35.2%", "HP"], \
        'ascen':"**[✦-----]**:5,000 Mora, Tile of Decarabian's Tower x2, Heavy Horn x2, Whopperflower Nectar x1\n \
        **[✦✦----]**:10,000 Mora, Debris of Decarabian's City x2, Heavy Horn 8, Whopperflower Nectar x5\n \
        **[✦✦✦---]**:15,000 Mora, Debris of Decarabian's City x4, Black Bronze Horn x4, Shimmering Nectar x4\n \
        **[✦✦✦✦--]**:20,000 Mora, Fragment of Decarabian's Epic x2, Black Bronze Horn x8, Shimmering Nectar x6\n \
        **[✦✦✦✦✦-]**:25,000 Mora, Fragment of Decarabian's Epic x4, Black Crystal Horn x6, Energy Nectar x4\n \
        **[✦✦✦✦✦✦]**:30,000 Mora, Scattered Piece of Decarabian's Dream x3, Black Crystal Horn x12, Energy Nectar x8", 'name':"Ferrous Shadow"}
        return lst107
    elif name.lower() == "white tassel":
        lst108 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/1/1f/Weapon_White_Tassel.png/revision/latest/scale-to-width-down/256?cb=20201116035549", \
        'his':"มาตรฐานการสวมใส่ของ Millelith Soldier ตัวหอกแข็งแรง ปลายหอกทนทาน ช่างเป็นอาวุธที่มิอาจเทียบได้", \
        'type':"Polearm", 'stat':["401", "23.4%", "CRIT Rate"], \
        'ascen':"**[✦-----]**:5,000 Mora, Luminous Sands from Guyun x2, Hunter's Sacrificial Knife x2, Recruit's Insignia x1\n \
        **[✦✦----]**:10,000 Mora, Lustrous Stone from Guyun x2, Hunter's Sacrificial Knife x8, Recruit's Insignia x5\n \
        **[✦✦✦---]**:15,000 Mora, Lustrous Stone from Guyun x4, Agent's Sacrificial Knife x4, Sergeant's Insignia x4\n \
        **[✦✦✦✦--]**:20,000 Mora, Relic from Guyun x2, Agent's Sacrificial Knife x8, Sergeant's Insignia x6\n \
        **[✦✦✦✦✦-]**:25,000 Mora, Relic from Guyun x4, Inspector's Sacrificial Knife x6, Lieutenant's Insignia x4\n \
        **[✦✦✦✦✦✦]**:30,000 Mora, Divine Body from Guyun x3, Inspector's Sacrificial Knife x12, Lieutenant's Insignia x8", 'name':"White Tassel"}
        return lst108
    elif name.lower() == "black tassel":
        lst109 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/4/43/Weapon_Black_Tassel.png/revision/latest/scale-to-width-down/256?cb=20201116033134", \
        'his':"พู่สีดำที่ช่วยแก้ปัญหาของทวนที่มีพู่สีขาวซึ่งเลอะง่ายได้อย่างดี", \
        'type':"Polearm", 'stat':["354", "46.9%", "HP"], \
        'ascen':"**[✦-----]**:5,000 Mora, Grain of Aerosiderite x2, Fragile Bone Shard x2, Firm Arrowhead x1\n \
        **[✦✦----]**:10,000 Mora, Piece of Aerosiderite x2, Fragile Bone Shard x8, Firm Arrowhead x5\n \
        **[✦✦✦---]**:15,000 Mora, Piece of Aerosiderite x4, Sturdy Bone Shard x4, Sharp Arrowhead x4\n \
        **[✦✦✦✦--]**:20,000 Mora, Bit of Aerosiderite x2, Sturdy Bone Shard x8, Sharp Arrowhead x6\n \
        **[✦✦✦✦✦-]**:25,000 Mora, Bit of Aerosiderite x4, Fossilized Bone Shard x6, Weathered Arrowhead x4\n \
        **[✦✦✦✦✦✦]**:30,000 Mora, Chunk of Aerosiderite x3, Fossilized Bone Shard x12, Weathered Arrowhead x8", 'name':"Black Tassel"}
        return lst109
    elif name.lower() == "halberd":
        lst110 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/4/41/Weapon_Halberd.png/revision/latest/scale-to-width-down/256?cb=20201116033956", \
        'his':"หอกที่มีใบมีดคล้ายขวานติดตั้งอยู่ที่ปลายหอก สามารถสร้างความเสียหายได้ประมาณหนึ่ง เป็นอาวุธที่ทหาร Millelith ชื่นชอบ", \
        'type':"Polearm", 'stat':["448", "23.8%", "ATK"], \
        'ascen':"**[✦-----]**:5,000 Mora, Mist Veiled Lead Elixir x2, Mist Grass Pollen x2, Whopperflower Nectar x1\n \
        **[✦✦----]**:10,000 Mora, Mist Veiled Mercury Elixir x2, Mist Grass Pollen x8, Whopperflower Nectar x5\n \
        **[✦✦✦---]**:15,000 Mora, Mist Veiled Mercury Elixir x4, Mist Grass x4, Shimmering Nectar x4\n \
        **[✦✦✦✦--]**:20,000 Mora, Mist Veiled Gold Elixir x2, Mist Grass x8, Shimmering Nectar x6\n \
        **[✦✦✦✦✦-]**:25,000 Mora, Mist Veiled Gold Elixir x4, Mist Grass Wick x6, Energy Nectar x4\n \
        **[✦✦✦✦✦✦]**:30,000 Mora, Mist Veiled Primo Elixir x3, Mist Grass Wick x12, Energy Nectar x8", 'name':"Halberd"}
        return lst110
    elif name.lower() == "harbinger of dawn":
        lst111 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/2/23/Weapon_Harbinger_of_Dawn.png/revision/latest/scale-to-width-down/256?cb=20201119233056", \
        'his':'ดาบที่ครั้งหนึ่งเคยส่องประกายดั่งแสงตะวัน ผู้กวัดแกว่งดาบเล่มนี้จะได้รับพรและบัฟ "ความรู้สึกดี" วัสดุที่สะท้อนแสงอยู่บนใบดาบนั้น ได้หมดแสงของมันไปนานแล้ว', \
        'type':"Sword", 'stat':["401", "46.9%", "CRIT DMG"], \
        'ascen':"**[✦-----]**:5,000 Mora, Boreal Wolf's Milk Tooth x2, Dead Ley Line Branch x2, Slime Condensate x1\n \
        **[✦✦----]**:10,000 Mora, Boreal Wolf's Cracked Tooth x2, Dead Ley Line Branch x8, Slime Condensate x5\n \
        **[✦✦✦---]**:15,000 Mora, Boreal Wolf's Cracked Tooth x4, Dead Ley Line Leaves x4, Slime Secretions x4\n \
        **[✦✦✦✦--]**:20,000 Mora, Boreal Wolf's Broken Fang x2, Dead Ley Line Leaves x8, Slime Secretions x6\n \
        **[✦✦✦✦✦-]**:25,000 Mora, Boreal Wolf's Broken Fang x4, Ley Line Sprout x6, Slime Concentrate x4\n \
        **[✦✦✦✦✦✦]**:30,000 Mora, Boreal Wolf's Nostalgia x3, Ley Line Sprout x12, Slime Concentrate x8", 'name':"Harbinger of Dawn"}
        return lst111
    elif name.lower() == "fillet blade":
        lst112 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/f/f7/Weapon_Fillet_Blade.png/revision/latest/scale-to-width-down/256?cb=20201116033941", \
        'his':"มีดแล่เนื้อที่คมกริบ ใบมีดยาว บาง และคมมาก", \
        'type':"Sword", 'stat':["401", "35.2%", "ATK"], \
        'ascen':"**[✦-----]**:5,000 Mora, Mist Veiled Lead Elixir x2, Mist Grass Pollen x2, Treasure Hoarder Insignia x1\n \
        **[✦✦----]**:10,000 Mora, Mist Veiled Mercury Elixir x2, Mist Grass Pollen x8, Treasure Hoarder Insignia x5\n \
        **[✦✦✦---]**:15,000 Mora, Mist Veiled Mercury Elixir x4, Mist Grass x4, Silver Raven Insignia x4\n \
        **[✦✦✦✦--]**:20,000 Mora, Mist Veiled Gold Elixir x2, Mist Grass x8, Silver Raven Insignia x6\n \
        **[✦✦✦✦✦-]**:25,000 Mora, Mist Veiled Gold Elixir x4, Mist Grass Wick x6, Golden Raven Insignia x4\n \
        **[✦✦✦✦✦✦]**:30,000 Mora, Mist Veiled Primo Elixir x3, Mist Grass Wick x12, Golden Raven Insignia x8", 'name':"Fillet Blade"}
        return lst112
    elif name.lower() == "skyrider sword":
        lst113 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/3/34/Weapon_Skyrider_Sword.png/revision/latest/scale-to-width-down/256?cb=20201116035206", \
        'his':"ดาบเหล็กกล้าที่พึ่งพาได้ เคยมีบางคนพยายามขี่มันเพราะชื่อของมันด้วย", \
        'type':"Sword", 'stat':["354", "51.7%", "Energy Recharge"], \
        'ascen':"**[✦-----]**:5,000 Mora, Grain of Aerosiderite x2, Fragile Bone Shard x2, Recruit's Insignia x1\n \
        **[✦✦----]**:10,000 Mora, Piece of Aerosiderite x2, Fragile Bone Shard x8, Recruit's Insignia x5\n \
        **[✦✦✦---]**:15,000 Mora, Piece of Aerosiderite x4, Sturdy Bone Shard x4, Sergeant's Insignia x4\n \
        **[✦✦✦✦--]**:20,000 Mora, Bit of Aerosiderite x2, Sturdy Bone Shard x8, Sergeant's Insignia x6\n \
        **[✦✦✦✦✦-]**:25,000 Mora, Bit of Aerosiderite x4, Fossilized Bone Shard x6, Lieutenant's Insignia x4\n \
        **[✦✦✦✦✦✦]**:30,000 Mora, Chunk of Aerosiderite x3, Fossilized Bone Shard x12, Lieutenant's Insignia x8", 'name':"Skyrider Sword"}
        return lst113
    elif name.lower() == "dark iron sword":
        lst114 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/3/3a/Weapon_Dark_Iron_Sword.png/revision/latest/scale-to-width-down/256?cb=20201119235556", \
        'his':"ที่จริงแล้วมันก็เป็นแค่ดาบเหล็กที่สีเข้มเท่านั้นเอง", \
        'type':"Sword", 'stat':["401", "141", "Elemental Mastery"], \
        'ascen':"**[✦-----]**:5,000 Mora, Luminous Sands from Guyun x2, Hunter's Sacrificial Knife x2, Damaged Mask x1\n \
        **[✦✦----]**:10,000 Mora, Lustrous Stone from Guyun x2, Hunter's Sacrificial Knife x8, Damaged Mask x5\n \
        **[✦✦✦---]**:15,000 Mora, Lustrous Stone from Guyun x4, Agent's Sacrificial Knife x4, Stained Mask x4\n \
        **[✦✦✦✦--]**:20,000 Mora, Relic from Guyun x2, Agent's Sacrificial Knife x8, Stained Mask x6\n \
        **[✦✦✦✦✦-]**:25,000 Mora, Relic from Guyun x4, Inspector's Sacrificial Knife x6, Ominous Mask x4\n \
        **[✦✦✦✦✦✦]**:30,000 Mora, Divine Body from Guyun x3, Inspector's Sacrificial Knife x12, Ominous Mask x8", 'name':"Dark Iron Sword"}
        return lst114
    elif name.lower() == "cool steel":
        lst115 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/9/9c/Weapon_Cool_Steel.png/revision/latest/scale-to-width-down/256?cb=20201119233444", \
        'his':"อาวุธที่สร้างขึ้นจากเหล็กกล้าดูพึ่งพาได้ เป็นเครื่องพิสูจน์ถึงการผจญภัยอันยิ่งใหญ่ของเจ้าของเก่าของมัน", \
        'type':"Sword", 'stat':["401", "35.2%", "ATK"], \
        'ascen':"**[✦-----]**:5,000 Mora, Tile of Decarabian's Tower x2, Heavy Horn x2, Firm Arrowhead x1\n \
        **[✦✦----]**:10,000 Mora, Debris of Decarabian's City x2, Heavy Horn 8, Firm Arrowhead x5\n \
        **[✦✦✦---]**:15,000 Mora, Debris of Decarabian's City x4, Black Bronze Horn x4, Sharp Arrowhead x4\n \
        **[✦✦✦✦--]**:20,000 Mora, Fragment of Decarabian's Epic x2, Black Bronze Horn x8, Sharp Arrowhead x6\n \
        **[✦✦✦✦✦-]**:25,000 Mora, Fragment of Decarabian's Epic x4, Black Crystal Horn x6, Weathered Arrowhead x4\n \
        **[✦✦✦✦✦✦]**:30,000 Mora, Scattered Piece of Decarabian's Dream x3, Black Crystal Horn x12, Weathered Arrowhead x8", 'name':"Cool Steel"}
        return lst115
    elif name.lower() == "traveler's handy sword":
        lst116 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/c/c9/Weapon_Traveler%27s_Handy_Sword.png/revision/latest/scale-to-width-down/256?cb=20201116035456", \
        'his':"ดาบเหล็กกล้าที่มีกรรไกร, แว่นขยาย, ที่จุดไฟ และอื่น ๆ เก็บไว้ในฝักดาบ", \
        'type':"Sword", 'stat':["448", "27.5%", "DEF"], \
        'ascen':"**[✦-----]**:5,000 Mora, Fetters of the Dandelion Gladiator x2, Chaos Device x2, Divining Scroll x1\n \
        **[✦✦----]**:10,000 Mora, Chains of the Dandelion Gladiator x2, Chaos Device x8, Divining Scroll x5\n \
        **[✦✦✦---]**:15,000 Mora, Chains of the Dandelion Gladiator x4, Chaos Circuit x4, Sealed Scroll x4\n \
        **[✦✦✦✦--]**:20,000 Mora, Shackles of the Dandelion Gladiator x2, Chaos Circuit x8, Sealed Scroll x6\n \
        **[✦✦✦✦✦-]**:25,000 Mora, Shackles of the Dandelion Gladiator x4, Chaos Core x6, Forbidden Curse Scroll x4\n \
        **[✦✦✦✦✦✦]**:30,000 Mora, Dream of the Dandelion Gladiator x3, Chaos Core x12, Forbidden Curse Scroll x8", 'name':"Traveler's Handy Sword"}
        return lst116
    elif name.lower() == "seasoned hunter's bow":
        lst117 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/8/82/Weapon_Seasoned_Hunter%27s_Bow.png/revision/latest/scale-to-width-down/256?cb=20201116035113", \
        'his':"คันธนูที่สร้างขึ้นอย่างประณีตด้วยเวลา และดูแลรักษาด้วยมือ ให้ความรู้สึกดั่งเป็นส่วนหนึ่งของแขนของนักธนูเอง", \
        'type':"Bow", 'stat':["243", "-", "None"], \
        'ascen':"**[✦-----]**:5,000 Mora, Boreal Wolf's Milk Tooth x1, Dead Ley Line Branch x1, Treasure Hoarder Insignia x1\n \
        **[✦✦----]**:5,000 Mora, Boreal Wolf's Cracked Tooth x1, Dead Ley Line Branch x5, Treasure Hoarder Insignia x4\n \
        **[✦✦✦---]**:10,000 Mora, Boreal Wolf's Cracked Tooth x3, Dead Ley Line Leaves x3, Silver Raven Insignia x3\n \
        **[✦✦✦✦--]**:15,000 Mora, Boreal Wolf's Broken Fang x1, Dead Ley Line Leaves x5, Silver Raven Insignia x4", 'name':"Seasoned Hunter's Bow"}
        return lst117
    elif name.lower() == "hunter's bow":
        lst118 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/4/44/Weapon_Hunter%27s_Bow.png/revision/latest/scale-to-width-down/256?cb=20201116034023", \
        'his':"เสียงดนตรีของนักล่ามีอยู่เพียง สองเสียง เสียงดีดของคันธนู และเสียงแหวกอากาศ ของลูกธนู", \
        'type':"Bow", 'stat':["185", "-", "None"], \
        'ascen':"**[✦-----]**:0 Mora, Boreal Wolf's Milk Tooth x1, Dead Ley Line Branch x1, Treasure Hoarder Insignia x1\n \
        **[✦✦----]**:5,000 Mora, Boreal Wolf's Cracked Tooth x1, Dead Ley Line Branch x4, Treasure Hoarder Insignia x2\n \
        **[✦✦✦---]**:5,000 Mora, Boreal Wolf's Cracked Tooth x2, Dead Ley Line Leaves x2, Silver Raven Insignia x2\n \
        **[✦✦✦✦--]**:10,000 Mora, Boreal Wolf's Broken Fang x1, Dead Ley Line Leaves x4, Silver Raven Insignia x3", 'name':"Hunter's Bow"}
        return lst118
    elif name.lower() == "pocket grimoire":
        lst119 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/1/16/Weapon_Pocket_Grimoire.png/revision/latest/scale-to-width-down/256?cb=20201119204545", \
        'his':"หนังสือที่รวบรวมข้อมูลที่เฉพาะเจาะจงซึ่งเหลือเพียงคู่มือเวทมนตร์สำหรับอ้างอิงที่มุ่งเน้นไปที่เนื้อหาหลักของการสอบเท่านั้น", \
        'type':"Catalyst", 'stat':["243", "-", "None"], \
        'ascen':"**[✦-----]**:5,000 Mora, Tile of Decarabian's Tower x1, Heavy Horn x1, Damaged Mask x1\n \
        **[✦✦----]**:5,000 Mora, Debris of Decarabian's City x1, Heavy Horn x5, Damaged Mask x4\n \
        **[✦✦✦---]**:10,000 Mora, Debris of Decarabian's City x3, Black Bronze Horn x3, Stained Mask x3\n \
        **[✦✦✦✦--]**:15,000 Mora, Fragment of Decarabian's Epic x1, Black Bronze Horn  x5, Stained Mask x4", 'name':"Pocket Grimoire"}
        return lst119
    elif name.lower() == "apprentice's notes":
        lst120 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/c/cf/Weapon_Apprentice%27s_Notes.png/revision/latest/scale-to-width-down/256?cb=20201119233859", \
        'his':"ข้อความที่ทิ้งไว้โดย ยอดนักเรียนคนหนึ่ง ซึ่งเป็นรายชื่อเวทมนตร์ ที่มีประโยชน์เขียนด้วยลายมือ ที่สวยงาม", \
        'type':"Catalyst", 'stat':["185", "-", "None"], \
        'ascen':"**[✦-----]**:0 Mora, Tile of Decarabian's Tower x1, Heavy Horn x1, Damaged Mask x1\n \
        **[✦✦----]**:5,000 Mora, Debris of Decarabian's City x1, Heavy Horn x4, Damaged Mask x2\n \
        **[✦✦✦---]**:5,000 Mora, Debris of Decarabian's City x2, Black Bronze Horn x2, Stained Mask x2\n \
        **[✦✦✦✦--]**:10,000 Mora, Fragment of Decarabian's Epic x1, Black Bronze Horn  x4, Stained Mask x3", 'name':"Apprentice's Notes"}
        return lst120
    elif name.lower() == "old merc's pal":
        lst121 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/0/0b/Weapon_Old_Merc%27s_Pal.png/revision/latest/scale-to-width-down/256?cb=20201116034249", \
        'his':"ดาบใหญ่ที่ผ่านการใช้งานมาอย่างยาวนาน ทั้งวันที่ดีและร้ายปะปนเป็นแรมปี", \
        'type':"Claymore", 'stat':["243", "-", "None"], \
        'ascen':"**[✦-----]**:5,000 Mora, Boreal Wolf's Milk Tooth x1, Dead Ley Line Branch x1, Treasure Hoarder Insignia x1\n \
        **[✦✦----]**:5,000 Mora, Boreal Wolf's Cracked Tooth x1, Dead Ley Line Branch x5, Treasure Hoarder Insignia x4\n \
        **[✦✦✦---]**:10,000 Mora, Boreal Wolf's Cracked Tooth x3, Dead Ley Line Leaves x3, Silver Raven Insignia x3\n \
        **[✦✦✦✦--]**:15,000 Mora, Boreal Wolf's Broken Fang x1, Dead Ley Line Leaves x5, Silver Raven Insignia x4", 'name':"Old Merc's Pal"}
        return lst121
    elif name.lower() == "waster greatsword":
        lst122 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/4/4c/Weapon_Waster_Greatsword.png/revision/latest/scale-to-width-down/256?cb=20201120001015", \
        'his':"แผ่นเหล็กที่ทนทานซึ่งอาจ ทำลายได้แม้กระทั่งภูเขา หากมีแรงมุ่งมั่นที่มากพอ", \
        'type':"Claymore", 'stat':["185", "-", "None"], \
        'ascen':"**[✦-----]**:0 Mora, Boreal Wolf's Milk Tooth x1, Dead Ley Line Branch x1, Treasure Hoarder Insignia x1\n \
        **[✦✦----]**:5,000 Mora, Boreal Wolf's Cracked Tooth x1, Dead Ley Line Branch x4, Treasure Hoarder Insignia x2\n \
        **[✦✦✦---]**:5,000 Mora, Boreal Wolf's Cracked Tooth x2, Dead Ley Line Leaves x2, Silver Raven Insignia x2\n \
        **[✦✦✦✦--]**:10,000 Mora, Boreal Wolf's Broken Fang x1, Dead Ley Line Leaves x4, Silver Raven Insignia x3", 'name':"Waster Greatsword"}
        return lst122
    elif name.lower() == "iron point":
        lst123 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/2/25/Weapon_Iron_Point.png/revision/latest/scale-to-width-down/256?cb=20201116034039", \
        'his':"อาวุธปลายแหลมด้านเดียว เป็นอาวุธที่สมดุลและเป็นที่นิยมในหมู่นักเดินทาง", \
        'type':"Polearm", 'stat':["243", "-", "None"], \
        'ascen':"**[✦-----]**:5,000 Mora, Fetters of the Dandelion Gladiator x1, Chaos Device x1, Divining Scroll x1\n \
        **[✦✦----]**:5,000 Mora, Chains of the Dandelion Gladiator x1, Chaos Device x5, Divining Scroll x4\n \
        **[✦✦✦---]**:10,000 Mora, Chains of the Dandelion Gladiator x3, Chaos Circuit x3, Sealed Scroll x3\n \
        **[✦✦✦✦--]**:15,000 Mora, Shackles of the Dandelion Gladiator x1, Chaos Circuit x5, Sealed Scroll x4", 'name':"Iron Point"}
        return lst123
    elif name.lower() == "beginner's protector":
        lst124 = {'thum':"https://static.wikia.nocookie.net/genshin-impact/images/f/fc/Weapon_Beginner%27s_Protector.png/revision/latest/scale-to-width-down/256?cb=20210713085834&path-prefix=th", \
        'his':"หอกที่เหมือนเสาธง ใช้งานได้กับหลายสถานการณ์ รู้สึกประทับใจทุกครั้งเมื่อได้เหวี่ยงมัน", \
        'type':"Polearm", 'stat':["185", "-", "None"], \
        'ascen':"**[✦-----]**:0 Mora, Fetters of the Dandelion Gladiator x1, Chaos Device x1, Divining Scroll x1\n \
        **[✦✦----]**:5,000 Mora, Chains of the Dandelion Gladiator x1, Chaos Device x4, Divining Scroll x2\n \
        **[✦✦✦---]**:5,000 Mora, Chains of the Dandelion Gladiator x2, Chaos Circuit x2, Sealed Scroll x2\n \
        **[✦✦✦✦--]**:10,000 Mora, Shackles of the Dandelion Gladiator x1, Chaos Circuit x4, Sealed Scroll x3", 'name':"Beginner's Protector"}
        return lst124
    elif name.lower() == "silver sword":
        lst125 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/3/32/Weapon_Silver_Sword.png/revision/latest/scale-to-width-down/256?cb=20201116035150", \
        'his':"ดาบที่ใช้ไล่ปีศาจร้าย ทุกคนต่างรู้ดีว่ามันท่มาจากอัลลอย ไม่ใช่เงินแท้ ๆ สักหน่อย", \
        'type':"Sword", 'stat':["243", "-", "None"], \
        'ascen':"**[✦-----]**:5,000 Mora, Tile of Decarabian's Tower x1, Heavy Horn x1, Firm Arrowhead x1\n \
        **[✦✦----]**:5,000 Mora, Debris of Decarabian's City x1, Heavy Horn x5, Firm Arrowhead x4\n \
        **[✦✦✦---]**:10,000 Mora, Debris of Decarabian's City x3, Black Bronze Horn x3, Sharp Arrowhead x3\n \
        **[✦✦✦✦--]**:25,000 Mora, Fragment of Decarabian's Epic x1, Black Bronze Horn x5, Sharp Arrowhead x4", 'name':"Silver Sword"}
        return lst125
    elif name.lower() == "dull blade":
        lst126 = {'thum':"https://static.wikia.nocookie.net/gensin-impact/images/2/2f/Weapon_Dull_Blade.png/revision/latest/scale-to-width-down/256?cb=20201119235841", \
        'his':"ฝันในวัยเยาว์กับการผจญภัยอันน่าตื่นเต้น หากมันยังไม่พอ ก็เพิ่มความกล้าเข้าไปด้วยสิ", \
        'type':"Sword", 'stat':["185", "-", "None"], \
        'ascen':"**[✦-----]**:0 Mora, Tile of Decarabian's Tower x1, Heavy Horn x1, Firm Arrowhead x1\n \
        **[✦✦----]**:5,000 Mora, Debris of Decarabian's City x1, Heavy Horn x4, Firm Arrowhead x2\n \
        **[✦✦✦---]**:5,000 Mora, Debris of Decarabian's City x2, Black Bronze Horn x2, Sharp Arrowhead x2\n \
        **[✦✦✦✦--]**:10,000 Mora, Fragment of Decarabian's Epic x1, Black Bronze Horn x4, Sharp Arrowhead x3", 'name':"Dull Blade"}
        return lst126
    
                  