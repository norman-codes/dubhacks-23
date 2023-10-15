import * as React from 'react';
import { useState } from 'react';
import { AudioVisualizer, LiveAudioVisualizer } from 'react-audio-visualize';
import { AudioRecorder, useAudioRecorder } from 'react-audio-voice-recorder';
import { ref, uploadBytes } from 'firebase/storage';
import { storage } from './firebase';  // Ensure firebase.js is in the same directory and properly configured

export default function AudioInputAndDisplay() {
  const [blob, setBlob] = useState<Blob | null>(null);
  const recorder = useAudioRecorder(
    {
      noiseSuppression: true,
      echoCancellation: true,
    },
    (error) => console.table(error) // onNotAllowedOrFound
  );

  const addAudioElement = (blob: Blob | null) => {
    if (blob) {
      const url = URL.createObjectURL(blob);
      const audio = document.createElement('audio');
      audio.src = url;
      audio.controls = true;
      document.body.appendChild(audio);
    }
  }

  const saveAudio = (blob: Blob | null) => {
    if (blob) {
      // Get the current date and time
      const now = new Date();
  
      // Format the date and time components so that they have leading zeros if necessary
      const year = now.getFullYear();
      const month = String(now.getMonth() + 1).padStart(2, '0');  // Months are 0-based, so add 1
      const day = String(now.getDate()).padStart(2, '0');
      const hour = String(now.getHours()).padStart(2, '0');
      const minute = String(now.getMinutes()).padStart(2, '0');
      const second = String(now.getSeconds()).padStart(2, '0');
  
      // Combine the date and time components to form the file name
      const fileName = `${month}${day}${year}${hour}${minute}${second}.wav`;
  
      // Create a reference to the file in Firebase Cloud Storage
      const audioRef = ref(storage, `audio/${fileName}`);
  
      // Upload the blob
      uploadBytes(audioRef, blob).then((snapshot) => {
        console.log('Uploaded a blob or file!');
      });
    }
  };
  

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
        <React.Fragment>
        <AudioVisualizer
          blob={blob}
          width={500}
          height={75}
          barWidth={3}
          gap={2}
          barColor={'#4b2e83'}
        />
        <button onClick={() => addAudioElement(blob)}>Add Audio Element</button>
        <button onClick={() => saveAudio(blob)}>Save Audio</button>
        </React.Fragment>
      )}
    </div>
  );
}
