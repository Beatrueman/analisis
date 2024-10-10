interface ChatbotConfig {
  /**
  * Chat 接口地址
  */
  endpoint: string;
  /**
   * 是否默认显示聊天框
   */
  displayByDefault: boolean;
  /**
   * AiChat 组件的配置，详细参考：https://docs.nlkit.com/nlux/reference/ui/ai-chat
   */
  aiChatOptions: object;
  /**
   * @deprecated
   * AiChat 组件的配置。现在建议使用 aiChatOptions 字段来替代 options 字段。
   */
  options: object;

  /**
   * 数据处理器，用于调整数据发送和处理逻辑
   */
  dataProcessor: {
    /**
     * 在向后端大模型应用发起请求前改写 Prompt。
     * 可以用于总结网页场景，在发送前将网页内容包含在内，同时避免在前端显示这些内容。
     */
    rewritePrompt: (prompt: string) => string;

    /**
     * 在接收到大模型应用返回的数据后，对数据进行解析。
     * 可以用于去除大模型应用返回的数据中的 HTML 标签，避免在前端显示这些标签。
     */
    processChunk: (chunk: string) => [string, string];
  };
}
interface Window {
  CHATBOT_CONFIG: ChatbotConfig;
}
