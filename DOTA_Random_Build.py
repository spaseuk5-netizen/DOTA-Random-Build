import random

roles = ["5 pos", "4 pos", "3 pos", "2 pos", "1 pos"]

start_buy = [
    "Wraith Band", "Magic Wand", "Bracer", "Null Talisman"
]

heroes = [
    "Abaddon", "Alchemist", "Ancient Apparition", "Anti-Mage", "Arc Warden", "Axe",
    "Bane", "Batrider", "Beastmaster", "Bloodseeker", "Bounty Hunter", "Brewmaster",
    "Bristleback", "Broodmother", "Centaur Warrunner", "Chaos Knight", "Chen", "Clinkz",
    "Clockwerk", "Crystal Maiden", "Dark Seer", "Dark Willow", "Dawnbreaker", "Dazzle",
    "Death Prophet", "Disruptor", "Doom", "Dragon Knight", "Drow Ranger", "Earth Spirit",
    "Earthshaker", "Elder Titan", "Ember Spirit", "Enchantress", "Enigma", "Faceless Void",
    "Grimstroke", "Gyrocopter", "Hoodwink", "Huskar", "Invoker", "Io", "Jakiro",
    "Juggernaut", "Keeper of the Light", "Kez", "Kunkka", "Largo", "Legion Commander", "Leshrac",
    "Lich", "Lifestealer", "Lina", "Lion", "Lone Druid", "Luna", "Lycan", "Magnus",
    "Marci", "Mars", "Medusa", "Meepo", "Mirana", "Monkey King", "Morphling", "Muerta",
    "Naga Siren", "Nature's Prophet", "Necrophos", "Night Stalker", "Nyx Assassin",
    "Ogre Magi", "Omniknight", "Oracle", "Outworld Destroyer", "Pangolier",
    "Phantom Assassin", "Phantom Lancer", "Phoenix", "Primal Beast", "Puck", "Pudge",
    "Pugna", "Queen of Pain", "Razor", "Riki", "Ringmaster", "Rubick", "Sand King",
    "Shadow Demon", "Shadow Fiend", "Shadow Shaman", "Silencer", "Skywrath Mage",
    "Slardar", "Slark", "Snapfire", "Sniper", "Spectre", "Spirit Breaker", "Storm Spirit",
    "Sven", "Techies", "Templar Assassin", "Terrorblade", "Tidehunter", "Timbersaw",
    "Tinker", "Tiny", "Treant Protector", "Troll Warlord", "Tusk", "Underlord",
    "Undying", "Ursa", "Vengeful Spirit", "Venomancer", "Viper", "Visage", "Void Spirit",
    "Warlock", "Weaver", "Windranger", "Winter Wyvern", "Witch Doctor", "Wraith King", "Zeus",
]

boots = [
    "Arcane Boots", "Boots of Bearing", "Boots of Travel", "Boots of Travel 2",
    "Guardian Greaves", "Phase Boots", "Power Treads", "Tranquil Boots",
]

items = [
    # Early / Accessories
    "Falcon Blade", "Hand of Midas", "Oblivion Staff", "Orb of Corrosion",
    "Perseverance", "Soul Ring",
    # Support
    "Aether Lens", "Aghanim's Scepter", "Blink Dagger", "Arcane Blink",
    "Overwhelming Blink", "Swift Blink", "Drum of Endurance", "Essence Distiller",
    "Eul's Scepter of Divinity", "Wind Waker", "Force Staff", "Hurricane Pike",
    "Glimmer Cape", "Holy Locket", "Mekansm", "Pavise", "Solar Crest",
    "Pipe of Insight", "Rod of Atos", "Gleipnir", "Scythe of Vyse",
    "Spirit Vessel", "Urn of Shadows", "Veil of Discord", "Vladmir's Offering",
    # Magic
    "Aghanim's Blessing", "Bloodstone", "Crella's Crozier", "Dagon",
    "Ethereal Blade", "Kaya", "Kaya and Sange", "Yasha and Kaya",
    "Octarine Core", "Orchid Malevolence", "Bloodthorn", "Parasma",
    "Phylactery", "Refresher Orb", "Shiva's Guard", "Witch Blade",
    # Defense
    "Aeon Disk", "Assault Cuirass", "Black King Bar", "Blade Mail",
    "Consecrated Wraps", "Crimson Guard", "Eternal Shroud", "Heart of Tarrasque",
    "Heaven's Halberd", "Linken's Sphere", "Lotus Orb", "Manta Style",
    "Sange", "Sange and Yasha", "Soul Booster", "Vanguard",
    # Damage
    "Abyssal Blade", "Armlet of Mordiggian", "Battle Fury", "Butterfly",
    "Crystalys", "Daedalus", "Desolator", "Diffusal Blade", "Disperser",
    "Divine Rapier", "Dragon Lance", "Echo Sabre", "Harpoon", "Eye of Skadi",
    "Helm of the Dominator", "Maelstrom", "Mjollnir", "Mage Slayer",
    "Mask of Madness", "Meteor Hammer", "Monkey King Bar", "Moon Shard",
    "Nullifier", "Quarterstaff", "Radiance", "Revenant's Brooch",
    "Satanic", "Shadow Blade", "Silver Edge", "Skull Basher", "Yasha",
    # Patch 7.42 shop items
    "Bloodslinger", "Caduceus", "Ristul's Devotion", "Sabatons of Mordiggian",
    "Skypiercer", "Starforge",
]

# Drop-only / non-shop item from 7.42
special_drops = ["Greater Horn of Battle"]

lvls = [10, 15, 20, 25]
talents = ["Left (1)", "Right (2)"]
skills = ["Skill 1", "Skill 2", "Skill 3"]

while True:
    role = random.choice(roles)
    hero = random.choice(heroes)
    early_items = random.sample(start_buy, 2)
    chosen_boots = random.choice(boots)
    build = random.sample(items, 5)
    chosen_talents = random.choices(talents, k=4)
    talent_tree = [f"Lvl {lvl}: {side}" for lvl, side in zip(lvls, chosen_talents)]
    maxing = random.choice(skills)

    print(f"\nRole: {role}")
    print(f"Hero: {hero}")
    print("---------------")
    print(f"Early item: {', '.join(early_items)}")
    print(f"Boots (Slot 1): {chosen_boots}")
    print(f"Build (in order): {', '.join(build)}")
    print("---------------")
    print(f"Talents: {', '.join(talent_tree)}")
    print(f"Max first: {maxing}")

    cmd = input("\nEnter — new roll / q — quit: ").strip().lower()
    if cmd == 'q':
        break
