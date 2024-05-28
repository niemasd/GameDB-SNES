# GameDB-SNES
Super Nintendo Entertainment System (SNES), part of [GameDB](https://github.com/niemasd/GameDB).

## Structured Downloads
* **[`SNES.data.json`](https://github.com/niemasd/GameDB-SNES/releases/latest/download/SNES.data.json):** All data, structured in the JSON format
* **[`SNES.data.tsv`](https://github.com/niemasd/GameDB-SNES/releases/latest/download/SNES.data.tsv):** All data, structured in the TSV format
* **[`SNES.release_dates.pdf`](https://github.com/niemasd/GameDB-SNES/releases/latest/download/SNES.release_dates.pdf):** Histogram of release dates, stratified by region
* **[`SNES.titles.json`](https://github.com/niemasd/GameDB-SNES/releases/latest/download/SNES.titles.json):** Mapping of serial numbers to game titles, structured in the JSON format

# Notes

## Uniquely Identifying Games

SNES games don't have unique internal game IDs or serial numbers. The following 4 fields can be used to uniquely identify a game:

1. The **Internal Title**, which is at offsets `0x00` through `0x19` (inclusive) of the [ROM header](https://snes.nesdev.org/wiki/ROM_header#Cartridge_header)
2. The **Developer ID**, which is at offset `0x1A` of the [ROM header](https://snes.nesdev.org/wiki/ROM_header#Cartridge_header)
3. The **ROM Version**, which is at offset `0x1B` of the [ROM header](https://snes.nesdev.org/wiki/ROM_header#Cartridge_header)
4. The **Checksum** (see [calculation code](https://github.com/niemasd/GameID/blob/d038079574c2679de8f437101bcea056b9114646/GameID.py#L391-L411))

The game folders within [`games`](games) are named as follows (i.e., these 4 fields delimited by `.....`):

```
DEVELOPER_ID.....INTERNAL_TITLE.....ROM_VERSION.....CHECKSUM
```

See the [GameID SNES identification code](https://github.com/niemasd/GameID/blob/d038079574c2679de8f437101bcea056b9114646/GameID.py#L384-L474) for implementation details.

# Sources
* [GameID](https://github.com/niemasd/GameID)
