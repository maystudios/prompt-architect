# Planning and Visual Control Plane

## Canonical truth

Keep machine-readable, versioned truth in the project repository and project brain:

- `GAME_PLAN.md` for current Goal, milestones, workstreams, risks, and evidence;
- Mermaid or D2 source for dependency/system graphs;
- Decision Ledger and interface contracts;
- committed Goal Packets and handoff manifests when sessions cannot message directly.

External boards are synchronized views and collaboration surfaces, never the only copy of critical state.

## Free-first routing

**draw.io:** Primary free agentic canvas for system maps, dependencies, level/gameplay flows, roadmaps, and architecture. Prefer the official draw.io MCP and native editable diagram data. Validate generated XML before import and keep a repo-side source/export. A local launch path can use `npx @drawio/mcp` when the host and policy permit.

Official references: [draw.io MCP server](https://www.drawio.com/docs/manual/generate/drawio-mcp-server/) and [diagram generation/validation](https://www.drawio.com/docs/reference/diagram-generation/).

**HacknPlan Personal:** Optional game-production cockpit when credentials and API access already exist. At planning time its Personal offering was described as free with unlimited projects and users while omitting Studio features; verify the current terms before the Goal relies on that boundary. Use one game as one project and sessions as tasks/work items, not projects. Choose the project preset by work shape:

- Full Suite — full game production;
- Agile — vertical slice, backlog, or sprint-oriented development;
- Documentation — knowledge/design-only effort;
- Lite — small standalone feature;
- Custom — unusual plugin/tool/content pipeline.

Treat its beta API as a synchronized surface: queue writes, respect current rate limits, use scoped credentials, retry safely, and make updates idempotent. Keep dependencies and durable plans in repo artifacts when the selected free plan lacks a needed view.

Official references: [Personal terms](https://hacknplan.com/legal/terms-of-service-v4), [project setup](https://hacknplan.com/docs/projects/setting-up-a-project), and [API introduction](https://hacknplan.com/docs/api-introduction).

**Pencil:** UI/UX, HUD, menus, interaction states, visual concepts, token systems, and shader/script-backed game-UI studies. Apply `pencil-game-ui.md` in full.

## Optional tools

Use another installed planning system only when it has a concrete advantage and an export/sync path. Do not require a paid dependency. Existing paid services may be used when detected and beneficial; creating a new cost or subscription is a human gate.

## Synchronization

Assign one authority per field. The repository owns technical dependencies, commits, tests, and Goal Packets. The project brain owns durable decisions and learned knowledge. A production board may own scheduling and human work status. Pencil owns editable UI design artifacts. Reconcile status at each integration milestone and record sync failures rather than silently diverging.
