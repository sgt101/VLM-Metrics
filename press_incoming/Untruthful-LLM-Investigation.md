# Untruthful LLM Investigation: Economic & Compliance Harm in Regulated Sectors

## Research Objective

Locate and compile reputable sources that document how untruthful output from Large Language Models (LLMs) or Vision-Language Models (VLMs) have caused, or could cause, significant economic or compliance-related harm—especially within finance or life sciences. Emphasize instances where such failures have already produced measurable monetary losses, highlighting the regulated nature of these sectors.

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
