const axios = require('axios');

// Notion API 토큰
const notionToken = 'secret_Ar4jiLvCbf1pJzNfb4KYs6hK5HfXFFnUqT26TSIw2dY';

// 페이지의 ID (본인의 페이지 ID로 교체)
const pageId = '8c9d9a905a074adf8397951fd399a459';

// const notionApiUrl = `https://api.notion.com/v1/pages/${pageId}/children`;
// 으로 엔드포인트를 잡으면 400 상태 코드가 발생
const notionApiUrl = `https://api.notion.com/v1/pages/${pageId}`;

// HTTP 요청 헤더 설정
const headers = {
  'Authorization': `Bearer ${notionToken}`,
  'Notion-Version': '2021-08-16',  // 사용할 Notion API 버전
};

// Notion API에 GET 요청 보내기
axios.get(notionApiUrl, { headers })
  .then(response => {
    // 응답 데이터 처리
    const responseData = response.data;

    // 페이지의 하위 블록들 추출
    const childrenBlocks = responseData.results;

    // 각 블록을 순회하면서 내용을 출력 또는 필요한 작업 수행
    // 순회를 위해서 데이터가 있어야 하는데 undefined 상태
    // 즉 데이터가 없다.
    childrenBlocks.forEach(block => {
      // 각 블록에 대한 처리
      console.log('블록 내용:', block);
    });
  })
  .catch(error => {
    // 에러 처리
    console.error('Notion API 요청 중 오류:', error.message);
  });
