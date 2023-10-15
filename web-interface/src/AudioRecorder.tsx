/*
  Referenced from the following GitHub repository:
  - https://github.com/samhirtarif/react-audio-visualize
  - https://stackblitz.com/edit/stackblitz-starters-kjpu5q?file=src%2FApp.tsx
*/
import { error } from 'console';
import * as React from 'react';
import { useState } from 'react';
import { AudioVisualizer, LiveAudioVisualizer } from 'react-audio-visualize';
import { AudioRecorder, useAudioRecorder } from 'react-audio-voice-recorder';

export default function AudioInputAndDisplay() {
  const [blob, setBlob] = useState<Blob>();
  const recorder = useAudioRecorder(
    {
      noiseSuppression: true,
      echoCancellation: true,
    },
    (error) => console.table(error) // onNotAllowedOrFound
  );

  const addAudioElement = (blob: Blob) => {
    const url = URL.createObjectURL(blob);
    const audio = document.createElement('audio');
    audio.src = url;
    audio.controls = true;
    document.body.appendChild(audio);
  }

  return (
    <div>
      <AudioRecorder
        onRecordingComplete={setBlob}
        recorderControls={recorder}
      />

      {recorder.mediaRecorder && (
        <LiveAudioVisualizer
          mediaRecorder={recorder.mediaRecorder}
          width={200}
          height={75}
          barWidth={3}
          gap={2}
          barColor={'#4b2e83'}
        />
      )}

      {blob && (
        <AudioVisualizer
          blob={blob}
          width={500}
          height={75}
          barWidth={3}
          gap={2}
          barColor={'#4b2e83'}
        />
      )}

      <button onClick={() => addAudioElement(blob)}>Add Audio Element</button>

    </div>
  );
}
