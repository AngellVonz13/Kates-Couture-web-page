def run_kates_couture_app():
    print("Welcome to Kate's Couture!")
    print("\nYour journey to a perfectly custom-made garment starts here.")
    print("What can I create for you today?")

    all_garment_details = {
        "Blouse": {"base_cost": 45.00, "base_yardage": 1.5, "measurements": ["Bust/Chest", "Across Back/Shoulder to Shoulder", "Neck/Collar Circumference", "Waist", "Mid-Torso", "Shoulder to Waist"]},
        "Button Front": {"base_cost": 35.00, "base_yardage": 1.75, "measurements": ["Bust/Chest", "Across Back/Shoulder to Shoulder", "Neck/Collar Circumference", "Waist", "Mid-Torso", "Shoulder to Waist"]},
        "Crop": {"base_cost": 40.00, "base_yardage": 1.2, "measurements": ["Bust/Chest", "Across Back/Shoulder to Shoulder", "Neck/Collar Circumference", "Waist", "Mid-Torso", "Shoulder to Waist", "Neck to Belly Button"]},
        "Vest": {"base_cost": 50.00, "base_yardage": 1.0, "measurements": ["Across Back/Shoulder to Shoulder", "Shoulder to Waist", "Bust/Chest", "Mid-Torso", "Neck to Waist (Back)", "Neck to Belly Button"]},
        "Blazer": {"base_cost": 100.00, "base_yardage": 2.5, "measurements": ["Bust/Chest", "Across Back/Shoulder to Shoulder", "Waist", "Mid-Torso", "Shoulder to Waist", "Bicep Circumference", "Forearm Circumference", "Cuff Circumference", "Shoulder to Cuff (Arm Extended)", "Blazer Length"]},
        "Camisole": {"base_cost": 20.00, "base_yardage": 0.8, "measurements": ["Bust/Chest", "Waist", "Mid-Torso", "Shoulder to Waist", "Shoulder to Bust Apex"]},
        "Evening": {"base_cost": 35.00, "base_yardage": 1.5, "measurements": ["Bust/Chest", "Across Back/Shoulder to Shoulder", "Neck/Collar Circumference", "Waist", "Mid-Torso", "Shoulder to Waist"]},

        "Shorts": {"base_cost": 30.00, "base_yardage": 1.0, "measurements": ["Waist", "Hips", "Inseam", "Outseam"]},
        "Pants": {"base_cost": 70.00, "base_yardage": 2.0, "measurements": ["Waist", "Hips", "Inseam", "Outseam"]},
        "Skirt": {"base_cost": 50.00, "base_yardage": 1.5, "measurements": ["Waist", "Hips", "Outseam"]},

        "Dress": {"base_cost": 100.00, "base_yardage": 3.0, "measurements": ["Bust/Chest", "Across Back/Shoulder to Shoulder", "Waist", "Mid-Torso", "Hips", "Outseam", "Shoulder to Waist", "Shoulder to Bust Apex", "Neck to Waist (Front)", "Neck to Waist (Back)"]},
        "Suit (Vest/Blazer/Pants)": {"base_cost": 220.00, "base_yardage": 5.5, "measurements": ["Bust/Chest", "Across Back/Shoulder to Shoulder", "Neck/Collar Circumference", "Waist", "Mid-Torso", "Shoulder to Waist", "Bicep Circumference", "Forearm Circumference", "Cuff Circumference", "Shoulder to Cuff (Arm Extended)", "Blazer Length", "Hips", "Inseam", "Outseam", "Neck to Waist (Back)", "Neck to Belly Button"]},
        "Suit (Vest/Blazer)": {"base_cost": 140.00, "base_yardage": 3.5, "measurements": ["Bust/Chest", "Across Back/Shoulder to Shoulder", "Neck/Collar Circumference", "Waist", "Mid-Torso", "Shoulder to Waist", "Bicep Circumference", "Forearm Circumference", "Cuff Circumference", "Shoulder to Cuff (Arm Extended)", "Blazer Length", "Neck to Waist (Back)", "Neck to Belly Button"]},
        "Suit (Vest/Pants)": {"base_cost": 110.00, "base_yardage": 3.0, "measurements": ["Across Back/Shoulder to Shoulder", "Shoulder to Waist", "Bust/Chest", "Mid-Torso", "Neck to Waist (Back)", "Neck to Belly Button", "Waist", "Hips", "Inseam", "Outseam"]},
        "Suit (Blazer/Pants)": {"base_cost": 170.00, "base_yardage": 4.5, "measurements": ["Bust/Chest", "Across Back/Shoulder to Shoulder", "Waist", "Mid-Torso", "Shoulder to Waist", "Bicep Circumference", "Forearm Circumference", "Cuff Circumference", "Shoulder to Cuff (Arm Extended)", "Blazer Length", "Hips", "Inseam", "Outseam"]},
        "Evening Top and Pants": {"base_cost": 90.00, "base_yardage": 3.8, "measurements": ["Bust/Chest", "Across Back/Shoulder to Shoulder", "Neck/Collar Circumference", "Waist", "Mid-Torso", "Shoulder to Waist", "Hips", "Inseam", "Outseam"]},
        "Evening Top and Shorts": {"base_cost": 85.00, "base_yardage": 3.3, "measurements": ["Bust/Chest", "Across Back/Shoulder to Shoulder", "Neck/Collar Circumference", "Waist", "Mid-Torso", "Shoulder to Waist", "Hips", "Inseam", "Outseam"]},
        "Camisole and Evening Pants": {"base_cost": 75.00, "base_yardage": 2.8, "measurements": ["Bust/Chest", "Waist", "Mid-Torso", "Shoulder to Waist", "Shoulder to Bust Apex", "Hips", "Inseam", "Outseam"]},
        "Camisole and Evening Shorts": {"base_cost": 70.00, "base_yardage": 2.3, "measurements": ["Bust/Chest", "Waist", "Mid-Torso", "Shoulder to Waist", "Shoulder to Bust Apex", "Hips", "Inseam", "Outseam"]},
    }

    measurement_descriptions = {
        "Bust/Chest": "Around the fullest part of your bust/chest, keeping the tape horizontal.",
        "Across Back/Shoulder to Shoulder": "Measure straight across your back from the point where one shoulder seam would meet the sleeve seam to the corresponding point on the other shoulder.",
        "Neck/Collar Circumference": "Measure around the base of your neck where a collar would naturally sit.",
        "Waist": "Measure around your comfortable pant line, where your pants naturally sit (typically an inch or two above the hip line).",
        "Mid-Torso": "Measure horizontally around your torso at the level of your belly button.",
        "Shoulder to Waist": "Measure from the top of your shoulder (where a seam would sit) down to your natural waistline (pant line).",
        "Sleeve Length": "Measure from the top of your shoulder (arm relaxed) down to where you want the sleeve to end.",
        "Hips": "Measure around the fullest part of your hips, ensuring the tape is level.",
        "Inseam": "Measure from your crotch down to your desired hem length.",
        "Outseam": "Measure from your natural waistline (pant line) down to your desired hem length.",
        "Shoulder to Bust Apex": "Measure from the top of your shoulder (at the base of the neck) down to the fullest point of your bust.",
        "Neck to Waist (Front)": "Measure from the prominent bone at the base of your neck (front center) down to your natural waistline (pant line).",
        "Neck to Waist (Back)": "Measure from the prominent bone at the base of your neck (back center) down to your natural waistline (pant line).",
        "Bicep Circumference": "Measure around the fullest part of your upper arm.",
        "Forearm Circumference": "Measure around the fullest part of your forearm.",
        "Cuff Circumference": "Measure around your wrist where the cuff would sit.",
        "Shoulder to Cuff (Arm Extended)": "With your arm held straight out in front of you, measure from the top of your shoulder (where a seam would sit) down to where you want the cuff to rest on your wrist.",
        "Blazer Length": "Measure from the prominent bone at the base of your neck (center back) down your back to your desired blazer hem length.",
        "Neck to Belly Button": "Measure from the prominent bone at the base of your neck (front center) down the front to the exact point of your belly button.",
    }

    completed_orders = []
    customer_measurements_session = {}
    all_required_measurements = set()

    def get_garment_details(g_name):
        return all_garment_details.get(g_name, {"base_cost": 0, "base_yardage": 0, "measurements": []})

    while True:
        garment_name = ""
        base_cost = 0
        estimated_yardage = 0
        required_measurements_for_current_garment = []
        
        top_style_choice = "N/A"
        bottom_style_choice = "N/A"
        pants_style_choice = "N/A"
        shorts_style_choice = "N/A"
        skirt_style_choice = "N/A"
        dress_waistline_choice = "N/A"
        button_placement_choice = "N/A"
        vest_bottom_style = "N/A"
        sleeve_chosen_type = "N/A"
        collar_choice = "N/A"
        slits_chosen = "N/A"
        belt_loops_chosen = "N/A"
        pockets_chosen = "N/A"
        lining_chosen = "N/A"
        complex_customizations_chosen = []
        other_complex_description = "N/A"
        additional_cost = 0
        fabric_adjustment = 0
        chosen_fabrics = []

        print("\nSelect Your Garment Category")
        top_level_categories = {
            "1": "Top",
            "2": "Bottom",
            "3": "Combo"
        }

        for num, category in top_level_categories.items():
            print(f"{num}. {category}")

        while True:
            category_choice_num = input("Simply pick a number: ").strip()
            top_level_category = top_level_categories.get(category_choice_num)
            if top_level_category:
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")

        if top_level_category == "Top":
            print("\nSelect Your Top Garment")
            top_options = {
                "1": "Blouse",
                "2": "Button Front",
                "3": "Crop",
                "4": "Vest",
                "5": "Blazer",
                "6": "Camisole",
                "7": "Evening"
            }
            for num, option in top_options.items():
                print(f"{num}. {option}")

            while True:
                top_choice_num = input("Simply pick a number: ").strip()
                chosen_garment_key = top_options.get(top_choice_num)
                if chosen_garment_key:
                    garment_name = chosen_garment_key
                    garment_details = get_garment_details(garment_name)
                    base_cost = garment_details["base_cost"]
                    estimated_yardage = garment_details["base_yardage"]
                    required_measurements_for_current_garment.extend(garment_details["measurements"])
                    top_style_choice = "N/A"
                    break
                else:
                    print("Invalid choice. Please enter a number from 1 to 7.")

            if garment_name != "Camisole" and garment_name != "Vest" and garment_name != "Blazer":
                print("\nSelect Collar Type:")
                collar_options = {
                    "1": "Mandarin collar (A short, stand-up collar)",
                    "2": "Fold-over collar (A classic collar that folds down)",
                    "3": "Basic collar (A simple, non-folding neck finish)",
                    "4": "No collar (A clean, collarless neckline)"
                }
                for num, desc in collar_options.items():
                    print(f"{num}. {desc}")

                while True:
                    collar_choice_num = input("Simply pick a number: ").strip()
                    selected_collar = collar_options.get(collar_choice_num)
                    if selected_collar:
                        collar_choice = selected_collar.split(' ')[0] + " " + selected_collar.split(' ')[1] if "collar" in selected_collar else selected_collar.split(' ')[0]
                        if collar_choice == "No collar":
                            pass
                        elif collar_choice == "Mandarin collar":
                            additional_cost += 5.00
                        elif collar_choice == "Fold-over collar":
                            additional_cost += 8.00
                        elif collar_choice == "Basic collar":
                            additional_cost += 3.00

                        if collar_choice != "No collar" and "Neck/Collar Circumference" not in required_measurements_for_current_garment:
                            required_measurements_for_current_garment.append("Neck/Collar Circumference")
                        break
                    else:
                        print("Invalid choice. Please enter a number from 1 to 4.")

        elif top_level_category == "Bottom":
            print("\nSelect Your Bottom Garment")
            bottom_options = {
                "1": "Pants",
                "2": "Shorts",
                "3": "Skirt",
            }
            for num, option in bottom_options.items():
                print(f"{num}. {option}")

            while True:
                bottom_choice_num = input("Simply pick a number: ").strip()
                chosen_garment_key = bottom_options.get(bottom_choice_num)
                if chosen_garment_key:
                    garment_name = chosen_garment_key
                    garment_details = get_garment_details(garment_name)
                    base_cost = garment_details["base_cost"]
                    estimated_yardage = garment_details["base_yardage"]
                    required_measurements_for_current_garment.extend(garment_details["measurements"])
                    break
                else:
                    print("Invalid choice. Please enter a number from 1 to 3.")

            if garment_name == "Pants":
                print("\nSelect Your Pants Style")
                pants_styles = {
                    "1": "Slacks",
                    "2": "Sweats",
                    "3": "Joggers",
                    "4": "Boot Cut",
                    "5": "Evening",
                    "6": "Leggings"
                }
                for num, style_name in pants_styles.items():
                    print(f"{num}. {style_name}")

                while True:
                    pants_style_choice_num = input("Simply pick a number: ").strip()
                    pants_style_choice = pants_styles.get(pants_style_choice_num)
                    if pants_style_choice:
                        if pants_style_choice == "Evening":
                            additional_cost += 25.00
                            fabric_adjustment += 0.4
                        elif pants_style_choice == "Leggings":
                            additional_cost -= 20.00
                            fabric_adjustment -= 0.5
                        break
                    else:
                        print("Invalid choice. Please enter a number from 1 to 6.")
            elif garment_name == "Shorts":
                print("\nSelect Your Shorts Style")
                shorts_styles = {
                    "1": "Joggers",
                    "2": "Sweats",
                    "3": "Evening"
                }
                for num, style_name in shorts_styles.items():
                    print(f"{num}. {style_name}")

                while True:
                    shorts_style_choice_num = input("Simply pick a number: ").strip()
                    shorts_style_choice = shorts_styles.get(shorts_style_choice_num)
                    if shorts_style_choice:
                        if shorts_style_choice == "Evening":
                            additional_cost += 20.00
                            fabric_adjustment += 0.3
                        break
                    else:
                        print("Invalid choice. Please enter a number from 1 to 3.")
            elif garment_name == "Skirt":
                print("\nSelect Your Skirt Style")
                skirt_styles = {
                    "1": "Floor",
                    "2": "Ankle",
                    "3": "Mid-calf",
                    "4": "Knee",
                    "5": "Mini"
                }
                for num, style_name in skirt_styles.items():
                    print(f"{num}. {style_name}")

                while True:
                    skirt_style_choice_num = input("Simply pick a number: ").strip()
                    skirt_style_choice = skirt_styles.get(skirt_style_choice_num)
                    if skirt_style_choice:
                        break
                    else:
                        print("Invalid choice. Please enter a number from 1 to 5.")


        elif top_level_category == "Combo":
            print("\nSelect Your Combo Garment")
            print("1. Dress")
            print("2. Suit")
            print("  2.1. Vest/Blazer/Pants")
            print("  2.2. Vest/Blazer")
            print("  2.3. Vest/Pants")
            print("  2.4. Blazer/Pants")
            print("3. Evening Top and Pants")
            print("4. Evening Top and Shorts")
            print("5. Camisole and Evening Pants")
            print("6. Camisole and Evening Shorts")

            while True:
                combo_choice_num = input("Simply pick a number (e.g., 2.1 for Vest/Blazer/Pants Suit): ").strip()
                if combo_choice_num == "1":
                    garment_name = "Dress"
                elif combo_choice_num == "2.1":
                    garment_name = "Suit (Vest/Blazer/Pants)"
                elif combo_choice_num == "2.2":
                    garment_name = "Suit (Vest/Blazer)"
                elif combo_choice_num == "2.3":
                    garment_name = "Suit (Vest/Pants)"
                elif combo_choice_num == "2.4":
                    garment_name = "Suit (Blazer/Pants)"
                elif combo_choice_num == "3":
                    garment_name = "Evening Top and Pants"
                elif combo_choice_num == "4":
                    garment_name = "Evening Top and Shorts"
                elif combo_choice_num == "5":
                    garment_name = "Camisole and Evening Pants"
                elif combo_choice_num == "6":
                    garment_name = "Camisole and Evening Shorts"
                else:
                    print("Invalid choice. Please enter a valid number (e.g., 1, 2.1, 3, etc.).")
                    continue

                garment_details = get_garment_details(garment_name)
                base_cost = garment_details["base_cost"]
                estimated_yardage = garment_details["base_yardage"]
                required_measurements_for_current_garment.extend(garment_details["measurements"])

                break

        print("\nAdd Customization Details")

        if garment_name in ["Button Front", "Evening", "Blazer", "Vest"]:
            print("\nButton Placement")
            print("Choose the button placement:")
            print("1. Left Button (buttons on wearer's left, buttonholes on right)")
            print("2. Right Button (buttons on wearer's right, buttonholes on left)")
            while True:
                button_choice = input("Simply pick a number: ").strip()
                if button_choice == "1":
                    button_placement_choice = "Left Button"
                    break
                elif button_choice == "2":
                    button_placement_choice = "Right Button"
                    break
                else:
                    print("Invalid choice. Please enter 1 or 2.")

        if garment_name == "Dress":
            print("\nSelect Dress Waistline Option:")
            dress_waistline_options = {
                "1": "Empire/High",
                "2": "Mid-Torso",
                "3": "Natural",
                "4": "None"
            }
            for num, option in dress_waistline_options.items():
                print(f"{num}. {option}")
            while True:
                waistline_choice_num = input("Simply pick a number: ").strip()
                dress_waistline_choice = dress_waistline_options.get(waistline_choice_num)
                if dress_waistline_choice:
                    break
                else:
                    print("Invalid choice. Please enter a number from 1 to 4.")


        sleeves_applicable = False
        if garment_name in ["Blouse", "Button Front", "Crop", "Dress", "Blazer"] or \
           "Evening Top" in garment_name or "Camisole" in garment_name or \
           "Suit (" in garment_name:
            sleeves_applicable = True

        if "Camisole" in garment_name:
            sleeve_chosen_type = "None"
            print("Note: Camisoles do not typically have sleeves. Sleeve type set to 'None'.")
        elif garment_name == "Vest" or "Suit (Vest/Pants)" in garment_name:
            sleeve_chosen_type = "None"
            print("Note: Vests do not typically have sleeves. Sleeve type set to 'None'.")
        elif sleeves_applicable:
            sleeve_choice_prompt = "Sleeve type for top portion?" if "Suit (" in garment_name else "Sleeve type?"
            while True:
                sleeve_choice = input(f"{sleeve_choice_prompt} (Short, Long, None): ").strip().lower()
                if sleeve_choice in ["long", "l"]:
                    additional_cost += 10.00
                    fabric_adjustment += 0.5
                    sleeve_chosen_type = "Long"
                    break
                elif sleeve_choice in ["short", "s"]:
                    sleeve_chosen_type = "Short"
                    break
                elif sleeve_choice in ["none", "n"]:
                    sleeve_chosen_type = "None"
                    break
                else:
                    print("Invalid sleeve choice. Please enter 'Short', 'Long', 'None', or their single letter abbreviations (S, L, N).")

        if sleeve_chosen_type == "Long":
            if "Sleeve Length" not in required_measurements_for_current_garment:
                required_measurements_for_current_garment.append("Sleeve Length")
            if "Shoulder to Cuff (Arm Extended)" not in required_measurements_for_current_garment:
                required_measurements_for_current_garment.append("Shoulder to Cuff (Arm Extended)")
        elif sleeve_chosen_type == "Short":
            if "Sleeve Length" not in required_measurements_for_current_garment:
                required_measurements_for_current_garment.append("Sleeve Length")

        if garment_name == "Vest" or "Suit (Vest" in garment_name:
            print("\nVest Bottom Style")
            print("Choose the bottom style for the front flaps of your vest:")
            print("1. Rounded Bottom")
            print("2. Pointed/V Bottom")
            print("3. Double Pointed VV Bottom")
            print("4. Flat Bottom")
            while True:
                style_choice = input("Simply pick a number: ").strip()
                if style_choice == "1":
                    vest_bottom_style = "Rounded Bottom"
                    break
                elif style_choice == "2":
                    vest_bottom_style = "Pointed/V Bottom"
                    break
                elif style_choice == "3":
                    vest_bottom_style = "Double Pointed VV Bottom"
                    additional_cost += 5.00
                    break
                elif style_choice == "4":
                    vest_bottom_style = "Flat Bottom"
                    break
                else:
                    print("Invalid choice. Please enter a number from 1 to 4.")

        print("\n--- Additional Customizations ---")
        print("This section currently has no general customizations. Proceeding to the next step.")

        complex_design_prompt_input = input("Let's really slay! (yes/no): ").strip().lower()

        if complex_design_prompt_input in ["yes", "y"]:
            print("\nSelect Complex Design Details")
            print("You can choose multiple options. Type 'done' or 'd' when finished.")

            complex_options_with_desc = {
                "1": {"name": "Ruffles", "desc": "Gathered or pleated strips of fabric used as trim or decoration.", "cost": 35.00, "fabric_adj": 1.0},
                "2": {"name": "Pleats", "desc": "Folds in fabric, pressed or stitched in place, creating volume or texture.", "cost": 35.00, "fabric_adj": 1.0},
                "3": {"name": "Intricate Seams", "desc": "Complex or decorative stitching patterns, like French seams, flat-felled seams, or detailed topstitching.", "cost": 35.00, "fabric_adj": 1.0},
                "4": {"name": "Delicates", "desc": "Details requiring extremely fine or fragile materials, hand-stitching, or very careful handling (e.g., fine lace insertions, beadwork, embroidery).", "cost": 70.00, "fabric_adj": 2.0},
                "5": {"name": "Applique", "desc": "Decorative cut-outs of fabric sewn onto a larger piece of fabric.", "cost": 70.00, "fabric_adj": 2.0},
                "6": {"name": "Cut-outs", "desc": "Sections of fabric intentionally removed to create design elements, often revealing skin or underlayers.", "cost": 70.00, "fabric_adj": 2.0},
                "7": {"name": "Slits", "desc": "Openings in the fabric, usually at the hem or side seam, for ease of movement or style.", "cost": 10.00, "fabric_adj": 0.1},
                "8": {"name": "Lining", "desc": "An inner layer of fabric that provides structure, comfort, or opacity.", "cost": 25.00, "fabric_adj_factor": 0.75},
                "9": {"name": "Pockets", "desc": "Fabric pouches sewn into or onto a garment for carrying small items.", "cost": 15.00, "fabric_adj": 0.25},
                "10": {"name": "Belt Loops", "desc": "Small fabric loops sewn onto a waistband to hold a belt in place.", "cost": 5.00, "fabric_adj": 0.05},
                "11": {"name": "Other (Will describe at end)", "desc": "Any other unique complex detail not listed above."}
            }

            selected_complex_count = 0
            temp_complex_costs = 0
            temp_fabric_adjustments = 0

            while True:
                print("\nOptions:")
                for num, option_data in complex_options_with_desc.items():
                    print(f"{num}. {option_data['name']} - {option_data['desc']}")
                print("Type 'done' or 'd' to finish selecting.")

                choice = input("Enter a number for an option, or 'done'/'d': ").strip().lower()

                if choice in ["done", "d"]:
                    break

                chosen_option_data = complex_options_with_desc.get(choice)
                if chosen_option_data:
                    chosen_option_name = chosen_option_data['name']
                    if chosen_option_name not in complex_customizations_chosen:
                        complex_customizations_chosen.append(chosen_option_name)
                        selected_complex_count += 1

                        if chosen_option_name in ["Slits", "Lining", "Pockets", "Belt Loops"]:
                            additional_cost += chosen_option_data['cost']
                        else: 
                            temp_complex_costs += chosen_option_data['cost']
                            if 'fabric_adj' in chosen_option_data:
                                temp_fabric_adjustments += chosen_option_data['fabric_adj']

                        print(f"'{chosen_option_name}' added.")

                        if chosen_option_name == "Pockets":
                            print("\nWhat kind of pockets would you like?")
                            print("1. Standard Patch Pockets")
                            print("2. Hidden Seam Pockets")
                            print("3. Zipper Pockets")
                            pocket_type_choice = input("Simply pick a number (1-3): ").strip()
                            if pocket_type_choice == "1":
                                pass
                            elif pocket_type_choice == "2":
                                pass
                            elif pocket_type_choice == "3":
                                additional_cost += 5.00 
                            else:
                                print("Invalid pocket choice, defaulting to Standard Patch Pockets.")
                        elif chosen_option_name == "Lining":
                            lining_chosen = "Yes"
                            print("Lining will be factored into the fabric selection later.")
                        elif chosen_option_name == "Slits":
                            slits_chosen = "Yes"
                        elif chosen_option_name == "Belt Loops":
                            belt_loops_chosen = "Yes"
                    else:
                        print(f"'{chosen_option_name}' already selected. Please choose another option or 'done'/'d'.")
                else:
                    print("Invalid choice. Please enter a number from the list or 'done'/'d'.")

            if 1 <= selected_complex_count <= 3:
                additional_cost += 35.00
                fabric_adjustment += 1.0
            elif 4 <= selected_complex_count <= 6:
                additional_cost += 70.00
                fabric_adjustment += 2.0
            elif selected_complex_count > 6:
                additional_cost += 70.00
                fabric_adjustment += 2.0


        print("\nChoose Your Fabric(s)")
        fabric_prices = {
            "Polyester": 10.00,
            "Fleece": 11.00,
            "Cotton": 12.00,
            "Stretch Cotton": 13.00,
            "Flannel": 14.00,
            "Rayon": 15.00,
            "Linen": 18.00,
            "Satin": 20.00,
            "Wool": 22.00,
            "Lace": 28.00,
            "Velvet": 30.00,
            "Silk": 35.00,
        }

        def get_fabric_details(part_of_garment=""):
            print(f"\nSelect Fabric for {part_of_garment}:")
            print("Available Fabric Types (Least to Most Expensive):")
            sorted_fabrics = sorted(fabric_prices.items(), key=lambda item: item[1])
            fabric_options_map = {} 
            for i, (fabric, price) in enumerate(sorted_fabrics):
                fabric_options_map[str(i + 1)] = fabric
                print(f"{i + 1}. {fabric} (${price:.2f}/yard)")

            while True:
                try:
                    fabric_choice_num = input("Simply pick a number: ").strip()
                    fabric_name = fabric_options_map.get(fabric_choice_num)
                    if fabric_name:
                        price_per_yard = fabric_prices[fabric_name]
                        break
                    else:
                        print("Invalid choice. Please enter a valid number from the list.")
                except (ValueError, IndexError):
                    print("Invalid choice. Please enter a valid number from the list.")

            while True:
                fabric_style_choice = input("Choose fabric style (1. Solid Color / 2. Print/Pattern): ").strip()
                if fabric_style_choice == "1":
                    fabric_style_type = "Solid Color"
                    break
                elif fabric_style_choice == "2":
                    fabric_style_type = "Print/Pattern"
                    break
                else:
                    print("Invalid choice. Please enter 1 for Solid Color or 2 for Print/Pattern.")

            return fabric_name, fabric_style_type, price_per_yard

        if "Suit (" in garment_name:
            if "Vest" in garment_name:
                front_fabric_name, front_fabric_style, front_price_per_yard = get_fabric_details("Vest Front")
                chosen_fabrics.append({"part": "Vest Front", "name": front_fabric_name, "style": front_fabric_style, "price_per_yard": front_price_per_yard})
                back_fabric_name, back_fabric_style, back_price_per_yard = get_fabric_details("Vest Back")
                chosen_fabrics.append({"part": "Vest Back", "name": back_fabric_name, "style": back_fabric_style, "price_per_yard": back_price_per_yard})

            if "Blazer" in garment_name:
                blazer_fabric_name, blazer_fabric_style, blazer_price_per_yard = get_fabric_details("Blazer")
                chosen_fabrics.append({"part": "Blazer", "name": blazer_fabric_name, "style": blazer_fabric_style, "price_per_yard": blazer_price_per_yard})

            if "Pants" in garment_name:
                pants_fabric_name, pants_fabric_style, pants_price_per_yard = get_fabric_details("Pants")
                chosen_fabrics.append({"part": "Pants", "name": pants_fabric_name, "style": pants_fabric_style, "price_per_yard": pants_price_per_yard})

        elif garment_name in ["Evening Top and Pants", "Evening Top and Shorts", "Camisole and Evening Pants", "Camisole and Evening Shorts"]:
            top_type_for_fabric = "Evening Top" if "Evening Top" in garment_name else "Camisole Top"
            bottom_type_for_fabric = "Pants" if "Pants" in garment_name else "Shorts" 

            top_fabric_name, top_fabric_style, top_price_per_yard = get_fabric_details(top_type_for_fabric)
            chosen_fabrics.append({"part": top_type_for_fabric, "name": top_fabric_name, "style": top_fabric_style, "price_per_yard": top_price_per_yard})

            bottom_fabric_name, bottom_fabric_style, bottom_price_per_yard = get_fabric_details(bottom_type_for_fabric)
            chosen_fabrics.append({"part": bottom_type_for_fabric, "name": bottom_fabric_name, "style": bottom_fabric_style, "price_per_yard": bottom_price_per_yard})

        else: 
            fabric_name, fabric_style_type, price_per_yard = get_fabric_details("your garment")
            chosen_fabrics.append({"part": "Main", "name": fabric_name, "style": fabric_style_type, "price_per_yard": price_per_yard})

        if lining_chosen == "Yes":
            print("\nNow, choose the fabric for the Lining.")
            lining_fabric_name, lining_fabric_style, lining_price_per_yard = get_fabric_details("Lining")
            chosen_fabrics.append({"part": "Lining", "name": lining_fabric_name, "style": lining_fabric_style, "price_per_yard": lining_price_per_yard})

        final_yardage_single_garment = estimated_yardage + fabric_adjustment

        if garment_name == "Dress" and final_yardage_single_garment < 3.0:
            final_yardage_single_garment = 3.0
            print("Note: Dress fabric adjusted to minimum 3 yards, as per policy.")

        total_fabric_cost_single_garment = 0

        if "Suit (" in garment_name:
            vest_front_fabric_data = next((f for f in chosen_fabrics if f["part"] == "Vest Front"), None)
            vest_back_fabric_data = next((f for f in chosen_fabrics if f["part"] == "Vest Back"), None)
            blazer_fabric_data = next((f for f in chosen_fabrics if f["part"] == "Blazer"), None)
            pants_fabric_data = next((f for f in chosen_fabrics if f["part"] == "Pants"), None)
            lining_fabric_data = next((f for f in chosen_fabrics if f["part"] == "Lining"), None)

            blazer_base_yardage = all_garment_details["Blazer"]["base_yardage"] if "Blazer" in garment_name else 0
            vest_base_yardage_front = all_garment_details["Vest"]["base_yardage"] if "Vest" in garment_name else 0
            vest_base_yardage_back_factor = 0.5 
            pants_base_yardage = all_garment_details["Pants"]["base_yardage"] if "Pants" in garment_name else 0

            if vest_front_fabric_data:
                total_fabric_cost_single_garment += vest_base_yardage_front * vest_front_fabric_data["price_per_yard"]
            if vest_back_fabric_data:
                total_fabric_cost_single_garment += (vest_base_yardage_front * vest_base_yardage_back_factor) * vest_back_fabric_data["price_per_yard"] 
            if blazer_fabric_data:
                total_fabric_cost_single_garment += blazer_base_yardage * blazer_fabric_data["price_per_yard"]
            if pants_fabric_data:
                total_fabric_cost_single_garment += pants_base_yardage * pants_fabric_data["price_per_yard"]
            if lining_fabric_data:
                suit_total_base_yardage = blazer_base_yardage + vest_base_yardage_front + (vest_base_yardage_front * vest_base_yardage_back_factor) + pants_base_yardage
                total_fabric_cost_single_garment += suit_total_base_yardage * 0.75 * lining_fabric_data["price_per_yard"]

        elif garment_name in ["Evening Top and Pants", "Evening Top and Shorts", "Camisole and Evening Pants", "Camisole and Evening Shorts"]:
            top_fabric_data = next((f for f in chosen_fabrics if "Top" in f["part"]), None)
            bottom_fabric_data = next((f for f in chosen_fabrics if ("Pants" in f["part"] or "Shorts" in f["part"])), None)
            lining_fabric_data = next((f for f in chosen_fabrics if f["part"] == "Lining"), None)

            top_base_yardage = all_garment_details["Evening"]["base_yardage"] if "Evening Top" in garment_name else all_garment_details["Camisole"]["base_yardage"]
            bottom_base_yardage = all_garment_details["Pants"]["base_yardage"] if "Pants" in garment_name else all_garment_details["Shorts"]["base_yardage"]

            if top_fabric_data:
                total_fabric_cost_single_garment += top_base_yardage * top_fabric_data["price_per_yard"]
            if bottom_fabric_data:
                total_fabric_cost_single_garment += bottom_base_yardage * bottom_fabric_data["price_per_yard"]
            if lining_fabric_data:
                combo_total_base_yardage = top_base_yardage + bottom_base_yardage
                total_fabric_cost_single_garment += combo_total_base_yardage * 0.75 * lining_fabric_data["price_per_yard"]

        else: 
            main_fabric_data = next((f for f in chosen_fabrics if f["part"] == "Main"), None)
            lining_fabric_data = next((f for f in chosen_fabrics if f["part"] == "Lining"), None)

            if main_fabric_data:
                total_fabric_cost_single_garment = final_yardage_single_garment * main_fabric_data["price_per_yard"]
            if lining_fabric_data:
                total_fabric_cost_single_garment += estimated_yardage * 0.75 * lining_fabric_data["price_per_yard"]


        total_cost_single_garment = base_cost + total_fabric_cost_single_garment + additional_cost

        while True:
            try:
                quantity_str = input(f"How many of this '{garment_name}' would you like to order? (Enter a number): ").strip()
                quantity = int(quantity_str)
                if quantity <= 0:
                    print("Quantity must be a positive whole number. Please try again.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a whole number.")

        current_garment_order = {
            "garment_name": garment_name,
            "top_level_category": top_level_category,
            "top_style_choice": top_style_choice,
            "bottom_style_choice": bottom_style_choice,
            "pants_style_choice": pants_style_choice,
            "shorts_style_choice": shorts_style_choice,
            "skirt_style_choice": skirt_style_choice,
            "dress_waistline_choice": dress_waistline_choice,
            "vest_bottom_style": vest_bottom_style,
            "sleeve_chosen_type": sleeve_chosen_type,
            "collar_choice": collar_choice,
            "selected_customizations": complex_customizations_chosen, 
            "complex_customizations_chosen": complex_customizations_chosen,
            "other_complex_description": other_complex_description,
            "required_measurements_for_this_garment": list(set(required_measurements_for_current_garment)),
            "chosen_fabrics": chosen_fabrics,
            "final_yardage_single_garment": final_yardage_single_garment,
            "base_cost_single_garment": base_cost,
            "additional_customization_cost_single_garment": additional_cost,
            "total_fabric_cost_single_garment": total_fabric_cost_single_garment,
            "total_cost_per_unit": total_cost_single_garment,
            "quantity": quantity
        }
        completed_orders.append(current_garment_order)
        print(f"\n'{quantity} x {garment_name}' added to your order!")

        for meas in required_measurements_for_current_garment:
            all_required_measurements.add(meas)

        add_another = "" 
        while True:
            add_another = input("Would you like to add another garment to your order? (yes/no): ").strip().lower()
            if add_another in ["yes", "y"]:
                break
            elif add_another in ["no", "n"]:
                print("Proceeding to measurement collection and final order summary...")
                break
            else:
                print("Invalid choice. Please enter 'yes' or 'no'.")

        if add_another in ["no", "n"]:
            break

    potential_combos = {
        "Suit (Vest/Blazer/Pants)": {"components": ["Vest", "Blazer", "Pants"], "combo_cost_factor": 0.90}, 
        "Suit (Vest/Blazer)": {"components": ["Vest", "Blazer"], "combo_cost_factor": 0.90},
        "Suit (Vest/Pants)": {"components": ["Vest", "Pants"], "combo_cost_factor": 0.90},
        "Suit (Blazer/Pants)": {"components": ["Blazer", "Pants"], "combo_cost_factor": 0.90},
        "Evening Top and Pants": {"components": ["Evening", "Pants"], "combo_cost_factor": 0.90},
        "Evening Top and Shorts": {"components": ["Evening", "Shorts"], "combo_cost_factor": 0.90},
        "Camisole and Evening Pants": {"components": ["Camisole", "Pants"], "combo_cost_factor": 0.90},
        "Camisole and Evening Shorts": {"components": ["Camisole", "Shorts"], "combo_cost_factor": 0.90},
    }

    offered_combo_this_session = False 

    if not any(order["top_level_category"] == "Combo" for order in completed_orders) and completed_orders:
        
        current_individual_garments_tally = {}
        for order_item in completed_orders:
            if order_item["top_level_category"] != "Combo":
                garment_type = order_item["garment_name"]
                current_individual_garments_tally[garment_type] = current_individual_garments_tally.get(garment_type, 0) + order_item["quantity"]
        
        for combo_name, combo_data in potential_combos.items():
            components_needed = combo_data["components"]
            combo_cost_factor = combo_data["combo_cost_factor"]
            
            can_form_this_combo = True
            
            for comp in components_needed:
                if current_individual_garments_tally.get(comp, 0) < 1: 
                    can_form_this_combo = False
                    break
            
            if can_form_this_combo:
                print(f"\n--- Special Offer! ---")
                print(f"It looks like you've selected individual items that can form a '{combo_name}'.")
                print(f"If you combine these into the '{combo_name}', you can receive a {int((1 - combo_cost_factor) * 100)}% discount!")
                confirm_combo = input("Would you like to take advantage of this offer? (yes/no): ").strip().lower()

                if confirm_combo in ["yes", "y"]:
                    print(f"Great! Applying {int((1 - combo_cost_factor) * 100)}% discount to your '{combo_name}'.")
                    offered_combo_this_session = True

                    new_completed_orders = []
                    
                    consumed_items_info = {comp: 0 for comp in components_needed} 

                    for original_order_item in completed_orders:
                        current_garment_name = original_order_item["garment_name"]
                        current_quantity = original_order_item["quantity"]

                        if current_garment_name in components_needed and consumed_items_info[current_garment_name] < 1:
                            if current_quantity > 1:
                                temp_order_item = original_order_item.copy()
                                temp_order_item["quantity"] -= 1
                                temp_order_item["total_cost_per_unit"] = temp_order_item["base_cost_single_garment"] + temp_order_item["total_fabric_cost_single_garment"] + temp_order_item["additional_customization_cost_single_garment"]
                                new_completed_orders.append(temp_order_item)
                            consumed_items_info[current_garment_name] += 1
                        else:
                            new_completed_orders.append(original_order_item)
                    
                    combo_details = get_garment_details(combo_name)
                    
                    new_combo_base_cost_before_discount = combo_details["base_cost"]
                    discounted_base_cost = new_combo_base_cost_before_discount * combo_cost_factor

                    new_combo_estimated_yardage = combo_details["base_yardage"]


                    new_combo_chosen_fabrics = []
                    new_combo_additional_cost = 0
                    new_combo_lining_present = False
                    
                    for original_order_item in completed_orders:
                        if original_order_item["garment_name"] in components_needed and "Lining" in original_order_item["complex_customizations_chosen"]:
                            new_combo_lining_present = True
                            break 

                    default_fabric_name = "Cotton"
                    default_price_per_yard = fabric_prices[default_fabric_name]

                    new_combo_chosen_fabrics.append({"part": "Main", "name": default_fabric_name, "style": "Solid Color", "price_per_yard": default_price_per_yard})
                    
                    new_combo_total_fabric_cost = new_combo_estimated_yardage * default_price_per_yard
                    if new_combo_lining_present:
                        new_combo_total_fabric_cost += (new_combo_estimated_yardage * 0.75) * default_price_per_yard 
                        new_combo_chosen_fabrics.append({"part": "Lining", "name": default_fabric_name, "style": "Solid Color", "price_per_yard": default_price_per_yard})
                        new_combo_additional_cost += 25.00 

                    new_combo_total_cost_per_unit = (
                        discounted_base_cost +
                        new_combo_total_fabric_cost +
                        new_combo_additional_cost
                    )

                    new_combo_order_item = {
                        "garment_name": combo_name,
                        "top_level_category": "Combo",
                        "top_style_choice": "N/A", 
                        "bottom_style_choice": "N/A",
                        "pants_style_choice": "N/A",
                        "shorts_style_choice": "N/A",
                        "skirt_style_choice": "N/A",
                        "dress_waistline_choice": "N/A",
                        "vest_bottom_style": "N/A",
                        "sleeve_chosen_type": "N/A",
                        "collar_choice": "N/A",
                        "selected_customizations": ["Lining"] if new_combo_lining_present else [], 
                        "complex_customizations_chosen": ["Lining"] if new_combo_lining_present else [],
                        "other_complex_description": "N/A",
                        "required_measurements_for_this_garment": list(set(combo_details["measurements"])),
                        "chosen_fabrics": new_combo_chosen_fabrics,
                        "final_yardage_single_garment": new_combo_estimated_yardage,
                        "base_cost_single_garment": discounted_base_cost,
                        "additional_customization_cost_single_garment": new_combo_additional_cost,
                        "total_fabric_cost_single_garment": new_combo_total_fabric_cost,
                        "total_cost_per_unit": new_combo_total_cost_per_unit,
                        "quantity": 1 
                    }
                    new_completed_orders.append(new_combo_order_item)
                    
                    completed_orders = new_completed_orders

                    all_required_measurements.clear()
                    for order in completed_orders:
                        for meas in order["required_measurements_for_this_garment"]:
                            all_required_measurements.add(meas)
                    
                    print(f"Your order has been updated to include the '{combo_name}' with the discount.")
                    break 
                else:
                    print("No problem! Your individual selections will remain as is.")
                    break 

            if offered_combo_this_session: 
                break

    if completed_orders:
        print("\n" + "="*40)
        print("       Time for Measurements!")
        print("="*40)
        print("Please follow the instructions below to take all necessary measurements.")
        print("Enter each measurement in inches (e.g., 34.5).")

        sorted_required_measurements = sorted(list(all_required_measurements))

        for measurement_name in sorted_required_measurements:
            while True:
                try:
                    print(f"\nMeasurement: {measurement_name}")
                    print(f"Guide: {measurement_descriptions.get(measurement_name, 'Please measure carefully.')}")
                    value = float(input(f"Enter your {measurement_name} measurement (in inches): ").strip())
                    if value <= 0:
                        print("Measurement must be a positive number. Please try again.")
                    else:
                        customer_measurements_session[measurement_name] = value
                        break
                except ValueError:
                    print("Invalid input. Please enter a number (e.g., 34 or 34.5).")

        print("\nThank you for providing your precise measurements!")

    print("\n" + "="*40)
    print("       Your Complete Custom Order Summary")
    print("="*40)

    grand_total_cost = 0

    if not completed_orders:
        print("\nNo garments were added to your order.")
    else:
        print("\n--- Internal Design Details: Customer Measurements ---")
        if customer_measurements_session:
            for m_name in sorted(customer_measurements_session.keys()):
                print(f"  - {m_name}: {customer_measurements_session[m_name]:.1f} inches")
        else:
            print("  No measurements were collected during this session.")
        print("-" * 40)

        print("\n--- Garment Details (Customer View) ---")
        for i, order in enumerate(completed_orders):
            description_lines = []

            garment_display_prefix = ""
            if order['sleeve_chosen_type'] != "N/A":
                garment_display_prefix += f"{order['sleeve_chosen_type']} "

            garment_display_name = order['garment_name']

            if order['garment_name'] == "Pants" and order['pants_style_choice'] != "N/A":
                garment_display_name = f"{order['pants_style_choice']} Pants"
            elif order['garment_name'] == "Shorts" and order['shorts_style_choice'] != "N/A":
                garment_display_name = f"{order['shorts_style_choice']} Shorts"
            elif order['garment_name'] == "Skirt" and order['skirt_style_choice'] != "N/A":
                garment_display_name = f"{order['skirt_style_choice']} Skirt"
            elif order['garment_name'] == "Evening":
                garment_display_name = "Evening Top"
            elif order['garment_name'] == "Camisole":
                garment_display_name = "Camisole Top"

            if order['top_level_category'] == "Combo": 
                main_line = f"{order['quantity']} - {order['garment_name']}"
            else: 
                main_line = f"{order['quantity']} - {garment_display_prefix}{garment_display_name}"
            description_lines.append(main_line)

            if "Suit (" in order['garment_name']:
                vest_front_fabric = next((f for f in order['chosen_fabrics'] if f["part"] == "Vest Front"), None)
                vest_back_fabric = next((f for f in order['chosen_fabrics'] if f["part"] == "Vest Back"), None)
                blazer_fabric = next((f for f in order['chosen_fabrics'] if f["part"] == "Blazer"), None)
                pants_fabric = next((f for f in order['chosen_fabrics'] if f["part"] == "Pants"), None)

                if vest_front_fabric:
                    description_lines.append(f"  {vest_front_fabric['name']} {vest_front_fabric['style']} Vest Front")
                if vest_back_fabric:
                    description_lines.append(f"  {vest_back_fabric['name']} {vest_back_fabric['style']} Vest Back")
                if blazer_fabric:
                    description_lines.append(f"  {blazer_fabric['name']} {blazer_fabric['style']} Blazer")
                if pants_fabric:
                    description_lines.append(f"  {pants_fabric['name']} {pants_fabric['style']} Pants")
            elif " and " in order['garment_name']: 
                top_fabric = next((f for f in order['chosen_fabrics'] if "Top" in f["part"]), None)
                bottom_fabric = next((f for f in order['chosen_fabrics'] if ("Pants" in f["part"] or "Shorts" in f["part"])), None)
                if top_fabric:
                    description_lines.append(f"  {top_fabric['name']} {top_fabric['style']} Top")
                if bottom_fabric:
                    description_lines.append(f"  {bottom_fabric['name']} {bottom_fabric['style']} Bottom")
            else: 
                main_fabric = next((f for f in order['chosen_fabrics'] if f["part"] == "Main"), None)
                if main_fabric:
                    description_lines.append(f"  {main_fabric['name']} {main_fabric['style']}")
            
            lining_fabric = next((f for f in order['chosen_fabrics'] if f["part"] == "Lining"), None)
            if lining_fabric:
                description_lines.append(f"  Lining: {lining_fabric['name']} {lining_fabric['style']}")


            if order['collar_choice'] != "N/A":
                description_lines.append(f"  Collar: {order['collar_choice']}")

            if order['dress_waistline_choice'] != "N/A":
                description_lines.append(f"  Waistline: {order['dress_waistline_choice']}")
            
            if order['vest_bottom_style'] != "N/A":
                description_lines.append(f"  Vest Bottom Style: {order['vest_bottom_style']}")
            
            if 'button_placement_choice' in order and order['button_placement_choice'] != "N/A":
                description_lines.append(f"  Button Placement: {order['button_placement_choice']}")

            if order['complex_customizations_chosen']:
                description_lines.append("  Complex Details:")
                for complex_item in order['complex_customizations_chosen']:
                    description_lines.append(f"    - {complex_item}")


            for line in description_lines:
                print(line)
            print()

            item_total_cost = order['total_cost_per_unit'] * order['quantity']
            grand_total_cost += item_total_cost

        print("\n" + "="*40)
        print("         Financial Summary")
        print("="*40)
        for order in completed_orders:
            garment_display_name_summary = order['garment_name']

            if order['garment_name'] == "Pants" and order['pants_style_choice'] != "N/A":
                 garment_display_name_summary = f"{order['pants_style_choice']} Pants"
            elif order['garment_name'] == "Shorts" and order['shorts_style_choice'] != "N/A":
                garment_display_name_summary = f"{order['shorts_style_choice']} Shorts"
            elif order['garment_name'] == "Skirt" and order['skirt_style_choice'] != "N/A":
                garment_display_name_summary = f"{order['skirt_style_choice']} Skirt"
            elif order['garment_name'] == "Evening":
                garment_display_name_summary = "Evening Top"
            elif order['garment_name'] == "Camisole":
                garment_display_name_summary = "Camisole Top"

            if order['top_level_category'] != "Combo":
                if order['sleeve_chosen_type'] != "N/A":
                    garment_display_name_summary = f"{order['sleeve_chosen_type']} {garment_display_name_summary}"
                if order['collar_choice'] != "N/A":
                    if order['collar_choice'] != "No collar" and "Camisole" not in garment_display_name_summary and "Vest" not in garment_display_name_summary and "Blazer" not in garment_display_name_summary:
                        garment_display_name_summary = f"{order['collar_choice'].replace(' collar', '')} {garment_display_name_summary}"

            if order['quantity'] > 1:
                garment_display_name_summary += f" ({order['quantity']}x)"

            item_total_cost = order['total_cost_per_unit'] * order['quantity']
            print(f"{garment_display_name_summary} - ${item_total_cost:.2f}")

    print(f"\nTotal Order - ${grand_total_cost:.2f}")

    print("\nThis is an **estimated cost**. The final price may vary slightly based on final design discussions.")
    print("You will receive a detailed invoice upon final order confirmation.")
    print("When you are ready, you can proceed to the 'Pay now' or 'Finished' option to finalize your order.")

    print("Your custom piece(s) will be made precisely to the measurements you provided.")
    print("\nThank you for choosing Kate's Couture for your custom garment!")

run_kates_couture_app()