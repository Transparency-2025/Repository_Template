Choosing the right license is critical, as it defines the rules for how others can use your code. Open-source licenses generally fall into two categories: **Permissive** (minimal restrictions) and **Copyleft** (requires sharing derivative source code).

Here are summaries of the license types available directly in the GitHub template, and a separate table for other popular licenses.

## 📝 GitHub Template License Differences

The following table summarizes the key features and obligations of the licenses listed in GitHub's standard "Add a license" template.

| License Type | Category | Core Philosophy | Commercial Use | Share/Source Requirements (Copyleft) | Patent Grant |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **MIT** | Permissive | Simplest, minimal restrictions. "Do what you want, just keep the license." | ✅ Allowed | **None.** Derivative works can be closed-source. | ❌ None explicit |
| **Apache 2.0** | Permissive | Freedom, but with legal clarity. Highly corporate-friendly. | ✅ Allowed | **None.** Requires notice and attribution. | ✅ **Explicit** (Protects contributors from patent lawsuits). |
| **GPL v3.0** | Strong Copyleft | Freedom-guaranteeing. Ensures all derivative works remain open source. | ✅ Allowed | **Strong.** Must release the complete source code under GPL v3.0 upon distribution. | ✅ Explicit |
| **AGPL v3.0** | Strongest Copyleft | **GPL for network services.** Closes the "SaaS loophole." | ✅ Allowed | **Strongest.** Source must be made available even if software is only used over a network (SaaS). | ✅ Explicit |
| **LGPL v2.1** | Weak Copyleft | Designed for libraries. Allows proprietary programs to *link* to the code. | ✅ Allowed | **Weak.** Only modifications to the LGPL-licensed file/library itself must be shared. | ❌ None explicit |
| **MPL 2.0** | Weak Copyleft | Designed for clarity and mixing. | ✅ Allowed | **File-Level.** Modifications to MPL-licensed source files must be shared under MPL, but proprietary files can remain closed. | ✅ Explicit |
| **BSD 2-Clause** | Permissive | Very simple, highly similar to MIT. | ✅ Allowed | **None.** Requires copyright notice and license text retention. | ❌ None explicit |
| **Creative Commons Zero (CC0)** | Public Domain | Waives all copyright interest and dedicates the work to the Public Domain. | ✅ Allowed | **None.** Equivalent to no legal restriction whatsoever. | N/A |
| **The Unlicense** | Public Domain | Informal and shorter attempt to dedicate work to the Public Domain. | ✅ Allowed | **None.** | N/A |
| **EPL 2.0** | Weak Copyleft | Designed for business/enterprise. Similar to MPL but applies per file. | ✅ Allowed | **Weak/File-Level.** Modifications must be released under EPL. | ✅ Explicit |

---

## 🌎 Popular Licenses Not in GitHub's Template

While GitHub's template covers the vast majority of needs, other specialized or popular licenses exist that are often used in specific communities but are not included in the default list.

| License Name | Category | Core Purpose / Key Difference | Example Use Case |
| :--- | :--- | :--- | :--- |
| **ISC License** | Permissive | Functionally identical to the MIT and 2-Clause BSD licenses, but written to be even shorter and cleaner. | Used widely by the **OpenBSD** project and in Node.js packages. |
| **PostgreSQL License** | Permissive | A permissive license similar to BSD/MIT, specifically used for the PostgreSQL database system. | Database software projects. |
| **Artistic License 2.0** | Permissive/Hybrid | Used primarily by the **Perl** community. It is designed to encourage modifications while maintaining the integrity of the original package. | Perl modules and projects. |
| **EU Public License (EUPL)** | Copyleft | Designed to be fully compliant with **European Union** law and is available in all official EU languages. | Software developed for European public administration or institutions. |
