from graphviz import Digraph

class GraphvizGenerator:
    @staticmethod
    def generate_graphviz_svg(nfa):
        """
        Genera un gráfico SVG de un NFA usando Graphviz.
        """
        dot = Digraph(format="svg")
        dot.attr(rankdir="LR", fontname="Helvetica,Arial,sans-serif")

        # Añadir nodos finales (doublecircle)
        dot.attr("node", shape="doublecircle")
        for state in nfa.final_states:
            dot.node(state)

        # Añadir nodos normales
        dot.attr("node", shape="circle")
        for state in nfa.states:
            if state not in nfa.final_states:
                dot.node(state)

        # Añadir transiciones
        for src, transitions in nfa.transitions.items():
            for symbol, destinations in transitions.items():
                for dest in destinations:
                    dot.edge(src, dest, label=symbol)

        # Retornar el gráfico en formato SVG
        return dot.pipe().decode("utf-8")
