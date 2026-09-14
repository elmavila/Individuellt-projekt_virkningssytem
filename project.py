from datetime import datetime

# Vi använder en klass för att representera ett projekts information.
# Det gör det lättare att lagra relaterad data tillsammans, till exempel namn,
# kroknål, material och när projektet skapades.
class Yarn:
    def __init__(self, brand, color, material):
        self.brand = brand
        self.color = color
        self.material = material

    def display_yarn_info(self):
        return f"{self.brand} - {self.color} ({self.material})"


class CrochetProject:
    def __init__(self, name, hook_size, yarns):
        self.name = name
        self.hook_size = hook_size
        self.yarns = yarns
        self.date_added = datetime.now().strftime("%Y-%m-%d %H:%M")

    def display_info(self):
        print(f"Project Name: {self.name}")
        print(f"Hook Size: {self.hook_size}")
        print("Yarns:")
        if self.yarns:
            for yarn in self.yarns:
                print(f" {yarn.display_yarn_info()}")
        else:
            print("  - None")
        print(f"Date Added: {self.date_added}")





        