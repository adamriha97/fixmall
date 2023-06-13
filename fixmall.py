import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import os
import datetime
import shutil
import xml.etree.ElementTree as ET
import numpy as np

class Change:
    def __init__(self, koef, manuf, model, start, end):
        self.koef = koef
        self.manuf = manuf
        self.model = model
        self.start = start
        self.end = end

root = tk.Tk()

root.configure(bg="#00234b") #00234b #003876 #ef7a00
root.geometry("800x600")
root.title("FixMall ULTIMATE - AAD edition")

# název
logo_grig = tk.Frame(root, bg="#00234b")
logo_grig.columnconfigure(0, weight=1)
logo_grig.columnconfigure(1, weight=1)

logo = tk.Label(logo_grig, text="FixMall", font=("Impact", 30), bg="#00234b", fg="white")
logo.grid(column=0, row=0, rowspan=2, sticky="w", padx=5, pady=5)

logo_aad = tk.Label(logo_grig, text=("agentúra auto data").upper(), font=("Lexend", 10, "bold"), bg="#00234b", fg="#ef7a00")
logo_aad.grid(column=1, row=0, sticky="e", padx=5, pady=(5,0))

logo_edition = tk.Label(logo_grig, text="EDITION", font=("Lexend", 10, "bold"), bg="#00234b", fg="#ef7a00")
logo_edition.grid(column=1, row=1, sticky="e", padx=5, pady=(0, 5))

logo_grig.pack(fill="x")

# ultimate název
ultimate_grid = tk.Frame(root, bg="#00234b")
ultimate_grid.columnconfigure(0, weight=1)
ultimate_grid.columnconfigure(1, weight=2)
ultimate_grid.columnconfigure(2, weight=2)
ultimate_grid.columnconfigure(3, weight=2)
ultimate_grid.columnconfigure(4, weight=2)
ultimate_grid.columnconfigure(5, weight=2)
ultimate_grid.columnconfigure(6, weight=2)
ultimate_grid.columnconfigure(7, weight=1)
ult_U = tk.Label(ultimate_grid, text="U", font=("Georgia", 15, "bold"), bg="#00234b", fg="white")
ult_U.grid(column=0, row=0, padx=5, pady=(0, 15), sticky="w")
ult_L = tk.Label(ultimate_grid, text="L", font=("Georgia", 15, "bold"), bg="#00234b", fg="#ffe6cc")
ult_L.grid(column=1, row=0, padx=5, pady=(0, 15))
ult_T = tk.Label(ultimate_grid, text="T", font=("Georgia", 15, "bold"), bg="#00234b", fg="#ffcd99")
ult_T.grid(column=2, row=0, padx=5, pady=(0, 15))
ult_I = tk.Label(ultimate_grid, text="I", font=("Georgia", 15, "bold"), bg="#00234b", fg="#ffb266")
ult_I.grid(column=3, row=0, padx=5, pady=(0, 15))
ult_M = tk.Label(ultimate_grid, text="M", font=("Georgia", 15, "bold"), bg="#00234b", fg="#ff9933")
ult_M.grid(column=4, row=0, padx=5, pady=(0, 15))
ult_A = tk.Label(ultimate_grid, text="A", font=("Georgia", 15, "bold"), bg="#00234b", fg="#ff8000")
ult_A.grid(column=5, row=0, padx=5, pady=(0, 15))
ult_T2 = tk.Label(ultimate_grid, text="T", font=("Georgia", 15, "bold"), bg="#00234b", fg="#ff6600")
ult_T2.grid(column=6, row=0, padx=5, pady=(0, 15))
ult_E = tk.Label(ultimate_grid, text="E", font=("Georgia", 15, "bold"), bg="#00234b", fg="#ef7a00")
ult_E.grid(column=7, row=0, padx=5, pady=(0, 15), sticky="e")
ultimate_grid.pack(fill="x")

# název
# label = tk.Label(root, text="AAD XML Solver Ultimate", font=('Arial', 21))
# label.pack(padx=15, pady=15)

def destroyCahngesList():
    global changes_labels
    for i in range(0, len(changes_labels)):
        changes_labels[i][0].destroy()
        changes_labels[i][1].destroy()
        changes_labels[i][2].destroy()
        changes_labels[i][3].destroy()
        changes_labels[i][4].destroy()
        changes_labels[i][5].destroy()
    changes_labels = []

def fillChangesList():
    col = "#00234b" # "#003876"
    for i in range(0, len(changes)):
        changes_labels.append([
            tk.Label(changes_frame, text=str(len(changes)-i), bg=col, fg="white"),
            tk.Label(changes_frame, text=changes[len(changes)-i-1].manuf, bg=col, fg="white"),
            tk.Label(changes_frame, text=changes[len(changes)-i-1].model, bg=col, fg="white"),
            tk.Label(changes_frame, text=changes[len(changes)-i-1].start, bg=col, fg="white"),
            tk.Label(changes_frame, text=changes[len(changes)-i-1].end, bg=col, fg="white"),
            tk.Label(changes_frame, text=changes[len(changes)-i-1].koef, bg=col, fg="white")
        ])
        changes_labels[i][0].grid(row=i + 1, column=0, sticky="we")
        changes_labels[i][1].grid(row=i + 1, column=1, sticky="we")
        changes_labels[i][2].grid(row=i + 1, column=2, sticky="we")
        changes_labels[i][3].grid(row=i + 1, column=3, sticky="we")
        changes_labels[i][4].grid(row=i + 1, column=4, sticky="we")
        changes_labels[i][5].grid(row=i + 1, column=5, sticky="we")
        if col == "#00234b":
            col = "#003876"
        else:
            col = "#00234b"
def addChange():
    destroyCahngesList()
    changes.append(Change(koeficient.get(), znacka.get(), model.get(), od.get(), do.get()))
    changes_frame['text'] = "Aktuální úpravy: " + str(len(changes))
    delete_last_change['state'] = "normal"
    delete_last_change['bg'] = "#ef7a00"
    delete_last_change['fg'] = "white"
    delete_last_change.bind("<Enter>", on_enter)
    delete_last_change.bind("<Leave>", on_leave)
    delete_all_changes['state'] = "normal"
    delete_all_changes['bg'] = "#ef7a00"
    delete_all_changes['fg'] = "white"
    delete_all_changes.bind("<Enter>", on_enter)
    delete_all_changes.bind("<Leave>", on_leave)
    fillChangesList()

def deleteLastChange():
    destroyCahngesList()
    if len(changes) > 0:
        changes.pop()
    changes_frame['text'] = "Aktuální úpravy: " + str(len(changes))
    if len(changes) == 0:
        delete_last_change['state'] = "disabled"
        delete_last_change['bg'] = "#4c2400"
        delete_last_change.unbind("<Enter>")
        delete_last_change.unbind("<Leave>")
        delete_all_changes['state'] = "disabled"
        delete_all_changes['bg'] = "#4c2400"
        delete_all_changes.unbind("<Enter>")
        delete_all_changes.unbind("<Leave>")
    fillChangesList()

def deleteAllChanges():
    global changes
    destroyCahngesList()
    changes = []
    changes_frame['text'] = "Aktuální úpravy: " + str(len(changes))
    delete_last_change['state'] = "disabled"
    delete_last_change['bg'] = "#4c2400"
    delete_last_change.unbind("<Enter>")
    delete_last_change.unbind("<Leave>")
    delete_all_changes['state'] = "disabled"
    delete_all_changes['bg'] = "#4c2400"
    delete_all_changes.unbind("<Enter>")
    delete_all_changes.unbind("<Leave>")

def nactiModely(event):
    global modely
    modely = ["Všechny modely"]
    man_id = ""
    for man_rec in root_orig.find("Manufacturer"):
        if znacka.get() == man_rec.find("Text").text:
            man_id = man_rec.find("ManufacturerID").text
            break
    if man_id != "":
        for mod_rec in root_orig.find("Model"):
            if man_id == mod_rec.find("ManufacturerID").text:
                modely.append(mod_rec.find("Text").text)
    model['values'] = modely
    model.current(0)

def nactiZnacky():
    global znacky, tree, root_orig
    tree = ET.parse(os.path.join(directory, (file_name+".xml")))
    root_orig = tree.getroot()
    znacky = []
    for man_rec in root_orig.find("Manufacturer"):
        znacky.append(man_rec.find("Text").text)
    znacka['values'] = znacky
    znacka.current(0)
    model['state'] = "normal"
    nactiModely(0)
    koeficient['state'] = "normal"
    koeficient.set(1)
    od.current(0)
    do.current(0)
    od['state'] = "normal"
    do['state'] = "normal"
    add_change['state'] = "normal"
    add_change['bg'] = "#ef7a00"
    add_change.bind("<Enter>", on_enter)
    add_change.bind("<Leave>", on_leave)
    delete_last_change['state'] = "disabled"
    delete_last_change['bg'] = "#4c2400"
    delete_last_change.unbind("<Enter>")
    delete_last_change.unbind("<Leave>")
    delete_all_changes['state'] = "disabled"
    delete_all_changes['bg'] = "#4c2400"
    delete_all_changes.unbind("<Enter>")
    delete_all_changes.unbind("<Leave>")

def nahrat_fce():
    global directory, file_name, changes
    # "/Users/adamr/PycharmProjects/AAD_xml_solver_ultimate/"
    root.filename = filedialog.askopenfilename(initialdir="/", title="Vyberte XML", filetypes=(("XML soubory", "*.xml"), ("Všechny soubory", "*.*")))
    if root.filename != "":
        directory = os.path.dirname(root.filename)
        file_name = os.path.splitext(os.path.basename(root.filename))[0]
        nahrat_btn['text'] = file_name.upper()
        doplnit_btn['state'] = "normal"
        doplnit_btn['bg'] = "#ef7a00"
        doplnit_btn['text'] = "Doplnit XML"
        doplnit_btn.bind("<Enter>", on_enter)
        doplnit_btn.bind("<Leave>", on_leave)
        upravit_btn['state'] = "normal"
        upravit_btn['bg'] = "#ef7a00"
        upravit_btn['text'] ="Upravit XML"
        upravit_btn.bind("<Enter>", on_enter)
        upravit_btn.bind("<Leave>", on_leave)
        ultimate_btn['state'] = "normal"
        ultimate_btn['bg'] = "#ef7a00"
        ultimate_btn['text'] ="Ultimate XML"
        ultimate_btn.bind("<Enter>", on_enter)
        ultimate_btn.bind("<Leave>", on_leave)
        prefix_check['state'] = "normal"
        prefix_check['onvalue'] = file_name
        prefix_check['text'] = file_name + " +"
        prefix_check.select()
        prefix_check['state'] = "normal"
        new_file_name_entry['state'] = "normal"
        # file_grid2['state'] = "normal"
        znacka['state'] = "normal"
        destroyCahngesList()
        changes = []
        nactiZnacky()

def interpolate(arr):
    # Create an array of indices for the input array.
    x = np.arange(len(arr))
    # Create an array of values for the input array that are not NaN.
    y = arr[np.logical_not(np.isnan(arr))]
    # Interpolate the missing values using the interp() function.
    return np.interp(x, x[np.logical_not(np.isnan(arr))], y)

def fillXML_old(file, max_year=datetime.datetime.now().year):
    # Load the input XML file
    tree_new = ET.parse(file)
    root_new = tree_new.getroot()
    root_price = root_new.find("Price")

    # Get all unique VehicleIDs from the input XML file
    vehicle_ids = set()
    for vehicle_record in root_new.find("Vehicle"):
        vehicle_ids.add(vehicle_record.find("VehicleID").text)

    n = 0
    v = len(vehicle_ids)

    # Loop through all possible combinations of VehicleID and Year
    for vehicle_id in vehicle_ids:

        # hledání minimálního roku, pro který má dané vehicle_id vyplněnou cenu
        min_year_vehid = max_year
        for price_record in root_new.find("Price"):
            if (price_record.find("VehicleID").text == vehicle_id and int(
                    price_record.find("Year").text) < min_year_vehid):
                min_year_vehid = int(price_record.find("Year").text)

        # vytvoření pole pro hodnoty, jehož délka odpovídá poštu let stáří, pro které chceme hodnotu doplňovat
        values_arr = np.empty(max_year + 1 - min_year_vehid)
        values_arr[:] = np.nan

        # doplnění první hodnoty pole cenou NewPrice z elementu Vehicle a subelementu VehicleRecord pro daté vehicle_id
        for vehicle_record in root_new.find("Vehicle"):
            if (vehicle_record.find("VehicleID").text == vehicle_id):
                values_arr[0] = int(vehicle_record.find("NewPrice").text)
                break

        # doplnění známých hodnot z elementu Price a subelementu PriceRecord pro daté vehicle_id a daný Year
        for price_record in root_new.find("Price"):
            if (price_record.find("VehicleID").text == vehicle_id):
                values_arr[max_year - int(price_record.find("Year").text)] = int(price_record.find("Value").text)

        # doplnění chybějících cen lineární interpolací
        values_arr = interpolate(values_arr)

        # zaokrouhlení cen v poli na stovky
        # for i in range(0, len(values_arr)):
        #    values_arr[i] = round(values_arr[i], -2)

        # doplnění zaokrouhlených (na stovky) cen pro chybějící roky do XML
        for i in range(0, len(values_arr)):
            exists = False
            for price_record in root_new.find("Price"):
                if (price_record.find("VehicleID").text == vehicle_id and int(price_record.find("Year").text) == (
                        max_year - i)):
                    exists = True
                    break
            if not exists:
                new_pricerecord = ET.Element("PriceRecord")
                ET.SubElement(new_pricerecord, "VehicleID").text = vehicle_id
                ET.SubElement(new_pricerecord, "Year").text = str(max_year - i)
                ET.SubElement(new_pricerecord, "Value").text = str(round(round(values_arr[i]), -2))
                root_price.append(new_pricerecord)

        n = n+1
        print(n, "z", v, ",", n/v*100, "%")

    # propsání změn do nového XML dokumentu
    tree_new.write(file)

def fillXML(file, max_year=datetime.datetime.now().year):
    # Load the input XML file
    tree_new = ET.parse(file)
    root_new = tree_new.getroot()
    root_price = root_new.find("Price")
    root_vehicle = root_new.find("Vehicle")
    root_veh_rec = root_vehicle.find("VehicleRecord")

    # hledání maximálního a minimálního VehicleID
    min_vehid = int(root_veh_rec.find("VehicleID").text)
    max_vehid = min_vehid
    for veh_rec in root_vehicle:
        if int(veh_rec.find("VehicleID").text) < min_vehid:
            min_vehid = int(veh_rec.find("VehicleID").text)
        elif int(veh_rec.find("VehicleID").text) > max_vehid:
            max_vehid = int(veh_rec.find("VehicleID").text)

    # vytvoření vektorů, kde index bude posunuté VehicleID tak, že index 0 představuje minimální VehicleID, jeden pro minimální rok, jeden pro NewPrice
    min_year_arr = [int(max_year+1) for _ in range(max_vehid + 1 - min_vehid)] # np.empty(max_vehid + 1 - min_vehid)
    #min_year_arr[:] = np.nan
    new_price_arr = np.empty(max_vehid + 1 - min_vehid)
    new_price_arr[:] = np.nan
    values_arr = [[] for _ in range(max_vehid + 1 - min_vehid)] # np.empty(max_vehid + 1 - min_vehid)
    #values_arr[:] = np.nan
    values_bool_arr = [[] for _ in range(max_vehid + 1 - min_vehid)] # np.empty(max_vehid + 1 - min_vehid)
    #values_bool_arr[:] = np.nan

    # naplnění vytvořených vektorů
    for veh_rec in root_vehicle:
        min_year_arr[int(veh_rec.find("VehicleID").text)-min_vehid] = max_year
        new_price_arr[int(veh_rec.find("VehicleID").text) - min_vehid] = int(veh_rec.find("NewPrice").text)
    for pri_rec in root_price:
        if int(pri_rec.find("Year").text) < min_year_arr[int(pri_rec.find("VehicleID").text)-min_vehid]:
            min_year_arr[int(pri_rec.find("VehicleID").text) - min_vehid] = int(pri_rec.find("Year").text)

    # doplnění pole polí pro existující ceny v daných letech
    for vehid in range(min_vehid, max_vehid + 1):
        if min_year_arr[vehid - min_vehid] != int(max_year+1): # np.nan:*******************************************************************
            # vytvoření pole pro hodnoty, jehož délka odpovídá poštu let stáří, pro které chceme hodnotu doplňovat
            values_arr[vehid - min_vehid] = np.empty(round(max_year + 1 - min_year_arr[vehid - min_vehid]))
            values_arr[vehid - min_vehid][:] = np.nan
            values_bool_arr[vehid - min_vehid] = np.empty(round(max_year + 1 - min_year_arr[vehid - min_vehid]))
            values_bool_arr[vehid - min_vehid][:] = True

            # doplnění první hodnoty pole cenou NewPrice z elementu Vehicle a subelementu VehicleRecord pro daté vehicle_id
            values_arr[vehid - min_vehid][0] = new_price_arr[vehid - min_vehid]

    # naplnění pole polí pro existující ceny v daných letech
    for pri_rec in root_price:
        values_arr[int(pri_rec.find("VehicleID").text) - min_vehid][max_year - int(pri_rec.find("Year").text)] = int(pri_rec.find("Value").text)
        values_bool_arr[int(pri_rec.find("VehicleID").text) - min_vehid][max_year - int(pri_rec.find("Year").text)] = False

    n = 0
    v = max_vehid + 1 - min_vehid

    # lineární interpolace a naplnění XML
    for vehid in range(min_vehid, max_vehid + 1):
        if min_year_arr[vehid - min_vehid] != int(max_year+1): # np.nan:*******************************************************************
            # doplnění chybějících cen lineární interpolací
            values_arr[vehid - min_vehid] = interpolate(values_arr[vehid - min_vehid])

            # doplnění zaokrouhlených (na stovky) cen pro chybějící roky do XML
            for i in range(0, len(values_arr[vehid - min_vehid])):
                if values_bool_arr[vehid - min_vehid][i]:
                    new_pricerecord = ET.Element("PriceRecord")
                    ET.SubElement(new_pricerecord, "VehicleID").text = str(vehid)
                    ET.SubElement(new_pricerecord, "Year").text = str(max_year - i)
                    ET.SubElement(new_pricerecord, "Value").text = str(round(round(values_arr[vehid - min_vehid][i]), -2))
                    root_price.append(new_pricerecord)
        n = n + 1
        print(n, "z", v, ",", n / v * 100, "%")

    # propsání změn do nového XML dokumentu
    tree_new.write(file)

def doplnit_fce():
    if update_name.get().lower() == "" or (prefix.get().lower()+update_name.get().lower()) == file_name.lower():
        tk.messagebox.showerror("Špatný název nového souboru", "Změňte prosím název pro nový soubor tak, aby nebyl prázdný, nebo nebyl shodný s názvem nahraného souboru.")
    else:
        if prefix.get() + update_name.get() not in file_names_arr:
            shutil.copy(os.path.join(directory, (file_name + ".xml")),
                        os.path.join(directory, (prefix.get() + update_name.get() + ".xml")))
            file_names_arr.append(prefix.get()+update_name.get())
        fillXML(os.path.join(directory, (prefix.get()+update_name.get() + ".xml")))
        doplnit_btn['text'] = "Doplněno!"

def changeXML_old(file, koef, manuf, model, year_start, year_end):
    # Load the input XML file
    tree_new = ET.parse(file)
    root_new = tree_new.getroot()

    n = 0
    v = len(root_new.find("Price"))

    # propsání koeficientu do ceny u vybraných značek a modelů a také dle stáří
    for pri_rec in root_new.find("Price"):
        n = n + 1
        print(n, "z", v, ",", n / v * 100, "%")
        if (int(pri_rec.find("Year").text) <= year_end and int(pri_rec.find("Year").text) >= year_start):
            for veh_rec in root_new.find("Vehicle"):
                if (pri_rec.find("VehicleID").text == veh_rec.find("VehicleID").text):
                    for var_rec in root_new.find("Variant"):
                        if (var_rec.find("VariantID").text == veh_rec.find("VariantID").text):
                            for eng_rec in root_new.find("Engine"):
                                if (var_rec.find("EngineID").text == eng_rec.find("EngineID").text):
                                    for bum_rec in root_new.find("Bum"):
                                        if (bum_rec.find("BumID").text == eng_rec.find("BumID").text):
                                            for mod_rec in root_new.find("Model"):
                                                if (bum_rec.find("ModelID").text == mod_rec.find("ModelID").text and (
                                                        model == "Všechny modely" or mod_rec.find("Text").text == model)):
                                                    for man_rec in root_new.find("Manufacturer"):
                                                        if (man_rec.find("ManufacturerID").text == mod_rec.find(
                                                                "ManufacturerID").text and man_rec.find(
                                                                "Text").text == manuf):
                                                            pri_rec.find("Value").text = str(
                                                                round(round(int(pri_rec.find("Value").text) * koef),
                                                                      -2))
    # propsání změn do nového XML dokumentu
    tree_new.write(file)

def changeXML(file, koef, manuf, model, year_start, year_end):
    # Load the input XML file
    tree_new = ET.parse(file)
    root_new = tree_new.getroot()

    n = 0
    v = len(root_new.find("Manufacturer"))

    # propsání koeficientu do ceny u vybraných značek a modelů a také dle stáří
    for man_rec in root_new.find("Manufacturer"):
        n = n + 1
        print(n, "z", v, ",", n / v * 100, "%")
        if man_rec.find("Text").text == manuf:
            for mod_rec in root_new.find("Model"):
                if (model == "Všechny modely" or mod_rec.find("Text").text == model) and man_rec.find("ManufacturerID").text == mod_rec.find("ManufacturerID").text:
                    for bum_rec in root_new.find("Bum"):
                        if bum_rec.find("ModelID").text == mod_rec.find("ModelID").text:
                            for eng_rec in root_new.find("Engine"):
                                if bum_rec.find("BumID").text == eng_rec.find("BumID").text:
                                    for var_rec in root_new.find("Variant"):
                                        if var_rec.find("EngineID").text == eng_rec.find("EngineID").text:
                                            for veh_rec in root_new.find("Vehicle"):
                                                if var_rec.find("VariantID").text == veh_rec.find("VariantID").text:
                                                    for pri_rec in root_new.find("Price"):
                                                        if pri_rec.find("VehicleID").text == veh_rec.find("VehicleID").text and int(pri_rec.find("Year").text) <= year_end and int(pri_rec.find("Year").text) >= year_start:
                                                            pri_rec.find("Value").text = str(round(round(int(pri_rec.find("Value").text) * koef), -2))
    # propsání změn do nového XML dokumentu
    tree_new.write(file)

def upravit_fce():
    if update_name.get().lower() == "" or (prefix.get().lower()+update_name.get().lower()) == file_name.lower():
        tk.messagebox.showerror("Špatný název nového souboru", "Změňte prosím název pro nový soubor tak, aby nebyl prázdný, nebo nebyl shodný s názvem nahraného souboru.")
    elif changes == []:
        tk.messagebox.showerror("Žádné úpravy",
                                "Vytvořte úpravy, které chcete provést.")
    else:
        if prefix.get() + update_name.get() not in file_names_arr:
            shutil.copy(os.path.join(directory, (file_name + ".xml")),
                        os.path.join(directory, (prefix.get() + update_name.get() + ".xml")))
            file_names_arr.append(prefix.get()+update_name.get())
        for change in changes:
            changeXML(os.path.join(directory, (prefix.get()+update_name.get() + ".xml")), change.koef, change.manuf,
                      change.model, int(change.start), int(change.end))
        upravit_btn['text'] = "Upraveno!"

def ultimate_fce():
    if update_name.get().lower() == "" or (prefix.get().lower()+update_name.get().lower()) == file_name.lower():
        tk.messagebox.showerror("Špatný název nového souboru", "Změňte prosím název pro nový soubor tak, aby nebyl prázdný, nebo nebyl shodný s názvem nahraného souboru.")
    else:
        if prefix.get() + update_name.get() not in file_names_arr:
            shutil.copy(os.path.join(directory, (file_name + ".xml")),
                        os.path.join(directory, (prefix.get() + update_name.get() + ".xml")))
            file_names_arr.append(prefix.get()+update_name.get())
        fillXML(os.path.join(directory, (prefix.get()+update_name.get() + ".xml")))
        for change in changes:
            changeXML(os.path.join(directory, (prefix.get()+update_name.get() + ".xml")), change.koef, change.manuf,
                      change.model, int(change.start), int(change.end))
        ultimate_btn['text'] = "ULT1M4T3!"

# def showName():
    # show_name['text'] = prefix.get()+update_name.get()

def setOd(event):
    if int(do.get()) < int(od.get()):
        do.set(od.get())
    dos = []
    for i in np.arange(datetime.datetime.now().year, int(od.get())-1, -1):
        dos.append(i)
    do['values'] = dos

def setDo(event):
    if int(do.get()) < int(od.get()):
        od.set(do.get())
    ods = []
    for i in np.arange(2002, int(do.get())+1, 1):
        ods.append(i)
    od['values'] = ods

def on_enter(event):
    event.widget.configure(bg="white", fg="#ef7a00")  # Change the background color when the mouse enters #ff9933

def on_leave(event):
    event.widget.configure(bg="#ef7a00", fg="white")  # Change the background color when the mouse leaves

file_names_arr = []

# hlavní volba
main_grid = tk.Frame(root, bg="#00234b")
main_grid.columnconfigure(0, weight=1, uniform="columns")
main_grid.columnconfigure(1, weight=1, uniform="columns")

# tlačítko nahrát
nahrat_btn = tk.Button(main_grid, text="Nahrát XML", font=("Lexend", 15, "bold"), command=nahrat_fce, bg="#ef7a00", fg="white", activebackground="white", activeforeground="#ef7a00")
nahrat_btn.bind("<Enter>", on_enter)
nahrat_btn.bind("<Leave>", on_leave)
nahrat_btn.grid(padx=5, pady=5, row=0, column=0, columnspan=2, sticky="we")

# tlačítko doplnit
doplnit_btn = tk.Button(main_grid, text="Doplnit XML", font=("Lexend", 15, "bold"), state="disabled", command=doplnit_fce, bg="#4c2400", fg="white", activebackground="white", activeforeground="#ef7a00")
doplnit_btn.grid(padx=5, pady=5, row=1, column=0, sticky="we")

# tlačítko upravit
upravit_btn = tk.Button(main_grid, text="Upravit XML", font=("Lexend", 15, "bold"), state="disabled", command=upravit_fce, bg="#4c2400", fg="white", activebackground="white", activeforeground="#ef7a00")
upravit_btn.grid(padx=5, pady=5, row=1, column=1, sticky="we")

# tlačítko ultimate
ultimate_btn = tk.Button(main_grid, text="Ultimate XML", font=("Lexend", 15, "bold"), state="disabled", command=ultimate_fce, bg="#4c2400", fg="white", activebackground="white", activeforeground="#ef7a00")
ultimate_btn.grid(padx=5, pady=(5, 10), row=2, column=0, columnspan=2, sticky="we")

main_grid.pack(fill="x")

# název nového souboru
file_grid = tk.Frame(root, bg="white")
file_grid.columnconfigure(0, weight=1)
file_grid.columnconfigure(1, weight=1)
file_grid.columnconfigure(2, weight=30)

# file_grid1 = tk.Label(file_grid, text="Použít prefix?", font=('Arial', 11))
# file_grid1.grid(padx=5, pady=5, row=0, column=0)
# file_grid2 = tk.Button(file_grid, text="Ukázat nový název!", font=('Arial', 11), state="disabled", command=showName)
# file_grid2.grid(padx=5, pady=5, row=0, column=1)
# file_grid3 = tk.Label(file_grid, text="Úprava názvu:", font=('Arial', 11))
# file_grid3.grid(padx=5, pady=5, row=0, column=2)

file_grid1 = tk.Label(file_grid, bg="white", fg="#00234b", text="Název nového souboru:", font=('Arial', 11, 'bold'))
file_grid1.grid(padx=5, pady=5, row=0, column=0, sticky="w")

# prefix checkbox
file_name = ""
prefix = tk.StringVar()
prefix_check = tk.Checkbutton(file_grid, bg="white", fg="#00234b", text="vystup +", font=('Arial', 11), variable=prefix, onvalue=file_name, offvalue="", state="disabled")
prefix_check.deselect()
prefix_check.grid(padx=5, pady=5, row=0, column=1, sticky="e")

#zobrazení názvu nbového souboru
# show_name = tk.Label(file_grid, text="", font=('Arial', 11))
# show_name.grid(padx=5, pady=5, row=1, column=1)

# název nového xml
update_name = tk.StringVar()
update_name.set("_updated")
new_file_name_entry = tk.Entry(file_grid, bg="white", fg="#00234b", textvariable=update_name, state="disabled")
new_file_name_entry.grid(padx=5, pady=5, row=0, column=2, sticky="we")

file_grid.pack(fill="x")

# název nového souboru
change_grid = tk.Frame(root, bg="#003876")
change_grid.columnconfigure(0, weight=1, uniform="label")
change_grid.columnconfigure(1, weight=30, uniform="vyber")
change_grid.columnconfigure(2, weight=30, uniform="vyber")
change_grid.columnconfigure(3, weight=1, uniform="label")

change_grid1 = tk.Label(change_grid, text="Značka", font=('Arial', 11, "bold"), bg="#003876", fg="white")
change_grid1.grid(padx=5, pady=(15, 5), row=0, column=0)
change_grid2 = tk.Label(change_grid, text="Model", font=('Arial', 11, "bold"), bg="#003876", fg="white")
change_grid2.grid(padx=5, pady=5, row=1, column=0)
change_grid3 = tk.Label(change_grid, text="Koeficient", font=('Arial', 11, "bold"), bg="#003876", fg="white")
change_grid3.grid(padx=5, pady=5, row=2, column=0)
change_grid4 = tk.Label(change_grid, text="Od", font=('Arial', 11, "bold"), bg="#003876", fg="white")
change_grid4.grid(padx=5, pady=(15, 5), row=0, column=3)
change_grid5 = tk.Label(change_grid, text="Do", font=('Arial', 11, "bold"), bg="#003876", fg="white")
change_grid5.grid(padx=5, pady=5, row=1, column=3)

# značka
znacky = []
znacka = ttk.Combobox(change_grid, values=znacky, state="disabled")
znacka.bind("<<ComboboxSelected>>", nactiModely)
znacka.grid(padx=5, pady=(15, 5), row=0, column=1, sticky="we")

# model
modely = []
model = ttk.Combobox(change_grid, values=modely, state="disabled")
model.grid(padx=5, pady=5, row=1, column=1, sticky="we")

# od
ods = []
for i in np.arange(2002, datetime.datetime.now().year+1, 1):
    ods.append(i)
od = ttk.Combobox(change_grid, values=ods, state="disabled")
od.current(0)
od.bind("<<ComboboxSelected>>", setOd)
od.grid(padx=5, pady=(15, 5), row=0, column=2, sticky="we")

# do
dos = []
for i in np.arange(datetime.datetime.now().year, 2001, -1):
    dos.append(i)
do = ttk.Combobox(change_grid, values=dos, state="disabled")
do.current(0)
do.bind("<<ComboboxSelected>>", setDo)
do.grid(padx=5, pady=5, row=1, column=2, sticky="we")

def zmenaKoef(event):
    koeficient_label['text'] = koeficient.get()

# koeficient
koeficient = tk.Scale(change_grid, from_=0, to=2, resolution=0.01, orient="horizontal", state="disabled", bg="#003876", fg="white", highlightbackground="#003876", command=zmenaKoef, showvalue=0)
koeficient.set(1)
koeficient.grid(padx=5, pady=5, row=2, column=1, columnspan=2, sticky="we")

koeficient_label = tk.Label(change_grid, text=koeficient.get(), font=('Arial', 11, "bold"), bg="#003876", fg="white")
koeficient_label.grid(padx=5, pady=5, row=2, column=3)

change_grid.pack(fill="x")

# název nového souboru
change_grid_btns = tk.Frame(root, bg="#003876")
change_grid_btns.columnconfigure(0, weight=1, uniform="vymazat")
change_grid_btns.columnconfigure(1, weight=1, uniform="vymazat")
change_grid_btns.columnconfigure(2, weight=1, uniform="vymazat")
change_grid_btns.columnconfigure(3, weight=1, uniform="vymazat")

#úpravy
changes = []
changes_labels = []

# tlačítko pridat úpravu
add_change = tk.Button(change_grid_btns, text="Přidat úpravu", font=('Arial', 10, "bold"), state="disabled", command=addChange, bg="#4c2400", fg="white", activebackground="white", activeforeground="#ef7a00")
add_change.grid(padx=5, pady=5, row=3, column=0, columnspan=2, sticky="we")

# tlačítko vymazat poslední úpravu
delete_last_change = tk.Button(change_grid_btns, text="Vymazat poslední úpravu", font=('Arial', 10, "bold"), state="disabled", command=deleteLastChange, bg="#4c2400", fg="white", activebackground="white", activeforeground="#ef7a00")
delete_last_change.grid(padx=5, pady=5, row=3, column=2, sticky="we")

# tlačítko vymazat všechny úpravy
delete_all_changes = tk.Button(change_grid_btns, text="Vymazat všechny úpravy", font=('Arial', 10, "bold"), state="disabled", command=deleteAllChanges, bg="#4c2400", fg="white", activebackground="white", activeforeground="#ef7a00")
delete_all_changes.grid(padx=5, pady=5, row=3, column=3, sticky="we")

change_grid_btns.pack(fill="x")

changes_frame = tk.LabelFrame(root, text="Aktuální úpravy: 0", bg="#003876", fg="white")

# changes_canvas = tk.Canvas(changes_labelframe)
# changes_canvas.pack(side="left", fill="both", expand=1)

# changes_scrollbar = ttk.Scrollbar(changes_labelframe, orient="vertical", command=changes_canvas.yview)
# changes_scrollbar.pack(side="right", fill="y")

# changes_canvas.configure(yscrollcommand=changes_scrollbar.set)
# changes_canvas.bind('<Configure>', lambda e: changes_canvas.configure(scrollregion=changes_canvas.bbox("all")))

# changes_frame = tk.Frame(changes_canvas)
# changes_canvas.create_window((0, 0), window=changes_frame, anchor="nw")

changes_frame.columnconfigure(0, weight=1)
changes_frame.columnconfigure(1, weight=1)
changes_frame.columnconfigure(2, weight=1)
changes_frame.columnconfigure(3, weight=1)
changes_frame.columnconfigure(4, weight=1)
changes_frame.columnconfigure(5, weight=1)

changes_frame_top0 = tk.Label(changes_frame, text="Úprava #", font=('Arial', 10, 'bold'), bg="#003876", fg="white")
changes_frame_top0.grid(row=0, column=0, sticky="we")
changes_frame_top1 = tk.Label(changes_frame, text="Značka", font=('Arial', 10, 'bold'), bg="#003876", fg="white")
changes_frame_top1.grid(row=0, column=1, sticky="we")
changes_frame_top2 = tk.Label(changes_frame, text="Model", font=('Arial', 10, 'bold'), bg="#003876", fg="white")
changes_frame_top2.grid(row=0, column=2, sticky="we")
changes_frame_top3 = tk.Label(changes_frame, text="Od", font=('Arial', 10, 'bold'), bg="#003876", fg="white")
changes_frame_top3.grid(row=0, column=3, sticky="we")
changes_frame_top4 = tk.Label(changes_frame, text="Do", font=('Arial', 10, 'bold'), bg="#003876", fg="white")
changes_frame_top4.grid(row=0, column=4, sticky="we")
changes_frame_top5 = tk.Label(changes_frame, text="Koeficient", font=('Arial', 10, 'bold'), bg="#003876", fg="white")
changes_frame_top5.grid(row=0, column=5, sticky="we")

changes_frame.pack(fill="both", expand=1)

def printnuti():
    #print(prefix.get())
    #print(update_name.get())
    #print(prefix.get()+update_name.get())
    #print(koeficient.get()*2)
    #print(datetime.datetime.now().year*3)
    #print(int(od.get())*2)
    #print(znacky, znacka.get())
    #print(modely, model.get())
    #print(root_orig)
    print(changes)
    #print(changes_labels)
    #print(file_names_arr)

# print_btn = tk.Button(root, text="printni", font=('Arial', 15), command=printnuti)
# print_btn.pack(padx=5, pady=5)

def confirmExit():
    exit = tk.messagebox.askyesno(title="Konec hry!", message="Určitě?")
    if exit:
        root.destroy()

root.protocol("WM_DELETE_WINDOW", confirmExit)
root.mainloop()
