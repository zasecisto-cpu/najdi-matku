# Najdi královnu 👑

Postřehová 2D hra v prohlížeči, optimalizovaná pro mobilní zařízení. Vaším úkolem je v roli včelaře co nejrychleji najít včelí královnu (Matku) v obrovském rojícím se úlu plném dělnic a trubců.

## 🎮 Vlastnosti hry
* **Tři úrovně obtížnosti**:
  * **Začátečník**: Královna je vždy vidět uprostřed obrazovky, nízké riziko schování pod jinou včelou, stres začíná po 30s nebo 5 chybách.
  * **Pokročilý**: Královna se může zrodit mimo obrazovku (45 % šance), začíná schovaná v 60 % případů, stres po 20s nebo 3 chybách.
  * **Profesionál**: Královna se zrodí mimo obrazovku v 90 % případů, začíná schovaná v 95 % případů, stres po 10s nebo 2 chybách.
* **Fyzika a animace**: Plynulé posouvání úlu (panning) s setrvačností, realistické animace chůze nožiček a třepotání křídel včel.
* **Stresový systém**: Pokud královnu nenajdete včas nebo příliš klikáte vedle, obraz se začne třást, rozmazávat a ztemňovat, což ztěžuje hledání.
* **Tabulka nejlepších výsledků (Leaderboard)**: Možnost zapsat svůj čas a porovnat se s ostatními hráči (s označením obtížnosti jako `(BEG)`, `(ADV)` nebo `(PRO)`).
* **Zvukové efekty**: Generované procedurálně přímo v prohlížeči pomocí Web Audio API (netřeba stahovat žádné audio soubory).

## 🚀 Jak spustit hru lokálně

Pro spuštění hry s funkční tabulkou výsledků je potřeba mít nainstalovaný **Python 3**.

1. Naklonujte nebo stáhněte tento repozitář.
2. Otevřete terminál (příkazový řádek) ve složce s projektem.
3. Spusťte vestavěný Python server:
   ```bash
   python3 server.py
   ```
4. Otevřete ve svém internetovém prohlížeči adresu:
   **[http://localhost:8080](http://localhost:8080)**

## 📁 Struktura souborů
* `index.html` - Hlavní soubor hry obsahující kompletní kód (Canvas engine, grafické styly, herní logiku, Web Audio a rozhraní).
* `server.py` - Jednoduchý Python backend zajišťující statický web server a API pro zápis/čtení skóre.
* `leaderboard.json` - Databáze výsledků uložená ve formátu JSON.
* `Delnice.png` - Grafika včely dělnice.
* `Trubec.png` - Grafika trubce.
* `Matka.png` - Grafika královny (matky).

## 🛠️ Použité technologie
* **Frontend**: HTML5 Canvas, Vanilla Javascript (ES6), CSS Custom Properties (skleněný design / glassmorphism).
* **Audio**: Web Audio API (procedurální syntezátor pro zvuky kliknutí, chyb a vítězství).
* **Backend**: Python (standardní knihovny `http.server` a `json`).
