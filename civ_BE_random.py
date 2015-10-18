import random
import argparse


# expects to be given the length of a list/array
def getrand(length):
    return random.randint(0, length - 1)

# Main function
def main(dlc):

    if dlc is False:
        nodlc = 4
    else:
        nodlc = 0

    random.seed()
    civList = [("American Reclamation Corporation (ARC)", "Suzanne Fielding"),
               ("Pan-Asian Cooperative (PAC)", "Daoming Sochua"),
               ("People's African Union (PAU)", "Samatar Jama Barre"),
               ("Franco-Iberia (FI)", "Elodie"),
               ("Kavithan Protectorate (KP)", "Thakur"),
               ("Brasilia", "Rejinaldo de Alencar"),
               ("Polystralia", "Hutama"),
               ("Slavic Federation (SF)", "Gen. Vadim Koslov"),
               ("Al Falah", "Arshia Kishk"),
               ("Chungsu", "Han Jae-Moon"),
               ("INTEGR", "Lena Ebner"),
               ("North Sea Alliance (NSA)", "Duncan Hughes ")]
    victoryList = ["Domination", "Contact", "Purity(Promised Land)", "Harmony(Transcendence)",
                   "Supremacy(Emancipation)"]
    mapTypeList = ["Terran World", "Protean World", "Atlantean World"]
    biomeList = ["Primordial", "Frigid", "Lust", "Fungal", "Arid"]
    mapSizeList = ["Duel", "Dwarf", "Small", "Standard", "Large", "Massive"]
    colonistsList = ["Scientists", "Refugees", "Aristocrats", "Engineers", "Artists"]
    spacecraftList = ["Continental Surveyor", "Retrograde Thrusters", "Tectonic Scanner", "Fusion Reactor",
                      "Lifeform Sensor"]
    cargoList = ["Hydroponics", "Laboratory", "Raw Materials", "Weapon Arsenal", "Machinery"]

    # If --DLC is used, then dlc value equal 0 and all civs can be chosen
    civ, leader = civList[getrand(len(civList) - nodlc)]
    print("Leader: " + leader +
          "\nCivilization: " + civ +
          "\nLOADOUT\n\t" + colonistsList[getrand(len(colonistsList))] + " \n\t" +
          spacecraftList[getrand(len(spacecraftList))] + " \n\t" + cargoList[getrand(len(cargoList))] +
          "\nVictory Condition: " + victoryList[getrand(len(victoryList))] +
          "\nMap Type: " + mapTypeList[getrand(len(mapTypeList))] +
          "\nMap Size: " + mapSizeList[getrand(len(mapSizeList))] +
          "\nWorld biome: "+ biomeList[getrand(len(biomeList))])
    input("\nPress the Enter/Return key to Exit")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Game randomize for Civ: Beyond Earth')
    parser.add_argument('-d', '--dlc', action="store_true", dest="d", default=False, help="Enables DLC Civs")
    results = parser.parse_args()
    main(results.d)
