# MCP GitHub Server Setup for The Steele Zone

## What This Does

Wires Claude Desktop (Comet assistant) directly to your GitHub repos so you can:
- Read/write files in `the-steele-zone` and other repos without copy-paste
- Create issues, branches, PRs from chat
- Keep all your n8n workflows, Docker configs, and prompts version-controlled
- Let the assistant see your full stack context

## Prerequisites

1. **Claude Desktop app** installed on your Mac
2. **GitHub Personal Access Token** with repo access
3. **Node.js** installed (for running MCP servers)

---

## Step 1: Create GitHub Personal Access Token

1. Go to: https://github.com/settings/tokens/new
2. Set **Token name**: `Claude MCP Server`
3. Set **Expiration**: 90 days (or No expiration if you want permanent)
4. Check these scopes:
   - ✅ `repo` (full control of private repositories)
   - ✅ `workflow` (if you want to manage GitHub Actions)
5. Click **Generate token**
6. **Copy the token immediately** (you won't see it again)
7. Save it somewhere secure (1Password, etc.)

---

## Step 2: Install the GitHub MCP Server

Open Terminal and run:

```bash
npx -y @modelcontextprotocol/server-github
```

This tests if it works. You should see output about available tools.

---

## Step 3: Configure Claude Desktop

### Find your config file:

```bash
# On Mac:
open ~/Library/Application\\ Support/Claude/
```

You should see a file called `claude_desktop_config.json`. If it doesn't exist, create it:

```bash
touch ~/Library/Application\\ Support/Claude/claude_desktop_config.json
```

### Edit the config file:

Open `claude_desktop_config.json` and paste this:

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-github"
      ],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "ghp_YOUR_TOKEN_HERE"
      }
    }
  }
}
```

**Replace `ghp_YOUR_TOKEN_HERE` with your actual GitHub token from Step 1.**

---

## Step 4: Restart Claude Desktop

1. Quit Claude Desktop completely (Cmd+Q)
2. Reopen Claude Desktop
3. Start a new chat

---

## Step 5: Test the Connection

In Claude Desktop, try asking:

> "List the files in the-steele-zone/the-steele-zone repo"

Or:

> "Show me the README from the-steele-zone repo"

If it works, Claude can now read/write to your GitHub repos directly.

---

## What You Can Do Now

### Version-control your entire stack:

1. **n8n workflows**: Export workflows as JSON, commit to `workflows/` folder
2. **Docker configs**: Keep `docker-compose.yml` and `.env.example` in repo
3. **Supabase schemas**: Export table schemas to `supabase/schema.sql`
4. **Agent prompts**: Store system prompts in `prompts/disco-bass.md`, `prompts/crystal-house.md`, etc.
5. **Webador embeds**: Keep chat widget configs in `webador/chat-config.json`

### Ask Claude to do things like:

- "Create a new branch for the Disco Bass concierge feature"
- "Show me all the n8n workflows we have in the workflows folder"
- "Update the Crystal Clear House prompt with these changes..."
- "Create an issue for setting up Supabase integration"

---

## Troubleshooting

### "MCP server not found" error:
- Make sure Node.js is installed: `node --version`
- Try installing globally: `npm install -g @modelcontextprotocol/server-github`

### "Authentication failed" error:
- Check your token has `repo` scope
- Verify the token in config file is correct (no extra spaces)
- Make sure the token hasn't expired

### Claude Desktop not loading config:
- Verify file path: `~/Library/Application Support/Claude/claude_desktop_config.json`
- Check JSON syntax (use JSONLint.com)
- Restart Claude Desktop after any config changes

---

## Next Steps

1. ✅ Wire in Docker MCP toolkit (for managing containers)
2. ✅ Add filesystem MCP server (for local file editing)
3. ✅ Create a "stack inventory" document listing all your services
4. ✅ Set up automated exports from n8n → GitHub

---

## Resources

- [MCP GitHub Server Docs](https://github.com/modelcontextprotocol/servers/tree/main/src/github)
- [Claude Desktop MCP Guide](https://docs.anthropic.com/claude/docs/mcp)
- [The Steele Zone Repo](https://github.com/the-steele-zone/the-steele-zone)
