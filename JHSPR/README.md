# JHSPR — Jasper

> JHSPR is the proposed polyglot programming-language layer in the connected Design Orchard LLC architecture. It is intended to bring multiple programming languages into a coherent system while retaining their distinct identities and capabilities.

**Pronunciation:** Jasper  
**Architectural context:** Design Orchard LLC / 🔬 DrMarchand’s Lab⚛︎ratory™  
**Record date:** November 6, 2026  
**Status:** Architecture statement; implementation and conformance not verified  
**Publication scope:** Public, release-safe description for review; not a completed release announcement

## What JHSPR is intended to do

JHSPR is described by its architect as a polyglot programming-language system that loads participating language(s). A language must be identified and exist before its code can be displayed through an interface. The language definition, implementation, data, interface, runtime, and authority to execute are separate responsibilities.

**Intent is not proof:** This directory currently documents the concept. It does not contain a demonstrated JHSPR parser, language loader, interpreter, compiler, runtime, adapter package, or passing conformance suite.

## Component responsibilities

| Layer | Stated role | Boundary |
| --- | --- | --- |
| **JHSPR (Jasper)** | Polyglot language layer and proposed language-loading coordination | Does not itself prove that a language implementation is available |
| **MURI — Marchand Universal Runtime Interface** | Presents code and supports inspection and interaction | Does not create languages or independently authorize execution |
| **DOLSA** | Defines applicable language, package, interface, and governance contracts | Standards do not prove conformance or grant run permission |
| **DrMarchand’s ⚙︎ Nɛuro-Forge Engine** | Orchestrates and validates operations within delegated permission | Does not make itself the language, legal authority, or UI |
| **External Bridges** | Describe bounded source-to-target connections | Do not become internal Engine components or transfer authority |

Examples previously discussed include JavaScript as a code and interaction language; Python, Ruby, and PHP as possible data-processing participants; and SQLite as a data storage/query component. **These examples are not a tested compatibility matrix.**

## Integration principle

1. Identify each real language and implementation, with a source revision and a responsible owner.
2. Establish explicit contracts for loading, input/output, errors, dependencies, and cross-language boundaries.
3. Use DOLSA contracts to define expectations and conformance checks.
4. Let MURI present and inspect the source or results without confusing UI interaction with authorization.
5. Allow DrMarchand’s ⚙︎ Nɛuro-Forge Engine to orchestrate operations only when delegated permission exists.
6. Record failures and positive/negative tests with exact revision and environment evidence, then preserve accepted records in 📚 DrMarchand’s ⚛︎ Library™ with authorized-human validation.

These steps describe a target architecture, **not a verified end-to-end execution sequence**.

## Current repository evidence and gaps

- The public Laboratory repository's main branch had no JHSPR directory before this documentation proposal. This file is a new architecture record, not recovered source code.
- The [Engine repository](https://github.com/DrMarchand/NFE) provides a related execution-oriented codebase, but its presence does not establish JHSPR or DOLSA integration.
- The authoritative implementation source, source revision, actual supported languages, adapter locations, syntax definition, and execution/conformance receipts remain unreconciled.
- No installation, build, or test command is advertised because none has been established as a JHSPR command from source.

## Verification and promotion requirements

A future implementation claim must link the exact source files and commits for language definitions, loaders, adapters, entry points, specifications, dependency manifests, and tests; demonstrate failures as well as successes; establish the authority and permission for runtime actions; and preserve receipts and permanent custody records.

Do not promote a JSON exchange prototype, a directory name, a roadmap, or a successful unrelated Python command as proof that JHSPR parses or executes multiple languages.

**Decision boundary:** Design Orchard LLC supplies organizational authority; an authorized human approves a release. This document grants no execution or publication permission and changes no existing rights or licenses.
