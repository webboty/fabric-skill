# Fabric AI Augmentation Framework - Skill

<div align="center">

[![Fabric](https://img.shields.io/badge/Fabric-v1.4+-blue?style=for-the-badge)](https://github.com/danielmiessler/Fabric)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Mac%20%7C%20Linux%20%7C%20Windows-999999?style=for-the-badge)](#installation)

**The AI skill that turns you into an AI power user**

</div>

---

## Why This Skill Will Unlock Your AI Super Powers

### The Problem

**You already have AI. But are you using it to its full potential?**

Every day, you copy-paste content into ChatGPT, Claude, or Gemini. You write the same prompts over and over. You spend minutes crafting the perfect query—only to get a response that needs more refinement.

Meanwhile, there's a framework with **150+ battle-tested AI prompts** for virtually every task imaginable. Summarizing articles. Analyzing code. Extracting insights from YouTube videos. Generating commit messages. Creating diagrams. Writing emails. The list goes on.

**Fabric** is that framework. And this skill makes it available to every AI assistant you use.

---

### The Solution

**What if every AI tool you use became 10x more powerful?**

Fabric is an open-source framework that organizes AI prompts into reusable "Patterns." Instead of starting from scratch every time, you leverage patterns crafted by thousands of practitioners worldwide.

**What Fabric does:**
- 📝 **Summarize** articles, papers, and documents in seconds
- 🎬 **Transcribe** YouTube videos with timestamps
- 💻 **Analyze** code, logs, malware, and security reports
- ✍️ **Create** commit messages, emails, art prompts, diagrams
- 🔍 **Extract** insights, questions, recommendations, wisdom
- 🧠 **Explain** complex code, math, or documentation

**What makes it special:**
- Works with **35+ AI providers** (OpenAI, Anthropic, Gemini, Ollama, Azure, and more)
- **150+ curated patterns** that actually work
- Fully **open-source** and community-driven
- Available via **CLI, REST API, or Docker**

---

### The Benefits

**Stop reinventing the wheel. Start using production-grade AI workflows.**

```
# Instead of crafting prompts from scratch...
echo "Long article here..." | fabric -p summarize

# Instead of manually summarizing videos...
fabric -y "https://youtube.com/watch?v=..." | fabric -p extract_wisdom

# Instead of writing generic commit messages...
git diff | fabric -p create_git_diff_commit

# Instead of struggling with complex tasks...
cat malware.py | fabric -p analyze_malware
```

**Your time is valuable.** Every minute spent crafting prompts is a minute stolen from actual work. Fabric patterns are:

- ✅ **Battle-tested** by thousands of users
- ✅ **Regularly updated** with improvements
- ✅ **Fully customizable** to your needs
- ✅ **Provider-agnostic**—use any AI backend

**The ROI is immediate:**
- Save 30+ minutes daily on prompt engineering
- Get consistent, high-quality outputs every time
- Access 150+ specialized workflows instantly
- Work with ANY AI provider you prefer

---

### Get Started

**Get started in 60 seconds:**

```bash
# 1. Install Fabric (Mac/Linux)
curl -fsSL https://raw.githubusercontent.com/danielmiessler/fabric/main/scripts/installer/install.sh | bash

# Windows PowerShell
iwr -useb https://raw.githubusercontent.com/danielmiessler/fabric/main/scripts/installer/install.ps1 | iex

# 2. Configure your AI provider
fabric --setup

# 3. Try it now
echo "Your content here" | fabric -p summarize
```

**Then load this skill into your AI assistant:**

```bash
npx skills add fabric
```

**You're now an AI power user.**

---

## Table of Contents

- [Why This Skill?](#why-this-skill)
- [Features](#features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Pattern Categories](#pattern-categories)
- [Usage Examples](#usage-examples)
- [Configuration](#configuration)
  - [Provider Setup](#provider-setup)
  - [Switch Between OpenAI & LM Studio](#2-switch-between-providers)
  - [Model Selection](#setting-your-llm-model)
- [Advanced Usage](#advanced-usage)
- [Contributing](#contributing)
- [License](#license)

---

## Why This Skill?

### For AI Coding Assistants

This skill transforms your AI assistant into a Fabric expert. When you load this skill:

1. **Instant expertise** — The assistant knows all 150+ patterns and when to use them
2. **Proper installation checks** — Automatically detects if Fabric is installed and guides setup
3. **Cross-platform support** — Works on Mac, Linux, and Windows
4. **Best practices** — Uses the most effective patterns for each task

### For End Users

- **Zero learning curve** — Just tell your AI assistant what you need
- **Consistent results** — Production-grade patterns, not hit-or-miss prompts
- **Future-proof** — Pattern library grows with community contributions

### AI Assistant Functions

This skill provides helper functions for AI assistants:

| Function | Description |
|----------|-------------|
| `show_fabric_capabilities()` | Display all 117 patterns in a formatted table with descriptions |
| `show_available_llms()` | List all available AI providers and models |
| `set_fabric_llm(provider, model)` | Set the LLM model to use for Fabric patterns |

---

## Features

### 🎯 Core Features

| Feature | Description |
|---------|-------------|
| **150+ Patterns** | Pre-built prompts for analysis, creation, extraction, and explanation |
| **35+ Providers** | Works with OpenAI, Anthropic, Gemini, Ollama, Azure, and more |
| **YouTube Integration** | Transcribe and analyze videos directly |
| **Code Analysis** | Explain code, analyze logs, detect malware |
| **Content Creation** | Summaries, emails, commits, art prompts, diagrams |
| **REST API** | Serve patterns as an API for other applications |
| **Streaming** | Real-time responses for better UX |
| **Custom Patterns** | Create and share your own patterns |

### 🌍 Cross-Platform

| Platform | Installation |
|----------|-------------|
| **macOS** | Homebrew, Go, or one-liner script |
| **Linux** | One-liner script or Go |
| **Windows** | PowerShell installer or Winget |
| **Docker** | Pre-built images available |
| **Web** | REST API server mode |

---

## Installation

### Prerequisites

1. **Fabric CLI** installed on your system
2. **AI provider** configured (API key)

### Install Fabric CLI

**macOS/Linux:**
```bash
# One-liner (recommended)
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

**Docker:**
```bash
docker run --rm -it kayvan/fabric:latest
```

### Install This Skill

```bash
npx skills add fabric
```

### Configure Fabric

```bash
# Run interactive setup
fabric --setup

# Verify installation
fabric --version
fabric --listpatterns
```

---

## Quick Start

### 1. Configure Provider

```bash
# Copy and edit credentials
cd scripts/
cp skill.env.example skill.env
nano skill.env

# Switch between providers
fabric-provider openai    # OpenAI cloud
fabric-provider lmstudio # Local LM Studio
```

### 2. Use Fabric

```bash
# Summarize text
echo "Your article text..." | fabric -p summarize

# Extract key insights
cat article.md | fabric -p extract_wisdom

# Analyze code
cat code.py | fabric -p explain_code

# Generate commit message
git diff | fabric -p create_git_diff_commit
```

### 3. YouTube Integration

```bash
# Get transcript
fabric -y "https://youtube.com/watch?v=..."

# With timestamps
fabric -y "URL" --transcript-with-timestamps

# Extract wisdom from video
fabric -y "URL" | fabric -p extract_wisdom
```

---

## Pattern Categories

### Complete Pattern Reference (117 Patterns)

**Analysis Patterns (23)**

| Pattern | Description |
|---------|-------------|
| `analyze_claims` | Analyze claims in text for accuracy |
| `analyze_comments` | Analyze comments (YouTube, social media) |
| `analyze_cfp_submission` | Analyze conference proposal submissions |
| `analyze_debate` | Analyze debate arguments |
| `analyze_email_headers` | Analyze email headers for security |
| `analyze_incident` | Analyze security incidents |
| `analyze_interviewer_techniques` | Analyze job interview techniques |
| `analyze_logs` | Analyze system/application logs |
| `analyze_malware` | Analyze malware samples |
| `analyze_paper` | Analyze academic papers |
| `analyze_patent` | Analyze patent documents |
| `analyze_personality` | Analyze personality from text |
| `analyze_presentation` | Analyze presentations |
| `analyze_product_feedback` | Analyze product feedback |
| `analyze_prose` | Analyze writing style |
| `analyze_prose_json` | Analyze prose with JSON output |
| `analyze_prose_pinker` | Analyze prose using Pinker's style |
| `analyze_sales_call` | Analyze sales call transcripts |
| `analyze_spiritual_text` | Analyze spiritual/religious texts |
| `analyze_tech_impact` | Analyze technology impact |
| `analyze_threat_report` | Analyze threat intelligence reports |
| `analyze_threat_report_trends` | Analyze threat report trends |
| `analyze_answers` | Analyze Q&A answers |

**Creation Patterns (42)**

| Pattern | Description |
|---------|-------------|
| `create_5_sentence_summary` | Create 5-sentence summary |
| `create_academic_paper` | Write academic papers |
| `create_ai_jobs_analysis` | Analyze AI job market |
| `create_aphorisms` | Create memorable sayings |
| `create_art_prompt` | Generate AI art prompts |
| `create_better_frame` | Reframe ideas positively |
| `create_coding_project` | Create coding project plans |
| `create_command` | Create shell commands |
| `create_cyber_summary` | Create cybersecurity summaries |
| `create_formal_email` | Write formal emails |
| `create_git_diff_commit` | Generate commit messages |
| `create_graph_from_input` | Create ASCII graphs |
| `create_hormozi_offer` | Create compelling offers |
| `create_idea_compass` | Analyze ideas from multiple angles |
| `create_investigation_visualization` | Create investigation diagrams |
| `create_keynote` | Create presentation outlines |
| `create_logo` | Create logo descriptions |
| `create_markmap_visualization` | Create markmap mind maps |
| `create_mermaid_visualization` | Create Mermaid diagrams |
| `create_mermaid_visualization_for_github` | GitHub-optimized Mermaid |
| `create_micro_summary` | Create micro summaries |
| `create_network_threat_landscape` | Create threat landscape docs |
| `create_npc` | Create NPC characters |
| `create_pattern` | Create new Fabric patterns |
| `create_quiz` | Create quizzes |
| `create_reading_plan` | Create reading plans |
| `create_recursive_outline` | Create recursive outlines |
| `create_report_finding` | Create report findings |
| `create_rpg_summary` | Create RPG summaries |
| `create_security_update` | Create security updates |
| `create_show_intro` | Create show introductions |
| `create_sigma_rules` | Create Sigma detection rules |
| `create_story_explanation` | Explain stories |
| `create_stride_threat_model` | Create STRIDE threat models |
| `create_summary` | Create summaries |
| `create_tags` | Create tags/categories |
| `create_threat_scenarios` | Create threat scenarios |
| `create_ttrc_graph` | Create threat tree graphs |
| `create_ttrc_narrative` | Create threat narratives |
| `create_upgrade_pack` | Create upgrade plans |
| `create_video_chapters` | Create video chapter markers |
| `create_visualization` | Create visualizations |

**Extraction Patterns (24)**

| Pattern | Description |
|---------|-------------|
| `extract_algorithm_update_recommendations` | Extract algorithm updates |
| `extract_article_wisdom` | Extract wisdom from articles |
| `extract_book_ideas` | Extract ideas from books |
| `extract_book_recommendations` | Extract book recommendations |
| `extract_business_ideas` | Extract business ideas |
| `extract_controversial_ideas` | Extract controversial ideas |
| `extract_extraordinary_claims` | Extract extraordinary claims |
| `extract_ideas` | Extract ideas |
| `extract_insights` | Extract insights |
| `extract_insights_dm` | Extract deep insights (Daniel Miessler) |
| `extract_instructions` | Extract instructions |
| `extract_jokes` | Extract jokes |
| `extract_main_idea` | Extract main ideas |
| `extract_patterns` | Extract patterns |
| `extract_poc` | Extract proof of concepts |
| `extract_predictions` | Extract predictions |
| `extract_primary_problem` | Extract primary problems |
| `extract_questions` | Extract questions |
| `extract_recommendations` | Extract recommendations |
| `extract_references` | Extract references |
| `extract_wisdom` | Extract wisdom |
| `extract_verbs` | Extract action verbs |

**Explanation Patterns (5)**

| Pattern | Description |
|---------|-------------|
| `explain_code` | Explain code |
| `explain_docs` | Explain documentation |
| `explain_math` | Explain mathematics |
| `explain_project` | Explain projects |
| `explain_terms` | Explain terminology |

**Writing Patterns (10)**

| Pattern | Description |
|---------|-------------|
| `agility_story` | Write agility stories |
| `answer_interview_question` | Answer interview questions |
| `capture_thinkers_work` | Capture intellectual work |
| `check_agreement` | Check text agreements |
| `clean_text` | Clean text formatting |
| `coding_master` | Master-level coding assistance |
| `compare_and_contrast` | Compare and contrast items |
| `export_data_as_csv` | Export data as CSV |
| `write_tiktok_script` | Write TikTok scripts |
| `write_tweet` | Write tweets |

**Special Patterns (3)**

| Pattern | Description |
|---------|-------------|
| `ai` | General AI assistant |
| `create_conceptmap` | Create HTML concept maps |
| `wellness` | Wellness/psychology analysis |

---

### Quick Reference

| Category | Count | Examples |
|----------|-------|----------|
| Analysis | 23 | analyze_logs, analyze_malware, analyze_paper |
| Creation | 42 | create_summary, create_git_diff_commit, create_art_prompt |
| Extraction | 24 | extract_wisdom, extract_insights, extract_questions |
| Explanation | 5 | explain_code, explain_docs, explain_math |
| Writing | 10 | clean_text, create_formal_email, compare_and_contrast |
| Special | 3 | ai, create_conceptmap, wellness |

### ✍️ Creation Patterns

Generate high-quality content:

| Pattern | Use Case |
|---------|----------|
| `create_summary` | Concise summaries |
| `create_5_sentence_summary` | Ultra-brief summaries |
| `create_micro_summary` | Micro summaries |
| `create_art_prompt` | AI art prompt generation |
| `create_command` | Shell command generation |
| `create_formal_email` | Professional emails |
| `create_git_diff_commit` | Commit messages |
| `create_mermaid_visualization` | Mermaid diagrams |
| `create_conceptmap` | HTML concept maps |
| `create_keynote` | Presentation outlines |
| `create_quiz` | Quiz generation |
| `create_logo` | Logo concept descriptions |

### 🎯 Extraction Patterns

Pull specific information from content:

| Pattern | Use Case |
|---------|----------|
| `extract_wisdom` | Key insights and takeaways |
| `extract_insights` | Deep insights |
| `extract_ideas` | Creative ideas |
| `extract_questions` | Generate questions |
| `extract_recommendations` | Actionable recommendations |
| `extract_main_idea` | Core message extraction |
| `extract_patterns` | Identify patterns |
| `extract_predictions` | Future predictions |
| `extract_references` | Citations and sources |
| `extract_jokes` | Humor extraction |

### 📚 Explanation Patterns

Understand complex content:

| Pattern | Use Case |
|---------|----------|
| `explain_code` | Code explanation |
| `explain_docs` | Documentation explanation |
| `explain_math` | Mathematical concepts |
| `explain_project` | Project overview |
| `explain_terms` | Terminology definitions |

---

## Usage Examples

### Example 1: Blog Post Summary

```bash
# Scrape and summarize a blog post
fabric --scrape_url "https://example.com/blog/post" | fabric -p summarize
```

### Example 2: Video Notes

```bash
# Get structured notes from a YouTube video
fabric -y "https://youtube.com/watch?v=..." | fabric -p extract_wisdom | fabric -p create_summary
```

### Example 3: Code Review

```bash
# Explain unfamiliar code
cat complex_module.py | fabric -p explain_code

# Check for issues
cat legacy_code.py | fabric -p analyze_prose
```

### Example 4: Security Analysis

```bash
# Analyze a threat report
cat threat_report.pdf | fabric -p analyze_threat_report

# Create mitigation recommendations
fabric -p create_stride_threat_model
```

### Example 5: Academic Research

```bash
# Analyze a research paper
cat paper.pdf | fabric -p analyze_paper

# Extract key findings
fabric -p extract_main_idea

# Generate discussion questions
fabric -p extract_questions
```

### Example 6: Content Creation

```bash
# Generate social media posts
cat blog_post.md | fabric -p extract_ideas | fabric -p create_tags

# Create variations
echo "Your content" | fabric -p create_better_frame
```

### Example 7: Meeting Notes

```bash
# Summarize meeting transcript
cat meeting.txt | fabric -p create_summary

# Extract action items
fabric -p extract_recommendations
```

---

## Configuration

### Provider Setup

This skill supports **dual-provider mode**: switch between OpenAI (cloud) and LM Studio (local) with one command.

#### 1. Configure Credentials

Copy the example file and add your credentials:

```bash
cd scripts/
cp skill.env.example skill.env
nano skill.env
```

Add your API keys:

```bash
# OpenAI Configuration
OPENAI_API_KEY=sk-your-openai-api-key-here
OPENAI_URL=https://api.openai.com/v1

# LM Studio / Local LLM Configuration
LMSTUDIO_URL=http://192.168.1.141:11435/v1
LMSTUDIO_KEY=ignored
```

> **Note:** `skill.env` is gitignored and never published. Only `skill.env.example` (with fake values) is shared.

#### 2. Switch Between Providers

```bash
# Switch to OpenAI (cloud) - uses GPT-4o, GPT-5, o3, etc.
fabric-provider openai

# Switch to LM Studio (local) - uses qwen3.5, gpt-oss, etc.
fabric-provider lmstudio

# Check current configuration
fabric-provider status

# Run setup wizard (interactive)
fabric-provider setup
```

#### 3. Provider Comparison

| Provider    | Endpoint                    | Best For                   | Cost        |
| ----------- | --------------------------- | -------------------------- | ----------- |
| **OpenAI**     | api.openai.com              | Cloud models, latest GPT-5 | Pay-per-use |
| **LM Studio**  | 192.168.1.141:11435         | Local, free, private       | Free        |

#### 4. Using Fabric After Switching

Once the provider is set, use Fabric normally:

```bash
# Works with current provider (OpenAI or LM Studio)
echo "Your content" | fabric -p summarize
echo "Your content" | fabric -p extract_insights

# YouTube + extract insights
fabric -y "https://youtube.com/watch?v=..." | fabric -p extract_insights
```

Or specify inline:

```bash
# Force specific provider/model
fabric -p ai -V OpenAI -m gpt-4o
fabric -p ai -V "LM Studio" -m qwen3.5-35b-a3b@4bit
```

### Setting Your LLM Model

**List available models:**
```bash
fabric --listvendors    # Show all providers
fabric --listmodels     # Show all models
```

**Use inline (per-command):**
```bash
fabric -p summarize -V anthropic -m claude-3-5-sonnet
fabric -p create_git_diff_commit -V openai -m gpt-4o
```

### Custom Patterns

Create your own patterns in `~/.config/fabric/patterns/`:

```
~/.config/fabric/patterns/my_pattern/
├── system.md    # System prompt
├── user.md      # User template
└── meta.md      # Metadata
```

### Multiple Providers

```bash
# Use specific provider
fabric -p summarize -V anthropic -m claude-3-5-sonnet

# List all providers
fabric --listvendors
```

---

## Advanced Usage

### REST API Server

```bash
# Start server
fabric --serve

# With Ollama compatibility
fabric --serve --serveOllama

# Custom port and auth
fabric --serve --address :8080 --api-key your-secret-key
```

### Web Search Integration

```bash
# Enable web search (Anthropic, OpenAI, Gemini)
echo "Latest AI news" | fabric -p ai --search

# With location
fabric -p ai --search --search-location "America/New_York"
```

### Image Generation

```bash
# Generate with Fabric patterns
fabric -p create_art_prompt --image-file output.png

# Custom dimensions
fabric -p create_art_prompt --image-file img.png --image-size 1536x1024 --image-quality high
```

### Speech to Text

```bash
# Transcribe audio/video
fabric --transcribe-file podcast.mp3

# With specific model
fabric --transcribe-file video.mp4 --transcribe-model whisper-1
```

### Custom Variables

```bash
# Pass custom parameters
echo "Content" | fabric -p extract_ideas -v=#max:20

# Multiple variables
fabric -p create_command -v=#role:devops -v=#task:"restart nginx"
```

---

## Pattern Philosophy

Fabric patterns are designed with specific principles:

1. **Markdown-based** — Maximum readability for humans and AI
2. **System-focused** — Instructions primarily in system prompts
3. **Clear structure** — Explicit step-by-step guidance
4. **Battle-tested** — Refined through thousands of use cases

This ensures consistent, high-quality outputs regardless of the content or provider.

---

## Supported AI Providers

### Native Integrations
- OpenAI
- Anthropic (Claude)
- Google Gemini
- Ollama (local models)
- Azure OpenAI
- AWS Bedrock
- Vertex AI

### OpenAI-Compatible
- Abacus
- AIML
- Cerebras
- DeepSeek
- DigitalOcean
- GitHub Models
- GrokAI
- Groq
- Langdock
- LiteLLM
- LM Studio
- MiniMax
- Mistral
- Novita AI
- OpenRouter
- Perplexity
- SiliconCloud
- Together
- Venice AI
- Z AI

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `fabric: command not found` | Add Go bin to PATH: `export PATH=$PATH:$(go env GOPATH)/bin` |
| API key error | Run `fabric --setup` to configure |
| Pattern not found | Run `fabric --updatepatterns` to sync |
| Model not available | Check `fabric --listvendors` for supported providers |

---

## Contributing

Contributions are welcome! Please see the [Fabric repository](https://github.com/danielmiessler/Fabric) for:

- Pattern submissions
- Bug reports
- Feature requests
- Documentation improvements

---

## Resources

- [Fabric GitHub](https://github.com/danielmiessler/Fabric)
- [DeepWiki Documentation](https://deepwiki.com/danielmiessler/Fabric)
- [Pattern Library](./references/patterns.md)
- [Changelog](https://github.com/danielmiessler/Fabric/blob/main/CHANGELOG.md)

---

## License

MIT License - See [LICENSE](LICENSE) for details.

---

<div align="center">

**Built with ❤️ by the AI community**

</div>
