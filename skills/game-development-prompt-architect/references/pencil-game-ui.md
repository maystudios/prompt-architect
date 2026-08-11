# Pencil Rules for Game UI

The user's canonical German policy is preserved verbatim in `pencil-atomic-design-policy-de.md`. Load it together with this file and preserve every requirement when compiling the English Goal; this file adds the operational script, GLSL, and engine-parity interpretation without weakening that policy.

## Exclusive Pencil access

Work inside Pencil exclusively through Pencil MCP. Do not modify `.pen` canvas data, nodes, components, variables, references, or its serialized representation directly outside Pencil MCP.

Real external source files are allowed and encouraged: `.js` scripts, `.glsl` shaders, images, fonts, captures, and other assets may be normal Git-tracked files. Create or edit their Pencil references only through Pencil MCP.

## Atomic Design

Build every design systematically:

`Atoms → Molecules → Organisms → Templates → Pages`

Create Atoms, Molecules, Organisms, and Templates as reusable Pencil components. Compose each layer from existing smaller components before introducing a duplicate. Pages are concrete states based on Templates.

- Atoms: semantic colors, typography, icons, buttons, focus rings, spacing primitives, reticles, simple indicators.
- Molecules: labeled controls, stat rows, inventory slots, ability prompts, dialog choices.
- Organisms: HUD clusters, menus, inventories, quest panels, multiplayer rosters.
- Templates: reusable screen/layout structures with state slots.
- Pages: concrete game screens and variants such as input method, resolution, localization, accessibility, pause, combat, and failure states.

## Tokens and variables

Do not hard-code design values when Pencil variables can express them. Define and reuse tokens for colors, typography, spacing, sizes, radii, shadows, layout, motion values, and other system values.

- no direct hex colors in components; use semantic color variables;
- no fixed radii, sizes, or spacing where a token applies;
- check for an existing token before creating one;
- create as few variables as possible and as many as necessary;
- make components consume the same canonical tokens;
- separate primitive values from semantic/game-state aliases when that enables themes or accessibility modes.

## Canvas structure

Maintain clearly labeled top-level regions on Pencil's canvas:

1. Components area on the left, containing organized Atoms, Molecules, Organisms, and Templates only.
2. Tokens area beside it, showing central variables and useful specimens.
3. Concrete product/game Pages to the right.

When Pencil represents these as large top-level frames rather than literal document pages, preserve the same spatial order and separation. Use a `.lib.pen` design library when shared components must span multiple files.

## Scripts

Pencil script nodes may reference real relative `.js` source files. Keep scripts deterministic, token-driven, small, and sandbox-compatible. Do not assume DOM, network, filesystem, asynchronous, or undeclared runtime access. The source file is authoritative; regenerate or resynchronize the canvas result through Pencil MCP after changes.

## Real GLSL shaders

Shader-backed game-UI studies must reference real `.glsl` files, not pasted pseudo-code. Follow Pencil's supported WebGL/GLSL contract, including `#version 100`, documented uniforms, resolution handling, stable IDs, and an explicit token-to-uniform mapping. Define performance limits and keep comparison captures.

Pencil GLSL is a design/reference implementation. Translate it into the engine-native shader/material form—Unreal HLSL/materials, Unity ShaderLab/HLSL or Shader Graph, Godot shader language—and validate visual parity automatically or with controlled captures. Reuse source directly only when compatibility is verified.

Official references: [AI integration](https://docs.pencil.dev/getting-started/ai-integration), [code on canvas](https://docs.pencil.dev/core-concepts/code-on-canvas), [variables](https://docs.pencil.dev/core-concepts/variables), [components](https://docs.pencil.dev/core-concepts/components), [design libraries](https://docs.pencil.dev/core-concepts/design-libraries), and [`.pen` format/shaders](https://docs.pencil.dev/for-developers/the-pen-format).
