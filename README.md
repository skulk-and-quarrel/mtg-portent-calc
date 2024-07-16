# Portent of Calamity Calculator

This web application calculates the probability of drawing at least four different card types in a Magic: The Gathering deck for the card named [Portent of Calamity](https://scryfall.com/card/blb/66/portent-of-calamity) based on user-defined deck composition.

## Features

- Input custom deck composition
- Calculate probabilities for drawing 0 to 10 cards
- Display results in an interactive line chart
- Responsive web design

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have installed Python 3.7 or later
- You have a basic understanding of Python and Flask

## Installing MTG Probability Calculator

To install the MTG Probability Calculator, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/skulk-and-quarrel/mtg-portent-calc.git
   cd mtg-portent-calc
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Using MTG Probability Calculator

To use the MTG Probability Calculator, follow these steps:

1. Ensure you're in the project directory and your virtual environment is activated (if you're using one).

2. Run the Flask application:
   ```
   python app.py
   ```

3. Open a web browser and navigate to `http://127.0.0.1:5000/`

4. Input your deck composition in the form and click "Calculate Probabilities"

5. View the results in the interactive chart

## Contributors

Thanks Claude!

## License

This project uses the following license: [MIT License](<link_to_license_file>).
