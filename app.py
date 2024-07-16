# app.py
from flask import Flask, render_template, request, jsonify
import itertools
import math
from collections import Counter
from scipy.special import comb

app = Flask(__name__)

def probability_of_4_different_types_refined(deck, X):
    card_types = list(deck.keys())
    num_types = len(card_types)
    total_cards = sum(deck.values())
    
    total_combinations = comb(total_cards, X, exact=True)
    
    def count_unique_types(combination, X):
        type_counter = Counter()
        for card_type, count in zip(card_types, combination):
            if card_type == 'artifact_creatures':
                if X >= 4:
                    type_counter['artifacts'] += count
                    type_counter['creatures'] += count
                else:
                    type_counter['artifact_creatures'] += count
            else:
                type_counter[card_type] += count
        if X < 4:
            return len([type for type, count in type_counter.items() if count > 0 and type != 'artifact_creatures'])
        else:
            return len([type for type, count in type_counter.items() if count > 0])

    favorable_outcomes = 0
    for combination in itertools.product(*[range(deck[card_type] + 1) for card_type in card_types]):
        if sum(combination) == X and count_unique_types(combination, X) >= 4:
            ways = math.prod([comb(deck[card_types[i]], combination[i], exact=True) for i in range(num_types)])
            favorable_outcomes += ways
    
    probability = favorable_outcomes / total_combinations
    return probability

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    deck = {
        'lands': int(request.form['lands']),
        'creatures': int(request.form['creatures']),
        'artifacts': int(request.form['artifacts']),
        'artifact_creatures': int(request.form['artifact_creatures']),
        'instants': int(request.form['instants']),
        'sorceries': int(request.form['sorceries']),
        'enchantments': int(request.form['enchantments']),
        'planeswalkers': int(request.form['planeswalkers'])
    }
    
    probabilities = {X: probability_of_4_different_types_refined(deck, X) for X in range(11)}
    return jsonify(probabilities)

if __name__ == '__main__':
    app.run(debug=True)
