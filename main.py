from project import CrochetProject, Yarn

# Detta program är byggt som en enkel projektlista för virkningsprojekt.
# Vi använder en lista som lagrar projektobjekt, eftersom det gör det enkelt
# att lägga till, söka, visa och ta bort projekt utan att behöva spara i en databas.


def show_menu():
    # Menyn visas så att användaren snabbt kan välja vad som ska hända.
    print("\n--- Crochet Project Manager ---")
    print("1. Add a new project")
    print("2. Show all projects")
    print("3. Search for a project")
    print("4. Edit a project")
    print("5. Delete a project")
    print("6. Exit")


def add_project(projects):
    # Den här funktionen lägger till ett nytt projekt i listan.
    name = input("Project name: ").strip()
    if not name:
        print("Project name cannot be empty.")
        return

    # Vi loopar tills användaren anger ett giltigt nummer.
    # Detta gör att programmet inte kraschar om användaren skriver text istället för ett tal.
    while True:
        hook_input = input("Hook size: ").strip()
        try:
            hook_size = float(hook_input)
            break
        except ValueError:
            print("Invalid input! Hook size must be a number.")

    # Varje garn sparas som ett Yarn-objekt eftersom ett projekt kan innehålla flera garn.
    yarns = []
    print("\n--- Add Yarns for this Project ---")
    while True:
        brand = input("Yarn brand: ").strip()
        color = input("Yarn color: ").strip()
        material = input("Material type: ").strip()

        if brand and color and material:
            yarns.append(Yarn(brand, color, material))
            print("Yarn added to project.")
        else:
            print("Information cannot be empty. Yarn skipped.")

        cont = input("Add another yarn? (y/n): ").strip().lower()
        if cont != "y":
            break

    # Vi skapar projektet först efter att all information har samlats in.
    new_project = CrochetProject(name, hook_size, yarns)
    projects.append(new_project)
    print("Project added successfully!")


def show_projects(projects):
    # Den här funktionen visar alla sparade projekt.
    # Vi använder en lista och enumerate för att få ett nummer till varje projekt.
    if not projects:
        print("No projects saved yet.")
        return

    for index, project in enumerate(projects, start=1):
        print(f"\n--- Project {index} ---")
        project.display_info()


def search_project(projects):
    # Sökningen görs på en del av projektnamnet, vilket gör det användarvänligt.
    # Vi jämför med lowercase för att sökningen inte ska vara skiftlägeskänslig.
    if not projects:
        print("No projects saved yet.")
        return

    search_word = input(
        "Enter part of the project name to search: ").strip().lower()
    found = False

    for project in projects:
        if search_word in project.name.lower():
            print("\n--- Found project ---:")
            project.display_info()
            found = True

    if not found:
        print("No project matched your search.")


def delete_project(projects):
    # Det är viktigt att visa projektlistan först så att användaren kan se vad som ska tas bort.
    # Vi använder index i listan för att enkelt radera ett projekt utan att påverka resten.
    if not projects:
        print("No projects saved yet.")
        return

    show_projects(projects)
    try:
        choice = int(
            input("\nEnter the number of the project you want to delete: "))
        if 1 <= choice <= len(projects):
            removed = projects.pop(choice - 1)
            print(f"Project '{removed.name}' has been deleted.")
        else:
            print("Invalid project number.")
    except ValueError:
        print("Please enter a valid number.")


def edit_project(projects):
    if not projects:
        print("No projects saved yet.")
        return

    show_projects(projects)
    try:
        choice = int(
            input("\nEnter the number of the project you want to edit: "))
        if 1 <= choice <= len(projects):
            project = projects[choice - 1]
            print(f"\nEditing project '{project.name}'")

            new_name = input(
                f"New name (leave blank to keep '{project.name}'): ").strip()
            if new_name:
                project.name = new_name

            new_hook_size_input = input(
                f"New hook size (leave blank to keep '{project.hook_size}'): ").strip()
            if new_hook_size_input:
                try:
                    project.hook_size = float(new_hook_size_input)
                except ValueError:
                    print(
                        "Invalid input! Hook size must be a number. Keeping the old value.")

            update_yarns = input("Do you want to update the yarns? (y/n): ").strip().lower()
            if update_yarns == "y":
                yarns = []
                print("\n--- Add New Yarns ---")
                while True:
                    brand = input("Yarn brand: ").strip()
                    color = input("Yarn color: ").strip()
                    material = input("Material type: ").strip()

                    if brand and color and material:
                        yarns.append(Yarn(brand, color, material))
                        print("Yarn added.")
                    else:
                        print("Information cannot be empty. Yarn skipped.")

                    cont = input("Add another yarn? (y/n): ").strip().lower()
                    if cont != "y":
                        break
                if yarns:
                    project.yarns = yarns

            print("Project updated successfully!")
        else:
            print("Invalid project number.")
    except ValueError:
        print("Please enter a valid number.")


def main():
    # Här lagras alla projekt i en lista under programkörningen.
    # Detta är ett enkelt sätt att hålla tillståndet i minnet så länge programmet körs.
    projects = []

    while True:
        show_menu()
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            add_project(projects)
            input("\n[Press Enter to continue]")
        elif choice == "2":
            show_projects(projects)
            input("\n[Press Enter to continue]")
        elif choice == "3":
            search_project(projects)
            input("\n[Press Enter to continue]")
        elif choice == "4":
            edit_project(projects)
            input("\n[Press Enter to continue]")
        elif choice == "5":
            delete_project(projects)
            input("\n[Press Enter to continue]")
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
            input("\n[Press Enter to continue]")


if __name__ == "__main__":
    # Den här kontrollen gör att programmet bara körs när filen startas direkt,
    # och inte när den importeras från en annan fil.
    main()
