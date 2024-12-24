# Visualizador de NFA

**Autor:** Ramón Chacal  
**Matrícula:** Y26019 

Este proyecto implementa un visualizador de **Autómatas Finitos No Deterministas (NFA)**, tomando como entrada un archivo JSON con la definición del NFA y generando un archivo HTML que incluye representaciones gráficas tanto en **Mermaid** como en **Graphviz**. El archivo HTML también contiene la definición estándar del NFA en un formato textual para facilitar su análisis.

---

## **Formato de Entrada**

El programa acepta un archivo JSON con la siguiente estructura:

```json
{
    "type": "nfa",
    "Q": ["q0", "q1", "q2"],
    "Sigma": ["a", "b"],
    "Delta": [
        ["q0", "a", ["q0", "q1"]],
        ["q0", "b", ["q0"]],
        ["q1", "a", ["q2"]],
        ["q1", "b", ["q2"]],
        ["q2", "a", ["q2"]],
        ["q2", "b", ["q2"]]
    ],
    "q0": "q0",
    "F": ["q2"]
}

```
## **Salida Generada**

El programa genera un archivo `output.html` que incluye:

1. La definición estándar del NFA (`Q`, `Σ`, `δ`, `q0`, `F`).
2. Un gráfico generado con **Mermaid**.
3. Un gráfico generado con **Graphviz**.

---

## **Instalación**

1. **Clonar el repositorio**:
   ```bash
   git clone <URL del repositorio>
   cd <nombre-del-repositorio>
   pip install graphviz




## **Justificación del Uso de Graphviz**

Inicialmente, el proyecto utilizaba exclusivamente **Mermaid** para la visualización de los NFA. Sin embargo, durante el desarrollo, se observó que:

### **Limitaciones en la Representación Visual**
- **Mermaid** no ofrece un control fino sobre la disposición de los nodos, especialmente para self-loops y transiciones entre múltiples nodos.

### **Estética del Diagrama**
- Los diagramas generados con **Graphviz** presentan una estructura visualmente más clara y profesional.
- Graphviz tiene capacidades avanzadas para organizar automáticamente los nodos y las transiciones, ofreciendo un diseño más limpio y legible.

Por estas razones, se decidió incluir **Graphviz** como una alternativa visual. Ambos gráficos se presentan en el HTML generado, permitiendo al usuario elegir el que mejor se adapte a sus necesidades.



