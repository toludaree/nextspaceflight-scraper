# Next SpaceFlight Scraper

This project is part of [Project Upwork](https://github.com/toludaree/project-upwork). This is the job [link](https://www.upwork.com/jobs/~01f82febe982663029).

## Job Description
I want to get all of the data listed on this website:
https://nextspaceflight.com/launches/past/?page=1&search=

I want the data on all of the pages, roughly ~7000 and for each of the flight I want the following:
Organisation
Location
Datetime
Details
Price
Status
Mission_Status

I want all of the data and also a python script, I want someone to do it within 4-6 hours. All of the data and the python script.
Also I don't want the script to open the browser and then scrape I want it to run in the background.

## Result Schema
- organization - name of company that handled the flight e.g SpaceX
- location - location the flight was launched
- datetime - date of flight launch
- details - some flight details
    - name - name of spaceship
    - mission_details
    - payloads - number of payloads of spaceship
    - total_mass - total mass of spaceship
    - orbit_type - orbit type of spaceship
- price - price of spaceship
- status - status of spaceship e.g Active
- mission_status - status of mission e.g Partial Failure

## Example Data (in JSON)
```json
{
    "organization": "SpaceX",
    "location": "SLC-40, Cape Canaveral SFS, Florida, USA",
    "datetime": "Mon Jul 08, 2024 23:30 UTC",
    "details": {
        "name": "Türksat 6A",
        "mission_details": "First communication geostationary satellite built in Turkey. (Some payloads are Canadian)\nTürksat 6A is a satellite that will provide data relay for civil and military communications to the Anatolian peninsula as well as most of the European continent, the Middle East, and the westernmost part of the Russian federation.\nThe satellite is equipped with 16(+4) Ku-band and 2(+1) X-band transponders. (reserve)",
        "payloads": "1",
        "total_mass": "4,250.0 kg",
        "orbit_type": "Geostationary Transfer Orbit"
    },
        "price": "$69.75 million",
        "status": "Active",
        "mission_status": "Success"
}
```

## Evolution
I used only Scrapy for this project and didn't need an automated browser.

## Reproducing

### Requirements
- Python (>= 3.10)

### Setup
- Clone the reposiory
    ```bash
    git clone https://github.com/toludaree/nextspaceflight-scraper.git
    ```
- Create a python virtual environment and activate it.
    ```bash
    python -m venv .venv

    # Activate
    .venv/Scripts/activate     # Windows
    source .venv/bin/activate  # Unix
    ```
- Install required libararies through  [requirements.txt](./requirements.txt)
    ```bash
    pip install -r requirements.txt
    ```

### Scrape away
- Naviagte to the [nextspaceflight](./nextspaceflight/) directory.
    ```bash
    cd nextspaceflight/
    ```
- Activate the `flights` spider with `scrapy crawl`.
    ```bash
    scrapy crawl flights -O flights.json
    ```
    - This saves the result as a JSON file. You can also save as a CSV or XML file.

