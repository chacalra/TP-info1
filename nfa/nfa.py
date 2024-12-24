import json

class NFA:
    def __init__(self, states, alphabet, transitions, start_state, final_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.final_states = final_states

    @classmethod
    def from_json(cls, json_path):
        """Carga el NFA desde un archivo JSON."""
        with open(json_path, 'r') as file:
            data = json.load(file)

        # Construir el diccionario de transiciones desde Delta
        transitions = {}
        for transition in data['Delta']:
            state, symbol, destinations = transition
            if state not in transitions:
                transitions[state] = {}
            transitions[state][symbol] = destinations

        return cls(
            states=data['Q'],
            alphabet=data['Sigma'],
            transitions=transitions,
            start_state=data['q0'],
            final_states=data['F']
        )

    def to_standard_definition(self):
        """Devuelve la representación estándar del NFA."""
        transitions_text = [
            f"δ({state},{symbol}) = {{{','.join(destinations)}}}"
            for state, trans in self.transitions.items()
            for symbol, destinations in trans.items()
        ]
        return (
            f"Q = {self.states}\n"
            f"Σ = {self.alphabet}\n"
            f"δ = {{\n  " + "\n  ".join(transitions_text) + "\n}}\n"
            f"q0 = {self.start_state}\n"
            f"F = {self.final_states}"
        )
