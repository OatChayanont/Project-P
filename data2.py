def weapon_info_list(name):
    if name.lower() == "polar star":
        lst = ["https://static.wikia.nocookie.net/gensin-impact/images/4/44/Weapon_Polar_Star.png/revision/latest/scale-to-width-down/256?cb=20211013042349", \
        "ธนูไร้มลทินที่แหลมคม ราวกับแท่งน้ำแข็งในฤดูหนาวที่แสนยาวนาน", "Bow", ["608", "33.1%", "CRIT Rate"], \
        "**[✦-----]**:10,000 Mora, Mask of the Wicked Lieutenant x5, Concealed Claw x5, Spectral Husk x3\n \
        **[✦✦----]**:20,000 Mora, Mask of the Tiger's Bite x5, Concealed Claw x18, Spectral Husk x12\n \
        **[✦✦✦---]**:30,000 Mora, Mask of the Tiger's Bite x9, Concealed Unguis x9, Spectral Heart x9\n \
        **[✦✦✦✦--]**:45,000 Mora, Mask of the One-Horned x5, Concealed Unguis x18, Spectral Heart x14\n \
        **[✦✦✦✦✦-]**:55,000 Mora, Mask of the One-Horned x9, Concealed Talon x14, Spectral Nucleus x9\n \
        **[✦✦✦✦✦✦]**:65,000 Mora, Mask of the Kijin x6, Concealed Talon x27, Spectral Nucleus x18", "Polar Star"]
        return lst
    elif name.lower() == "thundering pulse":
        lst2 = ["https://static.wikia.nocookie.net/gensin-impact/images/7/77/Weapon_Thundering_Pulse.png/revision/latest/scale-to-width-down/256?cb=20210811094805", \
        "A longbow that was a gift from the Shogun. Eternal lightning crackles all around it.", "Bow", ["608", "66.2%", "CRIT DMG"], \
        "**[✦-----]**:10,000 Mora, Narukami's Wisdom x5, Dismal Prism x5, Firm Arrowhead x3\n \
        **[✦✦----]**:20,000 Mora, Narukami's Joy x5, Dismal Prism x18, Firm Arrowhead x12\n \
        **[✦✦✦---]**:30,000 Mora, Narukami's Joy x9, Crystal Prism x9, Sharp Arrowhead x9\n \
        **[✦✦✦✦--]**:45,000 Mora, Narukami's Affection x5, Crystal Prism x18, Sharp Arrowhead x14\n \
        **[✦✦✦✦✦-]**:55,000 Mora, Narukami's Affection x9, Polarizing Prism x14, Weathered Arrowhead x9\n \
        **[✦✦✦✦✦✦]**:65,000 Mora, Narukami's Valor x6, Polarizing Prism x27, Weathered Arrowhead x18", "Thundering Pulse"]
        return lst2
    elif name.lower() == "elegy for the end":
        lst3 = ["https://static.wikia.nocookie.net/gensin-impact/images/a/a5/Weapon_Elegy_for_the_End.png/revision/latest/scale-to-width-down/256?cb=20210317075424", \
        "A bow as lovely as any bard's lyre, its arrows pierce the heart like a lamenting sigh.", "Bow", ["608", "55.1%", "Energy Recharge"], \
        "**[✦-----]**:10,000 Mora, Boreal Wolf's Milk Tooth x5, Heavy Horn x5, Recruit's Insignia x3\n \
        **[✦✦----]**:20,000 Mora, Boreal Wolf's Cracked Tooth x5, Heavy Horn x18, Recruit's Insignia x12\n \
        **[✦✦✦---]**:30,000 Mora, Boreal Wolf's Cracked Tooth x9, Black Bronze Horn x9, Sergeant's Insignia x9\n \
        **[✦✦✦✦--]**:45,000 Mora, Boreal Wolf's Broken Fang x5, Black Bronze Horn x18, Sergeant's Insignia x14\n \
        **[✦✦✦✦✦-]**:55,000 Mora, Boreal Wolf's Broken Fang x9, Black Crystal Horn x14, Black Crystal Horn x9\n \
        **[✦✦✦✦✦✦]**:65,000 Mora, Boreal Wolf's Nostalgia x6, Black Crystal Horn x27, Black Crystal Horn x18", "Elegy for the End"]
        return lst3
    elif name.lower() == "skyward harp":
        lst4 = ["https://static.wikia.nocookie.net/gensin-impact/images/1/19/Weapon_Skyward_Harp.png/revision/latest/scale-to-width-down/256?cb=20201116035246", \
        "A greatbow that symbolizes Dvalin's affiliation with the Anemo Archon. The sound of the bow firing is music to the Anemo Archon's ears. It contains the power of the sky and wind within.", 
        "Bow", ["674", "22.1%", "CRIT Rate"], \
        "**[✦-----]**:10,000 Mora, Boreal Wolf's Milk Tooth x5, Dead Ley Line Branch x5, Firm Arrowhead x3\n \
        **[✦✦----]**:20,000 Mora, Boreal Wolf's Cracked Tooth x5, Dead Ley Line Branch x18, Firm Arrowhead x12\n \
        **[✦✦✦---]**:30,000 Mora, Boreal Wolf's Cracked Tooth x9, Dead Ley Line Leaves x9, Sharp Arrowhead x9\n \
        **[✦✦✦✦--]**:45,000 Mora, Boreal Wolf's Broken Fang x5, Dead Ley Line Leaves x18, Sharp Arrowhead x14\n \
        **[✦✦✦✦✦-]**:55,000 Mora, Boreal Wolf's Broken Fang x9, Ley Line Sprout x14, Weathered Arrowhead x9\n \
        **[✦✦✦✦✦✦]**:65,000 Mora, Boreal Wolf's Nostalgia x6, Ley Line Sprout x27, Weathered Arrowhead x18", "Skyward Harp"]
        return lst4
    elif name.lower() == "amos' bow":
        lst5 = ["https://static.wikia.nocookie.net/gensin-impact/images/d/de/Weapon_Amos%27_Bow.png/revision/latest/scale-to-width-down/256?cb=20201120010513", \
        "An extremely ancient bow that has retained its power despite its original master being long gone. It draws power from everyone and everything in the world, and the further away you are from that which your heart desires, the more powerful it is.", \
        "Bow", ["608", "49.6%", "ATK"], \
        "**[✦-----]**:10,000 Mora, Fetters of the Dandelion Gladiator x5, Chaos Device x5, Slime Condensate x3\n \
        **[✦✦----]**:20,000 Mora, Chains of the Dandelion Gladiator x5, Chaos Device x18, Slime Condensate x12\n \
        **[✦✦✦---]**:30,000 Mora, Chains of the Dandelion Gladiator x9, Chaos Circuit x9, Slime Secretions x9\n \
        **[✦✦✦✦--]**:45,000 Mora, Shackles of the Dandelion Gladiator x5, Chaos Circuit x18, Slime Secretions x14\n \
        **[✦✦✦✦✦-]**:55,000 Mora, Shackles of the Dandelion Gladiator x9, Chaos Core x14, Slime Concentrate x9\n \
        **[✦✦✦✦✦✦]**:65,000 Mora, Dream of the Dandelion Gladiator x6, Chaos Core x27, Slime Concentrate x18", "Amos' Bow"]
        return lst5
    elif name.lower() == "lost prayer to the sacred winds":
        lst6 = ["https://static.wikia.nocookie.net/gensin-impact/images/9/98/Weapon_Lost_Prayer_to_the_Sacred_Winds.png/revision/latest/scale-to-width-down/256?cb=20201116034132", \
        "An educational tome written by anonymous early inhabitants who worshiped the wind. It has been blessed by the wind for its faithfulness and influence over the millennia.", \
        "Catalyst", ["608", "33.1%", "CRIT Rate"], \
        "**[✦-----]**:10,000 Mora, Fetters of the Dandelion Gladiator x5, Chaos Device x5, Slime Condensate x3\n \
        **[✦✦----]**:20,000 Mora, Chains of the Dandelion Gladiator x5, Chaos Device x18, Slime Condensate x12\n \
        **[✦✦✦---]**:30,000 Mora, Chains of the Dandelion Gladiator x9, Chaos Circuit x9, Slime Secretions x9\n \
        **[✦✦✦✦--]**:45,000 Mora, Shackles of the Dandelion Gladiator x5, Chaos Circuit x18, Slime Secretions x14\n \
        **[✦✦✦✦✦-]**:55,000 Mora, Shackles of the Dandelion Gladiator x9, Chaos Core x14, Slime Concentrate x9\n \
        **[✦✦✦✦✦✦]**:65,000 Mora, Dream of the Dandelion Gladiator x6, Chaos Core x27, Slime Concentrate x18", "Lost Prayer to the Sacred Winds"]
        return lst6
    elif name.lower() == "skyward atlas":
        lst7 = ["https://static.wikia.nocookie.net/gensin-impact/images/3/33/Weapon_Skyward_Atlas.png/revision/latest/scale-to-width-down/256?cb=20201116035225", \
        "A cloud atlas symbolizing Dvalin and its former master, the Anemo Archon. It details the winds and clouds of the northern regions and contains the powers of the sky and wind.", \
        "Catalyst", ["674", "33.1%", "ATK"], \
        "**[✦-----]**:10,000 Mora, Boreal Wolf's Milk Tooth x5, Dead Ley Line Branch x5, Firm Arrowhead x3\n \
        **[✦✦----]**:20,000 Mora, Boreal Wolf's Cracked Tooth x5, Dead Ley Line Branch x18, Firm Arrowhead x12\n \
        **[✦✦✦---]**:30,000 Mora, Boreal Wolf's Cracked Tooth x9, Dead Ley Line Leaves x9, Sharp Arrowhead x9\n \
        **[✦✦✦✦--]**:45,000 Mora, Boreal Wolf's Broken Fang x5, Dead Ley Line Leaves x18, Sharp Arrowhead x14\n \
        **[✦✦✦✦✦-]**:55,000 Mora, Boreal Wolf's Broken Fang x9, Ley Line Sprout x14, Weathered Arrowhead x9\n \
        **[✦✦✦✦✦✦]**:65,000 Mora, Boreal Wolf's Nostalgia x6, Ley Line Sprout x27, Weathered Arrowhead x18", "Skyward Atlas"]
        return lst7
    elif name.lower() == "everlasting moonglow":
        lst8 = ["https://static.wikia.nocookie.net/gensin-impact/images/e/e1/Weapon_Everlasting_Moonglow.png/revision/latest/scale-to-width-down/256?cb=20210921104126", \
        "A string of lovely jasper from the deep sea. It shines with a pure radiance like that of the moon, and just as ever-distant.", \
        "Catalyst", ["608", "49.6%", "HP"], \
        "**[✦-----]**:10,000 Mora, Coral Branch of a Distant Sea x5, Dismal Prism x5, Spectral Husk x3\n \
        **[✦✦----]**:20,000 Mora, Jeweled Branch of a Distant Sea x5, Dismal Prism x18, Spectral Husk x12\n \
        **[✦✦✦---]**:30,000 Mora, Jeweled Branch of a Distant Sea x9, Crystal Prism x9, Spectral Heart x9\n \
        **[✦✦✦✦--]**:45,000 Mora, Jade Branch of a Distant Sea x5, Crystal Prism x18, Spectral Heart x14\n \
        **[✦✦✦✦✦-]**:55,000 Mora, Jade Branch of a Distant Sea x9, Polarizing Prism x14, Spectral Nucleus x9\n \
        **[✦✦✦✦✦✦]**:65,000 Mora, Golden Branch of a Distant Sea x6, Polarizing Prism x27, Spectral Nucleus x18", "Everlasting Moonglow"]
        return lst8
    elif name.lower() == "memory of dust":
        lst9 = ["https://static.wikia.nocookie.net/gensin-impact/images/c/ca/Weapon_Memory_of_Dust.png/revision/latest/scale-to-width-down/256?cb=20201119232148", \
        "A stone dumbbell containing distant memories. Its endless transformations reveal the power within.", \
        "Catalyst", ["608", "49.6%", "ATK"], \
        "**[✦-----]**:10,000 Mora, Grain of Aerosiderite x5, Fragile Bone Shard x5, Damaged Mask x3\n \
        **[✦✦----]**:20,000 Mora, Piece of Aerosiderite x5, Fragile Bone Shard x18, Damaged Mask x12\n \
        **[✦✦✦---]**:30,000 Mora, Piece of Aerosiderite x9, Sturdy Bone Shard x9, Stained Mask x9\n \
        **[✦✦✦✦--]**:45,000 Mora, Bit of Aerosiderite x5, Sturdy Bone Shard x18, Stained Mask x14\n \
        **[✦✦✦✦✦-]**:55,000 Mora, Bit of Aerosiderite x9, Fossilized Bone Shard x14, Ominous Mask x9\n \
        **[✦✦✦✦✦✦]**:65,000 Mora, Chunk of Aerosiderite x6, Fossilized Bone Shard x27, Ominous Mask x18", "Memory of Dust"]
        return lst9
    elif name.lower() == "wolf's gravestone":
        lst10 = ["https://static.wikia.nocookie.net/gensin-impact/images/4/4f/Weapon_Wolf%27s_Gravestone.png/revision/latest/scale-to-width-down/256?cb=20201116035623", \
        "A longsword used by the Wolf Knight. Originally just a heavy sheet of iron given to the knight by a blacksmith from the city, it became endowed with legendary power owing to his friendship with the wolves.", \
        "Claymore", ["608", "49.6%", "ATK"], \
        "**[✦-----]**:10,000 Mora, Fetters of the Dandelion Gladiator x5, Chaos Device x5, Divining Scroll x3\n \
        **[✦✦----]**:20,000 Mora, Chains of the Dandelion Gladiator x5, Chaos Device x18, Divining Scroll x12\n \
        **[✦✦✦---]**:30,000 Mora, Chains of the Dandelion Gladiator x9, Chaos Circuit x9, Sealed Scroll x9\n \
        **[✦✦✦✦--]**:45,000 Mora, Shackles of the Dandelion Gladiator x5, Chaos Circuit x18, Sealed Scroll x14\n \
        **[✦✦✦✦✦-]**:55,000 Mora, Shackles of the Dandelion Gladiator x9, Chaos Core x14, Forbidden Curse Scroll x9\n \
        **[✦✦✦✦✦✦]**:65,000 Mora, Dream of the Dandelion Gladiator x6, Chaos Core x27, Forbidden Curse Scroll x18", "Wolf's Gravestone"]
        return lst10
    elif name.lower() == "skyward pride":
        lst11 = ["https://static.wikia.nocookie.net/gensin-impact/images/0/0b/Weapon_Skyward_Pride.png/revision/latest/scale-to-width-down/256?cb=20201116035255", \
        "A claymore that symbolizes the pride of Dvalin soaring through the skies. When swung, it emits a deep hum as the full force of Dvalin's command of the sky and the wind is unleashed.", \
        "Claymore", ["674", "36.8%", "Energy Recharge"], \
        "**[✦-----]**:10,000 Mora, Boreal Wolf's Milk Tooth x5, Dead Ley Line Branch x5, Slime Condensate x3\n \
        **[✦✦----]**:20,000 Mora, Boreal Wolf's Cracked Tooth x5, Dead Ley Line Branch x18, Slime Condensate x12\n \
        **[✦✦✦---]**:30,000 Mora, Boreal Wolf's Cracked Tooth x9, Dead Ley Line Leaves x9, Slime Secretions x9\n \
        **[✦✦✦✦--]**:45,000 Mora, Boreal Wolf's Broken Fang x5, Dead Ley Line Leaves x18, Slime Secretions x14\n \
        **[✦✦✦✦✦-]**:55,000 Mora, Boreal Wolf's Broken Fang x9, Ley Line Sprout x14, Slime Concentrate x9\n \
        **[✦✦✦✦✦✦]**:65,000 Mora, Boreal Wolf's Nostalgia x6, Ley Line Sprout x27, Slime Concentrate x18", "Skyward Pride"]
        return lst11
    elif name.lower() == "the unforged":
        lst12 = ["https://static.wikia.nocookie.net/gensin-impact/images/f/f7/Weapon_The_Unforged.png/revision/latest/scale-to-width-down/256?cb=20201129060814", \
        "Capable of driving away evil spirits and wicked people alike, this edgeless claymore seems to possess divine might.", \
        "Claymore", ["608", "49.6%", "ATK"], \
        "**[✦-----]**:10,000 Mora, Mist Veiled Lead Elixir x5, Mist Grass Pollen x5, Treasure Hoarder Insignia x3\n \
        **[✦✦----]**:20,000 Mora, Mist Veiled Mercury Elixir x5, Mist Grass Pollen x18, Treasure Hoarder Insignia x12\n \
        **[✦✦✦---]**:30,000 Mora, Mist Veiled Mercury Elixir x9, Mist Grass x9, Silver Raven Insignia x9\n \
        **[✦✦✦✦--]**:45,000 Mora, Mist Veiled Gold Elixir x5, Mist Grass x18, Silver Raven Insignia x14\n \
        **[✦✦✦✦✦-]**:55,000 Mora, Mist Veiled Gold Elixir x9, Mist Grass Wick x14, Golden Raven Insignia x9\n \
        **[✦✦✦✦✦✦]**:65,000 Mora, Mist Veiled Primo Elixir x6, Mist Grass Wick x27, Golden Raven Insignia x18", "The Unforged"]
        return lst12
    elif name.lower() == "song of broken pines":
        lst13 = ["https://static.wikia.nocookie.net/gensin-impact/images/d/dd/Weapon_Song_of_Broken_Pines.png/revision/latest/scale-to-width-down/256?cb=20210518151739", \
        "A greatsword as light as the sigh of grass in the breeze, yet as merciless to the corrupt as a typhoon.", \
        "Claymore", ["741", "20.7%", "Physical DMG Bonus"], \
        "**[✦-----]**:10,000 Mora, Tile of Decarabian's Tower x5, Heavy Horn x5, Damaged Mask x3\n \
        **[✦✦----]**:20,000 Mora, Debris of Decarabian's City x5, Heavy Horn x18, Damaged Mask x12\n \
        **[✦✦✦---]**:30,000 Mora, Debris of Decarabian's City x9, Black Bronze Horn x9, Stained Mask x9\n \
        **[✦✦✦✦--]**:45,000 Mora, Fragment of Decarabian's Epic x5, Black Bronze Horn x18, Stained Mask x14\n \
        **[✦✦✦✦✦-]**:55,000 Mora, Fragment of Decarabian's Epic x9, Black Crystal Hornx14, Ominous Mask x9\n \
        **[✦✦✦✦✦✦]**:65,000 Mora, Scattered Piece of Decarabian's Dream x6, Black Crystal Horn x27, Ominous Mask x18", "Song of Broken Pines"]
        return lst13
    elif name.lower() == "engulfing lightning":
        lst14 = ["https://static.wikia.nocookie.net/gensin-impact/images/2/21/Weapon_Engulfing_Lightning.png/revision/latest/scale-to-width-down/256?cb=20210901044846", \
        'A naginata used to "cut grass." Any army that stands before this weapon will probably be likewise cut down...', \
        "Polearm", ["608", "55.1%", "Energy Recharge"], \
        "**[✦-----]**:10,000 Mora, Mask of the Wicked Lieutenant x5, Chaos Gear x5, Old Handguard x3\n \
        **[✦✦----]**:20,000 Mora, Mask of the Tiger's Bite x5, Chaos Gear x18, Old Handguard x12\n \
        **[✦✦✦---]**:30,000 Mora, Mask of the Tiger's Bite x9, Chaos Axis x9, Kageuchi Handguard x9\n \
        **[✦✦✦✦--]**:45,000 Mora, Mask of the One-Horned x5, Chaos Axis x18, Kageuchi Handguard x14\n \
        **[✦✦✦✦✦-]**:55,000 Mora, Mask of the One-Horned x9, Chaos Oculus x14, Famed Handguard x9\n \
        **[✦✦✦✦✦✦]**:65,000 Mora, Mask of the Kijin x6, Chaos Oculus x27, Famed Handguard x18", "Engulfing Lightning"]
        return lst14
    elif name.lower() == "skyward spine":
        lst15 = ["https://static.wikia.nocookie.net/gensin-impact/images/6/69/Weapon_Skyward_Spine.png/revision/latest/scale-to-width-down/256?cb=20201116035301", \
        "A polearm that symbolizes Dvalin's fire resolve. The upright shaft of this weapon points towards the heavens, clad in the might of sky and wind.", \
        "Polearm", ["674", "36.8%", "Energy Recharge"], \
        "**[✦-----]**:10,000 Mora, Fetters of the Dandelion Gladiator x5, Chaos Device x5, Divining Scroll x3\n \
        **[✦✦----]**:20,000 Mora, Chains of the Dandelion Gladiator x5, Chaos Device x18, Divining Scroll x12\n \
        **[✦✦✦---]**:30,000 Mora, Chains of the Dandelion Gladiator x9, Chaos Circuit x9, Sealed Scroll x9\n \
        **[✦✦✦✦--]**:45,000 Mora, Shackles of the Dandelion Gladiator x5, Chaos Circuit x18, Sealed Scroll x14\n \
        **[✦✦✦✦✦-]**:55,000 Mora, Shackles of the Dandelion Gladiator x9, Chaos Core x14, Forbidden Curse Scroll x9\n \
        **[✦✦✦✦✦✦]**:65,000 Mora, Dream of the Dandelion Gladiator x6, Chaos Core x27, Forbidden Curse Scroll x18", "Skyward Spine"]
        return lst15
    elif name.lower() == "primordial jade winged-spear":
        lst16 = ["https://static.wikia.nocookie.net/gensin-impact/images/8/80/Weapon_Primordial_Jade_Winged-Spear.png/revision/latest/scale-to-width-down/256?cb=20201116152024", \
        "A jade polearm made by the archons, capable of slaying ancient beasts.", \
        "Polearm", ["674", "22.1%", "CRIT Rate"], \
        "**[✦-----]**:10,000 Mora, Luminous Sands from Guyun x5, Hunter's Sacrificial Knife x5, Recruit's Insignia x3\n \
        **[✦✦----]**:20,000 Mora, Lustrous Stone from Guyun x5, Hunter's Sacrificial Knife x18, Recruit's Insignia x12\n \
        **[✦✦✦---]**:30,000 Mora, Lustrous Stone from Guyun x9, Agent's Sacrificial Knife x9, Sergeant's Insignia x9\n \
        **[✦✦✦✦--]**:45,000 Mora, Relic from Guyun x5, Agent's Sacrificial Knife x18, Sergeant's Insignia x14\n \
        **[✦✦✦✦✦-]**:55,000 Mora, Relic from Guyun x9, Inspector's Sacrificial Knife x14, Lieutenant's Insignia x9\n \
        **[✦✦✦✦✦✦]**:65,000 Mora, Divine Body from Guyun x6, Inspector's Sacrificial Knife x27, Lieutenant's Insignia x18", "Primordial Jade Winged-Spear"]
        return lst16
    elif name.lower() == "staff of homa":
        lst17 = ["https://static.wikia.nocookie.net/gensin-impact/images/1/17/Weapon_Staff_of_Homa.png/revision/latest/scale-to-width-down/256?cb=20210225200935", \
        'A "firewood staff" that was once used in ancient and long-lost rituals.', \
        "Polearm", ["608", "66.2%", "CRIT DMG"], \
        "**[✦-----]**:10,000 Mora, Grain of Aerosiderite x5, Dead Ley Line Branch x5, Slime Condensate x3\n \
        **[✦✦----]**:20,000 Mora, Piece of Aerosiderite x5, Dead Ley Line Branch x18, Slime Condensate x12\n \
        **[✦✦✦---]**:30,000 Mora, Piece of Aerosiderite x9, Dead Ley Line Leaves x9, Slime Secretions x9\n \
        **[✦✦✦✦--]**:45,000 Mora, Bit of Aerosiderite x5, Dead Ley Line Leaves x18, Slime Secretions x14\n \
        **[✦✦✦✦✦-]**:55,000 Mora, Bit of Aerosiderite x9, Ley Line Sprout x14, Slime Concentrate x9\n \
        **[✦✦✦✦✦✦]**:65,000 Mora, Chunk of Aerosiderite x6, Ley Line Sprout x27, Slime Concentrate x18", "Staff of Homa"]
        return lst17
    elif name.lower() == "vortex vanquisher":
        lst18 = ["https://static.wikia.nocookie.net/gensin-impact/images/d/d6/Weapon_Vortex_Vanquisher.png/revision/latest/scale-to-width-down/256?cb=20201129060822", \
        "This sharp polearm can seemingly pierce through anything. When swung, one can almost see the rift it tears in the air.", \
        "Polearm", ["608", "49.6%", "ATK"], \
        "**[✦-----]**:10,000 Mora, Grain of Aerosiderite x5, Fragile Bone Shard x5, Treasure Hoarder Insignia x3\n \
        **[✦✦----]**:20,000 Mora, Piece of Aerosiderite x5, Fragile Bone Shard x18, Treasure Hoarder Insignia x12\n \
        **[✦✦✦---]**:30,000 Mora, Piece of Aerosiderite x9, Sturdy Bone Shard x9, Silver Raven Insignia x9\n \
        **[✦✦✦✦--]**:45,000 Mora, Bit of Aerosiderite x5, Sturdy Bone Shard x18, Silver Raven Insignia x14\n \
        **[✦✦✦✦✦-]**:55,000 Mora, Bit of Aerosiderite x9, Fossilized Bone Shard x14, Golden Raven Insignia x9\n \
        **[✦✦✦✦✦✦]**:65,000 Mora, Chunk of Aerosiderite x6, Fossilized Bone Shard x27, Golden Raven Insignia x18", "Vortex Vanquisher"]
        return lst18
    elif name.lower() == "mistsplitter reforged":
        lst19 = ["https://static.wikia.nocookie.net/gensin-impact/images/0/09/Weapon_Mistsplitter_Reforged.png/revision/latest/scale-to-width-down/350?cb=20210721035408", \
        'A sword that blazes with a fierce violet light. The name "Reforged" comes from it having been broken once before.', \
        "Sword", ["674", "44.1%", "CRIT DMG"], \
        "**[✦-----]**:10,000 Mora, Coral Branch of a Distant Sea x5, Chaos Gear x5, Old Handguard x3\n \
        **[✦✦----]**:20,000 Mora, Jeweled Branch of a Distant Sea x5, Chaos Gear x18, Old Handguard x12\n \
        **[✦✦✦---]**:30,000 Mora, Jeweled Branch of a Distant Sea x9, Chaos Axis x9, Kageuchi Handguard x9\n \
        **[✦✦✦✦--]**:45,000 Mora, Jade Branch of a Distant Sea x5, Chaos Axis x18, Kageuchi Handguard x14\n \
        **[✦✦✦✦✦-]**:55,000 Mora, Jade Branch of a Distant Sea x9, Chaos Oculus x14, Famed Handguard x9\n \
        **[✦✦✦✦✦✦]**:65,000 Mora, Golden Branch of a Distant Sea x6, Chaos Oculus x27, Famed Handguard x18", "Mistsplitter Reforged	"]
        return lst19
    elif name.lower() == "aquila favonia":
        lst20 = ["https://static.wikia.nocookie.net/gensin-impact/images/6/6a/Weapon_Aquila_Favonia.png/revision/latest/scale-to-width-down/256?cb=20201120002750", \
        "The soul of the Knights of Favonius. Millennia later, it still calls on the winds of swift justice to vanquish all evil—just like the last heroine who wielded it.", \
        "Sword", ["674", "41.3%", "Physical DMG"], \
        "**[✦-----]**:10,000 Mora, Tile of Decarabian's Tower x5, Heavy Horn x5, Firm Arrowhead x3\n \
        **[✦✦----]**:20,000 Mora, Debris of Decarabian's City x5, Heavy Horn x18, Firm Arrowhead x12\n \
        **[✦✦✦---]**:30,000 Mora, Debris of Decarabian's City x9, Black Bronze Horn x9, Sharp Arrowhead x9\n \
        **[✦✦✦✦--]**:45,000 Mora, Fragment of Decarabian's Epic x5, Black Bronze Horn x18, Sharp Arrowhead x14\n \
        **[✦✦✦✦✦-]**:55,000 Mora, Fragment of Decarabian's Epic x9, Black Crystal Horn x14, Weathered Arrowhead x9\n \
        **[✦✦✦✦✦✦]**:65,000 Mora, Scattered Piece of Decarabian's Dream x6, Black Crystal Horn x27, Weathered Arrowhead x18", "Aquila Favonia"]
        return lst20
    elif name.lower() == "summit shaper":
        lst21 = ["https://static.wikia.nocookie.net/gensin-impact/images/c/ca/Weapon_Summit_Shaper.png/revision/latest/scale-to-width-down/256?cb=20201223042936", \
        "A symbol of a legendary pact, this sharp blade once cut off the peak of a mountain.", \
        "Sword", ["608", "49.6%", "CRIT Rate"], \
        "**[✦-----]**:10,000 Mora, Luminous Sands from Guyun x5, Hunter's Sacrificial Knife x5, Damaged Mask x3\n \
        **[✦✦----]**:20,000 Mora, Lustrous Stone from Guyun x5, Hunter's Sacrificial Knife x18, Damaged Mask x12\n \
        **[✦✦✦---]**:30,000 Mora, Lustrous Stone from Guyun x9, Agent's Sacrificial Knife x9, Stained Mask x9\n \
        **[✦✦✦✦--]**:45,000 Mora, Relic from Guyun x5, Agent's Sacrificial Knife x18, Stained Mask x14\n \
        **[✦✦✦✦✦-]**:55,000 Mora, Relic from Guyun x9, Inspector's Sacrificial Knife x14, Ominous Mask x9\n \
        **[✦✦✦✦✦✦]**:65,000 Mora, Divine Body from Guyun x6, Inspector's Sacrificial Knife x27, Ominous Mask x18", "Summit Shaper"]
        return lst21
    elif name.lower() == "skyward blade":
        lst22 = ["https://static.wikia.nocookie.net/gensin-impact/images/0/03/Weapon_Skyward_Blade.png/revision/latest/scale-to-width-down/256?cb=20201116035239", \
        "The sword of a knight that symbolizes the restored honor of Dvalin. The blessings of the Anemo Archon rest on the fuller of the blade, imbuing the sword with the powers of the sky and the wind.", \
        "Sword", ["608", "55.1%", "Energy Recharge"], \
        "**[✦-----]**:10,000 Mora, Boreal Wolf's Milk Tooth x5, Dead Ley Line Branch x5, Slime Condensate x3\n \
        **[✦✦----]**:20,000 Mora, Boreal Wolf's Cracked Tooth x5, Dead Ley Line Branch x18, Slime Condensate x12\n \
        **[✦✦✦---]**:30,000 Mora, Boreal Wolf's Cracked Tooth x9, Dead Ley Line Leaves x9, Slime Secretions x9\n \
        **[✦✦✦✦--]**:45,000 Mora, Boreal Wolf's Broken Fang x5, Dead Ley Line Leaves x18, Slime Secretions x14\n \
        **[✦✦✦✦✦-]**:55,000 Mora, Boreal Wolf's Broken Fang x9, Ley Line Sprout x14, Slime Concentrate x9\n \
        **[✦✦✦✦✦✦]**:65,000 Mora, Boreal Wolf's Nostalgia x6, Ley Line Sprout x27, Slime Concentrate x18", "Skyward Blade"]
        return lst22
    elif name.lower() == "freedom-sworn":
        lst23 = ["https://static.wikia.nocookie.net/gensin-impact/images/3/39/Weapon_Freedom-Sworn.png/revision/latest/scale-to-width-down/256?cb=20210629202549", \
        "A straight sword, azure as antediluvian song, and as keen as the oaths of freedom taken in the Land of Wind.", \
        "Sword", ["608", "198", "Elemental Mastery"], \
        "**[✦-----]**:10,000 Mora, Fetters of the Dandelion Gladiator x5, Chaos Device x5, Divining Scroll x3\n \
        **[✦✦----]**:20,000 Mora, Chains of the Dandelion Gladiator x5, Chaos Device x18, Divining Scroll x12\n \
        **[✦✦✦---]**:30,000 Mora, Chains of the Dandelion Gladiator x9, Chaos Circuit x9, Sealed Scroll x9\n \
        **[✦✦✦✦--]**:45,000 Mora, Shackles of the Dandelion Gladiator x5, Chaos Circuit x18, Sealed Scroll x14\n \
        **[✦✦✦✦✦-]**:55,000 Mora, Shackles of the Dandelion Gladiator x9, Chaos Core x14, Forbidden Curse Scroll x9\n \
        **[✦✦✦✦✦✦]**:65,000 Mora, Dream of the Dandelion Gladiator x6, Chaos Core x27, Forbidden Curse Scroll x18", "Freedom-Sworn"]
        return lst23
    elif name.lower() == "primordial jade cutter":
        lst24 = ["https://static.wikia.nocookie.net/gensin-impact/images/2/2a/Weapon_Primordial_Jade_Cutter.png/revision/latest/scale-to-width-down/256?cb=20210319202419", \
        "A ceremonial sword masterfully carved from pure jade. There almost seems to be an audible sigh in the wind as it is swung.", \
        "Sword", ["542", "44.1%", "CRIT Rate"], \
        "**[✦-----]**:10,000 Mora, Mist Veiled Lead Elixir x5, Mist Grass Pollen x5, Treasure Hoarder Insignia x3\n \
        **[✦✦----]**:20,000 Mora, Mist Veiled Mercury Elixir x5, Mist Grass Pollen x18, Treasure Hoarder Insignia x12\n \
        **[✦✦✦---]**:30,000 Mora, Mist Veiled Mercury Elixir x9, Mist Grass x9, Silver Raven Insignia x9\n \
        **[✦✦✦✦--]**:45,000 Mora, Mist Veiled Gold Elixir x5, Mist Grass x18, Silver Raven Insignia x14\n \
        **[✦✦✦✦✦-]**:55,000 Mora, Mist Veiled Gold Elixir x9, Mist Grass Wick x14, Golden Raven Insignia x9\n \
        **[✦✦✦✦✦✦]**:65,000 Mora, Mist Veiled Primo Elixir x6, Mist Grass Wick x27, Golden Raven Insignia x18", "Primordial Jade Cutter"]
        return lst24
    elif name.lower() == "":
        lst = ["", \
        "", \
        "Sword", ["674", "22.1%", "CRIT Rate"], \
        "**[✦-----]**:10,000 Mora,  x5,  x5,  x3\n \
        **[✦✦----]**:20,000 Mora,  x5,  x18,  x12\n \
        **[✦✦✦---]**:30,000 Mora,  x9,  x9,  x9\n \
        **[✦✦✦✦--]**:45,000 Mora,  x5,  x18,  x14\n \
        **[✦✦✦✦✦-]**:55,000 Mora,  x9,  x14,  x9\n \
        **[✦✦✦✦✦✦]**:65,000 Mora,  x6,  x27,  x18"]
        return lst