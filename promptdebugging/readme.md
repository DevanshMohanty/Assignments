Assignment 7: Prompt Debugging – Reducing Hallucinations
Focus

Prompt Engineering + Reliability

This project demonstrates how prompt design impacts hallucinations, verbosity, and reliability in LLM outputs.
Using a weak Groq model, we progressively debug prompts to show that better prompting—not stronger models—reduces errors.

Objective

The goal of this assignment is to:

Identify hallucinations and vague claims caused by poor prompts

Improve prompt clarity step by step

Add constraints and guardrails to reduce risk

Reduce unnecessary verbosity

Demonstrate a prompt debugging mindset

Core Idea

Hallucinations are usually a prompt design failure, not a model failure.

By keeping the model constant and improving only the prompt structure, we show how reliability emerges.

Project Structure
.
├── PromptDebug.ipynb      # Main notebook (step-by-step experiment)
├── README.md              # Project documentation
├── .env                   # GROQ_API_KEY (not committed)
├── .gitignore

Setup Instructions
1. Install dependencies
pip install groq pydantic python-dotenv

2. Set environment variable

Create a .env file:

GROQ_API_KEY=your_api_key_here

Model Configuration

Provider: Groq

Model: openai/gpt-oss-20b (intentionally weak)

Temperature: 0 (deterministic output) to be able to influence the outcome based on each prompt while the randomness is not kept at a minimum.

The same model is used throughout to isolate the impact of prompt changes.

Experiment Design (Prompt Evolution)

The notebook contains five prompts, each demonstrating a different reliability level.

Prompt v1 — Unconstrained (Baseline Failure)

1.Vague task

2.No guardrails

3.Heavy hallucination and verbosity

Prompt v2 — Improved Clarity

1.More explicit rules

2.Still contradictory

3.Reduced but persistent hallucinations

Prompt v3 — Role Prompting (Incorrect → Fixed)

1.Demonstrates role misuse

2.Then corrected to proper System/User roles

3.hows that structure alone is not enough

Prompt v4 — Reliability-First Prompt

1.Strict constraints

2.Refusal logic

3.No hallucinations

4.Task completeness intentionally sacrificed

Prompt v5 — Production-Grade Sequential Prompt

1.Persistent system prompt

2.User prompts vary per task

3.Controlled inference allowed

4.Best balance of usefulness and safety

Guardrails Used

Explicit “DO NOT” rules

Refusal conditions when information is missing

Separation of behavior (system) and intent (user)

Low temperature

Optional schema validation (Pydantic)

Verbosity Reduction

As prompts improve:

Explanations are removed

Output becomes structured

Token usage decreases

Outputs become consistent

Key Learning Outcomes

Prompt failures cause hallucinations

Clarity reduces ambiguity but is not sufficient alone

Guardrails outperform model upgrades

System and user roles must be separated

Reliable systems require explicit permission for inference

Success Criteria (Achieved)

✔ Fewer false or exaggerated claims

✔ More consistent outputs

✔ Clear before vs after comparison

✔ Production-grade prompt design

Notes for Evaluators

Hallucinations are intentionally demonstrated in early prompts

A weaker model is used on purpose

Improvements are incremental and explainable
