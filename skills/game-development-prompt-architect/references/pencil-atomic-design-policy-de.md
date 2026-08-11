# Kanonische Pencil-Regel des Nutzers

Der folgende Block bleibt als kanonische Fassung unverändert erhalten:

> Du arbeitest in Pencil ausschließlich über das Pencil-MCP. Direkte Dateiänderungen außerhalb des Pencil-MCPs sind nicht erlaubt.
>
> Wenn wir in Pencil arbeiten, verwenden wir grundsätzlich das Atomic-Design-Framework. Das bedeutet: Designs werden systematisch von kleinen, wiederverwendbaren Bausteinen zu vollständigen Seiten aufgebaut. Die Hierarchie lautet:
>
> Atoms → Molecules → Organisms → Templates → Pages
>
> Alle Elemente dieser Hierarchie werden im Pencil-Component-System als wiederverwendbare Components angelegt. Atoms, Molecules, Organisms und Templates sind also jeweils eigenständige Components. Ziel ist es, zuerst die kleinsten Bausteine sauber zu definieren und diese anschließend konsequent in größeren Strukturen wiederzuverwenden.
>
> Dabei ist besonders wichtig, die Atomic-Design-Hierarchie einzuhalten:
> - Zuerst werden Atoms erstellt, zum Beispiel Farben, Typografie, Buttons, Icons, Abstände oder einfache UI-Elemente.
> - Danach werden Molecules aus bestehenden Atoms zusammengesetzt.
> - Organisms entstehen aus Atoms und Molecules.
> - Templates kombinieren Organisms zu wiederverwendbaren Seitenstrukturen.
> - Pages basieren auf Templates und stellen konkrete Ausprägungen dar.
>
> Zusätzlich arbeiten wir mit einem Token- bzw. Variablen-System, wie es in professionellen Designsystemen üblich ist. Werte wie Farben, Schriftgrößen, Abstände, Radien, Schatten, Layout-Größen oder andere Designwerte dürfen nicht hartcodiert werden. Stattdessen müssen sie als Variablen bzw. Design Tokens definiert und verwendet werden.
>
> Dabei gelten folgende Grundsätze:
> - Keine direkten Hex-Codes verwenden, sondern Farbvariablen.
> - Keine festen Radiuswerte verwenden, sondern Radius-Variablen.
> - Keine festen Größen oder Abstände verwenden, sondern passende Size- und Spacing-Variablen.
> - Keine doppelten oder unnötigen Variablen anlegen.
> - Vor dem Erstellen neuer Variablen prüfen, ob bereits passende Tokens existieren.
> - So wenige Variablen wie möglich, aber so viele wie nötig verwenden.
> - Alle Components sollen konsistent auf denselben Tokens basieren.
>
> Wir arbeiten außerdem immer mit einer klaren Seitenstruktur innerhalb von Pencil, wie man sie aus Figma und professionellen Designsystemen kennt.
>
> Es gibt eine eigene Components-Page, die ausschließlich für wiederverwendbare Designbausteine vorgesehen ist. Auf dieser Components-Page werden Atoms, Molecules, Organisms und Templates sinnvoll strukturiert, gruppiert und benannt. Diese Seite dient nicht zum Bau konkreter Produktseiten, sondern ausschließlich zur Pflege und Organisation des Component-Systems.
>
> Zusätzlich gibt es eine eigene Tokens-Page. Diese Seite ist ausschließlich für Design Tokens bzw. Variablen vorgesehen, zum Beispiel Farben, Typografie, Abstände, Radien, Größen, Schatten und weitere systemweite Designwerte. Die Tokens-Page dient als zentrale Referenz für alle verwendeten Variablen.
>
> Die Seitenstruktur soll grundsätzlich so aufgebaut sein:
> - Links befindet sich die Components-Page.
> - Daneben befindet sich die Tokens-Page.
> - Rechts davon befinden sich die normalen Pages, also die konkret gebauten Produkt-, Website- oder App-Seiten.
>
> Dadurch bleiben Systembestandteile und konkrete Seiten klar voneinander getrennt. Components und Tokens werden zentral gepflegt und anschließend auf den eigentlichen Pages wiederverwendet.
>
> Das Ziel ist ein sauberes, konsistentes und skalierbares Designsystem in Pencil, das vollständig auf wiederverwendbaren Components und zentral verwalteten Variablen basiert.

## Verbindliche Ergänzung für Game UI

- Die Regel „keine direkten Dateiänderungen außerhalb des Pencil-MCPs“ bezieht sich auf Pencil-Dokumente, Canvas-Daten, Nodes, Components, Variablen und Referenzen. Echte externe Quelldateien wie `.js`, `.glsl`, Bilder oder Fonts dürfen als normale Dateien erstellt und versioniert werden; ihre Einbindung in Pencil erfolgt ausschließlich über Pencil MCP.
- Pencil-Script-Nodes dürfen echte relative `.js`-Dateien verwenden. Diese bleiben deterministisch, token-gesteuert und mit der Pencil-Sandbox kompatibel; sie setzen keinen DOM-, Netzwerk-, Dateisystem- oder Async-Zugriff voraus.
- Shader-Studien verwenden wirkliche `.glsl`-Dateien mit Pencil-kompatiblem WebGL/GLSL-Vertrag, `#version 100`, dokumentierten Uniforms, Resolution-Handling, stabilen IDs, Token-zu-Uniform-Mapping, Referenz-Captures und Performance-Grenzen.
- Pencil-GLSL ist eine echte Design-Referenz. Für das Spiel wird es in Unreal-HLSL/Materialien, Unity-ShaderLab/HLSL beziehungsweise Godot-Shadercode übertragen und durch kontrollierte Paritäts-Captures verifiziert. Direkte Wiederverwendung ist nur nach nachgewiesener Kompatibilität erlaubt.
