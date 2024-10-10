import { AiChat, useAiChatApi, useAsStreamAdapter } from '@nlux/react';
import { createSend } from './send';
import { getChatOptions } from '../config/chatOptions';
import '@nlux/themes/nova.css';
import styles from './Chatbot.module.css'
import { forwardRef, useImperativeHandle, useState } from 'react';
import { stopIcon } from './icon/svgIcons';

export interface ChatbotInterface {
  resetConversation: () => void;
}

const App = forwardRef((_, ref) => {

  const options = getChatOptions();

  const api = useAiChatApi();
  const [isButtonVisible, setButtonVisible] = useState(false)

  const [send, stopGenerating] = createSend(setButtonVisible);
  const adapter = useAsStreamAdapter(send, []);
  const onClickStop = () => {
    stopGenerating();
  };

  useImperativeHandle(ref, () => ({
    resetConversation: () => {
      stopGenerating();
      api.conversation.reset();
      api.composer.cancel();
    },
  }));


  return (
    <>
      <AiChat api={api} adapter={adapter} {...options}>
      </AiChat>
      { isButtonVisible && <div className={styles.stopButton}>
          <button onClick={onClickStop}>{stopIcon}</button>
        </div>
      }
    </>
  )
});

export default App
