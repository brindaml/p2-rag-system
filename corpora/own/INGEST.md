# Ingest report

Written by `uv run p2 ingest`.
It lists every document in this corpus that ingest added, with what the cleaning pass did and anything that looks wrong.
Running ingest again adds to the table and replaces the "last run" section, and `uv run p2 ingest --report` rewrites it for the documents in docs/ now, after you removed some.

## Summary

- Documents: 226 (the final check needs at least 200)
- Words: 402,616
- Estimated tokens (words times 1.4): 563,662 (`p2 check` warns above 800,000 and fails above 1,000,000)
- Flagged documents: 0

## Documents

| docid | words | characters per page | flags | cleaning |
|---|---:|---:|---|---|
| `arceus` | 2,668 | - | - | - |
| `arctovish` | 1,214 | - | - | - |
| `arctozolt` | 1,214 | - | - | - |
| `ash_ketchum` | 2,457 | - | - | - |
| `ball_guy` | 977 | - | - | - |
| `blastoise` | 1,626 | - | - | - |
| `blaziken` | 1,744 | - | - | - |
| `brock_-pokemon` | 1,262 | - | - | - |
| `bulbasaur` | 1,656 | - | - | - |
| `butterfree` | 1,418 | - | - | - |
| `chandelure` | 1,840 | - | - | - |
| `charizard` | 2,165 | - | - | - |
| `charmander` | 1,902 | - | - | - |
| `cubone` | 1,730 | - | - | - |
| `cynthia_-pokemon` | 1,347 | - | - | - |
| `delibird` | 1,751 | - | - | - |
| `detective_pikachu_-film` | 4,028 | - | - | - |
| `detective_pikachu_-video_game` | 2,089 | - | - | - |
| `detective_pikachu_returns` | 771 | - | - | - |
| `diglett_and_dugtrio` | 2,139 | - | - | - |
| `ditto_-pokemon` | 2,687 | - | - | - |
| `dracovish` | 1,214 | - | - | - |
| `dracozolt` | 1,214 | - | - | - |
| `dracozolt-_arctozolt-_dracovish-_and_arctovish` | 1,218 | - | - | - |
| `dragonite` | 2,298 | - | - | - |
| `eevee` | 2,392 | - | - | - |
| `flygon` | 1,505 | - | - | - |
| `fuecoco` | 938 | - | - | - |
| `garchomp` | 1,185 | - | - | - |
| `gardevoir` | 2,220 | - | - | - |
| `gengar` | 1,774 | - | - | - |
| `gholdengo` | 2,161 | - | - | - |
| `gyarados` | 1,557 | - | - | - |
| `haunter_-pokemon` | 1,538 | - | - | - |
| `heracross` | 2,864 | - | - | - |
| `hex_maniac` | 972 | - | - | - |
| `hey_you-_pikachu` | 603 | - | - | - |
| `hop_-pokemon` | 1,367 | - | - | - |
| `jigglypuff` | 2,167 | - | - | - |
| `jynx` | 1,753 | - | - | - |
| `kleavor` | 1,400 | - | - | - |
| `klefki` | 1,019 | - | - | - |
| `larry_-pokemon` | 1,249 | - | - | - |
| `learn_with_pokemon-_typing_adventure` | 646 | - | - | - |
| `lebanne` | 1,013 | - | - | - |
| `liko_-pokemon` | 851 | - | - | - |
| `lillie_-pokemon` | 1,000 | - | - | - |
| `lucario` | 2,105 | - | - | - |
| `magikarp_and_gyarados` | 1,559 | - | - | - |
| `malamar` | 1,715 | - | - | - |
| `mawile` | 1,952 | - | - | - |
| `meltan` | 2,227 | - | - | - |
| `meowscarada` | 1,124 | - | - | - |
| `meowth` | 2,374 | - | - | - |
| `mew_-pokemon` | 2,548 | - | - | - |
| `mewtwo` | 3,823 | - | - | - |
| `mimikyu` | 1,373 | - | - | - |
| `missingno` | 1,477 | - | - | - |
| `misty_-pokemon` | 1,545 | - | - | - |
| `mr._mime` | 1,869 | - | - | - |
| `my_pokemon_ranch` | 1,000 | - | - | - |
| `nemona` | 974 | - | - | - |
| `nessa_-pokemon` | 1,319 | - | - | - |
| `new_pokemon_snap` | 7,287 | - | - | - |
| `ninetales` | 1,617 | - | - | - |
| `nintendo_puzzle_collection` | 933 | - | - | - |
| `pachirisu` | 1,185 | - | - | - |
| `parasect` | 1,150 | - | - | - |
| `pikachu` | 4,410 | - | - | - |
| `pinsir` | 1,806 | - | - | - |
| `planet_puzzle_league` | 2,193 | - | - | - |
| `pocket_monsters_stadium` | 973 | - | - | - |
| `pokemon-_arceus_and_the_jewel_of_life` | 1,325 | - | - | - |
| `pokemon-_destiny_deoxys` | 1,214 | - | - | - |
| `pokemon-_giratina_-_the_sky_warrior` | 1,092 | - | - | - |
| `pokemon-_jirachi-_wish_maker` | 1,026 | - | - | - |
| `pokemon-_let-s_go-_pikachu-_and_let-s_go-_eevee` | 2,104 | - | - | - |
| `pokemon-_lucario_and_the_mystery_of_mew` | 1,334 | - | - | - |
| `pokemon-_magikarp_jump` | 794 | - | - | - |
| `pokemon-_mewtwo_strikes_back_evolution` | 1,086 | - | - | - |
| `pokemon-_the_first_movie` | 3,840 | - | - | - |
| `pokemon-_the_rise_of_darkrai` | 1,648 | - | - | - |
| `pokemon-_twilight_wings` | 235 | - | - | - |
| `pokemon-_wild_card` | 216 | - | - | - |
| `pokemon_-tv_series` | 5,632 | - | - | - |
| `pokemon_-video_game_series` | 6,040 | - | - | - |
| `pokemon_3-_the_movie` | 1,393 | - | - | - |
| `pokemon_4ever` | 1,890 | - | - | - |
| `pokemon_apokelypse` | 1,812 | - | - | - |
| `pokemon_art_academy` | 564 | - | - | - |
| `pokemon_bank` | 471 | - | - | - |
| `pokemon_battle_revolution` | 1,009 | - | - | - |
| `pokemon_battle_trozei` | 533 | - | - | - |
| `pokemon_black_2_and_white_2` | 1,994 | - | - | - |
| `pokemon_black_and_white` | 5,319 | - | - | - |
| `pokemon_brilliant_diamond_and_shining_pearl` | 1,432 | - | - | - |
| `pokemon_cafe_remix` | 568 | - | - | - |
| `pokemon_card_gb2` | 1,389 | - | - | - |
| `pokemon_champions` | 647 | - | - | - |
| `pokemon_channel` | 1,991 | - | - | - |
| `pokemon_chronicles` | 858 | - | - | - |
| `pokemon_colosseum` | 3,085 | - | - | - |
| `pokemon_concierge` | 1,550 | - | - | - |
| `pokemon_conquest` | 1,076 | - | - | - |
| `pokemon_crystal` | 2,065 | - | - | - |
| `pokemon_dash` | 662 | - | - | - |
| `pokemon_diamond_and_pearl` | 4,688 | - | - | - |
| `pokemon_duel` | 1,545 | - | - | - |
| `pokemon_emerald` | 2,333 | - | - | - |
| `pokemon_evolutions` | 103 | - | - | - |
| `pokemon_firered_and_leafgreen` | 2,571 | - | - | - |
| `pokemon_friends` | 1,057 | - | - | - |
| `pokemon_generations` | 85 | - | - | - |
| `pokemon_go` | 9,670 | - | - | - |
| `pokemon_go_live_events` | 3,089 | - | - | - |
| `pokemon_gold_and_silver` | 3,435 | - | - | - |
| `pokemon_heartgold_and_soulsilver` | 2,673 | - | - | - |
| `pokemon_heroes` | 1,965 | - | - | - |
| `pokemon_home` | 2,064 | - | - | - |
| `pokemon_legends-_arceus` | 2,166 | - | - | - |
| `pokemon_legends-_z-a` | 2,607 | - | - | - |
| `pokemon_masters_ex` | 642 | - | - | - |
| `pokemon_mini` | 1,976 | - | - | - |
| `pokemon_mystery_dungeon` | 1,291 | - | - | - |
| `pokemon_mystery_dungeon-_blue_rescue_team_and_red_rescue_team` | 1,985 | - | - | - |
| `pokemon_mystery_dungeon-_explorers_of_sky` | 2,087 | - | - | - |
| `pokemon_mystery_dungeon-_explorers_of_time_and_explorers_of_dark` | 2,215 | - | - | - |
| `pokemon_mystery_dungeon-_gates_to_infinity` | 746 | - | - | - |
| `pokemon_mystery_dungeon-_rescue_team_dx` | 729 | - | - | - |
| `pokemon_omega_ruby_and_alpha_sapphire` | 1,068 | - | - | - |
| `pokemon_origins` | 133 | - | - | - |
| `pokemon_photo_booth` | 2,065 | - | - | - |
| `pokemon_picross` | 945 | - | - | - |
| `pokemon_pikachu` | 592 | - | - | - |
| `pokemon_pinball` | 833 | - | - | - |
| `pokemon_pinball-_ruby_-_sapphire` | 1,935 | - | - | - |
| `pokemon_platinum` | 3,495 | - | - | - |
| `pokemon_pokopia` | 1,253 | - | - | - |
| `pokemon_puzzle_challenge` | 1,124 | - | - | - |
| `pokemon_puzzle_league` | 1,271 | - | - | - |
| `pokemon_quest` | 1,098 | - | - | - |
| `pokemon_ranger` | 2,111 | - | - | - |
| `pokemon_ranger-_guardian_signs` | 760 | - | - | - |
| `pokemon_ranger-_shadows_of_almia` | 1,583 | - | - | - |
| `pokemon_ranger_and_the_temple_of_the_sea` | 1,064 | - | - | - |
| `pokemon_red-_blue-_and_yellow` | 6,022 | - | - | - |
| `pokemon_ruby_and_sapphire` | 3,678 | - | - | - |
| `pokemon_rumble` | 839 | - | - | - |
| `pokemon_rumble_blast` | 648 | - | - | - |
| `pokemon_rumble_rush` | 410 | - | - | - |
| `pokemon_rumble_u` | 659 | - | - | - |
| `pokemon_rumble_world` | 1,036 | - | - | - |
| `pokemon_scarlet_and_violet` | 4,613 | - | - | - |
| `pokemon_shuffle` | 713 | - | - | - |
| `pokemon_sleep` | 693 | - | - | - |
| `pokemon_smile` | 1,095 | - | - | - |
| `pokemon_snap` | 3,151 | - | - | - |
| `pokemon_stadium` | 2,596 | - | - | - |
| `pokemon_stadium_2` | 1,800 | - | - | - |
| `pokemon_sun_and_moon` | 3,149 | - | - | - |
| `pokemon_super_mystery_dungeon` | 1,296 | - | - | - |
| `pokemon_sword_and_shield` | 4,316 | - | - | - |
| `pokemon_tcg_online` | 609 | - | - | - |
| `pokemon_the_movie-_blackvictini_and_reshiram_and_whitevictini_an` | 1,677 | - | - | - |
| `pokemon_the_movie-_diancie_and_the_cocoon_of_destruction` | 1,217 | - | - | - |
| `pokemon_the_movie-_genesect_and_the_legend_awakened` | 1,161 | - | - | - |
| `pokemon_the_movie-_hoopa_and_the_clash_of_ages` | 1,070 | - | - | - |
| `pokemon_the_movie-_i_choose_you` | 2,261 | - | - | - |
| `pokemon_the_movie-_kyurem_vs._the_sword_of_justice` | 1,448 | - | - | - |
| `pokemon_the_movie-_secrets_of_the_jungle` | 1,216 | - | - | - |
| `pokemon_the_movie-_the_power_of_us` | 1,763 | - | - | - |
| `pokemon_the_movie-_volcanion_and_the_mechanical_marvel` | 1,474 | - | - | - |
| `pokemon_the_movie_2000` | 1,498 | - | - | - |
| `pokemon_trading_card_game_-video_game` | 1,392 | - | - | - |
| `pokemon_trading_card_game_pocket` | 1,989 | - | - | - |
| `pokemon_trozei` | 1,218 | - | - | - |
| `pokemon_ultra_sun_and_ultra_moon` | 1,950 | - | - | - |
| `pokemon_unite` | 1,326 | - | - | - |
| `pokemon_video_game_series_competitive_play` | 3,563 | - | - | - |
| `pokemon_winds_and_waves` | 198 | - | - | - |
| `pokemon_x_and_y` | 3,944 | - | - | - |
| `pokemon_xd-_gale_of_darkness` | 1,099 | - | - | - |
| `pokemonzoroark-_master_of_illusions` | 1,902 | - | - | - |
| `pokepark_2-_wonders_beyond` | 757 | - | - | - |
| `pokepark_wii-_pikachu-s_adventure` | 595 | - | - | - |
| `poketoon` | 114 | - | - | - |
| `pokken_tournament` | 1,036 | - | - | - |
| `popplio-_brionne-_and_primarina` | 1,499 | - | - | - |
| `primarina` | 1,496 | - | - | - |
| `professor_oak` | 2,992 | - | - | - |
| `psyduck` | 1,361 | - | - | - |
| `puzzle_league` | 856 | - | - | - |
| `raichu` | 2,172 | - | - | - |
| `regi_-pokemon` | 2,192 | - | - | - |
| `regice` | 2,191 | - | - | - |
| `regidrago` | 2,191 | - | - | - |
| `regieleki` | 2,191 | - | - | - |
| `regigigas` | 2,191 | - | - | - |
| `regirock` | 2,191 | - | - | - |
| `registeel` | 2,191 | - | - | - |
| `rika_-pokemon` | 1,214 | - | - | - |
| `scorbunny` | 1,653 | - | - | - |
| `serena_-pokemon` | 1,498 | - | - | - |
| `shedinja` | 1,450 | - | - | - |
| `slowpoke` | 2,489 | - | - | - |
| `smeargle` | 2,956 | - | - | - |
| `snorlax` | 1,438 | - | - | - |
| `sobble` | 1,238 | - | - | - |
| `sprigatito-_floragato-_and_meowscarada` | 1,127 | - | - | - |
| `squirtle` | 1,342 | - | - | - |
| `starmie` | 3,452 | - | - | - |
| `sudowoodo` | 2,006 | - | - | - |
| `talonflame` | 1,703 | - | - | - |
| `team_rocket` | 1,346 | - | - | - |
| `team_skull` | 1,515 | - | - | - |
| `tetris_attack` | 1,386 | - | - | - |
| `tinkaton` | 1,371 | - | - | - |
| `typhlosion` | 1,416 | - | - | - |
| `unown` | 1,540 | - | - | - |
| `victini` | 1,314 | - | - | - |
| `voltorb` | 2,157 | - | - | - |
| `weezing` | 1,506 | - | - | - |
| `wobbuffet` | 2,122 | - | - | - |
| `wooloo` | 1,584 | - | - | - |
| `wooper` | 1,470 | - | - | - |
| `zoroark` | 2,283 | - | - | - |

## Not added in the last run

Nothing was left out.

## What to check by eye

Ingest cleans text by rules, and rules miss things.
Take five minutes to open the shortest, a middle one and the longest document next to its original and read one page of each.

- Search the documents for `þ`, `¼`, `(cid:` and the replacement character.
  A hit usually means the PDF's font map is wrong, which no tool can repair, so treat it as a defect and leave that document out.
- Look at the end of a few papers.
  Ingest drops a trailing reference list when it finds a References heading or a run of numbered entries.
  A paper whose list has neither can keep it, and then every author and journal name matches queries it should not.
- Open the first lines of a few documents.
  Author lists, copyright pages and tables of contents are not removed automatically, and you may want to cut them.
- Compare one table with the PDF.
  A PDF prints footnote marks as small raised digits, and the converter glues them onto the word or number next to them: `ALUMINUM1` is the heading ALUMINUM with footnote 1, and `11210,000` can be 210,000 with footnote 11.
  Quotes still match the stored text, but a number read from it can be wrong, so check before you trust a figure in a query, a judgment or an answer.
- Fix the `license` column in the manifest for every document, then run `uv run p2 license`.
  It is `unknown` until you do, and `unknown` does not pass.

## If a document is flagged as scanned

A scan is a picture of a page, so there is no text for ingest to read.
This template does not install an OCR tool, because it is large and most students never need it.
If you do need one, the opt-in route is pymupdf4llm with rapidocr, run on its own outside the template's environment:

```
uv run --no-project --with pymupdf4llm --with rapidocr python -c "import pymupdf4llm, sys, pathlib; pathlib.Path(sys.argv[2]).write_text(pymupdf4llm.to_markdown(sys.argv[1], use_ocr=True, force_ocr=True), encoding='utf-8')" scan.pdf scan.md
```

Put the resulting `.md` file in your folder and ingest the folder again.
It costs about 2 seconds a page, and OCR text needs a second look: it misreads ligatures, hyphens and numbers.
pymupdf4llm is AGPL-3.0 software, so use it only as a tool on your own machine, and do not add it to this repo's dependencies or copy its code into the repo.
