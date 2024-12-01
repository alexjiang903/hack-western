<template>
  <div id="app">
    <button @click="callApi">Call API</button>
    <p>{{ result }}</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      result: ''
    };
  },
  methods: {
    async callApi() {
      try {
        const response = await axios.get('http://127.0.0.1:5000/api/vfFunction');
        this.result = response.data.result;  // Store the result in a data property
      } catch (error) {
        console.error("There was an error calling the API", error);
      }
    }
  }
};
</script>

<style>
/* Your styles here */
</style>
