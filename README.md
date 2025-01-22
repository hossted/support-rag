# support-rag
AI assisted RAG support framework powered by CrewAI for intelligent support ticket handling

## Overview
A modular framework implementing Retrieval-Augmented Generation (RAG) to enhance AI-powered support systems. The system uses CrewAI to orchestrate AI agents that analyze support tickets, predict resolution patterns, and augment support staff capabilities across multiple platforms.

## Features
- Document ingestion and processing
- Vector storage integration
- Semantic search capabilities
- Context-aware AI responses
- Support ticket classification
- Multi-platform support integration:
  - Freshdesk
  - ServiceNow
  - Zendesk
- Knowledge base connectors:
  - Wiki.js
  - Confluence
  - Notion
  - ServiceNow Knowledge
- AI-powered ticket analysis and resolution prediction
- Automated support agent assistance
- Knowledge article recommendation

## Architecture
### Core Components
- Support Platform Adapters: Modular integrations for different ticketing systems
- Knowledge Base Connectors: Pluggable interfaces for various knowledge sources
- CrewAI Agents:
  - Ticket Analyzer Agent: Processes and classifies incoming tickets
  - Resolution Predictor Agent: Suggests solutions based on historical patterns
  - Knowledge Navigator Agent: Identifies relevant documentation
  - Support Assistant Agent: Interfaces with support staff

## Getting Started
Documentation and setup instructions coming soon.

### Prerequisites
- Python 3.8+
- CrewAI
- Vector database (e.g., Pinecone, Weaviate)
- API access to supported platforms

## Development
### Adding New Platform Support
The framework provides abstract base classes for implementing new platform integrations:
- `BaseSupportAdapter`: For ticketing system integration
- `BaseKnowledgeConnector`: For knowledge base integration

## License
[License details to be added]
