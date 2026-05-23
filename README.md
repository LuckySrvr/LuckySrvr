# {{ lucky }}

A community-driven, decentralized high-availability backup proxy network. Protect your infrastructure by routing through the Lucky cluster.

## How to join Lucky

Follow these steps to securely register your server using a GitHub Pull Request:

1. **Fork** this repository to your personal GitHub account.
2. Navigate into the `nodes/` directory within your fork.
3. Create a brand-new file inside the `nodes/` folder named after your domain (e.g., `nodes/mywebsite.json`).
4. Paste the configuration syntax structure shown below into your file, substituting your routing parameters.
5. Commit your changes and submit a **Pull Request** back to the main repository.

## Configuration Syntax Structure

Your JSON layout inside the `nodes/` folder must match this specification:

```json
{
  "domain": "mywebsite.com",
  "primary_target_url": "http://192.0.2.1:8080"
}
```

Once your Pull Request is reviewed and merged into the master cluster, Lucky will immediately begin tracking your node health and intercept traffic automatically if a crash is encountered.
