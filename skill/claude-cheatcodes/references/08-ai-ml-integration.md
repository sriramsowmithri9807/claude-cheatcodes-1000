# 08-ai-ml-integration

LLM apps: Claude API, tool use, RAG, embeddings, agents, LangChain/LlamaIndex, prompt caching.

41 prompts. Search `## ` headings or ids; see index.md for the one-line list.

## Build AI Agents with Claude

**id:** `08-ai-ml-integration/ai-agents` · **Difficulty:** advanced · **Tags:** agents, tools, claude, ai

**Placeholders:** [DESCRIBE: research agent, coding agent, data analysis agent, customer service]

````text
Build an AI agent system using Claude with tool use.

Agent purpose: [DESCRIBE: research agent, coding agent, data analysis agent, customer service]

Implement:
1. **Tool definition**: define tools as JSON schema (Claude understands these)
2. **Tool examples**:
   - `search_web(query)` → results
   - `execute_code(code)` → output
   - `read_file(path)` → content
   - `query_database(sql)` → results
3. **Agentic loop**: Claude → tool call → result → Claude → ... → final answer
4. **Multi-agent**: orchestrator agent + specialist sub-agents
5. **Memory**: short-term (conversation), long-term (vector DB)
6. **Error handling**: tool failures, retries, fallbacks
7. **Safety guardrails**: what agents are NOT allowed to do
8. **Observation and logging**: trace every action for debugging

Node.js implementation with the Anthropic SDK.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Add AI-Powered Analytics

**id:** `08-ai-ml-integration/ai-analytics` · **Difficulty:** advanced · **Tags:** analytics, ai, claude, insights

**Placeholders:** [DESCRIBE YOUR METRICS AND DATABASES], [LIST 5-10 KEY BUSINESS QUESTIONS]

````text
Add AI-powered analytics and insights to my business application.

Data available: [DESCRIBE YOUR METRICS AND DATABASES]
Business questions to answer: [LIST 5-10 KEY BUSINESS QUESTIONS]

1. **Natural language to SQL**: Claude converts business questions to SQL queries
2. **Query execution**: run the SQL safely (read-only role)
3. **Result interpretation**: Claude explains what the numbers mean
4. **Anomaly detection**: flag unusual patterns in metrics
5. **Trend analysis**: identify and explain trends over time
6. **Prediction**: simple forecasting (Claude + statistical method)
7. **Automated insights**: weekly AI-generated insights report
8. **Comparative analysis**: compare periods, segments, cohorts
9. **Root cause analysis**: why did metric X drop this week?
10. **Chart recommendations**: which visualization best shows this data?

Safety: read-only database access, query validation.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Build an AI Code Generation Tool

**id:** `08-ai-ml-integration/ai-code-generation` · **Difficulty:** advanced · **Tags:** code-generation, claude, developer-tools, ai

**Placeholders:** [DESCRIBE: generate boilerplate, explain code, convert between languages, refactor], [PROGRAMMING LANGUAGES]

````text
Build an AI code generation and explanation tool.

Use case: [DESCRIBE: generate boilerplate, explain code, convert between languages, refactor]
Language focus: [PROGRAMMING LANGUAGES]

1. **Code generation**: from natural language description → working code
2. **Multi-file generation**: generate an entire feature spanning multiple files
3. **Code explanation**: explain what this code does, line by line
4. **Code refactoring**: improve readability, performance, patterns
5. **Language conversion**: Python → TypeScript, SQL → code, etc.
6. **Test generation**: generate unit tests for existing code
7. **Documentation**: generate JSDoc/docstrings for functions
8. **Debugging help**: identify bugs and suggest fixes
9. **Code review**: review for security, performance, style issues
10. **Interactive REPL**: user iterates on generated code in conversation

UI with Monaco editor (VS Code in browser).
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Build an AI Code Review Tool

**id:** `08-ai-ml-integration/ai-code-review` · **Difficulty:** advanced · **Tags:** code-review, claude, ai, development

**Placeholders:** [LIST], [SECURITY / PERFORMANCE / STYLE / ALL]

````text
Build an AI-powered code review tool using Claude.

Review focus: [SECURITY / PERFORMANCE / STYLE / ALL]
Languages: [LIST]

1. **GitHub PR integration**: webhook → fetch diff → analyze → comment
2. **Review prompt**: analyze for bugs, security issues, performance, style
3. **Structured output**: list of issues with: file, line, severity, description, suggestion
4. **Severity levels**: critical (must fix), major (should fix), minor (nice to fix)
5. **Context loading**: load related files for better analysis
6. **Auto-fix suggestions**: generate corrected code for simple issues
7. **False positive reduction**: learn from reviewer dismissals
8. **GitHub PR comments**: post inline comments on specific lines
9. **Summary comment**: overall assessment at top of PR
10. **Rate limiting**: respect both Claude and GitHub API limits

GitHub App implementation.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Build an AI Content Generation Pipeline

**id:** `08-ai-ml-integration/ai-content-pipeline` · **Difficulty:** intermediate · **Tags:** content, generation, claude, automation

**Placeholders:** [DESCRIBE DESIRED FORMAT], [DESCRIBE: blog posts, product descriptions, social media, emails], [DESCRIBE: product data, topics list, customer segment]

````text
Build an automated content generation pipeline using Claude.

Content type: [DESCRIBE: blog posts, product descriptions, social media, emails]
Input: [DESCRIBE: product data, topics list, customer segment]
Output: [DESCRIBE DESIRED FORMAT]

Pipeline:
1. **Input processing**: parse and validate input data
2. **Prompt construction**: dynamic prompt with input variables
3. **Parallel generation**: generate N pieces of content concurrently
4. **Quality filtering**: Claude self-evaluates each piece, reject below threshold
5. **Human review queue**: flag borderline content for review
6. **Post-processing**: format, add metadata, validate output schema
7. **Storage**: save to CMS or database
8. **Rate limiting**: respect Claude API rate limits
9. **Cost tracking**: track tokens and cost per run
10. **Monitoring**: alert on high rejection rates

Node.js implementation with BullMQ for queuing.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Optimize AI API Costs

**id:** `08-ai-ml-integration/ai-cost-optimization` · **Difficulty:** intermediate · **Tags:** cost, optimization, claude, tokens

**Placeholders:** [DESCRIBE: how many calls/day, average tokens, which models], [ESTIMATE]

````text
Optimize my Claude API usage costs without sacrificing quality.

Current usage: [DESCRIBE: how many calls/day, average tokens, which models]
Current monthly cost: [ESTIMATE]

Optimization strategies:
1. **Prompt caching**: cache shared system prompts (90% token discount)
2. **Model routing**: use Haiku for simple tasks, Sonnet for medium, Opus for complex
3. **Input compression**: remove unnecessary whitespace, abbreviate where safe
4. **Output length control**: `max_tokens` limits runaway outputs
5. **Batching**: batch API for non-real-time use cases (50% discount)
6. **Caching responses**: cache Claude responses for identical inputs (Redis)
7. **Streaming**: stream to user (doesn't affect cost, but better UX)
8. **Avoid retries on same prompt**: use exponential backoff for errors only
9. **Pre-computation**: generate and cache content in advance
10. **Monitor**: track cost per user, per feature, alert on anomalies

Target: 50% cost reduction. Show the math.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Handle AI Errors Gracefully

**id:** `08-ai-ml-integration/ai-error-handling` · **Difficulty:** intermediate · **Tags:** error-handling, claude, reliability, api

````text
Handle all error scenarios in my Claude API integration gracefully.

Error types to handle:
1. **Rate limit (429)**: exponential backoff: 1s, 2s, 4s, 8s, 16s, give up
2. **Overloaded (529)**: server busy — retry with longer delay
3. **Invalid request (400)**: prompt too long, invalid parameters — don't retry, fix it
4. **Auth error (401)**: invalid API key — alert, don't retry
5. **Timeout**: stream stalls — detect with timeout, abort and retry
6. **Partial response**: stream cut off mid-sentence — detect and complete or retry
7. **Content policy**: Claude refuses the request — graceful fallback message
8. **JSON parsing**: Claude returns malformed JSON — retry with stronger format instruction
9. **Token limit**: response truncated — detect and request continuation
10. **Network errors**: ECONNRESET, etc. — retry with backoff

Reusable retry wrapper for all Claude API calls.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Evaluate and Improve Your AI Features

**id:** `08-ai-ml-integration/ai-evaluation` · **Difficulty:** advanced · **Tags:** evaluation, llm, quality, metrics

**Placeholders:** [DESCRIBE]

````text
Build an evaluation framework for your AI-powered features.

AI feature to evaluate: [DESCRIBE]

1. **Eval dataset**: curate 200 representative test cases
   - Happy path inputs
   - Edge cases
   - Adversarial inputs
   - Common failure modes
2. **Metrics**:
   - Task success rate
   - Response quality (LLM judge 1-5)
   - Helpfulness (LLM judge)
   - Hallucination rate
   - Latency p50/p95
   - Cost per successful task
3. **LLM judge**: use Claude to score Claude's outputs against rubric
4. **Regression tracking**: track metrics over time, alert on drops
5. **Prompt experimentation**: A/B test prompt variants against eval set
6. **Error analysis**: cluster failures by type, identify patterns
7. **Human baseline**: how well would a human do this task?

Automated eval pipeline in CI that runs weekly.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Build an AI Feedback and Learning Loop

**id:** `08-ai-ml-integration/ai-feedback-loop` · **Difficulty:** advanced · **Tags:** feedback, ai, improvement, mlops

**Placeholders:** [DESCRIBE]

````text
Build a feedback loop to continuously improve your AI features.

AI feature: [DESCRIBE]

1. **Implicit feedback**: track engagement signals (did user accept the suggestion?)
2. **Explicit feedback**: thumbs up/down on AI responses
3. **Feedback storage**: log: input, output, user_action, timestamp
4. **Failure analysis**: weekly review of thumbs-down responses
5. **Prompt improvement**: use failures to improve prompts (human-in-the-loop)
6. **A/B testing framework**: compare prompt variants on live traffic
7. **Statistical significance**: how many samples before declaring winner
8. **Automated improvement**: use Claude to suggest prompt improvements based on failures
9. **Regression prevention**: eval set that catches any new regressions
10. **Quality metrics over time**: track improvement rate

Dashboard showing: satisfaction rate, top failure categories, prompt history.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Fine-Tune a Model for Your Task

**id:** `08-ai-ml-integration/ai-fine-tuning` · **Difficulty:** advanced · **Tags:** fine-tuning, ml, training, claude

**Placeholders:** [DESCRIBE WHY PROMPTING ALONE ISN'T ENOUGH], [DESCRIBE YOUR TASK]

````text
Design a fine-tuning strategy for my specialized task.

Task: [DESCRIBE YOUR TASK]
Why fine-tuning: [DESCRIBE WHY PROMPTING ALONE ISN'T ENOUGH]

Note: Claude API doesn't support fine-tuning (use Anthropic commercial agreements or another model)

Alternatives to fine-tuning first:
1. **Better prompting**: few-shot examples, chain-of-thought
2. **RAG**: add domain knowledge without training
3. **Prompt caching**: large few-shot set without cost

If fine-tuning is the right choice (open-source model):
4. **Dataset preparation**: format, quality, quantity requirements
5. **Base model selection**: Llama 3, Mistral, Phi-3
6. **Fine-tuning method**: LoRA / QLoRA (efficient)
7. **Training**: Google Colab, AWS EC2 GPU
8. **Evaluation**: compare fine-tuned vs base model on your eval set
9. **Serving**: Ollama local, Modal or HuggingFace for cloud
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Run AI Models Locally

**id:** `08-ai-ml-integration/ai-local` · **Difficulty:** intermediate · **Tags:** local-ai, ollama, llama, offline

**Placeholders:** [DESCRIBE: development, privacy-sensitive data, offline use, cost reduction]

````text
Run AI models locally for development and privacy.

Use case: [DESCRIBE: development, privacy-sensitive data, offline use, cost reduction]

Using: Ollama

1. **Installation**: `curl -fsSL https://ollama.ai/install.sh | sh`
2. **Pull models**: `ollama pull llama3.1:8b`, `ollama pull mistral`, `ollama pull codellama`
3. **Ollama API**: OpenAI-compatible REST API at localhost:11434
4. **Integration**: drop-in replacement for OpenAI SDK
5. **Model selection guide**: which model for which task
6. **GPU acceleration**: NVIDIA CUDA, Apple Metal (M1/M2)
7. **Context length**: manage smaller context windows
8. **Quantization**: Q4_K_M (smallest), Q8_0 (quality), F16 (full)
9. **Modelfile**: customize system prompt, temperature
10. **LM Studio**: GUI alternative to Ollama

Compare: local vs Claude API — when each makes sense.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Build AI Content Moderation

**id:** `08-ai-ml-integration/ai-moderation` · **Difficulty:** advanced · **Tags:** moderation, safety, claude, content

**Placeholders:** [DESCRIBE: text posts, images, user bios, comments], [SPAM / HATE / ADULT / VIOLENCE / OTHER]

````text
Build an AI content moderation system using Claude.

Content types to moderate: [DESCRIBE: text posts, images, user bios, comments]
Violation categories: [SPAM / HATE / ADULT / VIOLENCE / OTHER]

1. **Text moderation**: classify content by violation type
2. **Severity scoring**: 0-1 score for each category
3. **Action triggers**: auto-remove (high severity) vs human review (medium) vs allow (low)
4. **Context awareness**: same text may be ok in one community, not another
5. **Appeal system**: users can appeal, human reviews with AI suggestion
6. **Consistency**: same content → same decision (deterministic where possible)
7. **Adversarial inputs**: detect attempts to bypass moderation
8. **Performance**: < 100ms for text moderation (use Haiku)
9. **Audit log**: every decision logged with reasoning
10. **Calibration**: track false positive rate, adjust thresholds
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Build AI-Powered Personalization

**id:** `08-ai-ml-integration/ai-personalization` · **Difficulty:** advanced · **Tags:** personalization, recommendations, claude, ai

**Placeholders:** [DESCRIBE: behavior, preferences, demographics, history], [E-COMMERCE / CONTENT / LEARNING / OTHER]

````text
Build an AI personalization system for my platform.

Platform type: [E-COMMERCE / CONTENT / LEARNING / OTHER]
User data available: [DESCRIBE: behavior, preferences, demographics, history]

1. **User profile building**: summarize user interests from behavior
2. **Content recommendations**: find items matching user profile
3. **Collaborative filtering**: users similar to you also liked...
4. **Explanation**: "We recommend this because..."
5. **Diversity**: avoid filter bubble (mix familiar + new)
6. **Cold start**: new users with no history
7. **Contextual**: time of day, device, location adjustments
8. **Real-time**: recommendations update as user interacts
9. **A/B testing**: compare AI recommendations vs rule-based
10. **Feedback**: thumbs up/down to refine recommendations

Claude + embeddings for user/item matching.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Orchestrate AI Pipelines

**id:** `08-ai-ml-integration/ai-pipeline-orchestration` · **Difficulty:** advanced · **Tags:** orchestration, pipelines, claude, agents

**Placeholders:** [DESCRIBE YOUR MULTI-STEP AI WORKFLOW]

````text
Build a complex AI pipeline that chains multiple Claude calls.

Pipeline goal: [DESCRIBE YOUR MULTI-STEP AI WORKFLOW]

1. **Pipeline definition**: graph of steps with dependencies
2. **Step types**: transform, classify, generate, validate, branch
3. **Data flow**: output of step N → input of step N+1
4. **Parallelism**: run independent steps in parallel
5. **Branching**: different paths based on step output
6. **Validation gates**: validate output before passing to next step
7. **Retry logic**: retry failed steps with different approach
8. **State persistence**: save pipeline state (can resume if interrupted)
9. **Cost tracking**: track tokens per step
10. **Visualization**: diagram of pipeline execution
11. **Testing**: unit test each step independently
12. **Monitoring**: latency and success rate per step

Node.js implementation with a DAG executor.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Build a Question Answering System

**id:** `08-ai-ml-integration/ai-question-answering` · **Difficulty:** intermediate · **Tags:** qa, claude, knowledge-base, rag

**Placeholders:** [DESCRIBE WHO WILL ASK QUESTIONS], [DESCRIBE: documentation, FAQ, product manual, internal wiki]

````text
Build a question answering system over my knowledge base.

Knowledge base: [DESCRIBE: documentation, FAQ, product manual, internal wiki]
User types: [DESCRIBE WHO WILL ASK QUESTIONS]

1. **Document indexing**: chunk and embed all documents
2. **Question understanding**: rephrase/expand question for better retrieval
3. **Context retrieval**: find most relevant document sections
4. **Answer generation**: Claude answers using ONLY retrieved context
5. **Citation**: cite which document/section the answer comes from
6. **"I don't know"**: Claude admits when answer isn't in the knowledge base
7. **Followup handling**: conversational Q&A with memory
8. **Confidence**: flag uncertain answers for human review
9. **Analytics**: most common questions → improve documentation
10. **Feedback loop**: thumbs up/down improves retrieval over time

Full-stack implementation.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Secure Your AI Application

**id:** `08-ai-ml-integration/ai-security` · **Difficulty:** advanced · **Tags:** security, ai, prompt-injection, claude

**Placeholders:** [DESCRIBE YOUR AI FEATURE]

````text
Secure my AI application against prompt injection and abuse.

App: [DESCRIBE YOUR AI FEATURE]

Threats:
1. **Prompt injection**: user input overrides system prompt
   - Defense: XML tags around user input, clear delimiters
   - Defense: validate Claude's output before acting on it
2. **Jailbreaking**: bypass safety guidelines
   - Defense: Claude's built-in safety is strong, add extra layer
3. **Data exfiltration**: get Claude to reveal system prompt or training data
   - Defense: never put secrets in system prompt
4. **Resource exhaustion**: max_tokens abuse
   - Defense: output length limits per user tier
5. **Content policy violations**: generate harmful content
   - Defense: output scanning before displaying
6. **Cost attacks**: trigger expensive requests
   - Defense: rate limiting, cost per user limit
7. **Indirect injection**: malicious content in RAG documents injected into prompt
   - Defense: sanitize retrieved content

Implement all defenses in code.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Stream AI Responses in Real-Time

**id:** `08-ai-ml-integration/ai-streaming` · **Difficulty:** intermediate · **Tags:** streaming, claude, ux, real-time

````text
Implement real-time streaming of Claude responses for great UX.

UI framework: [React / Next.js / Vue]

Backend (Node.js):
1. Claude streaming API: `stream: true`
2. Event types: `message_start`, `content_block_delta`, `message_stop`
3. SSE endpoint: forward Claude stream to frontend
4. Error handling mid-stream
5. Abort: cancel stream when user clicks stop button

Frontend (React):
6. Fetch with ReadableStream
7. Append tokens to state as they arrive
8. Show typing indicator while waiting for first token
9. Auto-scroll to bottom
10. Stop button: abort fetch, stop stream

Edge deployment:
11. Vercel Edge Functions for minimal latency
12. OpenAI-compatible streaming format for compatibility

Full implementation with beautiful streaming chat UI.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Get Reliable Structured Output from Claude

**id:** `08-ai-ml-integration/ai-structured-output` · **Difficulty:** intermediate · **Tags:** structured-output, json, validation, claude

**Placeholders:** [DESCRIBE YOUR TARGET JSON SCHEMA]

````text
Get reliable structured JSON output from Claude every time.

Data structure needed: [DESCRIBE YOUR TARGET JSON SCHEMA]

Techniques (from fragile to reliable):

1. **Basic**: ask for JSON in the prompt
2. **Schema in prompt**: include your JSON schema with descriptions
3. **Few-shot examples**: show 2-3 examples of correct JSON output
4. **XML wrapping**: ask Claude to wrap JSON in `<json>` tags (parse easily)
5. **Validation + retry**: if Zod validation fails, send error back to Claude
6. **Format reminder**: end prompt with "Remember: respond ONLY with valid JSON"
7. **Temperature 0**: for consistency in structured tasks
8. **Output type in system prompt**: tell Claude its output type from the start
9. **Anthropic beta JSON mode**: if available, use tool_use with defined schema
10. **Post-processing**: fix common JSON mistakes (trailing commas, unquoted keys)

Reusable TypeScript function for each approach.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Build Text Summarization Features

**id:** `08-ai-ml-integration/ai-summarization` · **Difficulty:** intermediate · **Tags:** summarization, claude, nlp, content

**Placeholders:** [BULLET POINTS / PARAGRAPH / STRUCTURED SECTIONS], [DESCRIBE: articles, meeting transcripts, reports, emails], [WHO WILL READ THE SUMMARY]

````text
Add AI summarization to my application.

Content to summarize: [DESCRIBE: articles, meeting transcripts, reports, emails]
Summary format: [BULLET POINTS / PARAGRAPH / STRUCTURED SECTIONS]
Audience: [WHO WILL READ THE SUMMARY]

1. **Summary types**:
   - Executive summary: 3 bullet points for busy readers
   - Detailed summary: preserves all key points
   - Meeting minutes: action items, decisions, attendees
   - Abstractive: new sentences (not copied from original)
2. **Long document handling**: chunk → summarize each → meta-summarize
3. **Key points extraction**: numbered list of most important points
4. **Action items**: extract TODO items from meeting notes
5. **Sentiment**: add overall tone (positive/negative/neutral)
6. **Multilingual**: summarize in a different language
7. **Custom length**: user controls word count
8. **Citation**: which part of original supports each summary point

React component + backend API.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Test AI-Powered Features

**id:** `08-ai-ml-integration/ai-testing` · **Difficulty:** advanced · **Tags:** testing, ai, llm, evaluation

**Placeholders:** [DESCRIBE YOUR AI FEATURE]

````text
Design a testing strategy for AI-powered features.

AI feature to test: [DESCRIBE YOUR AI FEATURE]

Challenges with AI testing:
- Non-deterministic: same input → different output each time
- Hard to assert: what is a "correct" response?
- Expensive: can't run LLM calls in unit tests
- Prompt regression: changing prompt changes behavior unpredictably

Testing strategies:
1. **Mock Claude**: return canned responses in unit tests
2. **Eval datasets**: 100 input/expected-output pairs, run weekly
3. **LLM judge**: use Claude to evaluate Claude's own outputs
4. **Property tests**: test properties (length, format, tone) not exact text
5. **Regression testing**: compare new vs old prompt on same inputs
6. **Human evaluation**: periodic human review of 50 random outputs
7. **Red teaming**: adversarial inputs trying to break the system
8. **Latency testing**: measure p95 latency under load
9. **Cost regression**: alert if tokens per request increases 20%+
10. **Shadow mode**: run new prompt alongside old, compare before switching
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Build AI-Powered Translation

**id:** `08-ai-ml-integration/ai-translation` · **Difficulty:** intermediate · **Tags:** translation, multilingual, claude, nlp

**Placeholders:** [DESCRIBE: user content, UI strings, documents, real-time chat]

````text
Add AI-powered translation and localization to my app.

Use case: [DESCRIBE: user content, UI strings, documents, real-time chat]
Language pairs: [SOURCE → TARGET LANGUAGES]

1. **Basic translation**: Claude translates between any language pair
2. **Context-aware**: provide surrounding context for better translation
3. **Tone preservation**: formal vs informal, brand voice
4. **Domain-specific**: legal, medical, technical — use domain vocabulary
5. **Glossary**: maintain consistent translation of key terms
6. **Transliteration**: romanize scripts (Arabic, Chinese, etc.)
7. **Back-translation**: verify quality by translating back
8. **Streaming**: stream translation for real-time feel
9. **Caching**: cache translations to reduce API calls
10. **Quality evaluation**: BLEU score approximation

Integrate with i18next for UI string management.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Build AI-Powered Workflow Automation

**id:** `08-ai-ml-integration/ai-workflow-automation` · **Difficulty:** advanced · **Tags:** workflow, automation, claude, agents

**Placeholders:** [DESCRIBE: data processing, content moderation, report generation, etc.]

````text
Build an AI-powered workflow automation system.

Workflows to automate: [DESCRIBE: data processing, content moderation, report generation, etc.]

1. **Workflow definition**: define steps, triggers, conditions
2. **Claude as orchestrator**: plan the workflow steps dynamically
3. **Tool integrations**: connect Claude to: database, APIs, email, Slack, calendar
4. **Human-in-the-loop**: pause for human review when confidence is low
5. **Error recovery**: Claude handles errors, tries alternative approaches
6. **State management**: persist workflow state across multiple Claude calls
7. **Parallel execution**: run independent workflow steps simultaneously
8. **Logging and observability**: trace every decision and action
9. **Approval gates**: require human approval for high-impact actions
10. **Testing**: replay recorded workflows to test changes

Node.js + LangChain or custom implementation.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Build an AI Writing Assistant

**id:** `08-ai-ml-integration/ai-writing-assistant` · **Difficulty:** intermediate · **Tags:** writing, assistant, claude, nlp

**Placeholders:** [DESCRIBE YOUR PLATFORM: blog, email, code comments, etc.]

````text
Build an AI writing assistant for [DESCRIBE YOUR PLATFORM: blog, email, code comments, etc.].

Features:
1. **Grammar correction**: fix errors while preserving voice
2. **Tone adjustment**: rewrite as formal, casual, professional, friendly
3. **Expansion**: make this paragraph longer with more detail
4. **Condensation**: make this shorter, get to the point
5. **Subject line generation**: given email body, generate 5 subject options
6. **Headline generation**: SEO-optimized headlines for blog posts
7. **Completion**: continue writing from where user stopped
8. **Rephrasing**: say this differently (offer 3 options)
9. **Plagiarism check** (heuristic): flag if output looks copied
10. **Brand voice**: learn brand guidelines, apply to all rewrites

React integration with selection-based actions (like Notion AI).
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Build a Production Chatbot

**id:** `08-ai-ml-integration/chatbot-system` · **Difficulty:** advanced · **Tags:** chatbot, claude, conversational-ai, nlp

**Placeholders:** [DESCRIBE YOUR CONTENT], [DESCRIBE: customer support, internal knowledge base, onboarding]

````text
Build a production-grade AI chatbot powered by Claude.

Bot purpose: [DESCRIBE: customer support, internal knowledge base, onboarding]
Knowledge base: [DESCRIBE YOUR CONTENT]

1. **System prompt engineering**: persona, tone, capabilities, guardrails
2. **Context management**: conversation history with token budget
3. **RAG integration**: retrieve relevant knowledge base articles
4. **Intent classification**: route to specialized handlers (FAQ, human escalation)
5. **Guardrails**: refuse off-topic, harmful, or confidential-info requests
6. **Escalation**: hand off to human agent with conversation summary
7. **Multi-language**: detect language, respond in same language
8. **Feedback collection**: thumbs up/down → improve prompts
9. **Analytics**: most common questions, satisfaction score
10. **A/B testing**: compare different system prompts

React UI + Node.js backend with streaming.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Get Started with the Claude API

**id:** `08-ai-ml-integration/claude-api-basics` · **Difficulty:** beginner · **Tags:** claude, api, anthropic, integration

**Placeholders:** [DESCRIBE WHAT YOU WANT TO BUILD WITH CLAUDE]

````text
Build a complete starter integration with the Anthropic Claude API.

Use case: [DESCRIBE WHAT YOU WANT TO BUILD WITH CLAUDE]

1. **Setup**: install `@anthropic-ai/sdk`, configure API key safely
2. **Basic completion**: send a message, receive a response
3. **Streaming**: stream the response token by token (for UI)
4. **System prompt**: set Claude's role and behavior
5. **Multi-turn conversation**: maintain chat history correctly
6. **Model selection**: Haiku (fast/cheap) vs Sonnet (balanced) vs Opus (powerful) vs Fable 5 (latest)
7. **Parameters**: max_tokens, temperature, top_p
8. **Error handling**: rate limits, API errors, timeouts
9. **Cost estimation**: tokens → cost calculation
10. **Best practices**: prompt caching, batching, async processing

Output: working Node.js + TypeScript integration with all patterns above.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Leverage Claude Fable 5 Unique Features

**id:** `08-ai-ml-integration/claude-fable5-features` · **Difficulty:** advanced · **Tags:** fable-5, extended-thinking, claude, advanced

**Placeholders:** [DESCRIBE YOUR COMPLEX TASKS]

````text
Leverage Claude Fable 5's unique capabilities for advanced tasks.

Tasks requiring Fable 5: [DESCRIBE YOUR COMPLEX TASKS]

1. **Extended thinking**: enable for complex reasoning tasks
   - Set `thinking: {type: 'enabled', budget_tokens: 10000}`
   - Show thinking in UI or hide it (stream_thinking vs stream_text)
   - Use cases: math, logic, code architecture, complex analysis
2. **200K context window**: send entire codebases or long documents
3. **Superior code generation**: complex algorithms, architecture
4. **Advanced reasoning**: multi-step logical problems
5. **Tool use with thinking**: agent thinks before using tools
6. **Long-form writing**: coherent long documents, books, reports
7. **Complex analysis**: compare large datasets, find patterns
8. **Calibration**: Fable 5 knows what it doesn't know

When to use Fable 5 vs Sonnet 4 vs Haiku 3.5 — decision matrix.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Master Claude Tool Use (Function Calling)

**id:** `08-ai-ml-integration/claude-tool-use` · **Difficulty:** advanced · **Tags:** tool-use, function-calling, claude, agents

**Placeholders:** [DESCRIBE WHAT TOOLS YOUR AGENT NEEDS]

````text
Master Claude's tool use (function calling) feature.

Tools to implement: [DESCRIBE WHAT TOOLS YOUR AGENT NEEDS]

1. **Tool definition**: name, description, input_schema (JSON Schema)
2. **Tool examples**:
   ```
   get_weather(city: string) → temperature, conditions
   search_database(query: string, table: string) → results
   send_email(to: string, subject: string, body: string) → success
   create_calendar_event(title, start, end, attendees) → event_id
   ```
3. **Parallel tool use**: Claude calls multiple tools simultaneously
4. **Tool error handling**: tool fails → inform Claude → it adapts
5. **Confirmation pattern**: ask user before executing irreversible tools
6. **Tool result formatting**: how to structure results for Claude
7. **Chain of tools**: multi-step tasks using multiple tools
8. **Safety**: validate tool inputs before executing
9. **Logging**: audit trail of every tool call
10. **Streaming with tool use**: handle streaming when tools are involved

Node.js SDK implementation.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Integrate Vision AI into Your App

**id:** `08-ai-ml-integration/computer-vision` · **Difficulty:** advanced · **Tags:** vision, images, claude, multimodal

**Placeholders:** [DESCRIBE: product image analysis, document scanning, screenshot understanding, medical imaging]

````text
Integrate Claude's vision capabilities into my application.

Use case: [DESCRIBE: product image analysis, document scanning, screenshot understanding, medical imaging]

1. **Image input**: send images to Claude (URL or base64)
2. **Image description**: generate detailed description of image content
3. **Object detection**: identify and list objects in the image
4. **Document OCR**: extract text from documents and receipts
5. **Data extraction from images**: extract structured data from forms/tables
6. **Image comparison**: compare two images, describe differences
7. **UI analysis**: analyze screenshot, generate code to recreate it
8. **Chart understanding**: extract data from charts and graphs
9. **Batch processing**: analyze hundreds of images efficiently
10. **Caching**: cache analysis results to avoid re-processing same image

Node.js + TypeScript implementation with Claude's multimodal API.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Extract Structured Data from Unstructured Text

**id:** `08-ai-ml-integration/data-extraction` · **Difficulty:** intermediate · **Tags:** extraction, nlp, structured-data, claude

**Placeholders:** [DESCRIBE: receipts, resumes, medical notes, legal contracts, emails], [LIST FIELDS TO EXTRACT]

````text
Extract structured data from unstructured text using Claude.

Input text type: [DESCRIBE: receipts, resumes, medical notes, legal contracts, emails]
Data to extract: [LIST FIELDS TO EXTRACT]

1. **Define output schema** (TypeScript interface or Zod schema)
2. **Extraction prompt**: precise instructions for each field
3. **JSON mode**: force structured JSON output
4. **Validation**: Zod validate the extracted data
5. **Handling missing data**: null vs "not mentioned" vs inferred
6. **Tables extraction**: extract tabular data from text
7. **Multiple records**: extract list of items from one document
8. **Accuracy**: handle typos, abbreviations, different formats
9. **Normalization**: dates → ISO 8601, currencies → decimal
10. **Confidence**: flag fields where extraction is uncertain

Batch processing for high volume.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Build a Document Analysis System

**id:** `08-ai-ml-integration/document-analysis` · **Difficulty:** intermediate · **Tags:** documents, pdf, analysis, claude

**Placeholders:** [DESCRIBE: extract key data points, summarize, classify, compare]

````text
Build a system to analyze and extract information from documents.

Document types: [PDFs, Word docs, Excel, emails, etc.]
Extraction goal: [DESCRIBE: extract key data points, summarize, classify, compare]

Implement:
1. **Document loading**: PDF parsing (pdf-parse), DOCX (mammoth), Excel (xlsx)
2. **Text extraction**: preserve structure (headings, tables, lists)
3. **Claude analysis prompt**: extract specific structured data
4. **Structured output**: force JSON output with schema validation
5. **Table extraction**: extract tables as structured data
6. **Multi-document comparison**: compare N documents for differences
7. **Citation extraction**: identify and validate citations
8. **PII detection**: find and flag personal information
9. **Batch processing**: process hundreds of documents efficiently
10. **Output formats**: JSON, CSV, structured database records

Node.js + TypeScript with Zod validation.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Build a Knowledge Graph with AI

**id:** `08-ai-ml-integration/knowledge-graph` · **Difficulty:** advanced · **Tags:** knowledge-graph, neo4j, ai, claude

**Placeholders:** [DESCRIBE: documents, articles, research papers], [ENTITIES, RELATIONSHIPS]

````text
Build a knowledge graph powered by AI extraction.

Source content: [DESCRIBE: documents, articles, research papers]
Knowledge to extract: [ENTITIES, RELATIONSHIPS]

1. **Entity extraction**: Claude identifies named entities (people, orgs, concepts, products)
2. **Relationship extraction**: Claude identifies relationships between entities
3. **Coreference resolution**: "he" refers to "CEO John Smith"
4. **Entity deduplication**: "Apple Inc" and "Apple" are the same entity
5. **Confidence scoring**: flag low-confidence extractions for review
6. **Graph storage**: Neo4j for property graph
7. **Graph queries**: find connections, shortest path, influential nodes
8. **Visualization**: interactive graph UI (vis.js or D3 force graph)
9. **Updates**: add new documents without duplicating existing entities
10. **Export**: SPARQL-compatible RDF format

Python implementation with async processing.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Build with LangChain and Claude

**id:** `08-ai-ml-integration/langchain-integration` · **Difficulty:** advanced · **Tags:** langchain, claude, ai, chains

**Placeholders:** [DESCRIBE YOUR USE CASE]

````text
Build a LangChain application using Claude as the LLM.

Application: [DESCRIBE YOUR USE CASE]

Using: LangChain.js (or Python)

1. **Claude LLM setup**: `ChatAnthropic` with model selection
2. **Prompt templates**: `ChatPromptTemplate` with variables
3. **Chains**: LCEL (LangChain Expression Language) pipe syntax
4. **Retrieval chain**: RAG with document loader + splitter + vector store
5. **Conversational retrieval**: memory + retrieval for chat over docs
6. **Agents**: Claude-powered agent with web search tool
7. **Output parsers**: structured output (JSON, Pydantic)
8. **Callbacks**: streaming, logging, token counting
9. **Memory**: ConversationBufferMemory, VectorStoreMemory
10. **LangSmith**: tracing and debugging your chain

Output: complete application with all components.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Build a Multimodal AI App

**id:** `08-ai-ml-integration/multi-modal-app` · **Difficulty:** advanced · **Tags:** multimodal, vision, claude, images

**Placeholders:** [DESCRIBE: photo analysis app, document processor, visual Q&A, design feedback tool]

````text
Build a multimodal application using Claude's text + vision capabilities.

Application: [DESCRIBE: photo analysis app, document processor, visual Q&A, design feedback tool]

1. **File upload**: support images (JPEG, PNG, WebP, GIF) and PDFs
2. **Image preprocessing**: resize large images (< 5MB limit), convert format
3. **PDF handling**: extract pages as images for vision analysis
4. **Vision API call**: send image + text prompt to Claude
5. **Structured extraction**: extract structured data from images
6. **Multiple images**: compare multiple images in one prompt
7. **Conversation over image**: multi-turn conversation about uploaded image
8. **Caching**: cache analysis for same image hash
9. **Access control**: ensure users can only see their own uploaded images
10. **Usage tracking**: track image processing costs separately

Full-stack implementation.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Implement Claude Prompt Caching

**id:** `08-ai-ml-integration/prompt-caching` · **Difficulty:** intermediate · **Tags:** caching, claude, optimization, tokens

**Placeholders:** [DESCRIBE]

````text
Implement Claude's prompt caching feature to reduce costs and latency.

Use cases with large system prompts or repeated context: [DESCRIBE]

1. **What gets cached**: system prompt + any content before the last user message
2. **Cache breakpoint**: mark where to cache with `cache_control: {type: 'ephemeral'}`
3. **Cache window**: 5 minutes (extended with usage)
4. **Cost**: input tokens 90% cheaper when served from cache
5. **Latency**: cached tokens skip processing (faster TTFT)
6. **Pattern 1**: long system prompt with instructions + knowledge
7. **Pattern 2**: many-shot examples prepended to every request
8. **Pattern 3**: entire document as context for Q&A
9. **Measuring**: cache hits in API response headers
10. **Multi-turn**: cache grows as conversation continues

Calculate ROI: cost savings for your specific usage pattern.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Advanced Prompt Engineering for Claude

**id:** `08-ai-ml-integration/prompt-engineering` · **Difficulty:** intermediate · **Tags:** prompts, engineering, techniques, claude

**Placeholders:** [DESCRIBE YOUR TASK], [N], [X]

````text
Master advanced prompt engineering techniques for Claude.

Task: [DESCRIBE YOUR TASK]

Techniques to apply:
1. **Chain of Thought (CoT)**: "Let's think step by step"
2. **Few-shot examples**: show 3 examples of input → desired output
3. **Output format control**: JSON, XML, specific structure
4. **Role specification**: "You are an expert [X] with [N] years experience"
5. **Constraint specification**: what NOT to do
6. **Verification step**: ask Claude to check its own work
7. **Multi-step decomposition**: break complex tasks into steps
8. **Calibration prompts**: ask for confidence + reasoning
9. **XML tags for Claude**: `<context>`, `<task>`, `<format>` structure
10. **Extended thinking** (Claude Fable 5): enable deep reasoning

For MY task: the optimized prompt with each technique applied.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Build a RAG System

**id:** `08-ai-ml-integration/rag-system` · **Difficulty:** advanced · **Tags:** rag, embeddings, vector-db, claude

````text
Build a Retrieval-Augmented Generation (RAG) system using Claude.

Documents to search: [DESCRIBE YOUR CORPUS — docs, PDFs, codebase, support tickets]

Architecture:
1. **Document ingestion**:
   - Load documents (PDF, Markdown, HTML, code)
   - Chunk documents (strategies: fixed size, sentence, semantic)
   - Generate embeddings (Voyage AI or OpenAI embeddings)
   - Store in vector database (pgvector or Pinecone)
2. **Query pipeline**:
   - Embed user query
   - Vector similarity search (top-K results)
   - Re-rank results (cross-encoder)
   - Build context from retrieved chunks
   - Claude generates answer grounded in context
3. **Evaluation**: retrieval accuracy, answer faithfulness
4. **Optimizations**: hybrid search, metadata filtering, hypothetical document embeddings

Node.js + TypeScript implementation.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Build Semantic Search

**id:** `08-ai-ml-integration/semantic-search` · **Difficulty:** advanced · **Tags:** search, embeddings, vector-db, claude

**Placeholders:** [DESCRIBE WHAT USERS WILL SEARCH FOR], [DESCRIBE YOUR DATA]

````text
Build semantic search for my content.

Content to search: [DESCRIBE YOUR DATA]
Expected queries: [DESCRIBE WHAT USERS WILL SEARCH FOR]

1. **Embeddings**: choose embedding model (Voyage AI for best quality)
2. **Chunking strategy**: optimal chunk size for your content type
3. **Vector store**: pgvector (PostgreSQL) vs Pinecone vs Weaviate
4. **Indexing pipeline**: new content → embed → store
5. **Search**: embed query → similarity search → retrieve top-K
6. **Hybrid search**: combine BM25 (keyword) + semantic for best results
7. **Re-ranking**: use cross-encoder to re-rank top-20 → top-5
8. **Metadata filtering**: filter by date, category, author before vector search
9. **Query expansion**: use Claude to generate alternative queries
10. **Evaluation**: recall@K, NDCG metrics
11. **Result display**: highlight matching terms, show source

Full implementation with Node.js + pgvector.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Build a Text Classification System

**id:** `08-ai-ml-integration/text-classification` · **Difficulty:** intermediate · **Tags:** classification, nlp, claude, ml

**Placeholders:** [DESCRIBE: sentiment analysis, topic classification, spam detection, intent recognition], [EXPECTED VOLUME], [LIST YOUR CATEGORIES]

````text
Build a text classification system using Claude.

Classification task: [DESCRIBE: sentiment analysis, topic classification, spam detection, intent recognition]
Labels: [LIST YOUR CATEGORIES]
Input volume: [EXPECTED VOLUME]

1. **Zero-shot classification**: no examples needed (Claude understands)
2. **Few-shot classification**: provide examples for better accuracy
3. **Multi-label classification**: a document can belong to multiple categories
4. **Hierarchical classification**: coarse → fine-grained classification
5. **Confidence scores**: estimate confidence, flag low-confidence for review
6. **Batch processing**: classify thousands efficiently with caching
7. **Evaluation**: measure accuracy against labeled test set
8. **Confusion matrix**: which categories does the model confuse?
9. **Cost optimization**: cache results, use Haiku for simple cases
10. **Fine-tuning alternative**: when to use Claude vs a fine-tuned smaller model

Python implementation with async batching.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Set Up and Use a Vector Database

**id:** `08-ai-ml-integration/vector-database` · **Difficulty:** advanced · **Tags:** vector-db, pgvector, pinecone, embeddings

**Placeholders:** [DESCRIBE: semantic search, RAG, recommendation, deduplication], [DESCRIBE], [EXPECTED RECORD COUNT]

````text
Set up a vector database for AI/ML applications.

Use case: [DESCRIBE: semantic search, RAG, recommendation, deduplication]
Data to vectorize: [DESCRIBE]
Scale: [EXPECTED RECORD COUNT]

Option A — pgvector (PostgreSQL extension):
1. Install: `CREATE EXTENSION vector`
2. Column type: `embedding vector(1536)`
3. IVFFlat index: `CREATE INDEX ON items USING ivfflat (embedding vector_cosine_ops)`
4. HNSW index: faster search, more memory
5. Query: `ORDER BY embedding <-> $1 LIMIT 10`
6. Hybrid: combine with PostgreSQL FTS

Option B — Pinecone (managed):
7. Namespace for isolation
8. Metadata filtering
9. Sparse-dense hybrid

For my scale and query patterns: which to use and why?
Full indexing + query implementation.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` to your specific use case


## Configure RAG with [AI_STACK] and [OPTIMIZATION]

**id:** `08-ai-ml-integration/configure-rag-with-ai-stack-and-optimization` · **Difficulty:** intermediate/advanced · **Tags:** llm, ai, claude, agents, integration, retrieval-augmented, semantic, langchain, automated, llamaindex

**Variant group** (7 generated prompts collapsed). Pick one value per placeholder:
- `[AI_STACK]`: Claude SDK | LangChain | LlamaIndex | a Vector DB (Pinecone/Chroma)
- `[USE_CASE]`: agents with function calling capabilities | automated article summary engines | retrieval-augmented generation (RAG) pipelines | semantic search applications
- `[OPTIMIZATION]`: context window optimizations | prompt caching hooks | response streams handling | token usage analytics dashboards

````text
Set up a Retrieval-Augmented Generation pipeline using [AI_STACK] targeting [USE_CASE]. Implement [OPTIMIZATION] to optimize token costs.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Claude Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` and modify requirements based on your development environment and stack
- Use `--extended-thinking` mode for in-depth optimization suggestions

**Covers:** configure-rag-with-a-vector-db-pineconechroma-and-context-window-optimizations, configure-rag-with-claude-sdk-and-context-window-optimizations, configure-rag-with-claude-sdk-and-response-streams-handling, configure-rag-with-langchain-and-context-window-optimizations, configure-rag-with-langchain-and-token-usage-analytics-dashboards, configure-rag-with-llamaindex-and-prompt-caching-hooks, configure-rag-with-llamaindex-and-token-usage-analytics-dashboards


## Integrate [AI_STACK] for [USE_CASE]

**id:** `08-ai-ml-integration/integrate-ai-stack-for-use-case` · **Difficulty:** intermediate · **Tags:** email, llm, ai, anthropic, claude, integration, retrieval-augmented, hugging, agents, langchain, automated

**Variant group** (4 generated prompts collapsed). Pick one value per placeholder:
- `[AI_STACK]`: Anthropic Tool Use API | Claude SDK | Hugging Face transformers | LangChain
- `[USE_CASE]`: agents with function calling capabilities | automated article summary engines | email classification routes | retrieval-augmented generation (RAG) pipelines
- `[OPTIMIZATION]`: prompt caching hooks | token usage analytics dashboards

````text
Build a system that integrates [AI_STACK] to handle [USE_CASE]. Incorporate [OPTIMIZATION] to maximize performance and save API credits.
````

**Tips:**
- Works best with **Claude Sonnet 4** or **Claude Fable 5**
- Adjust `[BRACKETED PLACEHOLDERS]` and modify requirements based on your development environment and stack
- Use `--extended-thinking` mode for in-depth optimization suggestions

**Covers:** integrate-anthropic-tool-use-api-for-email-classification-routes, integrate-claude-sdk-for-retrieval-augmented-generation-rag-pipelines, integrate-hugging-face-transformers-for-agents-with-function-calling-capabilities, integrate-langchain-for-automated-article-summary-engines

