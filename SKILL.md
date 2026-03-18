---
name: fabric
description: "Fabric is an open-source AI augmentation framework by Daniel Miessler (github.com/danielmiessler/Fabric). Use when users want to: (1) Summarize, analyze, or extract information from any content (articles, code, videos, emails), (2) Create content using AI patterns (summaries, commits, emails, art prompts), (3) Process YouTube videos/podcasts for transcripts and summaries, (4) Analyze code, logs, or security reports, (5) Work with any of 150+ AI prompts called Patterns, (6) Set up or configure AI providers, (7) Any prompt engineering or AI workflow task. Triggers: fabric, pattern, summarize with fabric, analyze with AI, YouTube transcript, extract insights, AI prompt framework, fabric patterns, use fabric to..."
---

# Fabric Skill

Fabric is an open-source framework for augmenting humans using AI. It provides a modular system of AI prompts ("Patterns") that work with any supported AI provider.

## Installation Check

Always verify Fabric is installed when starting a Fabric-related task:

```bash
fabric --version
```

If NOT installed, provide installation instructions:

**macOS/Linux:**
```bash
# One-liner install
curl -fsSL https://raw.githubusercontent.com/danielmiessler/fabric/main/scripts/installer/install.sh | bash

# OR via Go
go install github.com/danielmiessler/fabric/cmd/fabric@latest

# OR via Homebrew
brew install fabric-ai
```

**Windows:**
```powershell
# PowerShell installer
iwr -useb https://raw.githubusercontent.com/danielmiessler/fabric/main/scripts/installer/install.ps1 | iex

# OR via Winget
winget install danielmiessler.Fabric
```

After installation, run `fabric --setup` to configure AI providers.

## Helper Functions

### show_fabric_capabilities()

When users ask "what can fabric do for me?" or similar questions, show ALL patterns in a formatted table:

Run: `fabric --listpatterns` to get current list

Display as a clean markdown table organized by category:

**All Fabric Patterns (117 total)**

| Pattern | Description |
|---------|-------------|
| analyze_claims | Analyze claims in text for accuracy |
| analyze_comments | Analyze comments (YouTube, social media) |
| analyze_cfp_submission | Analyze conference proposal submissions |
| analyze_debate | Analyze debate arguments |
| analyze_email_headers | Analyze email headers for security |
| analyze_incident | Analyze security incidents |
| analyze_interviewer_techniques | Analyze job interview techniques |
| analyze_logs | Analyze system/application logs |
| analyze_malware | Analyze malware samples |
| analyze_paper | Analyze academic papers |
| analyze_patent | Analyze patent documents |
| analyze_personality | Analyze personality from text |
| analyze_presentation | Analyze presentations |
| analyze_product_feedback | Analyze product feedback |
| analyze_prose | Analyze writing style |
| analyze_prose_json | Analyze prose with JSON output |
| analyze_prose_pinker | Analyze prose using Pinker's style |
| analyze_sales_call | Analyze sales call transcripts |
| analyze_spiritual_text | Analyze spiritual/religious texts |
| analyze_tech_impact | Analyze technology impact |
| analyze_threat_report | Analyze threat intelligence reports |
| analyze_threat_report_trends | Analyze threat report trends |
| analyze_answers | Analyze Q&A answers |
| create_5_sentence_summary | Create 5-sentence summary |
| create_academic_paper | Write academic papers |
| create_ai_jobs_analysis | Analyze AI job market |
| create_aphorisms | Create memorable sayings |
| create_art_prompt | Generate AI art prompts |
| create_better_frame | Reframe ideas positively |
| create_coding_project | Create coding project plans |
| create_command | Create shell commands |
| create_cyber_summary | Create cybersecurity summaries |
| create_formal_email | Write formal emails |
| create_git_diff_commit | Generate commit messages |
| create_graph_from_input | Create ASCII graphs |
| create_hormozi_offer | Create compelling offers |
| create_idea_compass | Analyze ideas from multiple angles |
| create_investigation_visualization | Create investigation diagrams |
| create_keynote | Create presentation outlines |
| create_logo | Create logo descriptions |
| create_markmap_visualization | Create markmap mind maps |
| create_mermaid_visualization | Create Mermaid diagrams |
| create_mermaid_visualization_for_github | GitHub-optimized Mermaid |
| create_micro_summary | Create micro summaries |
| create_network_threat_landscape | Create threat landscape docs |
| create_npc | Create NPC characters |
| create_pattern | Create new Fabric patterns |
| create_quiz | Create quizzes |
| create_reading_plan | Create reading plans |
| create_recursive_outline | Create recursive outlines |
| create_report_finding | Create report findings |
| create_rpg_summary | Create RPG summaries |
| create_security_update | Create security updates |
| create_show_intro | Create show introductions |
| create_sigma_rules | Create Sigma detection rules |
| create_story_explanation | Explain stories |
| create_stride_threat_model | Create STRIDE threat models |
| create_summary | Create summaries |
| create_tags | Create tags/categories |
| create_threat_scenarios | Create threat scenarios |
| create_ttrc_graph | Create threat tree graphs |
| create_ttrc_narrative | Create threat narratives |
| create_upgrade_pack | Create upgrade plans |
| create_video_chapters | Create video chapter markers |
| create_visualization | Create visualizations |
| extract_algorithm_update_recommendations | Extract algorithm updates |
| extract_article_wisdom | Extract wisdom from articles |
| extract_book_ideas | Extract ideas from books |
| extract_book_recommendations | Extract book recommendations |
| extract_business_ideas | Extract business ideas |
| extract_controversial_ideas | Extract controversial ideas |
| extract_extraordinary_claims | Extract extraordinary claims |
| extract_ideas | Extract ideas |
| extract_insights | Extract insights |
| extract_insights_dm | Extract deep insights (Daniel Miessler) |
| extract_instructions | Extract instructions |
| extract_jokes | Extract jokes |
| extract_main_idea | Extract main ideas |
| extract_patterns | Extract patterns |
| extract_poc | Extract proof of concepts |
| extract_predictions | Extract predictions |
| extract_primary_problem | Extract primary problems |
| extract_questions | Extract questions |
| extract_recommendations | Extract recommendations |
| extract_references | Extract references |
| extract_wisdom | Extract wisdom |
| extract_verbs | Extract action verbs |
| explain_code | Explain code |
| explain_docs | Explain documentation |
| explain_math | Explain mathematics |
| explain_project | Explain projects |
| explain_terms | Explain terminology |
| agility_story | Write agility stories |
| answer_interview_question | Answer interview questions |
| capture_thinkers_work | Capture intellectual work |
| check_agreement | Check text agreements |
| clean_text | Clean text formatting |
| coding_master | Master-level coding assistance |
| compare_and_contrast | Compare and contrast items |
| export_data_as_csv | Export data as CSV |
| write_tiktok_script | Write TikTok scripts |
| write_tweet | Write tweets |
| ai | General AI assistant |
| create_conceptmap | Create HTML concept maps |
| wellness | Wellness/psychology analysis |

### show_available_llms()

When users ask "what LLMs can I use?" or "list available models", run:

```bash
fabric --listvendors
fabric --listmodels
```

Display as a formatted table showing all available providers and models.

### set_fabric_llm(provider, model)

When users want to change or set the LLM model, help them:

1. First show available options with `show_available_llms()`
2. Then set the model using the provider switch script:

```bash
# Quick provider switch
fabric-provider openai     # Use OpenAI cloud
fabric-provider lmstudio   # Use local LM Studio
fabric-provider status    # Check current config

# Or use inline options
fabric -p summarize -V anthropic -m claude-3-5-sonnet
```

Help user add credentials with `fabric-provider setup`.

## Provider Selection

Fabric supports multiple OpenAI-compatible endpoints. You can switch between:

| Provider    | Endpoint                    | Models                    | Use Case                    |
| ----------- | --------------------------- | ------------------------- | --------------------------- |
| **OpenAI**     | api.openai.com              | GPT-4o, GPT-5, o3, etc.  | Cloud, most models          |
| **LM Studio**  | 192.168.1.141:11435         | qwen3.5, gpt-oss, etc.   | Local, free, private        |

### Quick Switch Commands

```bash
# Configure credentials first (one-time)
fabric-provider setup

# Switch to OpenAI (cloud)
fabric-provider openai

# Switch to LM Studio (local)
fabric-provider lmstudio

# Check current provider
fabric-provider status
```

### Manual Provider Switching

```bash
# Use OpenAI vendor with cloud endpoint
fabric -p <pattern> -V OpenAI -m gpt-4o

# Use LM Studio vendor with local endpoint  
fabric -p <pattern> -V "LM Studio" -m qwen3.5-35b-a3b@4bit
```

### Credentials Setup

1. **Copy the example file:**
   ```bash
   cd scripts/
   cp skill.env.example skill.env
   ```

2. **Edit with your credentials:**
   ```bash
   nano skill.env
   # OPENAI_API_KEY=your-actual-key
   # OPENAI_URL=https://api.openai.com/v1
   # LMSTUDIO_URL=http://your-local-ip:11435/v1
   ```

3. **Run setup wizard (optional):**
   ```bash
   fabric-provider setup
   ```

> **Note:** `skill.env` is gitignored and never published. Only `skill.env.example` (with fake values) is shared.

## Core Commands

```bash
fabric -p <pattern>           # Use a pattern
fabric --listpatterns        # List all patterns
fabric --listvendors         # List AI providers
fabric --listmodels          # List all models
fabric --setup               # Configure Fabric
fabric --updatepatterns      # Update patterns
```

## Common Patterns

### Text Processing
```bash
# Summarize
echo "Long text..." | fabric -p summarize

# Extract wisdom
cat article.md | fabric -p extract_wisdom
echo "Content" | fabric -p extract_insights

# Analyze writing
echo "Text" | fabric -p analyze_prose

# Clean text
echo "Messy text" | fabric -p clean_text
```

### Code Tasks
```bash
# Explain code
cat code.py | fabric -p explain_code

# Generate commits
git diff | fabric -p create_git_diff_commit

# Create commands
echo "deploy docker" | fabric -p create_command

# Analyze logs
tail -100 app.log | fabric -p analyze_logs
```

### YouTube/Podcasts
```bash
# Get transcript
fabric -y "https://youtube.com/watch?v=..."

# With timestamps
fabric -y "URL" --transcript-with-timestamps

# Get comments
fabric -y "URL" --comments

# Summarize video
fabric -y "URL" | fabric -p summarize
```

### Content Creation
```bash
# Summaries
echo "Content" | fabric -p create_summary
echo "Content" | fabric -p create_5_sentence_summary

# Emails
echo "Request" | fabric -p create_formal_email

# Art prompts
echo "Scene" | fabric -p create_art_prompt

# Quizzes
echo "Topic" | fabric -p create_quiz
```

### Analysis
```bash
# Security reports
cat threat_report.md | fabric -p analyze_threat_report

# Malware
cat malware.py | fabric -p analyze_malware

# Papers
cat paper.pdf | fabric -p analyze_paper

# Sales calls
cat transcript.txt | fabric -p analyze_sales_call
```

### Diagrams
```bash
# Mermaid
echo "Content" | fabric -p create_mermaid_visualization

# Concept maps
echo "Topic" | fabric -p create_conceptmap
```

## Advanced Usage

### Variables & Context
```bash
# Custom variables
echo "Content" | fabric -p extract_ideas -v=#max:20

# Custom context
fabric -p summarize -C my_context

# Sessions
fabric -p ai --session my_session
```

### Web & Media
```bash
# Scrape URL
fabric --scrape_url "https://example.com"

# Image generation
fabric -p create_art_prompt --image-file output.png

# Speech to text
fabric --transcribe-file audio.mp3
```

### REST API
```bash
# Start server
fabric --serve

# Ollama mode
fabric --serve --serveOllama
```

## Model Configuration
```bash
# Specific model inline
fabric -p summarize -m claude-opus-4

# By vendor inline
fabric -p summarize -V anthropic -m claude-3-5-sonnet

# List models
fabric --listmodels
```

## Debugging
```bash
# Dry run
echo "Content" | fabric -p summarize --dry-run

# Debug levels
fabric -p summarize --debug 1  # Basic
fabric -p summarize --debug 2  # Detailed
```

## Pattern Reference

See `references/patterns.md` for complete pattern list organized by category:
- Analysis: analyze_logs, analyze_malware, analyze_paper, etc.
- Creation: create_summary, create_git_diff_commit, etc.
- Extraction: extract_wisdom, extract_insights, etc.
- Explanation: explain_code, explain_docs, etc.

## Supported Providers

- **Native**: OpenAI, Anthropic, Google Gemini, Ollama, Azure, Bedrock, Vertex
- **Compatible**: DeepSeek, Groq, Perplexity, Mistral, OpenRouter, Cerebras, GitHub Models, Venice AI, and 20+ more

Run `fabric --listvendors` for full list.
