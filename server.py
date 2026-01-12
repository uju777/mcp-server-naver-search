import os
import httpx
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

NAVER_CLIENT_ID = os.getenv("NAVER_CLIENT_ID")
NAVER_CLIENT_SECRET = os.getenv("NAVER_CLIENT_SECRET")

if not NAVER_CLIENT_ID or not NAVER_CLIENT_SECRET:
    raise ValueError("Error: .env 파일에 NAVER_CLIENT_ID와 NAVER_CLIENT_SECRET을 설정해주세요.")

mcp = FastMCP("Naver Search")

@mcp.tool()
async def search_naver(query: str, category: str = "blog", display: int = 5) -> str:
    """
    네이버 검색 API를 사용하여 한국 현지 정보를 검색합니다.

    Args:
        query (str): 검색어 (예: "맥북프로 M4 최저가", "삼성전자 주가 뉴스")
        category (str): 검색 카테고리
            - "shop": 쇼핑 최저가 검색 (★인기 기능)
            - "cafe": 네이버 카페 글 검색 (★찐 후기)
            - "news": 실시간 뉴스 기사
            - "blog": 블로그 리뷰
            - "local": 맛집, 장소 전화번호
        display (int): 가져올 결과 개수 (기본 5개)
    """

    base_url = "https://openapi.naver.com/v1/search"
    endpoints = {
        "shop": f"{base_url}/shop.json",
        "cafe": f"{base_url}/cafearticle.json",
        "news": f"{base_url}/news.json",
        "blog": f"{base_url}/blog.json",
        "local": f"{base_url}/local.json"
    }

    url = endpoints.get(category, endpoints["blog"])

    headers = {
        "X-Naver-Client-Id": NAVER_CLIENT_ID,
        "X-Naver-Client-Secret": NAVER_CLIENT_SECRET
    }

    params = {
        "query": query,
        "display": display,
        "sort": "sim"
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            items = data.get('items', [])

            if not items:
                return "검색 결과가 없습니다."

            formatted_results = []

            for idx, item in enumerate(items, 1):
                title = item.get('title', '').replace('<b>', '').replace('</b>', '')

                if category == "shop":
                    # 쇼핑: 가격과 브랜드 정보 강조
                    lprice = item.get('lprice', '0')
                    mall = item.get('mallName', '')
                    brand = item.get('brand', '')
                    link = item.get('link', '')
                    formatted_results.append(
                        f"### {idx}. {title}\n"
                        f"- **가격**: {int(lprice):,}원\n"
                        f"- **판매처**: {mall}\n"
                        f"- **브랜드**: {brand}\n"
                        f"- **링크**: {link}\n"
                    )
                elif category == "cafe":
                    # 카페: 카페 이름과 글 내용 강조
                    desc = item.get('description', '').replace('<b>', '').replace('</b>', '')
                    cafename = item.get('cafename', '')
                    link = item.get('link', '')
                    formatted_results.append(
                        f"### {idx}. {title}\n"
                        f"- **출처**: {cafename} (네이버 카페)\n"
                        f"- **요약**: {desc}\n"
                        f"- **링크**: {link}\n"
                    )
                else:
                    # 뉴스/블로그/지역
                    desc = item.get('description', '').replace('<b>', '').replace('</b>', '')
                    link = item.get('link', '')
                    if category == "local":
                        addr = item.get('roadAddress', '')
                        formatted_results.append(f"### {idx}. {title}\n- 주소: {addr}\n- 링크: {link}")
                    else:
                        formatted_results.append(f"### {idx}. {title}\n- 내용: {desc}\n- 링크: {link}")

            return "\n".join(formatted_results)

        except Exception as e:
            return f"오류 발생: {str(e)}"

if __name__ == "__main__":
    mcp.run()
