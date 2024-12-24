from graphviz import Digraph

class MermaidGenerator:
    @staticmethod
    def generate_mermaid(nfa):
        """
        Genera el código Mermaid para visualizar el NFA de forma organizada.
        """
        transitions = ["stateDiagram-v2", "direction LR"]

        # Marcar el estado inicial
        transitions.append(f'[*] --> {nfa.start_state}')

        # Crear transiciones agrupadas
        for state, trans in nfa.transitions.items():
            grouped_transitions = {}  # Agrupa destinos por símbolo
            for symbol, destinations in trans.items():
                for dest in destinations:
                    if (state, dest) not in grouped_transitions:
                        grouped_transitions[(state, dest)] = []
                    grouped_transitions[(state, dest)].append(symbol)

            # Añadir transiciones agrupadas
            for (src, dest), symbols in grouped_transitions.items():
                symbol_label = ",".join(symbols)  # Agrupar símbolos
                transitions.append(f'{src} --> {dest} : {symbol_label}')

        # Marcar estados finales con doble círculo y estilo
        for final_state in nfa.final_states:
            transitions.append(f'style {final_state} fill:#f9f,stroke:#333,stroke-width:2px;')

        return "\n".join(transitions)
