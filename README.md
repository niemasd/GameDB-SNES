# GameDB-SNES
Super Nintendo Entertainment System (SNES), part of [GameDB](https://github.com/niemasd/GameDB).

## Structured Downloads
* **[`SNES.data.json`](https://github.com/niemasd/GameDB-SNES/releases/latest/download/SNES.data.json):** All data, structured in the JSON format
* **[`SNES.data.tsv`](https://github.com/niemasd/GameDB-SNES/releases/latest/download/SNES.data.tsv):** All data, structured in the TSV format
* **[`SNES.release_dates.pdf`](https://github.com/niemasd/GameDB-SNES/releases/latest/download/SNES.release_dates.pdf):** Histogram of release dates, stratified by region
* **[`SNES.titles.json`](https://github.com/niemasd/GameDB-SNES/releases/latest/download/SNES.titles.json):** Mapping of serial numbers to game titles, structured in the JSON format

# Notes

* SNES games don't have unique internal game IDs or serial numbers, so the game folders within [`games`](games) are named with a unique ID as follows:
    * The first field is the **developer ID**
    * The second field is the **internal title**, but with special characters replaced with `_`
        * Some games have internal titles that are not human-readable strings, so for those, I represent the internal title as a hex string starting with `0x`
    * The third field is the **ROM version**
    * The fourth field is the **checksum**
    * The fields are delimited using `.....` (i.e., 5 space characters)

# Sources
* [GameID](https://github.com/niemasd/GameID)
