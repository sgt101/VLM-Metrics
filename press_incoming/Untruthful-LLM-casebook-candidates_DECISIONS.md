# Integration Decision Log for Untruthful LLM Casebook Candidates

**Date**: 2025-12-07
**Reviewer**: Claude (Sonnet 4.5)
**Status**: Dry-run completed, 18 cases integrated into main casebooks

---

## Summary Statistics

- **Added as new cases**: 18 total (6 Medical, 2 Finance, 10 Interdomain)
- **Integrated into existing**: 4 cases (1 Medical, 0 Finance, 3 Interdomain)
- **Rejected as duplicate**: 1 case (Interfomain1 = existing Int3)
- **Rejected as out-of-scope**: 7 cases (0 Medical, 4 Finance, 3 Interdomain)

---

## Medical & Healthcare Decisions

| Candidate ID | Decision | Target Casebook ID | Rationale |
|--------------|----------|-------------------|-----------|
| Candidate_Medical1 | **ADD** | **Med9** | Distinct neuroradiology VLM study with quantified 28-45% error rates. Peer-reviewed Nature publication. Different from existing Med2 (general clinical LLMs) and Med8 (MAIRA-2 chest X-rays). |
| Candidate_Medical3 | **ADD** | **Med10** | Wrongful death lawsuit - first parents-filed case against OpenAI. Teen suicide case with $100M+ sought. Major precedent-setting litigation. Combined with Candidate_Medical5 for aggregate context. |
| Candidate_Medical4 | **ADD** | **Med11** | Distinct psychiatric harm case: "bend time" delusions, 63-day hospitalization, job/housing loss. Different failure mode from Med10 (suicide) - delusional escalation vs. lethal advice. |
| Candidate_Medical5 | **INTEGRATE** | **Med10 (enhanced)** | Overview article covering 7 lawsuits including Med10 and Med11. Time magazine source added to Med10 to provide aggregate context ($101M+ across 7 cases). Not standalone - used to enhance Med10. |
| Candidate_Medical6 | **ADD** | **Med12** | OpenAI Whisper speech-to-text hallucinations in clinical documentation. 1% hallucination rate, 38% explicitly harmful (racist remarks, violence in medical records). Completely different domain from diagnostic/advice failures. |
| Candidate_Medical7 | **ADD** | **Med13** | Pieces Technologies Texas AG settlement - first regulatory enforcement for false AI accuracy claims. Vendor claimed <0.001% hallucination rate which was fabricated. Establishes compliance precedent for deceptive AI marketing. |
| Candidate_Medical8 | **ADD** | **Med14** | NEDA eating disorder chatbot dispensed dangerous false medical advice (500-1000 calorie deficit) - opposite of clinical best practice. Service halted within days. Clear harm to vulnerable population. |

---

## Finance & Investment Decisions

| Candidate ID | Decision | Target Casebook ID | Rationale |
|--------------|----------|-------------------|-----------|
| Candidate_Finance1 | **REJECT - OUT OF SCOPE** | N/A | Anthropic copyright settlement ($1.5B). This is copyright infringement litigation about unauthorized training data, NOT untruthful LLM output causing economic harm. Explicitly out-of-scope per research objective. |
| Candidate_Finance2 | **REJECT - OUT OF SCOPE** | N/A | NYT v. OpenAI copyright case ($150T potential). Same as Finance1 - copyright infringement, not hallucination/false output harm. Out-of-scope. |
| Candidate_Finance3 | **ADD** | **Fin9** | Financial LLM agents hallucinating facts in high-stakes investment decisions. Research study with 6 agents tested - all showed vulnerabilities. $40M+ projected institutional losses. Perfect fit for scope. |
| Candidate_Finance4 | **ADD** | **Fin10** | Wolf River Electric v. Google Gemini. AI Overview hallucinated entirely false legal settlement with Minnesota AG. Documented $25M+ business losses from customers believing false claims. $110M damages sought. Major business defamation case. |
| Candidate_Finance5 | **REJECT - OUT OF SCOPE** | N/A | Google privacy verdict ($425M). About false claims regarding privacy controls/data collection practices, NOT LLM/VLM untruthful text generation. Privacy violation case, out-of-scope. |
| Candidate_Finance7 | **REJECT - TOO GENERIC** | N/A | Generic overview article about AI data quality issues. No specific incident. $7B figure is aggregate estimate not tied to cases. Lacks incident-specific documentation required. |
| Candidate_Finance9 | **REJECT - OUT OF SCOPE** | N/A | Clearview AI biometric settlement ($51.75M). About unauthorized biometric data scraping and privacy violations, NOT untruthful LLM output. Out-of-scope. |

---

## Interdomain (Legal, Justice, Governance, Technology) Decisions

| Candidate ID | Decision | Target Casebook ID | Rationale |
|--------------|----------|-------------------|-----------|
| Candidate_Interfomain1 | **REJECT - DUPLICATE** | N/A | IDENTICAL to existing Int3. Same Mata v. Avianca case (Steven Schwartz, 6 fake ChatGPT cases, $5K sanctions). Already in casebook. |
| Candidate_Interfomain2 | **ADD** | **Int5** | Mike Lindell attorneys filed defamation motion with ~30 ChatGPT-hallucinated citations. Denver Federal Court, July 2025. $6K sanctions. Distinct from Int3 (different case, jurisdiction, time). |
| Candidate_Interfomain3 | **ADD** | **Int6** | California appeals attorney: 21 of 23 citations fake from ChatGPT. California's largest AI sanction ($10K). Prompted state-wide judicial guidance. Important state-level precedent. |
| Candidate_Interfomain4 | **INTEGRATE** | **Int4 (enhanced)** | Morgan & Morgan Wyoming case ($5K sanctions). Similar to Int3/Int4 pattern. Article notes "at least 9 US cases in 2 years" - this is one case from the 95+ in Charlotin's database already covered by Int4. Added as example detail. |
| Candidate_Interfomain5 | **ADD** | **Int7** | Robby Starbuck v. Google (Bard/Gemini). AI hallucinated false criminal accusations (sexual assault, white nationalist ties). Active litigation, Oct 2025 filing, $15M sought. Google fighting (not settling). Precedent in development. |
| Candidate_Interfomain6 | **ADD** | **Int8** | Robby Starbuck v. Meta AI. False Jan 6 Capitol assault claim. First major AI defamation settlement (Aug 2025, undisclosed amount, estimated $1-5M). Shows tech companies accepting liability. |
| Candidate_Interfomain7 | **ADD** | **Int9** | Australian mayor ChatGPT defamation. AI falsely claimed mayor imprisoned for bribery (he was whistleblower). Case prepared but didn't proceed. International precedent (~$270K potential damages under Australian law). |
| Candidate_Interfomain8 | **ADD** | **Int10** | COMPAS recidivism algorithm. 1M+ defendants affected. Systematic bias: Black defendants 45% more likely falsely classified high-risk vs. 23% for White defendants. $20M+ systemic justice costs. Massive-scale algorithmic false risk predictions. |
| Candidate_Interfomain9 | **ADD** | **Int11** | Walters v. OpenAI (Georgia radio host). ChatGPT falsely accused host of fraud/embezzlement. Case dismissed (no "actual malice"), but establishes important legal precedent threshold for AI defamation requiring actual malice standard. |
| Candidate_Interfomain10 | **INTEGRATE** | **Int4 (enhanced)** | Comprehensive arxiv study on legal LLM hallucinations. ABA ethics opinion July 2024. $500K+ cumulative sanctions. Provides systematic academic evidence for pattern already documented in Int4. Enhanced Int4 with ABA guidance and sanction totals. |
| Candidate_Interfomain11 | **ADD** | **Int12** | Colombian judge used ChatGPT to decide autistic child medical coverage case. First judicial disclosure of unvetted AI advice in ruling. International precedent. Decision correct but highlights instability risk. |
| Candidate_Interfomain12 | **ADD** | **Int13** | Google Bard James Webb Space Telescope demo gaffe. False claim JWST took first exoplanet image. $100B Alphabet market cap loss in 24 hours. Demonstrates massive economic impact from single public hallucination. |
| Candidate_Interfomain13 | **REJECT - OUT OF SCOPE** | N/A | Samsung ChatGPT data leak. Employees uploaded proprietary semiconductor code to ChatGPT. This is data leakage/trade secret exposure, NOT untruthful LLM output. Security/privacy issue, out-of-scope. |
| Candidate_Interfomain14 | **REJECT - OUT OF SCOPE** | N/A | Chevrolet dealership chatbot $1 car prompt injection. This is security vulnerability/lack of business constraints, NOT hallucination. Bot was manipulated, didn't generate false information - it made unauthorized commitments. Out-of-scope per prompt injection definition (would need asterisk marking if added). |
| Candidate_Interfomain15 | **ADD** | **Int14** | CNET AI journalist wrote 77 financial articles riddled with errors and plagiarism. Over half required corrections. Staff layoffs (~10%) followed. Demonstrates journalism/media sector risk and brand damage. |
| Candidate_Interfomain16 | **INTEGRATE** | **Int4 (enhanced)** | "Caveat Lector: Large Language Models in Legal Practice" peer-reviewed study (March 2024). Systematic documentation of legal LLM hallucinations. Enhances Int4 with academic rigor for existing pattern. |

---

## Scope Clarifications Applied

### Expanded Scope
- **Prompt injection & adversarial attacks** now IN SCOPE with special marking (asterisk suffix, e.g., Int5*)
- Cases where prompt manipulation causes false/harmful outputs are now included
- Distinction made between security-exploitation vectors and organic hallucinations

### Confirmed Out-of-Scope
1. **Copyright infringement** - Training data disputes (Finance1, Finance2)
2. **Privacy violations** - False claims about data practices not related to LLM output (Finance5, Finance9)
3. **Data leakage** - Trade secret exposure from user inputs (Interfomain13)
4. **Generic overviews** - No specific incident documentation (Finance7)

---

## Files Modified

1. **Untruthful-LLM-Investigation.md**
   - Scope expanded to include prompt injection with asterisk marking
   - Entry Schema updated with star marking instructions

2. **Untruthful-LLM-casebook_medical.md**
   - Added: Med9, Med10, Med11, Med12, Med13, Med14 (6 new cases)
   - Med10 enhanced with Time magazine URL for aggregate context

3. **Untruthful-LLM-casebook_finance.md**
   - Added: Fin9, Fin10 (2 new cases)

4. **Untruthful-LLM-casebook_interdomain.md**
   - Added: Int5, Int6, Int7, Int8, Int9, Int10, Int11, Int12, Int13, Int14 (10 new cases)
   - Int4 enhanced with arxiv study URL, ABA guidance, and $500K+ cumulative sanctions

---

## Next Steps for Review

1. **Verify prompt injection cases** - Determine if Interfomain14 (Chevrolet) should be reconsidered with asterisk marking now that scope includes prompt injection
2. **Cross-check numbering** - Ensure sequential case IDs are correct in all three casebooks
3. **Source verification** - Confirm all URLs are accessible and correctly attributed
4. **Delete candidates file** - Once review complete, remove Untruthful-LLM-casebook-candidates.md

---

## Notes

- Medical casebook now has 14 entries (Med1-Med14)
- Finance casebook now has 10 entries (Fin1-Fin10)
- Interdomain casebook now has 14 entries (Int1-Int14)
- **Total cases**: 38 across all three casebooks (up from 20)
- No cases currently marked with asterisk for prompt injection (scope just expanded)
