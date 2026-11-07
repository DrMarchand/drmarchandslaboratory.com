# Design Orchard Software License Selector — Laboratory Working Prototype

> **File rights:** Copyright holder pending work-specific review. This proposal does not grant the code or documentation an MIT/Apache license.

**Work identity:** Design Orchard LLC software license selector  
**Current working version:** `0.0.1-initializing`  
**Working implementation custody:** 🔬 DrMarchand’s Lab⚛︎ratory™  
**Historical software version custody:** 📚 DrMarchand’s ⚛︎ Library™ (no historical version archived/verified yet)  
**Development status:** Local prototype tests passed; not deployed and not approved for production/relicensing

## Current files

- [Pure recommendation engine](current/v0.0.1-initializing/recommend-license.mjs) — deterministic and read-only: `Apache-2.0` vs `MIT`.
- [Unit tests](current/v0.0.1-initializing/recommend-license.test.mjs) — 19 isolated test scenarios covering flags, blockers and advisory recommendations.
- [Interactive CLI](current/v0.0.1-initializing/review-license-cli.mjs) — prompts for purpose, distribution, contributor/patent risk, rights, dependencies and existing license, then shows a tentative choice. **No file, license, release, or legal state is altered by the CLI.**

To run with Node.js v22 in a local read-only sandbox:

```bash
cd SoftwareLicensing/current/v0.0.1-initializing
node --test recommend-license.test.mjs
node review-license-cli.mjs
```

## Governance and candidates

The proposed Design Orchard [license selection policy](https://github.com/DrMarchand/DesignOrchard.LLC/blob/docs/jhspr-v0.0.1-initializing-20261106/Registry/Licensing/README.md), license catalog, schema and validation receipt live in the company-level **draft policy registry**. That registry describes legal/risk decisions but **must not become the authoritative current working software source**. The current prototype's executable files live in this Laboratory branch.

Apache Software Foundation currently publishes Apache License **2.0**. The second allowed candidate is **MIT**. They are permissive software licenses; neither enforces proprietary-only terms, exclusivity, noncommercial use, or bans on derivatives. A new Apache release must be investigated, rights-checked and human-reviewed before it can be a candidate; never silently change license text in a repository.

An existing license, third-party component, artwork, client agreement, code provenance, and any prior license grant can override the simplicity of a two-choice menu. **Do not treat this as a completed legal audit.**

## Human and technical authority

A recommendation can be output even while work-specific ownership or dependency review is blocked. `applicationAllowed:false` and `releaseAuthorized:false` remain hard-coded in the current engine. The UI/CLI can record a *tentative choice*, but it does not grant permission. Actual application must be a separate authorized-human operation with exact artifact and version, copyright owner, licenses of bundled dependencies, existing grants, third-party notices, target publication scope, test evidence and a protected receipt.

**No ownership verification, production deployment, automated source scanning, Library custody, or release authorization is established by this branch.** If this version becomes superseded, archive the historical source, hashes and decision receipt into 📚 DrMarchand’s ⚛︎ Library™ before declaring that custody complete.
