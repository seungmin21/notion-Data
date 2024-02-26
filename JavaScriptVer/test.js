const axios = require('axios');

// Notion API 토큰
const notionToken = 'secret_Ar4jiLvCbf1pJzNfb4KYs6hK5HfXFFnUqT26TSIw2dY';

// Notion 페이지 URL (또는 페이지 ID)
const notionPageUrl = '8c9d9a905a074adf8397951fd399a459';

// Notion API 엔드포인트 URL 생성
const notionPageApiUrl = `https://api.notion.com/v1/pages/${notionPageUrl}`;

// HTTP 요청 헤더 설정
const headers = {
  'Authorization': `Bearer ${notionToken}`,
  'Notion-Version': '2021-08-16',  // 사용할 Notion API 버전
};

// Notion API에 GET 요청 보내기 (페이지의 블록 가져오기)
axios.get(notionPageApiUrl, { headers })
  .then(response => {
    // 응답 데이터 처리
    const data = response.data;
    console.log('Notion API 응답 데이터:', data);
  })
  .catch(error => {
    // 에러 처리
    console.error("Notion API 요청 오류")
  });