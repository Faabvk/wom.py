# wom.py - An asynchronous wrapper for the Wise Old Man API.
# Copyright (c) 2023-present Jonxslays
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from __future__ import annotations

from enum import Enum


class BaseEnum(Enum):
    """The base enum all library enums inherit from."""

    value: str  # pyright: ignore
    """The value of the enum member."""


class Metric(BaseEnum):
    """Represents a metric, this enum has no attributes itself.

    Will be one of:
        - `Activity`
        - `Boss`
        - `ComputedMetric`
        - `Skill`
    """


class Period(BaseEnum):
    FiveMins = "five_min"
    Day = "day"
    Week = "week"
    Month = "month"
    Year = "year"


class Skill(Metric):
    Overall = "overall"
    Attack = "attack"
    Defence = "defence"
    Strength = "strength"
    Hitpoints = "hitpoints"
    Ranged = "ranged"
    Prayer = "prayer"
    Magic = "magic"
    Cooking = "cooking"
    Woodcutting = "woodcutting"
    Fletching = "fletching"
    Fishing = "fishing"
    Firemaking = "firemaking"
    Crafting = "crafting"
    Smithing = "smithing"
    Mining = "mining"
    Herblore = "herblore"
    Agility = "agility"
    Thieving = "thieving"
    Slayer = "slayer"
    Farming = "farming"
    Runecrafting = "runecrafting"
    Hunter = "hunter"
    Construction = "construction"


class Activity(Metric):
    LeaguePoints = "league_points"
    BountyHunterHunter = "bounty_hunter_hunter"
    BountyHunterRogue = "bounty_hunter_rogue"
    ClueScrollsAll = "clue_scrolls_all"
    ClueScrollsBeginner = "clue_scrolls_beginner"
    ClueScrollsEasy = "clue_scrolls_easy"
    ClueScrollsMedium = "clue_scrolls_medium"
    ClueScrollsHard = "clue_scrolls_hard"
    ClueScrollsElite = "clue_scrolls_elite"
    ClueScrollsMaster = "clue_scrolls_master"
    LastManStanding = "last_man_standing"
    PvpArena = "pvp_arena"
    SoulWarsZeal = "soul_wars_zeal"
    GuardiansOfTheRift = "guardians_of_the_rift"


class Boss(Metric):
    AbyssalSire = "abyssal_sire"
    AlchemicalHydra = "alchemical_hydra"
    BarrowsChests = "barrows_chests"
    Brophyta = "bryophyta"
    Callisto = "callisto"
    Cerberus = "cerberus"
    ChambersOfXeric = "chambers_of_xeric"
    ChambersOfXericChallenge = "chambers_of_xeric_challenge_mode"
    ChaosElemental = "chaos_elemental"
    ChaosFanatic = "chaos_fanatic"
    CommanderZilyana = "commander_zilyana"
    CorporealBeast = "corporeal_beast"
    CrazyArchaeologist = "crazy_archaeologist"
    DagganothPrime = "dagannoth_prime"
    DagganothRex = "dagannoth_rex"
    DagganothSupreme = "dagannoth_supreme"
    DerangedArchaeologist = "deranged_archaeologist"
    GeneralGraardor = "general_graardor"
    GiantMole = "giant_mole"
    GrotesqueGuardians = "grotesque_guardians"
    Hespori = "hespori"
    KalphiteQueen = "kalphite_queen"
    KingBlackDragon = "king_black_dragon"
    Kraken = "kraken"
    Kreearra = "kreearra"
    KrilTsutaroth = "kril_tsutsaroth"
    Mimic = "mimic"
    Nex = "nex"
    Nightmare = "nightmare"
    PhosanisNightmare = "phosanis_nightmare"
    Obor = "obor"
    PhantomMuspah = "phantom_muspah"
    Sarachnis = "sarachnis"
    Scorpia = "scorpia"
    Skotizo = "skotizo"
    Tempoross = "tempoross"
    TheGuantlet = "the_gauntlet"
    TheCorruptedGauntlet = "the_corrupted_gauntlet"
    TheatreOfBlood = "theatre_of_blood"
    TheatreOfBloodHard = "theatre_of_blood_hard_mode"
    ThermonuclearSmokeDevil = "thermonuclear_smoke_devil"
    TombsOfAmascut = "tombs_of_amascut"
    TombsOfAmascutExpert = "tombs_of_amascut_expert"
    TzkalZuk = "tzkal_zuk"
    TztokJad = "tztok_jad"
    Venenatis = "venenatis"
    Vetion = "vetion"
    Vorkath = "vorkath"
    Wintertodt = "wintertodt"
    Zalcano = "zalcano"
    Zulrah = "zulrah"


class ComputedMetric(Metric):
    """A metric that is computed."""

    Ehp = "ehp"
    """Efficient hours played."""
    Ehb = "ehb"
    """Efficient hours bossed."""