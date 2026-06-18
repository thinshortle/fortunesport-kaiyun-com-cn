def read_site_data():
    return [
        {
            "url": "https://fortunesport-kaiyun.com.cn",
            "keyword": "开云开运体育",
            "tags": ["体育", "娱乐", "赛事"],
            "description": "提供全天候体育赛事资讯与互动体验的专业平台"
        },
        {
            "url": "https://fortunesport-kaiyun.com.cn/about",
            "keyword": "开云开运体育",
            "tags": ["介绍", "品牌"],
            "description": "了解开云开运体育的品牌背景与发展历程"
        },
        {
            "url": "https://fortunesport-kaiyun.com.cn/events",
            "keyword": "开云开运体育",
            "tags": ["活动", "促销", "会员"],
            "description": "定期推出会员专属活动和限时优惠，提升参与感"
        }
    ]


def extract_summary(entry):
    return {
        "url": entry["url"],
        "keyword": entry["keyword"],
        "tags": ", ".join(entry["tags"]),
        "description": entry["description"]
    }


def format_summary_line(entry):
    line = f"关键词：{entry['keyword']}\n"
    line += f"URL：{entry['url']}\n"
    line += f"标签：{entry['tags']}\n"
    line += f"说明：{entry['description']}\n"
    line += "---"
    return line


def generate_structured_summary(site_list):
    summary_parts = []
    for item in site_list:
        parsed = extract_summary(item)
        block = format_summary_line(parsed)
        summary_parts.append(block)
    return "\n\n".join(summary_parts)


def print_summary_to_console(summary_text):
    print("站点资料摘要（结构化）")
    print("=" * 40)
    print(summary_text)
    print("=" * 40)


def main():
    site_data = read_site_data()
    if not site_data:
        print("没有可用站点数据。")
        return

    summary = generate_structured_summary(site_data)
    print_summary_to_console(summary)


if __name__ == "__main__":
    main()