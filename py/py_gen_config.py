import os
import json
from datetime import datetime

BASE_URL = "https://raw.githubusercontent.com/ssmhdssmhd/pg/main"
CDN_URL = "https://cdn.jsdelivr.net/gh/ssmhdssmhd/pg"
GHP_URL = "https://ghp.ci/" + BASE_URL

CONFIG = {
    "version": "1.0.0",
    "update_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "description": "PG 影视配置源 - AI自动更新",
    "sources": {
        "jsm": {
            "name": "点播源配置",
            "description": "jsm.json 包含所有影视点播源",
            "urls": {
                "github": f"{BASE_URL}/jsm.json",
                "jsdelivr": f"{CDN_URL}/jsm.json",
                "ghpci": f"{GHP_URL}/jsm.json",
            }
        },
        "live_cn": {
            "name": "国内直播",
            "description": "国内直播源（央视、卫视、地方台等）",
            "urls": {
                "github": f"{BASE_URL}/ai_output/国内直播.txt",
                "jsdelivr": f"{CDN_URL}/ai_output/国内直播.txt",
                "ghpci": f"{GHP_URL}/ai_output/国内直播.txt",
            }
        },
        "live_world": {
            "name": "国外直播",
            "description": "国外直播源（全球各国电视台）",
            "urls": {
                "github": f"{BASE_URL}/ai_output/国外直播.txt",
                "jsdelivr": f"{CDN_URL}/ai_output/国外直播.txt",
                "ghpci": f"{GHP_URL}/ai_output/国外直播.txt",
            }
        },
        "live_m3u": {
            "name": "直播源 M3U",
            "description": "标准 M3U 格式直播源",
            "urls": {
                "github": f"{BASE_URL}/live.m3u",
                "jsdelivr": f"{CDN_URL}/live.m3u",
                "ghpci": f"{GHP_URL}/live.m3u",
            }
        },
        "live_lite_m3u": {
            "name": "精简直播源 M3U",
            "description": "精简版 M3U 格式直播源",
            "urls": {
                "github": f"{BASE_URL}/live_lite.m3u",
                "jsdelivr": f"{CDN_URL}/live_lite.m3u",
                "ghpci": f"{GHP_URL}/live_lite.m3u",
            }
        },
        "live_txt": {
            "name": "直播源 TXT",
            "description": "标准 TXT 格式直播源",
            "urls": {
                "github": f"{BASE_URL}/live.txt",
                "jsdelivr": f"{CDN_URL}/live.txt",
                "ghpci": f"{GHP_URL}/live.txt",
            }
        },
    },
    "guide": {
        "ok_ys": {
            "name": "OK影视 / 影视仓",
            "description": "在配置中添加以下链接",
            "steps": [
                "打开 OK影视 / 影视仓 APP",
                "进入设置 -> 配置管理",
                "点击添加配置",
                "输入名称: PG影视配置",
                "输入地址: https://cdn.jsdelivr.net/gh/ssmhdssmhd/pg/jsm.json",
                "保存并使用",
            ]
        },
        "tvbox": {
            "name": "TVBox",
            "description": "在设置中添加以下配置链接",
            "steps": [
                "打开 TVBox APP",
                "点击菜单 -> 设置 -> 配置地址",
                "输入: https://cdn.jsdelivr.net/gh/ssmhdssmhd/pg/jsm.json",
                "确定并重启 APP",
            ]
        },
        "iptv": {
            "name": "IPTV 播放器",
            "description": "添加直播源链接",
            "steps": [
                "打开 IPTV 播放器",
                "添加直播源",
                "输入: https://cdn.jsdelivr.net/gh/ssmhdssmhd/pg/ai_output/国内直播.txt",
                "保存并刷新列表",
            ]
        }
    },
    "tips": {
        "国内用户推荐": "优先使用 jsdelivr 或 ghp.ci 加速链接",
        "更新频率": "每周一、周四自动更新",
        "AI资源站": "jsm.json 中以 AI_ 开头的资源站是 AI 自动探测的",
    }
}

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'ai_output')
os.makedirs(OUTPUT_DIR, exist_ok=True)

output_file = os.path.join(OUTPUT_DIR, 'config.json')
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(CONFIG, f, ensure_ascii=False, indent=2)

print(f"配置文件已生成: {output_file}")
print()
print("=" * 60)
print("📺 影视APP配置链接")
print("=" * 60)
print()
print("🎯 主配置（点播源）- 推荐国内用户使用 jsdelivr:")
print(f"   jsdelivr: {CONFIG['sources']['jsm']['urls']['jsdelivr']}")
print(f"   github:   {CONFIG['sources']['jsm']['urls']['github']}")
print(f"   ghp.ci:   {CONFIG['sources']['jsm']['urls']['ghpci']}")
print()
print("📺 国内直播源:")
print(f"   {CONFIG['sources']['live_cn']['urls']['jsdelivr']}")
print()
print("🌍 国外直播源:")
print(f"   {CONFIG['sources']['live_world']['urls']['jsdelivr']}")
print()
print("=" * 60)
print("📋 使用方法")
print("=" * 60)
print("1. OK影视 / 影视仓:")
print("   设置 -> 配置管理 -> 添加配置")
print("   地址: https://cdn.jsdelivr.net/gh/ssmhdssmhd/pg/jsm.json")
print()
print("2. TVBox:")
print("   设置 -> 配置地址")
print("   地址: https://cdn.jsdelivr.net/gh/ssmhdssmhd/pg/jsm.json")
print()
print("3. IPTV播放器:")
print("   添加直播源")
print("   地址: https://cdn.jsdelivr.net/gh/ssmhdssmhd/pg/ai_output/国内直播.txt")
