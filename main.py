'''
*******************************
Author: u3327375, u3330354, u3334444
Group: Assignment 3
Assessment: Software Technology 1
Date: 13/05/2026
*******************************
'''

from src.services.workflow_service import WorkflowService

def show_species_menu(workflow):
    """Show interactive species selection menu."""
    dataframe = workflow.load_dataframe()
    species_list = sorted(dataframe["label"].unique())

    while True:
        print("\n--- Select a species to view details ---")
        for i, species in enumerate(species_list, 1):
            print(f"  {i}. {species}")
        print("  0. Exit")

        choice = input("\nEnter number: ").strip()

        if choice == "0":
            print("Exiting...")
            break

        try:
            index = int(choice) - 1
            if 0 <= index < len(species_list):
                species = species_list[index]
                species_data = dataframe[dataframe["label"] == species]
                print(f"\n{species}:")
                print(f"  Total images : {len(species_data)}")
                print(f"  Avg Width    : {species_data['width'].mean():.0f}px")
                print(f"  Avg Height   : {species_data['height'].mean():.0f}px")
                print("\nPress Enter to go back to menu...")
                input()
            else:
                print("Invalid number. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    """Run the main project workflow."""
    print("Starting Macroinvertebrate Image Analysis System...")
    workflow = WorkflowService()
    workflow.run_full_pipeline()
    show_species_menu(workflow)

if __name__ == "__main__":
    main()