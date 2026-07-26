# Use Ace Data Cloud credits in VS Code

This repository includes a project configuration for the **Continue** VS Code
extension. Continue connects to Ace Data Cloud through its OpenAI-compatible API,
so prompts sent with the `Ace Data Cloud` model consume the balance associated
with the supplied Ace Data Cloud API key.

## What credential to use

Use an **Ace Data Cloud API key** as `ACEDATA_API_KEY`. An OAuth Client ID is a
public application identifier and is not an API key; the Client ID shown on the
OAuth Apps page cannot authenticate model requests by itself.

Never paste the API key into `.continue/config.yaml`, VS Code settings, source
files, or Git. If a secret has already been shared or committed, revoke it before
continuing and create a replacement.

## Setup

1. Open this repository as a folder in VS Code.
2. Install the recommended **Continue - open-source AI code agent** extension
   (`continue.continue`).
3. Obtain an API key from the Ace Data Cloud developer dashboard. Do not use the
   OAuth Client ID as the key.
4. Open Continue, choose **Local Config**, and add a secret named
   `ACEDATA_API_KEY` when Continue prompts for the unresolved secret in
   `.continue/config.yaml`.
5. Reload the VS Code window, open Continue, and select **Ace Data Cloud** from
   the model picker.

The checked-in configuration uses:

- API base: `https://api.acedata.cloud/v1`
- Provider protocol: OpenAI-compatible
- Default model: `gpt-4o-mini`

If the Ace dashboard lists a different model identifier for the account, replace
only the `model` value in `.continue/config.yaml` with that exact identifier.

## Verify the API key and credit access

Before troubleshooting VS Code, verify the key directly from a terminal. This
command reads the key without echoing it and does not save it to shell history:

```bash
read -rsp "Ace Data Cloud API key: " ACEDATA_API_KEY && echo
curl --fail-with-body --silent --show-error \
  -H "Authorization: Bearer ${ACEDATA_API_KEY}" \
  -H "Content-Type: application/json" \
  https://api.acedata.cloud/v1/models
unset ACEDATA_API_KEY
```

A successful response listing models confirms authentication. Then send a short
prompt in Continue and confirm the request appears in the Ace Data Cloud usage or
billing dashboard.

## Common errors

| Error | Resolution |
| --- | --- |
| `401` or `invalid_api_key` | Use an API key, not the OAuth Client ID, and replace a revoked or expired key. |
| `402`, insufficient balance, or quota error | Add credits or confirm the key belongs to the funded Ace Data Cloud account. |
| Model not found | Copy an available model ID from the dashboard or `/v1/models` into `.continue/config.yaml`. |
| Continue shows no project model | Open the repository root, reload VS Code, and check the YAML for local edits. |
| Requests use another provider | Explicitly select **Ace Data Cloud** in Continue's model picker. |

