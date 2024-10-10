# 在网站中添加一个大模型 AI 助手 - 前端组件代码
此项目是阿里云教程文档 [10分钟在网站上增加一个 AI 助手](https://help.aliyun.com/zh/model-studio/developer-reference/add-an-ai-assistant-to-your-website-in-10-minutes) 中的 AI 助手前端组件代码。


## 如何运行
运行：
```bash
cd web-chatbot-ui
npm install
npm run dev
```

## 如何构建出 index.js 和 index.css
运行：
```bash
cd web-chatbot-ui
npm install
npm run build
```

## 代码结构
```bash
├── component
│   ├── Chatbot.module.css
│   ├── Chatbot.tsx                   # AI 助手组件
│   ├── ChatbotContainer.module.css
│   ├── ChatbotContainer.tsx          # AI 助手的容器及网站右下角唤起 AI 助手的图标
│   └── send.ts                       # 与函数计算中的 /chat 接口交互获取大模型生成数据的关键代码。
├── config
│   └── chatOptions.ts                # AI 助手的配置项，包括图标、欢迎信息，以及重写 render 等。这些 options 会被透传给 AiChat 组件，更多完整的参数可以查阅 NLUX 官方文档：https://docs.nlkit.com/nlux/reference/ui/ai-chat
├── index.css                         # AI 助手样式，这里我们覆盖了 NLUX 默认的样式，改成了类似阿里云官网 AI 助手的样式
├── main.tsx
├── types.d.ts
└── vite-env.d.ts
```

## 自定义建议
### 补充功能
- 如果你希望为 AI 助手的回复信息后增加点赞、点踩、重新生成按钮，可以在 chatOptions 中增加 `messageOptions.responseRenderer` 来[自定义回复消息样式](https://docs.nlkit.com/nlux/reference/ui/ai-chat#message-options)。
- 如果你希望支持历史对话查看，可以在 `ChatbotContainer` 中的 `onClickRefresh` 中增加历史对话保存逻辑，然后再 `ChatbotContainer` 增加功能入口和相关界面来展示历史对话。
### 调整样式
- 如果你希望让 AI 助手的样式更符合你的网站风格，可以调整 `index.css`、`src/component/Chatbot.module.css` 的样式。也可以进一步参考 [NLUX 文档](https://docs.nlkit.com/nlux/reference/ui/ai-chat#message-options) 做更多定制开发。
