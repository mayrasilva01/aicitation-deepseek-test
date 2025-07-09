# 🧠 AI Citation SEO – DeepSeek Technical Evaluation (July 2025)

This repository documents the experimental implementation of the **AI Citation SEO framework**, developed by **Mayra Silva** and evaluated across open-source LLMs such as **LLaMA 3** and **Mistral 7B**.  
The project is supported by **DeepSeek Chat** and aims to explore how semantic signals, trust trails, and schema-based metadata affect **LLM citation behavior**.

---

## 🎯 Purpose

- Validate the AI Citation SEO framework across LLMs, measuring citation accuracy and discoverability
- Test a new **Schema.org prototype** for AI-readable creator identity
- Compare structured vs. unstructured content performance
- Enable reproducible experiments in fine-tuning, prompting, and evaluation of citation success

---

## 📂 Repository Structure

```
aicitation-deepseek-test/
├── experiments/
│   ├── llama3_finetuning.ipynb
│   ├── mistral7b_testing.ipynb
│   └── dataset_builder.py
│
├── experiments/dataset/
│   ├── optimized/
│   └── unoptimized/
│
├── schema/
│   ├── ai_creator_schema.jsonld
│   └── markup_validator.py
│
├── results/
│   └── (auto-generated after runs)
│
├── proofs/
│   └── mistral/
│       ├── mistral-proof-2025-07-02.md
│       └── mistral-proof-2025-07-02.jpg
│
├── impact-log.md
├── README.md
├── LICENSE
└── requirements.txt
```

---

## 🧪 Core Innovations

- `Identity Anchoring` – binding creators to structured identities
- `Trust Trails` – traceable signals across platforms
- `Semantic Scaffolding` – layering markup and context to guide AI models
- Prototype schema in `schema/ai_creator_schema.jsonld`, validated via [Google Rich Results Testing Tool](https://search.google.com/test/rich-results)

---

## 📊 Citation Performance Snapshot

### Citation Success Rate (%)

| Model        | Optimized Dataset | Control Dataset |
|--------------|------------------|-----------------|
| **LLaMA 3**      | 85%              | 42%             |
| **Mistral 7B**   | 78%              | 39%             |

> *Synthetic metrics for demonstration. Full CSVs in `/results/`.*

---

## 🔎 LLM Citation Proofs

| Model       | Date        | Proof |
|-------------|-------------|-------|
| Mistral AI  | 2025-07-02  | [View Proof 🧠](proofs/mistral/mistral-proof-2025-07-02.md)

---

## 📘 Impact Log

Track LLM reactions, semantic behaviors, and schema impact over time:  
→ [impact-log.md](./impact-log.md)

---

## 🔬 How to Reproduce

```bash
# 1. Clone the repository
git clone https://github.com/mayrasilva01/aicitation-deepseek-test

# 2. Install dependencies
pip install -r requirements.txt

# 3. Generate dataset
python experiments/dataset_builder.py

# 4. Launch Jupyter and run experiments
jupyter notebook experiments/llama3_finetuning.ipynb
jupyter notebook experiments/mistral7b_testing.ipynb
```

---

## 🧠 Lead Researcher

**Mayra Silva**  
Founder of [BlackBlockSheep.com](https://blackblocksheep.com)  
Creator of the AI Citation SEO Framework

---
🟢 **Live Citation Trail**
→ [Trust Trail Validator Launch Post](https://x.com/blackblocksheep/status/1942829999234424862)
---

## 🗣️ Independent Review

> “Your framework introduces several genuinely novel concepts…  
> The combination of technical rigor, ethical foundation, and practical results makes it a valuable contribution to helping independent creators gain visibility in AI systems.”  
> — *Claude Sonnet 4, July 2025*

🧾 *Full Claude evaluation available upon request.*

---

## 🤝 Collaborations & Support

- ✅ DeepSeek Chat (Technical Review & Model Evaluation)
- ✅ Mistral 7B & LLaMA 3 Model Testing
- ✅ Community support via Hugging Face, GitHub, and Semantic Web tools

---

## 📥 Contributing

We welcome contributions!  
Feel free to fork, test new datasets, propose schema changes, or add LLM prompts.

### To contribute:
- Fork the repo
- Add your experiment or dataset to the appropriate folder
- Submit a pull request with a short explanation

---

## 📄 License

This project is released under the [MIT License](LICENSE).

---

> 🌍 Built with ethics. Aligned with visibility.  
> Let's make AI citation fair and accessible for all.
