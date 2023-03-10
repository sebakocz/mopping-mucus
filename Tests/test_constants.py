from Database.Models.draft import PickType, DraftStatus

INPUT_FILE_LINES = [
    "https://files.collective.gg/p/cards/9803f3b0-2b61-11eb-a0f9-41a57384b22e-s.png",
    "https://files.collective.gg/p/cards/ee442390-8fce-11eb-9348-5bd7bae36142-s.png",
    "https://files.collective.gg/p/cards/17d9dd00-627d-11eb-96e6-21b90bd58800-s.png",
    "Red Leaf Warshaman",
    "Huntsman's Return",
    "Head Chieftain Dzikus",
    "00cb6290-61b4-11ed-82b4-833eed596c50",
    "612f6fe0-f3e2-11ec-a26e-9defb71be79c",
    "d43cdd40-612b-11ed-82b4-833eed596c50",
]

INPUT_FILE_LINES_LONG = [
    "https://files.collective.gg/p/cards/d3d4c5d0-1806-11ec-bcd0-97cc3bf19ee0-s.png",
    "https://files.collective.gg/p/cards/d6a1ef90-1806-11ec-bcd0-97cc3bf19ee0-s.png",
    "https://files.collective.gg/p/cards/d96d1d80-1806-11ec-bcd0-97cc3bf19ee0-s.png",
    "https://files.collective.gg/p/cards/dbee7130-1806-11ec-bcd0-97cc3bf19ee0-s.png",
    "https://files.collective.gg/p/cards/de5d9c70-1806-11ec-bcd0-97cc3bf19ee0-s.png",
    "https://files.collective.gg/p/cards/e0d13480-1806-11ec-bcd0-97cc3bf19ee0-s.png",
    "https://files.collective.gg/p/cards/e337d440-1806-11ec-bcd0-97cc3bf19ee0-s.png",
    "https://files.collective.gg/p/cards/e5d73740-1806-11ec-bcd0-97cc3bf19ee0-s.png",
    "https://files.collective.gg/p/cards/e8544530-1806-11ec-bcd0-97cc3bf19ee0-s.png",
    "https://files.collective.gg/p/cards/eac85270-1806-11ec-bcd0-97cc3bf19ee0-s.png",
    "https://files.collective.gg/p/cards/ed678e60-1806-11ec-bcd0-97cc3bf19ee0-s.png",
    "https://files.collective.gg/p/cards/efd05100-1806-11ec-bcd0-97cc3bf19ee0-s.png",
    "https://files.collective.gg/p/cards/f22fc4d0-1806-11ec-bcd0-97cc3bf19ee0-s.png",
    "https://files.collective.gg/p/cards/f496d9c0-1806-11ec-bcd0-97cc3bf19ee0-s.png",
    "https://files.collective.gg/p/cards/f723c630-1806-11ec-bcd0-97cc3bf19ee0-s.png",
    "https://files.collective.gg/p/cards/f9688610-1806-11ec-bcd0-97cc3bf19ee0-s.png",
    "https://files.collective.gg/p/cards/fbc75da0-1806-11ec-bcd0-97cc3bf19ee0-s.png",
    "https://files.collective.gg/p/cards/fe703680-1806-11ec-bcd0-97cc3bf19ee0-s.png",
    "https://files.collective.gg/p/cards/00e247f0-1807-11ec-bcd0-97cc3bf19ee0-s.png",
    "https://files.collective.gg/p/cards/03439080-1807-11ec-bcd0-97cc3bf19ee0-s.png",
    "https://files.collective.gg/p/cards/05df4a00-1807-11ec-bcd0-97cc3bf19ee0-m.png",
    "https://files.collective.gg/p/cards/084a7da0-1807-11ec-bcd0-97cc3bf19ee0-m.png",
    "https://files.collective.gg/p/cards/0acc6d90-1807-11ec-bcd0-97cc3bf19ee0-m.png",
    "https://files.collective.gg/p/cards/0d3afc90-1807-11ec-bcd0-97cc3bf19ee0-m.png",
    "https://files.collective.gg/p/cards/0fb57270-1807-11ec-bcd0-97cc3bf19ee0-m.png",
    "https://files.collective.gg/p/cards/12323240-1807-11ec-bcd0-97cc3bf19ee0-m.png",
    "https://files.collective.gg/p/cards/149c2d60-1807-11ec-bcd0-97cc3bf19ee0-m.png",
    "https://files.collective.gg/p/cards/17276c20-1807-11ec-bcd0-97cc3bf19ee0-m.png",
    "https://files.collective.gg/p/cards/19ad53b0-1807-11ec-bcd0-97cc3bf19ee0-m.png",
    "https://files.collective.gg/p/cards/1c27a280-1807-11ec-bcd0-97cc3bf19ee0-m.png",
    "https://files.collective.gg/p/cards/1ed7f570-1807-11ec-bcd0-97cc3bf19ee0-m.png",
    "https://files.collective.gg/p/cards/21488040-1807-11ec-bcd0-97cc3bf19ee0-m.png",
    "https://files.collective.gg/p/cards/23bd29c0-1807-11ec-bcd0-97cc3bf19ee0-m.png",
    "https://files.collective.gg/p/cards/265057c0-1807-11ec-bcd0-97cc3bf19ee0-m.png",
    "https://files.collective.gg/p/cards/28eb4df0-1807-11ec-bcd0-97cc3bf19ee0-m.png",
    "https://files.collective.gg/p/cards/2b5dfba0-1807-11ec-bcd0-97cc3bf19ee0-m.png",
    "https://files.collective.gg/p/cards/2e0db250-1807-11ec-bcd0-97cc3bf19ee0-m.png",
    "https://files.collective.gg/p/cards/3080d530-1807-11ec-bcd0-97cc3bf19ee0-m.png",
    "https://files.collective.gg/p/cards/32fcaaa0-1807-11ec-bcd0-97cc3bf19ee0-m.png",
    "https://files.collective.gg/p/cards/356bfcf0-1807-11ec-bcd0-97cc3bf19ee0-m.png",
    "https://files.collective.gg/p/cards/3828abf0-1807-11ec-bcd0-97cc3bf19ee0-s.png",
    "https://files.collective.gg/p/cards/3a6ccf90-1807-11ec-bcd0-97cc3bf19ee0-s.png",
    "https://files.collective.gg/p/cards/3caf93a0-1807-11ec-bcd0-97cc3bf19ee0-s.png",
    "https://files.collective.gg/p/cards/3eed9cc0-1807-11ec-bcd0-97cc3bf19ee0-s.png",
    "https://files.collective.gg/p/cards/412d5390-1807-11ec-bcd0-97cc3bf19ee0-s.png",
    "https://files.collective.gg/p/cards/435eb280-1807-11ec-bcd0-97cc3bf19ee0-s.png",
    "https://files.collective.gg/p/cards/45a28800-1807-11ec-bcd0-97cc3bf19ee0-s.png",
    "https://files.collective.gg/p/cards/47edd790-1807-11ec-bcd0-97cc3bf19ee0-s.png",
    "https://files.collective.gg/p/cards/4a2b9290-1807-11ec-bcd0-97cc3bf19ee0-s.png",
    "https://files.collective.gg/p/cards/4c5e7820-1807-11ec-bcd0-97cc3bf19ee0-s.png",
    "https://files.collective.gg/p/cards/4ed76760-1807-11ec-bcd0-97cc3bf19ee0-s.png",
    "https://files.collective.gg/p/cards/5116a900-1807-11ec-bcd0-97cc3bf19ee0-s.png",
    "https://files.collective.gg/p/cards/535e9d30-1807-11ec-bcd0-97cc3bf19ee0-s.png",
    "https://files.collective.gg/p/cards/559d69a0-1807-11ec-bcd0-97cc3bf19ee0-s.png",
    "https://files.collective.gg/p/cards/57df6a60-1807-11ec-bcd0-97cc3bf19ee0-s.png",
    "https://files.collective.gg/p/cards/5a289710-1807-11ec-bcd0-97cc3bf19ee0-s.png",
    "https://files.collective.gg/p/cards/5c6b5b20-1807-11ec-bcd0-97cc3bf19ee0-s.png",
    "https://files.collective.gg/p/cards/5eaee280-1807-11ec-bcd0-97cc3bf19ee0-s.png",
    "https://files.collective.gg/p/cards/60f35440-1807-11ec-bcd0-97cc3bf19ee0-s.png",
    "https://files.collective.gg/p/cards/63237ab0-1807-11ec-bcd0-97cc3bf19ee0-s.png",
]

CARDS_LIST_LONG = [
    {
        "name": "Chrosyian Archivist",
        "link": "https://files.collective.gg/p/cards/d3d4c5d0-1806-11ec-bcd0-97cc3bf19ee0-s.png",
    },
    {
        "name": "Chrosyian Archivist",
        "link": "https://files.collective.gg/p/cards/d6a1ef90-1806-11ec-bcd0-97cc3bf19ee0-s.png",
    },
    {
        "name": "Chrosyian Archivist",
        "link": "https://files.collective.gg/p/cards/d96d1d80-1806-11ec-bcd0-97cc3bf19ee0-s.png",
    },
    {
        "name": "Chrosyian Archivist",
        "link": "https://files.collective.gg/p/cards/dbee7130-1806-11ec-bcd0-97cc3bf19ee0-s.png",
    },
    {
        "name": "Chrosyian Archivist",
        "link": "https://files.collective.gg/p/cards/de5d9c70-1806-11ec-bcd0-97cc3bf19ee0-s.png",
    },
    {
        "name": "Chrosyian Archivist",
        "link": "https://files.collective.gg/p/cards/e0d13480-1806-11ec-bcd0-97cc3bf19ee0-s.png",
    },
    {
        "name": "Chrosyian Archivist",
        "link": "https://files.collective.gg/p/cards/e337d440-1806-11ec-bcd0-97cc3bf19ee0-s.png",
    },
    {
        "name": "Chrosyian Archivist",
        "link": "https://files.collective.gg/p/cards/e5d73740-1806-11ec-bcd0-97cc3bf19ee0-s.png",
    },
    {
        "name": "Chrosyian Archivist",
        "link": "https://files.collective.gg/p/cards/e8544530-1806-11ec-bcd0-97cc3bf19ee0-s.png",
    },
    {
        "name": "Chrosyian Archivist",
        "link": "https://files.collective.gg/p/cards/eac85270-1806-11ec-bcd0-97cc3bf19ee0-s.png",
    },
    {
        "name": "Reusable Partling",
        "link": "https://files.collective.gg/p/cards/ed678e60-1806-11ec-bcd0-97cc3bf19ee0-s.png",
    },
    {
        "name": "Reusable Partling",
        "link": "https://files.collective.gg/p/cards/efd05100-1806-11ec-bcd0-97cc3bf19ee0-s.png",
    },
    {
        "name": "Reusable Partling",
        "link": "https://files.collective.gg/p/cards/f22fc4d0-1806-11ec-bcd0-97cc3bf19ee0-s.png",
    },
    {
        "name": "Reusable Partling",
        "link": "https://files.collective.gg/p/cards/f496d9c0-1806-11ec-bcd0-97cc3bf19ee0-s.png",
    },
    {
        "name": "Reusable Partling",
        "link": "https://files.collective.gg/p/cards/f723c630-1806-11ec-bcd0-97cc3bf19ee0-s.png",
    },
    {
        "name": "Reusable Partling",
        "link": "https://files.collective.gg/p/cards/f9688610-1806-11ec-bcd0-97cc3bf19ee0-s.png",
    },
    {
        "name": "Reusable Partling",
        "link": "https://files.collective.gg/p/cards/fbc75da0-1806-11ec-bcd0-97cc3bf19ee0-s.png",
    },
    {
        "name": "Reusable Partling",
        "link": "https://files.collective.gg/p/cards/fe703680-1806-11ec-bcd0-97cc3bf19ee0-s.png",
    },
    {
        "name": "Reusable Partling",
        "link": "https://files.collective.gg/p/cards/00e247f0-1807-11ec-bcd0-97cc3bf19ee0-s.png",
    },
    {
        "name": "Reusable Partling",
        "link": "https://files.collective.gg/p/cards/03439080-1807-11ec-bcd0-97cc3bf19ee0-s.png",
    },
    {
        "name": "Mass Production",
        "link": "https://files.collective.gg/p/cards/05df4a00-1807-11ec-bcd0-97cc3bf19ee0-m.png",
    },
    {
        "name": "Mass Production",
        "link": "https://files.collective.gg/p/cards/084a7da0-1807-11ec-bcd0-97cc3bf19ee0-m.png",
    },
    {
        "name": "Mass Production",
        "link": "https://files.collective.gg/p/cards/0acc6d90-1807-11ec-bcd0-97cc3bf19ee0-m.png",
    },
    {
        "name": "Mass Production",
        "link": "https://files.collective.gg/p/cards/0d3afc90-1807-11ec-bcd0-97cc3bf19ee0-m.png",
    },
    {
        "name": "Mass Production",
        "link": "https://files.collective.gg/p/cards/0fb57270-1807-11ec-bcd0-97cc3bf19ee0-m.png",
    },
    {
        "name": "Mass Production",
        "link": "https://files.collective.gg/p/cards/12323240-1807-11ec-bcd0-97cc3bf19ee0-m.png",
    },
    {
        "name": "Mass Production",
        "link": "https://files.collective.gg/p/cards/149c2d60-1807-11ec-bcd0-97cc3bf19ee0-m.png",
    },
    {
        "name": "Mass Production",
        "link": "https://files.collective.gg/p/cards/17276c20-1807-11ec-bcd0-97cc3bf19ee0-m.png",
    },
    {
        "name": "Mass Production",
        "link": "https://files.collective.gg/p/cards/19ad53b0-1807-11ec-bcd0-97cc3bf19ee0-m.png",
    },
    {
        "name": "Mass Production",
        "link": "https://files.collective.gg/p/cards/1c27a280-1807-11ec-bcd0-97cc3bf19ee0-m.png",
    },
    {
        "name": "Framework",
        "link": "https://files.collective.gg/p/cards/1ed7f570-1807-11ec-bcd0-97cc3bf19ee0-m.png",
    },
    {
        "name": "Framework",
        "link": "https://files.collective.gg/p/cards/21488040-1807-11ec-bcd0-97cc3bf19ee0-m.png",
    },
    {
        "name": "Framework",
        "link": "https://files.collective.gg/p/cards/23bd29c0-1807-11ec-bcd0-97cc3bf19ee0-m.png",
    },
    {
        "name": "Framework",
        "link": "https://files.collective.gg/p/cards/265057c0-1807-11ec-bcd0-97cc3bf19ee0-m.png",
    },
    {
        "name": "Framework",
        "link": "https://files.collective.gg/p/cards/28eb4df0-1807-11ec-bcd0-97cc3bf19ee0-m.png",
    },
    {
        "name": "Framework",
        "link": "https://files.collective.gg/p/cards/2b5dfba0-1807-11ec-bcd0-97cc3bf19ee0-m.png",
    },
    {
        "name": "Framework",
        "link": "https://files.collective.gg/p/cards/2e0db250-1807-11ec-bcd0-97cc3bf19ee0-m.png",
    },
    {
        "name": "Framework",
        "link": "https://files.collective.gg/p/cards/3080d530-1807-11ec-bcd0-97cc3bf19ee0-m.png",
    },
    {
        "name": "Framework",
        "link": "https://files.collective.gg/p/cards/32fcaaa0-1807-11ec-bcd0-97cc3bf19ee0-m.png",
    },
    {
        "name": "Framework",
        "link": "https://files.collective.gg/p/cards/356bfcf0-1807-11ec-bcd0-97cc3bf19ee0-m.png",
    },
    {
        "name": "Grid Monitor",
        "link": "https://files.collective.gg/p/cards/3828abf0-1807-11ec-bcd0-97cc3bf19ee0-s.png",
    },
    {
        "name": "Grid Monitor",
        "link": "https://files.collective.gg/p/cards/3a6ccf90-1807-11ec-bcd0-97cc3bf19ee0-s.png",
    },
    {
        "name": "Grid Monitor",
        "link": "https://files.collective.gg/p/cards/3caf93a0-1807-11ec-bcd0-97cc3bf19ee0-s.png",
    },
    {
        "name": "Grid Monitor",
        "link": "https://files.collective.gg/p/cards/3eed9cc0-1807-11ec-bcd0-97cc3bf19ee0-s.png",
    },
    {
        "name": "Grid Monitor",
        "link": "https://files.collective.gg/p/cards/412d5390-1807-11ec-bcd0-97cc3bf19ee0-s.png",
    },
    {
        "name": "Grid Monitor",
        "link": "https://files.collective.gg/p/cards/435eb280-1807-11ec-bcd0-97cc3bf19ee0-s.png",
    },
    {
        "name": "Grid Monitor",
        "link": "https://files.collective.gg/p/cards/45a28800-1807-11ec-bcd0-97cc3bf19ee0-s.png",
    },
    {
        "name": "Grid Monitor",
        "link": "https://files.collective.gg/p/cards/47edd790-1807-11ec-bcd0-97cc3bf19ee0-s.png",
    },
    {
        "name": "Grid Monitor",
        "link": "https://files.collective.gg/p/cards/4a2b9290-1807-11ec-bcd0-97cc3bf19ee0-s.png",
    },
    {
        "name": "Grid Monitor",
        "link": "https://files.collective.gg/p/cards/4c5e7820-1807-11ec-bcd0-97cc3bf19ee0-s.png",
    },
    {
        "name": "N3ON Triple Ace",
        "link": "https://files.collective.gg/p/cards/4ed76760-1807-11ec-bcd0-97cc3bf19ee0-s.png",
    },
    {
        "name": "N3ON Triple Ace",
        "link": "https://files.collective.gg/p/cards/5116a900-1807-11ec-bcd0-97cc3bf19ee0-s.png",
    },
    {
        "name": "N3ON Triple Ace",
        "link": "https://files.collective.gg/p/cards/535e9d30-1807-11ec-bcd0-97cc3bf19ee0-s.png",
    },
    {
        "name": "N3ON Triple Ace",
        "link": "https://files.collective.gg/p/cards/559d69a0-1807-11ec-bcd0-97cc3bf19ee0-s.png",
    },
    {
        "name": "N3ON Triple Ace",
        "link": "https://files.collective.gg/p/cards/57df6a60-1807-11ec-bcd0-97cc3bf19ee0-s.png",
    },
    {
        "name": "N3ON Triple Ace",
        "link": "https://files.collective.gg/p/cards/5a289710-1807-11ec-bcd0-97cc3bf19ee0-s.png",
    },
    {
        "name": "N3ON Triple Ace",
        "link": "https://files.collective.gg/p/cards/5c6b5b20-1807-11ec-bcd0-97cc3bf19ee0-s.png",
    },
    {
        "name": "N3ON Triple Ace",
        "link": "https://files.collective.gg/p/cards/5eaee280-1807-11ec-bcd0-97cc3bf19ee0-s.png",
    },
    {
        "name": "N3ON Triple Ace",
        "link": "https://files.collective.gg/p/cards/60f35440-1807-11ec-bcd0-97cc3bf19ee0-s.png",
    },
    {
        "name": "N3ON Triple Ace",
        "link": "https://files.collective.gg/p/cards/63237ab0-1807-11ec-bcd0-97cc3bf19ee0-s.png",
    },
]

OUTPUT_CARD_OBJECTS = [
    {
        "name": "Red Leaf Warshaman",
        "link": "https://files.collective.gg/p/cards/a54bed60-f790-11eb-89bb-8d69998314a9-m.png",
    },
    {
        "name": "Huntsman's Return",
        "link": "https://files.collective.gg/p/cards/0800fac0-010c-11ec-82dc-6f26f557b807-s.png",
    },
    {
        "name": "Head Chieftain Dzikus",
        "link": "https://files.collective.gg/p/cards/b4af1590-b526-11eb-b069-75e1b18ca834-m.png",
    },
    {
        "name": "Wanda Walsh, CPA",
        "link": "https://files.collective.gg/p/cards/9803f3b0-2b61-11eb-a0f9-41a57384b22e-s.png",
    },
    {
        "name": "Aspamalgam",
        "link": "https://files.collective.gg/p/cards/ee442390-8fce-11eb-9348-5bd7bae36142-s.png",
    },
    {
        "name": "Door to Elsewhere",
        "link": "https://files.collective.gg/p/cards/17d9dd00-627d-11eb-96e6-21b90bd58800-s.png",
    },
    {
        "name": "Akai Twin-Blade",
        "link": "https://files.collective.gg/p/cards/00cb6290-61b4-11ed-82b4-833eed596c50-m.png",
    },
    {
        "name": "Bumblebeam",
        "link": "https://files.collective.gg/p/cards/612f6fe0-f3e2-11ec-a26e-9defb71be79c-m.png",
    },
    {
        "name": "Yoricho Aspirant",
        "link": "https://files.collective.gg/p/cards/d43cdd40-612b-11ed-82b4-833eed596c50-s.png",
    },
]

DRAFT_OPTIONS = {
    "owner_discord_id": 225657172216905730,
    "name": "Test Draft",
    "description": "Test Description",
    "pick_type": PickType.BLUEPRINT,
    "packs_per_player": 3,
    "cards_per_pack": 5,
    "seconds_per_pick": 30,
    "max_participants": 4,
}

DRAFT_OPTIONS_TWO = {
    "owner_discord_id": 225657172216905730,
    "name": "Test Draft 2",
    "description": "Test Description",
    "pick_type": PickType.SINGLETON,
    "packs_per_player": 4,
    "cards_per_pack": 9,
    "seconds_per_pick": 33,
    "max_participants": 8,
}
