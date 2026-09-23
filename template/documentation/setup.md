# Before the workshop

Bring a Mac with Glyphs 4, a working Glyphs Python scripting environment, a text
editor, internet access, and an AI client/account that supports the tested
connection recipe. Account features and access vary; installing a chat app is
not by itself proof that it can connect to your local server.

## 1. Install Glyphs MCP

1. Save your existing work and quit Glyphs normally.
2. Download the signed Glyphs MCP app from the release linked on the workshop page.
   The preparation draft links Beta 6; check the final workshop build before class.
3. Open the DMG, drag Glyphs MCP.app to Applications, and launch that installed copy.
4. In Setup, choose **Install All**, or install the required component and client
   cards individually. A previously installed component shows **Update** instead.
5. Restart Glyphs, then reload/restart your AI client when its card requests it.
6. Check that the server reports Ready and that the client can identify Glyphs.

On a fresh Glyphs installation, install Python in **Window → Plugin Manager →
Modules**, restart Glyphs, then explicitly choose the Python version labelled
**(Glyphs)** under **Glyphs → Settings → Addons**. Do not bypass macOS security
warnings; use a signed release and its documented troubleshooting instructions.

## 2. Connect your client

The app has setup cards for Codex, Claude Code, Claude Desktop and Cursor.
The first workshop draft uses **Claude Desktop for font work**, with a code-capable
client as an optional path for the script exercise. This is a proposed teaching
path pending rehearsal, not a completed compatibility certification.

Claude Desktop's MCP setup does not install the same managed skills as the
code-client cards. ChatGPT's exact connection route is not yet qualified for
this workshop. Use only the final, rehearsed recipe for your selected client;
do not expose a local server to the internet as a workaround.

## 3. Create your own workshop project

Extract the workshop ZIP. In Glyphs MCP choose **Project → Add Local Template…**,
select the extracted template folder, then **Use Template**. Name the new project
and choose a local parent folder. Review the file preview and create it.
For a full repository checkout, select its `template/` subfolder.

Open the new project's `sources/Workshop Demo.glyphs`, not the master template.
Save it if the app asks. Confirm one master (Regular), H and O, and a width of
600 units for both. The template intentionally has no dependencies or automatic
scripts. Select H and O in an Edit tab when testing the reporting script.

## 4. First connection prompt

> Check Glyphs MCP status and identify my Workshop Demo font, including its file
> path and masters. Do not change anything. Summarize what you can inspect.

Compare the name and path with the font you opened. Stop if the assistant finds
a different font. Preparation requires a saved, clean source; saving includes
the whole document, so use only the disposable workshop copy.
