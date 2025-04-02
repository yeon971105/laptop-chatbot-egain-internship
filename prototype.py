# --------------------------------------------------------
# Laptop Whisperer: A Chatbot for Laptop Recommendations
# Scenario: Assisting a customer with choosing the right laptop
# --------------------------------------------------------

def budget():
    """
    Ask the user for their budget range.
    Offers three predefined choices.
    If input is invalid, assumes default value of '1' (under $600).
    """
    print("Hey there! Let’s talk budgets—what’s your price range for a shiny new laptop?")
    print("1. Keeping it chill under $600")
    print("2. Mid-range magic between $600 and $1000")
    print("3. Splurging over $1000 for the good stuff")

    while True:
        budget_choice = input("Just pick 1, 2, or 3, and we’ll get rolling: ").strip()
        if budget_choice in ['1', '2', '3']:
            return budget_choice
        else:
            print("\nHmm, that’s not quite what I expected! No worries, let’s assume you’re leaning toward the under $600 vibe for now.")
            return '1'  # default assumption


def usage():
    """
    Ask the user about the primary purpose of the laptop.
    Offers three common use cases.
    If input is invalid, assumes default value of '1' (Office/School).
    """
    print("\nOkay, next big question: What’s the main thing you’ll be doing with your laptop?")
    print("1. Crushing it at office work or school stuff")
    print("2. Diving into epic gaming adventures")
    print("3. Unleashing your inner artist with video or photo editing")

    while True:
        usage_choice = input("Pick 1, 2, or 3, and let’s see what fits: ").strip()
        if usage_choice in ['1', '2', '3']:
            return usage_choice
        else:
            print("\nOh, I think we might’ve crossed wires there! Let’s go with office/school work as a safe bet for now.")
            return '1'  # default assumption


def weight():
    """
    Ask the user if portability is important.
    Continues to prompt until a valid 'yes' or 'no' answer is received.
    """
    while True:
        print("\nDo you dream of a laptop that’s light as a feather and easy to carry around?")
        portability_answer = input("Just say ‘yes’ or ‘no’, and we’re golden: ").strip().lower()
        if portability_answer in ['yes', 'no']:
            return portability_answer
        else:
            print("\nHehe, let’s try that again! I’m all ears for a simple ‘yes’ or ‘no’.")


def suggest_laptop(budget, usage, portability):
    """
    Given budget, usage, and portability preferences,
    recommend a laptop based on rule-based logic.
    """
    if budget == '1' and usage == '1' and portability == 'yes':
        return "Lenovo IdeaPad 3 – perfect for light work on the go!"
    elif budget == '2' and usage == '2' and portability == 'no':
        return "Acer Nitro 5 – your new gaming beast, no suitcase needed!"
    elif budget == '3' and usage == '3' and portability == 'yes':
        return "MacBook Pro 14\" – sleek, powerful, and ready to create anywhere!"
    elif budget == '1' and usage == '2' and portability == 'no':
        return "HP Pavilion Gaming – budget-friendly fun for your games!"
    elif budget == '2' and usage == '1' and portability == 'yes':
        return "Dell XPS 13 – stylish, portable, and great for work!"
    elif budget == '3' and portability == 'no':
        return "MSI Creator Z16 – a powerhouse for creators who stay put!"
    else:
        return "Dell Inspiron 15 – a solid all-arounder to keep you happy!"


def main():
    """
    Main driver of the chatbot conversation.
    Welcomes the user, asks all key questions, and prints the recommendation.
    """
    print("Hi! I’m your Laptop Whisperer, here to match you with your perfect tech soulmate!\n")
    print("Let’s have a quick chat, and I’ll find just the right laptop for you. Sound good?")

    # Collect user preferences
    budget_pick = budget()
    usage_pick = usage()
    portability_pick = weight()

    # Determine best match
    perfect_match = suggest_laptop(budget_pick, usage_pick, portability_pick)

    # Present the result
    print("\nBased on what you told me, here’s my top pick:")
    print("-------------------------------------------------")
    print(f"  {perfect_match}")
    print("-------------------------------------------------")
    print("I hope you love it as much as I do! Thanks for letting me help—you’re awesome!")


# Run the chatbot
if __name__ == "__main__":
    main()
