#!/usr/bin/env python3
"""
뉴스 생성 스크립트
OpenAI API를 사용하여 AI 관련 뉴스를 생성하고 Jekyll 포스트로 저장합니다.
"""

import os
import sys
import datetime
from pathlib import Path
from openai import OpenAI

def load_prompt_template(date_string):
    """프롬프트 템플릿 파일을 읽어서 날짜를 채워넣습니다."""
    script_dir = Path(__file__).parent
    template_path = script_dir / "prompt_template.md"
    
    try:
        with open(template_path, 'r', encoding='utf-8') as f:
            template = f.read()
        return template.format(date_string=date_string)
    except FileNotFoundError:
        print(f"Error: 프롬프트 템플릿 파일을 찾을 수 없습니다: {template_path}")
        sys.exit(1)

def generate_news():
    """AI 뉴스를 생성하고 Jekyll 포스트 파일로 저장합니다."""
    
    # OpenAI API 키 확인
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("Error: OPENAI_API_KEY 환경 변수가 설정되지 않았습니다.")
        sys.exit(1)
    
    client = OpenAI(api_key=api_key)
    
    # 현재 날짜 및 시간
    now = datetime.datetime.now()
    date_string = now.strftime("%Y-%m-%d")
    datetime_string = now.strftime("%Y-%m-%d-%H%M%S")
    time_string = now.strftime("%H:%M:%S")
    year_month = now.strftime("%Y%m")  # 년월 형식 (예: 202511)
    
    # 프롬프트 템플릿 로드
    prompt = load_prompt_template(date_string)
    
    try:
        # OpenAI API 호출
        response = client.responses.create(
            model="gpt-5",
            tools=[{"type": "web_search"}],
            input=prompt,
        )

        blog_content = response.output_text
        
        # 프로젝트 루트 디렉토리 찾기 (scripts 폴더의 상위 디렉토리)
        script_dir = Path(__file__).parent
        project_root = script_dir.parent
        
        # Jekyll 포스트 기본 디렉토리
        posts_dir = project_root / "_posts"
        posts_dir.mkdir(exist_ok=True)
        
        # 년월 기준 하위 디렉토리 생성
        year_month_dir = posts_dir / year_month
        year_month_dir.mkdir(exist_ok=True)
        
        # 파일명 형식: YYYY-MM-DD-HH24MISS-ai-news.md
        post_filename = year_month_dir / f"{datetime_string}-ai-news.md"
        
        # Jekyll 포스트 프론트매터 추가
        frontmatter = f"""---
layout: post
title: "{date_string} AI 뉴스"
date: {date_string} {time_string} +0900
categories: news
---

"""
        
        with open(post_filename, 'w', encoding='utf-8') as post_file:
            post_file.write(frontmatter + blog_content)
        
        print(f"뉴스 포스트가 생성되었습니다: {post_filename}")
        return str(post_filename)
        
    except Exception as e:
        print(f"Error: 뉴스 생성 중 오류가 발생했습니다: {e}")
        sys.exit(1)

if __name__ == "__main__":
    generate_news()