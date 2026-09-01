# ELYSIUM Taxonomy Federation Charter

**Version:** 0.1
**Status:** Active
**Authority:** Yannick

## 1. Founding decision

ELYSIUM preserves two valid taxonomies. Their coexistence is intentional. The Federation records relations between them without selecting a winner, manufacturing equivalence, or erasing the conceptual and historical value of either model.

## 2. Invariants

| Invariant | Operational rule |
|---|---|
| Preservation | No source content is deleted, renamed, overwritten, or replaced by the Federation. |
| Provenance | Every registered source and relation records repository, branch, path, content hash, and observation date. |
| Non-equivalence | A correspondence is a typed relation, not identity or succession, unless a human decision explicitly states otherwise. |
| Local authority | Each source retains authority over its own semantics and lifecycle. Source-of-truth claims do not automatically extend across repositories. |
| Human arbitration | Yannick is the final strategic authority for a new relation, a changed status, or any mutation. |
| Reversibility | Derived views are regenerable. Any future write must be isolated in an atomic pull request with an explicit rollback path. |

## 3. Authority domains

| Domain | Source of authority | Federation role |
|---|---|---|
| Metabolic model | `elysium-book@master:00-meta/ontology-map.md` | Reference and relate, never overwrite. |
| Open-infrastructure model | `elysium-civilizational-ontology@main:03_BOOK_AND_PUBLICATION/06_ONTOLOGY_SPECIFICATION.md` | Reference and relate, never overwrite. |
| Ontology program state | `00_PROGRAM_OFFICE/ELYSIUM_PROGRAM_STATE.*` | Reference only. |
| Book manuscript state | `elysium-book@master:00-meta/manuscript-status.md` | Reference only. |
| Cross-model relationship | This Federation, after human validation. | Record explicit, scoped, versioned relations. |

## 4. Relation taxonomy

| Type | Meaning | Does not mean |
|---|---|---|
| `PRIMARY_CORRESPONDENCE` | Strong functional correspondence with preserved differences. | Equivalent definition or merged node. |
| `PRIMARY_CORRESPONDENCE_WITH_SCOPE_DELTA` | Strong correspondence with a documented difference of scale or scope. | Permission to reduce the wider scope. |
| `SECONDARY_CORRESPONDENCE` | Supporting, partial or contextual connection. | Primary ownership or direct substitution. |
| `TRANSVERSAL_UNREPRESENTED` | A meaningful dimension in one model has no strict peer in the other. | A defect requiring forced absorption. |
| `REVIEW_REQUIRED` | A relationship needs additional source evidence or human arbitration. | A negative judgement about either source. |

## 5. Change protocol

1. Record a fresh source observation with its content hash.
2. Add or revise one relation at a time, including its evidence and non-equivalence note.
3. Obtain an explicit human decision for a relation or status change.
4. Generate derived views only from approved relations.
5. Use a separate pull request for any source change; never combine a source mutation with a Federation registry update.

## 6. Explicit exclusions

This charter does not create a third source ontology, determine a final vocabulary, migrate ELYSIUM into Y-OS Core, decide the final list of facets, or authorize changes to source taxonomies.
