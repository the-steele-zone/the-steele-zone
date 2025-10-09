# Helius Mainnet Endpoints

## What are Helius Endpoints?

Helius provides high-performance RPC (Remote Procedure Call) endpoints for interacting with the Solana blockchain. These endpoints offer:

- **Enhanced reliability**: Enterprise-grade infrastructure with high uptime
- **Advanced features**: Enhanced APIs including webhooks, NFT APIs, and DAS (Digital Asset Standard) API
- **Better performance**: Optimized for speed and low latency
- **Developer tools**: Built-in analytics and debugging capabilities

Helius endpoints are available in two formats:
- **HTTP/HTTPS**: For standard request-response interactions
- **WebSocket (WSS)**: For real-time streaming and subscription-based updates

## Endpoints

### HTTP Endpoint
```
https://mainnet.helius-rpc.com/?api-key=YOUR_API_KEY
```

### WebSocket Endpoint
```
wss://mainnet.helius-rpc.com/?api-key=YOUR_API_KEY
```

## How to Use in Node.js

### HTTP Endpoint Example

```javascript
// Install dependencies: npm install @solana/web3.js dotenv

require('dotenv').config();
const { Connection, PublicKey, clusterApiUrl } = require('@solana/web3.js');

// Initialize connection with Helius HTTP endpoint
const connection = new Connection(
  `https://mainnet.helius-rpc.com/?api-key=${process.env.HELIUS_API_KEY}`,
  'confirmed'
);

// Example: Get account balance
async function getBalance(walletAddress) {
  try {
    const publicKey = new PublicKey(walletAddress);
    const balance = await connection.getBalance(publicKey);
    console.log(`Balance: ${balance / 1e9} SOL`);
    return balance;
  } catch (error) {
    console.error('Error fetching balance:', error);
  }
}

// Example: Get recent blockhash
async function getRecentBlockhash() {
  try {
    const { blockhash } = await connection.getLatestBlockhash();
    console.log('Recent blockhash:', blockhash);
    return blockhash;
  } catch (error) {
    console.error('Error fetching blockhash:', error);
  }
}

// Usage
getBalance('YourWalletAddressHere');
getRecentBlockhash();
```

### WebSocket Endpoint Example

```javascript
// Install dependencies: npm install @solana/web3.js dotenv

require('dotenv').config();
const { Connection, PublicKey } = require('@solana/web3.js');

// Initialize connection with Helius WebSocket endpoint
const connection = new Connection(
  `https://mainnet.helius-rpc.com/?api-key=${process.env.HELIUS_API_KEY}`,
  {
    commitment: 'confirmed',
    wsEndpoint: `wss://mainnet.helius-rpc.com/?api-key=${process.env.HELIUS_API_KEY}`
  }
);

// Example: Subscribe to account changes
async function subscribeToAccount(walletAddress) {
  try {
    const publicKey = new PublicKey(walletAddress);
    
    console.log(`Subscribing to account: ${walletAddress}`);
    
    const subscriptionId = connection.onAccountChange(
      publicKey,
      (accountInfo, context) => {
        console.log('Account changed!');
        console.log('Slot:', context.slot);
        console.log('New balance:', accountInfo.lamports / 1e9, 'SOL');
      },
      'confirmed'
    );
    
    console.log('Subscription ID:', subscriptionId);
    
    // To unsubscribe later:
    // await connection.removeAccountChangeListener(subscriptionId);
    
  } catch (error) {
    console.error('Error subscribing to account:', error);
  }
}

// Example: Subscribe to program account changes
async function subscribeToProgramAccounts(programId) {
  try {
    const publicKey = new PublicKey(programId);
    
    console.log(`Subscribing to program: ${programId}`);
    
    const subscriptionId = connection.onProgramAccountChange(
      publicKey,
      (accountInfo, context) => {
        console.log('Program account changed!');
        console.log('Slot:', context.slot);
        console.log('Account pubkey:', accountInfo.accountId.toString());
      },
      'confirmed'
    );
    
    console.log('Subscription ID:', subscriptionId);
    
  } catch (error) {
    console.error('Error subscribing to program:', error);
  }
}

// Usage
subscribeToAccount('YourWalletAddressHere');
```

## Security Best Practices

### Never Commit API Keys

**⚠️ CRITICAL**: Never commit your API keys to version control. Always use environment variables.

### Use .env Files

1. Create a `.env` file in your project root:
```bash
HELIUS_API_KEY=your_actual_api_key_here
```

2. Add `.env` to your `.gitignore`:
```bash
echo ".env" >> .gitignore
```

3. Create a `.env.example` file as a template (without actual keys):
```bash
HELIUS_API_KEY=your_api_key_here
```

4. Load environment variables in your code:
```javascript
require('dotenv').config();
const apiKey = process.env.HELIUS_API_KEY;
```

### Additional Security Tips

- **Rotate keys regularly**: Generate new API keys periodically
- **Use rate limiting**: Implement proper rate limiting in your application
- **Monitor usage**: Check your Helius dashboard for unusual activity
- **Restrict key scope**: If possible, use keys with minimal required permissions
- **Server-side only**: Never expose API keys in client-side code

## Official Documentation

- [Helius Official Documentation](https://docs.helius.dev/)
- [Helius API Reference](https://docs.helius.dev/solana-rpc-nodes/alpha-nodes)
- [Helius Enhanced APIs](https://docs.helius.dev/api-reference/enhanced-transactions-api)
- [Solana Web3.js Documentation](https://solana-labs.github.io/solana-web3.js/)
- [Helius Dashboard](https://dashboard.helius.dev/) (for managing API keys)

## Getting Started

1. Sign up at [Helius Dashboard](https://dashboard.helius.dev/)
2. Create a new API key for your project
3. Install required dependencies: `npm install @solana/web3.js dotenv`
4. Set up your `.env` file with your API key
5. Start building with the examples above!

## Support

For questions and support:
- [Helius Discord](https://discord.gg/helius)
- [Helius Twitter](https://twitter.com/heliuslabs)
- [GitHub Issues](https://github.com/helius-labs)
