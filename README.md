# The Steele Zone — Sophie & Jax Steele | Exclusive Couple Content + BTS + Customs
### Real couple. Real chemistry. Real content.

---

## 🔥 What We Offer

We're Sophie & Jax Steele — a genuine couple creating exclusive, consent-first content that celebrates our connection. Every week, we drop fresh couple content, behind-the-scenes moments, and custom experiences made just for you.

- 💑 **Authentic Couple Content** — Real intimacy, real passion
- 📸 **Weekly Content Drops** — New exclusive photos & videos every week
- 🎬 **Behind-the-Scenes Access** — See what goes into creating our content
- ✨ **Custom Content Available** — Personalized requests welcome
- 🤝 **Consent-First Always** — Respectful, ethical content creation

---

## 💎 Where to Find Us

### 🔗 Primary Platform

👉 **[Subscribe on OnlyFans](https://onlyfans.com/thesteelezone)** 👈

Get instant access to:
- Exclusive couple photos & videos
- Weekly fresh content
- Behind-the-scenes footage
- Direct messaging with us
- Custom content requests
- VIP treatment & early access

### 🌐 All Links in One Place

🔗 **[Linkfly - All Our Links](https://linkfly.to/thesteelezone)**

Find everything here: OnlyFans, social media, contact info, and more.

---

## 📱 Follow Us on Social Media

Stay connected and never miss an update:

- 📸 **Instagram**: [@the_steele_zone](https://instagram.com/the_steele_zone) — Daily posts, stories, and teasers
- 🎵 **TikTok**: [@sophie__steele](https://tiktok.com/@sophie__steele) — Fun couple content and trends
- 🔗 **Linkfly**: [linkfly.to/thesteelezone](https://linkfly.to/thesteelezone) — All our links

---

## 💌 Get in Touch

Interested in custom content or collaborations?

📧 **Email**: [vip.thesteelezone@gmail.com](mailto:vip.thesteelezone@gmail.com)
🔗 **Website**: [onlyfans.com/thesteelezone](https://onlyfans.com/thesteelezone)

---

## 🤖 Automated Social Media to Discord Workflow

### 🎯 Essential Infrastructure for @thesteelezone and @thediscobassnft

This repository contains a critical GitHub Actions workflow that automatically posts new social media content (TikTok/Instagram) to Discord channels. This workflow is the backbone of our community engagement and NFT project automation.

### 📂 Workflow File Location

**[`.github/workflows/main.yml`](.github/workflows/main.yml)** - Social Media to Discord Auto-Post Workflow

### ✨ Features

- 🔄 **Automatic Posting**: Runs every 15 minutes to check for new social media content
- 🎮 **Discord Integration**: Posts directly to Discord channels with rich embeds
- 💎 **Solana NFT Integration**: Monitors treasury wallet balance for @thediscobassnft project
- 📊 **Real-time Monitoring**: Tracks mint prices, treasury status, and engagement
- 🧪 **Test Mode**: Safe testing without affecting production channels
- 📱 **Multi-Platform**: Supports both TikTok and Instagram content

### 🚀 How It Works

1. **Scheduled Runs**: Automatically checks for new content every 15 minutes
2. **Manual Triggers**: Can be triggered manually via GitHub Actions interface
3. **Content Processing**: Downloads media, creates Discord embeds with metadata
4. **Community Engagement**: Auto-reacts with 🔥💎🚀 emojis
5. **Logging**: Maintains detailed logs in dedicated Discord channel

### 🔧 Required Secrets

To use this workflow, configure these secrets in GitHub repository settings:

#### Discord Configuration (Required)
- `DISCORD_BOT_TOKEN` - Your Discord bot token
- `DISCORD_GUILD_ID` - Discord server ID
- `DISCORD_DROPS_CHANNEL_ID` - Channel for content drops
- `DISCORD_LOG_CHANNEL_ID` - Channel for workflow logs

#### Solana/NFT Configuration (Optional for @thediscobassnft)
- `SOLANA_RPC` - Helius RPC endpoint
- `TREASURY_WALLET` - Solana wallet address
- `NETWORK` - Solana network (mainnet/devnet)
- `MINT_PRICE_SOL` - NFT mint price in SOL
- `MIN_TREASURY_BALANCE_SOL` - Minimum balance threshold

#### Pricing & Limits (Optional)
- `MAX_DYNAMIC_PRICE_UP_PCT` - Max price increase percentage
- `MAX_DYNAMIC_PRICE_DOWN_PCT` - Max price decrease percentage
- `DAILY_SPEND_SOL_CAP` - Daily spending cap in SOL
- `WEEKLY_SPEND_SOL_CAP` - Weekly spending cap in SOL

### 📖 Usage Examples

#### Manual Trigger

1. Go to [Actions tab](../../actions/workflows/main.yml)
2. Click "Run workflow"
3. Select platform (TikTok/Instagram)
4. Enter media URL and post text
5. Toggle test mode if needed
6. Click "Run workflow"

#### Automatic Operation

The workflow runs automatically every 15 minutes. No manual intervention needed for scheduled checks.

### 🔗 Quick Links

- **[View Workflow File](.github/workflows/main.yml)** - Complete YAML configuration
- **[GitHub Actions Dashboard](../../actions)** - Monitor workflow runs
- **[Workflow Runs History](../../actions/workflows/main.yml)** - Past execution logs

### 🎯 Use Cases

#### For @thesteelezone:
- Automatically share new TikTok/Instagram posts to Discord community
- Keep fans engaged with instant notifications
- Cross-platform content distribution

#### For @thediscobassnft:
- Announce NFT drops with Solana integration
- Monitor treasury wallet balance
- Display mint prices and availability
- Community alerts for new mints

### 📝 Important Notes

- ⚠️ **DO NOT DELETE THIS WORKFLOW** - It's essential for both projects
- 🔒 **Keep Secrets Secure** - Never commit actual API keys or tokens
- 🧪 **Test Before Production** - Use test mode for new configurations
- 📊 **Monitor Logs** - Check Discord log channel for workflow status

---

## 🔌 Helius Integration

This project uses Helius for Solana blockchain RPC access and enhanced APIs.

### Project Details

- **Project ID**: `c0065bc7-ee1b-426b-883a-ce86109e02ba`
- **Project Name**: Gargoylethorn
- **API Key Format**: `YOUR-API-KEY-HERE` (use placeholder, never commit actual keys)

### Available Endpoints

#### RPC URLs

- **Mainnet RPC**: `https://mainnet.helius-rpc.com/?api-key=YOUR-API-KEY-HERE`
- **Devnet RPC**: `https://devnet.helius-rpc.com/?api-key=YOUR-API-KEY-HERE`

#### Websocket URLs

- **Standard Websocket (Mainnet)**: `wss://mainnet.helius-rpc.com/?api-key=YOUR-API-KEY-HERE`
- **Standard Websocket (Devnet)**: `wss://devnet.helius-rpc.com/?api-key=YOUR-API-KEY-HERE`
- **Enhanced Websocket**: Requires Business plan or higher upgrade

#### Enhanced Solana APIs

- **Parse Transaction(s)**: `https://api.helius.xyz/v0/transactions/?api-key=YOUR-API-KEY-HERE`
- **Parse Transaction History**: `https://api.helius.xyz/v0/addresses/{address}/transactions/?api-key=YOUR-API-KEY-HERE`

### Usage Notes

#### SOL Rebates (Optional Feature)

Earn automatic SOL rebates via post-trade backruns with no additional risk of toxic MEV:

- Add `rebate-address=YOUR_WALLET_ADDRESS` query parameter to any `sendTransaction` call on mainnet
- This is completely optional - Helius will never do this without your permission
- Example: `https://mainnet.helius-rpc.com/?api-key=YOUR-API-KEY-HERE&rebate-address=YOUR_WALLET_ADDRESS`

#### Security Best Practices

- Never commit actual API keys to the repository
- Use environment variables to store sensitive credentials
- Store API keys in `.env` file (already listed in `.gitignore`)
- Use placeholder `YOUR-API-KEY-HERE` in documentation

#### Access Control

The Free Plan provides basic access with limited performance. Consider upgrading for:

- Enhanced Websocket URLs
- Improved performance
- Additional features

### Useful Links

- **Helius Dashboard**: [https://dashboard.helius.dev/dashboard?projectId=c0065bc7-ee1b-426b-883a-ce86109e02ba](https://dashboard.helius.dev/dashboard?projectId=c0065bc7-ee1b-426b-883a-ce86109e02ba)
- **Endpoints Page**: [https://dashboard.helius.dev/endpoints?projectId=c0065bc7-ee1b-426b-883a-ce86109e02ba](https://dashboard.helius.dev/endpoints?projectId=c0065bc7-ee1b-426b-883a-ce86109e02ba)
- **API Documentation**: [https://www.helius.dev/docs](https://www.helius.dev/docs)
- **RPC Testing Playground**: [https://dashboard.helius.dev/playground?projectId=c0065bc7-ee1b-426b-883a-ce86109e02ba](https://dashboard.helius.dev/playground?projectId=c0065bc7-ee1b-426b-883a-ce86109e02ba)
- **Support**: [https://dashboard.helius.dev/support?projectId=c0065bc7-ee1b-426b-883a-ce86109e02ba](https://dashboard.helius.dev/support?projectId=c0065bc7-ee1b-426b-883a-ce86109e02ba)
- **System Status**: [https://dashboard.helius.dev/system-status?projectId=c0065bc7-ee1b-426b-883a-ce86109e02ba](https://dashboard.helius.dev/system-status?projectId=c0065bc7-ee1b-426b-883a-ce86109e02ba)
- **Billing/Upgrade**: [https://dashboard.helius.dev/billing?projectId=c0065bc7-ee1b-426b-883a-ce86109e02ba](https://dashboard.helius.dev/billing?projectId=c0065bc7-ee1b-426b-883a-ce86109e02ba)

### Supported Features

#### Available on Free Plan

- RPC URL access (mainnet and devnet)
- Standard Websocket URLs
- Enhanced Solana APIs (Parse Transactions)
- Basic performance and access

#### Requires Upgrade

- Enhanced Websocket URLs (Business plan or above)
- Improved performance
- Additional advanced features
- Priority support
