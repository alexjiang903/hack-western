<template>
  <div class="audio-recorder">
    <button @click="startRecording" :disabled="isRecording">Start Recording</button>
    <button @click="stopRecording" :disabled="!isRecording">Stop Recording</button>
    <p v-if="transcription">Transcription: {{ transcription }}</p>
    <p v-if="processing">Processing...</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      isRecording: false,
      audioBlob: null, // audio recorded during conversation
      transcription: "",
      processing: false,
      mediaRecorder: null,
      chunks: [],
    };
  },

  methods: {
    async startRecording() {
      console.log("test start recording");
      if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia) {
        alert("Your browser does not support audio recording.");
        return;
      }

      this.isRecording = true;
      this.transcription = "";
      this.chunks = [];

      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      this.mediaRecorder = new MediaRecorder(stream);

      this.mediaRecorder.ondataavailable = (event) => {
        if (event.data.size > 0) this.chunks.push(event.data);
      };

      this.mediaRecorder.onstop = this.processAudio;
      this.mediaRecorder.start();
    },

    mounted() {
      console.log("audio recorder mounted");
    },

    stopRecording() {
      this.isRecording = false;
      if (this.mediaRecorder) this.mediaRecorder.stop();
    },

    // Corrected async function definition
    // async sendToWhisperAPI(audioBlob) {
    //   const formData = new FormData();
    //   formData.append('audio_file', audioBlob, 'audio.mp3');

    //   const startTime = performance.now();

    //   const response = await fetch("http://localhost:9000/asr", {
    //     method: 'POST',
    //     headers: {
    //       Accept: 'application/json',
    //     },
    //     body: formData,
    //   });

    //   const endTime = performance.now();
    //   const elapsedTime = ((endTime - startTime) / 1000).toFixed(2);

    //   if (response.ok) {
    //     const data = await response.json();
    //     return { text: data.text, elapsedTime };
    //   } else {
    //     console.error('Error sending audio to Whisper API:', response);
    //     alert('Failed to send audio to Whisper API.');
    //     return 'Error: Failed to convert speech to text.';
    //   }
    // },

    async processAudio() {
      this.processing = true;

      const audioBlob = new Blob(this.chunks, { type: "audio/wav" });
      console.log("audio blob", audioBlob);
      // const { text, elapsedTime } = await this.sendToWhisperAPI(audioBlob);
      // console.log(text);

      const formData = new FormData();
      const audioFile = new File([audioBlob], "audio.wav", { type: "audio/wav" });
      formData.append("audio_file", audioFile);

      try {
        const response = await axios.post("http://localhost:9000/asr", formData, {
          headers: { "Content-Type": "multipart/form-data" },
        });

        this.transcription = response.data.text;
      } catch (error) {
        console.error("Error transcribing audio:", error);
        alert("Failed to process audio. Please try again.");
      } finally {
        this.processing = false;
      }
    },
  },
};
</script>

<style scoped>
.audio-recorder {
  text-align: center;
}
</style>
