# FiF transformation domains

Source material extracted from Yannick's FiF (Futures in Focus) Replit app. Acceptance status: source material. English names follow `shared/schema.ts`. UI labels that differ are shown beside them.

Thesis, from `FUTURES_SPEC.md`: Humanity is moving from a scarcity-driven, labor-based civilization to an intelligence-abundant, meaning-driven one.

## Categories

| Slug | Name | Spec color | Archive UI color | EN | FR | IT |
|---|---|---|---|---|---|---|
| `cognitive` | Cognitive Revolution | #3B82F6 | #3B82F6 | Cognitive Revolution | Révolution Cognitive | Rivoluzione Cognitiva |
| `physical` | Physical Revolution | #10B981 | #10B981 | Physical Revolution | Révolution Physique | Rivoluzione Fisica |
| `life` | Life Revolution | #8B5CF6 | #8B5CF6 | Life Revolution | Révolution de la Vie | Rivoluzione della Vita |
| `systems` | Systems Revolution | #F59E0B | #F59E0B | Systems Revolution | Révolution des Systèmes | Rivoluzione dei Sistemi |
| `perception` | Perception Revolution | #06B6D4 | #EC4899 | Perception Revolution | Révolution Perceptive | Rivoluzione Percettiva |
| `meaning` | Meaning Revolution | #EC4899 | #06B6D4 | Meaning Revolution | Révolution du Sens | Rivoluzione del Significato |

Perception and Meaning colors differ between the specification and `Archive.tsx`. Domain accent colors follow the specification.

## Domains

### 1. Artificial General Intelligence

- Slug: `agi`
- Category: `cognitive`
- Subtitle: Cognitive Automation - When Machines Think
- Why it matters: It changes WHO thinks
- Icon: `Brain`
- Accent: `#3B82F6`
- Labels: EN Artificial General Intelligence · FR Intelligence Artificielle Générale · IT Intelligenza Artificiale Generale
- Economy: Knowledge work automation, new value creation paradigms
- Society: Education reimagined, power concentration risks, governance challenges
- Individual: Cognitive augmentation, skill adaptation, human-AI collaboration

### 2. Energy Revolution

- Slug: `energy`
- Category: `physical`
- Subtitle: Abundance Systems - Unlimited Clean Power
- Why it matters: It changes WHAT limits us
- Icon: `Zap`
- Accent: `#10B981`
- Labels: EN Energy Revolution · FR Révolution Énergétique · IT Rivoluzione Energetica
- Economy: Energy cost approaches zero, new industrial possibilities
- Society: Decentralized power, climate solutions, geopolitical shifts
- Individual: Energy independence, new lifestyles, location freedom

### 3. Biotechnology & Synthetic Life

- Slug: `biotech`
- Category: `life`
- Subtitle: Life Engineering - Rewriting the Code of Life
- Why it matters: It changes WHAT we are
- Icon: `Dna`
- Accent: `#8B5CF6`
- Labels: EN Biotechnology & Synthetic Life · FR Biotechnologie · IT Biotecnologia
- Economy: Programmable biology, bio-manufacturing, food revolution
- Society: Healthspan extension, population dynamics, ethical frontiers
- Individual: Genetic optimization, disease elimination, longevity

### 4. Robotics & Automation

- Slug: `robotics`
- Category: `physical`
- Subtitle: Physical World Transformation - When Machines Act
- Why it matters: It changes WHO acts
- Icon: `Bot`
- Accent: `#10B981`
- Labels: EN Robotics & Automation · FR Robotique et Automatisation · IT Robotica e Automazione
- Economy: Labor market transformation, new manufacturing paradigms
- Society: Care robots, autonomous logistics, urban redesign
- Individual: Personal robots, new human roles, physical augmentation

### 5. Collective Intelligence

- Slug: `collective_intelligence`
- Category: `cognitive`
- Subtitle: Networked Consciousness - Humanity's Hive Mind
- Why it matters: It changes HOW humanity coordinates
- Icon: `Network`
- Accent: `#3B82F6`
- Labels: EN Collective Intelligence · FR Intelligence Collective · IT Intelligenza Collettiva
- Economy: Swarm decision-making, prediction markets, distributed organizations
- Society: Informal networks outpace institutions, new governance forms
- Individual: New participation modes, amplified influence, collective sense-making

### 6. Digital Money & Programmable Finance

- Slug: `digital_finance`
- Category: `systems`
- Subtitle: Economic Infrastructure - Money Becomes Code
- Why it matters: It changes HOW value flows
- Icon: `Coins`
- Accent: `#F59E0B`
- Labels: EN Digital Money & Finance · FR Finance Numérique · IT Finanza Digitale
- Economy: Instant settlement, tokenized assets, algorithmic markets
- Society: State monetary monopoly challenged, new economic models
- Individual: Financial sovereignty, new investment paradigms, risks

### 7. Institutional Collapse & Rebuild

- Slug: `institutions`
- Category: `systems`
- Subtitle: Governance Evolution - Trust Shifts
- Why it matters: It changes WHO we trust
- Icon: `Building2`
- Accent: `#F59E0B`
- Labels: EN Institutional Evolution · FR Évolution Institutionnelle · IT Evoluzione Istituzionale
- Economy: Individuals + AI outperform organizations, new business forms
- Society: New governance models, legitimacy crises, social contracts
- Individual: Self-sovereignty, new responsibilities, community formation

### 8. Spatial Computing

- Slug: `spatial_computing`
- Category: `perception`
- Subtitle: Reality Blending - The World Becomes Interface
- Why it matters: It changes HOW we perceive
- Icon: `Glasses`
- Accent: `#06B6D4`
- Labels: EN Spatial Computing · FR Informatique Spatiale · IT Spatial Computing
- Economy: Digital twins, virtual collaboration, new entertainment
- Society: Blended reality normalization, presence transformation
- Individual: Enhanced perception, new skills, reality customization

### 9. Materials Science

- Slug: `materials`
- Category: `physical`
- Subtitle: Atomic-Level Manufacturing - Programmable Matter
- Why it matters: It changes WHAT we build with
- Icon: `Atom`
- Accent: `#10B981`
- Labels: EN Materials Science · FR Science des Matériaux · IT Scienza dei Materiali
- Economy: AI-designed materials, new industries, sustainable production
- Society: Self-healing infrastructure, bio-integrated systems
- Individual: Personalized materials, health applications, enhanced products

### 10. Human Identity & Meaning

- Slug: `meaning`
- Category: `meaning`
- Subtitle: The Purpose Revolution - Who Are We Now?
- Why it matters: It changes WHY we exist
- Icon: `Compass`
- Accent: `#EC4899`
- Labels: EN Human Identity & Meaning · FR Identité et Sens · IT Identità e Significato
- Economy: Meaning economy, purpose-driven work, post-labor society
- Society: Spiritual/philosophical renaissance, new cultural forms
- Individual: Identity reformation, existential exploration, new life scripts

## Exploration modes

Designed in `FUTURES_SPEC.md`. The Archive shows the UI label and description. The server does not inject these mode texts. See [PROMPTS.md](PROMPTS.md).

| Id | Spec description | AI approach | Output | EN label | FR label |
|---|---|---|---|---|---|
| `deep_dive` | Technical depth within one domain | Detailed, technical, comprehensive | Long-form explanation with examples | Deep Dive | Plongée Profonde |
| `systems_weave` | Cross-domain connections & cascading effects | Relational, connecting dots between domains | How this domain affects/is affected by others | Systems Weave | Tissage Systémique |
| `essential_insight` | Distilled key takeaways (5-minute read) | Concise, punchy, memorable | Core concepts in bullet points with one-liners | Essential Insight | Insight Essentiel |
| `strategic_questions` | Personal and societal implications to consider | Socratic, provocative, actionable | Questions to reflect on, scenarios to consider | Strategic Questions | Questions Stratégiques |
| `action_gateway` | How to position yourself, skills to build | Practical, career-focused, skill-oriented | Concrete actions, resources, learning paths | Action Gateway | Porte d'Action |

Italian mode labels are absent from `translations.ts` and fall back to English.

