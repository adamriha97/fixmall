# <p style="text-align: center;">FixMall ULTIMATE <sub>AAD edition</sub><p>

_FixMall_ je program sloužící k úpravě XML souborů stahovaných z portálu [AAD](https://www.aad.sk/). Lze v něm __doplňovat__ chybějící ceny vozů za pomoci [lineární interpolace](https://cs.wikipedia.org/wiki/Line%C3%A1rn%C3%AD_interpolace). Dále program umožňuje __upravovat__ ceny vybraných _značek_, popřípadě _modelů_ a intervalu _stáří_ pomocí pronásobení zvoleným koeficientem.

---

## Spuštění programu

Po spuštění programu je funkční pouze tlačítko `Nahrát XML`, po jehož stisknutí vyskočí okno, ve které uživatel vybere XML soubor, který stáhl ze stránek [AAD](https://www.aad.sk/). Po nahrání se zpřístupní ostatní možnosti programu.

---

## Úprava názvu pro nový soubor

Program neupravuje nahraný XML soubor, ale vytváří nový XML soubor ve stejné složce, ze které byl původní XML soubor nahrán. Název pro tento nový soubor si může uživatel zvolit v sekci `Název nového souboru` v textovém poli. Při zaškrtnutí boxu bude použit název nahraného XML souboru jako prefix pro název nového XML souboru. Výchozí nastavení je včetně prefixu a dodatkem `_updated`.

> Příklad: Bude-li název nahraného souboru `vystup`, pak jsou tyto možnosti pro název nového souboru:
> - [x] vystup + `_updated` ... název nového souboru bude `vystup_updated`
> - [x] vystup + `-new` ... název nového souboru bude `vystup-new`
> - [ ] vystup + `newXML` ... název nového souboru bude `newXML`

---

## Vytvoření nového XML souboru s doplněnými daty

Pro vytvoření nového XML souboru, který bude mít pouze doplněná data cen vozidel na chybějících místech pomocí [lineární interpolace](https://cs.wikipedia.org/wiki/Line%C3%A1rn%C3%AD_interpolace), stačí kliknout na tlačítko `Doplnit XML`. Tímto se vytvoří nový XML soubor, který bude mít zachované všechny ceny, které již byly v původním XML souboru a doplní chybějící ceny pro všechny roky stáří, které jsou nižší než nejvyšší rok stáří v původním XML souboru.

> Příklad:
> 
> Původní XML soubor:
> | **Rok** |   2023   | 2022 | 2021 |   2020   | 2019 |   2018   | 2017 |
> |:---------:|:-----:|:-:|:-:|:-----:|:-:|:-----:|:-:|
> |  **Ceny** | 5000 |   |   | 2000 |   | 1000 |   |
>
> Doplněný XML soubor:
> | **Rok** |   2023   | 2022 | 2021 |   2020   | 2019 |   2018   | 2017 |
> |:---------:|:-----:|:-----------:|:-----------:|:-----:|:-----------:|:-----:|:-:|
> |  **Ceny** | 5000 | **_4000_** | **_3000_** | 2000 | **_1500_** | 1000 |   |

---

## Vytvoření nového XML souboru s upravenými daty

Pro vytvoření nového XML souboru, který bude mít pouze upravená již vyplněná data cen vozidel, stačí kliknout na tlačítko `Upravit XML`. Tímto se vytvoří nový XML soubor, který bude mít upraveny všechny ceny podle toho, jaké úpravy si uživatel navolí ve spodní části programu.

Upravit lze ceny všech vozidel, vozidel konkrétní značky (filtr `Značka`), nebo jen vozidel konkrétního modelu (filtr `Model`). Do úpravy lze také přidat rozmezí let, v jakých se má úprava provést (filtry `Od` a `Do`, filtr platí včetně). Poslední část úpravy je `Koeficient`, podle kterého se daná úprava procede tak, že volenou hodnotou `koeficientu` se pronásobí včechny ceny, které vyhovují přechozí volbě úpravy.

Aby bala úprava provedena, musí být přidána do sekce `Aktuální úpravy`. To se provede tlačítkem `Přidat úpravu`. Poslední přidanou úpravu můžete odstranit tlačítkem `Vymazat poslední úpravu`. Všechny úpravy pak můžete odstranit tlačítkem `Vymazat všechny úpravy`. Stiskem tlačítka `Upravit XML` se pak vytvoří nový XML soubor, do kterého se propíší všechny úpravy ze sekce `Aktuální úpravy`.

---

## Ultimate funkce

Vytvoření nového XML souboru s doplněnými a zároveň upravenými daty můžete provést stiskem tlačítka `Ultimate XML`. Nejprve proběhne doplnění, až poté proběhne úprava, což může být důležité v případě, že se upravuje jen určitý interval stáří pomocí `Od` a `Do`.

---

## Foto funkce

Pokud máte ve složce s nahraným XML souborem přítomnou složku `pic` s obrázky jednotlivých automobilů (tato složka je přítomna v `zip` souboru, který se stahuje z [AAD](https://www.aad.sk/)), pak se po výběru konkrétního `Modelu` aktivuje tlačítko `Foto`. Po jeho stisku se objeví další okno, ve kterém lze pomoví tlačítek `<` a `>` přepínat informace a fotky jednotlivých variant daného `Modelu`.

<p align="center">
  <img src="https://raw.githubusercontent.com/adamriha97/fixmall/main/icon_fixmall.ico" />
</p>