# Connect Atlassian MCP when a source cannot be read

Use this guide when a Business to Build workflow cannot read a Jira or Confluence
link because the current assistant lacks an authenticated connection. This is
shared guidance for all six skills, not an additional skill or bundled server.
Setup guidance last checked against official documentation: 2026-10-31.

## Diagnose and help the user

1. Check available tools and connection state first. Report the observed failure:
   no Atlassian tools, login required, expired authorization, denied access,
   missing page, or a connection/network error. Do not imply a page read was
   attempted if only tool discovery was possible.
2. Ask the user to connect or reconnect **Atlassian MCP in the assistant they
   are currently using**, and give the relevant steps below. For example:
   “Please connect Atlassian MCP with access to this Confluence space. In the
   Plugins directory, search for Atlassian, install it, and complete sign-in.
   Then start a new chat if the tools do not appear.”
3. Use the host's supported integration discovery/connection UI where available.
   Follow its suggestion rules and avoid repeatedly suggesting the same pending
   installation. Do not assume an installation or sign-in succeeded.
4. After the connection is confirmed, discover the tools again and retry the
   original source read. Verify the returned page/issue ID and title before
   resuming dependent analysis. If a new chat is required, give the user the
   original source URL and a short prompt to resume the workflow there.

Continue useful independent drafting with source verification pending. Do not
replace inaccessible content with guesses or repeatedly try the same failing URL.
Installing Business to Build alone does not connect Atlassian.

## ChatGPT or Codex plugin setup

For a surface with a Plugins directory:

1. Open [Plugins](https://chatgpt.com/plugins) and search for **Atlassian**.
2. Open the plugin details and select Install or the plus button.
3. Follow the connection prompt. Sign in with the Atlassian account that can
   open the supplied Jira/Confluence link and complete the authorization flow.
4. Start a new chat after installation and ask it to use Business to Build and
   the connected Atlassian tools. A plugin may request authentication during
   installation or first use.

This route depends on host, account and workspace availability. If it is absent,
use the assistant's supported remote MCP setup instead; do not invent menu paths.
See [OpenAI's plugin instructions](https://learn.chatgpt.com/docs/plugins).

## Codex CLI alternative

Add the official remote server using the command documented by Atlassian:

```sh
codex mcp add atlassian --url https://mcp.atlassian.com/v2/mcp
```

Complete sign-in when the client starts its authentication flow. If authentication
does not start, use the installed client's documented MCP authentication controls;
check its help rather than guessing version-specific commands. Avoid configuring
a second connection if a working Atlassian integration is already present.

## Claude Code

```sh
claude mcp add --transport http atlassian https://mcp.atlassian.com/v2/mcp
```

Open a Claude Code session, run `/mcp`, and authenticate the Atlassian connection.
This does not require changing the shared Business to Build skills.

## Antigravity or another MCP-capable host

Use the host's documented remote MCP connection flow with the official server URL
`https://mcp.atlassian.com/v2/mcp` and its supported Atlassian authorization flow.
If the installed host cannot authenticate this server, consult the host's current
documentation rather than copying another assistant's configuration format.
Do not assume Codex plugins, Claude commands or authentication transfer between
hosts. Provide this portable setup request where the agent supports MCP setup:

```text
Set up Atlassian MCP for this assistant using the official guide:
https://support.atlassian.com/atlassian-ai-gateway/docs/get-started-with-the-atlassian-remote-mcp-server/
Server URL: https://mcp.atlassian.com/v2/mcp
Start the authentication flow so I can sign in, then verify read access
to <original-Jira-or-Confluence-URL>.
```

The endpoint and Codex/Claude commands above come from
[Atlassian's official setup guide](https://support.atlassian.com/atlassian-ai-gateway/docs/get-started-with-the-atlassian-remote-mcp-server/).
Recheck official guidance before changing connection configuration if these steps
fail or a host version differs. This package has not verified live authentication
in all three assistants.

## If connection succeeds but access still fails

| Observed issue | Next action |
| --- | --- |
| Tools still absent | Confirm the integration is enabled in this host/workspace; start a new chat/session if required. |
| Expired sign-in or wrong account/site | Reauthenticate through the host and select the account with access to the source. |
| Permission denied | Check whether that account can open the source directly; ask its owner for access or the Atlassian admin about MCP restrictions. |
| Missing/deleted page or wrong URL | Ask for the corrected source link; a new MCP connection cannot restore missing content. |
| Network/service error | Report the error and retry when connectivity is restored; do not assume an authentication fault. |

MCP respects existing Atlassian access permissions. Never request passwords, API
tokens or authorization codes in chat. A connection enables tools; it does not
authorize publishing pages, creating tickets or changing permissions.

## Verify and resume

Offer a read-only test using the user's actual source, not a sample private site:

```text
Use Business to Build's knowledge-maintenance skill to read <Confluence-URL>.
Confirm its title and summarize the documentation structure. Report access
problems and missing evidence before continuing. Draft proposed updates.
```

For other skills, keep the original skill and task in the resume prompt. Confirm
actual read results before claiming the connection works; do not claim a full
documentation or design review from a successful connection test alone.
