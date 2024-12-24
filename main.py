import sys
from nfa.nfa import NFA
from nfa.mermaid_generator import MermaidGenerator
from nfa.graphviz_generator import GraphvizGenerator

def generate_html(nfa_text, mermaid_code, graphviz_svg):
    """
    Genera el contenido del archivo HTML con ambos gráficos (Mermaid y Graphviz).
    """
    template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Visualizador de NFA</title>
        <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
        <script>
            mermaid.initialize({{startOnLoad: true}});
        </script>
    </head>
    <body>
        <h1>Definición del NFA</h1>
        <pre>{nfa_text}</pre>

        <h1>Gráfico Generado con Mermaid</h1>
        <div class="mermaid">
            {mermaid_code}
        </div>

        <h1>Gráfico Generado con Graphviz</h1>
        <div>
            {graphviz_svg}
        </div>
    </body>
    </html>
    """
    return template.format(nfa_text=nfa_text, mermaid_code=mermaid_code, graphviz_svg=graphviz_svg)


def main(input_json, output_html):
    # Leer el NFA desde el archivo JSON
    nfa = NFA.from_json(input_json)

    # Obtener la definición estándar del NFA
    nfa_text = nfa.to_standard_definition()

    # Generar el gráfico Mermaid
    mermaid_code = MermaidGenerator.generate_mermaid(nfa)

    # Generar el gráfico SVG con Graphviz
    graphviz_svg = GraphvizGenerator.generate_graphviz_svg(nfa)

    # Generar el archivo HTML con ambos gráficos
    html_content = generate_html(nfa_text, mermaid_code, graphviz_svg)

    # Guardar el archivo HTML
    with open(output_html, "w") as file:
        file.write(html_content)

    print(f"NFA visualizado en: {output_html}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python main.py <archivo_entrada.json> <archivo_salida.html>")
        sys.exit(1)

    input_json = sys.argv[1]
    output_html = sys.argv[2]
    main(input_json, output_html)
