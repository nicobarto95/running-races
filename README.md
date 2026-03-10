# 🏃💨 Running Races | Data Vault

This project provides an automated, up-to-date calendar of major global running events, maintained automatically via GitHub Actions.

## 🔗 Live Dashboard
You can view the interactive version here: https://nicobarto95.github.io/running-races/

---

## 📅 Race Calendar Overview

The table below is updated automatically every day at 04:00 UTC.

This entire line, and everything between the markers, will be replaced by the Python script with the updated table and statistics. **Do not modify the content between the two markers.**

Start Tables

| 📊 Statistics | Value |
| :--- | :--- |
| Total Races | **22** |
| Open Registrations | **13** |
| World Majors | **6** |

***
* Last automatic update: **2026-03-10 05:10:48 UTC**


| Date        | Race                                       | city              | Country        | Distances   | Price              | Status            | Link                                                                             |
|:------------|:-------------------------------------------|:------------------|:---------------|:------------|:-------------------|:------------------|:---------------------------------------------------------------------------------|
| 25 Jan 2026 | **Standard Chartered Dubai Marathon**      | Dubai             | UAE            | 42K, 21K    | €100 - €120        | ✅ Open            | [🌐 Sito](https://www.dubaimarathon.org)                                          |
| 15 Feb 2026 | **Kyoto Marathon**                         | Kyoto             | Japan          | 42K         | ¥15,000            | ❌ Sold Out        | [🌐 Sito](https://www.kyoto-marathon.com)                                         |
| 15 Feb 2026 | **Seville Marathon**                       | Seville           | Spain          | 42K         | €75                | ❌ Sold Out        | [🌐 Sito](https://www.zurichmaratonsevilla.es)                                    |
| 01 Mar 2026 | **Tokyo Marathon** 🏆 WMM                   | Tokyo             | Japan          | 42K         | ¥18,000            | ❌ Sold Out        | [🌐 Sito](https://www.marathon.tokyo)                                             |
| 15 Mar 2026 | **RomaOstia Half Marathon**                | Roma              | Italy          | 21K         | €40                | ✅ Open            | [🌐 Sito](https://www.romaostia.it)                                               |
| 12 Apr 2026 | **Schneider Electric Marathon de Paris**   | Parigi            | France         | 42K         | Charity            | ❌ Charity Entries | [🌐 Sito](https://www.parismarathon.com)                                          |
| 12 Apr 2026 | **Hannover Marathon**                      | Hannover          | Germany        | 42K, 21K    | €90                | ✅ Open            | [🌐 Sito](https://www.marathon-hannover.de/landingpage.html)                      |
| 13 Apr 2026 | **Boston Marathon** 🏆 WMM                  | Boston            | USA            | 42K         | $200 - $250        | ❌ Sold Out        | [🌐 Sito](https://www.baa.org)                                                    |
| 19 Apr 2026 | **Connemara International Marathon**       | Connemara, Galway | Ireland        | 42K         | €70                | ✅ Open            | [🌐 Sito](https://www.connemarathon.com/)                                         |
| 26 Apr 2026 | **Maratona di Londra** 🏆 WMM               | Londra            | UK             | 42K         | £80                | ❌ Sold Out        | [🌐 Sito](https://www.tcslondonmarathon.com)                                      |
| 03 May 2026 | **Prague Marathon**                        | Prague            | Czech Republic | 42K         | €120 (2,900.00 Kč) | ✅ Open            | [🌐 Sito](https://www.runczech.com/en)                                            |
| 03 May 2026 | **ColleMar-athon**                         | Fano              | Italy          | 42K         | €30                | ✅ Open            | [🌐 Sito](https://www.collemar-athon.com/)                                        |
| 14 Jun 2026 | **Phnom Penh International Half Marathon** | Phnom Penh        | Cambodia       | 21K         | $40                | ✅ Open            | [🌐 Sito](https://www.phnompenhmarathon.org)                                      |
| 27 Sep 2026 | **Baxter Lockness Marathon**               | Inverness         | UK             | 42K         | £60                | ✅ Open            | [🌐 Sito](https://lochnessmarathon.com/)                                          |
| 27 Sep 2026 | **BMW Berlin Marathon** 🏆 WMM              | Berlino           | Germany        | 42K         | €190               | ❌ Sold Out        | [🌐 Sito](https://www.bmw-berlin-marathon.com)                                    |
| 10 Oct 2026 | **Lisbon Marathon**                        | Lisbona           | Portugal       | 42K         | €70 - €90          | ✅ Open            | [🌐 Sito](https://maratonaclubedeportugal.com/en/prova/edp-lisbon-marathon-2026/) |
| 11 Oct 2026 | **Bank of America Chicago Marathon** 🏆 WMM | Chicago           | USA            | 42K         | $240               | ❌ Sold Out        | [🌐 Sito](https://www.chicagomarathon.com)                                        |
| 18 Oct 2026 | **TCS Amsterdam Marathon**                 | Amsterdam         | Netherlands    | 42K, 21K    | €95 - €125         | ✅ Open            | [🌐 Sito](https://www.tcsamsterdammarathon.eu)                                    |
| 25 Oct 2026 | **Venice Marathon**                        | Venezia           | Italy          | 42K, 21K    | €70 - €100         | ✅ Open            | [🌐 Sito](https://www.venicemarathon.it)                                          |
| 01 Nov 2026 | **TCS New York City Marathon** 🏆 WMM       | New York City     | USA            | 42K         | $295 - $350        | ❌ Sold Out        | [🌐 Sito](https://www.nycmarathon.org)                                            |
| 29 Nov 2026 | **Amazing Thailand Marathon Bangkok**      | Bangkok           | Thailand       | 42K, 21K    | ฿1,500 - ฿2,000    | ✅ Open            | [🌐 Sito](https://amazingthailandmarathon.com)                                    |
| 06 Dec 2026 | **Valencia Marathon Trinidad Alfonso**     | Valencia          | Spain          | 42K         | €80 - €120         | ✅ Open            | [🌐 Sito](https://www.maratonvalencia.com)                                        |


End Tables

## 🛠️ Project Structure
* **data/gare.json:** The single source of truth for race information.
* **index.html:** The interactive web dashboard (for GitHub Pages).
* **scripts/build_readme.py:** The script that generates the table above.