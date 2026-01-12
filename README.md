# Naver Search MCP Server

Connecting Claude Desktop & Cursor to **Naver(Korea's #1 Search Engine)**.
Claude에서 **네이버 쇼핑 최저가, 카페 리얼 후기, 실시간 뉴스**를 검색하세요.

> **Why use this?**
> Brave Search or Google often fail to retrieve local Korean information (Prices, Cafe posts, News).
> This MCP serves as a bridge to Naver's robust database.

## Key Features

- **Shopping (쇼핑):** Compare lowest prices from Naver Shopping.
- **Cafe (카페):** Search community posts (Naver Cafe) for real user reviews.
- **News (뉴스):** Get real-time Korean news articles.
- **Blog (블로그):** Find authentic reviews from Korean bloggers.

## Quick Start

### 1. Prerequisites
- Python 3.10+
- [Naver Developers API Key](https://developers.naver.com/apps/#/register) (Free 25,000 reqs/day)

### 2. Installation

<details>
<summary><b>Claude Desktop</b></summary>

Add this to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "naver-search": {
      "command": "uv",
      "args": [
        "run",
        "--with", "mcp[cli]",
        "--with", "httpx",
        "--with", "python-dotenv",
        "/YOUR/PATH/TO/mcp-server-naver-search/server.py"
      ],
      "env": {
        "NAVER_CLIENT_ID": "YOUR_ID",
        "NAVER_CLIENT_SECRET": "YOUR_SECRET"
      }
    }
  }
}
```

</details>

<details>
<summary><b>Claude Code (CLI)</b></summary>

Add this to your `~/.claude/settings.json`:

```json
{
  "mcpServers": {
    "naver-search": {
      "command": "sh",
      "args": [
        "-c",
        "export PATH=\"$HOME/.local/bin:$PATH\" && cd /YOUR/PATH/TO/mcp-server-naver-search && uv run --with 'mcp[cli]' --with httpx --with python-dotenv python server.py"
      ],
      "env": {
        "NAVER_CLIENT_ID": "YOUR_ID",
        "NAVER_CLIENT_SECRET": "YOUR_SECRET"
      }
    }
  }
}
```

> **Note:** Claude Code requires `sh -c` with PATH export because it doesn't inherit your shell's PATH configuration.

</details>

<details>
<summary><b>Cursor</b></summary>

Add this to your Cursor MCP settings:

```json
{
  "mcpServers": {
    "naver-search": {
      "command": "uv",
      "args": [
        "run",
        "--with", "mcp[cli]",
        "--with", "httpx",
        "--with", "python-dotenv",
        "/YOUR/PATH/TO/mcp-server-naver-search/server.py"
      ],
      "env": {
        "NAVER_CLIENT_ID": "YOUR_ID",
        "NAVER_CLIENT_SECRET": "YOUR_SECRET"
      }
    }
  }
}
```

</details>

## Usage Examples (Try these!)

After restarting Claude, ask:

### 1. Shopping - Find Lowest Price
```
"맥북 프로 M4 14인치 네이버 쇼핑 최저가 알려줘. 판매처랑 가격 비교해줘."
("Find the lowest price for MacBook Pro M4 on Naver Shopping.")
```

### 2. Cafe - Real Community Reviews
```
"서울 성수동 데이트 코스 추천해줘. 네이버 카페 글 위주로 찾아줘."
("Recommend date spots in Seongsu-dong using Naver Cafe posts.")
```

### 3. News - Breaking News
```
"오늘 삼성전자 주가 관련 뉴스 5개만 요약해줘."
("Summarize 5 latest news articles about Samsung Electronics stock.")
```

## License

MIT License © 2026 [uju777](https://github.com/uju777)

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Contributing

Issues and Pull Requests are welcome!

## Author

**uju777** - [GitHub](https://github.com/uju777)
