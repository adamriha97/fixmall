# <p style="text-align: center;">FixMall ULTIMATE <sub>AAD edition</sub><p>

_FixMall_ is a program designed to modify XML files downloaded from the [AAD](https://www.aad.sk/) portal. In this program, it is possible to __complete__ missing car prices using [linear interpolation](https://en.wikipedia.org/wiki/Linear_interpolation). Additionally, the program allows for __editing__ prices of selected _brands_, _models_, and age _ranges_ by multiplying them by a chosen coefficient.

---

## Running the Program

Upon launching the program, only the `Load XML` (`Nahrát XML`) button is functional. Upon clicking it, a window will appear for the user to select an XML file downloaded from the [AAD](https://www.aad.sk/) website. After loading the file, other program options will become accessible.


---

## Modifying the Name for the New File

The program does not modify the uploaded XML file but creates a new XML file in the same folder from which the original XML file was uploaded. The user can choose the name for this new file in the `New File Name` (`Název nového souboru`) section using a text field. When the checkbox is selected, the name of the uploaded XML file will be used as a prefix for the new XML file. The default setting includes the prefix and the suffix `_updated`.

> Example: If the name of the uploaded file is `output`, the following options are available for the new file name:
> - [x] output + `_updated` ... the new file name will be `output_updated`
> - [x] output + `-new` ... the new file name will be `output-new`
> - [ ] output + `newXML` ... the new file name will be `newXML`

---

## Creating a New XML File with Filled Data

To create a new XML file with only the filled vehicle price data using [linear interpolation](https://en.wikipedia.org/wiki/Linear_interpolation), simply click the `Fill XML` (`Doplnit XML`) button. This will create a new XML file that preserves all the prices already present in the original XML file and fills in the missing prices for all age years lower than the highest age year in the original XML file.

> Example:
>
> Original XML file:
> | **Year** |   2023   | 2022 | 2021 |   2020   | 2019 |   2018   | 2017 |
> |:-------:|:-----:|:-:|:-:|:-----:|:-:|:-----:|:-:|
> | **Prices** | 5000 |   |   | 2000 |   | 1000 |   |
>
> Filled XML file:
> | **Year** |   2023   | 2022 | 2021 |   2020   | 2019 |   2018   | 2017 |
> |:-------:|:-----:|:-----------:|:-----------:|:-----:|:-----------:|:-----:|:-:|
> | **Prices** | 5000 | **_4000_** | **_3000_** | 2000 | **_1500_** | 1000 |   |

---


## Creating a New XML File with Modified Data

To create a new XML file with only the modified already filled vehicle price data, simply click the `Modify XML` (`Upravit XML`) button. This will create a new XML file with all the prices adjusted according to the modifications chosen by the user in the lower section of the program.

You can modify the prices of all vehicles, vehicles of a specific brand (using the `Brand` (`Značka`) filter), or vehicles of a specific model (using the `Model` filter). You can also specify a range of years for which the modification should be applied (using the `From` (`Od`) and `To` (`Do`) filters, inclusive). The final part of the modification is the `Coefficient` (`Koeficient`), which is used to adjust the prices. The selected `coefficient` value is multiplied by all the prices that meet the previous modification criteria.

To apply the modification, it needs to be added to the `Current Modifications` (`Aktuální úpravy`) section. This can be done by clicking the `Add Modification` (`Přidat úpravu`) button. The most recent modification can be removed using the `Remove Last Modification` (`Vymazat poslední úpravu`) button. All modifications can be cleared using the `Clear All Modifications` (`Vymazat všechny úpravy`) button. By clicking the `Modify XML` (`Upravit XML`) button, a new XML file will be created, incorporating all the modifications from the `Current Modifications` (`Aktuální úpravy`) section.

---

## Ultimate Function

To create a new XML file with both filled and modified data, you can use the `Ultimate XML` button.


<p align="center">
  <img src="https://raw.githubusercontent.com/adamriha97/fixmall/main/icon_fixmall.ico" />
</p>