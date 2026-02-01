
def configure_printer(**settings):
    print("Erwünschte Printer Settings")
    print("-"*30)
    for key, value in settings.items():
        print(f"{key}: {value}")


configure_printer(papierformate = "A4", duplex =  True, farbe = False, qualitaet = "draft")