# AI News Blog

매일 자동으로 AI 서비스 관련 뉴스를 수집하여 발행하는 Jekyll 블로그입니다.

## 테마

이 블로그는 [Lanyon](https://github.com/poole/lanyon) 테마를 사용합니다.

## 설정

### 1. 로컬 개발 환경 설정

```bash
# 의존성 설치
bundle install

# 로컬 서버 실행
bundle exec jekyll serve
```

브라우저에서 `http://localhost:4000`으로 접속하여 확인할 수 있습니다.

### 2. GitHub Actions 설정

#### OpenAI API 키 설정

1. GitHub 리포지토리로 이동
2. Settings > Secrets and variables > Actions 클릭
3. "New repository secret" 클릭
4. Name: `OPENAI_API_KEY`
5. Value: OpenAI API 키 입력
6. "Add secret" 클릭

#### 자동 뉴스 발행

GitHub Actions가 매일 서울시간 오전 9시(UTC 00:00)에 자동으로 실행됩니다.

수동으로 실행하려면:
1. Actions 탭으로 이동
2. "Daily AI News Publish" 워크플로우 선택
3. "Run workflow" 클릭

## 프로젝트 구조

```
.
├── _config.yml          # Jekyll 설정
├── _layouts/            # 레이아웃 템플릿
├── _posts/              # 블로그 포스트 (자동 생성됨)
├── css/                 # 스타일시트
├── js/                  # JavaScript 파일
├── generate_news.py     # 뉴스 생성 스크립트
└── .github/
    └── workflows/
        └── daily-news.yml  # GitHub Actions 워크플로우
```

## 라이선스

MIT License

