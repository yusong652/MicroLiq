---
title: "Appendix 3: AI-Assisted Workflow for DEM Simulations"
tags: [thesis, appendix-3, LLM, agent, DEM, numerical-simulation, aiNagisa]
aliases: [Appendix 3, aiNagisa, AI-Assisted DEM]
---

# Appendix 3 AI-Assisted Workflow for DEM Simulations

## A3.1 Introduction

### A3.1.1 Rise of LLM-based agents

<!-- TODO: Web search for recent developments -->

The emergence of large language models (LLMs) such as GPT, Claude, and Gemini has fundamentally transformed human-computer interaction. Beyond simple question-answering, these models have evolved into autonomous agents capable of executing complex, multi-step tasks. This paradigm shift—from passive response to active action—has given rise to a new category of AI systems known as LLM-based agents.

Several domains have witnessed remarkable success with agent-based approaches:

**Customer service agents.** ...

**Coding assistants.** Tools such as GitHub Copilot, Cursor, and Claude Code have demonstrated that LLMs can effectively assist software development. These agents not only generate code but also read existing codebases, execute commands, and iteratively refine their outputs based on feedback. ...

**Data analysis agents.** ...

### A3.1.2 Gap: Scientific computing and numerical simulation

Despite the proliferation of LLM agents across various domains, their application in scientific computing and numerical simulation remains notably limited. This gap can be attributed to several unique challenges:

**Domain-specific syntax.** Numerical simulation software such as PFC, FLAC, and ABAQUS employs specialized command languages with strict syntax requirements. Unlike general-purpose programming languages, these domain-specific syntaxes are less represented in LLM training data, leading to potential hallucination and syntax errors.

**Computational time scales.** While typical coding tasks complete within seconds, numerical simulations may run for hours or even days. This temporal mismatch poses challenges for agent architectures designed around rapid request-response cycles.

**Reliability requirements.** In scientific computing, incorrect parameters or commands can lead to simulation divergence, non-physical results, or wasted computational resources. The tolerance for errors is significantly lower than in many other agent applications.

### A3.1.3 Motivation: Numerical simulation agent

The success of coding assistants provides a compelling template for numerical simulation agents. If LLMs can effectively assist software development—reading documentation, writing code, executing tests, and iterating based on results—the same paradigm could potentially accelerate numerical simulation workflows.

This appendix presents aiNagisa, an AI assistant designed specifically for DEM simulations using ITASCA PFC. The system addresses the challenges outlined above through:

1. **Documentation-driven code generation** that ensures command syntax reliability
2. **Script-based workflows** that maintain reproducibility and enable cross-session learning
3. **Background task management** that accommodates long-running simulations

The following sections detail these approaches and demonstrate their application to the research workflows presented in this thesis.

## A3.2 Challenges in LLM-assisted numerical simulations

### A3.2.1 Command syntax reliability

When LLMs generate code for numerical simulation software, syntax errors present a significant challenge. Unlike compilation errors in general-purpose languages, incorrect commands in simulation software may:

- Fail silently and produce unexpected behavior
- Cause simulation divergence after hours of computation
- Generate non-physical results that require expert inspection to identify

For example, in PFC, the command for generating particles requires specific keyword combinations and parameter ranges. An LLM unfamiliar with these constraints may generate syntactically plausible but semantically incorrect commands.

### A3.2.2 Multi-stage simulation workflows

DEM simulations typically involve multiple sequential stages:

1. **Geometry creation**: Defining boundaries and initial particle configurations
2. **Initial equilibrium**: Allowing particles to settle under gravity
3. **Consolidation**: Applying confining stresses to achieve target stress states
4. **Loading**: Executing the primary loading path (shear, compression, etc.)
5. **Post-processing**: Extracting results and computing derived quantities

Each stage depends on the successful completion of previous stages, and parameters must remain consistent across the workflow. Managing this complexity requires careful coordination that goes beyond single-command generation.

### A3.2.3 Long-running simulations and progress monitoring

Large-scale DEM simulations may require hours to days of computation time. During this period, researchers need to:

- Monitor simulation progress without blocking other work
- Detect potential issues early (e.g., excessive unbalanced forces)
- Access intermediate results for preliminary analysis

Traditional command-line interfaces provide limited support for these requirements, particularly when integrated with conversational AI systems designed for rapid interaction.

## A3.3 Documentation-driven approach

### A3.3.1 Query-before-generate paradigm

To address the reliability challenge, aiNagisa implements a documentation-driven approach where the LLM queries relevant documentation before generating any simulation commands. This paradigm inverts the typical generative process:

**Traditional approach:**
```
User request → LLM generates code (from memory) → Execute → Handle errors
```

**Documentation-driven approach:**
```
User request → Query documentation → LLM generates code (informed) → Execute
```

By retrieving authoritative documentation at generation time, the system ensures that:

1. Command syntax follows official specifications
2. Parameter constraints are respected
3. Available options are accurately represented

This approach trades a small amount of latency for significantly improved reliability—a worthwhile exchange in scientific computing contexts where debugging incorrect simulations is costly.

### A3.3.2 Structured documentation system

The documentation system organizes PFC commands and Python APIs into a searchable knowledge base:

```
documentation/
├── command_docs/
│   └── commands/
│       ├── ball/          # Particle generation and manipulation
│       ├── contact/       # Contact model properties
│       ├── model/         # Simulation control
│       └── wall/          # Boundary definitions
└── python_sdk_docs/
    └── modules/           # Python API documentation
```

Each documentation entry includes:

- **Syntax specification**: Exact command format and required keywords
- **Parameter descriptions**: Valid ranges and default values
- **Usage examples**: Concrete applications demonstrating correct usage
- **Python alternatives**: SDK methods when available

A BM25-based search engine enables efficient retrieval, with query times under 15 milliseconds for the complete documentation corpus.

### A3.3.3 Test-first workflow

Following practices from software engineering, aiNagisa implements a test-first approach to simulation development:

1. **Write test script**: Generate a minimal script with reduced particle count (e.g., 10 particles instead of 10,000)
2. **Execute and validate**: Run the test script to verify syntax correctness
3. **Scale to production**: Upon successful validation, generate the full-scale simulation script

This workflow catches errors early when computational cost is low, preventing wasted hours on simulations with fundamental syntax issues.

## A3.4 Script as reproducible research context

### A3.4.1 From interactive commands to versioned scripts

Traditional numerical simulation workflows often rely on interactive command entry or GUI operations. While convenient for exploration, these approaches create challenges for:

- **Reproducibility**: Recreating exact simulation conditions
- **Documentation**: Recording methodological decisions
- **Collaboration**: Sharing workflows with colleagues

aiNagisa addresses these issues by generating Python scripts for all simulation operations. Each script represents a complete, executable record of the simulation setup:

```python
# Example: K0 consolidation setup (generated by aiNagisa)
import itasca as it

# Create specimen geometry
it.command("model new")
it.command("model domain extent -0.1 0.1 -0.1 0.1 -0.2 0.2")

# Generate particles
it.command("ball generate radius 0.002 0.003 porosity 0.4")

# Set contact model
it.command("contact cmat default model linear property kn 1e8 ks 1e8")

# Apply K0 consolidation
# σv = 100 kPa, K0 = 0.5 → σh = 50 kPa
it.command("wall servo activate true")
# ... (continued)
```

### A3.4.2 Building simulation knowledge base

As scripts accumulate, they form a knowledge base that the LLM can reference for future tasks. This "script as context" philosophy enables:

**Cross-session learning**: Successful simulation patterns persist beyond individual conversations

**Template discovery**: Common workflows (e.g., undrained shear setup) become reusable templates

**Error prevention**: Previously encountered issues inform future code generation

The task management system maintains metadata for each script execution:

- Execution status (running, completed, failed)
- Output logs and error messages
- Elapsed time and resource usage

This historical context transforms isolated simulations into a connected research narrative.

### A3.4.3 Reproducibility in computational research

The script-based approach directly supports reproducibility standards increasingly required in computational geomechanics research. Each script serves as:

1. **Method documentation**: Complete specification of simulation parameters
2. **Version-controlled artifact**: Trackable through git history
3. **Executable specification**: Can be re-run to verify results

When combined with saved model states, researchers can precisely recreate any point in their simulation workflow—essential for responding to reviewer comments or extending previous analyses.

## A3.5 Application to thesis research

### A3.5.1 Integration with HCA simulation workflow

The hollow cylinder apparatus (HCA) simulations presented in Chapter 4 involve complex stress path control requiring precise command sequences. aiNagisa facilitates this workflow by:

**Automating servo mechanism setup**: Generating the combined-servo-mechanism scripts for undrained conditions with correct feedback parameters

**Managing multi-stage loading**: Coordinating consolidation, saturation, and shear phases while maintaining state consistency

**Extracting microscopic parameters**: Automatically generating post-processing scripts to compute coordination number ($Z_m$), fabric tensor ($F_c$), and void ratio ($e$)

### A3.5.2 Fabric evolution analysis automation

The fabric evolution analyses in Chapters 3 and 4 require extracting contact orientations and computing directional distributions. aiNagisa assists by:

- Querying documentation for contact property access methods
- Generating scripts to export contact data at specified intervals
- Creating visualization scripts for fabric tensor evolution

This automation reduces the time between simulation completion and scientific insight.

### A3.5.3 Accelerating research iteration

By lowering the barrier to simulation setup, aiNagisa enables rapid exploration of parameter spaces. Researchers can:

- Quickly test alternative contact models or boundary conditions
- Generate parameter sweep scripts for sensitivity analyses
- Iterate on simulation designs based on preliminary results

The time savings compound across a research project, potentially enabling investigations that would otherwise be impractical.

## A3.6 Discussion

### A3.6.1 Comparison with existing approaches

<!-- TODO: Compare with traditional scripting, GUI macros, other automation tools -->

The documentation-driven approach differs from existing simulation automation methods in several key aspects:

| Approach | Syntax Reliability | Flexibility | Learning Curve |
|----------|-------------------|-------------|----------------|
| Manual scripting | High (if expert) | High | Steep |
| GUI macros | Medium | Low | Moderate |
| Template libraries | High | Low | Low |
| aiNagisa | High | High | Low |

### A3.6.2 Limitations and future directions

**Current limitations:**

- Documentation coverage depends on manual curation
- Complex multi-physics simulations may exceed current capabilities
- Validation still requires domain expertise

**Future directions:**

- Extension to other simulation platforms (FLAC, ABAQUS, OpenFOAM)
- Integration with optimization algorithms for automated parameter calibration
- Multi-agent collaboration for complex simulation campaigns

## A3.7 Conclusions

This appendix presented aiNagisa, an AI assistant for DEM simulations that addresses key challenges in applying LLM agents to numerical simulation workflows. The documentation-driven approach ensures command syntax reliability, while the script-based workflow maintains reproducibility and enables cross-session learning.

As LLM capabilities continue to advance, such domain-specific agents may become increasingly valuable tools for computational research, reducing the technical barrier to sophisticated numerical simulations while maintaining the rigor required for scientific applications.
