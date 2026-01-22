# AI Agents & Workflows - The Practical Guide

A comprehensive course project for learning AI agents and LLM-based workflows using OpenAI APIs and modern Python practices.

## Project Structure

```
ai-agents-workflows/
├── main.py                          # Entry point - basic X post generation
├── pyproject.toml                   # Project metadata and dependencies
├── .env                             # Environment variables (API keys)
├── .python-version                  # Python version specification
├── .gitignore                       # Git exclusions
├── uv.lock                          # Dependency lock file
├── README.MD                        # Course documentation
├── slides/                          # Course presentation materials
└── code/
    ├── 02-ai-workflows/             # 13 progressive workflow examples
    ├── 03-ai-agents/                # 6 agent examples with tool use
    └── 04-third-party/              # CrewAI framework examples
```

---

## AI Workflows (`code/02-ai-workflows/`)

Progressive examples demonstrating AI workflow patterns from basic to advanced.

### 01-first-workflow-openai-api

**Purpose:** Basic X post generator using raw HTTP requests to OpenAI API

| File | Functions | Description |
|------|-----------|-------------|
| `main.py` | - | Direct API calls with `requests`, error handling, environment variables |

---

### 02-using-openai-sdk

**Purpose:** Refactored version using OpenAI Python SDK

| File | Functions | Description |
|------|-----------|-------------|
| `main.py` | - | Cleaner SDK usage, improved prompt engineering |

---

### 03-few-shot-prompting

**Purpose:** X post generation with few-shot examples

| File | Functions | Description |
|------|-----------|-------------|
| `main.py` | `generate_x_post()` | Constructs formatted examples in prompts |
| `posts.json` | - | JSON file containing example posts for in-context learning |

---

### 04-multi-step-multi-model

**Purpose:** Website content extraction, summarization, and X post generation pipeline

| File | Functions | Description |
|------|-----------|-------------|
| `main.py` | `get_website_html()` | Fetches website content via HTTP |
| | `extract_core_website_content()` | Extracts main content from HTML |
| | `summarize_content()` | Creates concise summary using gpt-4o-mini |
| | `generate_x_post()` | Generates final post from summary |

---

### 05-using-local-open-models

**Purpose:** Same workflow as 04 but designed for local open-source models (Ollama/similar)

| File | Functions | Description |
|------|-----------|-------------|
| `main.py` | Same as 04 | Alternative to paid APIs using local models |

---

### 06-structured-outputs

**Purpose:** Invoice PDF extraction with structured JSON output

| File | Functions | Description |
|------|-----------|-------------|
| `main.py` | `setup_database()` | Creates SQLite database for invoices |
| | `extract_invoice_details()` | Uses JSON schema for structured output |
| | `insert_invoice_data()` | Stores extracted data in database |
| `*.pdf` | - | Sample invoice PDF files |

---

### 07-structured-outputs-pydantic

**Purpose:** Invoice extraction using Pydantic models for type safety

| File | Functions/Classes | Description |
|------|-------------------|-------------|
| `main.py` | `Vendor` (class) | Pydantic model for vendor data |
| | `Customer` (class) | Pydantic model for customer data |
| | `Invoice` (class) | Pydantic model for invoice data |
| | Uses `client.responses.parse()` | Type-safe parsing with Pydantic |

---

### 08-another-example-content-generation

**Purpose:** Blog post generation from outline

| File | Functions | Description |
|------|-----------|-------------|
| `main.py` | `load_file()` | Reads files from disk |
| | `save_file()` | Writes files to disk |
| | `generate_article_draft()` | Generates markdown blog post |
| `examples/` | - | Example blog posts for few-shot learning |
| `outline.md` | - | Input outline for generation |

---

### 09-generating-images

**Purpose:** Blog post generation with AI-generated thumbnail images

| File | Functions | Description |
|------|-----------|-------------|
| `main.py` | `load_file()`, `save_file()` | File I/O operations |
| | `generate_article_draft()` | Blog post generation |
| | `generate_thumbnail()` | Uses gpt-image-1 model for image generation |

---

### 10-control-flow

**Purpose:** Complete content generation pipeline with quality evaluation loops

| File | Functions/Classes | Description |
|------|-------------------|-------------|
| `main.py` | `Evaluation` (Pydantic) | Structured evaluation result |
| | `evaluate_article_draft()` | AI-based quality evaluation |
| | `generate_linkedin_post()` | LinkedIn content from article |
| | While loop with max 3 iterations | Agentic improvement cycles |
| | `ThreadPoolExecutor` | Parallel execution (thumbnail + LinkedIn) |

---

### 11-human-in-the-loop

**Purpose:** Same as 10 with human feedback integration

| File | Functions | Description |
|------|-----------|-------------|
| `main.py` | Same as 10 + `input()` | User can accept/reject/provide feedback |

---

### 12-external-service-slack

**Purpose:** Complete pipeline with Slack notification integration

| File | Functions | Description |
|------|-----------|-------------|
| `main.py` | Same as 11 | All previous functionality |
| | `send_slack_notification()` | Posts to Slack channel via API |

---

### 13-final-version

**Purpose:** Production-ready version with refactored helper functions

| File | Functions | Description |
|------|-----------|-------------|
| `main.py` | `load_and_format_example_posts()` | Reusable utility for DRY code |
| | All previous functions | Organized and production-ready |

---

### starting-project

**Purpose:** Template project structure for learners to start from scratch

---

## AI Agents (`code/03-ai-agents/`)

Progressive examples demonstrating AI agent patterns with tool use and autonomous behavior.

### 01-tool-use-from-scratch

**Purpose:** Temperature lookup agent with manual tool calling

| File | Functions | Description |
|------|-----------|-------------|
| `main.py` | `get_temperature()` | Mock temperature service |
| | Manual parsing | Detects tool requests in output, executes, feeds back |

---

### 02-openai-functions

**Purpose:** Temperature lookup using OpenAI structured function calling

| File | Functions/Structures | Description |
|------|----------------------|-------------|
| `main.py` | `tools` array | Formal function definitions with parameters |
| | `available_functions` dict | Maps function names to implementations |
| | `execute_tool_call()` | Parses and executes tool calls |

---

### 03-multi-tool-versatile

**Purpose:** Customer service agent with 5 tools

| File | Functions/Tools | Description |
|------|-----------------|-------------|
| `main.py` | `verify_customer()` | Verifies customer identity |
| | `get_orders()` | Retrieves customer orders |
| | `check_refund_eligibility()` | Checks if order can be refunded |
| | `issue_refund()` | Processes refund |
| | `submit_feedback()` | Records customer feedback |
| `database.py` | `setup_database()` | Creates SQLite with sample data |
| | Customer & Order tables | Relational data storage |

---

### 04-using-classes

**Purpose:** Refactored agent using OOP patterns

| File | Classes | Description |
|------|---------|-------------|
| `main.py` | `Tool` | Base tool class |
| | `VerifyCustomerTool` | Tool implementation |
| | `GetOrdersTool` | Tool implementation |
| | `CheckRefundEligibilityTool` | Tool implementation |
| | `IssueRefundTool` | Tool implementation |
| | `SubmitFeedbackTool` | Tool implementation |
| | `Agent` | Base agent class with tool registration |
| | `CustomerServiceAgent` | Specialized agent extending Agent |

---

### 05-multi-agent

**Purpose:** Three-agent research workflow with coordination

| File | Classes/Functions | Description |
|------|-------------------|-------------|
| `main.py` | `ResearchPlannerAgent` | Plans research from user input |
| | `WebSearchAgent` | Uses Brave Search API |
| | `SummaryReportAgent` | Creates markdown report |
| | `SearchConfig` (Pydantic) | Structured search configuration |
| `database.py` | `setup_database()` | Stores research plans |
| | `save_research_plan()` | Persists plan to database |
| | `get_research_plan()` | Retrieves plan from database |

---

### starting-project

**Purpose:** Template for learners to build their own agents

---

## Third-Party Frameworks (`code/04-third-party/`)

### research-crew-finished/

**Purpose:** Complete CrewAI project for research workflows

| File | Components | Description |
|------|------------|-------------|
| `src/research_crew/crew.py` | `@agent` decorators | Defines Researcher & ReportingAnalyst agents |
| | `@task` decorators | Defines research_task & reporting_task |
| | `@crew` decorator | Defines crew with sequential process |
| | `BraveSearchTool` | Web search capability |
| `src/research_crew/main.py` | `run()` | Entry point to execute crew |
| `pyproject.toml` | - | CrewAI dependencies |

### research_crew-start/

**Purpose:** Template/starting point for CrewAI projects

| File | Description |
|------|-------------|
| `src/research_crew/config/agents.yaml` | Agent configurations |
| `src/research_crew/config/tasks.yaml` | Task configurations |
| `src/research_crew/crew.py` | Crew definition template |

---

## Key Patterns & Concepts

### Workflow Patterns

| Pattern | Description | Examples |
|---------|-------------|----------|
| **Simple** | Input → LLM → Output | 01, 02, 03 |
| **Multi-step** | Extract → Summarize → Generate | 04, 05 |
| **Evaluation Loop** | Generate → Evaluate → Improve | 10 |
| **Human-in-the-loop** | Generate → Human Review → Update | 11 |
| **Multi-agent** | Specialized agents coordination | 05 (agents) |

### Tool/Function Patterns

| Pattern | Description | Examples |
|---------|-------------|----------|
| **Manual tool calling** | Parse output for tool requests | Agents 01 |
| **Function calling** | Structured schemas, automatic parsing | Agents 02 |
| **Class-based tools** | OOP with Tool base class | Agents 04 |
| **Multi-tool coordination** | Registry pattern | Agents 03-05 |

### Data Handling

| Type | Usage | Examples |
|------|-------|----------|
| **Unstructured** | Plain text, Markdown | Blog posts, reports |
| **Structured** | JSON, Pydantic, JSON Schema | Invoices, configs |
| **Binary** | Base64 encoded images | Thumbnails |
| **Relational** | SQLite with foreign keys | Customers, orders |

---

## Dependencies

```toml
# Common across projects
openai          # OpenAI SDK for API calls
python-dotenv   # Environment variable management
requests        # HTTP library for external APIs
pydantic        # Data validation with type hints
pypdf           # PDF reading

# For third-party examples
crewai          # Multi-agent framework
crewai-tools    # Tools for CrewAI
```

---

## Setup & Configuration

### Environment Variables

Create a `.env` file with:

```env
OPENAI_API_KEY=your_openai_api_key
SLACK_ACCESS_TOKEN=your_slack_token      # For workflow 12
BRAVE_API_KEY=your_brave_api_key         # For agent 05
```

### Running Examples

Each example is independently runnable:

```bash
# Navigate to example directory
cd code/02-ai-workflows/04-multi-step-multi-model

# Install dependencies with uv
uv sync

# Run the example
uv run main.py
```

---

## Learning Progression

1. **Basics** (Workflows 01-02): Direct API usage and SDK adoption
2. **Prompt Engineering** (03-04): Few-shot learning, multi-step workflows
3. **Advanced Features** (05-07): Local models, structured outputs, Pydantic
4. **Complex Workflows** (08-13): Content generation, images, human feedback, external services
5. **Tool Use** (Agents 01-02): Basic and structured function calling
6. **Autonomous Agents** (Agents 03-05): Multi-tool, OOP design, multi-agent systems
7. **Frameworks** (04-third-party): Using CrewAI for production systems

---

## License

This project is for educational purposes as part of the Udemy course "AI Agents & Workflows - The Practical Guide".
