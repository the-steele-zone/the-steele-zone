# The Steele Zone | AI-Powered Content Automation & Web3 Development Hub

## 🚀 Overview

Welcome to The Steele Zone - a comprehensive automation and development repository featuring AI-powered workflows, blockchain integrations, and content management systems. This project showcases advanced n8n workflows, Supabase integrations, Solana/Helius RPC connections, and automated social media management.

## 🛠️ Tech Stack

- **Automation**: n8n Cloud Workflows
- **Database**: Supabase (PostgreSQL)
- **Blockchain**: Solana via Helius RPC
- **AI**: Google Gemini, Claude AI (MCP), OpenAI
- **Infrastructure**: Docker, GitHub Actions
- **Languages**: Python, JavaScript, SQL

## 📁 Repository Structure

```
the-steele-zone/
├── .github/workflows/      # GitHub Actions automation
├── ai-assistants/          # AI assistant configurations
├── claude-desktop-config/  # MCP server configurations
├── content-automation/     # Social media automation scripts
├── docs/                   # Documentation
├── n8n-config/            # N8N cloud variables and settings
├── n8n-workflows/         # N8N workflow documentation
│   └── supabase_query_webhook.md
├── social-media-tools/    # Social media management utilities
├── docker-compose.yml     # Docker setup for local development
├── helius_endpoints.md    # Solana/Helius RPC documentation
└── requirements.txt       # Python dependencies
```

## ✨ Key Features

### 🤖 N8N Automation Workflows

#### Multi-Agent Research & Report Generator
- **Workflow**: [View in n8n](https://thesteelezone.app.n8n.cloud/workflow/JXaYP9LBUb8x1k1f)
- **Features**:
  - Multi-agent orchestration with GPT-4
  - Research agent for data gathering
  - Fact-check agent for verification
  - Report writer agent for synthesis
  - HTML email editor for professional formatting
  - Automated HTML email delivery

#### Supabase Query Webhook
- **Endpoint**: `POST https://thesteelezone.app.n8n.cloud/webhook/query_supabase`
- **Features**:
  - Dynamic table queries via POST requests
  - Flexible filtering system
  - Security with API key authentication
  - Support for comparison operators (>, <, =)
  - [Full Documentation](./n8n-workflows/supabase_query_webhook.md)

#### Crypto Agent - Tool Webhooks
- **Workflow**: [View in n8n](https://thesteelezone.app.n8n.cloud/workflow/JXaYP9LBUb8x1k1f)
- Real-time cryptocurrency data analysis
- Automated trading alerts
- Portfolio tracking integration

### ⛓️ Blockchain Integration

#### Helius RPC Endpoints
- **HTTP Endpoint**: `https://mainnet.helius-rpc.com/?api-key=YOUR_API_KEY`
- **WebSocket**: `wss://mainnet.helius-rpc.com/?api-key=YOUR_API_KEY`
- **Features**:
  - Enterprise-grade Solana RPC access
  - NFT APIs and DAS (Digital Asset Standard)
  - Webhooks for real-time blockchain events
  - Enhanced transaction APIs
- **Documentation**: [helius_endpoints.md](./helius_endpoints.md)

### 🗄️ Supabase Database

- PostgreSQL database with real-time subscriptions
- Row-level security policies
- RESTful API auto-generated
- Integration with n8n workflows
- Tables for content, analytics, users, and automation logs

### 🎨 Content Automation

- Automated social media posting
- Content scheduling and management
- Analytics tracking and reporting
- Multi-platform support (Instagram, TikTok, Twitter/X)
- Engagement automation

### 🤝 AI Integrations

- **Claude Desktop MCP**: Local AI assistant with GitHub integration
- **Google Gemini**: Content generation and analysis
- **OpenAI GPT-4**: Advanced reasoning and multi-agent workflows
- Custom AI assistants for specific tasks

## 🔧 Getting Started

### Prerequisites

```bash
# Required software
- Node.js 18+
- Python 3.10+
- Docker & Docker Compose
- Git
```

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/the-steele-zone/the-steele-zone.git
cd the-steele-zone
```

2. **Set up environment variables**
```bash
cp .env.example .env
# Edit .env with your API keys and credentials
```

3. **Install Python dependencies**
```bash
pip install -r requirements.txt
```

4. **Start Docker services** (optional, for local development)
```bash
docker-compose up -d
```

5. **Configure n8n workflows**
- Import workflows from `n8n-workflows/` directory
- Update webhook URLs and credentials
- Test each workflow endpoint

### Environment Variables

```env
# Supabase
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your_supabase_anon_key

# Helius (Solana RPC)
HELIUS_API_KEY=your_helius_api_key

# N8N
N8N_WEBHOOK_URL=https://thesteelezone.app.n8n.cloud
WEBHOOK_API_KEY=your_webhook_security_key

# AI Services
OPENAI_API_KEY=your_openai_key
ANTHROPIC_API_KEY=your_claude_key
GOOGLE_AI_API_KEY=your_gemini_key

# Social Media
INSTAGRAM_ACCESS_TOKEN=your_instagram_token
TIKTOK_API_KEY=your_tiktok_key
```

## 📖 Documentation

- **[Setup Guide](./SETUP_GUIDE.md)** - Complete setup instructions
- **[Master Setup Documentation](./THE-STEELE-ZONE-MASTER-SETUP.md)** - Comprehensive system documentation
- **[Helius Endpoints](./helius_endpoints.md)** - Solana RPC integration guide
- **[Supabase Query Webhook](./n8n-workflows/supabase_query_webhook.md)** - API endpoint documentation
- **[MCP GitHub Server](./docs/)** - Claude Desktop integration setup

## 🔗 Connect With Me

### Social Media
- **Instagram**: [@the_steele_zone](https://www.instagram.com/the_steele_zone)
- **TikTok**: [@the_steele_zone](https://www.tiktok.com/@the_steele_zone) 
- **Twitter/X**: [@the_steele_zone](https://twitter.com/the_steele_zone)
- **All Links**: [linkfly.to/thesteelezone](https://linkfly.to/thesteelezone)

### Premium Content
- **OnlyFans**: [@thesteelezone](https://onlyfans.com/thesteelezone)
- **Fansly**: Coming Soon

### Professional
- **GitHub**: [@the-steele-zone](https://github.com/the-steele-zone)
- **LinkedIn**: Connect for business inquiries
- **Discord**: Join the community (link in bio)

## 🎯 Use Cases

### For Content Creators
- Automate social media posting across platforms
- Track engagement and analytics
- Schedule content in advance
- Generate AI-powered captions and descriptions

### For Developers
- Learn n8n workflow automation
- Integrate Supabase with webhooks
- Build Solana/Web3 applications
- Implement multi-agent AI systems

### For Entrepreneurs
- Automate business workflows
- Build custom APIs without code
- Integrate multiple services seamlessly
- Scale operations with automation

## 🔐 Security Best Practices

- ✅ Never commit API keys or credentials
- ✅ Use environment variables for sensitive data
- ✅ Implement API key authentication on webhooks
- ✅ Enable rate limiting on public endpoints
- ✅ Use table whitelisting for database queries
- ✅ Regularly rotate API keys and tokens
- ✅ Monitor logs for suspicious activity

## 🚧 Roadmap

- [ ] GraphQL API layer for Supabase
- [ ] Advanced analytics dashboard
- [ ] Mobile app integration
- [ ] Real-time collaboration features
- [ ] Enhanced AI agent capabilities
- [ ] Blockchain-based content verification
- [ ] Automated video content generation
- [ ] Multi-language support

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Contribution Guidelines
- Follow existing code style and conventions
- Add tests for new features
- Update documentation as needed
- Keep commits atomic and well-described

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- **n8n** - For the amazing workflow automation platform
- **Supabase** - For the powerful backend infrastructure
- **Helius** - For enterprise-grade Solana RPC access
- **Anthropic & OpenAI** - For cutting-edge AI capabilities
- **Open Source Community** - For inspiration and support

## 💬 Support

- **Issues**: [GitHub Issues](https://github.com/the-steele-zone/the-steele-zone/issues)
- **Discussions**: [GitHub Discussions](https://github.com/the-steele-zone/the-steele-zone/discussions)
- **Email**: Contact via social media DMs
- **Community**: Join our Discord server

## 📊 Project Stats

![Python](https://img.shields.io/badge/Python-79.7%25-blue)
![HTML](https://img.shields.io/badge/HTML-20.3%25-orange)
![Stars](https://img.shields.io/github/stars/the-steele-zone/the-steele-zone)
![Forks](https://img.shields.io/github/forks/the-steele-zone/the-steele-zone)
![Issues](https://img.shields.io/github/issues/the-steele-zone/the-steele-zone)

---

**Built with ❤️ by The Steele Zone | Automating the Future, One Workflow at a Time**

*Last Updated: December 23, 2024*
