const { Client } = require('@notionhq/client');

const notion = new Client({ auth: process.env.NOTION_API_KEY });

(async () => {
  const blockId = '8c9d9a90-5a07-4adf-8397-951fd399a459';
  const response = await notion.blocks.children.list({
    block_id: blockId,
    page_size: 50,
  });
  console.log(response);
})();