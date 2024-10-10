import { DisplayOptions } from "@nlux/react";
import merge from 'lodash/merge';

const displayOptions: DisplayOptions = {
  height: 600,
  width: 400,
  colorScheme: "light",
};
export const defaultOptions = {
  personaOptions: {
    assistant: {
      name: '你好，我是你的 AI 助手',
      avatar: 'https://img.alicdn.com/imgextra/i2/O1CN01Pda9nq1YDV0mnZ31H_!!6000000003025-54-tps-120-120.apng',
      tagline: '您可以尝试点击下方的快捷入口开启体验！',
    },
    user: {
      name: 'You',
      avatar: 'https://img.alicdn.com/tfs/TB1YeRbaSRRMKJjy0FlXXXFepXa-166-166.png',
    }
  },
  displayOptions,
  composerOptions: {
    placeholder: '请输入您的问题，使用 Shift + Enter 换行。',
    hideStopButton: true
  }
};

export const getChatOptions = () => {
  return merge({}, defaultOptions, window.CHATBOT_CONFIG.aiChatOptions || window.CHATBOT_CONFIG.options);
};
