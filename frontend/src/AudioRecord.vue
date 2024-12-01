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
        audioBlob: null, //audio recorded during conversation
        transcription: "",
        processing: false,
        mediaRecorder: null,
        chunks: [],
      };
    },
    
    methods: {
      async startRecording() {
        console.log("test start recording")
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
      async processAudio() {
        this.processing = true;
  
        const audioBlob = new Blob(this.chunks, { type: "audio/wav" });
        console.log("audio blob", audioBlob);

        const formData = new FormData();

        formData.append("audio_file", audioBlob); //problematic code, cannot append audio file to form data
        
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