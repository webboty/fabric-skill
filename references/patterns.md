# Fabric Patterns Reference

Complete list of Fabric patterns organized by category.

## Categories

### Analysis Patterns

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

### Creation Patterns

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

### Extraction Patterns

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

### Explanation Patterns

| Pattern | Description |
|---------|-------------|
| `explain_code` | Explain code |
| `explain_docs` | Explain documentation |
| `explain_math` | Explain mathematics |
| `explain_project` | Explain projects |
| `explain_terms` | Explain terminology |

### Writing Patterns

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

### Special Patterns

| Pattern | Description |
|---------|-------------|
| `ai` | General AI assistant |
| `create_conceptmap` | Create HTML concept maps |
| `wellness` | Wellness/psychology analysis |

## Usage Examples

```bash
# Summarize text from clipboard
echo "Long article text..." | fabric -p summarize

# Extract wisdom from content
echo "Article content..." | fabric -p extract_wisdom

# Analyze code
cat code.py | fabric -p explain_code

# Create a commit message
git diff | fabric -p create_git_diff_commit

# Transcribe YouTube video
fabric -y "https://youtube.com/watch?v=..."

# Use specific pattern with streaming
echo "Input" | fabric -p summarize --stream

# Use with custom context
fabric -p summarize -C my_context

# Use specific model
fabric -p summarize -m claude-opus-4

# Set custom variables
echo "Input" | fabric -p create_command -v=#task:"deploy docker"

# Dry run (preview without API call)
echo "Input" | fabric -p summarize --dry-run

# List patterns
fabric --listpatterns

# Update patterns from upstream
fabric --updatepatterns
```

## Pattern Structure

Each pattern typically contains:
- `system.md` - System prompt/instructions
- `user.md` - User prompt template (optional)
- `meta.md` - Pattern metadata (optional)

Patterns are stored in `~/.config/fabric/patterns/` by default.
