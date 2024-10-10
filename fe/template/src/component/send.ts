import { StreamSend, StreamingAdapterObserver } from '@nlux/react';
import { SetStateAction } from 'react';

sessionStorage.removeItem('chatSessionId');
type StopFunction = () => void;
let reader: ReadableStreamDefaultReader<Uint8Array>;

function defaultProcessChunk(chunks: string) {
    let result = '';
    let sessionId = null;
    chunks.split("\nid").forEach(chunk => {
      let data: any = chunk.split('HTTP_STATUS/200\ndata:')[1];
      try {
        data = JSON.parse(data);
        sessionId = data.output.session_id;
        result += data.output.text || '';
      } catch (e) {
        throw(e);
      }
    });
    return [result, sessionId];
}
export const createSend = function(setStopFunctionVisible: { (value: SetStateAction<boolean>): void }): [StreamSend, StopFunction] {
    const stopGenerating: StopFunction = () => {
        reader && reader.cancel();
    };

    return [async (
        prompt: string,
        observer: StreamingAdapterObserver,
    ) => {
        // 插件扩展点 - 在发送请求前重写 prompt。
        if (window.CHATBOT_CONFIG.dataProcessor?.rewritePrompt) {
            prompt = window.CHATBOT_CONFIG.dataProcessor.rewritePrompt(prompt);
        }
        const body = {
            sessionId: sessionStorage.getItem('chatSessionId'),
            prompt
        };
        const response = await fetch(window.CHATBOT_CONFIG.endpoint, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(body),
        });

        if (response.status !== 200) {
            observer.error(new Error('Failed to connect to the server'));
            return;
        }

        if (!response.body) {
            return;
        }

        // Read a stream of server-sent events
        // and feed them to the observer as they are being generated
        reader = response.body.getReader();
        const textDecoder = new TextDecoder();
        while (true) {
            const {value, done} = await reader.read();
            if (!done) {
                setStopFunctionVisible(true);
            }
            if (done) {
                break;
            }

            const content = textDecoder.decode(value);
            if (content) {
                const processChunk = window.CHATBOT_CONFIG.dataProcessor?.processChunk || defaultProcessChunk;
                try {
                    const [text, sessionId] = processChunk(content);
                    sessionStorage.setItem('chatSessionId', sessionId);
                    text && observer.next(text);
                } catch (e) {
                    console.warn('Parse content failed: ' + content, e);
                    observer.error(new Error('Parse content failed'));
                }
            }
        }
        setStopFunctionVisible(false);
        observer.complete();
    }, stopGenerating];
}
