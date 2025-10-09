# TikTok/Instagram to Discord Auto-Post Setup Guide

## Overview
This repository contains a GitHub Actions workflow that automatically posts TikTok and Instagram content to Discord with Solana blockchain integration for treasury monitoring.

## Features
- ✅ Automatic posting from TikTok/Instagram to Discord
- ✅ Media attachment support (images and videos)
- ✅ Solana treasury balance monitoring
- ✅ Customizable pricing and spend caps
- ✅ Discord embed formatting with reactions
- ✅ Logging to dedicated log channel
- ✅ Test mode for safe testing
- ✅ Scheduled checks every 15 minutes
- ✅ Manual workflow dispatch

## Prerequisites

### 1. Discord Bot Setup
1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Create a new application
3. Navigate to "Bot" section and create a bot
4. Enable the following privileged intents:
   - Server Members Intent
   - Message Content Intent
5. Copy the bot token (DISCORD_BOT_TOKEN)
6. Invite the bot to your server with permissions:
   - Send Messages
   - Embed Links
   - Attach Files
   - Add Reactions
   - Read Message History

### 2. Discord Server Configuration
1. Enable Developer Mode in Discord (Settings > Advanced > Developer Mode)
2. Right-click your server name → Copy ID (DISCORD_GUILD_ID)
3. Right-click your drops channel → Copy ID (DISCORD_DROPS_CHANNEL_ID)
4. Right-click your log channel → Copy ID (DISCORD_LOG_CHANNEL_ID)

### 3. Solana Wallet (Optional)
1. Use your existing Solana wallet address (TREASURY_WALLET)
2. Example: `HwUvurCPfmuhr6WwPjnnLK2EXxRmr7oqx94mTB5Fyr1U`

## GitHub Secrets Configuration

### Required Secrets
Navigate to: **Repository Settings → Secrets and variables → Actions → New repository secret**

Add the following secrets:

| Secret Name | Description | Example Value |
|------------|-------------|---------------|
| `DISCORD_BOT_TOKEN` | Your Discord bot token | `MTIzNDU2Nzg5MDEyMzQ1Njc4OTAuGaBcDe.FgHiJkLmNoPqRsTuVwXyZ` |
| `DISCORD_GUILD_ID` | Your Discord server ID | `1234567890123456789` |
| `DISCORD_DROPS_CHANNEL_ID` | Channel for posting content | `9876543210987654321` |
| `DISCORD_LOG_CHANNEL_ID` | Channel for logging | `1122334455667788990` |

### Optional Secrets (Solana Integration)

| Secret Name | Description | Default Value |
|------------|-------------|---------------|
| `SOLANA_RPC` | Solana RPC endpoint | `https://api.mainnet-beta.solana.com` |
| `TREASURY_WALLET` | Your Solana wallet address | Your wallet address |
| `NETWORK` | Solana network | `mainnet` |
| `MINT_PRICE_SOL` | NFT mint price in SOL | `1.0` |
| `MAX_DYNAMIC_PRICE_UP_PCT` | Max price increase % | `25` |
| `MAX_DYNAMIC_PRICE_DOWN_PCT` | Max price decrease % | `25` |
| `DAILY_SPEND_SOL_CAP` | Daily spending cap in SOL | `5.0` |
| `WEEKLY_SPEND_SOL_CAP` | Weekly spending cap in SOL | `20.0` |
| `MIN_TREASURY_BALANCE_SOL` | Minimum treasury balance | `2.0` |

## Installation Steps

### Step 1: Configure GitHub Secrets
1. Go to your repository on GitHub
2. Click **Settings** → **Secrets and variables** → **Actions**
3. Click **New repository secret**
4. Add each secret from the table above
5. Click **Add secret** for each one

### Step 2: Verify Files
Ensure these files exist in your repository:
- `.github/workflows/main.yml` - GitHub Actions workflow
- `requirements.txt` - Python dependencies

### Step 3: Test the Workflow

#### Manual Test
1. Go to **Actions** tab in your repository
2. Click **Social Media to Discord Auto-Post**
3. Click **Run workflow**
4. Fill in the test parameters:
   - **Platform**: `tiktok` or `instagram`
   - **Media URL**: URL to test media (e.g., `https://example.com/image.jpg`)
   - **Post caption/text**: Your test message
   - **Test mode**: ✅ Check this for testing
5. Click **Run workflow**
6. Check your Discord channel for the test post

#### Scheduled Execution
The workflow runs automatically every 15 minutes to check for new posts.

## Workflow Triggers

1. **Manual Dispatch** - Run workflow manually from GitHub Actions tab
2. **Schedule** - Automatic checks every 15 minutes (`*/15 * * * *`)
3. **Repository Dispatch** - Webhook-triggered via API

## Python Dependencies

The workflow installs these packages from `requirements.txt`:
- `fastapi` - Web framework for webhook handling
- `uvicorn` - ASGI server
- `pydantic` - Data validation
- `python-dotenv` - Environment variable management
- `httpx` - HTTP client
- `discord.py==2.4.0` - Discord bot library
- `apscheduler` - Scheduling automation
- `base58` - Base58 encoding for Solana
- `pynacl` - Cryptography for Solana
- `solana` - Solana blockchain integration

## Node.js Dependencies

The workflow automatically installs:
- `discord.js` - Discord API library
- `@discordjs/rest` - REST API utilities
- `discord-api-types` - TypeScript types
- `axios` - HTTP client for media downloads
- `dotenv` - Environment variables
- `@solana/web3.js` - Solana Web3 SDK

## Security Best Practices

⚠️ **IMPORTANT**: Never commit secrets to your repository!

✅ **DO**:
- Store all sensitive data in GitHub Secrets
- Use environment variables in Render
- Rotate tokens periodically
- Use test mode for initial testing
- Monitor log channel for issues

❌ **DON'T**:
- Commit `.env` files
- Hardcode tokens in workflow files
- Share bot tokens publicly
- Commit private keys

## Render Environment Configuration

If deploying a backend service on Render:

1. Go to your Render dashboard
2. Select your service
3. Navigate to **Environment** tab
4. Add environment variables:
   - All Discord variables
   - All Solana variables
   - PORT=8000
   - Any other custom variables

## Testing the Setup

### Test 1: Manual Workflow Run
```bash
# From GitHub Actions UI
1. Go to Actions → Social Media to Discord Auto-Post
2. Click "Run workflow"
3. Fill in test data
4. Enable "Test mode"
5. Click "Run workflow"
```

### Test 2: Check Discord
1. Verify bot is online in your server
2. Check drops channel for test post
3. Verify reactions are added
4. Check log channel for success message

### Test 3: Verify Python Installation
The workflow includes a verification step that shows:
- Python version
- Installed packages
- Check workflow logs to confirm

## Troubleshooting

### Bot Not Posting
- ✅ Verify bot token is correct
- ✅ Ensure bot has proper permissions
- ✅ Check channel IDs are correct
- ✅ Review workflow logs for errors

### Missing Python Packages
- ✅ Verify `requirements.txt` exists
- ✅ Check workflow logs for pip errors
- ✅ Ensure Python version is 3.11+

### Media Not Downloading
- ✅ Verify media URL is accessible
- ✅ Check file size (Discord has limits)
- ✅ Test with different media formats

### Solana Integration Issues
- ✅ Verify wallet address format
- ✅ Check RPC endpoint connectivity
- ✅ Ensure network is set correctly

## Workflow Structure

```yaml
Checkout Repository
  ↓
Setup Python 3.11
  ↓
Install Python Dependencies (requirements.txt)
  ↓
Setup Node.js 20
  ↓
Install Node.js Dependencies
  ↓
Create Discord Posting Script
  ↓
Verify Python Installation
  ↓
Run Discord Posting Script
  ↓
Notify on Success/Failure
```

## Next Steps

1. ✅ Configure all required GitHub Secrets
2. ✅ Run a test workflow with test mode enabled
3. ✅ Verify Discord post appears correctly
4. ✅ Check log channel for confirmation
5. ✅ Disable test mode for production
6. ✅ Set up Render environment if using backend
7. ✅ Monitor scheduled runs

## Support

For issues or questions:
1. Check workflow logs in Actions tab
2. Review Discord log channel messages
3. Verify all secrets are configured
4. Test with simple media first

## License

This project is configured for automated social media integration with Discord and Solana blockchain monitoring.
