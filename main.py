import feedparser

# 1. 你要抓取的“情报源”列表
RSS_SOURCES = [
    ("AI新品 (Product Hunt)", "https://rsshub.app/producthunt/daily"),
    ("GitHub 热门AI项目", "https://rsshub.app/github/trending/daily?language=python"),
    ("Hacker News AI讨论", "https://rsshub.app/hackernews/frontpage"),
    ("AI新闻聚合", "https://www.artificialintelligence-news.com/feed/")
]

def get_news():
    all_content = ""
    for name, url in RSS_SOURCES:
        all_content += f"\n--- {name} ---\n"
        feed = feedparser.parse(url)
        # 每个源只取前 5 条，免得太长
        for entry in feed.entries[:5]:
            all_content += f"标题: {entry.title}\n链接: {entry.link}\n摘要: {entry.get('summary', '无')[:100]}...\n\n"
    return all_content

# 2. 组装成你要的“超级提示词 (Prompt)”
prompt_template = f"""
你是AI商业分析专家，请基于以下【原始情报】输出一份《AI赚钱日报》：

目标用户：希望找赚钱机会的大学生。
输出要求：
1. 今日AI趋势（用大白话讲）
2. AI新工具/产品（挑3个最火的）
3. 赚钱机会（重点：普通人怎么用它变现？）
4. 关键技术点（简单科普）

---
【原始情报开始】
{get_news()}
【原始情报结束】
"""

print(prompt_template)
