# Untruthful LLM Investigation: Economic & Compliance Harm in Regulated Sectors

## Research Objective

Locate and compile reputable sources that document how untruthful output from Large Language Models (LLMs) or Vision-Language Models (VLMs) have caused, or could cause, significant economic or compliance-related harm—especially within finance or life sciences. Emphasize instances where such failures have already produced measurable monetary losses, highlighting the regulated nature of these sectors.

**Scope Definition:**

**IN SCOPE** — Untruthful LLM/VLM output including:
- **Hallucinations**: Fabricated facts, fake citations, non-existent data, or invented references
- **Bias**: Systematically skewed recommendations, analysis, or decision-making
- **Indeterminism**: Inconsistent or variable responses to identical queries that cause harm
- **Unfaithful retrieval**: Incorrect recall or misrepresentation of factual knowledge, including failures in Retrieval-Augmented Generation (RAG) systems and agent-based architectures
- **Miscalibrated confidence**: Failure to recognize or communicate uncertainty; asserting false information with high confidence; inability to acknowledge knowledge boundaries
- **Multimodal systems**: Vision-Language Models (VLMs) and multimodal LLMs that process and analyze text, images, medical scans, financial charts, or other visual data
- **Application domains**: Text generation, advice, analysis, diagnosis, decision-support, report generation, and question-answering

**OUT OF SCOPE** — Issues not related to untruthful textual/analytical output:
- Image generation models (DALL-E, Midjourney, Stable Diffusion, etc.) and purely generative visual content
- Copyright infringement and intellectual property disputes
- Autonomous vehicles and driverless car incidents
- Pure robotics or physical automation failures
- Cybersecurity attacks or adversarial exploits unrelated to truthfulness

### Entry Schema for New Cases

When adding new cases to the casebooks, follow this standardized format:

**Table Columns (in order):**

1. **# (Case ID)**
   - Format: Three-letter prefix + sequential number
   - Prefixes: `Med` (Medical casebook), `Fin` (Finance casebook), `Int` (Interdomain casebook)
   - **IMPORTANT**: New entries awaiting review must use prefix WITHOUT number (e.g., `Med`, `Fin`, `Int`)
   - Only after review and approval should entries be assigned sequential numbers (Med9, Fin9, Int5, etc.)
   - Example workflow: Draft entry as `Med` → Review → Approve → Renumber to `Med9`

2. **URL(s)**
   - Primary source URL(s) as bare links (no markdown formatting in this column)
   - Multiple URLs separated by `<br>` tags
   - Include DOIs, court dockets, official reports where available
   - Verify URLs are accessible; note if paywalled or access-restricted

3. **YYYY-MM**
   - Publication, filing, or incident date in YYYY-MM format
   - Extract from URL path when possible (e.g., `/2024/02/` → `2024-02`)
   - Mark uncertain dates with `(estimate)` suffix
   - For ongoing cases, use earliest significant date (filing, report, ruling)
   - Leave blank if date cannot be reasonably determined

4. **Entities involved**
   - List format (comma-separated)
   - Include: companies, government agencies, models (e.g., GPT-4, ChatGPT), individuals/plaintiffs (anonymized if appropriate), courts/tribunals, researchers/institutions
   - Order by relevance: primary actors first

5. **Concise Case synopsis**
   - 2-4 sentence summary of the incident
   - Structure: What happened → What LLM/VLM did → What the consequence was
   - Include case names, jurisdictions, or study titles where applicable
   - Focus on factual description; save analysis for next column

6. **Additional commentary**
   - Contextual analysis: regulatory implications, sector significance, precedent value
   - Why this matters for compliance/risk management
   - Links to broader patterns or related cases
   - Technical details (model type, failure mode) if relevant

7. **Damage/Risk Estimate (USD)**
   - Monetary values in USD
   - Format examples:
     - Exact: `5,000` or `721`
     - Range: `10,000–50,000 per incident`
     - Aggregate: `Tens of millions aggregate (estimate)`
     - Qualitative: `Not quantified; risk per wrong decision variable`
   - Include basis for estimate in parentheses when helpful
   - For non-USD currencies, convert and note original (e.g., `721 (C$812 total)`)
   - Mark estimates clearly; prefer ranges over false precision

**Quality Standards:**

- **Verifiability**: Prefer primary sources (court documents, regulatory filings, peer-reviewed papers) over news coverage
- **Relevance**: Must demonstrate actual or credible potential economic/compliance harm from LLM/VLM untruthfulness
- **Recency**: Prioritize 2023-present; older cases acceptable if high precedent value
- **Sector fit**: Medical/pharma/healthcare → Med; Banking/finance/investment/accounting → Fin; All others → Int

---

## Comprehensive Top-20 Cases

The following 20 cases have been categorized into three domain-specific casebooks:

### Medical, Pharma & Healthcare (8 cases)
See: [Untruthful-LLM-casebook_medical.md](./Untruthful-LLM-casebook_medical.md)
- Med1–Med8: Cases involving clinical LLMs, diagnostic errors, patient harm, and medical VLM hallucinations

### Banking, Investment, Trading, Accounting & Corporate Finance (8 cases)
See: [Untruthful-LLM-casebook_finance.md](./Untruthful-LLM-casebook_finance.md)
- Fin1–Fin8: Cases involving investment losses, regulatory warnings, consumer finance violations, and banking sector risks

### Interdomain & Cross-Sector Incidents (4 cases)
See: [Untruthful-LLM-casebook_interdomain.md](./Untruthful-LLM-casebook_interdomain.md)
- Int1–Int4: Cases involving air transport, consulting, legal filings, and cross-sectoral litigation

---

## How this ties back to regulated finance and life sciences

A few synthesized points, tuned to your context:

### Fundamental insights

- **In finance**, we already see a continuum from small but real consumer losses (Pearl.com / Investopedia survey) to clear regulatory concern (CFPB, SEC, SwissBanking, BizTech). The pattern is:
  - ➳ retail users act on unverified LLM advice →
  - ➳ regulated firms consider embedding LLMs in advisory, customer service, and reporting →
  - ➳ supervisors issue guidance and begin enforcement where outputs or disclosures are misleading.

- **In life sciences and healthcare**, the evidence is shifting from "toy errors" to documented clinical incidents and strong mechanistic studies:
  - ➳ a concrete toxicology case (bromism) where ChatGPT-style advice fed into patient behavior
  - ➳ population-level signals (poison-control trends, surveys of Americans following wrong AI medical advice)
  - ➳ technical papers showing both LLMs and VLMs hallucinate in precisely the domains that drive diagnostic and treatment decisions.

### Pro-tips (how to weaponize this for your narrative)

#### For boards / regulators:
- ➳ Start with Int1 and Int2 as "clean" case studies: small claim (Air Canada) and big-ticket consulting refund (Deloitte) – both show that hallucinations invalidate contracts and shift liability onto the deploying organization, not the model vendor.
- ➳ Then link to FCA/SEC/CFPB and SwissBanking material to show that supervisors already see hallucinations as a compliance problem, not just a UX bug.

#### For healthcare / pharma QA & regulatory:
- ➳ Use Med1–Med8 to show that the scientific community has converged on "medical hallucination" as a recognized safety category, specifically for LLMs and medical VLMs.
- ➳ Combine the bromism case and poison-center signal with Nature / medRxiv work to argue that ignoring hallucinations is incompatible with current expectations for clinical risk management and post-market surveillance.

---

## Necessary next steps if you want to build on this

- **Build your own short "casebook"** distilled from the URLs above with: incident description, model type, control failures, economic/compliance consequence, and mitigations.
- **Map each failure mode** to your own AI-governance controls (RAG vs base-LLM, human-in-the-loop, provenance, evaluation of hallucination rate, etc.) and to specific regulatory articles (FINMA/FINSA, GDPR/FADP, MDR/IVDR, FDA, FCA/SEC).
- **For finance and life sciences clients**, you can now credibly argue: "There is already case law and supervisory scrutiny linking hallucinations to monetary loss and liability. The question is not whether this happens, but how you limit it and document that limitation."
